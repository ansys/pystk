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


import gc
import typing

class InterfaceProxy(object):
    """Proxy class to isolate the call strategy (COM, gRPC, etc)."""
    def __init__(self):
        pass

    def __eq__(self, other):
        """Check for equivalence of the underlying interface."""
        return False

    def __hash__(self):
        """Manage reference count."""
        return 0

    def __bool__(self):
        """Represent a valid interface."""
        return False

    def query_interface(self, intf_metadata:dict) -> "InterfaceProxy":
        """Return a new object with the requested guid."""
        return InterfaceProxy()

    def invoke(self, intf_metadata:dict, method_metadata:dict, *args):
        pass

    def get_property(self, intf_metadata:dict, method_metadata:dict):
        pass

    def set_property(self, intf_metadata:dict, method_metadata:dict, value):
        pass

class EnumeratorProxy(object):
    """Proxy class to isolate the call strategy for enumeration (COM, gRPC, etc)."""
    def __init__(self):
        pass

    def next(self) -> typing.Any:
        """Return the next item in the collection."""
        return None

    def reset(self):
        """Reset the enumeration of the collection."""

class SupportsDeleteCallback(object):
    """Execute callbacks on object deletion."""
    def __init__(self):
        self.__dict__["_del_callbacks"] = []

    def __del__(self):
        for callback in self._del_callbacks:
            callback()

    def _add_delete_callback(self, callback:typing.Callable) -> None:
        self._del_callbacks.append(callback)

class OutArg(object):
    pass

class GcDisabler(object):
    """Temporarily disable garbage collection."""
    def __init__(self):
        self._is_gc_enabled = False
    def __enter__(self):
        if gc.isenabled is not None and gc.isenabled():
            self._is_gc_enabled = True
            gc.disable()
        return self
    def __exit__(self, type, value, tb):
        if self._is_gc_enabled:
            gc.enable()
        return False

def initialize_from_source_object(this, sourceObject, interfaceType):
    this.__dict__["_intf"] = InterfaceProxy()
    if sourceObject is not None and sourceObject._intf is not None:
        intf = sourceObject._intf.query_interface(interfaceType._metadata)
        if intf is not None:
            this._private_init(intf)
            del(intf)
        else:
            raise RuntimeError(f"Failed to create {interfaceType.__name__} from source object.")

def get_interface_property(attrname, interfaceType):
    if attrname in interfaceType.__dict__ and type(interfaceType.__dict__[attrname]) == property:
        return interfaceType.__dict__[attrname]
    return None

def set_interface_attribute(this, attrname, value, interfaceType, baseType):
    if interfaceType._get_property(this, attrname) is not None:
        interfaceType._get_property(this, attrname).__set__(this, value)
    elif baseType is not None:
        baseType.__setattr__(this, attrname, value)
    else:
        raise AttributeError(f"{attrname} is not a recognized attribute in {interfaceType.__name__}.")

def set_class_attribute(this, attrname, value, classType, interfaceTypes):
    found_prop = None
    for interfaceType in interfaceTypes:
        found_prop_in_interface = interfaceType._get_property(this, attrname)
        if found_prop_in_interface is not None:
            found_prop = found_prop_in_interface
    if found_prop is not None:
        found_prop.__set__(this, value)
    else:
        raise AttributeError(f"{attrname} is not a recognized attribute in {classType.__name__}.")

def _unquoted(s:str) -> str:
    if s is not None and len(s) > 0:
        if s[0] == "\"":
            s = s[1:]
        if len(s) > 0 and s[-1] == "\"":
            s = s[:-1]
    return s

def read_registry_key(key, value=None, root=None, silent_exception=False):
    try:
        import winreg
        if root is None:
            root = winreg.HKEY_CLASSES_ROOT
        with winreg.OpenKey(root, key) as hkey:
            (val, typ) = winreg.QueryValueEx(hkey, value)
        return _unquoted(val)
    except Exception as e:
        if not silent_exception:
            raise RuntimeError(f"Error Reading Registry for {key}: {e}")
        return None

def winreg_stk_binary_dir():
    try:
        import winreg
        return _unquoted(read_registry_key(f"SOFTWARE\\AGI\\STK_ODTK\\13.0", root=winreg.HKEY_LOCAL_MACHINE, value="STKBinaryFolder"))
    except Exception as e:
        return None

def error_msg_from_hresult(hr:int) -> str:
    '''Error messages from common HRESULT values.'''
    hr = (hr & 0xFFFFFFFF)
    if hr == 0x80070057: # E_INVALIDARG
        return "One or more arguments are invalid."
    elif hr == 0x8007000E: # E_OUTOFMEMORY
        return "Data size exceeds memory limit. Try chunking the data request."
    elif hr == 0x80004003: # E_POINTER
        return "Invalid object instance."
    else:
        return "(HRESULT = 0x%x)" % (hr)