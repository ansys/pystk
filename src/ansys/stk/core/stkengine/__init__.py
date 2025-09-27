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

"""Starts STK Engine and provides access to the Object Model root."""

__all__ = ["STKEngine", "STKEngineApplication", "STKEngineTimerType"]

import atexit
from ctypes import byref
from enum import IntEnum
import os

if os.name != "nt":
    from ctypes import CFUNCTYPE, cdll
    from ctypes.util import find_library

    from ..internal.timerutil import NullTimer, SigAlarmTimer, SigRtTimer, TclTimer
else:
    from ..internal.timerutil import NullTimer

from ..internal.comutil import (
    CLSCTX_INPROC_SERVER,
    GUID,
    CoInitializeManager,
    IUnknown,
    ObjectLifetimeManager,
    OLE32Lib,
    Succeeded,
)
from ..internal.eventutil import EventSubscriptionManager
from ..internal.stkxinitialization import STKXInitialize
from ..stkobjects import STKObjectModelContext, STKObjectRoot
from ..stkx import STKXApplication, STKXApplicationPartnerAccess
from ..utilities.grpcutilities import GrpcCallBatcher


class STKEngineTimerType(IntEnum):
    """
    Specify the timer implementation to use.

    Timers are needed for events on Linux applications.
    May be overridden by specifying environment variable STK_PYTHONAPI_TIMERTYPE.
    """

    DISABLE_TIMERS     = 1
    """Disable timers. This option is always selected on Windows applications."""
    TKINTER_MAIN_LOOP   = 2
    """Tkinter TCL timer dependent on the tkinter main loop. Default for tkinter applications."""
    INTERACTIVE_PYTHON = 3
    """Tkinter TCL timer dependent on the interactive Python environment. Default for interactive Python applications."""
    SIG_ALARM          = 4
    """Use the standard signal SIGALRM for timer notifications. Default when not using tkinter or interactice Python."""
    SIG_RT             = 5
    """Use a real-time signal for timer notifications. Default signal is SIGRTMIN. May be overridden by specifying environment variable STK_PYHONAPI_TIMERTYPE5_SIGRTMIN_OFFSET."""

class STKEngineApplication(STKXApplication):
    """
    Interact with STK Engine.

    Use STKEngine.StartApplication() to obtain an initialized STKEngineApplication object.
    """

    def __init__(self):
        """Construct an object of type STKEngineApplication."""
        STKXApplication.__init__(self)
        self.__dict__["_initialized"] = False
        self.__dict__["_grpc_exceptions"] = True

    def _private_init(self, unknown:IUnknown, no_graphics):
        STKXApplication._private_init(self, unknown)
        if os.name!="nt" or OLE32Lib.use_xcom_registry:
            self._stkx_intialize()
        self._stkx_intialize_timer(no_graphics)
        self.__dict__["_initialized"] = True

    def __del__(self):
        """Destruct the STKEngineApplication object after all references to the object are deleted."""
        self.shutdown()

    def _stkx_intialize(self):
        clsid_agstkxinitialize = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString("{AF678C04-D41C-43D2-B8FA-28111812AA0C}", clsid_agstkxinitialize)):
            iid_iunknown = GUID(IUnknown._guid)
            stkxinit_unk = IUnknown()
            if Succeeded(OLE32Lib.CoCreateInstance(byref(clsid_agstkxinitialize), None, CLSCTX_INPROC_SERVER, byref(iid_iunknown), byref(stkxinit_unk.p))):
                stkxinit_unk.take_ownership()
                stkxinit = STKXInitialize()
                stkxinit._private_init(stkxinit_unk)
                install_dir = os.getenv("STK_INSTALL_DIR")
                if install_dir is None:
                    raise RuntimeError("Please set a valid STK_INSTALL_DIR environment variable.")
                config_dir = os.getenv("STK_CONFIG_DIR")
                if config_dir is None:
                    raise RuntimeError("Please set a valid STK_CONFIG_DIR environment variable.")
                all_users_dir = os.getenv("STK_ALLUSERS_DIR")
                all_users_dir = all_users_dir if all_users_dir is not None else ""
                stkxinit.initialize_data(install_dir, all_users_dir, config_dir)

    @staticmethod
    def _get_signo(sigrtmin_offset):
        if os.name=="nt":
            return None
        libc = cdll.LoadLibrary(find_library("c"))
        __libc_current_sigrtmin = CFUNCTYPE(c_int)(("__libc_current_sigrtmin", libc))
        return __libc_current_sigrtmin() + sigrtmin_offset

    def _set_timer_type_from_env(self):
        timer_type = int(os.getenv("STK_PYTHONAPI_TIMERTYPE", "4"))
        if os.name=="nt" or timer_type == STKEngineTimerType.DISABLE_TIMERS:
            self.__dict__["_timer_impl"] = NullTimer()
        elif os.name != "nt":
            if timer_type == STKEngineTimerType.TKINTER_MAIN_LOOP or timer_type == STKEngineTimerType.INTERACTIVE_PYTHON:
                self.__dict__["_timer_impl"] = TclTimer()
            elif timer_type == STKEngineTimerType.SIG_ALARM:
                self.__dict__["_timer_impl"] = SigAlarmTimer()
            elif timer_type == STKEngineTimerType.SIG_RT:
                sigrtmin_offset = int(os.getenv("STK_PYTHONAPI_TIMERTYPE5_SIGRTMIN_OFFSET", "0"))
                signo = STKEngineApplication._get_signo(sigrtmin_offset)
                self.__dict__["_timer_impl"] = SigRtTimer(signo)

    def _user_override_timer_type(self) -> bool:
        return ("STK_PYTHONAPI_TIMERTYPE" in os.environ)

    def _stkx_intialize_timer(self, no_graphics):
        if os.name=="nt":
            #Timers are not implemented on Windows, use a placeholder.
            self.__dict__["_timer_impl"] = NullTimer()
        elif no_graphics:
            self._set_timer_type_from_env()
        else:
            #default to Tkinter mainloop in graphics applications, but allow the user to override
            #e.g. if controls are not being used, the SIG_ALARM timer might be desired.
            if self._user_override_timer_type():
                self._set_timer_type_from_env()
            else:
                self.__dict__["_timer_impl"] = TclTimer()

    def new_object_root(self) -> STKObjectRoot:
        """Create a new object model root for the STK Engine application."""
        if not self.__dict__["_initialized"]:
            raise RuntimeError("STKEngineApplication has not been properly initialized.  Use StartApplication() to obtain the STKEngineApplication object.")
        clsid_agstkobjectroot = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString("{97F9B4C7-6526-40D6-8ED7-0ACCD8A287B4}", clsid_agstkobjectroot)):
            iid_iunknown = GUID(IUnknown._guid)
            root_unk = IUnknown()
            OLE32Lib.CoCreateInstance(byref(clsid_agstkobjectroot), None, CLSCTX_INPROC_SERVER, byref(iid_iunknown), byref(root_unk.p))
            root_unk.take_ownership()
            root = STKObjectRoot()
            root._private_init(root_unk)
            return root

    def new_object_model_context(self) -> STKObjectModelContext:
        """Create a new object model context for the STK Engine application."""
        if not self.__dict__['_initialized']:
            raise RuntimeError('STKEngineApplication has not been properly initialized.  Use StartApplication() to obtain the STKEngineApplication object.')
        clsid_agstkobjectmodelcontext = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString('{D45C0F17-AAB4-4D2B-A9A2-5A125F528B6B}', clsid_agstkobjectmodelcontext)):
            iid_iunknown = GUID(IUnknown._guid)
            context_unk = IUnknown()
            OLE32Lib.CoCreateInstance(byref(clsid_agstkobjectmodelcontext), None, CLSCTX_INPROC_SERVER, byref(iid_iunknown), byref(context_unk.p))
            context_unk.take_ownership()
            context = STKObjectModelContext()
            context._private_init(context_unk)
            return context

    def set_grpc_options(self, options:dict) -> None:
        """
        Grpc is not available with STK Engine. Provided for parity with STK Runtime and Desktop.

        Available options include:
        { "raise exceptions with STK Engine" : bool }. Set to false to suppress exceptions when
        using SetGrpcOptions and NewGrpcCallBatcher with STK Engine.
        """
        if "raise exceptions with STK Engine" in options:
            self.__dict__["_grpc_exceptions"] = options["raise exceptions with STK Engine"]
        if self._grpc_exceptions:
            raise SyntaxError("gRPC is not available with STK Engine. Disable this exception with SetGrpcOptions({\"raise exceptions with STK Engine\" : False}).")

    def new_grpc_call_batcher(self, max_batch:int=None, disable_batching:bool=True) -> GrpcCallBatcher:
        """Grpc is not available with STK Engine. Provided for parity with STK Runtime and Desktop."""
        if self._grpc_exceptions:
            raise SyntaxError("gRPC is not available with STK Engine. Disable this exception with SetGrpcOptions({\"raise exceptions with STK Engine\" : False}).")
        return GrpcCallBatcher(disable_batching=True)

    def shutdown(self) -> None:
        """Shut down the STK Engine application."""
        if self._initialized:
            EventSubscriptionManager.unsubscribe_all()
            self._timer_impl.terminate()
            ObjectLifetimeManager.release_all(releaseApplication=False)
            self.terminate()
            ObjectLifetimeManager.release_all(releaseApplication=True)
            CoInitializeManager.uninitialize()
            self.__dict__["_initialized"] = False


class STKEngine(object):
    """Initialize and manage the STK Engine application."""

    _is_engine_running = False

    @staticmethod
    def _init_x11(no_graphics):
        if no_graphics or os.name=="nt":
            return
        try:
            x11lib = cdll.LoadLibrary(find_library("X11"))
            xinit_threads = CFUNCTYPE(None)(("XInitThreads", x11lib))
            xinit_threads()
        except OSError:
            raise RuntimeError("Failed attempting to run graphics mode without X11.")

    @staticmethod
    def _new_engine_application(unknown:IUnknown, no_graphics:bool) -> STKEngineApplication:
        STKEngine._is_engine_running = True
        STKEngine._init_x11(no_graphics)
        engine = STKEngineApplication()
        engine._private_init(unknown, no_graphics)
        engine.no_graphics = no_graphics
        atexit.register(engine.shutdown)
        return engine

    @staticmethod
    def _start_stkx_application(no_graphics:bool) -> STKEngineApplication:
        CoInitializeManager.initialize()
        clsid_agstkxapplication = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString("{5F1B7A77-663D-44E9-99A9-2367B4F9AF6F}", clsid_agstkxapplication)):
            unknown = IUnknown()
            iid_iunknown = GUID(IUnknown._guid)
            if Succeeded(OLE32Lib.CoCreateInstance(byref(clsid_agstkxapplication), None, CLSCTX_INPROC_SERVER, byref(iid_iunknown), byref(unknown.p))):
                unknown.take_ownership(isApplication=True)
                return STKEngine._new_engine_application(unknown, no_graphics)
        raise RuntimeError("Failed to create STK Engine application. Check for successful install and registration.")

    @staticmethod
    def _start_stkx_partner_access(no_graphics:bool, vendor:str, product:str, key:str) -> STKEngineApplication:
        CoInitializeManager.initialize()
        clsid_entry_class = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString("{9FD979E7-2D25-4147-95A2-43536161F6EF}", clsid_entry_class)):
            unknown = IUnknown()
            iid_iunknown = GUID(IUnknown._guid)
            if Succeeded(OLE32Lib.CoCreateInstance(byref(clsid_entry_class), None, CLSCTX_INPROC_SERVER, byref(iid_iunknown), byref(unknown.p))):
                unknown.take_ownership(isApplication=False)
                pa = STKXApplicationPartnerAccess()
                pa._private_init(unknown)
                stkx_pa_app = pa.grant_partner_access(vendor, product, key)
                app_unknown = stkx_pa_app._intf
                app_unknown.set_as_application()
                return STKEngine._new_engine_application(app_unknown, no_graphics)
        raise RuntimeError("Failed to create STKX Partner Access application. Check for successful install and registration.")
    @staticmethod
    def start_application(no_graphics:bool=True, **kwargs) -> STKEngineApplication:
        """
        Initialize STK Engine in-process and return the instance.

        Must only be used once per Python process.
        Specify no_graphics = True to start the application in no-graphics mode.
        """
        if STKEngine._is_engine_running:
            raise RuntimeError("Only one STK Engine instance is allowed per Python process.")
        if len(kwargs) == 0:
            return STKEngine._start_stkx_application(no_graphics)
        else:
            if set(list(kwargs)) == set(["vendor", "product", "key"]):
                return STKEngine._start_stkx_partner_access(no_graphics, kwargs["vendor"], kwargs["product"], kwargs["key"])
            else:
                raise RuntimeError(f"Unrecognized or incomplete kwargs: {list(kwargs)}.")