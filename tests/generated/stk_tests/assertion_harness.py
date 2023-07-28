from test_util import *
from ansys.stk.core.stkobjects import *


class Unit(object):
    def __init__(self, dimension: str, name: str):
        self.Dimension: str = dimension
        self.UnitName: str = name


class TryCatchAssertBlock(object):
    @staticmethod
    def DoAssert(message: str, action):
        TryCatchAssertBlock.ExpectedException("", action)

    @staticmethod
    def DoAssertInvalidCast(action):
        exceptionType: str = "No exception"
        try:
            action()

        except STKInvalidCastError:
            # OK
            return

        except Exception as e:
            exceptionType = type(e).ToString()
            Assert.fail((str(type(e)) + " was thrown rather than InvalidCastException"))

        Assert.fail("{0} was thrown. InvalidCastException was expected.", exceptionType)

    @staticmethod
    def ExpectedException(message: str, action):
        try:
            action()

        except Exception as ex:
            if str(ex).find(message) == -1:
                raise
            # Otherwise, the exception is expected
            # Console.WriteLine(ex.Message);
            return

        Assert.fail("Expected exception: {0}", message)

    @staticmethod
    def DoAssert2(action):
        TryCatchAssertBlock.ExpectedException("", action)

    @staticmethod
    def DoActionRunFinalize(action, finalizer):
        try:
            action()

        finally:
            finalizer()

    @staticmethod
    def DoActionRunFinalize2(root: "IStkObjectRoot", action, finalizer, *units):
        try:
            runner = CodeRunner(root)
            runner.DoWithUnits(action, units)

        finally:
            finalizer()


class CodeRunner(object):
    def __init__(self, root: "IStkObjectRoot", bBeginEndUpdate: bool = False):
        self._root: "IStkObjectRoot" = root
        self._bBeginEndUpdate: bool = bBeginEndUpdate

    def DoWithUnits(self, action, *units):
        self.DoWithUnits2(action, Enumerable.ToList(units))

    def Iterate(self, maxIterations: int, action, *units):
        watch = None
        if self._bBeginEndUpdate:
            self._root.BeginUpdate()
        try:

            def action1():
                nonlocal watch
                watch = Stopwatch.StartNew()

                i: int = 0
                while i < maxIterations:
                    action(i)

                    i += 1

                watch.Stop()

            self.DoWithUnits(action1, units)

        finally:
            if self._bBeginEndUpdate:
                self._root.EndUpdate()

        Assert.assertIsNotNone(watch)
        return watch.Elapsed

    def DoWithUnits2(self, action, units):
        temp = []
        try:
            for unit in units:
                saved = Unit(unit.Dimension, self._root.UnitPreferences.GetCurrentUnitAbbrv(unit.Dimension))
                temp.append(saved)
                self._root.UnitPreferences.SetCurrentUnit(unit.Dimension, unit.UnitName)

            action()

        finally:
            for unit in temp:
                self._root.UnitPreferences.SetCurrentUnit(unit.Dimension, unit.UnitName)
