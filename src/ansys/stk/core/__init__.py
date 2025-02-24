"""
PySTK.

A Python API for Systems Tool Kit (STK).
"""
 

from . import graphics, stkobjects, stkrfchannelmodeler, stkutil, vgt
from .stkobjects import astrogator, aviator

__version__ = "0.1.dev0"
"""Current version of PySTK."""

__all__ = ["__version__", "graphics", "stkobjects", "stkutil", "vgt", "stkrfchannelmodeler", "astrogator", "aviator"]
"""Available modules when using wildcard import."""