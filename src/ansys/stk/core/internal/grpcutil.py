# Copyright 2020-2023, Ansys Government Initiatives 

import typing
import grpc
from enum import IntEnum, IntFlag
from concurrent.futures import ThreadPoolExecutor

from . import AgGrpcServices_pb2
from . import AgGrpcServices_pb2_grpc

from .marshall import AgEnum_arg, OLE_COLOR_arg
from .apiutil import out_arg
from ..utilities.exceptions import *
from ..utilities.colors import Color

IID_IEnumVARIANT = "{00020404-0000-0000-C000-000000000046}"
        
def _is_list_type(arg:typing.Any) -> bool:
    if type(arg) == str or not hasattr(arg, '__iter__'):
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
                    raise STKRuntimeError("Arrays with dimension > 2 are not supported argument types.")
                if len(arg[j]) != col_length:
                    raise STKRuntimeError(f"Malformed array argument. len(array[{j}]) != len(array[0]).")
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
        if type(input_arg) == out_arg:
            return_val = return_vals[ret_val_iter] if multiple_returns else return_vals
            ret_val_iter += 1
            if type(marshaller)==AgEnum_arg:
                temp_return_list.append(marshaller(return_val).python_val)
            elif marshaller is OLE_COLOR_arg:
                c = Color()
                c._FromOLECOLOR(return_val)
                temp_return_list.append(c)
            else:
                temp_return_list.append(return_val)
    if len(temp_return_list) == 1:
        return temp_return_list[0]
    else:
        return tuple(temp_return_list)

class grpc_interface(object):
    def __init__(self, client, obj):
        self.client = client
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

    def query_interface(self, guid) -> "grpc_interface":
        if self.client.SupportsInterface(self.obj, str(guid)):
            return self
        else:
            return None

    def invoke(self, intf_metatdata:dict, method_metadata:dict, *args):
        guid_str = intf_metatdata["uuid"]
        method_offset = intf_metatdata["method_offsets"][method_metadata["name"]]
        return _grpc_post_process_return_vals(self.client.Invoke(self.obj, guid_str, method_offset, *args), method_metadata["marshallers"], *args)

    def get_property(self, intf_metatdata:dict, method_metadata:dict):
        guid_str = intf_metatdata["uuid"]
        method_offset = intf_metatdata["method_offsets"]["get_" + method_metadata["name"]]
        return _grpc_post_process_return_vals(self.client.GetProperty(self.obj, guid_str, method_offset), method_metadata["marshallers"], out_arg())

    def set_property(self, intf_metatdata:dict, method_metadata:dict, value):
        guid_str = intf_metatdata["uuid"]
        method_offset = intf_metatdata["method_offsets"]["set_" + method_metadata["name"]]
        return self.client.SetProperty(self.obj, guid_str, method_offset, value)

    def subscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        return self.client.Subscribe(self.obj, event_handler, event, callback)

    def unsubscribe(self, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        return self.client.Unsubscribe(self.obj, event_handler, event, callback)
        
    def unsubscribe_all(self, event_handler:AgGrpcServices_pb2.EventHandler):
        return self.client.Unsubscribe(self.obj, event_handler, "", None)

class grpc_application(grpc_interface):
    def __init__(self, client, obj):
        self.client = client
        self.obj = obj
        self.client._register_app(self.obj)

    def __del__(self):
        # The application reference is released by the server when calling TerminateConnection()
        pass

class unmanaged_grpc_interface(grpc_interface):
    def __init__(self, client, obj):
        self.client = client
        self.obj = obj

    def __del__(self):
        # Intentionally not calling grpc_interface.__del__
        pass

    def release(self):
        self.client.Release(self.obj)

class grpc_enumerator(grpc_interface):
    _NEXT_INDEX = 1
    _SKIP_INDEX = 2
    _RESET_INDEX = 3
    _CLONE_INDEX = 4
    
    def __init__(self, client, obj):
        grpc_interface.__init__(self, client=client, obj=obj)

    def next(self) -> typing.Any:
        (retval, num_fetched) = self.client.Invoke(self.obj, IID_IEnumVARIANT, grpc_enumerator._NEXT_INDEX)
        if num_fetched == 1:
            return retval
        return None

    def reset(self):
        self.client.Invoke(self.obj, IID_IEnumVARIANT, grpc_enumerator._RESET_INDEX)

class grpc_client(object):

    def __init__(self):
       self.channel = None
       self.stub = None
       self._addr = ''
       self._connection_id = 0
       self._app = None
       self._objects = []
       self._shutdown_stkruntime = False
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

    def __del__(self):
        self.TerminateConnection()

    def __eq__(self, other):
        return self._addr == other._addr

    def __hash__(self):
        return hash(self._addr)

    def _register_app(self, obj:AgGrpcServices_pb2.STKObject):
        self._app = obj

    def _register_obj(self, obj:AgGrpcServices_pb2.STKObject):
        self._objects.append(obj)

    def _release_all_objects(self):
        while len(self._objects) > 0:
            self.Release(self._objects.pop())

    def _release_obj(self, obj:AgGrpcServices_pb2.STKObject):
        if obj in self._objects:
            self.Release(obj)
            self._objects.remove(obj)
            
    def _initialize_connection(self):
        connect_request = AgGrpcServices_pb2.EmptyMessage()
        connect_response = self.stub.GetConnectionMetadata(connect_request)
        server_version = f"{connect_response.version}.{connect_response.release}.{connect_response.update}"
        expected_version = "12.8.0"
        if server_version != expected_version:
            raise STKRuntimeError(f"Version mismatch between Python client and gRPC server. Expected STK {expected_version}, found STK {server_version}.")
        self._connection_id = connect_response.connection_id

    @staticmethod
    def new_client(host, port, timeout_sec:int=60) -> "grpc_client":
        addr = f"{host}:{port}"
        new_grpc_client = grpc_client()
        new_grpc_client.channel = grpc.insecure_channel(addr)
        try:
            grpc.channel_ready_future(new_grpc_client.channel).result(timeout=timeout_sec)
            new_grpc_client.stub = AgGrpcServices_pb2_grpc.STKGrpcServiceStub(new_grpc_client.channel)
            new_grpc_client._addr = addr
            new_grpc_client._initialize_connection()
            return new_grpc_client
        except grpc.FutureTimeoutError:
            pass

    def set_shutdown_stkruntime(self, shutdown_stkruntime:bool):
        self._shutdown_stkruntime = shutdown_stkruntime
        
    def TerminateConnection(self):
        if self.active():
            self.StopEventLoop()
            self._executor.shutdown(wait=True)
            self._release_all_objects()
            shutdown_request = AgGrpcServices_pb2.ShutDownRequest()
            shutdown_request.app_to_release.MergeFrom(self._app)
            shutdown_request.shutdown_stkruntime = self._shutdown_stkruntime
            self.stub.ShutDownServer(shutdown_request)
            self.stub = None
            if self.channel is not None:
                self.channel.close()
        
    def active(self) -> bool:
        return self.stub is not None
        
    def AddRef(self, obj:AgGrpcServices_pb2.STKObject) -> int:
        request = AgGrpcServices_pb2.RefCountRequest()
        request.obj.value = obj.value
        response = self.stub.AddRef(request)
        ret = response.count
        return ret
    
    def Release(self, obj:AgGrpcServices_pb2.STKObject) -> int:
        if self.active():
            request = AgGrpcServices_pb2.RefCountRequest()
            request.obj.value = obj.value
            response = self.stub.Release(request)
            ret = response.count
            return ret
        
    def SupportsInterface(self, obj:AgGrpcServices_pb2.STKObject, guid:str) -> bool:
        if self.active():
            request = AgGrpcServices_pb2.SupportsInterfaceRequest()
            request.obj.value = obj.value
            request.interface_guid = guid
            response = self.stub.SupportsInterface(request)
            ret = response.result
            return ret
        
    def _marshall_grpc_obj_to_py_class(self, obj:AgGrpcServices_pb2.STKObject, managed:bool=True) -> typing.Any:
        from .coclassutil import AgClassCatalog
        clsid = obj.guid
        if AgClassCatalog.check_clsid_available(clsid):
            cls = AgClassCatalog.get_class(clsid)
            pyobj = cls()
            if managed:
                intf = grpc_interface(obj=obj, client=self)
            else:
                intf = unmanaged_grpc_interface(obj=obj, client=self)
            pyobj._private_init(intf)
            return pyobj
        elif clsid == IID_IEnumVARIANT:
            return grpc_enumerator(obj=obj, client=self)
        else:
            self.Release(obj)
            return None
        
    def GetStkApplicationInterface(self) -> grpc_interface:
        grpc_app_request = AgGrpcServices_pb2.EmptyMessage()
        grpc_app_response = self.stub.GetStkApplication(grpc_app_request)
        intf = grpc_application(obj=grpc_app_response.obj, client=self)
        return intf
        
    def NewObjectRoot(self) -> grpc_interface:
        grpc_response = self.stub.EngineNewRoot(AgGrpcServices_pb2.EmptyMessage())
        intf = grpc_interface(obj=grpc_response.obj, client=self)
        return intf
        
    def NewObjectModelContext(self) -> grpc_interface:
        grpc_response = self.stub.EngineNewRootContext(AgGrpcServices_pb2.EmptyMessage())
        intf = grpc_interface(obj=grpc_response.obj, client=self)
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
        
    def _marshall_input_arg(self, arg:typing.Any, dest_grpc_arg) -> None:
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
                rpc_val.obj.value = val._intf.obj.value
                rpc_val.obj.guid = val._intf.obj.guid
            elif val is None:
                rpc_val.null.SetInParent()
            elif type(val) == Color:
                rpc_val.unsigned_int_val = val._ToOLECOLOR()
            dest_grpc_arg.values.append(rpc_val)
        
    def Invoke(self, p:AgGrpcServices_pb2.STKObject, guid:str, method_offset, *args) -> typing.Any:
        request = AgGrpcServices_pb2.InvokeRequest()
        request.obj.MergeFrom(p)
        request.index = method_offset
        request.interface_guid = guid
        for arg in args:
            if type(arg) != out_arg:
                new_grpc_arg = AgGrpcServices_pb2.Variant()
                self._marshall_input_arg(arg, new_grpc_arg)
                request.args.append(new_grpc_arg)
        try:
            response = self.stub.Invoke(request)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)
        if len(response.return_vals) == 0:
            return
        elif len(response.return_vals) == 1:
            return self._marshall_return_arg(response.return_vals[0])
        else:
            return tuple([self._marshall_return_arg(arg) for arg in response.return_vals])
                
    def GetProperty(self, p:AgGrpcServices_pb2.STKObject, guid:str, method_offset) -> typing.Any:
        request = AgGrpcServices_pb2.GetPropertyRequest()
        request.obj.MergeFrom(p)
        request.index = method_offset
        request.interface_guid = guid
        try:
            response = self.stub.GetProperty(request)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)
        return self._marshall_return_arg(response.variant)
            
    def SetProperty(self, p:AgGrpcServices_pb2.STKObject, guid:str, method_offset, *args) -> None:
        request = AgGrpcServices_pb2.SetPropertyRequest()
        request.obj.MergeFrom(p)
        request.index = method_offset
        request.interface_guid = guid
        for arg in args:
            if type(arg) != out_arg:
                self._marshall_input_arg(arg, request.variant)
        try:
            response = self.stub.SetProperty(request)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)

    def _handle_rpc_error(self, rpc_error):
        """If the RPC error is an STK Runtime Error, raises a STKRuntimeError exception. Otherwise rethrow it."""
        code = rpc_error.code()
        if code == grpc.StatusCode.UNKNOWN:
            details = rpc_error.details()
            prelude = "STKRuntimeError: "
            if details.startswith(prelude):
                msg = details[len(prelude):]
                raise STKRuntimeError(msg) from None
        raise # rethrow last exception that occurred, which is rpc_error 

    def AcknowledgeEvent(self, event_id:int) -> None:
        request = AgGrpcServices_pb2.EventLoopData()
        request.event_loop_id = self._event_loop_id
        request.event_id = event_id
        response = self.stub.AcknowledgeEvent(request)

    def _fire_event(self, callbacks, args, event_id):
        if callbacks is not None:
            for callback in callbacks:
                callback(*args)
        self.AcknowledgeEvent(event_id)

    def _consume_events(self, stream):
        try:
            for event in stream:
                handler = event.subscription.event_handler
                name = event.subscription.event_name
                p = event.subscription.obj
                args = [self._marshall_return_arg(arg, False) for arg in event.callback_args]
                callbacks = self._event_callbacks[handler][name][p.value]
                self._executor.submit(self._fire_event, callbacks, args, event.event_id)
        except:
            pass

    def StartEventLoop(self):
        if self._event_loop_id is None:
            event_stream = self.stub.StartEventLoop(AgGrpcServices_pb2.EmptyMessage())
            metadata = event_stream.next()
            self._event_loop_id = metadata.subscription.event_loop_id
            self._consumer_future = self._executor.submit(self._consume_events, event_stream)

    def StopEventLoop(self):
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

    def Subscribe(self, p:AgGrpcServices_pb2.STKObject, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
        if self._event_loop_id is None:
            self.StartEventLoop()
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

    def Unsubscribe(self, p:AgGrpcServices_pb2.STKObject, event_handler:AgGrpcServices_pb2.EventHandler, event:str, callback:callable):
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
                self.StopEventLoop()
