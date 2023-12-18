import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.stkobjects import *


@category("CategoryA")
class ClassA(unittest.TestCase):

    @category("CategoryB")
    def test_One(self):
        pass

    def test_Two(self):
        pass

class ClassB(unittest.TestCase):

    @category("CategoryB")
    def test_One(self):
        pass

    def test_Two(self):
        pass



# Excluded      Included      Tests to run
# -             -             One+Two
# CategoryA     -             -
# CategoryB     -             Two
# -             CategoryA     Two
# -             CategoryB     One