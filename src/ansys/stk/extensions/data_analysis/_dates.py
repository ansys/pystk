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

"""
PySTK Date Extension.

A set of utilities to facilitate the manipulation of dates and times in PySTK.
"""

from ansys.stk.core.stkobjects import STKObjectRoot
from ansys.stk.core.stkutil import ConversionUtility, Date, Quantity


class _STKDate:
    """Wrapper class associated with STK Date object."""

    def __init__(self, date: Date):
        """Create an STKDate object from Date."""
        self.stk_date: Date = date

    def __sub__(self, date: Date) -> float:
        """Subtract an STKDate, returning the time difference in seconds."""
        span : Quantity =  self.stk_date.span(date.stk_date)
        if span.unit != "sec":
            span.convert_to_unit("sec")
        return span.value

    def __lt__(self, other: "_STKDate"):
        """Compare STKDate to STKDate."""
        if isinstance(other, _STKDate):
            return self - other < 0
        return NotImplemented

    def __gt__(self, other: "_STKDate"):
        """Compare STKDate to STKDate."""
        if isinstance(other, _STKDate):
            return self - other > 0
        return NotImplemented

    def __ge__(self, other: "_STKDate"):
        """Compare STKDate to STKDate."""
        if isinstance(other, _STKDate):
            return self > other or self == other
        return NotImplemented

    def __eq__(self, other: "_STKDate"):
        """Compare equality of STKDates."""
        if isinstance(other, _STKDate):
            return self.get_utcg() == other.get_utcg()
        return NotImplemented

    def __add__(self, seconds: float) -> Date:
        """Add seconds to the date."""
        return _STKDate(self.stk_date.add("sec", seconds))

    def get_epsec(self) -> float:
        """Return the date in Epoch Seconds.

        Returns
        -------
        float
            The date in Epoch Seconds.

        """
        return float(self.stk_date.format('EpSec'))

    def get_utcg(self) -> str:
        """Return the date formatted in UTCG.

        Returns
        -------
        str
            The date formatted as UTCG.

        """
        return self.stk_date.format('UTCG')

    def format(self, unit: str) -> str:
        """Return the date formatted as any unit.

        Parameters
        ----------
        unit : str
            The unit to format the date as.

        Returns
        -------
        str
            The formatted date.

        """
        return self.stk_date.format(unit)


class _STKDateFactory:
    """Factory class to create STKDate objects."""
    def __init__(self, root: STKObjectRoot):
        """Create STKDateFactory."""
        self.conversion_utility : ConversionUtility = root.conversion_utility

    def new_date(self, value: str, unit: str = "UTCG") -> _STKDate:
        """Create a new STKDate object.

        Parameters
        ----------
        value : str
            String containing date to be parsed.
        unit : str
            String representing the unit the date is in (the default is UTCG).

        Returns
        -------
        ansys.stk.extensions.data_analysis.dates.STKDate
            The `STKDate` object.

        """
        return _STKDate(self.conversion_utility.new_date(unit, value))