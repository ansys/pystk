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
#

# """Test the dates module."""

import pytest

from ansys.stk.extensions.data_analysis._dates import _STKDate

from stk_environment import stk_root

def test_date_spans_over_leap_second(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, '30 Jun 2015 23:59:59')
    date2 = _STKDate.from_value_and_format(stk_root, '30 Jun 2015 23:59:60')
    date3 = _STKDate.from_value_and_format(stk_root, '1 Jul 2015 00:00:00')

    assert date2 - date1 == 1.0
    assert date3 - date2 == 1.0
    assert date3 - date1 == 2.0

def test_date_spans_not_over_leap_second(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, '30 Jun 2015 23:58:57')
    date2 = _STKDate.from_value_and_format(stk_root, '30 Jun 2015 23:58:59')

    assert date2 - date1 == 2.0
    assert date1 - date2 == -2.0

def test_date_additions_over_leap_second(stk_root):
    date = _STKDate.from_value_and_format(stk_root, '30 Jun 2015 23:59:59')

    assert (date + 1.0).get_utcg() == '30 Jun 2015 23:59:60.000'
    assert (date + 2.0).get_utcg() == '1 Jul 2015 00:00:00.000'

def test_date_additions_not_over_leap_second(stk_root):
    date = _STKDate.from_value_and_format(stk_root, '30 Jun 2015 23:58:59')

    assert (date + 1.0).get_utcg() == '30 Jun 2015 23:59:00.000'
    assert (date + 2.0).get_utcg() == '30 Jun 2015 23:59:01.000'

def test_date_format(stk_root):
    date = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    assert date.format("TAIJ") == "170/25 16:00:37.000"
    assert date.format("YYYYDDD") == "2025170.160000"

def test_dates_less_than(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = _STKDate.from_value_and_format(stk_root, "20 Jun 2025 16:00:00.000")
    assert date1 < date2
    assert not (date2 < date1)
    date3 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:59.000")
    date4 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:60.000")
    assert date3 < date4

def test_dates_less_than_not_implemented(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = 47
    result = date1.__lt__(date2)
    assert result is NotImplemented
    date3 = "19 Jun 2025 16:00:00.000"
    result = date1.__lt__(date3)
    assert result is NotImplemented
    with pytest.raises(TypeError) as excinfo:
        date3 < date1
    assert "'<' not supported between instances" in str(excinfo.value)

def test_dates_greater_than(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = _STKDate.from_value_and_format(stk_root, "20 Jun 2025 16:00:00.000")
    assert date2 > date1
    assert not (date1 > date2)
    date3 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:59.000")
    date4 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:60.000")
    assert date4 > date3

def test_dates_greater_than_not_implemented(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = 47
    result = date1.__gt__(date2)
    assert result is NotImplemented
    date3 = "19 Jun 2025 16:00:00.000"
    result = date1.__gt__(date3)
    assert result is NotImplemented
    with pytest.raises(TypeError) as excinfo:
        date1 > date3
    assert "'>' not supported between instances" in str(excinfo.value)

def test_dates_greater_equal(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = _STKDate.from_value_and_format(stk_root, "20 Jun 2025 16:00:00.000")
    assert date2 >= date1
    assert not (date2 <= date1)
    date3 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:59.000")
    date4 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:60.000")
    assert date4 >= date3

def test_dates_greater_equal_not_implemented(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = 47
    result = date1.__ge__(date2)
    assert result is NotImplemented
    date3 = "19 Jun 2025 16:00:00.000"
    result = date1.__ge__(date3)
    assert result is NotImplemented
    with pytest.raises(TypeError) as excinfo:
        date1 >= date3
    assert "'>=' not supported between instances" in str(excinfo.value)

def test_dates_equality(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date3 = _STKDate.from_value_and_format(stk_root, "20 Jun 2025 16:00:00.000")
    assert date1 == date2
    assert date1 != date3
    date3 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:59.000")
    date4 = _STKDate.from_value_and_format(stk_root, "30 Jun 2015 23:59:60.000")
    assert date3 != date4

def test_dates_equal_not_implemented(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = 47
    result = date1.__eq__(date2)
    assert result is NotImplemented
    date3 = "19 Jun 2025 16:00:00.000"
    result = date1.__eq__(date3)
    assert result is NotImplemented

def test_get_epsec(stk_root):
    date1 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:00:00.000")
    date2 = _STKDate.from_value_and_format(stk_root, "19 Jun 2025 16:01:00.000")
    assert date2.get_epsec() - date1.get_epsec() == 60.0