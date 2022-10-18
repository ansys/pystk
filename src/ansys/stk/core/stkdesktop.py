################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################

__all__ = ["STKDesktop", "STKDesktopApplication"]

import os
from ctypes import byref

if os.name !="nt":
    raise RuntimeError("STKDesktop is only available on Windows.  Use STKEngine.")
    
from .internal.comutil       import *
from .internal.coclassutil   import attach_to_stk_by_pid
from .internal.eventutil     import EventSubscriptionManager
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
    _iid_IUnknown = GUID(IUnknown._guid)
    def __init__(self, obj):
       if not hasattr(obj, "_pUnk"):
           raise STKRuntimeError("Invalid object to passed to ThreadMarshaller.")
       self._obj = obj
       self._obj_type = type(obj)
       self._pStream = PVOID()
       if not Succeeded(CoMarshalInterThreadInterfaceInStream(byref(ThreadMarshaller._iid_IUnknown), obj._pUnk.p, byref(self._pStream))):
           raise STKRuntimeError("ThreadMarshaller failed to initialize.")
           
    def __del__(self):
        if self._pStream is not None:
            CoReleaseMarshalData(self._pStream)
        del(self._obj)
       
    def GetMarshalledToCurrentThread(self) -> typing.Any:
        """Returns an instance of the original stk_object that may be used on the current thread. May only be called once."""
        if self._pStream is None:
            raise STKRuntimeError(f"{self._obj_type} object has already been marshalled to a thread.")
        pUnk_raw = PVOID()
        hr = CoGetInterfaceAndReleaseStream(self._pStream, byref(ThreadMarshaller._iid_IUnknown), byref(pUnk_raw))
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
        
    def InitializeThread(self) -> None:
        """Must be called on the destination thread prior to calling GetMarshalledToCurrentThread()."""
        CoInitializeEx(None, COINIT_APARTMENTTHREADED)
        
    def ReleaseThread(self) -> None:
        """Call in the destination thread after all calls to STK are finished."""
        CoUninitialize()

class STKDesktopApplication(AgUiApplication):
    """
    Interact with an STK Desktop application.  Use STKDesktop.StartApplication() or 
    STKDesktop.AttachToApplication() to obtain an initialized STKDesktopApplication object.
    """
    def __init__(self):
        self.__dict__["_pUnk"] = None
        AgUiApplication.__init__(self)
        self.__dict__["_initialized"] = False
        self.__dict__["_root"] = None
        
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        AgUiApplication._private_init(self, pUnk)
        self.__dict__["_initialized"] = True
        
    def __del__(self):
        if self.__dict__["_initialized"]:
            CoInitializeManager.uninitialize()

    @property
    def Root(self) -> AgStkObjectRoot:
        """Get the object model root associated with this instance of STK Desktop application."""
        if not self.__dict__["_initialized"]:
            raise RuntimeError("STKDesktopApplication has not been properly initialized.  Use StartApplication() or AttachToApplication() to obtain the STKDesktopApplication object.")
        if self.__dict__["_root"] is not None:
            return self.__dict__["_root"]
        if self.__dict__["_pUnk"] is not None:
            self.__dict__["_root"] = self.Personality2
            return self.__dict__["_root"]
            
    def ShutDown(self) -> None:
        """Close this STK Desktop instance (or detach if the instance was obtained through STKDesktop.AttachToApplication())."""
        if self.__dict__["_pUnk"] is not None:
            if self.__dict__["_root"] is not None:
                self.__dict__["_root"].CloseScenario()
            self.Quit()
            self.__dict__["_root"] = None
            self.__dict__["_pUnk"] = None
            

class STKDesktop(object):
    """Create, initialize, and manage STK Desktop application instances."""

    @staticmethod
    def StartApplication(visible:bool=False, userControl:bool=False) -> STKDesktopApplication:
        """
        Create a new STK Desktop application instance.  
        Specify visible = True to show the application window.
        Specify userControl = True to return the application to the user's control 
        (the application remains open) after terminating the Python API connection.
        """
        CoInitializeManager.initialize()
        CLSID_AgUiApplication = GUID()
        if Succeeded(CLSIDFromString("STK12.Application", CLSID_AgUiApplication)):
            pUnk = IUnknown()
            IID_IUnknown = GUID(IUnknown._guid)
            if Succeeded(CoCreateInstance(byref(CLSID_AgUiApplication), None, CLSCTX_LOCAL_SERVER, byref(IID_IUnknown), byref(pUnk.p))):
                pUnk.TakeOwnership(isApplication=True)
                app = STKDesktopApplication()
                app._private_init(pUnk)
                app.Visible = visible
                app.UserControl = userControl
                return app
        raise STKInitializationError("Failed to create STK Desktop application.  Check for successful install and registration.")
        
    @staticmethod
    def AttachToApplication(pid:int=None) -> STKDesktopApplication:
        """
        Attach to an existing STK Desktop instance. 
        Specify the Process ID (PID) in case multiple processes are open.
        Specify userControl = True to return the application to the user's control 
        (the application remains open) after terminating the Python API connection.
        """
        CoInitializeManager.initialize()
        if pid is None:
            CLSID_AgUiApplication = GUID()
            if Succeeded(CLSIDFromString("STK12.Application", CLSID_AgUiApplication)):
                pUnk = IUnknown()
                IID_IUnknown = GUID(IUnknown._guid)
                if Succeeded(GetActiveObject(byref(CLSID_AgUiApplication), None, byref(pUnk.p))):
                    pUnk.TakeOwnership(isApplication=True)
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
    def ReleaseAll() -> None:
        """Releases all handles from Python to STK Desktop applications."""
        EventSubscriptionManager.UnsubscribeAll()
        ObjectLifetimeManager.ReleaseAll()
        
    @staticmethod
    def CreateThreadMarshaller(stk_object:typing.Any) -> ThreadMarshaller:
        """Returns a ThreadMarshaller instance capable of marshalling the stk_object argument to a new thread."""
        return ThreadMarshaller(stk_object)
       

################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################