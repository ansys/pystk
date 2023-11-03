# Copyright 2020-2023, Ansys Government Initiatives 

import typing

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
        """Represents a valid interface."""
        return False

    def query_interface(self, guid) -> "interface_proxy":
        """Returns a new object with the requested guid."""
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
        """Returns the next item in the collection."""
        return None

    def reset(self):
        """Resets the enumeration of the collection."""

class out_arg(object):
    pass