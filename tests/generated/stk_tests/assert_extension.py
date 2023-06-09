from test_util import *


class AssertEx(object):
    @staticmethod
    def AreEqual(expected, actual):
        Assert.assertEqual((expected._ToOLECOLOR() & 16777215), (actual._ToOLECOLOR() & 16777215))
