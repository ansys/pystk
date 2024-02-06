################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################

"""Starts STK Desktop or attaches to an already running STK Desktop, and provides access to the Object Model root."""

__all__ = ["STKDesktop", "STKDesktopApplication"]

import os
import typing
import atexit
from ctypes import byref
import subprocess
if os.name == "nt":
    import winreg

from .internal.comutil       import (OLE32Lib, OLEAut32Lib, GUID, IUnknown, CoInitializeManager, Succeeded,
                                 CLSCTX_LOCAL_SERVER, ObjectLifetimeManager, PVOID, COINIT_APARTMENTTHREADED)
from .internal.coclassutil   import attach_to_stk_by_pid
from .internal.eventutil     import EventSubscriptionManager
from .internal.apiutil       import InterfaceProxy
from .utilities.exceptions   import *
from .graphics               import *
from .stkobjects             import *
from .stkobjects.astrogator  import *
from .stkobjects.aviator     import *
from .stkutil                import *
from .uiapplication          import *
from .uicore                 import *
from .vgt                    import *

class ThreadMarshaller(object):
    _iid_IUnknown = GUID.from_registry_format(IUnknown._guid)
    def __init__(self, obj):
        if os.name != "nt":
            raise RuntimeError("ThreadMarshaller is only available on Windows.")
        if not hasattr(obj, "_intf"):
            raise STKRuntimeError("Invalid object to passed to ThreadMarshaller.")
        if type(obj._intf) != IUnknown:
            raise STKRuntimeError("ThreadMarshaller is not available on the gRPC API.")
        self._obj = obj
        self._obj_type = type(obj)
        self._pStream = PVOID()
        if not Succeeded(OLE32Lib.CoMarshalInterThreadInterfaceInStream(byref(ThreadMarshaller._iid_IUnknown), obj._intf.p, byref(self._pStream))):
            raise STKRuntimeError("ThreadMarshaller failed to initialize.")
           
    def __del__(self):
        if self._pStream is not None:
            OLE32Lib.CoReleaseMarshalData(self._pStream)
        del(self._obj)
       
    def get_marshalled_to_current_thread(self) -> typing.Any:
        """Return an instance of the original stk_object that may be used on the current thread. May only be called once."""
        if self._pStream is None:
            raise STKRuntimeError(f"{self._obj_type} object has already been marshalled to a thread.")
        pUnk_raw = PVOID()
        hr = OLE32Lib.CoGetInterfaceAndReleaseStream(self._pStream, byref(ThreadMarshaller._iid_IUnknown), byref(pUnk_raw))
        self._pStream = None
        if not Succeeded(hr):
            if hr == CO_E_NOTINITIALIZED:
                raise STKRuntimeError("Thread not initialized. Call InitializeThread() before the call to GetMarshalledToCurrentThread().")
            else:
                raise STKRuntimeError("Could not marshall to thread.")
        pUnk = IUnknown()
        pUnk.p = pUnk_raw
        marshalled_obj = self._obj_type()
        marshalled_obj._private_init(pUnk)
        del(pUnk)
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
        if os.name != "nt":
            raise RuntimeError("STKDesktopApplication is only available on Windows. Use STKEngine.")
        self.__dict__["_intf"] = InterfaceProxy()
        UiApplication.__init__(self)
        self.__dict__["_root"] = None
        
    def _private_init(self, intf: InterfaceProxy):
        UiApplication._private_init(self, intf)
        
    def __del__(self):
        if self._intf and type(self._intf) == IUnknown:
            CoInitializeManager.uninitialize()

    @property
    def root(self) -> StkObjectRoot:
        """Get the object model root associated with this instance of STK Desktop application."""
        if not self._intf:
            raise RuntimeError("STKDesktopApplication has not been properly initialized.  Use STKDesktop to obtain the STKDesktopApplication object.")
        if self._root is not None:
            return self._root
        if self._intf:
            self.__dict__["_root"] = self.personality2
            return self.__dict__["_root"]
            
    def new_object_model_context(self) -> StkObjectModelContext:
        '''Create a new object model context for the STK Desktop application.'''
        return self.create_object("{7A12879C-5018-4433-8415-5DB250AFBAF9}", "")
    
    def shutdown(self) -> None:
        """Close this STK Desktop instance (or detach if the instance was obtained through STKDesktop.AttachToApplication())."""
        if self._root is not None:
            assert(isinstance(self._root, StkObjectRoot))
            self._root.close_scenario()
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
            self._intf.client.TerminateConnection()
            self.__dict__["_intf"] = InterfaceProxy()


class STKDesktop(object):
    """Create, initialize, and manage STK Desktop application instances."""
    
    @staticmethod
    def _read_registry_key(root, key, value=None, silent_exception=False):
        try:
            with winreg.OpenKey(root, key) as hkey:
                (val, typ) = winreg.QueryValueEx(hkey, value)
            return val
        except Exception as e:
            if not silent_exception:
                raise STKInitializationError(f"Error Reading Registry for {key}: {e}")
            return None

    @staticmethod
    def start_application(visible:bool=False, \
                         userControl:bool=False, \
                         grpc_server:bool=False, \
                         grpc_host:str="0.0.0.0", \
                         grpc_port:int=40704, \
                         grpc_timeout_sec:int=60, \
                         grpc_desktop_options:str="") -> STKDesktopApplication:
        """
        Create a new STK Desktop application instance.  

        Specify visible = True to show the application window.
        Specify userControl = True to return the application to the user's control .
        (the application remains open) after terminating the Python API connection.
        Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        grpc_desktop_options passes extra command line options to UiApplication.
        Only available on Windows.
        """
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")

        CoInitializeManager.initialize()
        if grpc_server:
            try:
                pass
            except ModuleNotFoundError:
                raise STKInitializationError(f"gRPC use requires Python modules grpcio and protobuf.")
            executable = STKDesktop._read_registry_key(winreg.HKEY_CLASSES_ROOT, 'CLSID\{7ADA6C22-FA34-4578-8BE8-65405A55EE15}\LocalServer32')
            cmd_line = f"{executable} /pers STK /grpcServer On /grpcHost {grpc_host} /grpcPort {grpc_port} {grpc_desktop_options}"
            app_process = subprocess.Popen(cmd_line)
            host = "localhost" if grpc_host=="0.0.0.0" else grpc_host
            app = STKDesktop.attach_to_application(None, grpc_server, host, grpc_port, grpc_timeout_sec)
            app.visible = visible
            app.user_control = userControl
            return app
        else:
            CLSID_AgUiApplication = GUID()
            if Succeeded(OLE32Lib.CLSIDFromString("STK12.Application", CLSID_AgUiApplication)):
                pUnk = IUnknown()
                IID_IUnknown = GUID(IUnknown._guid)
                if Succeeded(OLE32Lib.CoCreateInstance(byref(CLSID_AgUiApplication), None, CLSCTX_LOCAL_SERVER, byref(IID_IUnknown), byref(pUnk.p))):
                    pUnk.take_ownership(isApplication=True)
                    app = STKDesktopApplication()
                    app._private_init(pUnk)
                    app.visible = visible
                    app.user_control = userControl
                    return app
            raise STKInitializationError("Failed to create STK Desktop application.  Check for successful install and registration.")
        
    @staticmethod
    def attach_to_application(pid:int=None, \
                            grpc_server:bool=False, \
                            grpc_host:str="localhost", \
                            grpc_port:int=40704, \
                            grpc_timeout_sec:int=60) -> STKDesktopApplication:
        """
        Attach to an existing STK Desktop instance. 

        Specify the Process ID (PID) in case multiple processes are open.
        Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        Only available on Windows.
        """
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")

        CoInitializeManager.initialize()
        if grpc_server:
            if pid is not None:
                raise STKInitializationError(f"Retry using either 'pid' or 'grpc_server'. Cannot initialize using both.")
            try:
                from .internal.grpcutil import GrpcClient
            except ModuleNotFoundError:
                raise STKInitializationError(f"gRPC use requires Python modules grpcio and protobuf.")
            client = GrpcClient.new_client(grpc_host, grpc_port, grpc_timeout_sec)
            if client is not None:
                pAppImpl = client.get_stk_application_interface()
                app = STKDesktopApplication()
                app._private_init(pAppImpl)
                atexit.register(app._disconnect_grpc)
                return app
            else:
                raise STKInitializationError(f"Could not connect to gRPC server at {grpc_host}:{grpc_port}.")
        elif pid is None:
            CLSID_AgUiApplication = GUID()
            if Succeeded(OLE32Lib.CLSIDFromString("STK12.Application", CLSID_AgUiApplication)):
                pUnk = IUnknown()
                IID_IUnknown = GUID(IUnknown._guid)
                if Succeeded(OLEAut32Lib.GetActiveObject(byref(CLSID_AgUiApplication), None, byref(pUnk.p))):
                    pUnk.take_ownership(isApplication=True)
                    app = STKDesktopApplication()
                    app._private_init(pUnk)
                    return app
                else:
                    raise STKInitializationError("Failed to attach to an active STK 12 Application instance.")
        else:
            pUnk = attach_to_stk_by_pid(pid)
            if pUnk is not None: 
                app = STKDesktopApplication()
                app._private_init(pUnk)
                return app
            else:
                raise STKInitializationError("Failed to attach to STK with pid " + str(pid) + ".")

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


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################