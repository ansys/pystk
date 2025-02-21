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
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class UnitPreferenceState(IDisposable):
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.Dispose()

    def __init__(self, application: "StkObjectRoot"):
        self._disposed: bool = False
        self._state = {}

        self._application: "StkObjectRoot" = application
        self.SaveState(application.units_preferences)

    def RestoreState(self, dimensions: "UnitPreferencesDimensionCollection"):
        dimension: "UnitPreferencesDimension"
        for dimension in dimensions:
            key: str = dimension.name
            abbr: str = self._state[key]
            if not String.IsNullOrEmpty(abbr):
                dimension.set_current_unit(abbr)

    def SaveState(self, dimensions: "UnitPreferencesDimensionCollection"):
        dimension: "UnitPreferencesDimension"
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
            self.RestoreState(self._application.units_preferences)
            self._application = None

        self._disposed = True
