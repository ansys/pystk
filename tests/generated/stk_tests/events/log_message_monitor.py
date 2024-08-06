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

        self.csToPy_OnLogMessageSubscription = (self._root).Subscribe()
        self.csToPy_OnLogMessageSubscription.on_log_message += self._root_OnLogMessage

    def _root_OnLogMessage(
        self,
        Message: str,
        MsgType: "LOG_MESSAGE_TYPE",
        ErrorCode: int,
        Filename: str,
        LineNo: int,
        DispID: "LOG_MESSAGE_DISP_ID",
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
