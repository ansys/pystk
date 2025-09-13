# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from __future__ import annotations

import grpc
import logging
import re
import typing
from enum import IntEnum, IntFlag
from concurrent.futures import ThreadPoolExecutor
from queue import SimpleQueue

from . import AgGrpcServices_pb2
from . import AgGrpcServices_pb2_grpc

from .marshall import EnumArg, OLEColorArg
from .apiutil import OutArg, GcDisabler, error_msg_from_hresult
from ..utilities.colors import Color

# comutil.GUID.from_registry_format("{00020404-0000-0000-C000-000000000046}").as_data_pair()
IID_IEnumVARIANT = (132100, 5044031582654955712)

_logger = logging.getLogger("stk.internal.grpcutil")

def _is_list_type(arg:typing.Any) -> bool:
    if type(arg) == str \
        or isinstance(arg, IntFlag) \
        or not hasattr(arg, '__iter__'):
        return False
    return True

def _array_num_columns(arg:typing.Any) -> int:
    if not _is_list_type(arg):
        return 0
    if len(arg) == 0:
        # Empty list
        return 1
    if not _is_list_type(arg[0]):
        return 1
    return len(arg)

def _input_arg_to_single_dim_list(arg:typing.Any) -> list:
    if not _is_list_type(arg):
        return [arg]
    else:
        num_cols = _array_num_columns(arg)
        if num_cols == 1:
            return list(arg)
        else:
            ret = list()
            col_length = len(arg[0])
            for j in range(num_cols):
                if len(arg[j]) > 0 and _is_list_type(arg[j][0]):
                    raise RuntimeError("Arrays with dimension > 2 are not supported argument types.")
                if len(arg[j]) != col_length:
                    raise RuntimeError(f"Malformed array argument. len(array[{j}]) != len(array[0]).")
                ret += arg[j]
            return ret

def _grpc_post_process_return_vals(return_vals, marshallers, *input_args):
    """
    Enums come back from gRPC as ints; marshall them to class type.
    """
    if return_vals is None:
        return
    multiple_returns = True if type(return_vals) == tuple else False
    ret_val_iter = 0
    temp_return_list = []
    for input_arg, marshaller in zip(input_args, marshallers):
        if type(input_arg) == OutArg:
            return_val = return_vals[ret_val_iter] if multiple_returns else return_vals
            ret_val_iter += 1
            if type(marshaller)==EnumArg:
                temp_return_list.append(marshaller(return_val).python_val)
            elif marshaller is OLEColorArg:
                c = Color()
                c._from_ole_color(return_val)
                temp_return_list.append(c)
            else:
                temp_return_list.append(return_val)
    if len(temp_return_list) == 1:
        return temp_return_list[0]
    else:
        return tuple(temp_return_list)

def _grpc_guid(metadata:dict) -> AgGrpcServices_pb2.InterfaceID:
    iid = AgGrpcServices_pb2.InterfaceID()
    iid.data1 = metadata["iid_data"][0]
    iid.data2 = metadata["iid_data"][1]
    return iid

def _marshall_input_arg(arg:typing.Any, dest_grpc_arg) -> None:
    dest_grpc_arg.num_columns_in_repeated_values = _array_num_columns(arg)
    vals = _input_arg_to_single_dim_list(arg)
    for val in vals:
        rpc_val = AgGrpcServices_pb2.Variant.VariantValue()
        if type(val) == bool:
            rpc_val.bool_val = val
        elif type(val) == str:
            rpc_val.str_val = val
        elif type(val) == int:
            if val < 0:
                rpc_val.signed_int_val = val
            else:
                rpc_val.unsigned_int_val = val
        elif type(val) == float:
            rpc_val.double_val = val
        elif isinstance(val, IntEnum) or isinstance(val, IntFlag):
            rpc_val.signed_int_val = int(val)
        elif hasattr(val, "_intf"):
            if type(val._intf)==GrpcInterfacePimpl and type(val._intf._impl)==GrpcInterfaceFuture:
                rpc_val.obj_future_id = val._intf._impl.future_call_data.id
            else:
                rpc_val.obj.value = val._intf.obj.value
                rpc_val.obj.guid.MergeFrom(val._intf.obj.guid)
        elif val is None:
            rpc_val.null.SetInParent()
        elif type(val) == Color:
            rpc_val.unsigned_int_val = val._to_ole_color()
        dest_grpc_arg.values.append(rpc_val)

class GrpcInterface(object):
    def __init__(self, client: "GrpcClient", obj: AgGrpcServices_pb2.STKObject):
        self.client: "GrpcClient" = client
        self.obj = obj
        self.client._register_obj(self.obj)

    def __del__(self):
        self.client._release_obj(self.obj)

    def __eq__(self, other):
        return self.obj.value == other.obj.value and self.client == other.client

    def __hash__(self):
        return hash((self.obj.value, self.client))

    def __bool__(self):
        return self.client.active() and self.obj.value > 0

    def query_interface(self, intf_metadata:dict) -> "GrpcInterface":
        guid = _grpc_guid(intf_metadata)
        if self.client.supports_interface(self.obj, guid):
            return self
        else:
            return None

    def _query_backwards_compatability_interface(self, intf_metadata:dict, method_offset, *args):
        from .coclassutil import AgBackwardsCompatabilityMapping
        iid_tuple = (intf_metadata['iid_data'][0], intf_metadata['iid_data'][1])
        if AgBackwardsCompatabilityMapping.check_guid_available(iid_tuple):
            old_iid = AgBackwardsCompatabilityMapping.get_old_guid(iid_tuple)
            old_grpc_guid = _grpc_guid({"iid_data":[old_iid[0], old_iid[1]]})
            return self.client.invoke(self.obj, old_grpc_guid, method_offset, False, *args)
        return None

    def invoke(self, intf_metadata:dict, method_metadata:dict, *args):
        guid = _grpc_guid(intf_metadata)
        method_offset = method_metadata["offset"]
        try:
            invoke_return = self.client.invoke(self.obj, guid, method_offset, False, *args)
        except grpc.RpcError as rpc_error:
            if rpc_error.details() == "Interface not implemented.":
                invoke_return = self._query_backwards_compatability_interface(intf_metadata, method_offset, *args)
                if invoke_return is None:
                    raise rpc_error
            else:
                raise rpc_error
        return _grpc_post_process_return_vals(invoke_return, method_metadata["marshallers"], *args)

    def get_property(self, intf_metadata:dict, method_metadata:dict):
        guid = _grpc_guid(intf_metadata)
        method_offset = method_metadata["offset"]
        return _grpc_post_process_return_vals(self.client.get_property(self.obj, guid, method_offset), method_metadata["marshallers"], OutArg())

    def set_property(self, intf_metadata:dict, method_metadata:dict, value):
        guid = _grpc_guid(intf_metadata)
        method_offset = method_metadata["offset"]
        return self.client.set_property(self.obj, guid, method_offset, value)

    def subscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        return self.client.subscribe(self.obj, event_handler, event, callback)

    def unsubscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        return self.client.unsubscribe(self.obj, event_handler, event, callback)

    def unsubscribe_all(self, event_handler:AgGrpcServices_pb2.EventHandler):
        return self.client.unsubscribe(self.obj, event_handler, "", None)

class GrpcInterfacePimpl(object):

    def __init__(self, impl):
        self._impl = impl
        self.active = True

    def __eq__(self, other):
        return self._impl.__eq__(other)

    def __hash__(self):
        return self._impl.__hash__()

    def __bool__(self):
        return self._impl.__bool__()

    @property
    def obj(self):
        return self._impl.obj

    @property
    def client(self):
        return self._impl.client

    def deactivate(self):
        self.active = False

    def reset_impl(self, new_impl):
        self._impl = new_impl

    def _flush_batcher(self):
        if type(self._impl) == GrpcInterfaceFuture:
            # Executing the batch will bind the future
            # i.e. self._impl will become GrpcInterface instead of GrpcInterfaceFuture
            self._impl.batcher.execute_batch()

    def query_interface(self, intf_metadata:dict) -> "GrpcInterface":
        self._flush_batcher()
        return self._impl.query_interface(intf_metadata)

    def invoke(self, intf_metadata:dict, method_metadata:dict, *args):
        for arg in args:
            if type(arg) == OutArg:
                self._flush_batcher()
                break
        return self._impl.invoke(intf_metadata, method_metadata, *args)

    def get_property(self, intf_metadata:dict, method_metadata:dict):
        self._flush_batcher()
        return self._impl.get_property(intf_metadata, method_metadata)

    def set_property(self, intf_metadata:dict, method_metadata:dict, value):
        return self._impl.set_property(intf_metadata, method_metadata, value)

    def subscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        self._flush_batcher()
        return self._impl.subscribe(event_handler, event, callback)

    def unsubscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        self._flush_batcher()
        return self._impl.unsubscribe(event_handler, event, callback)

    def unsubscribe_all(self, event_handler:AgGrpcServices_pb2.EventHandler):
        self._flush_batcher()
        return self._impl.unsubscribe_all(event_handler)

class GrpcInterfaceFuture(object):

    def __init__(self, batcher:"GrpcCallBatcher", future_id:int, source_obj:typing.Any, future_provider:typing.Union[typing.Callable, property], *args):
        call_interface = None
        attr_name = None
        if hasattr(future_provider, "__name__"):
            attr_name = future_provider.__name__
        for superclass in reversed(source_obj.__class__.mro()):
            if attr_name is None:
                if hasattr(superclass, "_property_names"):
                    if future_provider in superclass._property_names:
                        attr_name = superclass._property_names[future_provider]
            if attr_name is None:
                continue
            if f"_{attr_name}_metadata" in superclass.__dict__:
                call_interface = superclass
                attr_metadata_name = f"_{attr_name}_metadata"
                break
            elif f"_get_{attr_name}_metadata" in superclass.__dict__:
                call_interface = superclass
                attr_metadata_name = f"_get_{attr_name}_metadata"
                break
        if call_interface is None:
            raise SyntaxError(f"Cannot create gRPC future; incorrect type.")
        self.batcher = batcher
        self.future_call_data = AgGrpcServices_pb2.STKObjectPromise()
        if type(source_obj._intf)==GrpcInterfacePimpl and type(source_obj._intf._impl)==GrpcInterfaceFuture:
            self.future_call_data.obj_future_id = source_obj._intf._impl.future_call_data.id
        else:
            self.future_call_data.obj.MergeFrom(source_obj._intf.obj)
        self.future_call_data.id = future_id
        intf_metadata = getattr(call_interface, "_metadata")
        guid = _grpc_guid(intf_metadata)
        method_metadata = getattr(call_interface, attr_metadata_name)
        method_offset = method_metadata["offset"]
        self.future_call_data.index = method_offset
        self.future_call_data.interface_guid.MergeFrom(guid)
        for arg in args:
            if type(arg) != OutArg:
                new_grpc_arg = AgGrpcServices_pb2.Variant()
                _marshall_input_arg(arg, new_grpc_arg)
                self.future_call_data.args.append(new_grpc_arg)
        self._enqueue_promise_in_batcher()

    def _enqueue_promise_in_batcher(self):
        """
        Enqueue batch request without a method invocation.

        On the STK side this will bind the future which will
        then be available to future request that use the future.
        """
        request = AgGrpcServices_pb2.InvokeRequest()
        request.future.MergeFrom(self.future_call_data)
        self.batcher._enqueue_batch_request(request)

    def query_interface(self, intf_metadata:dict) -> "GrpcInterface":
        raise SyntaxError(f"gRPC futures can not be casted to other types.")

    def invoke(self, intf_metadata:dict, method_metadata:dict, *args):
        guid = _grpc_guid(intf_metadata)
        request = AgGrpcServices_pb2.InvokeRequest()
        request.future.MergeFrom(self.future_call_data)
        request.index = method_metadata["offset"]
        request.interface_guid.MergeFrom(guid)
        for arg in args:
            if type(arg) == OutArg:
                raise SyntaxError(f"gRPC futures do not return values.")
            new_grpc_arg = AgGrpcServices_pb2.Variant()
            _marshall_input_arg(arg, new_grpc_arg)
            request.args.append(new_grpc_arg)
        try:
            self.batcher._enqueue_batch_request(request)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)

    def get_property(self, intf_metadata:dict, method_metadata:dict):
        raise SyntaxError(f"gRPC futures do not return values.")

    def set_property(self, intf_metadata:dict, method_metadata:dict, value):
        guid = _grpc_guid(intf_metadata)
        request = AgGrpcServices_pb2.InvokeRequest()
        request.future.MergeFrom(self.future_call_data)
        request.index = method_metadata["offset"]
        request.interface_guid.MergeFrom(guid)
        try:
            new_grpc_arg = AgGrpcServices_pb2.Variant()
            _marshall_input_arg(value, new_grpc_arg)
            request.args.append(new_grpc_arg)
            self.batcher._enqueue_batch_request(request)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)

    def subscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        raise SyntaxError(f"gRPC futures are not compatible with events.")

    def unsubscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        raise SyntaxError(f"gRPC futures are not compatible with events.")

    def unsubscribe_all(self, event_handler:AgGrpcServices_pb2.EventHandler):
        raise SyntaxError(f"gRPC futures are not compatible with events.")

class GrpcApplication(GrpcInterface):
    def __init__(self, client: "GrpcClient", obj):
        self.client: "GrpcClient" = client
        self.obj = obj
        self.client._register_app(self.obj)

    def __del__(self):
        # The application reference is released by the server when calling terminating the connection
        pass

class UnmanagedGrpcInterface(GrpcInterface):
    def __init__(self, client: "GrpcClient", obj):
        self.client: "GrpcClient" = client
        self.obj = obj

    def __del__(self):
        # Intentionally not calling GrpcInterface.__del__
        pass

    def release(self):
        self.client.release(self.obj)

class GrpcEnumerator(GrpcInterface):
    _NEXT_INDEX = 1
    _SKIP_INDEX = 2
    _RESET_INDEX = 3
    _CLONE_INDEX = 4
    _iid_data = AgGrpcServices_pb2.InterfaceID()
    _iid_data.data1 = IID_IEnumVARIANT[0]
    _iid_data.data2 = IID_IEnumVARIANT[1]

    def __init__(self, client: "GrpcClient", obj):
        GrpcInterface.__init__(self, client=client, obj=obj)
        self._reset()

    def _reset(self) -> None:
        self._item_queue = SimpleQueue()
        self._done_collecting = False

    def _enqueue_next_batch(self) -> None:
        if self._done_collecting or not self._item_queue.empty():
            return
        request = AgGrpcServices_pb2.CollectionRequest()
        request.obj.MergeFrom(self.obj)
        request.max_items = self.client._collection_batch_size
        response = self.client.stub.EnumerateCollection(request)
        self._done_collecting = response.done_collecting
        for item in response.items:
            self._item_queue.put(self.client._marshall_return_arg(item))

    def next(self) -> typing.Any:
        self._enqueue_next_batch()
        if self._item_queue.empty():
            return None
        return self._item_queue.get(block=False)

    def reset(self):
        self.client.invoke(self.obj, GrpcEnumerator._iid_data, GrpcEnumerator._RESET_INDEX, True)
        self._reset()

class GrpcClient(object):

    DEFAULT_RELEASE_BATCH_SIZE = 12
    DEFAULT_COLLECTION_BATCH_SIZE = 100

    _active_batchers = {}

    client_interceptor = None

    def __init__(self):
       self.channel = None
       self.stub = None
       self._addr = ''
       self._connection_id = 0
       self._release_batch_size = GrpcClient.DEFAULT_RELEASE_BATCH_SIZE
       self._collection_batch_size = GrpcClient.DEFAULT_COLLECTION_BATCH_SIZE
       self._app = None
       self._objects = []
       self._released_objects = []
       self._app_control_shutdown = False
       self._executor = ThreadPoolExecutor()
       self._event_loop_id = None
       self._event_callbacks = {
        AgGrpcServices_pb2.EventHandler.eIAgStkObjectRootEvents : {},
        AgGrpcServices_pb2.EventHandler.eIAgSTKXApplicationEvents : {},
        AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsSceneEvents : {},
        AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsKmlGraphicsEvents : {},
        AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsImageCollectionEvents : {},
        AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsTerrainCollectionEvents : {},
       }

    def set_grpc_options(self, options:dict) -> None:
        from ..utilities.grpcutilities import GrpcCallBatcher
        for option in options:
            value = options[option]
            if option == "release batch size":
                self._release_batch_size = value
            elif option == "collection iteration batch size":
                self._collection_batch_size = value if value > 0 else GrpcClient.DEFAULT_COLLECTION_BATCH_SIZE
            elif option == "disable batching":
                GrpcCallBatcher._disable_batching = value
            elif option == "raise exceptions with STK Engine":
                continue
            else:
                raise SyntaxError(f"Unrecognized gRPC option \"{option}\".")

    def __del__(self):
        self.terminate_connection()

    def __eq__(self, other):
        return self._addr == other._addr

    def __hash__(self):
        return hash(self._addr)

    def _register_app(self, obj:AgGrpcServices_pb2.STKObject):
        self._app = obj

    def _register_obj(self, obj:AgGrpcServices_pb2.STKObject):
        with GcDisabler():
            self._objects.append(obj)

    def _release_all_objects(self):
        with GcDisabler():
            self.BatchedRelease(self._released_objects + self._objects)
            self._objects = []
            self._released_objects = []

    def _release_obj(self, obj:AgGrpcServices_pb2.STKObject):
        with GcDisabler():
            if obj in self._objects:
                self._objects.remove(obj)
                self._released_objects.append(obj)
                if len(self._released_objects) >= self._release_batch_size:
                    self.BatchedRelease(self._released_objects)
                    self._released_objects = []

    def _initialize_connection(self):
        connect_request = AgGrpcServices_pb2.EmptyMessage()
        connect_response = self.stub.GetConnectionMetadata(connect_request)
        server_version = f"{connect_response.version}.{connect_response.release}.{connect_response.update}"
        expected_version = "13.0.0"
        if server_version != expected_version:
            raise RuntimeError(f"Version mismatch between Python client and gRPC server. Expected STK {expected_version}, found STK {server_version}.")
        self._connection_id = connect_response.connection_id

    def _enqueue_batch_request(self, request:AgGrpcServices_pb2.InvokeRequest):
        batcher = GrpcClient._active_batchers[self]
        batcher._enqueue_batch_request(request)
        if batcher._ready_for_invoke():
            batcher.execute_batch()

    def _batching_active(self) -> bool:
        return self in GrpcClient._active_batchers

    def _execute_batched_invoke(self) -> typing.List[AgGrpcServices_pb2.BatchedInvokeReturn.BoundFuture]:
        if self._batching_active():
            batcher = GrpcClient._active_batchers[self]
            batch = batcher._get_requests_for_invoke()
            if len(batch.requests) > 0:
                try:
                    batch_return = self.stub.BatchedInvoke(batch)
                    return batch_return.bound_futures
                except grpc.RpcError as rpc_error:
                    self._handle_rpc_error(rpc_error)

    @staticmethod
    def execute_call_batcher(batcher:"GrpcCallBatcher") -> typing.List[AgGrpcServices_pb2.BatchedInvokeReturn.BoundFuture]:
        return GrpcClient._execute_batched_invoke(batcher._client)

    @staticmethod
    def register_call_batcher(batcher:"GrpcCallBatcher") -> None:
        if batcher._client in GrpcClient._active_batchers:
            raise SyntaxError("Nested GrpcCallBatchers are not permitted.")
        GrpcClient._active_batchers[batcher._client] = batcher

    @staticmethod
    def unregister_call_batcher(batcher:"GrpcCallBatcher") -> None:
        del GrpcClient._active_batchers[batcher._client]

    @staticmethod
    def bind_future(batcher:"GrpcCallBatcher", future:GrpcInterfacePimpl, binding:AgGrpcServices_pb2.BatchedInvokeReturn.BoundFuture) -> None:
        """Replaces future's GrpcInterfaceFuture with a bound GrpcInterface."""
        bound_intf = GrpcInterface(obj=binding.obj, client=batcher._client)
        future.reset_impl(bound_intf)

    @staticmethod
    def new_client(host,
                   port,
                   timeout_sec:int=60,
                   max_receive_message_size:int=0,
                   grpc_channel_credentials:grpc.ChannelCredentials|None=None) -> "GrpcClient":
        addr = f"{host}:{port}"
        new_grpc_client = GrpcClient()
        channel_args = []
        if max_receive_message_size > 0:
            channel_args.append(("grpc.max_receive_message_length", max_receive_message_size))

        if grpc_channel_credentials == None:
            new_grpc_client.channel = grpc.insecure_channel(addr, options=channel_args)
        else:
            new_grpc_client.channel = grpc.secure_channel(addr, credentials=grpc_channel_credentials, options=channel_args)

        try:
            grpc.channel_ready_future(new_grpc_client.channel).result(timeout=timeout_sec)

            if GrpcClient.client_interceptor is not None:
                new_grpc_client.channel = grpc.intercept_channel(new_grpc_client.channel, GrpcClient.client_interceptor)

            new_grpc_client.stub = AgGrpcServices_pb2_grpc.STKGrpcServiceStub(new_grpc_client.channel)
            new_grpc_client._addr = addr
            new_grpc_client._initialize_connection()
            return new_grpc_client
        except grpc.FutureTimeoutError:
            pass

    def set_app_control_shutdown(self):
        self._app_control_shutdown = True

    def terminate_connection(self, call_shutdown=True):
        if self.active():
            self._execute_batched_invoke()
            self.stop_event_loop()
            self._executor.shutdown(wait=True)
            self._release_all_objects()
            if call_shutdown:
                shutdown_request = AgGrpcServices_pb2.ShutDownRequest()
                shutdown_request.app_to_release.MergeFrom(self._app)
                shutdown_request.app_control_shutdown = self._app_control_shutdown
                self.stub.ShutDownServer(shutdown_request)
            self.stub = None
            if self.channel is not None:
                self.channel.close()

    def active(self) -> bool:
        return self.stub is not None

    def add_ref(self, obj:AgGrpcServices_pb2.STKObject) -> int:
        request = AgGrpcServices_pb2.RefCountRequest()
        request.obj.value = obj.value
        response = self.stub.AddRef(request)
        ret = response.count
        return ret

    def release(self, obj:AgGrpcServices_pb2.STKObject) -> int:
        if self.active():
            request = AgGrpcServices_pb2.RefCountRequest()
            request.obj.value = obj.value
            response = self.stub.Release(request)
            ret = response.count
            return ret

    def BatchedRelease(self, objects:typing.List[AgGrpcServices_pb2.STKObject]) -> None:
        if self.active():
            request = AgGrpcServices_pb2.BatchedReleaseRequest()
            request.objects.extend(objects)
            response = self.stub.BatchedRelease(request)

    def supports_interface(self, obj:AgGrpcServices_pb2.STKObject, guid:AgGrpcServices_pb2.InterfaceID) -> bool:
        if self.active():
            request = AgGrpcServices_pb2.SupportsInterfaceRequest()
            request.obj.value = obj.value
            request.interface_guid.MergeFrom(guid)
            response = self.stub.SupportsInterface(request)
            ret = response.result
            return ret

    def _marshall_grpc_obj_to_py_class(self, obj:AgGrpcServices_pb2.STKObject, managed:bool=True) -> typing.Any:
        from .coclassutil import AgClassCatalog
        clsid = (obj.guid.data1, obj.guid.data2)
        if AgClassCatalog.check_clsid_available(clsid):
            cls = AgClassCatalog.get_class(clsid)
            pyobj = cls()
            if managed:
                intf = GrpcInterface(obj=obj, client=self)
            else:
                intf = UnmanagedGrpcInterface(obj=obj, client=self)
            pyobj._private_init(intf)
            return pyobj
        elif clsid == IID_IEnumVARIANT:
            return GrpcEnumerator(obj=obj, client=self)
        else:
            self.release(obj)
            return None

    def get_stk_application_interface(self) -> GrpcInterface:
        self._execute_batched_invoke()
        grpc_app_request = AgGrpcServices_pb2.EmptyMessage()
        grpc_app_response = self.stub.GetStkApplication(grpc_app_request)
        intf = GrpcApplication(obj=grpc_app_response.obj, client=self)
        return intf

    def new_object_root(self) -> GrpcInterface:
        self._execute_batched_invoke()
        grpc_response = self.stub.EngineNewRoot(AgGrpcServices_pb2.EmptyMessage())
        intf = GrpcInterface(obj=grpc_response.obj, client=self)
        return intf

    def new_object_model_context(self) -> GrpcInterface:
        self._execute_batched_invoke()
        grpc_response = self.stub.EngineNewRootContext(AgGrpcServices_pb2.EmptyMessage())
        intf = GrpcInterface(obj=grpc_response.obj, client=self)
        return intf

    def _marshall_single_grpc_value(self, val:AgGrpcServices_pb2.Variant.VariantValue, manage_ref_counts:bool=True) -> typing.Any:
        which_val = val.WhichOneof("Value")
        if which_val=="obj":
            return self._marshall_grpc_obj_to_py_class(val.obj, manage_ref_counts)
        elif which_val=="str_val":
            return val.str_val
        elif which_val=="bool_val":
            return val.bool_val
        elif which_val=="double_val":
            return val.double_val
        elif which_val=="unsigned_int_val":
            return val.unsigned_int_val
        elif which_val=="signed_int_val":
            return val.signed_int_val
        elif which_val=="null":
            return None
        elif which_val=="nested_array":
            return self._marshall_return_arg(val.nested_array)

    def _marshall_return_arg(self, arg:AgGrpcServices_pb2.Variant, manage_ref_counts:bool=True) -> typing.Any:
        if arg.num_columns_in_repeated_values > 0:
            # This is an array and we need to return a list, even if the array has 0 or 1 element
            num_cols = arg.num_columns_in_repeated_values
            if num_cols == 1:
                return [self._marshall_single_grpc_value(val, manage_ref_counts) for val in arg.values]
            else:
                num_rows = round(len(arg.values) / num_cols)
                return_array = list()
                for i in range(num_rows):
                    row_array = list()
                    for j in range(num_cols):
                        row_array.append(self._marshall_single_grpc_value(arg.values[i+j*num_rows], manage_ref_counts))
                    return_array.append(row_array)
                return return_array
        elif len(arg.values) == 0:
            return
        elif len(arg.values) == 1:
            return self._marshall_single_grpc_value(arg.values[0], manage_ref_counts)

    def invoke(self, p:AgGrpcServices_pb2.STKObject, guid:AgGrpcServices_pb2.InterfaceID, method_offset:int, disable_batch:bool, *args) -> typing.Any:
        request = AgGrpcServices_pb2.InvokeRequest()
        request.obj.MergeFrom(p)
        request.index = method_offset
        request.interface_guid.MergeFrom(guid)
        use_batch = not disable_batch
        for arg in args:
            if type(arg) != OutArg:
                new_grpc_arg = AgGrpcServices_pb2.Variant()
                _marshall_input_arg(arg, new_grpc_arg)
                request.args.append(new_grpc_arg)
            else:
                use_batch = False
        try:
            if use_batch and self._batching_active():
                self._enqueue_batch_request(request)
            else:
                self._execute_batched_invoke()
                response = self.stub.Invoke(request)
                if len(response.return_vals) == 0:
                    return
                elif len(response.return_vals) == 1:
                    return self._marshall_return_arg(response.return_vals[0])
                else:
                    return tuple([self._marshall_return_arg(arg) for arg in response.return_vals])
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
                raise RuntimeError("gRPC message size limit exceeded. Try chunking the data request or specify a larger limit using grpc_max_message_size when starting the application.")
            else:
                self._handle_rpc_error(rpc_error)

    def get_property(self, p:AgGrpcServices_pb2.STKObject, guid:AgGrpcServices_pb2.InterfaceID, method_offset) -> typing.Any:
        self._execute_batched_invoke()
        request = AgGrpcServices_pb2.GetPropertyRequest()
        request.obj.MergeFrom(p)
        request.index = method_offset
        request.interface_guid.MergeFrom(guid)
        try:
            response = self.stub.GetProperty(request)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)
        return self._marshall_return_arg(response.variant)

    def set_property(self, p:AgGrpcServices_pb2.STKObject, guid:AgGrpcServices_pb2.InterfaceID, method_offset, arg) -> None:
        use_batching = self._batching_active()
        if use_batching:
            request = AgGrpcServices_pb2.InvokeRequest()
        else:
            request = AgGrpcServices_pb2.SetPropertyRequest()
        request.obj.MergeFrom(p)
        request.index = method_offset
        request.interface_guid.MergeFrom(guid)
        try:
            if use_batching:
                new_grpc_arg = AgGrpcServices_pb2.Variant()
                _marshall_input_arg(arg, new_grpc_arg)
                request.args.append(new_grpc_arg)
                self._enqueue_batch_request(request)
            else:
                _marshall_input_arg(arg, request.variant)
                response = self.stub.SetProperty(request)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)

    def _handle_rpc_error(self, rpc_error):
        """If the RPC error is an STK Runtime Error, raise a RuntimeError exception. Otherwise rethrow it."""
        code = rpc_error.code()
        if code == grpc.StatusCode.UNKNOWN:
            details = rpc_error.details()
            prelude = "STKRuntimeError: "
            if details.startswith(prelude):
                msg = details[len(prelude):]
                m = re.search(r"HRESULT = (0[xX][0-9A-Fa-f]+)", msg)
                if m is not None:
                    hr = int(m.group(1), 16)
                    msg = error_msg_from_hresult(hr)
                raise RuntimeError(msg) from None
        raise # rethrow last exception that occurred, which is rpc_error

    def acknowledge_event(self, event_id:int) -> None:
        request = AgGrpcServices_pb2.EventLoopData()
        request.event_loop_id = self._event_loop_id
        request.event_id = event_id
        response = self.stub.AcknowledgeEvent(request)

    def _fire_event(self, callbacks, args, event_id):
        if callbacks is not None:
            for callback in callbacks:
                try:
                    callback(*args)
                except:
                    _logger.exception(f"Exception raised during callback registered to {callback.__name__}:")
                self._execute_batched_invoke()
        self.acknowledge_event(event_id)

    def _consume_events(self, stream):
        try:
            for event in stream:
                self._execute_batched_invoke()
                handler = event.subscription.event_handler
                name = event.subscription.event_name
                p = event.subscription.obj
                args = [self._marshall_return_arg(arg, False) for arg in event.callback_args]
                callbacks = self._event_callbacks[handler][name][p.value]
                self._executor.submit(self._fire_event, callbacks, args, event.event_id)
        except:
            _logger.exception("Exception raised during handling of STK events:")

    def start_event_loop(self):
        if self._event_loop_id is None:
            event_stream = self.stub.StartEventLoop(AgGrpcServices_pb2.EmptyMessage())
            metadata = event_stream.next()
            self._event_loop_id = metadata.subscription.event_loop_id
            self._consumer_future = self._executor.submit(self._consume_events, event_stream)

    def stop_event_loop(self):
        if self._event_loop_id is not None:
            request = AgGrpcServices_pb2.EventLoopData()
            request.event_loop_id = self._event_loop_id
            response = self.stub.StopEventLoop(request)
            self._consumer_future.result(timeout=None)
            self._event_loop_id = None

    def _has_subscriptions(self):
        for handler in self._event_callbacks:
            for event in self._event_callbacks[handler]:
                for ptr in self._event_callbacks[handler][event]:
                    if self._event_callbacks[handler][event][ptr] is not None:
                        if len(self._event_callbacks[handler][event][ptr]) > 0:
                            return True
        return False

    def subscribe(self, p:AgGrpcServices_pb2.STKObject, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        if self._event_loop_id is None:
            self.start_event_loop()
        request = AgGrpcServices_pb2.SubscriptionData()
        request.event_loop_id = self._event_loop_id
        request.obj.MergeFrom(p)
        request.event_handler = event_handler
        request.event_name = event
        response = self.stub.Subscribe(request)
        if event not in self._event_callbacks[event_handler]:
            self._event_callbacks[event_handler][event] = {}
        if p.value not in self._event_callbacks[event_handler][event]:
            self._event_callbacks[event_handler][event][p.value] = []
        self._event_callbacks[event_handler][event][p.value].append(callback)

    def unsubscribe(self, p:AgGrpcServices_pb2.STKObject, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        if self._event_loop_id is not None:
            request = AgGrpcServices_pb2.SubscriptionData()
            request.event_loop_id = self._event_loop_id
            request.obj.MergeFrom(p)
            request.event_handler = event_handler
            request.event_name = event
            response = self.stub.Unsubscribe(request)
            if event == "":
                for event_name in self._event_callbacks[event_handler]:
                    self._event_callbacks[event_handler][event_name][p.value] = None
            else:
                self._event_callbacks[event_handler][event][p.value].remove(callback)
            if not self._has_subscriptions():
                self.stop_event_loop()
