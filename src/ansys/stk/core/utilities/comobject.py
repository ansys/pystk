# Copyright 2020-2020, Ansys Government Initiatives 
"""This module contains a wrapper for a raw COM object that is not part of the STK Object Model."""

from ctypes import c_void_p

class COMObject(object):
    """
    Holds a raw COM pointer.
    
    May be returned from STK if the return argument is not part of the STK Object Model.
    """
    def __init__(self):
        self._pUnk = None
        
    def GetPointer(self) -> c_void_p:
        """Return the COM object pointer as a ctypes.c_void_p."""
        if self._pUnk is None:
            return c_void_p()
        else:
            return self._pUnk.p
    