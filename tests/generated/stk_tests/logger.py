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


class Logger(object):
    instance = None

    def __init__(self, *args, **kwargs):
        self._Enabled = None
        self.m_LogFilename: str = None
        loggingEnabled: str = ConfigurationManager.AppSettings.Get("loggingEnabled")
        logFilePrefix: str = ConfigurationManager.AppSettings.Get("logFilePrefix")

        self.Enabled = loggingEnabled == "true"
        self.LogFilename = Path.Combine(Path.GetTempPath(), ((logFilePrefix + str(Guid.NewGuid())) + ".txt"))
        if self.Enabled:
            self.ResetLog()

    @staticproperty
    def Instance():
        if Logger.instance == None:
            Logger.instance = Logger()

        return Logger.instance

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, value):
        self._Enabled = value

    @property
    def LogFilename(self):
        return self.m_LogFilename

    @LogFilename.setter
    def LogFilename(self, value):
        self.m_LogFilename = value
        if self.Enabled:
            dir: str = Path.GetDirectoryName(self.m_LogFilename)
            if not Directory.Exists(dir):
                Directory.CreateDirectory(dir)

    def ResetLog(self):
        if File.Exists(self.LogFilename):
            File.Delete(self.LogFilename)

    def Write(self, line: str):
        if self.Enabled:
            Console.Write(line)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(line)

    def Write2(self, format: str, s: str):
        if self.Enabled:
            Console.Write(format, s)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(format, s)

    def Write3(self, format: str, i: int):
        if self.Enabled:
            Console.Write(format, i)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(format, i)

    def Write4(self, format: str, obj1: typing.Any, obj2: typing.Any):
        if self.Enabled:
            Console.Write(format, obj1, obj2)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(format, obj1, obj2)

    def WriteLine(self, line: str):
        if self.Enabled:
            Console.WriteLine(line)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line)

    def WriteLine2(self, obj: typing.Any):
        if self.Enabled:
            Console.WriteLine(obj)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(obj)

    def WriteLine3(self, line: str, i: int):
        if self.Enabled:
            Console.WriteLine(line, i)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line)

    def WriteLine4(self, line: str, b: bool):
        if self.Enabled:
            Console.WriteLine(line, b)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line, b)

    def WriteLine5(self, line: str, s: str):
        if self.Enabled:
            Console.WriteLine(line, s)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line, s)

    def WriteLine6(self, format: str, obj1: typing.Any):
        if self.Enabled:
            Console.WriteLine(format, obj1)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1)

    def WriteLine7(self, format: str, obj1: typing.Any, obj2: typing.Any):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1, obj2)

    def WriteLine8(self, format: str, obj1: typing.Any, obj2: typing.Any, obj3: typing.Any):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2, obj3)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1, obj2, obj3)

    def WriteLine9(self, format: str, obj1: typing.Any, obj2: typing.Any, obj3: typing.Any, obj4: typing.Any):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2, obj3, obj4)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1, obj2, obj3, obj4)

    def WriteLine10(self, format: str, *args: "List[typing.Any]"):
        if self.Enabled:
            Console.WriteLine(format, args)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, args)
