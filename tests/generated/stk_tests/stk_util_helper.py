import pytest
from test_util import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class STKUtilHelper(object):
    m_logger = Logger.Instance

    @staticmethod
    def TestComponent(comp: "IComponentInfo", isReadOnly: bool):
        Assert.assertIsNotNone(comp.name)
        Assert.assertIsNotNone(comp.user_comment)
        if isReadOnly:
            with pytest.raises(Exception):
                comp.name = "Test"
            with pytest.raises(Exception):
                comp.user_comment = "Test"
            desc: str = comp.description
            readOnly: bool = comp.is_read_only()

        else:
            oldName: str = comp.name
            oldUserComment: str = comp.user_comment

            comp.name = "TestName"
            Assert.assertEqual("TestName", comp.name)
            comp.user_comment = "UserComment"
            Assert.assertEqual("UserComment", comp.user_comment)
            desc: str = comp.description
            readOnly: bool = comp.is_read_only()

            comp.name = oldName
            comp.user_comment = oldUserComment

            cloneable: "ICloneable" = clr.CastAs(comp, ICloneable)
            if cloneable != None:
                clone: typing.Any = cloneable.clone_object()

    @staticmethod
    def TestDoublesCollection(dc: "DoublesCollection", value: float, min: float, max: float):
        with pytest.raises(Exception):
            dc.add((min - 1e-06))
        with pytest.raises(Exception):
            dc.add((max + 1e-06))

        origCount: int = dc.count
        arDoubles = dc.to_array()  # save off the doubles
        if dc.count > 0:
            with pytest.raises(Exception):
                dc.remove_at(dc.count)

            dHold: float = dc[0]
            dc.remove_at(0)
            Assert.assertEqual((origCount - 1), dc.count)
            dc.add(dHold)
            Assert.assertEqual(origCount, dc.count)

            dc.add(dHold)  # attempt to add a dup. Count should not change.
            Assert.assertEqual(origCount, dc.count)

            dc.set_at(0, value)  # change the first element to the new value (then the collection is sorted)
            Assert.assertEqual(origCount, dc.count)

            with pytest.raises(Exception):
                dc.set_at(dc.count, value)

            found: bool = False
            d: float
            for d in dc:
                if d == value:
                    found = True
                    break

            Assert.assertTrue(found)

            dc.remove_all()
            Assert.assertEqual(0, dc.count)

            d: float

            for d in arDoubles:
                dc.add(d)  # put them back in

            i: int = 0
            while i < dc.count:
                Assert.assertEqual(dc[i], arDoubles[i])  # verify they all got back in

                i += 1
