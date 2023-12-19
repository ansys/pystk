################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

__all__ = ["BasicManeuverMATLABFactory", "IStrategyMATLAB3DGuidance", "IStrategyMATLABFull3D", "IStrategyMATLABNav", "IStrategyMATLABProfile", 
"StrategyMATLAB3DGuidance", "StrategyMATLABFull3D", "StrategyMATLABNav", "StrategyMATLABProfile"]

import typing

from ctypes   import POINTER

from ...internal  import comutil          as agcom
from ...internal  import coclassutil      as agcls
from ...internal  import marshall         as agmarshall
from ...internal.comutil     import IUnknown
from ...internal.apiutil     import interface_proxy, out_arg
from ...internal.eventutil   import *
from ...utilities.exceptions import *

from ...stkobjects.aviator import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class IStrategyMATLABNav(object):
    """Interface used to access options for a MATLAB - Horizontal Plane Strategy of a Basic Maneuver Procedure."""
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{e53fcce4-1a17-488d-9053-c236d27b8b6e}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_function_name" : 1,
                             "set_function_name" : 2,
                             "is_function_path_valid" : 3,
                             "get_check_for_errors" : 4,
                             "set_check_for_errors" : 5,
                             "get_display_output" : 6,
                             "set_display_output" : 7, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IStrategyMATLABNav._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLABNav from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IStrategyMATLABNav.__dict__ and type(IStrategyMATLABNav.__dict__[attrname]) == property:
            return IStrategyMATLABNav.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IStrategyMATLABNav.")
    
    _get_function_name_metadata = { "name" : "function_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def function_name(self) -> str:
        """The name of the MATLAB function."""
        return self._intf.get_property(IStrategyMATLABNav._metadata, IStrategyMATLABNav._get_function_name_metadata)

    _set_function_name_metadata = { "name" : "function_name",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @function_name.setter
    def function_name(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        return self._intf.set_property(IStrategyMATLABNav._metadata, IStrategyMATLABNav._set_function_name_metadata, newVal)

    _is_function_path_valid_metadata = { "name" : "is_function_path_valid",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(IStrategyMATLABNav._metadata, IStrategyMATLABNav._is_function_path_valid_metadata, out_arg())

    _get_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def check_for_errors(self) -> bool:
        """The option to check the function for errors."""
        return self._intf.get_property(IStrategyMATLABNav._metadata, IStrategyMATLABNav._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @check_for_errors.setter
    def check_for_errors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        return self._intf.set_property(IStrategyMATLABNav._metadata, IStrategyMATLABNav._set_check_for_errors_metadata, newVal)

    _get_display_output_metadata = { "name" : "display_output",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def display_output(self) -> bool:
        """The option to display the output from the MATLAB function."""
        return self._intf.get_property(IStrategyMATLABNav._metadata, IStrategyMATLABNav._get_display_output_metadata)

    _set_display_output_metadata = { "name" : "display_output",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @display_output.setter
    def display_output(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        return self._intf.set_property(IStrategyMATLABNav._metadata, IStrategyMATLABNav._set_display_output_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{e53fcce4-1a17-488d-9053-c236d27b8b6e}", IStrategyMATLABNav)
agcls.AgTypeNameMap["IStrategyMATLABNav"] = IStrategyMATLABNav

class IStrategyMATLABProfile(object):
    """Interface used to access options for a MATLAB - Vertical Plane Strategy of a Basic Maneuver Procedure."""
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{c5c0a490-9e7d-4ff9-95e9-9c10ed89500b}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_function_name" : 1,
                             "set_function_name" : 2,
                             "is_function_path_valid" : 3,
                             "get_check_for_errors" : 4,
                             "set_check_for_errors" : 5,
                             "get_display_output" : 6,
                             "set_display_output" : 7, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IStrategyMATLABProfile._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLABProfile from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IStrategyMATLABProfile.__dict__ and type(IStrategyMATLABProfile.__dict__[attrname]) == property:
            return IStrategyMATLABProfile.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IStrategyMATLABProfile.")
    
    _get_function_name_metadata = { "name" : "function_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def function_name(self) -> str:
        """The name of the MATLAB function."""
        return self._intf.get_property(IStrategyMATLABProfile._metadata, IStrategyMATLABProfile._get_function_name_metadata)

    _set_function_name_metadata = { "name" : "function_name",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @function_name.setter
    def function_name(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        return self._intf.set_property(IStrategyMATLABProfile._metadata, IStrategyMATLABProfile._set_function_name_metadata, newVal)

    _is_function_path_valid_metadata = { "name" : "is_function_path_valid",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(IStrategyMATLABProfile._metadata, IStrategyMATLABProfile._is_function_path_valid_metadata, out_arg())

    _get_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def check_for_errors(self) -> bool:
        """The option to check the function for errors."""
        return self._intf.get_property(IStrategyMATLABProfile._metadata, IStrategyMATLABProfile._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @check_for_errors.setter
    def check_for_errors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        return self._intf.set_property(IStrategyMATLABProfile._metadata, IStrategyMATLABProfile._set_check_for_errors_metadata, newVal)

    _get_display_output_metadata = { "name" : "display_output",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def display_output(self) -> bool:
        """The option to display the output from the MATLAB function."""
        return self._intf.get_property(IStrategyMATLABProfile._metadata, IStrategyMATLABProfile._get_display_output_metadata)

    _set_display_output_metadata = { "name" : "display_output",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @display_output.setter
    def display_output(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        return self._intf.set_property(IStrategyMATLABProfile._metadata, IStrategyMATLABProfile._set_display_output_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{c5c0a490-9e7d-4ff9-95e9-9c10ed89500b}", IStrategyMATLABProfile)
agcls.AgTypeNameMap["IStrategyMATLABProfile"] = IStrategyMATLABProfile

class IStrategyMATLABFull3D(object):
    """Interface used to access options for a MATLAB - Full 3D Strategy of a Basic Maneuver Procedure."""
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{eb6b432e-50fc-4546-9d4b-a4285ae96a9d}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_function_name" : 1,
                             "set_function_name" : 2,
                             "is_function_path_valid" : 3,
                             "get_check_for_errors" : 4,
                             "set_check_for_errors" : 5,
                             "get_display_output" : 6,
                             "set_display_output" : 7, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IStrategyMATLABFull3D._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLABFull3D from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IStrategyMATLABFull3D.__dict__ and type(IStrategyMATLABFull3D.__dict__[attrname]) == property:
            return IStrategyMATLABFull3D.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IStrategyMATLABFull3D.")
    
    _get_function_name_metadata = { "name" : "function_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def function_name(self) -> str:
        """The name of the MATLAB function."""
        return self._intf.get_property(IStrategyMATLABFull3D._metadata, IStrategyMATLABFull3D._get_function_name_metadata)

    _set_function_name_metadata = { "name" : "function_name",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @function_name.setter
    def function_name(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        return self._intf.set_property(IStrategyMATLABFull3D._metadata, IStrategyMATLABFull3D._set_function_name_metadata, newVal)

    _is_function_path_valid_metadata = { "name" : "is_function_path_valid",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(IStrategyMATLABFull3D._metadata, IStrategyMATLABFull3D._is_function_path_valid_metadata, out_arg())

    _get_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def check_for_errors(self) -> bool:
        """The option to check the function for errors."""
        return self._intf.get_property(IStrategyMATLABFull3D._metadata, IStrategyMATLABFull3D._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @check_for_errors.setter
    def check_for_errors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        return self._intf.set_property(IStrategyMATLABFull3D._metadata, IStrategyMATLABFull3D._set_check_for_errors_metadata, newVal)

    _get_display_output_metadata = { "name" : "display_output",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def display_output(self) -> bool:
        """The option to display the output from the MATLAB function."""
        return self._intf.get_property(IStrategyMATLABFull3D._metadata, IStrategyMATLABFull3D._get_display_output_metadata)

    _set_display_output_metadata = { "name" : "display_output",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @display_output.setter
    def display_output(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        return self._intf.set_property(IStrategyMATLABFull3D._metadata, IStrategyMATLABFull3D._set_display_output_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{eb6b432e-50fc-4546-9d4b-a4285ae96a9d}", IStrategyMATLABFull3D)
agcls.AgTypeNameMap["IStrategyMATLABFull3D"] = IStrategyMATLABFull3D

class IStrategyMATLAB3DGuidance(object):
    """Interface used to access options for a MATLAB - 3D Guidance Strategy of a Basic Maneuver Procedure."""
    _num_methods = 29
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{fa4719ee-da5b-4845-af69-09ce61f4109e}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_target_name" : 1,
                             "set_target_name" : 2,
                             "get_valid_target_names" : 3,
                             "get_target_resolution" : 4,
                             "set_target_resolution" : 5,
                             "get_use_stop_time_to_go" : 6,
                             "get_stop_time_to_go" : 7,
                             "set_stop_time_to_go" : 8,
                             "get_use_stop_slant_range" : 9,
                             "get_stop_slant_range" : 10,
                             "set_stop_slant_range" : 11,
                             "get_function_name" : 12,
                             "set_function_name" : 13,
                             "is_function_path_valid" : 14,
                             "get_check_for_errors" : 15,
                             "set_check_for_errors" : 16,
                             "get_display_output" : 17,
                             "set_display_output" : 18,
                             "get_closure_mode" : 19,
                             "set_closure_mode" : 20,
                             "get_hobs_max_angle" : 21,
                             "set_hobs_max_angle" : 22,
                             "get_hobs_angle_tol" : 23,
                             "set_hobs_angle_tol" : 24,
                             "get_compute_tas_dot" : 25,
                             "set_compute_tas_dot" : 26,
                             "get_airspeed_options" : 27,
                             "get_position_vel_strategies" : 28,
                             "cancel_tgt_position_vel" : 29, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IStrategyMATLAB3DGuidance._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLAB3DGuidance from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IStrategyMATLAB3DGuidance.__dict__ and type(IStrategyMATLAB3DGuidance.__dict__[attrname]) == property:
            return IStrategyMATLAB3DGuidance.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IStrategyMATLAB3DGuidance.")
    
    _get_target_name_metadata = { "name" : "target_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def target_name(self) -> str:
        """The target name."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_target_name_metadata)

    _set_target_name_metadata = { "name" : "target_name",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @target_name.setter
    def target_name(self, newVal:str) -> None:
        """The target name."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_target_name_metadata, newVal)

    _get_valid_target_names_metadata = { "name" : "valid_target_names",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    @property
    def valid_target_names(self) -> list:
        """Return the valid target names."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_valid_target_names_metadata)

    _get_target_resolution_metadata = { "name" : "target_resolution",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def target_resolution(self) -> float:
        """The target position/velocity sampling resolution."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_target_resolution_metadata)

    _set_target_resolution_metadata = { "name" : "target_resolution",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @target_resolution.setter
    def target_resolution(self, newVal:float) -> None:
        """The target position/velocity sampling resolution."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_target_resolution_metadata, newVal)

    _get_use_stop_time_to_go_metadata = { "name" : "use_stop_time_to_go",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def use_stop_time_to_go(self) -> bool:
        """The option to specify a time to go stopping condition."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_use_stop_time_to_go_metadata)

    _get_stop_time_to_go_metadata = { "name" : "stop_time_to_go",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def stop_time_to_go(self) -> float:
        """The stop time from the target at which the maneuver will stop."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_stop_time_to_go_metadata)

    _set_stop_time_to_go_metadata = { "name" : "set_stop_time_to_go",
            "arg_types" : (agcom.VARIANT_BOOL, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg, agmarshall.DOUBLE_arg,) }
    def set_stop_time_to_go(self, enable:bool, time:float) -> None:
        """Set the option to use the stop time from target stopping condition and set the according value."""
        return self._intf.invoke(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_stop_time_to_go_metadata, enable, time)

    _get_use_stop_slant_range_metadata = { "name" : "use_stop_slant_range",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def use_stop_slant_range(self) -> bool:
        """The option to specify a range from target stopping condition."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_use_stop_slant_range_metadata)

    _get_stop_slant_range_metadata = { "name" : "stop_slant_range",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def stop_slant_range(self) -> float:
        """The range from the target at which the maneuver will stop."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_stop_slant_range_metadata)

    _set_stop_slant_range_metadata = { "name" : "set_stop_slant_range",
            "arg_types" : (agcom.VARIANT_BOOL, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg, agmarshall.DOUBLE_arg,) }
    def set_stop_slant_range(self, enable:bool, range:float) -> None:
        """Set the option to use the stop slant range stopping condition and set the according value."""
        return self._intf.invoke(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_stop_slant_range_metadata, enable, range)

    _get_function_name_metadata = { "name" : "function_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def function_name(self) -> str:
        """The name of the MATLAB function."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_function_name_metadata)

    _set_function_name_metadata = { "name" : "function_name",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @function_name.setter
    def function_name(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_function_name_metadata, newVal)

    _is_function_path_valid_metadata = { "name" : "is_function_path_valid",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    def is_function_path_valid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        return self._intf.invoke(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._is_function_path_valid_metadata, out_arg())

    _get_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def check_for_errors(self) -> bool:
        """The option to check the function for errors."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_check_for_errors_metadata)

    _set_check_for_errors_metadata = { "name" : "check_for_errors",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @check_for_errors.setter
    def check_for_errors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_check_for_errors_metadata, newVal)

    _get_display_output_metadata = { "name" : "display_output",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def display_output(self) -> bool:
        """The option to display the output from the MATLAB function."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_display_output_metadata)

    _set_display_output_metadata = { "name" : "display_output",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @display_output.setter
    def display_output(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_display_output_metadata, newVal)

    _get_closure_mode_metadata = { "name" : "closure_mode",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(CLOSURE_MODE),) }
    @property
    def closure_mode(self) -> "CLOSURE_MODE":
        """The closure mode for the guidance strategy."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_closure_mode_metadata)

    _set_closure_mode_metadata = { "name" : "closure_mode",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(CLOSURE_MODE),) }
    @closure_mode.setter
    def closure_mode(self, newVal:"CLOSURE_MODE") -> None:
        """The closure mode for the guidance strategy."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_closure_mode_metadata, newVal)

    _get_hobs_max_angle_metadata = { "name" : "hobs_max_angle",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def hobs_max_angle(self) -> typing.Any:
        """The closure high off boresight max angle."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_hobs_max_angle_metadata)

    _set_hobs_max_angle_metadata = { "name" : "hobs_max_angle",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @hobs_max_angle.setter
    def hobs_max_angle(self, newVal:typing.Any) -> None:
        """The closure high off boresight max angle."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_hobs_max_angle_metadata, newVal)

    _get_hobs_angle_tol_metadata = { "name" : "hobs_angle_tol",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def hobs_angle_tol(self) -> typing.Any:
        """The closure high off boresight angle tolerance."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_hobs_angle_tol_metadata)

    _set_hobs_angle_tol_metadata = { "name" : "hobs_angle_tol",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @hobs_angle_tol.setter
    def hobs_angle_tol(self, newVal:typing.Any) -> None:
        """The closure high off boresight angle tolerance."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_hobs_angle_tol_metadata, newVal)

    _get_compute_tas_dot_metadata = { "name" : "compute_tas_dot",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def compute_tas_dot(self) -> bool:
        """The option to allow MATLAB to compute the true airspeed for the aircraft."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_compute_tas_dot_metadata)

    _set_compute_tas_dot_metadata = { "name" : "compute_tas_dot",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @compute_tas_dot.setter
    def compute_tas_dot(self, newVal:bool) -> None:
        """The option to allow MATLAB to compute the true airspeed for the aircraft."""
        return self._intf.set_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._set_compute_tas_dot_metadata, newVal)

    _get_airspeed_options_metadata = { "name" : "airspeed_options",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def airspeed_options(self) -> "IBasicManeuverAirspeedOptions":
        """Get the airspeed options."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_airspeed_options_metadata)

    _get_position_vel_strategies_metadata = { "name" : "position_vel_strategies",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def position_vel_strategies(self) -> "IBasicManeuverTargetPositionVel":
        """The position velocity strategies for MATLAB 3D Guidance."""
        return self._intf.get_property(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._get_position_vel_strategies_metadata)

    _cancel_tgt_position_vel_metadata = { "name" : "cancel_tgt_position_vel",
            "arg_types" : (),
            "marshallers" : () }
    def cancel_tgt_position_vel(self) -> None:
        """Cancel the position velocity strategies for MATLAB 3D Guidance."""
        return self._intf.invoke(IStrategyMATLAB3DGuidance._metadata, IStrategyMATLAB3DGuidance._cancel_tgt_position_vel_metadata, )


agcls.AgClassCatalog.add_catalog_entry("{fa4719ee-da5b-4845-af69-09ce61f4109e}", IStrategyMATLAB3DGuidance)
agcls.AgTypeNameMap["IStrategyMATLAB3DGuidance"] = IStrategyMATLAB3DGuidance



class StrategyMATLABNav(IStrategyMATLABNav, IBasicManeuverStrategy):
    """Class defining the MATLAB - Horizontal Plane strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLABNav.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IStrategyMATLABNav._private_init(self, intf)
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IStrategyMATLABNav._get_property(self, attrname) is not None: found_prop = IStrategyMATLABNav._get_property(self, attrname)
        if IBasicManeuverStrategy._get_property(self, attrname) is not None: found_prop = IBasicManeuverStrategy._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in StrategyMATLABNav.")

agcls.AgClassCatalog.add_catalog_entry("{4447B282-8834-4451-8CD8-0A3168015B45}", StrategyMATLABNav)
agcls.AgTypeNameMap["StrategyMATLABNav"] = StrategyMATLABNav

class StrategyMATLABProfile(IStrategyMATLABProfile, IBasicManeuverStrategy):
    """Class defining the MATLAB - Vertical Plane strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLABProfile.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IStrategyMATLABProfile._private_init(self, intf)
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IStrategyMATLABProfile._get_property(self, attrname) is not None: found_prop = IStrategyMATLABProfile._get_property(self, attrname)
        if IBasicManeuverStrategy._get_property(self, attrname) is not None: found_prop = IBasicManeuverStrategy._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in StrategyMATLABProfile.")

agcls.AgClassCatalog.add_catalog_entry("{1bf89982-311b-4b61-ba17-00881de09863}", StrategyMATLABProfile)
agcls.AgTypeNameMap["StrategyMATLABProfile"] = StrategyMATLABProfile

class StrategyMATLABFull3D(IStrategyMATLABFull3D, IBasicManeuverStrategy):
    """Class defining the MATLAB - Full 3D strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLABFull3D.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IStrategyMATLABFull3D._private_init(self, intf)
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IStrategyMATLABFull3D._get_property(self, attrname) is not None: found_prop = IStrategyMATLABFull3D._get_property(self, attrname)
        if IBasicManeuverStrategy._get_property(self, attrname) is not None: found_prop = IBasicManeuverStrategy._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in StrategyMATLABFull3D.")

agcls.AgClassCatalog.add_catalog_entry("{7fdf8025-0f64-4f1a-9c12-8275051354d4}", StrategyMATLABFull3D)
agcls.AgTypeNameMap["StrategyMATLABFull3D"] = StrategyMATLABFull3D

class StrategyMATLAB3DGuidance(IStrategyMATLAB3DGuidance, IBasicManeuverStrategy):
    """Class defining the MATLAB - 3D Guidance strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLAB3DGuidance.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IStrategyMATLAB3DGuidance._private_init(self, intf)
        IBasicManeuverStrategy._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IStrategyMATLAB3DGuidance._get_property(self, attrname) is not None: found_prop = IStrategyMATLAB3DGuidance._get_property(self, attrname)
        if IBasicManeuverStrategy._get_property(self, attrname) is not None: found_prop = IBasicManeuverStrategy._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in StrategyMATLAB3DGuidance.")

agcls.AgClassCatalog.add_catalog_entry("{c90db66d-a2fa-4474-9c21-2e8f61b93fad}", StrategyMATLAB3DGuidance)
agcls.AgTypeNameMap["StrategyMATLAB3DGuidance"] = StrategyMATLAB3DGuidance

class BasicManeuverMATLABFactory(IAutomationStrategyFactory):
    """Class defining the factory to create the basic maneuver PropNav strategies."""
    def __init__(self, sourceObject=None):
        IAutomationStrategyFactory.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IAutomationStrategyFactory._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAutomationStrategyFactory._get_property(self, attrname) is not None: found_prop = IAutomationStrategyFactory._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in BasicManeuverMATLABFactory.")

agcls.AgClassCatalog.add_catalog_entry("{29352A63-3095-4D7E-A056-189D672BF458}", BasicManeuverMATLABFactory)
agcls.AgTypeNameMap["BasicManeuverMATLABFactory"] = BasicManeuverMATLABFactory


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
