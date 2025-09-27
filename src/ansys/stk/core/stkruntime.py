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

"""Starts STK Runtime or attaches to an already running STK Runtime, and provides access to the Object Model root."""

__all__ = ["STKRuntime", "STKRuntimeApplication"]

import atexit
import os
import pathlib
import socket

# The subprocess module is needed to start the backend.
# Excluding low severity bandit warning as the validity of the inputs is enforced.
import subprocess  # nosec B404
import typing

if typing.TYPE_CHECKING:
    import grpc

from .internal.apiutil import InterfaceProxy, read_registry_key, winreg_stk_binary_dir
from .internal.grpcutil import GrpcClient
from .stkobjects import STKObjectModelContext, STKObjectRoot
from .stkx import STKXApplication
from .utilities.grpcutilities import GrpcCallBatcher


class STKRuntimeApplication(STKXApplication):
    """
    Interact with STK Runtime.

    Use STKRuntime.StartApplication() or STKRuntime.AttachToApplication()
    to obtain an initialized STKRuntimeApplication object.
    """

    def __init__(self):
        """Construct an object of type STKRuntimeApplication."""
        self.__dict__["_intf"] = InterfaceProxy()
        STKXApplication.__init__(self)
        self.__dict__["_root"] = None
        self.__dict__["_shutdown"] = False

    def _private_init(self, intf: InterfaceProxy):
        STKXApplication._private_init(self, intf)

    def __del__(self):
        """Destruct the STKRuntimeApplication object when all references to the object are deleted."""
        if self._intf:
            client: GrpcClient = self._intf.client
            client.terminate_connection(call_shutdown=self._shutdown)

    def new_object_root(self) -> STKObjectRoot:
        """May be used to obtain an Object Model Root from a running STK Engine application."""
        if self._intf:
            client: GrpcClient = self._intf.client
            root_unk = client.new_object_root()
            root = STKObjectRoot()
            root._private_init(root_unk)
            return root
        raise RuntimeError("Not connected to the gRPC server.")

    def new_object_model_context(self) -> STKObjectModelContext:
        """May be used to obtain an Object Model Context from a running STK Engine application."""
        if self._intf:
            client: GrpcClient = self._intf.client
            context_unk = client.new_object_model_context()
            context = STKObjectModelContext()
            context._private_init(context_unk)
            return context
        raise RuntimeError("Not connected to the gRPC server.")

    def set_grpc_options(self, options:dict) -> None:
        """
        Set advanced-usage options for the gRPC client.

        Available options include:
        { "collection iteration batch size" : int }. Number of items to preload while iterating
        through a collection object. Default is 100. Use 0 to indicate no limit (load entire collection).
        { "disable batching" : bool }. Disable all batching operations.
        { "release batch size" : int }. Number of interfaces to be garbage collected before
        sending the entire batch to STK to be released. Default value is 12.
        """
        if self._intf:
            client: GrpcClient = self._intf.client
            client.set_grpc_options(options)

    def new_grpc_call_batcher(self, max_batch:int=None, disable_batching:bool=False) -> GrpcCallBatcher:
        """
        Construct a GrpcCallBatcher linked to this gRPC client that may be used to improve API performance.

        max_batch is the maximum number of calls to batch together.
        Set disable_batching=True to disable batching operations for this batcher.
        See grpcutilities module for more information.
        """
        batcher = GrpcCallBatcher(disable_batching)
        batcher._private_init(self._intf.client, max_batch)
        return batcher

    def shutdown(self) -> None:
        """Shut down the STKRuntime application."""
        self.__dict__["_shutdown"] = True
        self._disconnect()

    def _disconnect(self) -> None:
        """Safely disconnect from STKRuntime."""
        if self._intf:
            client: GrpcClient = self._intf.client
            client.terminate_connection(call_shutdown=self._shutdown)
            self.__dict__["_intf"] = InterfaceProxy()

class STKRuntime(object):
    """Connect to STKRuntime using gRPC."""

    @staticmethod
    def start_application(grpc_host:str="localhost",
                         grpc_port:int=40704,
                         grpc_timeout_sec:int=60,
                         grpc_max_message_size:int=0,
                         user_control:bool=False,
                         no_graphics:bool=True,
                         grpc_channel_credentials:"grpc.ChannelCredentials|None"=None) -> STKRuntimeApplication:
        """
        Create a new STK Runtime instance and attach to the remote host.

        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
        user_control specifies if the application returns to the user's control
        (the application remains open) after terminating the Python API connection.
        no_graphics controls if runtime is started with or without graphics.
        grpc_channel_credentials are channel credentials to be attached to the grpc channel (most common use case: SSL credentials,
        see https://grpc.io/docs/guides/auth/ for more information).
        """
        if grpc_port < 0 or grpc_port > 65535:
            raise RuntimeError(f"{grpc_port} is not a valid port number for the gRPC server.")
        if grpc_host != "localhost":
            try:
                socket.inet_pton(socket.AF_INET, grpc_host)
            except OSError:
                try:
                    socket.inet_pton(socket.AF_INET6, grpc_host)
                except OSError:
                    raise RuntimeError(f"Could not resolve host \"{grpc_host}\" for the gRPC server.")

        cmd_line = []
        if os.name != "nt":
            ld_env = os.getenv('LD_LIBRARY_PATH')
            if ld_env:
                for path in ld_env.split(':'):
                    stkruntime_path = (pathlib.Path(path) / "stkruntime").resolve()
                    if stkruntime_path.exists():
                        cmd_line = [stkruntime_path, "--grpcHost", grpc_host, "--grpcPort", str(grpc_port)]
                        if no_graphics:
                            cmd_line.append("--noGraphics")
                        break
            else:
                raise RuntimeError("LD_LIBRARY_PATH not defined. Add STK bin directory to LD_LIBRARY_PATH before running.")
        else:
            from .internal.comutil import OLE32Lib
            if OLE32Lib.xcom_bin_dir is not None:
                stkruntime_path = pathlib.Path(OLE32Lib.xcom_bin_dir) / "STKRuntime.exe"
            else:
                clsid_stkxapplication = "{5F1B7A77-663D-44E9-99A9-2367B4F9AF6F}"
                stkx_dll_registry_value = read_registry_key(f"CLSID\\{clsid_stkxapplication}\\InprocServer32", silent_exception=True)
                stkruntime_path = None if stkx_dll_registry_value is None else pathlib.Path(stkx_dll_registry_value).parent / "STKRuntime.exe"
                if stkruntime_path is None or not stkruntime_path.exists():
                    stkruntime_path = pathlib.Path(winreg_stk_binary_dir()) / "STKRuntime.exe"
                    if not stkruntime_path.exists():
                        raise RuntimeError("Could not find STKRuntime.exe. Verify STK installation.")
            cmd_line = [str(stkruntime_path.resolve()), "/grpcHost", grpc_host, "/grpcPort", str(grpc_port)]
            if no_graphics:
                cmd_line.append("/noGraphics")

        # Calling subprocess.Popen (without shell equals true) to start the backend.
        # Excluding low severity bandit check as the validity of the inputs has been ensured.
        subprocess.Popen(cmd_line) # nosec B603
        host = grpc_host
        # Ignoring B104 warning as it is a false positive. The hard-coded string "0.0.0.0" is being filtered
        # to ensure that it is not used.
        if grpc_host=="0.0.0.0": # nosec B104
            host = "localhost"
        app = STKRuntime.attach_to_application(host, grpc_port, grpc_timeout_sec, grpc_max_message_size, grpc_channel_credentials)
        app.__dict__["_shutdown"] = not user_control
        return app


    @staticmethod
    def attach_to_application(grpc_host:str="localhost",
                            grpc_port:int=40704,
                            grpc_timeout_sec:int=60,
                            grpc_max_message_size:int=0,
                            grpc_channel_credentials:"grpc.ChannelCredentials|None"=None) -> STKRuntimeApplication:
        """
        Attach to STKRuntime.

        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
        grpc_channel_credentials are channel credentials to be attached to the grpc channel (most common use case: SSL credentials,
        see https://grpc.io/docs/guides/auth/ for more information).
        """
        client = GrpcClient.new_client(grpc_host, grpc_port, grpc_timeout_sec, grpc_max_message_size, grpc_channel_credentials)
        if client is not None:
            app_intf = client.get_stk_application_interface()
            app = STKRuntimeApplication()
            app._private_init(app_intf)
            atexit.register(app._disconnect)
            return app
        raise RuntimeError(f"Cannot connect to the gRPC server on {grpc_host}:{grpc_port}.")