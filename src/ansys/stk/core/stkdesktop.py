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

"""Starts STK Desktop or attaches to an already running STK Desktop, and provides access to the Object Model root."""

__all__ = ["STKDesktop", "STKDesktopApplication"]

import atexit
from ctypes import byref
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
from .internal.coclassutil import attach_to_stk_by_pid
from .internal.comutil import (
    CLSCTX_LOCAL_SERVER,
    CO_E_NOTINITIALIZED,
    COINIT_APARTMENTTHREADED,
    GUID,
    PVOID,
    CoInitializeManager,
    IUnknown,
    ObjectLifetimeManager,
    OLE32Lib,
    OLEAut32Lib,
    Succeeded,
)
from .internal.eventutil import EventSubscriptionManager
from .stkobjects import STKObjectModelContext, STKObjectRoot
from .uiapplication import UiApplication
from .utilities.grpcutilities import GrpcCallBatcher


class ThreadMarshaller(object):
    """Automate multiple STK instances from one Python script using threads."""
    _iid_iunknown = GUID.from_registry_format(IUnknown._guid)
    def __init__(self, obj):
        if os.name != "nt":
            raise RuntimeError("ThreadMarshaller is only available on Windows.")
        if not hasattr(obj, "_intf"):
            raise RuntimeError("Invalid object to passed to ThreadMarshaller.")
        if type(obj._intf) is not IUnknown:
            raise RuntimeError("ThreadMarshaller is not available on the gRPC API.")
        self._obj = obj
        self._obj_type = type(obj)
        self._pStream = PVOID()
        if not Succeeded(OLE32Lib.CoMarshalInterThreadInterfaceInStream(byref(ThreadMarshaller._iid_iunknown), obj._intf.p, byref(self._pStream))):
            raise RuntimeError("ThreadMarshaller failed to initialize.")

    def __del__(self):
        if self._pStream is not None:
            OLE32Lib.CoReleaseMarshalData(self._pStream)
        del(self._obj)

    def get_marshalled_to_current_thread(self) -> typing.Any:
        """Return an instance of the original stk_object that may be used on the current thread. May only be called once."""
        if self._pStream is None:
            raise RuntimeError(f"{self._obj_type} object has already been marshalled to a thread.")
        unknown_raw = PVOID()
        hr = OLE32Lib.CoGetInterfaceAndReleaseStream(self._pStream, byref(ThreadMarshaller._iid_iunknown), byref(unknown_raw))
        self._pStream = None
        if not Succeeded(hr):
            if hr == CO_E_NOTINITIALIZED:
                raise RuntimeError("Thread not initialized. Call InitializeThread() before the call to GetMarshalledToCurrentThread().")
            else:
                raise RuntimeError("Could not marshall to thread.")
        unknown = IUnknown()
        unknown.p = unknown_raw
        marshalled_obj = self._obj_type()
        marshalled_obj._private_init(unknown)
        del(unknown)
        return marshalled_obj

    def initialize_thread(self) -> None:
        """Must be called on the destination thread prior to calling GetMarshalledToCurrentThread()."""
        OLE32Lib.CoInitializeEx(None, COINIT_APARTMENTTHREADED)

    def release_thread(self) -> None:
        """Call in the destination thread after all calls to STK are finished."""
        OLE32Lib.CoUninitialize()

class STKDesktopApplication(UiApplication):
    """
    Interact with an STK Desktop application.

    Use STKDesktop.StartApplication() or STKDesktop.AttachToApplication()
    to obtain an initialized STKDesktopApplication object.
    """

    def __init__(self):
        """Construct an object of type STKDesktopApplication."""
        self.__dict__["_intf"] = InterfaceProxy()
        UiApplication.__init__(self)
        self.__dict__["_root"] = None

    def _private_init(self, intf: InterfaceProxy):
        UiApplication._private_init(self, intf)

    def __del__(self):
        """Destruct the STKDesktopApplication object after all references to the object are deleted."""
        if self._intf and type(self._intf) is IUnknown:
            CoInitializeManager.uninitialize()

    @property
    def root(self) -> STKObjectRoot:
        """Get the object model root associated with this instance of STK Desktop application."""
        if not self._intf:
            raise RuntimeError("STKDesktopApplication has not been properly initialized.  Use STKDesktop to obtain the STKDesktopApplication object.")
        if self._root is not None:
            return self._root
        if self._intf:
            self.__dict__["_root"] = self.personality2
            return self.__dict__["_root"]

    def new_object_model_context(self) -> STKObjectModelContext:
        """Create a new object model context for the STK Desktop application."""
        return self.create_object("{D45C0F17-AAB4-4D2B-A9A2-5A125F528B6B}", "")

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
        if hasattr(self._intf, "client"):
            self._intf.client.set_grpc_options(options)

    def new_grpc_call_batcher(self, max_batch:int=None, disable_batching:bool=False) -> GrpcCallBatcher:
        """
        Construct a GrpcCallBatcher linked to this gRPC client that may be used to improve API performance.

        If gRPC is not active, the batcher will be disabled.
        max_batch is the maximum number of calls to batch together.
        Set disable_batching=True to disable batching operations for this batcher.
        See grpcutilities module for more information.
        """
        if hasattr(self._intf, "client"):
            batcher = GrpcCallBatcher(disable_batching)
            batcher._private_init(self._intf.client, max_batch)
        else:
            batcher = GrpcCallBatcher(disable_batching=True)
        return batcher

    def shutdown(self) -> None:
        """Close this STK Desktop instance (or detach if the instance was obtained through STKDesktop.AttachToApplication())."""
        if self._root is not None:
            root : STKObjectRoot = self._root
            root.close_scenario()
            self.__dict__["_root"] = None
        if hasattr(self._intf, "client"):
            self.user_control = False
            self._disconnect_grpc()
        else:
            self.quit()
            self.__dict__["_intf"] = InterfaceProxy()

    def _disconnect_grpc(self) -> None:
        """Safely disconnect from STK."""
        if self._intf:
            if typing.TYPE_CHECKING:
                from .internal.grpcutil import GrpcClient
            client: GrpcClient = self._intf.client
            client.terminate_connection()
            self.__dict__["_intf"] = InterfaceProxy()


class STKDesktop(object):
    """Create, initialize, and manage STK Desktop application instances."""

    _disable_pop_ups = False

    @staticmethod
    def start_application(visible:bool=False,
                         user_control:bool=False,
                         grpc_server:bool=False,
                         grpc_host:str="localhost",
                         grpc_port:int=40704,
                         grpc_timeout_sec:int=60,
                         grpc_max_message_size:int=0,
                         grpc_channel_credentials:"grpc.ChannelCredentials|None"=None) -> STKDesktopApplication:
        """
        Create a new STK Desktop application instance.

        Specify visible = True to show the application window.
        Specify user_control = True to return the application to the user's control.
        (the application remains open) after terminating the Python API connection.
        Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
        grpc_channel_credentials are channel credentials to be attached to the grpc channel (most common use case: SSL credentials,
        see https://grpc.io/docs/guides/auth/ for more information).
        Only available on Windows.
        """
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows.")

        CoInitializeManager.initialize()
        if grpc_server:
            try:
                pass
            except ModuleNotFoundError:
                raise RuntimeError("gRPC use requires Python modules grpcio and protobuf.")
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
            clsid_stk13application = "{93AB39CF-2C16-43F9-BF8B-37228BCBCC88}"
            executable = read_registry_key(f"CLSID\\{clsid_stk13application}\\LocalServer32", silent_exception=True)
            if executable is None or not pathlib.Path(executable).exists():
                bin_dir = pathlib.Path(winreg_stk_binary_dir()).resolve()
                if bin_dir.exists():
                    executable = bin_dir / "AgUiApplication.exe"
                else:
                    raise RuntimeError("Could not find AgUiApplication.exe. Verify STK 13 installation.")
            cmd_line = [f"{executable}", "/pers", "STK", "/grpcServer", "On", "/grpcHost", grpc_host, "/grpcPort", str(grpc_port)]
            if STKDesktop._disable_pop_ups:
                cmd_line.append("/Automation")

            # Calling subprocess.Popen (without shell equals true) to start the backend.
            # Excluding low severity bandit check as the validity of the inputs has been ensured.
            subprocess.Popen(cmd_line) # nosec B603
            host = grpc_host
            # Ignoring B104 warning as it is a false positive. The hard-coded string "0.0.0.0" is being filtered
            # to ensure that it is not used.
            if grpc_host=="0.0.0.0": # nosec B104
                host = "localhost"
            app = STKDesktop.attach_to_application(None, grpc_server, host, grpc_port, grpc_timeout_sec, grpc_max_message_size, grpc_channel_credentials)
            app.visible = visible
            app.user_control = user_control
            return app
        else:
            clsid_aguiapplication = GUID()
            if Succeeded(OLE32Lib.CLSIDFromString("STK13.Application", clsid_aguiapplication)):
                unknown = IUnknown()
                iid_iunknown = GUID(IUnknown._guid)
                if Succeeded(OLE32Lib.CoCreateInstance(byref(clsid_aguiapplication), None, CLSCTX_LOCAL_SERVER, byref(iid_iunknown), byref(unknown.p))):
                    unknown.take_ownership(isApplication=True)
                    app = STKDesktopApplication()
                    app._private_init(unknown)
                    app.visible = visible
                    app.user_control = user_control
                    return app
            raise RuntimeError("Failed to create STK Desktop application.  Check for successful install and registration.")

    @staticmethod
    def attach_to_application(pid:int=None,
                            grpc_server:bool=False,
                            grpc_host:str="localhost",
                            grpc_port:int=40704,
                            grpc_timeout_sec:int=60,
                            grpc_max_message_size:int=0,
                            grpc_channel_credentials:"grpc.ChannelCredentials|None"=None) -> STKDesktopApplication:
        """
        Attach to an existing STK Desktop instance.

        Specify the Process ID (PID) in case multiple processes are open.
        Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
        grpc_channel_credentials are channel credentials to be attached to the grpc channel (most common use case: SSL credentials,
        see https://grpc.io/docs/guides/auth/ for more information).
        Only available on Windows.
        """
        if os.name != "nt" and not grpc_server:
            raise RuntimeError("STK Desktop is only available on Windows. Use grpc_server=True to attach to STK Desktop running on Windows.")

        CoInitializeManager.initialize()
        if grpc_server:
            if pid is not None:
                raise RuntimeError("Retry using either 'pid' or 'grpc_server'. Cannot initialize using both.")
            try:
                from .internal.grpcutil import GrpcClient
            except ModuleNotFoundError:
                raise RuntimeError("gRPC use requires Python modules grpcio and protobuf.")
            client: GrpcClient = GrpcClient.new_client(grpc_host, grpc_port, grpc_timeout_sec, grpc_max_message_size, grpc_channel_credentials)
            if client is not None:
                client.set_app_control_shutdown()
                app_impl = client.get_stk_application_interface()
                app = STKDesktopApplication()
                app._private_init(app_impl)
                atexit.register(app._disconnect_grpc)
                return app
            else:
                raise RuntimeError(f"Could not connect to gRPC server at {grpc_host}:{grpc_port}.")
        elif pid is None:
            clsid_aguiapplication = GUID()
            if Succeeded(OLE32Lib.CLSIDFromString("STK13.Application", clsid_aguiapplication)):
                unknown = IUnknown()
                if Succeeded(OLEAut32Lib.GetActiveObject(byref(clsid_aguiapplication), None, byref(unknown.p))):
                    unknown.take_ownership(isApplication=True)
                    app = STKDesktopApplication()
                    app._private_init(unknown)
                    return app
                else:
                    raise RuntimeError("Failed to attach to an active STK 13 Application instance.")
        else:
            unknown = attach_to_stk_by_pid(pid)
            if unknown is not None:
                app = STKDesktopApplication()
                app._private_init(unknown)
                return app
            else:
                raise RuntimeError("Failed to attach to STK with pid " + str(pid) + ".")

    @staticmethod
    def release_all() -> None:
        """
        Release all handles from Python to STK Desktop applications.

        Not applicable to gRPC connections.
        """
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows.")
        EventSubscriptionManager.unsubscribe_all()
        ObjectLifetimeManager.release_all()

    @staticmethod
    def create_thread_marshaller(stk_object:typing.Any) -> ThreadMarshaller:
        """
        Return a ThreadMarshaller instance capable of marshalling the stk_object argument to a new thread.

        Not applicable to gRPC connections.
        """
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows.")
        return ThreadMarshaller(stk_object)