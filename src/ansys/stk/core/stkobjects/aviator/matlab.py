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

"""
Object Model components to support the MATLAB strategies found in the Basic Maneuver Procedure.

MATLAB strategies allow the users to utilize MATLAB
Aerospace Toolbox functions to define the force modeling of the aircraft.
"""

__all__ = ["BasicManeuverMATLABFactory", "StrategyMATLAB3DGuidance", "StrategyMATLABFull3D", "StrategyMATLABNavigation",
"StrategyMATLABProfile"]

from ctypes import POINTER
import typing

from ...internal import coclassutil as agcls, comutil as agcom, marshall as agmarshall
from ...internal.apiutil import (
    InterfaceProxy,
    OutArg,
    SupportsDeleteCallback,
    get_interface_property,
    initialize_from_source_object,
    set_class_attribute,
)
from ...internal.comutil import IUnknown
from ...stkobjects.aviator import ClosureMode, IAutomationStrategyFactory, IBasicManeuverStrategy


class StrategyMATLABNavigation(IBasicManeuverStrategy, SupportsDeleteCallback):
    """Interface used to access options for a MATLAB - Horizontal Plane Strategy of a Basic Maneuver Procedure."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_function_name_method_offset = 1
    _set_function_name_method_offset = 2
    _is_function_path_valid_method_offset = 3
    _get_check_for_errors_method_offset = 4
    _set_check_for_errors_method_offset = 5
    _get_display_output_method_offset = 6
    _set_display_output_method_offset = 7
    _metadata = {
        "iid_data" : (4693738194356967383, 14734181398989770921),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StrategyMATLABNavigation)

    _get_function_name_metadata = { "offset" : _get_function_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def function_name(self) -> str:
        """Get or set the name of the MATLAB function."""
        return self._intf.get_property(StrategyMATLABNavigation._metadata, StrategyMATLABNavigation._get_function_name_metadata)

    _set_function_name_metadata = { "offset" : _set_function_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @function_name.setter
    def function_name(self, value:str) -> None:
        """Get or set the name of the MATLAB function."""
        return self._intf.set_property(StrategyMATLABNavigation._metadata, StrategyMATLABNavigation._set_function_name_metadata, value)

    _is_function_path_valid_metadata = { "offset" : _is_function_path_valid_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(StrategyMATLABNavigation._metadata, StrategyMATLABNavigation._is_function_path_valid_metadata, OutArg())

    _get_check_for_errors_metadata = { "offset" : _get_check_for_errors_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def check_for_errors(self) -> bool:
        """Get or set the option to check the function for errors."""
        return self._intf.get_property(StrategyMATLABNavigation._metadata, StrategyMATLABNavigation._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "offset" : _set_check_for_errors_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @check_for_errors.setter
    def check_for_errors(self, value:bool) -> None:
        """Get or set the option to check the function for errors."""
        return self._intf.set_property(StrategyMATLABNavigation._metadata, StrategyMATLABNavigation._set_check_for_errors_metadata, value)

    _get_display_output_metadata = { "offset" : _get_display_output_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def display_output(self) -> bool:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.get_property(StrategyMATLABNavigation._metadata, StrategyMATLABNavigation._get_display_output_metadata)

    _set_display_output_metadata = { "offset" : _set_display_output_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @display_output.setter
    def display_output(self, value:bool) -> None:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.set_property(StrategyMATLABNavigation._metadata, StrategyMATLABNavigation._set_display_output_metadata, value)

    _property_names[function_name] = "function_name"
    _property_names[check_for_errors] = "check_for_errors"
    _property_names[display_output] = "display_output"

    def __init__(self, source_object=None):
        """Construct an object of type StrategyMATLABNavigation."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StrategyMATLABNavigation)
        IBasicManeuverStrategy.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StrategyMATLABNavigation, [StrategyMATLABNavigation, IBasicManeuverStrategy])

agcls.AgClassCatalog.add_catalog_entry((5225404421302427357, 16343776315648835216), StrategyMATLABNavigation)
agcls.AgTypeNameMap["StrategyMATLABNavigation"] = StrategyMATLABNavigation

class StrategyMATLABProfile(IBasicManeuverStrategy, SupportsDeleteCallback):
    """Interface used to access options for a MATLAB - Vertical Plane Strategy of a Basic Maneuver Procedure."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_function_name_method_offset = 1
    _set_function_name_method_offset = 2
    _is_function_path_valid_method_offset = 3
    _get_check_for_errors_method_offset = 4
    _set_check_for_errors_method_offset = 5
    _get_display_output_method_offset = 6
    _set_display_output_method_offset = 7
    _metadata = {
        "iid_data" : (5148147632220002052, 17898467848992200636),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StrategyMATLABProfile)

    _get_function_name_metadata = { "offset" : _get_function_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def function_name(self) -> str:
        """Get or set the name of the MATLAB function."""
        return self._intf.get_property(StrategyMATLABProfile._metadata, StrategyMATLABProfile._get_function_name_metadata)

    _set_function_name_metadata = { "offset" : _set_function_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @function_name.setter
    def function_name(self, value:str) -> None:
        """Get or set the name of the MATLAB function."""
        return self._intf.set_property(StrategyMATLABProfile._metadata, StrategyMATLABProfile._set_function_name_metadata, value)

    _is_function_path_valid_metadata = { "offset" : _is_function_path_valid_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(StrategyMATLABProfile._metadata, StrategyMATLABProfile._is_function_path_valid_metadata, OutArg())

    _get_check_for_errors_metadata = { "offset" : _get_check_for_errors_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def check_for_errors(self) -> bool:
        """Get or set the option to check the function for errors."""
        return self._intf.get_property(StrategyMATLABProfile._metadata, StrategyMATLABProfile._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "offset" : _set_check_for_errors_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @check_for_errors.setter
    def check_for_errors(self, value:bool) -> None:
        """Get or set the option to check the function for errors."""
        return self._intf.set_property(StrategyMATLABProfile._metadata, StrategyMATLABProfile._set_check_for_errors_metadata, value)

    _get_display_output_metadata = { "offset" : _get_display_output_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def display_output(self) -> bool:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.get_property(StrategyMATLABProfile._metadata, StrategyMATLABProfile._get_display_output_metadata)

    _set_display_output_metadata = { "offset" : _set_display_output_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @display_output.setter
    def display_output(self, value:bool) -> None:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.set_property(StrategyMATLABProfile._metadata, StrategyMATLABProfile._set_display_output_metadata, value)

    _property_names[function_name] = "function_name"
    _property_names[check_for_errors] = "check_for_errors"
    _property_names[display_output] = "display_output"

    def __init__(self, source_object=None):
        """Construct an object of type StrategyMATLABProfile."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StrategyMATLABProfile)
        IBasicManeuverStrategy.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StrategyMATLABProfile, [StrategyMATLABProfile, IBasicManeuverStrategy])

agcls.AgClassCatalog.add_catalog_entry((4727677235214853696, 1637040926132612234), StrategyMATLABProfile)
agcls.AgTypeNameMap["StrategyMATLABProfile"] = StrategyMATLABProfile

class StrategyMATLABFull3D(IBasicManeuverStrategy, SupportsDeleteCallback):
    """Interface used to access options for a MATLAB - Full 3D Strategy of a Basic Maneuver Procedure."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_function_name_method_offset = 1
    _set_function_name_method_offset = 2
    _is_function_path_valid_method_offset = 3
    _get_check_for_errors_method_offset = 4
    _set_check_for_errors_method_offset = 5
    _get_display_output_method_offset = 6
    _set_display_output_method_offset = 7
    _metadata = {
        "iid_data" : (4933395837275083186, 5728383285686110601),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StrategyMATLABFull3D)

    _get_function_name_metadata = { "offset" : _get_function_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def function_name(self) -> str:
        """Get or set the name of the MATLAB function."""
        return self._intf.get_property(StrategyMATLABFull3D._metadata, StrategyMATLABFull3D._get_function_name_metadata)

    _set_function_name_metadata = { "offset" : _set_function_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @function_name.setter
    def function_name(self, value:str) -> None:
        """Get or set the name of the MATLAB function."""
        return self._intf.set_property(StrategyMATLABFull3D._metadata, StrategyMATLABFull3D._set_function_name_metadata, value)

    _is_function_path_valid_metadata = { "offset" : _is_function_path_valid_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(StrategyMATLABFull3D._metadata, StrategyMATLABFull3D._is_function_path_valid_metadata, OutArg())

    _get_check_for_errors_metadata = { "offset" : _get_check_for_errors_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def check_for_errors(self) -> bool:
        """Get or set the option to check the function for errors."""
        return self._intf.get_property(StrategyMATLABFull3D._metadata, StrategyMATLABFull3D._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "offset" : _set_check_for_errors_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @check_for_errors.setter
    def check_for_errors(self, value:bool) -> None:
        """Get or set the option to check the function for errors."""
        return self._intf.set_property(StrategyMATLABFull3D._metadata, StrategyMATLABFull3D._set_check_for_errors_metadata, value)

    _get_display_output_metadata = { "offset" : _get_display_output_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def display_output(self) -> bool:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.get_property(StrategyMATLABFull3D._metadata, StrategyMATLABFull3D._get_display_output_metadata)

    _set_display_output_metadata = { "offset" : _set_display_output_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @display_output.setter
    def display_output(self, value:bool) -> None:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.set_property(StrategyMATLABFull3D._metadata, StrategyMATLABFull3D._set_display_output_metadata, value)

    _property_names[function_name] = "function_name"
    _property_names[check_for_errors] = "check_for_errors"
    _property_names[display_output] = "display_output"

    def __init__(self, source_object=None):
        """Construct an object of type StrategyMATLABFull3D."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StrategyMATLABFull3D)
        IBasicManeuverStrategy.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StrategyMATLABFull3D, [StrategyMATLABFull3D, IBasicManeuverStrategy])

agcls.AgClassCatalog.add_catalog_entry((5373249918517851774, 5395661847088340112), StrategyMATLABFull3D)
agcls.AgTypeNameMap["StrategyMATLABFull3D"] = StrategyMATLABFull3D

class StrategyMATLAB3DGuidance(IBasicManeuverStrategy, SupportsDeleteCallback):
    """Interface used to access options for a MATLAB - 3D Guidance Strategy of a Basic Maneuver Procedure."""

    _num_methods = 29
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_target_name_method_offset = 1
    _set_target_name_method_offset = 2
    _get_valid_target_names_method_offset = 3
    _get_target_resolution_method_offset = 4
    _set_target_resolution_method_offset = 5
    _get_use_stop_time_to_go_method_offset = 6
    _get_stop_time_to_go_method_offset = 7
    _set_stop_time_to_go_method_offset = 8
    _get_use_stop_slant_range_method_offset = 9
    _get_stop_slant_range_method_offset = 10
    _set_stop_slant_range_method_offset = 11
    _get_function_name_method_offset = 12
    _set_function_name_method_offset = 13
    _is_function_path_valid_method_offset = 14
    _get_check_for_errors_method_offset = 15
    _set_check_for_errors_method_offset = 16
    _get_display_output_method_offset = 17
    _set_display_output_method_offset = 18
    _get_closure_mode_method_offset = 19
    _set_closure_mode_method_offset = 20
    _get_hobs_max_angle_method_offset = 21
    _set_hobs_max_angle_method_offset = 22
    _get_hobs_angle_tol_method_offset = 23
    _set_hobs_angle_tol_method_offset = 24
    _get_compute_tas_dot_method_offset = 25
    _set_compute_tas_dot_method_offset = 26
    _get_airspeed_options_method_offset = 27
    _get_position_velocity_strategies_method_offset = 28
    _cancel_target_position_velocity_method_offset = 29
    _metadata = {
        "iid_data" : (5143209814694955910, 16817896824929652403),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StrategyMATLAB3DGuidance)

    _get_target_name_metadata = { "offset" : _get_target_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def target_name(self) -> str:
        """Get or set the target name."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_target_name_metadata)

    _set_target_name_metadata = { "offset" : _set_target_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @target_name.setter
    def target_name(self, value:str) -> None:
        """Get or set the target name."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_target_name_metadata, value)

    _get_valid_target_names_metadata = { "offset" : _get_valid_target_names_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def valid_target_names(self) -> list:
        """Return the valid target names."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_valid_target_names_metadata)

    _get_target_resolution_metadata = { "offset" : _get_target_resolution_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def target_resolution(self) -> float:
        """Get or set the target position/velocity sampling resolution."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_target_resolution_metadata)

    _set_target_resolution_metadata = { "offset" : _set_target_resolution_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @target_resolution.setter
    def target_resolution(self, value:float) -> None:
        """Get or set the target position/velocity sampling resolution."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_target_resolution_metadata, value)

    _get_use_stop_time_to_go_metadata = { "offset" : _get_use_stop_time_to_go_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def use_stop_time_to_go(self) -> bool:
        """Get the option to specify a time to go stopping condition."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_use_stop_time_to_go_metadata)

    _get_stop_time_to_go_metadata = { "offset" : _get_stop_time_to_go_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def stop_time_to_go(self) -> float:
        """Get the stop time from the target at which the maneuver will stop."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_stop_time_to_go_metadata)

    _set_stop_time_to_go_metadata = { "offset" : _set_stop_time_to_go_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VariantBoolArg, agmarshall.DoubleArg,) }
    def set_stop_time_to_go(self, enable:bool, time:float) -> None:
        """Set the option to use the stop time from target stopping condition and set the according value."""
        return self._intf.invoke(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_stop_time_to_go_metadata, enable, time)

    _get_use_stop_slant_range_metadata = { "offset" : _get_use_stop_slant_range_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def use_stop_slant_range(self) -> bool:
        """Get the option to specify a range from target stopping condition."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_use_stop_slant_range_metadata)

    _get_stop_slant_range_metadata = { "offset" : _get_stop_slant_range_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def stop_slant_range(self) -> float:
        """Get the range from the target at which the maneuver will stop."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_stop_slant_range_metadata)

    _set_stop_slant_range_metadata = { "offset" : _set_stop_slant_range_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VariantBoolArg, agmarshall.DoubleArg,) }
    def set_stop_slant_range(self, enable:bool, range:float) -> None:
        """Set the option to use the stop slant range stopping condition and set the according value."""
        return self._intf.invoke(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_stop_slant_range_metadata, enable, range)

    _get_function_name_metadata = { "offset" : _get_function_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def function_name(self) -> str:
        """Get or set the name of the MATLAB function."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_function_name_metadata)

    _set_function_name_metadata = { "offset" : _set_function_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @function_name.setter
    def function_name(self, value:str) -> None:
        """Get or set the name of the MATLAB function."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_function_name_metadata, value)

    _is_function_path_valid_metadata = { "offset" : _is_function_path_valid_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._is_function_path_valid_metadata, OutArg())

    _get_check_for_errors_metadata = { "offset" : _get_check_for_errors_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def check_for_errors(self) -> bool:
        """Get or set the option to check the function for errors."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "offset" : _set_check_for_errors_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @check_for_errors.setter
    def check_for_errors(self, value:bool) -> None:
        """Get or set the option to check the function for errors."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_check_for_errors_metadata, value)

    _get_display_output_metadata = { "offset" : _get_display_output_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def display_output(self) -> bool:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_display_output_metadata)

    _set_display_output_metadata = { "offset" : _set_display_output_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @display_output.setter
    def display_output(self, value:bool) -> None:
        """Get or set the option to display the output from the MATLAB function."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_display_output_metadata, value)

    _get_closure_mode_metadata = { "offset" : _get_closure_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ClosureMode),) }
    @property
    def closure_mode(self) -> "ClosureMode":
        """Get or set the closure mode for the guidance strategy."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_closure_mode_metadata)

    _set_closure_mode_metadata = { "offset" : _set_closure_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ClosureMode),) }
    @closure_mode.setter
    def closure_mode(self, value:"ClosureMode") -> None:
        """Get or set the closure mode for the guidance strategy."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_closure_mode_metadata, value)

    _get_hobs_max_angle_metadata = { "offset" : _get_hobs_max_angle_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def hobs_max_angle(self) -> typing.Any:
        """Get or set the closure high off boresight max angle."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_hobs_max_angle_metadata)

    _set_hobs_max_angle_metadata = { "offset" : _set_hobs_max_angle_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @hobs_max_angle.setter
    def hobs_max_angle(self, value:typing.Any) -> None:
        """Get or set the closure high off boresight max angle."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_hobs_max_angle_metadata, value)

    _get_hobs_angle_tol_metadata = { "offset" : _get_hobs_angle_tol_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def hobs_angle_tol(self) -> typing.Any:
        """Get or set the closure high off boresight angle tolerance."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_hobs_angle_tol_metadata)

    _set_hobs_angle_tol_metadata = { "offset" : _set_hobs_angle_tol_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @hobs_angle_tol.setter
    def hobs_angle_tol(self, value:typing.Any) -> None:
        """Get or set the closure high off boresight angle tolerance."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_hobs_angle_tol_metadata, value)

    _get_compute_tas_dot_metadata = { "offset" : _get_compute_tas_dot_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def compute_tas_dot(self) -> bool:
        """Get or set the option to allow MATLAB to compute the true airspeed for the aircraft."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_compute_tas_dot_metadata)

    _set_compute_tas_dot_metadata = { "offset" : _set_compute_tas_dot_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @compute_tas_dot.setter
    def compute_tas_dot(self, value:bool) -> None:
        """Get or set the option to allow MATLAB to compute the true airspeed for the aircraft."""
        return self._intf.set_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._set_compute_tas_dot_metadata, value)

    _get_airspeed_options_metadata = { "offset" : _get_airspeed_options_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def airspeed_options(self) -> "IBasicManeuverAirspeedOptions":
        """Get the airspeed options."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_airspeed_options_metadata)

    _get_position_velocity_strategies_metadata = { "offset" : _get_position_velocity_strategies_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def position_velocity_strategies(self) -> "IBasicManeuverTargetPositionVelocity":
        """Get the position velocity strategies for MATLAB 3D Guidance."""
        return self._intf.get_property(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._get_position_velocity_strategies_metadata)

    _cancel_target_position_velocity_metadata = { "offset" : _cancel_target_position_velocity_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def cancel_target_position_velocity(self) -> None:
        """Cancel the position velocity strategies for MATLAB 3D Guidance."""
        return self._intf.invoke(StrategyMATLAB3DGuidance._metadata, StrategyMATLAB3DGuidance._cancel_target_position_velocity_metadata, )

    _property_names[target_name] = "target_name"
    _property_names[valid_target_names] = "valid_target_names"
    _property_names[target_resolution] = "target_resolution"
    _property_names[use_stop_time_to_go] = "use_stop_time_to_go"
    _property_names[stop_time_to_go] = "stop_time_to_go"
    _property_names[use_stop_slant_range] = "use_stop_slant_range"
    _property_names[stop_slant_range] = "stop_slant_range"
    _property_names[function_name] = "function_name"
    _property_names[check_for_errors] = "check_for_errors"
    _property_names[display_output] = "display_output"
    _property_names[closure_mode] = "closure_mode"
    _property_names[hobs_max_angle] = "hobs_max_angle"
    _property_names[hobs_angle_tol] = "hobs_angle_tol"
    _property_names[compute_tas_dot] = "compute_tas_dot"
    _property_names[airspeed_options] = "airspeed_options"
    _property_names[position_velocity_strategies] = "position_velocity_strategies"

    def __init__(self, source_object=None):
        """Construct an object of type StrategyMATLAB3DGuidance."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StrategyMATLAB3DGuidance)
        IBasicManeuverStrategy.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StrategyMATLAB3DGuidance, [StrategyMATLAB3DGuidance, IBasicManeuverStrategy])

agcls.AgClassCatalog.add_catalog_entry((5423305017016857142, 9141607060078030747), StrategyMATLAB3DGuidance)
agcls.AgTypeNameMap["StrategyMATLAB3DGuidance"] = StrategyMATLAB3DGuidance

class BasicManeuverMATLABFactory(IAutomationStrategyFactory, SupportsDeleteCallback):
    """Class defining the factory to create the basic maneuver PropNav strategies."""
    def __init__(self, source_object=None):
        """Construct an object of type BasicManeuverMATLABFactory."""
        SupportsDeleteCallback.__init__(self)
        IAutomationStrategyFactory.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAutomationStrategyFactory._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, BasicManeuverMATLABFactory, [IAutomationStrategyFactory])

agcls.AgClassCatalog.add_catalog_entry((4698013157004820294, 14854422989691544197), BasicManeuverMATLABFactory)
agcls.AgTypeNameMap["BasicManeuverMATLABFactory"] = BasicManeuverMATLABFactory