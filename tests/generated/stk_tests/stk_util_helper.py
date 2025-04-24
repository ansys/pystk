# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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
        newName: str = Guid.NewGuid().ToString()  # Unique name string
        newComment: str = Guid.NewGuid().ToString()  # Unique comment string

        Assert.assertIsNotNone(comp.name)
        Assert.assertIsNotNone(comp.user_comment)
        if isReadOnly:
            with pytest.raises(Exception):
                comp.name = newName
            with pytest.raises(Exception):
                comp.user_comment = newComment
            Assert.assertTrue((len(comp.description) > 0))
            Assert.assertTrue(comp.is_read_only())

        else:
            oldName: str = comp.name
            oldUserComment: str = comp.user_comment

            comp.name = newName
            Assert.assertEqual(newName, comp.name)
            comp.user_comment = newComment
            Assert.assertEqual(newComment, comp.user_comment)
            Assert.assertTrue((len(comp.description) > 0))
            Assert.assertFalse(comp.is_read_only())

            cloneable: "ICloneable" = clr.CastAs(comp, ICloneable)
            if cloneable != None:
                clone: "IComponentInfo" = clr.CastAs(cloneable.clone_object(), IComponentInfo)
                Assert.assertIsNotNone(clone)

                Assert.assertEqual(comp.name, clone.name)
                Assert.assertEqual(comp.user_comment, clone.user_comment)
                Assert.assertEqual(comp.description, clone.description)
                Assert.assertFalse(clone.is_read_only())

            comp.name = oldName
            comp.user_comment = oldUserComment

    @staticmethod
    def TestComponentLinking(linkEmbedControl: "IComponentLinkEmbedControl", supportedComponentCount: int):
        Assert.assertEqual(supportedComponentCount, Array.Length(linkEmbedControl.supported_components))

        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.LINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, linkEmbedControl.reference_type)

        Assert.assertIsNotNone(linkEmbedControl.component)
        STKUtilHelper.TestComponent(linkEmbedControl.component, True)

        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, linkEmbedControl.reference_type)

        STKUtilHelper.TestComponent(linkEmbedControl.component, False)

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
