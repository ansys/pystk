"""Tests for the launcher extension."""

import pytest

from ansys.stk.extensions.launcher import launch_stk

mode_and_config = (
    ("engine", {"no_graphics": True}),
    #("desktop", {"visible": False, "user_control": False, "grpc_server": False}),
    #("runtime", {"grpc_host": "127.0.0.1", "grpc_port": "40704"}),
)
"""Launch mode and its corresponding configuration."""


@pytest.mark.parametrize("mode, config", mode_and_config)
def test_launch_stk(mode, config):
    stk = launch_stk(mode=mode, **config)
    stk.shutdown()
