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

import pytest

from ansys.stk.extensions.visualization import GlobeVisualization, MapVisualization


class _FakeJupyterBackend:
    def __init__(self, root, width, height, title):
        self.root = root
        self.width = width
        self.height = height
        self.title = title
        self.shown = False

    def show(self):
        self.shown = True
        return "shown"


class _FakeTkBackend:
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.kwargs = kwargs


def test_globe_visualization_uses_jupyter_backend(monkeypatch):
    monkeypatch.setattr("ansys.stk.extensions.visualization.is_jupyter_environment", lambda: True)
    monkeypatch.setattr(GlobeVisualization, "_load_backends", lambda self: (_FakeJupyterBackend, _FakeTkBackend))

    visualization = GlobeVisualization(root="root", width=640, height=480, title="A")

    assert isinstance(visualization.backend, _FakeJupyterBackend)
    assert visualization.backend.width == 640
    assert visualization.show() == "shown"


def test_map_visualization_uses_tk_backend(monkeypatch):
    monkeypatch.setattr("ansys.stk.extensions.visualization.is_jupyter_environment", lambda: False)
    monkeypatch.setattr(MapVisualization, "_load_backends", lambda self: (_FakeJupyterBackend, _FakeTkBackend))

    visualization = MapVisualization(parent="window", width=320, height=200)

    assert isinstance(visualization.backend, _FakeTkBackend)
    assert visualization.backend.parent == "window"
    assert visualization.backend.kwargs["width"] == 320
    assert visualization.backend.kwargs["height"] == 200


def test_visualization_requires_root_for_jupyter(monkeypatch):
    monkeypatch.setattr("ansys.stk.extensions.visualization.is_jupyter_environment", lambda: True)
    monkeypatch.setattr(GlobeVisualization, "_load_backends", lambda self: (_FakeJupyterBackend, _FakeTkBackend))

    with pytest.raises(ValueError, match="root"):
        GlobeVisualization()


def test_visualization_requires_parent_for_tk(monkeypatch):
    monkeypatch.setattr("ansys.stk.extensions.visualization.is_jupyter_environment", lambda: False)
    monkeypatch.setattr(MapVisualization, "_load_backends", lambda self: (_FakeJupyterBackend, _FakeTkBackend))

    with pytest.raises(ValueError, match="parent"):
        MapVisualization(root="root")


def test_visualization_rejects_invalid_backend(monkeypatch):
    monkeypatch.setattr("ansys.stk.extensions.visualization.is_jupyter_environment", lambda: False)
    monkeypatch.setattr(GlobeVisualization, "_load_backends", lambda self: (_FakeJupyterBackend, _FakeTkBackend))

    with pytest.raises(ValueError, match="backend"):
        GlobeVisualization(parent="window", backend="bad-backend")
