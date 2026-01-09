# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Module for unifying the launching of STK."""

from enum import Enum, unique
from typing import TypeAlias

from ansys.stk.core.stkengine import STKEngine, STKEngineApplication
from ansys.stk.core.stkdesktop import STKDesktop, STKDesktopApplication
from ansys.stk.core.stkruntime import STKRuntime, STKRuntimeApplication


STKApplication: TypeAlias = STKEngineApplication | STKDesktopApplication | STKRuntimeApplication
"""Type alias for supported STK application instances."""

# TODO: use StrEnum when minimum Python version is 3.11
@unique
class STKApplicationType(str, Enum):
    """Supported STK application types."""

    ENGINE = "engine"
    """Launch STK without the graphical user interface."""

    DESKTOP = "desktop"
    """Launch STK with the graphical user interface."""

    RUNTIME = "runtime"
    """Launch STK out-of-process using gRPC."""


def launch_stk(mode: STKApplicationType | str, **configuration) -> STKApplication:
    """Launch STK based on the configured application type.

    Parameters
    ----------
    mode : STKApplicationType | str
        The mode in which to launch STK.
    **configuration : dict, default: None
        Supported configuration for the selected launch mode. For allowable
        keyword arguments, see the corresponding methods for each mode:

        * For ``ENGINE`` mode, see the :func:`ansys.stk.core.stkengine.STKEngine.start_application` method.
        * For ``DESKTOP`` mode, see the :func:`ansys.stk.core.stkdesktop.STKDesktop.start_application` method.
        * For ``RUNTIME`` mode, see the :func:`ansys.stk.core.stkruntime.STKRuntime.start_application` method.

    Returns
    -------
    STKApplication
        An instance of the launched STK application.

    Raises
    ------
    ValueError
        If an unsupported application type is configured.
    """
    # Normalize mode to STKApplicationType
    if isinstance(mode, str):
        try:
            mode = STKApplicationType(mode)
        except ValueError as exc:
            raise ValueError(f"Unsupported STK application type: {mode!r}") from exc
    if not isinstance(mode, STKApplicationType):
        raise ValueError(
            "Mode must be an instance of STKApplicationType or a valid string value."
        )

    # Dispatch to the appropriate launcher
    if mode == STKApplicationType.ENGINE:
        stk = STKEngine
    elif mode == STKApplicationType.DESKTOP:
        stk = STKDesktop
    elif mode == STKApplicationType.RUNTIME:
        stk = STKRuntime

    return stk.start_application(**configuration)
