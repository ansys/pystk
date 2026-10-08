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

"""Unified globe and map visualization helpers."""

from __future__ import annotations

from typing import Any

__all__ = ["GlobeVisualization", "MapVisualization", "is_jupyter_environment"]


def is_jupyter_environment() -> bool:
    """Determine whether the active Python process runs in a Jupyter kernel.

    Returns
    -------
    bool
        ``True`` when running inside a Jupyter kernel. ``False`` otherwise.
    """
    try:
        from IPython import get_ipython
    except ModuleNotFoundError:
        return False

    shell = get_ipython()
    if shell is None:
        return False

    return bool(getattr(shell, "kernel", None))


class _VisualizationBase:
    """Create a map or globe visualization with an auto-selected backend."""

    _jupyter_backend_name: str
    _tk_backend_name: str

    def __init__(
        self,
        root=None,
        *,
        parent=None,
        width: int = 800,
        height: int = 600,
        title: str | None = None,
        backend: str = "auto",
        **kwargs,
    ):
        """Initialize a visualization wrapper around a concrete UI backend.

        Parameters
        ----------
        root : object, optional
            Root object passed to the Jupyter widget backend. Required when
            ``backend="jupyter"`` or when ``backend="auto"`` resolves to Jupyter.
        parent : object, optional
            Parent container passed to the Tk backend. Required when
            ``backend="tk"`` or when ``backend="auto"`` resolves to Tk.
        width : int, default: 800
            Width of the visualization surface in pixels.
        height : int, default: 600
            Height of the visualization surface in pixels.
        title : str, optional
            Window title for backends that support it.
        backend : {"auto", "jupyter", "tk"}, default: "auto"
            Backend selection strategy.
        **kwargs
            Additional keyword arguments forwarded to the Tk backend constructor.

        Raises
        ------
        ValueError
            Raised when a required backend argument is not provided or when
            ``backend`` is not one of ``"auto"``, ``"jupyter"``, or ``"tk"``.
        """
        self._backend = self._create_backend(
            root=root,
            parent=parent,
            width=width,
            height=height,
            title=title,
            backend=backend,
            **kwargs,
        )

    @property
    def backend(self) -> Any:
        """Return the concrete backend instance selected for this visualization.

        Returns
        -------
        typing.Any
            Backend object that implements the underlying visualization behavior.
        """
        return self._backend

    def _create_backend(
        self,
        root,
        parent,
        width: int,
        height: int,
        title: str | None,
        backend: str,
        **kwargs,
    ):
        active_backend = self._select_backend(backend)
        jupyter_backend, tk_backend = self._load_backends()

        if active_backend == "jupyter":
            if root is None:
                raise ValueError("The 'root' argument is required when using the Jupyter backend.")
            return jupyter_backend(root, width, height, title)

        if parent is None:
            raise ValueError("The 'parent' argument is required when using the Tk backend.")
        return tk_backend(parent, width=width, height=height, **kwargs)

    def _select_backend(self, backend: str) -> str:
        if backend == "auto":
            return "jupyter" if is_jupyter_environment() else "tk"
        if backend not in {"jupyter", "tk"}:
            raise ValueError("The 'backend' argument must be one of: auto, jupyter, tk.")
        return backend

    def _load_backends(self):
        from ..core.experimental import jupyterwidgets
        from ..core.stkengine import tkcontrols

        return (
            getattr(jupyterwidgets, self._jupyter_backend_name),
            getattr(tkcontrols, self._tk_backend_name),
        )

    def show(self):
        """Render the current visualization if the backend exposes ``show``.

        Returns
        -------
        typing.Any
            Return value from ``backend.show()`` when available; otherwise this
            visualization wrapper instance.
        """
        show_method = getattr(self._backend, "show", None)
        if callable(show_method):
            return show_method()
        return self

    def __getattr__(self, name):
        return getattr(self._backend, name)


class GlobeVisualization(_VisualizationBase):
    """Create a globe visualization using either the Jupyter or Tk backend.

    Parameters
    ----------
    root : object, optional
        Root object passed to the Jupyter ``GlobeWidget`` backend.
    parent : object, optional
        Parent Tk object passed to the ``GlobeControl`` backend.
    width : int, default: 800
        Width of the visualization surface in pixels.
    height : int, default: 600
        Height of the visualization surface in pixels.
    title : str, optional
        Window title for the Jupyter backend when supported.
    backend : {"auto", "jupyter", "tk"}, default: "auto"
        Backend selection strategy. ``"auto"`` selects Jupyter when running in a
        notebook kernel; otherwise Tk.
    **kwargs
        Additional keyword arguments forwarded to the Tk backend.

    Raises
    ------
    ValueError
        Raised when ``root`` or ``parent`` is missing for the selected backend,
        or when ``backend`` is not a supported option.
    """

    _jupyter_backend_name = "GlobeWidget"
    _tk_backend_name = "GlobeControl"


class MapVisualization(_VisualizationBase):
    """Create a map visualization using either the Jupyter or Tk backend.

    Parameters
    ----------
    root : object, optional
        Root object passed to the Jupyter ``MapWidget`` backend.
    parent : object, optional
        Parent Tk object passed to the ``MapControl`` backend.
    width : int, default: 800
        Width of the visualization surface in pixels.
    height : int, default: 600
        Height of the visualization surface in pixels.
    title : str, optional
        Window title for the Jupyter backend when supported.
    backend : {"auto", "jupyter", "tk"}, default: "auto"
        Backend selection strategy. ``"auto"`` selects Jupyter when running in a
        notebook kernel; otherwise Tk.
    **kwargs
        Additional keyword arguments forwarded to the Tk backend.

    Raises
    ------
    ValueError
        Raised when ``root`` or ``parent`` is missing for the selected backend,
        or when ``backend`` is not a supported option.
    """

    _jupyter_backend_name = "MapWidget"
    _tk_backend_name = "MapControl"
