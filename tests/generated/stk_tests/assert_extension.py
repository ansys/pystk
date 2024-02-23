from test_util import *
from ansys.stk.core.utilities.colors import *


class AssertEx(object):
    @staticmethod
    def AreEqual(expected: Color, actual: Color):
        Assert.assertEqual((expected._to_ole_color() & 16777215), (actual._to_ole_color() & 16777215))
