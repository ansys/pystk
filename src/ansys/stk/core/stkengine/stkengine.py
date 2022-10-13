################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################

__all__ = ["STKEngine", "STKEngineApplication", "STKEngineTimerType"]

import os
from ctypes import byref
from enum import IntEnum
from agi.stk12.internal.timerutil import *

if os.name != "nt":
    from ctypes                       import CFUNCTYPE, cdll
    from ctypes.util                  import find_library

from agi.stk12.internal.comutil            import CLSCTX_INPROC_SERVER, COINIT_APARTMENTTHREADED, GUID
from agi.stk12.internal.comutil            import CLSIDFromString, CoCreateInstance, CoInitializeManager, IUnknown, ObjectLifetimeManager, Succeeded
from agi.stk12.internal.eventutil          import EventSubscriptionManager
from agi.stk12.internal.stkxinitialization import *
from agi.stk12.utilities.exceptions        import *
from agi.stk12.graphics                    import *
from agi.stk12.stkobjects                  import *
from agi.stk12.stkobjects.astrogator       import *
from agi.stk12.stkobjects.aviator          import *
from agi.stk12.stkutil                     import *
from agi.stk12.stkx                        import *
from agi.stk12.vgt                         import *

class STKEngineTimerType(IntEnum):
    DisableTimers     = 1
    TkinterMainloop   = 2
    InteractivePython = 3
    SigAlarm          = 4
    SigRt             = 5

class STKEngineApplication(AgSTKXApplication):
    """
    Interact with STK Engine.
    Use STKEngine.StartApplication() to obtain an initialized STKEngineApplication object.
    """
    def __init__(self):
        AgSTKXApplication.__init__(self)
        self.__dict__["_stk_install_dir"] = None
        self.__dict__["_stk_config_dir"] = None
        self.__dict__["_initialized"] = False

    def _private_init(self, pUnk:IUnknown, stk_install_dir, stk_config_dir, noGraphics):
        AgSTKXApplication._private_init(self, pUnk)
        self.__dict__["_stk_install_dir"] = stk_install_dir
        self.__dict__["_stk_config_dir"] = stk_config_dir
        self._STKXInitialize()
        self._STKXInitializeTimer(noGraphics)
        self.__dict__["_initialized"] = True
        
    def __del__(self):
        self.ShutDown()
        
    def _STKXInitialize(self):
        if os.name=="nt":
            return
        CLSID_AgSTKXInitialize = GUID()
        if Succeeded(CLSIDFromString("{3B85901D-FC82-4733-97E6-5BB25CE69379}", CLSID_AgSTKXInitialize)):
            IID_IUnknown = GUID(IUnknown._guid)
            stkxinit_unk = IUnknown()
            if Succeeded(CoCreateInstance(byref(CLSID_AgSTKXInitialize), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(stkxinit_unk.p))):
                stkxinit_unk.TakeOwnership()
                pInit = IAgSTKXInitialize()
                pInit._private_init(stkxinit_unk)
                install_dir = self.__dict__["_stk_install_dir"] if self.__dict__["_stk_install_dir"] is not None else os.getenv("STK_INSTALL_DIR")
                if install_dir is None:
                    raise STKInitializationError("Please set a valid STK_INSTALL_DIR environment variable.")
                config_dir = self.__dict__["_stk_config_dir"] if self.__dict__["_stk_config_dir"] is not None else os.getenv("STK_CONFIG_DIR")
                if config_dir is None:
                    raise STKInitializationError("Please set a valid STK_CONFIG_DIR environment variable.")
                pInit.InitializeData(install_dir, config_dir)
                
    @staticmethod
    def _get_signo(sigrtmin_offset):
        if os.name=="nt":
            return None
        libc = cdll.LoadLibrary(find_library("c"))
        __libc_current_sigrtmin = CFUNCTYPE(c_int)(("__libc_current_sigrtmin", libc))
        return __libc_current_sigrtmin() + sigrtmin_offset
        
    def _set_timer_type_from_env(self):
        timer_type = int(os.getenv("STK_PYTHONAPI_TIMERTYPE", "4"))
        if os.name=="nt" or timer_type == STKEngineTimerType.DisableTimers:
            self.__dict__["_timer_impl"] = NullTimer()
        elif timer_type == STKEngineTimerType.TkinterMainloop or timer_type == STKEngineTimerType.InteractivePython:
            self.__dict__["_timer_impl"] = TclTimer()
        elif timer_type == STKEngineTimerType.SigAlarm:
            self.__dict__["_timer_impl"] = SigAlarmTimer()
        elif timer_type == STKEngineTimerType.SigRt:
            sigrtmin_offset = int(os.getenv("STK_PYTHONAPI_TIMERTYPE5_SIGRTMIN_OFFSET", "0"))
            signo = STKEngineApplication._get_signo(sigrtmin_offset)
            self.__dict__["_timer_impl"] = SigRtTimer(signo)
            
    def _user_override_timer_type(self) -> bool:
        return ("STK_PYTHONAPI_TIMERTYPE" in os.environ)
                
    def _STKXInitializeTimer(self, noGraphics):
        if os.name=="nt":
            #Timers are not implemented on Windows, use a placeholder.
            self.__dict__["_timer_impl"] = NullTimer()
        elif noGraphics:
            self._set_timer_type_from_env()
        else:
            #default to Tkinter mainloop in graphics applications, but allow the user to override
            #e.g. if controls are not being used, the SigAlarm timer might be desired.
            if self._user_override_timer_type():
                self._set_timer_type_from_env()
            else:
                self.__dict__["_timer_impl"] = TclTimer()
        
    def NewObjectRoot(self) -> AgStkObjectRoot:
        """Create a new object model root for the STK Engine application."""
        if not self.__dict__["_initialized"]:
            raise RuntimeError("STKEngineApplication has not been properly initialized.  Use StartApplication() to obtain the STKEngineApplication object.")
        CLSID_AgStkObjectRoot = GUID()
        if Succeeded(CLSIDFromString("{96C1CE4E-C61D-4657-99CB-8581E12693FE}", CLSID_AgStkObjectRoot)):
            IID_IUnknown = GUID(IUnknown._guid)
            root_unk = IUnknown()
            CoCreateInstance(byref(CLSID_AgStkObjectRoot), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(root_unk.p))
            root_unk.TakeOwnership()
            root = AgStkObjectRoot()
            root._private_init(root_unk)
            return root

    def ShutDown(self) -> None:
        """Shut down the STK Engine application."""
        if self._initialized:
            EventSubscriptionManager.UnsubscribeAll()
            self._timer_impl.Terminate()
            ObjectLifetimeManager.ReleaseAll(releaseApplication=False)
            self.Terminate()
            ObjectLifetimeManager.ReleaseAll(releaseApplication=True)
            CoInitializeManager.uninitialize()
            self.__dict__["_initialized"] = False


class STKEngine(object):
    """Initialize and manage the STK Engine application."""
    _is_engine_running = False
    _stk_config_dir = None
    _stk_install_dir = None
            
    @staticmethod
    def _initX11(noGraphics):
        if noGraphics or os.name=="nt":
            return
        try:
            x11lib = cdll.LoadLibrary(find_library("X11"))
            XInitThreads = CFUNCTYPE(None)(("XInitThreads", x11lib))
            XInitThreads()
        except:
            raise STKRuntimeError("Failed attempting to run graphics mode without X11.")
            
    @staticmethod
    def StartApplication(noGraphics:bool=True) -> STKEngineApplication:
        """
        Initialize STK Engine in-process and return the instance.
        Must only be used once per Python process.
        """
        if STKEngine._is_engine_running:
            raise RuntimeError("Only one STKEngine instance is allowed per Python process.")
        CoInitializeManager.initialize()
        CLSID_AgSTKXApplication = GUID()
        if Succeeded(CLSIDFromString("{062AB565-B121-45B5-A9A9-B412CEFAB6A9}", CLSID_AgSTKXApplication)):
            pUnk = IUnknown()
            IID_IUnknown = GUID(IUnknown._guid)
            if Succeeded(CoCreateInstance(byref(CLSID_AgSTKXApplication), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(pUnk.p))):
                pUnk.TakeOwnership(isApplication=True)
                STKEngine._is_engine_running = True
                STKEngine._initX11(noGraphics)
                engine = STKEngineApplication()
                engine._private_init(pUnk, STKEngine._stk_install_dir, STKEngine._stk_config_dir, noGraphics)
                engine.NoGraphics = noGraphics
                return engine
        raise STKInitializationError("Failed to create STK Engine application.  Check for successful install and registration.")
                
    if os.name != "nt":
        @staticmethod
        def SetSTKInstallDir(stkInstallDir:str) -> None:
            """
            Setting the install directory using this method will override the STK_INSTALL_DIR environment variable.
            If this method is not called, STK_INSTALL_DIR will be used instead.  This method must be called before
            StartApplication().
            """
            STKEngine._stk_install_dir = stkInstallDir
            
        @staticmethod
        def SetSTKConfigDir(stkConfigDir:str) -> None:
            """
            Setting the config directory using this method will override the STK_CONFIG_DIR environment variable.
            If this method is not called, STK_CONFIG_DIR will be used instead.  This method must be called before
            StartApplication().
            """
            STKEngine._stk_config_dir = stkConfigDir
        
       
################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
