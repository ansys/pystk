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

"""Information for a specific call captured while recording."""


class CallRecord:
    """Capture the information for a specific call."""

    def __init__(
        self,
        filename,
        type_name,
        member_name,
        lineno,
        end_lineno,
        col_offset,
        end_col_offset,
    ):
        """Construct a new CallRecord."""
        self.filename = filename
        self.type_name = type_name
        self.member_name = member_name
        self.lineno = lineno
        self.end_lineno = end_lineno
        self.col_offset = col_offset
        self.end_col_offset = end_col_offset

    def __eq__(self, other):
        """Compare this object with another object for equality."""
        if isinstance(other, CallRecord):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        """Return the hash value for the object."""
        return hash(
            (
                self.filename,
                self.type_name,
                self.member_name,
                self.lineno,
                self.end_lineno,
                self.col_offset,
                self.end_col_offset,
            )
        )

    def __lt__(self, other):
        """
        Define the behavior of the less-than operator (<) for this class.

        Sort by order of appearance in the source file.
        """
        if isinstance(other, CallRecord):
            return (
                self.filename,
                self.lineno,
                self.col_offset,
                self.end_lineno,
                self.end_col_offset,
            ).__lt__(
                (
                    other.filename,
                    other.lineno,
                    other.col_offset,
                    other.end_lineno,
                    other.end_col_offset,
                )
            )
        return NotImplemented
