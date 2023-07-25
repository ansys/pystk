import enum
import math
import os
import pytz
import re
import unittest
import sys
import typing  # noqa

from datetime import datetime, timedelta

from ansys.stk.core.stkengine import *

if os.name == "nt":
    from ansys.stk.core.stkdesktop import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.stkobjects.aviator import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *
from ansys.stk.core.utilities.colors import Colors
from ansys.stk.core.utilities.exceptions import *
from app_provider import TestTarget


class frmStkX:
    def __init__(self):
        from tkinter import Tk, BOTH, YES, LEFT
        from ansys.stk.core.stkengine.tkcontrols import GlobeControl, MapControl

        self.window = Tk()
        self.globeControl = GlobeControl(self.window, width=320, height=200)
        self.globeControl.pack(fill=BOTH, expand=YES, side=LEFT)
        self.mapControl = MapControl(self.window, width=320, height=200)
        self.mapControl.pack(fill=BOTH, expand=YES, side=LEFT)
        self.window.update()

    def destroy(self):
        self.window.destroy()

    def update(self):
        self.window.update()


class EngineLifetimeManager:
    stk = None
    locked = False
    target = None
    ctrlWindow = None

    @staticmethod
    def Initialize(lock=False, target="StkXNoGfx"):
        if os.name != "nt" and target == "Stk":
            raise RuntimeError("Stk target not supported on Linux.")
        if EngineLifetimeManager.target is None:
            if target == "Stk":
                EngineLifetimeManager.target = TestTarget.eStk
            elif target == "StkX":
                EngineLifetimeManager.target = TestTarget.eStkX
            elif target == "StkXNoGfx":
                EngineLifetimeManager.target = TestTarget.eStkNoGfx
        if EngineLifetimeManager.stk is None:
            if EngineLifetimeManager.target == TestTarget.eStk:
                EngineLifetimeManager.stk = STKDesktop.StartApplication(userControl=False, visible=True)
            elif EngineLifetimeManager.target == TestTarget.eStkX:
                EngineLifetimeManager.stk = STKEngine.StartApplication(noGraphics=False)
                EngineLifetimeManager.ctrlWindow = frmStkX()
                print(EngineLifetimeManager.stk.ExecuteCommand("GetStkVersion /")[0])
            elif EngineLifetimeManager.target == TestTarget.eStkNoGfx:
                EngineLifetimeManager.stk = STKEngine.StartApplication(noGraphics=True)
                print(EngineLifetimeManager.stk.ExecuteCommand("GetStkVersion /")[0])
            EngineLifetimeManager.locked = lock
        return EngineLifetimeManager.stk

    @staticmethod
    def Uninitialize(force=False):
        if force or not EngineLifetimeManager.locked:
            if EngineLifetimeManager.ctrlWindow is not None:
                EngineLifetimeManager.ctrlWindow.destroy()
            EngineLifetimeManager.stk.ShutDown()
            EngineLifetimeManager.stk = None

    @staticmethod
    def Lock():
        EngineLifetimeManager.locked = True

    @staticmethod
    def UpdateWindow():
        if EngineLifetimeManager.target == TestTarget.eStkX:
            EngineLifetimeManager.ctrlWindow.update()


class Path:
    @staticmethod
    def Combine(*args):
        result = ""
        for value in args:
            result = os.path.join(result, value)
        return result

    @staticmethod
    def GetTempPath():
        import tempfile

        return tempfile.gettempdir()

    @staticmethod
    def GetFileNameWithoutExtension(path):
        return os.path.splitext(os.path.basename(path))[0]

    @staticmethod
    def GetFileName(path):
        return os.path.basename(path)

    @staticmethod
    def GetFullPath(path):
        return os.path.abspath(path)

    @staticmethod
    def GetDirName(path):
        return os.path.dirname(path)


class ClrTypeOfResult:
    def __init__(self, typeinfo):
        self.typeinfo = typeinfo

    @property
    def FullName(self):
        return self.typeinfo.__module__ + "." + self.typeinfo.__qualname__

    def IsInstanceOfType(self, inst):
        return isinstance(inst, self.typeinfo)


class clr:
    @staticmethod
    def Convert(a, b):
        if isinstance(a, b):
            return a
        elif issubclass(b, enum.Enum):
            try:
                return b(a)
            except ValueError as ex:
                return a
        return b(a)

    @staticmethod
    def CastAs(a, b):
        if isinstance(a, b):
            return a
        else:
            try:
                return b(a)
            except:
                return None

    @staticmethod
    def Is(expr, type):
        if isinstance(expr, type):
            return True
        else:
            try:
                unused = type(expr)
                return True
            except:
                return False

    @staticmethod
    def TypeOf(obj):
        return ClrTypeOfResult(obj)


class GC:
    @staticmethod
    def SuppressFinalize(obj):
        pass


class Assert:
    @staticmethod
    def _getTestCaseFromStack():
        import inspect

        frameinfos = inspect.getouterframes(inspect.currentframe())
        for frameinfo in frameinfos:
            frame = frameinfo[0]
            locals = frame.f_locals
            if "self" in locals:
                candidate = locals["self"]
                if isinstance(candidate, unittest.TestCase):
                    return candidate
        return None

    @staticmethod
    def assertIsNone(obj, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertIsNone(obj, msg)
        elif obj is not None:
            raise AssertionError("unexpectedly not None")

    @staticmethod
    def assertIsNotNone(obj, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertIsNotNone(obj, msg)
        elif obj is None:
            raise AssertionError("unexpectedly None")

    @staticmethod
    def assertIsNotEmpty(obj, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            if isinstance(obj, list):
                testCase.assertNotEqual(len(obj), 0)
            else:
                testCase.assertNotEqual(obj, "")
        else:
            if isinstance(obj, list):
                if len(obj) != 0:
                    raise AssertionError("unexpectedly empty")
            else:
                if obj != "":
                    raise AssertionError("unexpectedly empty")

    @staticmethod
    def assertTrue(condition, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertTrue(condition, msg)
        elif not condition:
            raise AssertionError("unexpectedly not true")

    @staticmethod
    def assertFalse(condition, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertFalse(condition, msg)
        elif condition:
            raise AssertionError("unexpectedly not false")

    @staticmethod
    def assertEqual(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertEqual(first, second, msg)
        elif first != second:
            raise AssertionError("unexpectedly not equal")

    @staticmethod
    def assertNotEqual(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertNotEqual(first, second, msg)
        elif first == second:
            raise AssertionError("unexpectedly equal")

    @staticmethod
    def assertAlmostEqual(first, second, delta=None, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertAlmostEqual(first, second, msg=msg, delta=delta)
        elif abs(second - first) > (delta if delta is not None else 0):
            raise AssertionError("unexpectedly equal")

    @staticmethod
    def assertIs(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertIs(first, second, msg=msg)
        elif first is not second:
            raise AssertionError("unexpectedly isn't")

    @staticmethod
    def assertIsNot(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertIsNot(first, second, msg=msg)
        elif first is second:
            raise AssertionError("unexpectedly is")

    @staticmethod
    def assertRaises(fun):
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertRaises(Exception, fun)
        else:
            try:
                fun()
            except:
                return
            raise AssertionError("expected exception not raised")

    @staticmethod
    def assertGreater(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertGreater(first, second, msg)
        elif first <= second:
            raise AssertionError("unexpectedly not greater")

    @staticmethod
    def assertGreaterEqual(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertGreaterEqual(first, second, msg)
        elif first < second:
            raise AssertionError("unexpectedly not greater or equal")

    @staticmethod
    def assertLess(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertLess(first, second, msg)
        elif first >= second:
            raise AssertionError("unexpectedly not less")

    @staticmethod
    def assertLessEqual(first, second, msg=None):
        testCase = Assert._getTestCaseFromStack()
        Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.assertLessEqual(first, second, msg)
        elif first > second:
            raise AssertionError("unexpectedly not less or equal")

    @staticmethod
    def fail(*args):
        if len(args) > 0:
            msg = String.Format(*args)
        else:
            msg = None
        testCase = Assert._getTestCaseFromStack()
        if testCase is not None:
            testCase.fail(msg)
        else:
            raise AssertionError(f"unconditional failure" + (f": {msg}" if msg is not None else ""))


class StringAssert:
    @staticmethod
    def StartsWith(expected, actual, msg):
        if not actual.startswith(expected):
            assertMsg = f"{msg}, " if msg is not None else ""
            assertMsg += f"expected [{actual}] to starts with [{expected}]"
            raise AssertionError(assertMsg)

    @staticmethod
    def Contains(expected, actual, msg=None):
        if not expected in actual:
            assertMsg = f"{msg}, " if msg is not None else ""
            assertMsg += f"expected [{actual}] to contain [{expected}]"
            raise AssertionError(assertMsg)


class CollectionAssert:
    @staticmethod
    def AreEquivalent(expected, actual, message, *args):
        expectedSet = set(expected)
        actualSet = set(actual)
        if expectedSet != actualSet:
            if len(args) > 0:
                msg = String.Format(*args)
            else:
                msg = None
            raise AssertionError(f"collections not equivalent" + (f": {msg}" if msg is not None else ""))


class Math:
    def Round(value, digits=0):
        return round(value, digits)

    def Min(val1, val2):
        return min(val1, val2)

    def Max(val1, val2):
        return max(val1, val2)

    def Sin(value):
        return math.sin(value)

    def Sqrt(value):
        return math.sqrt(value)

    def Abs(value):
        return abs(value)


class Math2:
    Epsilon12 = 0.0000000000001
    Epsilon11 = 0.000000000001
    Epsilon10 = 0.00000000001
    Epsilon9 = 0.0000000001
    Epsilon8 = 0.000000001
    Epsilon7 = 0.00000001
    Epsilon6 = 0.0000001
    Epsilon5 = 0.000001
    Epsilon4 = 0.00001
    Epsilon3 = 0.0001
    Epsilon2 = 0.001
    Epsilon = 0.01


class ExceptionAssert:
    def Throws(action):
        try:
            action()
        except Exception as ex:
            return ex
        raise AssertionError("expected exception not thrown")

    def ThrowsIfExceptionProvided(expectedException, expectedMessage, matchType, action):
        if expectedException or expectedMessage:
            if not expectedException:
                expectedException = Exception
            ex = ExceptionAssert.Throws(action)
            if expectedMessage:
                if matchType == ExceptionMessageMatch.Contains:
                    StringAssert.Contains(expectedMessage, str(ex), "Exception message mismatch")
                elif matchType == ExceptionMessageMatch.StartsWith:
                    StringAssert.StartsWith(expectedMessage, str(ex), "Exception message mismatch")
                elif matchType == ExceptionMessageMatch.Exact:
                    Assert.AreEqual(expectedMessage, str(ex), "Exception message mismatch")
        else:
            action()


class COMException(Exception):
    pass


class ArgumentException(Exception):
    pass


class NullReferenceException(Exception):
    pass


class ArgumentOutOfRangeException(Exception):
    pass


class Enum:
    @staticmethod
    def GetValues(cls):
        if isinstance(cls, ClrTypeOfResult):
            cls = cls.typeinfo
        return list(map(lambda e: e, cls))


class staticproperty(property):
    def __get__(self, cls, owner):
        return staticmethod(self.fget).__get__(None, owner)()


class Color:
    @staticmethod
    def FromArgb(*args):
        if len(args) == 1:  # argb
            return Colors.FromRGB((args[0] & 0xFF0000) >> 16, (args[0] & 0x00FF00) >> 8, args[0] & 0xFF)
        elif len(args) == 3:  # r, g, b
            return Colors.FromRGB(args[0], args[1], args[2])
        elif len(args) == 4:  # a, r, g, b
            return Colors.FromRGB(args[1], args[2], args[3])
        else:
            raise Exception("unsupported color conversion")

    @staticproperty
    def Blue():
        return Colors.Blue

    @staticproperty
    def Green():
        return Colors.Green

    @staticproperty
    def Yellow():
        return Colors.Yellow

    @staticproperty
    def Black():
        return Colors.Black

    @staticproperty
    def Cyan():
        return Colors.Cyan

    @staticproperty
    def Pink():
        return Colors.Pink

    @staticproperty
    def Silver():
        return Colors.Silver

    @staticproperty
    def Red():
        return Colors.Red

    @staticproperty
    def White():
        return Colors.White

    @staticproperty
    def Orange():
        return Colors.Orange

    @staticproperty
    def RoyalBlue():
        return Colors.RoyalBlue

    @staticproperty
    def AliceBlue():
        return Colors.AliceBlue

    @staticproperty
    def AntiqueWhite():
        return Colors.AntiqueWhite


class NameValueCollection:
    @staticmethod
    def Get(name):
        if name == "loggingEnabled":
            return False
        elif name == "logFilePrefix":
            return "NUnit_STKX_log"
        raise Exception("Unsupported app setting")


class ConfigurationManager:
    AppSettings = NameValueCollection()


class Guid:
    @staticmethod
    def NewGuid():
        import uuid

        return str(uuid.uuid4())


class IDisposable:
    pass


class String:
    @staticmethod
    def Format(*args):
        if len(args) == 0:
            return ""
        result = args[0]
        for idx, p in enumerate(args[1:]):
            from enum import IntEnum

            if isinstance(p, IntEnum):
                strp = p.name
            else:
                strp = str(p)
            result = result.replace(f"{{{idx}}}", strp)
        return result

    @staticproperty
    def Empty():
        return ""

    @staticmethod
    def IsNullOrEmpty(s):
        return not s

    @staticmethod
    def Compare(strA, strB, ignoreCase):
        if ignoreCase:
            lowerStrA = strA.lower()
            lowerStrB = strB.lower()
            if lowerStrA == lowerStrB:
                return 0
            elif lowerStrA < lowerStrB:
                return -1
            else:
                return 1
        else:
            if strA == strB:
                return 0
            elif strA < strB:
                return -1
            else:
                return 1

    @staticmethod
    def Split(input, separators):
        import re

        return re.split("|".join([re.escape(sep) for sep in separators]), input)


class Console:
    @staticmethod
    def Write(*args):
        print(String.Format(*args), end="")

    @staticmethod
    def WriteLine(*args):
        print(String.Format(*args))


class Logger:
    Instance = None

    def __init__(self, *args):
        self.Enabled = True

    def Write(self, line):
        if self.Enabled:
            Console.Write(line)

    def Write2(self, format, s):
        if self.Enabled:
            Console.Write(format, s)

    def Write3(self, format, i):
        if self.Enabled:
            Console.Write(format, i)

    def Write4(self, format, obj1, obj2):
        if self.Enabled:
            Console.Write(format, obj1, obj2)

    def WriteLine(self, line):
        if self.Enabled:
            Console.WriteLine(line)

    def WriteLine2(self, obj):
        if self.Enabled:
            Console.WriteLine(obj)

    def WriteLine3(self, line, i):
        if self.Enabled:
            Console.WriteLine(line, i)

    def WriteLine4(self, line, b):
        if self.Enabled:
            Console.WriteLine(line, b)

    def WriteLine5(self, line, s):
        if self.Enabled:
            Console.WriteLine(line, s)

    def WriteLine6(self, format, obj1):
        if self.Enabled:
            Console.WriteLine(format, obj1)

    def WriteLine7(self, format, obj1, obj2):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2)

    def WriteLine8(self, format, obj1, obj2, obj3):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2, obj3)

    def WriteLine9(self, format, obj1, obj2, obj3, obj4):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2, obj3, obj4)

    def WriteLine10(self, format, *args):
        if self.Enabled:
            Console.WriteLine(format, args)


Logger.Instance = Logger()


class StringBuilder:
    def __init__(self, *args):
        self.buffer = ""

    def AppendFormat(self, *args):
        self.buffer += String.Format(*args)
        return self

    def ToString(self):
        return self.buffer

    def Append(self, value):
        if value is not None:
            if isinstance(value, list):
                self.buffer += ",".join(value)
            else:
                self.buffer += str(value)
        return self

    def AppendLine(self, value=None):
        self.Append(value)
        self.buffer += os.linesep
        return self

    @property
    def Length(self):
        return len(self.buffer)


class Double:
    @staticmethod
    def TryParse(str):
        try:
            return (True, float(str))
        except:
            return (False, math.nan)

    @staticmethod
    def ToString(value):
        return "{:g}".format(value)

    @staticproperty
    def MaxValue():
        return sys.float_info.max

    @staticproperty
    def MinValue():
        return sys.float_info.min


class Convert:
    @staticmethod
    def ToDouble(value):
        res, convertedValue = Double.TryParse(value)
        if not res:
            raise Exception(f"Cannot convert [{value}] to double")
        else:
            return convertedValue

    @staticmethod
    def ToInt32(value):
        return int(value)

    @staticmethod
    def ToInt16(value):
        return int(value)


class StreamReader:
    def __init__(self, filename):
        self.filename = filename
        self.handle = None

    def OpenText(self):
        self.handle = open(self.filename, "rt")

    def ReadToEnd(self):
        return self.handle.read()

    def ReadLine(self):
        return self.handle.readline()

    def Close(self):
        self.handle.close()


class FileInfo:
    def __init__(self, filename):
        self.filename = filename

    def OpenText(self):
        streamReader = StreamReader(self.filename)
        streamReader.OpenText()
        return streamReader

    def Exists(self):
        return os.path.exists(self.filename)

    def Delete(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def CopyTo(self, destFileName, overwrite):
        if overwrite and os.path.exists(destFileName):
            os.remove(destFileName)
        import shutil

        shutil.copyfile(self.filename, destFileName)

    @property
    def FullName(self):
        return os.path.abspath(self.filename)


class DirectoryInfo:
    def __init__(self, dirname):
        self.dirname = dirname

    @property
    def Exists(self):
        return os.path.exists(self.dirname) and os.path.isdir(self.dirname)

    def Create(self):
        return os.makedirs(self.dirname)

    def Delete(self, recursive=True):
        if recursive:
            if len(os.listdir(self.dirname)) > 100:
                # safeguard during development
                raise Exception(f"Trying to delete large number of files from {self.dirname}")
            import shutil

            shutil.rmtree(self.dirname, ignore_errors=True)
        else:
            os.rmdir(self.dirname)

    def GetFiles(self):
        return [os.path.abspath(f) for f in os.listdir(self.dirname) if os.path.isfile(f)]


class FileAttributes:
    ReadOnly = 1
    Normal = 128


class File:
    @staticmethod
    def Exists(filename):
        return os.path.exists(filename)

    @staticmethod
    def Copy(srcFileName, destFileName, overwrite=False):
        if overwrite and os.path.exists(destFileName):
            os.remove(destFileName)
        import shutil

        shutil.copyfile(srcFileName, destFileName)

    @staticmethod
    def Delete(filename):
        os.remove(filename)

    @staticmethod
    def ReadAllBytes(filename):
        with open(filename, "rb") as f:
            return bytearray(f.read())

    @staticmethod
    def WriteAllBytes(filename, content):
        with open(filename, "wb") as f:
            return f.write(content)

    @staticmethod
    def SetAttributes(filename, attributes):
        if attributes == FileAttributes.ReadOnly:
            from stat import S_IREAD

            os.chmod(filename, S_IREAD)
        elif attributes == FileAttributes.Normal:
            from stat import S_IWRITE, S_IREAD

            os.chmod(filename, S_IWRITE | S_IREAD)
        else:
            raise Exception(f"unsupported call to File.SetAttributes, filename={filename}, attributes={attributes}")

    @staticmethod
    def OpenText(filename):
        streamReader = StreamReader(filename)
        streamReader.OpenText()
        return streamReader


class Directory:
    @staticmethod
    def Exists(path):
        return os.path.isdir(path) and os.path.exists(path)

    @staticmethod
    def CreateDirectory(path):
        return os.makedirs(path)

    @staticmethod
    def Delete(path, recursive):
        if recursive:
            import shutil

            shutil.rmtree(path, ignore_errors=True)
        else:
            os.rmdir(path)


class EncodingAscii:
    @staticmethod
    def GetBytes(str):
        return bytearray(str, encoding="ascii")


class Encoding:
    @staticproperty
    def ASCII():
        return EncodingAscii()


class Application:
    def DoEvents():
        EngineLifetimeManager.UpdateWindow()


class IAgAppProvider:
    pass


class PythonStkApplicationProvider(IAgAppProvider):
    Target = TestTarget.eStk

    Application = None

    def __init__(self, stk, root):
        self.stk = stk
        PythonStkApplicationProvider.Application = root

    def CreateApplication(self, ignored):
        return self.stk.Root

    def InstantiateStkObjectModelContext(self):
        return self.stk.NewObjectModelContext()


class PythonStkXApplicationProvider(IAgAppProvider):
    Target = TestTarget.eStkX

    Application = None

    def __init__(self, stk, root):
        self.stk = stk
        PythonStkXApplicationProvider.Application = root

    def CreateApplication(self, ignored):
        return self.stk.NewObjectRoot()

    def InstantiateStkObjectModelContext(self):
        return self.stk.NewObjectModelContext()

    def InstantiateSTKXApplication(self):
        return self.stk


class PythonStkXNoGfxApplicationProvider(IAgAppProvider):
    Target = TestTarget.eStkNoGfx

    Application = None

    def __init__(self, stk, root):
        self.stk = stk
        PythonStkXNoGfxApplicationProvider.Application = root

    def CreateApplication(self, ignored):
        return self.stk.NewObjectRoot()

    def InstantiateStkObjectModelContext(self):
        return self.stk.NewObjectModelContext()


class TestBase(unittest.TestCase):
    Application = None
    stk = None
    root = None
    logger = Logger()
    NoGraphicsMode = True
    Units = None
    OriginalAccConstraintPaths = []

    CurrentDirectory = None
    CodeBaseDir = None
    ScenarioDirectory = None
    NonSupportedDirectory = None
    DataProvidersDirectory = None

    ScenarioDirName = "data"

    ApplicationProvider = None
    Target = None

    _tempDirectory = None
    _stkHomeDir = None
    _stkDbDir = None

    @staticmethod
    def Initialize():
        TestBase.stk = EngineLifetimeManager.Initialize()
        if EngineLifetimeManager.target == TestTarget.eStk:
            TestBase.root = TestBase.stk.Root
        else:
            TestBase.root = TestBase.stk.NewObjectRoot()

        TestBase.root.NewScenario("Snippet")
        parent = TestBase.root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "parent")
        parent.Propagator.Propagate()
        accessConstraints = parent.AccessConstraints

        TestBase.Application = TestBase.root
        TestBase.Units = TestBase.Application.UnitPreferences

        TestBase.CurrentDirectory = TestBase._GetTestBaseDirectory()
        TestBase.CodeBaseDir = TestBase.CurrentDirectory
        TestBase.ScenarioDirectory = Path.Combine(TestBase.CodeBaseDir, TestBase.ScenarioDirName)
        TestBase.NonSupportedDirectory = Path.Combine(TestBase.ScenarioDirectory, "NonSupportedScen")
        TestBase.DataProvidersDirectory = Path.Combine(TestBase.ScenarioDirectory, "DataProviders")

        if EngineLifetimeManager.target == TestTarget.eStk:
            TestBase.ApplicationProvider = PythonStkApplicationProvider(TestBase.stk, TestBase.root)
            TestBase.NoGraphicsMode = False
        elif EngineLifetimeManager.target == TestTarget.eStkX:
            TestBase.ApplicationProvider = PythonStkXApplicationProvider(TestBase.stk, TestBase.root)
            TestBase.NoGraphicsMode = False
        elif EngineLifetimeManager.target == TestTarget.eStkNoGfx:
            TestBase.ApplicationProvider = PythonStkXNoGfxApplicationProvider(TestBase.stk, TestBase.root)
        TestBase.Target = TestBase.ApplicationProvider.Target

    @staticproperty
    def TemporaryDirectory():
        if TestBase._tempDirectory == None:
            import tempfile

            TestBase._tempDirectory = tempfile.TemporaryDirectory()
        return TestBase._tempDirectory.name

    @staticmethod
    def Uninitialize():
        EngineLifetimeManager.UpdateWindow()

        if TestBase.root.CurrentScenario is not None:
            TestBase.root.CloseScenario()
        TestBase.root = None
        TestBase.Application = None
        EngineLifetimeManager.Uninitialize()

    @staticmethod
    def LoadTestScenario(path):
        if TestBase.Application.CurrentScenario is not None:
            TestBase.Application.CloseScenario()
        TestBase.ScenarioDirectory = Path.Combine(TestBase.CodeBaseDir, TestBase.ScenarioDirName)
        baseScenario = TestBase.GetScenarioFile(path)
        TestBase.Application.LoadScenario(baseScenario)
        if Path.GetDirName(path):
            TestBase.ScenarioDirectory = Path.Combine(
                TestBase.CodeBaseDir, TestBase.ScenarioDirName, Path.GetDirName(path)
            )
        TestBase.Application.UnitPreferences.ResetUnits()

    @staticmethod
    def LoadBaseScenario():
        TestBase.ScenarioDirectory = Path.Combine(TestBase.CodeBaseDir, TestBase.ScenarioDirName)
        TestBase.LoadTestScenario("Scenario1.sc")

        ac1: IAircraft = clr.CastAs(TestBase.Application.CurrentScenario.Children["Boing737"], IAircraft)
        ac1.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        ga: IVehiclePropagatorGreatArc = clr.CastAs(ac1.Route, IVehiclePropagatorGreatArc)
        ga.Method = AgEVeWayPtCompMethod.eDetermineVelFromTime
        wpe = ga.Waypoints.Add()
        wpe.Latitude = 0
        wpe.Longitude = 0
        wpe.Time = "1 Jul 1999 00:00:00.000"
        wpe = ga.Waypoints.Add()
        wpe.Latitude = 10
        wpe.Longitude = 20
        wpe.Time = "1 Jul 1999 00:55:00.000"
        ga.Propagate()
        gv1: IGroundVehicle = clr.CastAs(
            TestBase.Application.CurrentScenario.Children["GroundVehicle1"], IGroundVehicle
        )
        gv1.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        ga: IVehiclePropagatorGreatArc = clr.CastAs(gv1.Route, IVehiclePropagatorGreatArc)
        ga.Method = AgEVeWayPtCompMethod.eDetermineVelFromTime
        wpe = ga.Waypoints.Add()
        wpe.Latitude = 0
        wpe.Longitude = 0
        wpe.Time = "1 Jul 1999 00:00:00.000"
        wpe = ga.Waypoints.Add()
        wpe.Latitude = 10
        wpe.Longitude = 20
        wpe.Time = "1 Jul 1999 00:55:00.000"
        ga.Propagate()
        sh1: IShip = clr.CastAs(TestBase.Application.CurrentScenario.Children["Ship1"], IShip)
        sh1.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        ga: IVehiclePropagatorGreatArc = clr.CastAs(sh1.Route, IVehiclePropagatorGreatArc)
        ga.Method = AgEVeWayPtCompMethod.eDetermineVelFromTime
        wpe = ga.Waypoints.Add()
        wpe.Latitude = 0
        wpe.Longitude = 0
        wpe.Time = "1 Jul 1999 00:00:00.000"
        wpe = ga.Waypoints.Add()
        wpe.Latitude = 10
        wpe.Longitude = 20
        wpe.Time = "1 Jul 1999 00:55:00.000"
        ga.Propagate()
        ms1: IMissile = clr.CastAs(TestBase.Application.CurrentScenario.Children["Missile1"], IMissile)
        ms1.SetTrajectoryType(AgEVePropagatorType.ePropagatorBallistic)
        ballistic: IVehiclePropagatorBallistic = clr.CastAs(ms1.Trajectory, IVehiclePropagatorBallistic)
        ballistic.Step = 59
        ballistic.Propagate()
        lt: ILineTarget = clr.CastAs(TestBase.Application.CurrentScenario.Children["LineTarget2"], ILineTarget)
        lt.Points.Add(0, 0)
        lt.Points.Add(2, 2)

    @staticmethod
    def _GetTestBaseDirectory():
        return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

    @staticmethod
    def GetScenarioFile(path):
        return os.path.abspath(os.path.join(TestBase.ScenarioDirectory, path))

    @staticmethod
    def GetScenarioRootDir():
        return os.path.abspath(os.path.join(TestBase._GetTestBaseDirectory(), TestBase.ScenarioDirName))

    def CreateApplication(self, ignored):
        return TestBase.ApplicationProvider.CreateApplication(ignored)

    @staticmethod
    def PathCombine(*paths):
        result = None
        for path in paths:
            if result is None:
                result = path
            else:
                result = Path.Combine(result, path)
        return result

    @staticmethod
    def GetSTKDBDir():
        if TestBase._stkDbDir is None:
            databaseDir = TestBase.Application.ExecuteCommand("GetDB /")[0]
            if os.path.exists(os.path.join(databaseDir, "Databases")):
                # user config
                TestBase._stkDbDir = databaseDir
            elif os.path.exists(os.path.join(TestBase.GetSTKHomeDir(), "Databases")):
                # install directory
                TestBase._stkDbDir = TestBase.GetSTKHomeDir()
            else:
                # all users
                TestBase._stkDbDir = os.path.join(os.environ["ALLUSERSPROFILE"], "AGI", "STK 12")
            print(f"Using STKDB={TestBase._stkDbDir}")
        return TestBase._stkDbDir

    @staticmethod
    def GetSTKHomeDir():
        if TestBase._stkHomeDir is None:
            TestBase._stkHomeDir = TestBase.Application.ExecuteCommand("GetSTKHomeDir /")[0]
            print(f"Using STKHOMEDIR={TestBase._stkHomeDir}")
        return TestBase._stkHomeDir

    def setUp(self):
        TestBase.Application.UnitPreferences.ResetUnits()

    def tearDown(self):
        EngineLifetimeManager.UpdateWindow()

    @staticmethod
    def CleanupUserDirectory():
        pass

    class GravModel(enum.IntEnum):
        unknown = 0
        WGS84_EGM96 = 1
        EGM2008 = 2

    @property
    def EarthGravModel(self):
        sc = clr.Convert(TestBase.Application.CurrentScenario, IScenario)
        cbEarth: IAstrogatorCentralBody = clr.CastAs(
            sc.ComponentDirectory.GetComponents(AgEComponent.eComponentAstrogator).GetFolder("Central Bodies")["Earth"],
            IAstrogatorCentralBody,
        )
        if cbEarth.DefaultGravityModelName == "EGM2008":
            return TestBase.GravModel.EGM2008
        elif cbEarth.DefaultGravityModelName == "WGS84 EGM96":
            return TestBase.GravModel.WGS84_EGM96
        else:
            raise Exception("New cb file detected, need to check the numbers.")

    @property
    def HasUnderseaLicense(self):
        licenseResults = TestBase.Application.ExecuteCommand("GetLicenses /")
        for licenseResult in licenseResults:
            if "Undersea" in licenseResult:
                if "Excluded" in licenseResult:
                    return False
                else:
                    return not "No License" in licenseResult
        return False

    @staticmethod
    def DoEvents():
        Application.DoEvents()

    @staticmethod
    def DoubleQuoted(s):
        return f'"{s}"'

    @staticmethod
    def IsPythonLanguage():
        return True


class Stopwatch:
    def __init__(self):
        self.start = None
        self.stop = None

    def Start(self):
        import time

        self.start = time.perf_counter()

    def Stop(self):
        import time

        self.stop = time.perf_counter()

    @property
    def ElapsedMilliseconds(self):
        return (self.stop - self.start) * 1000.0


class OSHelper:
    @staticmethod
    def Is64Bit():
        return True

    @staticmethod
    def IsLinux():
        from sys import platform

        return platform.startswith("linux")


class TimeSpan:
    def __init__(self, time):
        self.time = time

    def ToString(self):
        return str(self.time)


class DateTime:
    def __init__(self, dateTime):
        self.dateTime = dateTime

    @staticproperty
    def Now():
        return DateTime(datetime.now())

    @property
    def TimeOfDay(self):
        return TimeSpan(self.dateTime.time())

    def ToString(self, format="%Y-%m-%d %H:%M:%S"):
        return self.dateTime.strftime(format)

    @property
    def Ticks(self):
        return (self.dateTime - datetime(1, 1, 1)).total_seconds() * 10000000

    def Subtract(self, other):
        return DateTime(self.dateTime - other.dateTime)

    def AddSeconds(self, value):
        return DateTime(self.dateTime + timedelta(0, value))

    def __lt__(self, other):
        return self.dateTime < other

    def __gt__(self, other):
        return self.dateTime > other


class Random:
    def __init__(self, seed=None):
        import random

        self.generator = random.Random(seed)

    def Next(self, minValue, maxValue=sys.maxsize):
        return self.generator.randint(minValue, maxValue)


class Object:
    @staticmethod
    def ReferenceEquals(objA, objB):
        return objA is objB

    @staticmethod
    def GetType(obj):
        return type(obj)


class Array:
    @staticmethod
    def CreateInstance(elementType, length1, length2=0):
        if length2 > 0:
            return [[0 for x in range(length2)] for y in range(length1)]
        else:
            return [0 for x in range(length1)]

    @staticmethod
    def IndexOf(collection, item):
        return collection.index(item) if item in collection else -1

    @staticmethod
    def Create(count):
        return [None for x in range(count)]

    @staticmethod
    def Rank(array):
        rank = 1
        if len(array) > 0:
            element1 = array[0]
            if isinstance(element1, list):
                rank = 2
                if len(element1) > 0:
                    element2 = element1[0]
                    if isinstance(element2, list):
                        rank = 3
        return rank

    @staticmethod
    def Length(array):
        length = len(array)
        if length > 0:
            element1 = array[0]
            if isinstance(element1, list):
                len2 = len(element1)
                length *= len2
                if len2 > 0:
                    element2 = element1[0]
                    if isinstance(element2, list):
                        length *= len(element2)
        return length

    @staticmethod
    def Sort(array):
        return array.sort()

    @staticmethod
    def BinarySearch(array, element):
        import bisect

        index = bisect.bisect(array, element) - 1
        return index if array[index] == element else -1

    @staticmethod
    def CopyTo(arrayFrom, arrayTo, arrayToIndex):
        j = arrayToIndex
        for i in range(0, len(arrayFrom)):
            arrayTo[j] = arrayFrom[i]
            j += 1

    @staticmethod
    def ForEach(array, func):
        for element in array:
            func(element)


class Enumerable:
    @staticmethod
    def ToList(l):
        if type(l) == tuple:
            return list(*l)
        else:
            return list(l)

    @staticmethod
    def Contains(source, value):
        return value in source


class List:
    @staticmethod
    def Sort(list, cmp=None):
        if cmp is None:
            list.sort()
        else:
            from functools import cmp_to_key

            list = sorted(list, key=cmp_to_key(cmp))

    @staticmethod
    def Remove(list, element):
        if element in list:
            list.remove(element)
            return True
        else:
            return False


class TestContext:
    @staticproperty
    def CurrentContext():
        return TestContext()

    @property
    def TestDirectory(self):
        return TestBase.CurrentDirectory


def cmp(a, b):
    return (a > b) - (a < b)


class GroupCollection:
    def __init__(self, match):
        self.match = match

    def __getitem__(self, index):
        if isinstance(index, int):
            return list(self.match.groups())[index - 1]
        return self.match.groupdict()[index]


class Match:
    def __init__(self, value):
        self.value = value

    @property
    def Value(self):
        return self.value

    @property
    def Groups(self):
        return GroupCollection(self.value)


class MatchCollection:
    def __init__(self, matches):
        self.matches = matches

    @property
    def Count(self):
        return len(self.matches)

    def __getitem__(self, index):
        return self.matches[index]


class Regex:
    def __init__(self, pattern):
        self.pattern = re.sub(r"\(\?<(\w*)>", r"(?P<\1>", pattern)  # replaces ?<id> with ?P<id>

    def Match(self, input):
        return Match(re.match(self.pattern, input))

    @staticmethod
    def Matches(input, pattern):
        return MatchCollection([Match(m) for m in re.findall(pattern, input)])

    @staticmethod
    def IsMatch(input, pattern):
        return re.match(pattern, input) is not None

    @staticmethod
    def Replace(input, pattern, replacement):
        p = re.compile(pattern)
        p.sub(replacement, input)


class Environment:
    @staticproperty
    def NewLine():
        return os.linesep


class StackFrame:
    def __init__(self):
        import inspect

        self.frameinfos = inspect.getouterframes(inspect.currentframe())

    def GetMethod(self):
        class Method:
            def __init__(self, name):
                self.name = name

            @property
            def Name(self):
                return self.name

            def __str__(self):
                return self.name

        return Method(self.frameinfos[1].function)


class LocalTimeZoneInfo:
    @staticmethod
    def IsDaylightSavingTime(dateTime):
        localtimezone = pytz.timezone("US/Eastern")
        localjan1st = localtimezone.localize(datetime(datetime.now().year, 1, 1, 0, 0, 0))
        localDateTime = localtimezone.localize(dateTime.dateTime)
        return not (localDateTime.utcoffset() == localjan1st.utcoffset())


class TimeZoneInfo:
    @staticproperty
    def Local():
        return LocalTimeZoneInfo()


class CSToJavaArrayHelper:
    def ToOneDimensionalObjectArray(obj):
        if isinstance(obj, list):
            result = []
            for e in obj:
                if isinstance(e, list):
                    result.extend(CSToJavaArrayHelper.ToOneDimensionalObjectArray(e))
                else:
                    result.append(e)
            return result
        else:
            return obj


class DataProviderResultWriter(object):
    def __init__(self, result):
        self.outStr = ""
        self._result = result

    def Dump(self):
        self.WriteLine(0, "Result Info")
        self.WriteLine(0, "-----------")
        self.WriteLine(0, ("Category:" + str(self._result.Category)))
        if self._result.Category == AgEDrCategories.eDrCatIntervalList:
            self.DumpDPIntervalList(clr.Convert(self._result.Value, IDataProviderResultIntervalCollection), 1)
        elif self._result.Category == AgEDrCategories.eDrCatSubSectionList:
            self.DumpDPSubSectionList(clr.Convert(self._result.Value, IDataProviderResultSubSectionCollection), 1)
        elif self._result.Category == AgEDrCategories.eDrCatMessage:
            self.DumpDPMessage(clr.Convert(self._result.Value, IDataProviderResultTextMessage), 1)
        return Regex.Replace(self.outStr, "\n", "")

    def DumpDPIntervalList(self, intList, indent):
        index = 0
        for intrvl in intList:
            index += 1
            self.DumpInterval(intrvl, index, (indent + 1))

    def DumpDPSubSectionList(self, sections, indent):
        index = 0
        for section in sections:
            index += 1
            self.DumpDPSection(section, index, (indent + 1))

    def DumpDPSection(self, section, index, indent):
        self.WriteLine(indent, ((("Section #" + str(index)) + ": ") + section.Title))
        self.WriteLine(indent, "{")
        self.DumpDPIntervalList(section.Intervals, (indent + 1))
        self.WriteLine(indent, "}")

    def DumpDPMessage(self, msgContainer, indent):
        self.WriteLine(indent, "Message ")
        self.WriteLine(indent, "{")
        i = 0
        while i < msgContainer.Count:
            self.WriteLine(indent, clr.Convert(msgContainer[i], str))
            i += 1
        self.WriteLine(indent, "}")

    def DumpDPDataSet(self, ds, index, indent):
        self.WriteLine(indent, ("  DataSet #" + str(index)))
        self.WriteLine(indent, "  {")
        self.WriteLine(indent, ("    Element Name:  " + ds.ElementName))
        self.WriteLine(indent, ("    Dimension Name:     " + ds.DimensionName))
        self.WriteLine(indent, ("    # of elements: " + str(ds.Count)))
        self.WriteStr(indent, "    values:       [")
        values = ds.GetValues()
        for d in values:
            if d != values[0]:
                Console.Write(", ")
            Console.Write(d)
        Console.WriteLine("]")
        self.WriteLine(indent, "  }")

    def DumpDPDataSetList(self, datasets, indent):
        Console.WriteLine("DumpDPDataSetList: Num elements in collection: {0}", str(datasets.Count))
        i = 0
        while i < datasets.Count:
            dataset = datasets[i]
            Console.WriteLine(dataset.ElementName)
            i += 1
        Console.WriteLine("DumpDPDataSetList: Num rows in datasetcollection: {0}", str(datasets.RowCount))
        i = 0
        while i < datasets.RowCount:
            arRow = datasets.GetRow(i)
            for obj in arRow:
                Console.WriteLine("    Row({0}): {1}", i, str(obj))
            i += 1
        arArray = datasets.ToArray()
        for obj in arArray:
            Console.WriteLine("    Row: {0}", str(obj))
        arElementNames = datasets.ElementNames
        for elementName in arElementNames:
            Console.WriteLine("DumpDPDataSetList: elementName: {0}", elementName)
        index = 0
        for ds in datasets:
            index += 1
            self.DumpDPDataSet(ds, index, indent)
            self.WriteLine(indent, "DataSets Count: " + str(ds.Count))
            self.WriteLine(indent, "DataSets GetValues Length: " + str(len(ds.GetValues())))

    def DumpInterval(self, interval, index, indent):
        self.WriteLine(indent, ("Interval #" + str(index)))
        self.WriteLine(indent, "{")
        self.WriteLine(
            indent,
            "  start="
            + str(interval.StartTime)
            + ", stop="
            + str(interval.StopTime)
            + ", #datasets="
            + str(interval.DataSets.Count),
        )
        self.DumpDPDataSetList(interval.DataSets, (indent + 1))
        self.WriteLine(indent, "}")

    def WriteLine(self, indent, strMsg):
        indentStr = " " * (4 * indent)
        Console.WriteLine("{0}{1}", indentStr, strMsg)
        self.outStr += strMsg

    def WriteStr(self, indent, strMsg):
        indentStr = " " * (4 * indent)
        Console.Write("{0}{1}", indentStr, strMsg)
        self.outStr += strMsg


class CategoryManager:
    included_categories = []
    excluded_categories = []

    @staticmethod
    def AddIncludedCategory(name):
        CategoryManager.included_categories.append(name)

    @staticmethod
    def AddExcludedCategory(name):
        CategoryManager.excluded_categories.append(name)

    @staticmethod
    def IsIncluded(name):
        if len(CategoryManager.included_categories) > 0:
            return name in CategoryManager.included_categories
        else:
            return True

    @staticmethod
    def IsExcluded(name):
        if len(CategoryManager.excluded_categories) > 0:
            return name in CategoryManager.excluded_categories
        else:
            return False


def category(name):
    if not CategoryManager.IsIncluded(name):
        return unittest.skip(f'Category "{name}" is not included')
    elif CategoryManager.IsExcluded(name):
        return unittest.skip(f'Category "{name}" is excluded')
    else:

        def _identity(obj):
            return obj

        return _identity


class ExceptionMessageMatch(enum.IntEnum):
    Exact = 0
    Contains = 1
    StartsWith = 2
    NoException = 3
