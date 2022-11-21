################################################################################
#          Copyright 2021-2021, Analytical Graphics, Inc.
################################################################################

import os
import time
import signal

from enum import Enum
from ctypes import CFUNCTYPE, cdll, c_size_t, c_int, c_void_p
from ctypes.util import find_library

from ..utilities.exceptions import *

TIMERPROC = CFUNCTYPE(None, c_size_t)
INSTALLTIMER = CFUNCTYPE(c_size_t, c_int, TIMERPROC, c_void_p)
DELETETIMER = CFUNCTYPE(c_int, c_size_t, c_void_p)

if os.name != "nt":
    class agutillib:
        _handle = None
        AgUtSetTimerCallbacks = None
        AgUtInitializeLibrtTimers = None
        AgUtUninitializeLibrtTimers = None
        AgUtFireLibrtTimerCallbacks = None

        def initialize():
            if agutillib._handle is None:
                agutillib._handle = cdll.LoadLibrary("libagutil.so")
                agutillib.AgUtSetTimerCallbacks = CFUNCTYPE(None, INSTALLTIMER, DELETETIMER, c_void_p)(("AgUtSetTimerCallbacks", agutillib._handle), ((1, "pInstallTimer"), (1, "pDeleteTimer"), (1, "pCallbackData")))
                agutillib.AgUtInitializeLibrtTimers = CFUNCTYPE(None, c_int)(("AgUtInitializeLibrtTimers", agutillib._handle), ((1, "signo"),))
                agutillib.AgUtUninitializeLibrtTimers = CFUNCTYPE(None)(("AgUtUninitializeLibrtTimers", agutillib._handle))
                agutillib.AgUtFireLibrtTimerCallbacks = CFUNCTYPE(None)(("AgUtFireLibrtTimerCallbacks", agutillib._handle))

class _ClockTimer(object):
    def __init__(self, id, milliseconds, TIMERPROC, callbackData):
        self.id = id
        self.interval = milliseconds/1000
        self.callback = TIMERPROC
        self.callback_data = callbackData
        self._reset()
        
    def _reset(self):
        self.next_proc = time.clock_gettime(time.CLOCK_REALTIME) + self.interval
        
    def fire(self):
        if time.clock_gettime(time.CLOCK_REALTIME) >= self.next_proc:
            self.callback(self.id)
            self._reset()
            
    @staticmethod
    def NextTimerProc(timers:dict):
        """Return time in sec until next timer proc"""
        if len(timers) == 0:
            return 0.050
        else:
            proc_times = list()
            for timerid in timers:
                proc_times.append(timers[timerid].next_proc)
            delta_s = min(proc_times)-time.clock_gettime(time.CLOCK_REALTIME)
            if delta_s > 0:
                return delta_s
            else:
                return 0
    
class NullTimer(object):
    def __init__(self):
        if os.name != "nt":
            self._install_timer_cfunc = INSTALLTIMER(self.__InstallTimer)
            self._delete_timer_cfunc = DELETETIMER(self.__DeleteTimer)
            agutillib.initialize()
            agutillib.AgUtSetTimerCallbacks(self._install_timer_cfunc, self._delete_timer_cfunc, c_void_p())
        else:
            pass
        
    def Terminate(self):
        pass
        
    def __InstallTimer(self, milliseconds, TIMERPROC, callbackData):
        return 0

    def __DeleteTimer(self, timerID, callbackData):
        return 0
    
if os.name != "nt":
    try:
        from tkinter import Tcl
    except:
        class Tcl(object):
            def __init__(self):
                raise STKInvalidTimerError("Cannot use STKEngineTimerType.TkinterMainloop nor STKEngineTimerType.InteractivePython because tkinter installation is not found.")
            
    class TclTimer(object):
        def __init__(self):
            self._next_id = 1
            self._timers = dict()
            self._install_timer_cfunc = INSTALLTIMER(self.__InstallTimer)
            self._delete_timer_cfunc = DELETETIMER(self.__DeleteTimer)
            agutillib.initialize()
            agutillib.AgUtSetTimerCallbacks(self._install_timer_cfunc, self._delete_timer_cfunc, c_void_p())
            self._tcl = Tcl()
            self._tcl.after(self._NextTimerProc(), self._LoopTimers)
            
        def Terminate(self):
            del(self._tcl)
            
        def __InstallTimer(self, milliseconds, TIMERPROC, callbackData):
            id = self._next_id
            self._next_id = id + 1
            self._timers[id] = _ClockTimer(id, milliseconds, TIMERPROC, callbackData)
            return id

        def __DeleteTimer(self, timerID, callbackData):
            if timerID in self._timers:
                del(self._timers[timerID])
            return 0
            
        def _FireTimers(self):
            timers = self._timers.copy()
            for timerid in timers:
                timers[timerid].fire()
            
        def _NextTimerProc(self):
            """Return time in ms until next timer proc"""
            return int(_ClockTimer.NextTimerProc(self._timers.copy())*1000)
                    
        def _LoopTimers(self):
            self._FireTimers()
            self._tcl.after(self._NextTimerProc(), self._LoopTimers)
        
    class SigAlarmTimer(object):
        def __init__(self):
            self._next_id = 1
            self._timers = dict()
            self._install_timer_cfunc = INSTALLTIMER(self.__InstallTimer)
            self._delete_timer_cfunc = DELETETIMER(self.__DeleteTimer)
            agutillib.initialize()
            agutillib.AgUtSetTimerCallbacks(self._install_timer_cfunc, self._delete_timer_cfunc, c_void_p())
            self.previous_sighandler = signal.signal(signal.SIGALRM, self._FireTimers)
        
        def Terminate(self):
            signal.setitimer(signal.ITIMER_REAL, 0, 0)
            try:
                signal.signal(signal.SIGALRM, self.previous_sighandler)
            except:
                pass
                
        def __InstallTimer(self, milliseconds, TIMERPROC, callbackData):
            id = self._next_id
            self._next_id = id + 1
            self._timers[id] = _ClockTimer(id, milliseconds, TIMERPROC, callbackData)
            self._SetAlarmForNextTimerProc()
            return id

        def __DeleteTimer(self, timerID, callbackData):
            if timerID in self._timers:
                del(self._timers[timerID])
            return 0
            
        def _FireTimers(self, signo, frame):
            timers = self._timers.copy()
            for timerid in timers:
                timers[timerid].fire()
            self._SetAlarmForNextTimerProc()
                    
        def _SetAlarmForNextTimerProc(self):
            next_proc = _ClockTimer.NextTimerProc(self._timers.copy())
            if next_proc > 0:
                signal.setitimer(signal.ITIMER_REAL, next_proc, 0)
            else:
                self._FireTimers(signal.SIGALRM, None)
                self._SetAlarmForNextTimerProc()
            
            
    class SigRtTimer(object):
        def __init__(self, signo):
            self._next_id = 1
            self._timers = dict()
            self._signo = signo
            self.previous_sighandler = signal.signal(self._signo, self._FireTimers)
            agutillib.initialize()
            agutillib.AgUtInitializeLibrtTimers(self._signo)
            
        def Terminate(self):
            agutillib.AgUtUninitializeLibrtTimers()
            try:
                signal.signal(self._signo, self.previous_sighandler)
            except:
                pass
            
        def _FireTimers(self, signo, frame):
            agutillib.AgUtFireLibrtTimerCallbacks()

    

################################################################################
#          Copyright 2021-2021, Analytical Graphics, Inc.
################################################################################