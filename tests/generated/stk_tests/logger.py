from test_util import *


class Logger(object):
    instance = None

    def __init__(self, *args, **kwargs):
        self._Enabled = None
        self.m_LogFilename = None
        loggingEnabled = ConfigurationManager.AppSettings.Get("loggingEnabled")
        logFilePrefix = ConfigurationManager.AppSettings.Get("logFilePrefix")

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
            dir = Path.GetDirectoryName(self.m_LogFilename)
            if not Directory.Exists(dir):
                Directory.CreateDirectory(dir)

    def ResetLog(self):
        if File.Exists(self.LogFilename):
            File.Delete(self.LogFilename)

    def Write(self, line):
        if self.Enabled:
            Console.Write(line)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(line)

    def Write2(self, format, s):
        if self.Enabled:
            Console.Write(format, s)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(format, s)

    def Write3(self, format, i):
        if self.Enabled:
            Console.Write(format, i)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(format, i)

    def Write4(self, format, obj1, obj2):
        if self.Enabled:
            Console.Write(format, obj1, obj2)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.Write(format, obj1, obj2)

    def WriteLine(self, line):
        if self.Enabled:
            Console.WriteLine(line)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line)

    def WriteLine2(self, obj):
        if self.Enabled:
            Console.WriteLine(obj)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(obj)

    def WriteLine3(self, line, i):
        if self.Enabled:
            Console.WriteLine(line, i)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line)

    def WriteLine4(self, line, b):
        if self.Enabled:
            Console.WriteLine(line, b)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line, b)

    def WriteLine5(self, line, s):
        if self.Enabled:
            Console.WriteLine(line, s)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(line, s)

    def WriteLine6(self, format, obj1):
        if self.Enabled:
            Console.WriteLine(format, obj1)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1)

    def WriteLine7(self, format, obj1, obj2):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1, obj2)

    def WriteLine8(self, format, obj1, obj2, obj3):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2, obj3)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1, obj2, obj3)

    def WriteLine9(self, format, obj1, obj2, obj3, obj4):
        if self.Enabled:
            Console.WriteLine(format, obj1, obj2, obj3, obj4)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, obj1, obj2, obj3, obj4)

    def WriteLine10(self, format, *args):
        if self.Enabled:
            Console.WriteLine(format, args)
            with StreamWriter(self.LogFilename, True) as writer:
                writer.WriteLine(format, args)
