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

from .internal.apiutil import InterfaceProxy, read_registry_key, winreg_stk_binary_dir
from .internal.grpcutil import GrpcClient
from .stkobjects import STKObjectModelContext, STKObjectRoot
from .stkx import STKXApplication
from .utilities.exceptions import STKInitializationError
from .utilities.grpcutilities import (
    GrpcAuthenticationMode,
    GrpcCallBatcher,
    _get_authentication_mode_string,
    _validate_authentication_mode,
)


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
        raise STKInitializationError("Not connected to the gRPC server.")

    def new_object_model_context(self) -> STKObjectModelContext:
        """May be used to obtain an Object Model Context from a running STK Engine application."""
        if self._intf:
            client: GrpcClient = self._intf.client
            context_unk = client.new_object_model_context()
            context = STKObjectModelContext()
            context._private_init(context_unk)
            return context
        raise STKInitializationError("Not connected to the gRPC server.")

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
    def start_application(grpc_host:str="127.0.0.1",
                         grpc_port:int=40704,
                         grpc_timeout_sec:int=60,
                         grpc_max_message_size:int=0,
                         user_control:bool=False,
                         no_graphics:bool=True,
                         grpc_allow_remote_host:bool=False,
                         grpc_server_cert:str=None,
                         grpc_server_key:str=None,
                         grpc_client_cert:str=None,
                         grpc_client_key:str=None,
                         grpc_ca:str=None,
                         grpc_uds_directory:str=None,
                         grpc_uds_id:str=None,
                         grpc_authentication_mode:GrpcAuthenticationMode=GrpcAuthenticationMode.DEFAULT) -> STKRuntimeApplication:
        """
        Create a new STK Runtime instance and attach to the remote host.

        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
        user_control specifies if the application returns to the user's control
        (the application remains open) after terminating the Python API connection.
        no_graphics controls if runtime is started with or without graphics.
        Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or
            other remote address as the grpc_host.
        grpc_server_cert is the path to the server certificate file. Required for mTLS authentication.
        grpc_server_key is the path to the server key file. Required for mTLS authentication.
        grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
        grpc_client_key is the path to the client key file. Required for mTLS authentication.
        grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
        grpc_uds_directory is an optional override of the path to the directory for UDS socket files. Only supported on Linux.
        grpc_uds_id is the optional ID for UDS socket file naming (stk-runtime-grpc<-id>.sock). Only supported on Linux.
        grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER on Windows,
            UNIX_DOMAIN_SOCKET on Linux.
        """
        if grpc_port < 0 or grpc_port > 65535:
            raise STKInitializationError(f"{grpc_port} is not a valid port number for the gRPC server.")
        if grpc_host not in ["localhost", "127.0.0.1"]:
            if not grpc_allow_remote_host:
                raise RuntimeError("Remote host connections are not allowed. Use grpc_allow_remote_host to enable.")
            try:
                socket.inet_pton(socket.AF_INET, grpc_host)
            except OSError:
                try:
                    socket.inet_pton(socket.AF_INET6, grpc_host)
                except OSError:
                    raise STKInitializationError(f"Could not resolve host \"{grpc_host}\" for the gRPC server.")

        _validate_authentication_mode(grpc_authentication_mode, grpc_host)

        cmd_line = []
        if os.name != "nt":
            ld_env = os.getenv('LD_LIBRARY_PATH')
            if ld_env:
                for path in ld_env.split(':'):
                    stkruntime_path = (pathlib.Path(path) / "stkruntime").resolve()
                    if stkruntime_path.exists():
                        cmd_line = [stkruntime_path]
                        if any([grpc_uds_directory, grpc_uds_id]):
                            if grpc_uds_directory:
                                cmd_line.extend(["--grpcUdsDir", grpc_uds_directory])
                            if grpc_uds_id:
                                cmd_line.extend(["--grpcUdsId", grpc_uds_id])
                        else:
                            cmd_line.extend(["--grpcHost", grpc_host, "--grpcPort", str(grpc_port)])
                        break
            else:
                raise STKInitializationError("LD_LIBRARY_PATH not defined. Add STK bin directory to LD_LIBRARY_PATH before running.")
        else:
            clsid_stkxapplication = "{062AB565-B121-45B5-A9A9-B412CEFAB6A9}"
            stkx_dll_registry_value = read_registry_key(f"CLSID\\{clsid_stkxapplication}\\InprocServer32", silent_exception=True)
            stkruntime_path = None if stkx_dll_registry_value is None else pathlib.Path(stkx_dll_registry_value).parent / "STKRuntime.exe"
            if stkruntime_path is None or not stkruntime_path.exists():
                stkruntime_path = pathlib.Path(winreg_stk_binary_dir()) / "STKRuntime.exe"
                if not stkruntime_path.exists():
                    raise STKInitializationError("Could not find STKRuntime.exe. Verify STK installation.")
            cmd_line = [str(stkruntime_path.resolve()), "/grpcHost", grpc_host, "/grpcPort", str(grpc_port)]

        flag = '--' if os.name != 'nt' else '/'
        cmd_line.extend([f"{flag}grpcAuthMode", _get_authentication_mode_string(grpc_authentication_mode)])
        if grpc_server_cert:
            cmd_line.extend([f"{flag}grpcServerCert", str(pathlib.Path(grpc_server_cert).resolve())])
        if grpc_server_key:
            cmd_line.extend([f"{flag}grpcServerKey", str(pathlib.Path(grpc_server_key).resolve())])
        if grpc_ca:
            cmd_line.extend([f"{flag}grpcCa", str(pathlib.Path(grpc_ca).resolve())])
        if grpc_allow_remote_host:
            cmd_line.append(f"{flag}grpcAllowRemoteHost")
        if no_graphics:
            cmd_line.append(f"{flag}noGraphics")

        # Calling subprocess.Popen (without shell equals true) to start the backend.
        # Excluding low severity bandit check as the validity of the inputs has been ensured.
        p = subprocess.Popen(cmd_line) # nosec B603
        host = grpc_host
        # Ignoring B104 warning as it is a false positive. The hard-coded string "0.0.0.0" is being filtered
        # to ensure that it is not used.
        if grpc_host=="0.0.0.0": # nosec B104
            host = "127.0.0.1"
        try:
            app = STKRuntime.attach_to_application(host,
                                                 grpc_port,
                                                 grpc_timeout_sec,
                                                 grpc_max_message_size,
                                                 grpc_allow_remote_host,
                                                 grpc_client_cert,
                                                 grpc_client_key,
                                                 grpc_ca,
                                                 grpc_uds_directory,
                                                 grpc_uds_id,
                                                 grpc_authentication_mode)

            app.__dict__["_shutdown"] = not user_control
            return app
        except Exception:
            if not user_control:
                p.terminate()
            raise


    @staticmethod
    def attach_to_application(grpc_host:str="127.0.0.1",
                            grpc_port:int=40704,
                            grpc_timeout_sec:int=60,
                            grpc_max_message_size:int=0,
                            grpc_allow_remote_host:bool=False,
                            grpc_client_cert:str=None,
                            grpc_client_key:str=None,
                            grpc_ca:str=None,
                            grpc_uds_directory:str=None,
                            grpc_uds_id:str=None,
                            grpc_authentication_mode:GrpcAuthenticationMode=GrpcAuthenticationMode.DEFAULT) -> STKRuntimeApplication:
        """
        Attach to STKRuntime.

        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
        Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or
            other remote address as the grpc_host.
        grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
        grpc_client_key is the path to the client key file. Required for mTLS authentication.
        grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
        grpc_uds_directory is an optional override of the path to the directory for UDS socket files. Only supported on Linux.
        grpc_uds_id is the optional ID for UDS socket file naming (stk-runtime-grpc<-id>.sock). Only supported on Linux.
        grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER on Windows,
            UNIX_DOMAIN_SOCKET on Linux.
        """
        if grpc_host not in ["localhost", "127.0.0.1"] and not grpc_allow_remote_host:
            raise RuntimeError("Remote host connections are not allowed. Use grpc_allow_remote_host to enable.")

        _validate_authentication_mode(grpc_authentication_mode, grpc_host)

        if grpc_authentication_mode != GrpcAuthenticationMode.UNIX_DOMAIN_SOCKET and any([grpc_uds_directory, grpc_uds_id]):
            raise RuntimeError("grpc_authentication_mode must be set to UNIX_DOMAIN_SOCKET if UDS parameters are provided.")
        elif grpc_authentication_mode != GrpcAuthenticationMode.MUTUAL_TLS and any([grpc_client_cert, grpc_client_key, grpc_ca]):
            raise RuntimeError("grpc_authentication_mode must be set to MUTUAL_TLS if mutual TLS parameters are provided.")

        if grpc_authentication_mode == GrpcAuthenticationMode.UNIX_DOMAIN_SOCKET:
            if grpc_uds_directory:
                grpc_uds_directory = pathlib.Path(grpc_uds_directory).resolve()
            else:
                config_dir = os.getenv("STK_CONFIG_DIR")
                if config_dir:
                    grpc_uds_directory = (pathlib.Path(config_dir) / "STK12" / "Config" / ".conn").resolve()
                else:
                    raise RuntimeError("Please provide a value for grpc_uds_directory or set a valid STK_CONFIG_DIR " /
                                       "environment variable to use the default UDS directory.")

        client: GrpcClient = GrpcClient.new_client(grpc_host,
                                                   grpc_port,
                                                   grpc_timeout_sec,
                                                   grpc_max_message_size,
                                                   _get_authentication_mode_string(grpc_authentication_mode),
                                                   grpc_client_cert,
                                                   grpc_client_key,
                                                   grpc_ca,
                                                   grpc_uds_directory,
                                                   grpc_uds_id)

        if client is not None:
            app_intf = client.get_stk_application_interface()
            app = STKRuntimeApplication()
            app._private_init(app_intf)
            atexit.register(app._disconnect)
            return app
        raise STKInitializationError(f"Cannot connect to the gRPC server on {grpc_host}:{grpc_port}.")