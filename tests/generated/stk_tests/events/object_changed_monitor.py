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

from test_util import *
from events.object_model_event_monitor import *
from ansys.stk.core.stkobjects import *


class ObjectChangedMonitor(IObjectModelEventMonitor):
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.Dispose()

    def __init__(self, root: "StkObjectRoot"):
        self._lastSender: str = None
        self._counter: int = 0
        self._root: "StkObjectRoot" = root

        self.csToPy_OnStkObjectChangedSubscription = (self._root).subscribe()
        self.csToPy_OnStkObjectChangedSubscription.on_stk_object_changed += self._root_OnStkObjectChanged

    @property
    def Counter(self):
        return self._counter

    @property
    def Sender(self):
        return self._lastSender

    def Terminate(self):
        self.csToPy_OnStkObjectChangedSubscription.on_stk_object_changed -= self._root_OnStkObjectChanged

    def _root_OnStkObjectChanged(self, pArgs: "StkObjectChangedEventArguments"):
        sPath: str = pArgs.path
        self._counter += 1
        self._lastSender = pArgs.path

    # region IDisposable Members

    def Dispose(self):
        self.Terminate()
        GC.SuppressFinalize(self)

    # endregion
