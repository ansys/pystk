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
from ansys.stk.core.stkutil import *


class LogMessageMonitor(IObjectModelEventMonitor):
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.Dispose()

    def __init__(self, root: "StkObjectRoot", filterEcho: bool):
        self._messages = []
        self._filterEcho: bool = filterEcho
        self._counter: int = 0
        self._root: "StkObjectRoot" = root

        self.csToPy_OnLogMessageSubscription = (self._root).subscribe()
        self.csToPy_OnLogMessageSubscription.on_log_message += self._root_OnLogMessage

    def _root_OnLogMessage(
        self,
        Message: str,
        MsgType: "LogMessageType",
        ErrorCode: int,
        Filename: str,
        LineNo: int,
        DispID: "LogMessageDisplayID",
    ):
        if self._filterEcho:
            if Message.startswith("STK/CON:"):
                return

        self._counter += 1
        self._messages.append(Message)

    @property
    def Counter(self):
        return self._counter

    @property
    def Messages(self):
        return self._messages

    def Terminate(self):
        self.csToPy_OnLogMessageSubscription.on_log_message -= self._root_OnLogMessage

    # region IDisposable Members

    def Dispose(self):
        self.Terminate()
        GC.SuppressFinalize(self)

    # endregion
