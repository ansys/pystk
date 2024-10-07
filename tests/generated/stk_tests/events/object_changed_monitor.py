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

    def _root_OnStkObjectChanged(self, pArgs: "StkObjectChangedEventArgs"):
        sPath: str = pArgs.path
        self._counter += 1
        self._lastSender = pArgs.path

    # region IDisposable Members

    def Dispose(self):
        self.Terminate()
        GC.SuppressFinalize(self)

    # endregion
