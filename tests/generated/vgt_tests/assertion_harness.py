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


class Unit(object):
    def __init__(self, dimension: str, name: str):
        self.Dimension: str = dimension
        self.UnitName: str = name


class TryCatchAssertBlock(object):
    @staticmethod
    def DoActionRunFinalize(action, finalizer):
        try:
            action()

        finally:
            finalizer()

    @staticmethod
    def DoActionRunFinalize2(root: "StkObjectRoot", action, finalizer, *units):
        try:
            runner = CodeRunner(root)
            runner.DoWithUnits2(action, Enumerable.ToList(units))

        finally:
            finalizer()


class CodeRunner(object):
    def __init__(self, root: "StkObjectRoot", bBeginEndUpdate: bool = False):
        self._root: "StkObjectRoot" = root
        self._bBeginEndUpdate: bool = bBeginEndUpdate

    def DoWithUnits(self, action, *units):
        self.DoWithUnits2(action, Enumerable.ToList(units))

    def Iterate(self, maxIterations: int, action, *units):
        watch = Stopwatch()
        if self._bBeginEndUpdate:
            self._root.begin_update()
        try:

            def action1():
                nonlocal watch
                watch.Start()

                i: int = 0
                while i < maxIterations:
                    action(i)

                    i += 1

                watch.Stop()

            self.DoWithUnits2(action1, Enumerable.ToList(units))

        finally:
            if self._bBeginEndUpdate:
                self._root.end_update()

        Assert.assertIsNotNone(watch)
        return watch.Elapsed

    def DoWithUnits2(self, action, units):
        temp = []
        try:
            for unit in units:
                saved = Unit(unit.Dimension, self._root.units_preferences.get_current_unit_abbrv(unit.Dimension))
                temp.append(saved)
                self._root.units_preferences.set_current_unit(unit.Dimension, unit.UnitName)

            action()

        finally:
            for unit in temp:
                self._root.units_preferences.set_current_unit(unit.Dimension, unit.UnitName)
