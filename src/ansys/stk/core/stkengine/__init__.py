################################################################################
#          Copyright 2020-2020, Ansys Government Initiatives
################################################################################

__all__ = ["STKEngine", "STKEngineApplication", "STK_ENGINE_TIMER_TYPE"]

import os
import atexit
from ctypes import byref
from enum import IntEnum
from ..internal.timerutil import *

if os.name != "nt":
    from ctypes                       import CFUNCTYPE, cdll
    from ctypes.util                  import find_library

from ..internal.comutil            import CLSCTX_INPROC_SERVER, GUID
from ..internal.comutil            import OLE32Lib, CoInitializeManager, IUnknown, ObjectLifetimeManager, Succeeded
from ..internal.eventutil          import EventSubscriptionManager
from ..internal.stkxinitialization import *
from ..utilities.exceptions        import *
from ..graphics                    import *
from ..stkobjects                  import *
from ..stkobjects.astrogator       import *
from ..stkobjects.aviator          import *
from ..stkutil                     import *
from ..stkx                        import *
from ..vgt                         import *

class STK_ENGINE_TIMER_TYPE(IntEnum):
    DISABLE_TIMERS     = 1
    TKINTER_MAIN_LOOP   = 2
    INTERACTIVE_PYTHON = 3
    SIG_ALARM          = 4
    SIG_RT             = 5

class STKEngineApplication(STKXApplication):
    """
    Interact with STK Engine.

    Use STKEngine.StartApplication() to obtain an initialized STKEngineApplication object.
    """
    def __init__(self):
        STKXApplication.__init__(self)
        self.__dict__["_initialized"] = False

    def _private_init(self, pUnk:IUnknown, noGraphics):
        STKXApplication._private_init(self, pUnk)
        if os.name!="nt":
            self._stkx_intialize()
        self._stkx_intialize_timer(noGraphics)
        self.__dict__["_initialized"] = True
        
    def __del__(self):
        self.shutdown()
        
    def _stkx_intialize(self):
        CLSID_AgSTKXInitialize = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString("{3B85901D-FC82-4733-97E6-5BB25CE69379}", CLSID_AgSTKXInitialize)):
            IID_IUnknown = GUID(IUnknown._guid)
            stkxinit_unk = IUnknown()
            if Succeeded(OLE32Lib.CoCreateInstance(byref(CLSID_AgSTKXInitialize), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(stkxinit_unk.p))):
                stkxinit_unk.take_ownership()
                pInit = STKXInitialize()
                pInit._private_init(stkxinit_unk)
                install_dir = os.getenv("STK_INSTALL_DIR")
                if install_dir is None:
                    raise STKInitializationError("Please set a valid STK_INSTALL_DIR environment variable.")
                config_dir = os.getenv("STK_CONFIG_DIR")
                if config_dir is None:
                    raise STKInitializationError("Please set a valid STK_CONFIG_DIR environment variable.")
                pInit.initialize_data(install_dir, config_dir)
                
    @staticmethod
    def _get_signo(sigrtmin_offset):
        if os.name=="nt":
            return None
        libc = cdll.LoadLibrary(find_library("c"))
        __libc_current_sigrtmin = CFUNCTYPE(c_int)(("__libc_current_sigrtmin", libc))
        return __libc_current_sigrtmin() + sigrtmin_offset
        
    def _set_timer_type_from_env(self):
        timer_type = int(os.getenv("STK_PYTHONAPI_TIMERTYPE", "4"))
        if os.name=="nt" or timer_type == STK_ENGINE_TIMER_TYPE.DISABLE_TIMERS:
            self.__dict__["_timer_impl"] = NullTimer()
        elif timer_type == STK_ENGINE_TIMER_TYPE.TKINTER_MAIN_LOOP or timer_type == STK_ENGINE_TIMER_TYPE.INTERACTIVE_PYTHON:
            self.__dict__["_timer_impl"] = TclTimer()
        elif timer_type == STK_ENGINE_TIMER_TYPE.SIG_ALARM:
            self.__dict__["_timer_impl"] = SigAlarmTimer()
        elif timer_type == STK_ENGINE_TIMER_TYPE.SIG_RT:
            sigrtmin_offset = int(os.getenv("STK_PYTHONAPI_TIMERTYPE5_SIGRTMIN_OFFSET", "0"))
            signo = STKEngineApplication._get_signo(sigrtmin_offset)
            self.__dict__["_timer_impl"] = SigRtTimer(signo)
            
    def _user_override_timer_type(self) -> bool:
        return ("STK_PYTHONAPI_TIMERTYPE" in os.environ)
                
    def _stkx_intialize_timer(self, noGraphics):
        if os.name=="nt":
            #Timers are not implemented on Windows, use a placeholder.
            self.__dict__["_timer_impl"] = NullTimer()
        elif noGraphics:
            self._set_timer_type_from_env()
        else:
            #default to Tkinter mainloop in graphics applications, but allow the user to override
            #e.g. if controls are not being used, the SIG_ALARM timer might be desired.
            if self._user_override_timer_type():
                self._set_timer_type_from_env()
            else:
                self.__dict__["_timer_impl"] = TclTimer()
        
    def new_object_root(self) -> StkObjectRoot:
        """Create a new object model root for the STK Engine application."""
        if not self.__dict__["_initialized"]:
            raise RuntimeError("STKEngineApplication has not been properly initialized.  Use StartApplication() to obtain the STKEngineApplication object.")
        CLSID_AgStkObjectRoot = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString("{96C1CE4E-C61D-4657-99CB-8581E12693FE}", CLSID_AgStkObjectRoot)):
            IID_IUnknown = GUID(IUnknown._guid)
            root_unk = IUnknown()
            OLE32Lib.CoCreateInstance(byref(CLSID_AgStkObjectRoot), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(root_unk.p))
            root_unk.take_ownership()
            root = StkObjectRoot()
            root._private_init(root_unk)
            return root

    def new_object_model_context(self) -> StkObjectModelContext:
        """Create a new object model context for the STK Engine application."""
        if not self.__dict__['_initialized']:
            raise RuntimeError('STKEngineApplication has not been properly initialized.  Use StartApplication() to obtain the STKEngineApplication object.')
        CLSID_AgStkObjectModelContext = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString('{7A12879C-5018-4433-8415-5DB250AFBAF9}', CLSID_AgStkObjectModelContext)):
            IID_IUnknown = GUID(IUnknown._guid)
            context_unk = IUnknown()
            OLE32Lib.CoCreateInstance(byref(CLSID_AgStkObjectModelContext), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(context_unk.p))
            context_unk.take_ownership()
            context = StkObjectModelContext()
            context._private_init(context_unk)
            return context

    def shutdown(self) -> None:
        """Shut down the STK Engine application."""
        if self._initialized:
            EventSubscriptionManager.unsubscribe_all()
            self._timer_impl.Terminate()
            ObjectLifetimeManager.ReleaseAll(releaseApplication=False)
            self.terminate()
            ObjectLifetimeManager.ReleaseAll(releaseApplication=True)
            CoInitializeManager.uninitialize()
            self.__dict__["_initialized"] = False


class STKEngine(object):
    """Initialize and manage the STK Engine application."""
    _is_engine_running = False
            
    @staticmethod
    def _init_x11(noGraphics):
        if noGraphics or os.name=="nt":
            return
        try:
            x11lib = cdll.LoadLibrary(find_library("X11"))
            XInitThreads = CFUNCTYPE(None)(("XInitThreads", x11lib))
            XInitThreads()
        except:
            raise STKRuntimeError("Failed attempting to run graphics mode without X11.")
            
    @staticmethod
    def start_application(noGraphics:bool=True) -> STKEngineApplication:
        """
        Initialize STK Engine in-process and return the instance.

        Must only be used once per Python process.
        """
        if STKEngine._is_engine_running:
            raise RuntimeError("Only one STKEngine instance is allowed per Python process.")
        CoInitializeManager.initialize()
        CLSID_AgSTKXApplication = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString("{062AB565-B121-45B5-A9A9-B412CEFAB6A9}", CLSID_AgSTKXApplication)):
            pUnk = IUnknown()
            IID_IUnknown = GUID(IUnknown._guid)
            if Succeeded(OLE32Lib.CoCreateInstance(byref(CLSID_AgSTKXApplication), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(pUnk.p))):
                pUnk.take_ownership(isApplication=True)
                STKEngine._is_engine_running = True
                STKEngine._init_x11(noGraphics)
                engine = STKEngineApplication()
                engine._private_init(pUnk, noGraphics)
                engine.no_graphics = noGraphics
                atexit.register(engine.shutdown)
                return engine
        raise STKInitializationError("Failed to create STK Engine application.  Check for successful install and registration.")
       
################################################################################
#          Copyright 2020-2020, Ansys Government Initiatives
################################################################################
