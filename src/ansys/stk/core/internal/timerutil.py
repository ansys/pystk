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

import os
import time
import signal

from ctypes import CFUNCTYPE, cdll, c_size_t, c_int, c_void_p

TIMERPROC = CFUNCTYPE(None, c_size_t)
INSTALLTIMER = CFUNCTYPE(c_size_t, c_int, TIMERPROC, c_void_p)
DELETETIMER = CFUNCTYPE(c_int, c_size_t, c_void_p)

if os.name != "nt":
    class UtilLib:
        _handle = None
        set_timer_callbacks = None
        initialize_librt_timers = None
        uninitialize_librt_timers = None
        fire_librt_timer_callbacks = None

        def initialize():
            if UtilLib._handle is None:
                UtilLib._handle = cdll.LoadLibrary("libagutil.so")
                UtilLib.set_timer_callbacks = CFUNCTYPE(None, INSTALLTIMER, DELETETIMER, c_void_p)(("AgUtSetTimerCallbacks", UtilLib._handle), ((1, "pInstallTimer"), (1, "pDeleteTimer"), (1, "pCallbackData")))
                UtilLib.initialize_librt_timers = CFUNCTYPE(None, c_int)(("AgUtInitializeLibrtTimers", UtilLib._handle), ((1, "signo"),))
                UtilLib.uninitialize_librt_timers = CFUNCTYPE(None)(("AgUtUninitializeLibrtTimers", UtilLib._handle))
                UtilLib.fire_librt_timer_callbacks = CFUNCTYPE(None)(("AgUtFireLibrtTimerCallbacks", UtilLib._handle))

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
    def next_time_proc(timers:dict):
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
            self._install_timer_cfunc = INSTALLTIMER(self.__install_timer)
            self._delete_timer_cfunc = DELETETIMER(self.__delete_timer)
            UtilLib.initialize()
            UtilLib.set_timer_callbacks(self._install_timer_cfunc, self._delete_timer_cfunc, c_void_p())
        else:
            pass

    def terminate(self):
        pass

    def __install_timer(self, milliseconds, TIMERPROC, callbackData):
        return 0

    def __delete_timer(self, timerID, callbackData):
        return 0

if os.name != "nt":
    try:
        from tkinter import Tcl
    except:
        class Tcl(object):
            def __init__(self):
                raise RuntimeError("Cannot use STKEngineTimerType.TKINTER_MAIN_LOOP nor STKEngineTimerType.INTERACTIVE_PYTHON because tkinter installation is not found.")

    class TclTimer(object):
        def __init__(self):
            self._next_id = 1
            self._timers = dict()
            self._install_timer_cfunc = INSTALLTIMER(self.__install_timer)
            self._delete_timer_cfunc = DELETETIMER(self.__delete_timer)
            UtilLib.initialize()
            UtilLib.set_timer_callbacks(self._install_timer_cfunc, self._delete_timer_cfunc, c_void_p())
            self._tcl = Tcl()
            self._tcl.after(self._next_timer_proc(), self._loop_timers)
            self._terminated = False

        def terminate(self):
            self._terminated = True
            del(self._tcl)

        def __install_timer(self, milliseconds, TIMERPROC, callbackData):
            id = self._next_id
            self._next_id = id + 1
            self._timers[id] = _ClockTimer(id, milliseconds, TIMERPROC, callbackData)
            return id

        def __delete_timer(self, timerID, callbackData):
            if timerID in self._timers:
                del(self._timers[timerID])
            return 0

        def _fire_timers(self):
            timers = self._timers.copy()
            for timerid in timers:
                timers[timerid].fire()

        def _next_timer_proc(self):
            """Return time in ms until next timer proc"""
            return int(_ClockTimer.next_time_proc(self._timers.copy())*1000)

        def _loop_timers(self):
            self._fire_timers()
            if not self._terminated:
                self._tcl.after(self._next_timer_proc(), self._loop_timers)

    class SigAlarmTimer(object):
        def __init__(self):
            self._next_id = 1
            self._timers = dict()
            self._install_timer_cfunc = INSTALLTIMER(self.__install_timer)
            self._delete_timer_cfunc = DELETETIMER(self.__delete_timer)
            UtilLib.initialize()
            UtilLib.set_timer_callbacks(self._install_timer_cfunc, self._delete_timer_cfunc, c_void_p())
            self.previous_sighandler = signal.signal(signal.SIGALRM, self._fire_timers)

        def terminate(self):
            signal.setitimer(signal.ITIMER_REAL, 0, 0)
            signal.signal(signal.SIGALRM, self.previous_sighandler)

        def __install_timer(self, milliseconds, TIMERPROC, callbackData):
            id = self._next_id
            self._next_id = id + 1
            self._timers[id] = _ClockTimer(id, milliseconds, TIMERPROC, callbackData)
            self._set_alarm_for_next_timer_proc()
            return id

        def __delete_timer(self, timerID, callbackData):
            if timerID in self._timers:
                del(self._timers[timerID])
            return 0

        def _fire_timers(self, signo, frame):
            timers = self._timers.copy()
            for timerid in timers:
                timers[timerid].fire()
            self._set_alarm_for_next_timer_proc()

        def _set_alarm_for_next_timer_proc(self):
            next_proc = _ClockTimer.next_time_proc(self._timers.copy())
            if next_proc > 0:
                signal.setitimer(signal.ITIMER_REAL, next_proc, 0)
            else:
                self._fire_timers(signal.SIGALRM, None)
                self._set_alarm_for_next_timer_proc()


    class SigRtTimer(object):
        def __init__(self, signo):
            self._next_id = 1
            self._timers = dict()
            self._signo = signo
            self.previous_sighandler = signal.signal(self._signo, self._fire_timers)
            UtilLib.initialize()
            UtilLib.initialize_librt_timers(self._signo)

        def terminate(self):
            UtilLib.uninitialize_librt_timers()
            signal.signal(self._signo, self.previous_sighandler)

        def _fire_timers(self, signo, frame):
            UtilLib.fire_librt_timer_callbacks()