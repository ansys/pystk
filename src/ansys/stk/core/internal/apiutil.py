# Copyright 2020-2023, Ansys Government Initiatives 

import typing

from ..utilities.exceptions import *

class interface_proxy(object):
    """Proxy class to isolate the call strategy to STK (COM, gRPC, etc)."""
    def __init__(self):
        pass

    def __eq__(self, other):
        """Check for equivalence of the underlying STK interface."""
        return False

    def __hash__(self):
        """Used primarily for reference count management."""
        return 0

    def __bool__(self):
        """Represent a valid interface."""
        return False

    def query_interface(self, guid) -> "interface_proxy":
        """Return a new object with the requested guid."""
        return interface_proxy()

    def invoke(self, intf_metatdata:dict, method_metadata:dict, *args):
        pass

    def get_property(self, intf_metatdata:dict, method_metadata:dict):
        pass

    def set_property(self, intf_metatdata:dict, method_metadata:dict, value):
        pass

class enumerator_proxy(object):
    """Proxy class to isolate the call strategy for enumeration (COM, gRPC, etc)."""
    def __init__(self):
        pass

    def next(self) -> typing.Any:
        """Return the next item in the collection."""
        return None

    def reset(self):
        """Reset the enumeration of the collection."""

class out_arg(object):
    pass

def initialize_from_source_object(this, sourceObject, interfaceType):
    this.__dict__["_intf"] = interface_proxy()
    if sourceObject is not None and sourceObject._intf is not None:
        intf = sourceObject._intf.query_interface(interfaceType._metadata["uuid"])
        if intf is not None:
            this._private_init(intf)
            del(intf)
        else:
            raise STKInvalidCastError(f"Failed to create {interfaceType.__name__} from source object.")

def get_interface_property(attrname, interfaceType):
    if attrname in interfaceType.__dict__ and type(interfaceType.__dict__[attrname]) == property:
        return interfaceType.__dict__[attrname]
    return None

def set_interface_attribute(this, attrname, value, interfaceType, baseType):
    if this._get_property(attrname) is not None:
        this._get_property(attrname).__set__(this, value)
    elif baseType is not None:
        baseType.__setattr__(this, attrname, value)
    else:
        raise STKAttributeError(f"{attrname} is not a recognized attribute in {interfaceType.__name__}.")

def set_class_attribute(this, attrname, value, classType, interfaceTypes):
    found_prop = None
    for interfaceType in interfaceTypes:
        found_prop_in_interface = interfaceType._get_property(this, attrname)
        if found_prop_in_interface is not None:
            found_prop = found_prop_in_interface
    if found_prop is not None:
        found_prop.__set__(this, value)
    else:
        raise STKAttributeError(f"{attrname} is not a recognized attribute in {classType.__name__}.")
