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

__all__ = ["STKXInitialize"]



from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal.comutil     import IDispatch
from ..internal.apiutil     import (InterfaceProxy, initialize_from_source_object, get_interface_property,
    set_class_attribute, SupportsDeleteCallback)



class STKXInitialize(SupportsDeleteCallback):
    """STK X Advanced Initialization Options."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _initialize_activation_context_method_offset = 1
    _initialize_data_method_offset = 2
    _initialize_data_ex_method_offset = 3
    _metadata = {
        "iid_data" : (5033046144316014528, 12414997222494834876),
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
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg,) }
    def initialize_data(self, install_home:str, all_users_directory:str, config_directory:str) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home and all users directory specified."""
        return self._intf.invoke(STKXInitialize._metadata, STKXInitialize._initialize_data_metadata, install_home, all_users_directory, config_directory)

    _initialize_data_ex_metadata = { "offset" : _initialize_data_ex_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg,) }
    def initialize_data_ex(self, install_home:str, all_users_directory:str, config_directory:str, defaults:bool, styles:bool, vgt:bool, amm:bool, gator:bool, online_data:bool, online_sgp4:bool) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home, all users directory, and config options specified."""
        return self._intf.invoke(STKXInitialize._metadata, STKXInitialize._initialize_data_ex_metadata, install_home, all_users_directory, config_directory, defaults, styles, vgt, amm, gator, online_data, online_sgp4)


    def __init__(self, source_object=None):
        """Construct an object of type STKXInitialize."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, STKXInitialize)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, STKXInitialize, [STKXInitialize, ])

agcls.AgClassCatalog.add_catalog_entry((4887201765317381124, 912561769072360120), STKXInitialize)
agcls.AgTypeNameMap["STKXInitialize"] = STKXInitialize