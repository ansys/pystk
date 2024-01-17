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
                saved = Unit(unit.Dimension, self._root.unit_preferences.get_current_unit_abbrv(unit.Dimension))
                temp.append(saved)
                self._root.unit_preferences.set_current_unit(unit.Dimension, unit.UnitName)

            action()

        finally:
            for unit in temp:
                self._root.unit_preferences.set_current_unit(unit.Dimension, unit.UnitName)
