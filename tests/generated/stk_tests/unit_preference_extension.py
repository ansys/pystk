from test_util import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class UnitPreferenceState(IDisposable):
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.Dispose()

    def __init__(self, application: "IStkObjectRoot"):
        self._disposed: bool = False
        self._state = {}

        self._application: "IStkObjectRoot" = application
        self.SaveState(application.unit_preferences)

    def RestoreState(self, dimensions: "IUnitPreferencesDimensionCollection"):
        dimension: "IUnitPreferencesDimension"
        for dimension in dimensions:
            key: str = dimension.name
            abbr: str = self._state[key]
            if not String.IsNullOrEmpty(abbr):
                dimension.set_current_unit(abbr)

    def SaveState(self, dimensions: "IUnitPreferencesDimensionCollection"):
        dimension: "IUnitPreferencesDimension"
        for dimension in dimensions:
            dim: str = dimension.name
            abrv: str = dimension.current_unit.abbrv
            self._state[dim] = abrv

    def __del__(self):
        pass

    def Dispose(self):
        self.Dispose2(True)

    def Dispose2(self, disposing: bool):
        if self._disposed:
            return
        if disposing:
            self.RestoreState(self._application.unit_preferences)
            self._application = None

        self._disposed = True
