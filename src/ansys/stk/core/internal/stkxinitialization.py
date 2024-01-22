################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

__all__ = ["ISTKXInitialize", "STKXInitialize"]



from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal.comutil     import IDispatch
from ..internal.apiutil     import (interface_proxy, initialize_from_source_object, get_interface_property, 
    set_interface_attribute, set_class_attribute)
from ..internal.eventutil   import *
from ..utilities.exceptions import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class ISTKXInitialize(object):
    """STK X Advanced Initialization Options."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{EDC9E451-09B3-4D8B-9EC5-B75C6D95A52D}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "initialize_activation_context" : 1,
                             "initialize_data" : 2,
                             "initialize_data_ex" : 3, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, ISTKXInitialize)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, ISTKXInitialize)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, ISTKXInitialize, None)
    
    _initialize_activation_context_metadata = { "name" : "initialize_activation_context",
            "arg_types" : (),
            "marshallers" : () }
    def initialize_activation_context(self) -> None:
        """Initialize the activation context to be used by STK Engine based on the current activation context."""
        return self._intf.invoke(ISTKXInitialize._metadata, ISTKXInitialize._initialize_activation_context_metadata, )

    _initialize_data_metadata = { "name" : "initialize_data",
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def initialize_data(self, installHome:str, configDirectory:str) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home specified."""
        return self._intf.invoke(ISTKXInitialize._metadata, ISTKXInitialize._initialize_data_metadata, installHome, configDirectory)

    _initialize_data_ex_metadata = { "name" : "initialize_data_ex",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.VARIANT_BOOL_arg, agmarshall.VARIANT_BOOL_arg, agmarshall.VARIANT_BOOL_arg, agmarshall.VARIANT_BOOL_arg, agmarshall.VARIANT_BOOL_arg, agmarshall.VARIANT_BOOL_arg, agmarshall.VARIANT_BOOL_arg,) }
    def initialize_data_ex(self, installHome:str, configDirectory:str, bDefaults:bool, bStyles:bool, bVGT:bool, bAMM:bool, bGator:bool, bOnlineData:bool, bOnlineSGP4:bool) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home specified, and config options."""
        return self._intf.invoke(ISTKXInitialize._metadata, ISTKXInitialize._initialize_data_ex_metadata, installHome, configDirectory, bDefaults, bStyles, bVGT, bAMM, bGator, bOnlineData, bOnlineSGP4)


agcls.AgClassCatalog.add_catalog_entry("{EDC9E451-09B3-4D8B-9EC5-B75C6D95A52D}", ISTKXInitialize)
agcls.AgTypeNameMap["ISTKXInitialize"] = ISTKXInitialize



class STKXInitialize(ISTKXInitialize):
    """STK X Initialize object."""

    def __init__(self, sourceObject=None):
        ISTKXInitialize.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ISTKXInitialize._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        set_class_attribute(self, attrname, value, STKXInitialize, [ISTKXInitialize])

agcls.AgClassCatalog.add_catalog_entry("{3B85901D-FC82-4733-97E6-5BB25CE69379}", STKXInitialize)
agcls.AgTypeNameMap["STKXInitialize"] = STKXInitialize


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
