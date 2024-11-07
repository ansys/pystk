################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

__all__ = ["STKXInitialize"]



from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal.comutil     import IDispatch
from ..internal.apiutil     import (InterfaceProxy, initialize_from_source_object, get_interface_property, 
    set_class_attribute, SupportsDeleteCallback)
from ..internal.eventutil   import *
from ..utilities.exceptions import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")


class STKXInitialize(SupportsDeleteCallback):
    """STK X Advanced Initialization Options."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _initialize_activation_context_method_offset = 1
    _initialize_data_method_offset = 2
    _initialize_data_ex_method_offset = 3
    _metadata = {
        "iid_data" : (5587570431076459601, 3289199399803536798),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, STKXInitialize)
    
    _initialize_activation_context_metadata = { "offset" : _initialize_activation_context_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def initialize_activation_context(self) -> None:
        """Initialize the activation context to be used by STK Engine based on the current activation context."""
        return self._intf.invoke(STKXInitialize._metadata, STKXInitialize._initialize_activation_context_metadata, )

    _initialize_data_metadata = { "offset" : _initialize_data_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg,) }
    def initialize_data(self, install_home:str, config_directory:str) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home specified."""
        return self._intf.invoke(STKXInitialize._metadata, STKXInitialize._initialize_data_metadata, install_home, config_directory)

    _initialize_data_ex_metadata = { "offset" : _initialize_data_ex_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg,) }
    def initialize_data_ex(self, install_home:str, config_directory:str, defaults:bool, styles:bool, vgt:bool, amm:bool, gator:bool, online_data:bool, online_sgp4:bool) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home specified, and config options."""
        return self._intf.invoke(STKXInitialize._metadata, STKXInitialize._initialize_data_ex_metadata, install_home, config_directory, defaults, styles, vgt, amm, gator, online_data, online_sgp4)


    def __init__(self, sourceObject=None):
        """Construct an object of type STKXInitialize."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, sourceObject, STKXInitialize)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, STKXInitialize, [STKXInitialize, ])

agcls.AgClassCatalog.add_catalog_entry((5130722036779683869, 8760598985969493655), STKXInitialize)
agcls.AgTypeNameMap["STKXInitialize"] = STKXInitialize


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
