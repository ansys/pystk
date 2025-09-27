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

"""
Optimize performance of gRPC communications.

GrpcCallBatcher may be used to reduce the number of remote communications
by batching together API commands that do not require return values.
"""

import typing

from ..internal.apiutil import SupportsDeleteCallback

try:
    from ..internal.AgGrpcServices_pb2 import BatchedInvokeRequest, InvokeRequest
    from ..internal.grpcutil import GrpcClient, GrpcInterfaceFuture, GrpcInterfacePimpl
    _DEFAULT_BATCH_DISABLE = False
except ImportError:
    _DEFAULT_BATCH_DISABLE = True

class GrpcCallBatcher(object):
    """
    A class used to batch together API calls to optimize performance.

    Activating batching will cause the normal API exception behavior to be
    altered. Exceptions from one command may appear asynchronously. Therefore
    it is not recommended to use call batching while building and debugging,
    but rather as a performance optimization.

    Only calls that do not return a value may be batched together,
    such as set-property requests and methods without a return value.
    Any method that has a return value (including get-property requests)
    will automatically execute any previously batched commands before the
    method with a return value is executed.

    Therefore, to reduce the number of remote API requests and improve
    performance, code must be organized to group together commands that
    do not have a return value. Call chaining will interrupt a batch request
    because of the get-property command within the chain. E.g.:

        root.CurrentScenario.ShortDescription = short_description
        root.CurrentScenario.LongDescription = long_description

    will not be batched together because the call to `CurrentScenario` will
    get the scenario via an API call. These commands may be batched by
    factoring out the call chaining:

        scen = root.CurrentScenario
        scen.ShortDescription = short_description
        scen.LongDescription = long_description

    This class may be used via the explicit commands or by using the "with"
    statement to batch together the commands within the statement block.
    e.g.

        call_batcher = stk.NewGrpcCallBatcher()
        with call_batcher:
            facility1.LocalTimeOffset = 1.0
            facility1.HeightAboveGround = 10.0
            facility1.UseLocalTimeOffset = True
            facility1.ResetAzElMask()
    """

    _default_max_batch_size = 10000
    _disable_batching = _DEFAULT_BATCH_DISABLE

    def __init__(self, disable_batching=False):
        """Construct an object of type GrpcCallBatcher."""
        self._initialized = False
        self._max_batch = GrpcCallBatcher._default_max_batch_size
        self._disable_batching = GrpcCallBatcher._disable_batching or disable_batching
        self._reset()

    def _reset(self):
        self._next_future_id = 1
        self._unbound_futures = {}

    def _private_init(self, client:"GrpcClient", max_batch:int=None) -> None:
        self._initialized = True
        self._client = client
        self._requests = BatchedInvokeRequest()
        self._batching = False
        if max_batch is not None:
            if max_batch > GrpcCallBatcher._default_max_batch_size:
                raise SyntaxError(f"Batch size cannot exceed {GrpcCallBatcher._default_max_batch_size} due to gRPC message size restrictions.")
            self._max_batch = max_batch

    def __enter__(self):
        """Use GrpcCallBatcher with the "with" statement to activate batching."""
        if not self._disable_batching:
            self.start_batching()
        return self

    def __exit__(self, type, value, tb):
        """Use GrpcCallBatcher with the "with" statement to deactivate batching."""
        if not self._disable_batching:
            self.stop_batching()
        return False

    def start_batching(self) -> None:
        """Explicitly start batching until stop_batching() is called."""
        if not self._disable_batching and not self._batching:
            if not self._initialized:
                raise RuntimeError("The GrpcCallBatcher should be obtained from the STK application rather than constructed directly.")
            GrpcClient.register_call_batcher(self)
            self._batching = True

    def execute_batch(self) -> None:
        """Explicitly execute any queued batch commands."""
        if not self._disable_batching and self._batching:
            bindings = GrpcClient.execute_call_batcher(self)
            if bindings is not None:
                for binding in bindings:
                    GrpcClient.bind_future(self, self._unbound_futures[binding.obj_future_id], binding)
            self._reset()

    def stop_batching(self) -> None:
        """Explicitly stop batching."""
        if not self._disable_batching and self._initialized:
            self.execute_batch()
            GrpcClient.unregister_call_batcher(self)
            self._batching = False

    def _enqueue_batch_request(self, request:"InvokeRequest") -> None:
        self._requests.requests.append(request)

    def _ready_for_invoke(self) -> bool:
        if len(self._requests.requests) >= self._max_batch:
            return True
        return False

    def _get_requests_for_invoke(self) -> "BatchedInvokeRequest":
        batch = self._requests
        self._requests = BatchedInvokeRequest()
        active_futures = self._get_active_futures()
        if len(active_futures) > 0:
            batch.future_ids_to_return.extend(active_futures)
        return batch

    def _get_active_futures(self) -> typing.List[int]:
        active_list = []
        for future_id in self._unbound_futures:
            if self._unbound_futures[future_id].active:
                active_list.append(future_id)
        return active_list

    @staticmethod
    def _bypass_future_creation(source_obj:typing.Any, future_provider:typing.Union[typing.Callable, property], *args) -> typing.Any:
        if callable(future_provider):
            if hasattr(source_obj, future_provider.__name__):
                return future_provider(source_obj, *args)
        elif type(future_provider) is property:
            attr_name = None
            for superclass in reversed(source_obj.__class__.mro()):
                if hasattr(superclass, "_property_names"):
                    if future_provider in superclass._property_names:
                        attr_name = superclass._property_names[future_provider]
                        break
            if attr_name is None:
                raise SyntaxError("Cannot create gRPC future; incorrect type.")
            return getattr(source_obj, attr_name)

    def create_future(self, source_obj:typing.Any, future_provider:typing.Union[typing.Callable, property], future_type:typing.Any, *args) -> typing.Any:
        """
        Create an object of type future_type that supports batching operations.

        source_obj is an STK Object Model type, e.g. STKObjectRoot.
        future_provider is a member method or property of source_obj, e.g. STKObjectRoot.CurrentScenario.
        future_type is the STK Object Model type that is returned from future_provider, e.g. Scenario.
        args are the arguments passed to future_provider if applicable.
        """
        if self._disable_batching:
            return GrpcCallBatcher._bypass_future_creation(source_obj, future_provider, *args)
        if not self._batching:
            raise SyntaxError("Batcher must be active to create futures.")
        if not callable(future_type):
            raise SyntaxError("Future class type must be a full STK Object type (e.g. Scenario, not Scenario).")
        future = future_type()
        if not isinstance(future, SupportsDeleteCallback):
            raise SyntaxError("Future class type must be a full STK Object type (e.g. Scenario, not Scenario).")
        intf_proxy = GrpcInterfaceFuture(self, self._next_future_id, source_obj, future_provider, *args)
        intf_pimpl = GrpcInterfacePimpl(intf_proxy)
        future._private_init(intf_pimpl)
        future._add_delete_callback(intf_pimpl.deactivate)
        self._unbound_futures[self._next_future_id] = intf_pimpl
        self._next_future_id += 1
        return future
