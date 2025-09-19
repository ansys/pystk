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

"""Contains specific exceptions that may be raised from the STK API."""


class STKInitializationError(RuntimeError):
    """Raised in STKDesktop and STKEngine when unable to initialize or attach to STK."""

class STKInvalidCastError(RuntimeError):
    """Raised when attempting to cast an object to an unsupported interface or class type."""

class STKRuntimeError(RuntimeError):
    """Raised when an STK method call fails."""

class STKAttributeError(AttributeError):
    """Raised when attempting to set an unrecognized attribute within the STK API."""

class STKEventsAPIError(SyntaxError):
    """Raised when attempting to assign to an STK Event rather than using operator += or -=."""

class STKPluginMethodNotImplementedError(SyntaxError):
    """Raised when a plugin method is called by STK that was not implemented by the user."""

class STKInvalidTimerError(RuntimeError):
    """Raised when attempting to use an engine timer that cannot be implemented."""

class STKColorError(RuntimeError):
    """Raised when a problem is encountered with color classes."""

class GrpcUtilitiesError(SyntaxError):
    """Raised when using gRPC utilities in an unsupported manner."""
