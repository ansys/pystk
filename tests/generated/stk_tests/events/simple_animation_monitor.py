# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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

from test_util import *
from events.object_model_event_monitor import *
from logger import *
from ansys.stk.core.stkobjects import *


class SimpleAnimationUpdateMonitor(IObjectModelEventMonitor):
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.Dispose2()

    def __init__(self, root: "StkObjectRoot"):
        self._cycleCount: int = -1
        self._isEndOfTime: bool = False
        self._stopTime: float = 0
        self._startTime: float = 0
        self.m_logger = Logger.Instance
        self.disposed: bool = False
        self._root: "StkObjectRoot" = root
        self.HookupEvents()

    def Reset(self):
        self._cycleCount = -1
        self._isEndOfTime = False

    @property
    def IsRepeating(self):
        return self._cycleCount > 0

    @property
    def HasEnded(self):
        return self._isEndOfTime

    def __del__(self):
        pass

    def HookupEvents(self):
        scenario: "Scenario" = clr.CastAs(self._root.current_scenario, Scenario)
        if String.Compare(self._root.units_preferences.get_current_unit_abbrv("DateFormat"), "EpSec", True) != 0:
            self._stopTime = float(
                self._root.conversion_utility.convert_date(
                    "DateFormat", "EpSec", str(scenario.animation_settings.animation_cycle_time)
                )
            )
            self._startTime = float(
                self._root.conversion_utility.convert_date(
                    "DateFormat", "EpSec", str(scenario.animation_settings.start_time)
                )
            )

        else:
            self._stopTime = float(str(scenario.animation_settings.animation_cycle_time))
            self._startTime = float(str(scenario.animation_settings.start_time))

        self.csToPy_OnAnimUpdateSubscription = (self._root).subscribe()
        self.csToPy_OnAnimUpdateSubscription.on_anim_update += IAgStkObjectRootEvents_OnAnimUpdateEventHandler(
            self.root_OnAnimUpdate
        )

    def root_OnAnimUpdate(self, TimeEpSec: float):
        if self._isEndOfTime:
            self._isEndOfTime = False
        self._isEndOfTime = self._stopTime == TimeEpSec
        self._cycleCount += 1
        if TimeEpSec == self._startTime:
            pass
        self.m_logger.WriteLine6("ONANIMUPDATE: {0}", TimeEpSec)

    def UnhookEvents(self):
        self.csToPy_OnAnimUpdateSubscription.on_anim_update -= IAgStkObjectRootEvents_OnAnimUpdateEventHandler(
            self.root_OnAnimUpdate
        )

    def Dispose(self, disposing: bool):
        if not self.disposed:
            self.disposed = True
            self.UnhookEvents()
            if disposing:
                GC.SuppressFinalize(self)

    # region IDisposable Members

    def Dispose2(self):
        self.Dispose(True)

    # endregion
