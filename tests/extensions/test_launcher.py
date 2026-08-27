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

"""Tests for the launcher extension."""

from unittest.mock import MagicMock, patch

import pytest

from ansys.stk.extensions.launcher import (
    STKApplicationType,
    attach_to_application,
    launch_stk,
)

@patch("ansys.stk.extensions.launcher.STKEngine")
def test_launch_stk_engine_with_string(mock_engine):
    """Test launching STK in ENGINE mode using string mode."""
    mock_app = MagicMock()
    mock_engine.start_application.return_value = mock_app

    result = launch_stk(mode="engine", no_graphics=True)

    mock_engine.start_application.assert_called_once_with(no_graphics=True)
    assert result == mock_app


@patch("ansys.stk.extensions.launcher.STKEngine")
def test_launch_stk_engine_with_enum(mock_engine):
    """Test launching STK in ENGINE mode using enum mode."""
    mock_app = MagicMock()
    mock_engine.start_application.return_value = mock_app

    result = launch_stk(mode=STKApplicationType.ENGINE, no_graphics=True)

    mock_engine.start_application.assert_called_once_with(no_graphics=True)
    assert result == mock_app


@patch("ansys.stk.extensions.launcher.STKDesktop")
def test_launch_stk_desktop_with_string(mock_desktop):
    """Test launching STK in DESKTOP mode using string mode."""
    mock_app = MagicMock()
    mock_desktop.start_application.return_value = mock_app

    result = launch_stk(mode="desktop", visible=False, user_control=False)

    mock_desktop.start_application.assert_called_once_with(visible=False, user_control=False)
    assert result == mock_app


@patch("ansys.stk.extensions.launcher.STKDesktop")
def test_launch_stk_desktop_with_enum(mock_desktop):
    """Test launching STK in DESKTOP mode using enum mode."""
    mock_app = MagicMock()
    mock_desktop.start_application.return_value = mock_app

    result = launch_stk(mode=STKApplicationType.DESKTOP, visible=False, user_control=False)

    mock_desktop.start_application.assert_called_once_with(visible=False, user_control=False)
    assert result == mock_app


def test_launch_stk_runtime_with_string():
    """Test launching STK in RUNTIME mode using string mode."""
    result = launch_stk(mode="runtime", grpc_host="localhost", grpc_port=50051)
    result.shutdown()


def test_launch_stk_runtime_with_enum():
    """Test launching STK in RUNTIME mode using enum mode."""
    result = launch_stk(mode=STKApplicationType.RUNTIME, grpc_host="127.0.0.1", grpc_port=40704)
    result.shutdown()


def test_launch_stk_invalid_string_mode():
    """Test that invalid string mode raises ValueError."""
    with pytest.raises(ValueError, match="Unsupported STK application type: 'invalid'"):
        launch_stk(mode="invalid")


def test_launch_stk_invalid_mode_type():
    """Test that invalid mode type raises ValueError."""
    with pytest.raises(
        ValueError,
        match="Mode must be an instance of STKApplicationType or a valid string value.",
    ):
        launch_stk(mode=123)


@patch("ansys.stk.extensions.launcher.STKEngine")
def test_launch_stk_no_configuration(mock_engine):
    """Test launching STK without any configuration parameters."""
    mock_app = MagicMock()
    mock_engine.start_application.return_value = mock_app

    result = launch_stk(mode="engine")

    mock_engine.start_application.assert_called_once_with()
    assert result == mock_app


def test_enum_values():
    """Test that enum values are correct."""
    assert STKApplicationType.ENGINE.value == "engine"
    assert STKApplicationType.DESKTOP.value == "desktop"
    assert STKApplicationType.RUNTIME.value == "runtime"


def test_enum_string_conversion():
    """Test that string values can be converted to enum."""
    assert STKApplicationType("engine") == STKApplicationType.ENGINE
    assert STKApplicationType("desktop") == STKApplicationType.DESKTOP
    assert STKApplicationType("runtime") == STKApplicationType.RUNTIME


def test_enum_invalid_string():
    """Test that invalid string raises ValueError."""
    with pytest.raises(ValueError):
        STKApplicationType("invalid_mode")


def test_enum_uniqueness():
    """Test that all enum values are unique."""
    values = [e.value for e in STKApplicationType]
    assert len(values) == len(set(values))


@patch("ansys.stk.extensions.launcher.STKDesktop")
def test_attach_to_application_desktop_with_string(mock_desktop):
    """Test attaching to STK in DESKTOP mode using string mode."""
    mock_app = MagicMock()
    mock_desktop.attach_to_application.return_value = mock_app

    result = attach_to_application(mode="desktop")

    mock_desktop.attach_to_application.assert_called_once_with()
    assert result == mock_app


@patch("ansys.stk.extensions.launcher.STKDesktop")
def test_attach_to_application_desktop_with_enum(mock_desktop):
    """Test attaching to STK in DESKTOP mode using enum mode."""
    mock_app = MagicMock()
    mock_desktop.attach_to_application.return_value = mock_app

    result = attach_to_application(mode=STKApplicationType.DESKTOP)

    mock_desktop.attach_to_application.assert_called_once_with()
    assert result == mock_app


def test_attach_to_application_runtime_with_string():
    """Test attaching to STK in RUNTIME mode using string mode."""
    launch_stk(mode="runtime", grpc_host="localhost", grpc_port=50051)
    stk = attach_to_application(mode="runtime", grpc_host="localhost", grpc_port=50051)
    stk.shutdown()


def test_attach_to_application_runtime_with_enum():
    """Test attaching to STK in RUNTIME mode using enum mode."""
    launch_stk(mode=STKApplicationType.RUNTIME, grpc_host="127.0.0.1", grpc_port=40704)
    stk = attach_to_application(mode=STKApplicationType.RUNTIME, grpc_host="127.0.0.1", grpc_port=40704)
    stk.shutdown()


def test_attach_to_application_engine_not_supported_string():
    """Test that ENGINE mode with string raises ValueError."""
    with pytest.raises(
        NotImplementedError,
        match="STKEngine mode does not support attaching to an existing instance."
    ):
        attach_to_application(mode="engine")


def test_attach_to_application_engine_not_supported_enum():
    """Test that ENGINE mode with enum raises ValueError."""
    with pytest.raises(
        NotImplementedError,
        match="STKEngine mode does not support attaching to an existing instance."
    ):
        attach_to_application(mode=STKApplicationType.ENGINE)


def test_attach_to_application_invalid_string_mode():
    """Test that invalid string mode raises ValueError."""
    with pytest.raises(ValueError, match="Unsupported STK application type: 'invalid'"):
        attach_to_application(mode="invalid")


def test_attach_to_application_invalid_mode_type():
    """Test that invalid mode type raises ValueError."""
    with pytest.raises(
        ValueError,
        match="Mode must be an instance of STKApplicationType or a valid string value.",
    ):
        attach_to_application(mode=123)


@patch("ansys.stk.extensions.launcher.STKDesktop")
def test_attach_to_application_no_configuration(mock_desktop):
    """Test attaching to STK without any configuration parameters."""
    mock_app = MagicMock()
    mock_desktop.attach_to_application.return_value = mock_app

    result = attach_to_application(mode="desktop")

    mock_desktop.attach_to_application.assert_called_once_with()
    assert result == mock_app
