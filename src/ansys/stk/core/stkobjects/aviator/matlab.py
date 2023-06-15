################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["BasicManeuverMATLABFactory", "IStrategyMATLAB3DGuidance", "IStrategyMATLABFull3D", "IStrategyMATLABNav", "IStrategyMATLABProfile", 
"StrategyMATLAB3DGuidance", "StrategyMATLABFull3D", "StrategyMATLABNav", "StrategyMATLABProfile"]

import typing

from ctypes   import byref, POINTER

try:
    from numpy import ndarray # noqa
except ModuleNotFoundError:
    pass
    
try:
    from pandas import DataFrame # noqa
except ModuleNotFoundError:
    pass

from ...internal  import comutil          as agcom
from ...internal  import coclassutil      as agcls
from ...internal  import marshall         as agmarshall
from ...internal.comutil     import IUnknown, IAGFUNCTYPE
from ...internal.eventutil   import *
from ...utilities.exceptions import *

from ...stkobjects.aviator import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class IStrategyMATLABNav(object):
    """Interface used to access options for a MATLAB - Horizontal Plane Strategy of a Basic Maneuver Procedure."""
    _uuid = "{e53fcce4-1a17-488d-9053-c236d27b8b6e}"
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_SetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_IsFunctionPathValid"] = _raise_uninitialized_error
        self.__dict__["_GetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_SetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_GetDisplayOutput"] = _raise_uninitialized_error
        self.__dict__["_SetDisplayOutput"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IStrategyMATLABNav._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLABNav from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IStrategyMATLABNav = agcom.GUID(IStrategyMATLABNav._uuid)
        vtable_offset_local = IStrategyMATLABNav._vtable_offset - 1
        self.__dict__["_GetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABNav, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABNav, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_IsFunctionPathValid"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABNav, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABNav, vtable_offset_local+4, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABNav, vtable_offset_local+5, agcom.VARIANT_BOOL)
        self.__dict__["_GetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABNav, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABNav, vtable_offset_local+7, agcom.VARIANT_BOOL)
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
    
    @property
    def FunctionName(self) -> str:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFunctionName"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FunctionName.setter
    def FunctionName(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFunctionName"](arg_newVal.COM_val))

    def IsFunctionPathValid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_IsFunctionPathValid"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def CheckForErrors(self) -> bool:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCheckForErrors"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @CheckForErrors.setter
    def CheckForErrors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetCheckForErrors"](arg_newVal.COM_val))

    @property
    def DisplayOutput(self) -> bool:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetDisplayOutput"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @DisplayOutput.setter
    def DisplayOutput(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetDisplayOutput"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{e53fcce4-1a17-488d-9053-c236d27b8b6e}", IStrategyMATLABNav)
agcls.AgTypeNameMap["IStrategyMATLABNav"] = IStrategyMATLABNav

class IStrategyMATLABProfile(object):
    """Interface used to access options for a MATLAB - Vertical Plane Strategy of a Basic Maneuver Procedure."""
    _uuid = "{c5c0a490-9e7d-4ff9-95e9-9c10ed89500b}"
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_SetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_IsFunctionPathValid"] = _raise_uninitialized_error
        self.__dict__["_GetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_SetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_GetDisplayOutput"] = _raise_uninitialized_error
        self.__dict__["_SetDisplayOutput"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IStrategyMATLABProfile._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLABProfile from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IStrategyMATLABProfile = agcom.GUID(IStrategyMATLABProfile._uuid)
        vtable_offset_local = IStrategyMATLABProfile._vtable_offset - 1
        self.__dict__["_GetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABProfile, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABProfile, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_IsFunctionPathValid"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABProfile, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABProfile, vtable_offset_local+4, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABProfile, vtable_offset_local+5, agcom.VARIANT_BOOL)
        self.__dict__["_GetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABProfile, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABProfile, vtable_offset_local+7, agcom.VARIANT_BOOL)
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
    
    @property
    def FunctionName(self) -> str:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFunctionName"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FunctionName.setter
    def FunctionName(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFunctionName"](arg_newVal.COM_val))

    def IsFunctionPathValid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_IsFunctionPathValid"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def CheckForErrors(self) -> bool:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCheckForErrors"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @CheckForErrors.setter
    def CheckForErrors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetCheckForErrors"](arg_newVal.COM_val))

    @property
    def DisplayOutput(self) -> bool:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetDisplayOutput"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @DisplayOutput.setter
    def DisplayOutput(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetDisplayOutput"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{c5c0a490-9e7d-4ff9-95e9-9c10ed89500b}", IStrategyMATLABProfile)
agcls.AgTypeNameMap["IStrategyMATLABProfile"] = IStrategyMATLABProfile

class IStrategyMATLABFull3D(object):
    """Interface used to access options for a MATLAB - Full 3D Strategy of a Basic Maneuver Procedure."""
    _uuid = "{eb6b432e-50fc-4546-9d4b-a4285ae96a9d}"
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_SetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_IsFunctionPathValid"] = _raise_uninitialized_error
        self.__dict__["_GetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_SetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_GetDisplayOutput"] = _raise_uninitialized_error
        self.__dict__["_SetDisplayOutput"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IStrategyMATLABFull3D._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLABFull3D from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IStrategyMATLABFull3D = agcom.GUID(IStrategyMATLABFull3D._uuid)
        vtable_offset_local = IStrategyMATLABFull3D._vtable_offset - 1
        self.__dict__["_GetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABFull3D, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABFull3D, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_IsFunctionPathValid"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABFull3D, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABFull3D, vtable_offset_local+4, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABFull3D, vtable_offset_local+5, agcom.VARIANT_BOOL)
        self.__dict__["_GetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABFull3D, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLABFull3D, vtable_offset_local+7, agcom.VARIANT_BOOL)
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
    
    @property
    def FunctionName(self) -> str:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFunctionName"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FunctionName.setter
    def FunctionName(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFunctionName"](arg_newVal.COM_val))

    def IsFunctionPathValid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_IsFunctionPathValid"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def CheckForErrors(self) -> bool:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCheckForErrors"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @CheckForErrors.setter
    def CheckForErrors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetCheckForErrors"](arg_newVal.COM_val))

    @property
    def DisplayOutput(self) -> bool:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetDisplayOutput"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @DisplayOutput.setter
    def DisplayOutput(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetDisplayOutput"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{eb6b432e-50fc-4546-9d4b-a4285ae96a9d}", IStrategyMATLABFull3D)
agcls.AgTypeNameMap["IStrategyMATLABFull3D"] = IStrategyMATLABFull3D

class IStrategyMATLAB3DGuidance(object):
    """Interface used to access options for a MATLAB - 3D Guidance Strategy of a Basic Maneuver Procedure."""
    _uuid = "{fa4719ee-da5b-4845-af69-09ce61f4109e}"
    _num_methods = 27
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetTargetName"] = _raise_uninitialized_error
        self.__dict__["_SetTargetName"] = _raise_uninitialized_error
        self.__dict__["_GetValidTargetNames"] = _raise_uninitialized_error
        self.__dict__["_GetTargetResolution"] = _raise_uninitialized_error
        self.__dict__["_SetTargetResolution"] = _raise_uninitialized_error
        self.__dict__["_GetUseStopTimeToGo"] = _raise_uninitialized_error
        self.__dict__["_GetStopTimeToGo"] = _raise_uninitialized_error
        self.__dict__["_SetStopTimeToGo"] = _raise_uninitialized_error
        self.__dict__["_GetUseStopSlantRange"] = _raise_uninitialized_error
        self.__dict__["_GetStopSlantRange"] = _raise_uninitialized_error
        self.__dict__["_SetStopSlantRange"] = _raise_uninitialized_error
        self.__dict__["_GetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_SetFunctionName"] = _raise_uninitialized_error
        self.__dict__["_IsFunctionPathValid"] = _raise_uninitialized_error
        self.__dict__["_GetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_SetCheckForErrors"] = _raise_uninitialized_error
        self.__dict__["_GetDisplayOutput"] = _raise_uninitialized_error
        self.__dict__["_SetDisplayOutput"] = _raise_uninitialized_error
        self.__dict__["_GetClosureMode"] = _raise_uninitialized_error
        self.__dict__["_SetClosureMode"] = _raise_uninitialized_error
        self.__dict__["_GetHOBSMaxAngle"] = _raise_uninitialized_error
        self.__dict__["_SetHOBSMaxAngle"] = _raise_uninitialized_error
        self.__dict__["_GetHOBSAngleTol"] = _raise_uninitialized_error
        self.__dict__["_SetHOBSAngleTol"] = _raise_uninitialized_error
        self.__dict__["_GetComputeTASDot"] = _raise_uninitialized_error
        self.__dict__["_SetComputeTASDot"] = _raise_uninitialized_error
        self.__dict__["_GetAirspeedOptions"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IStrategyMATLAB3DGuidance._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IStrategyMATLAB3DGuidance from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IStrategyMATLAB3DGuidance = agcom.GUID(IStrategyMATLAB3DGuidance._uuid)
        vtable_offset_local = IStrategyMATLAB3DGuidance._vtable_offset - 1
        self.__dict__["_GetTargetName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetTargetName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_GetValidTargetNames"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+3, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetTargetResolution"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_SetTargetResolution"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+5, agcom.DOUBLE)
        self.__dict__["_GetUseStopTimeToGo"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetStopTimeToGo"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_SetStopTimeToGo"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+8, agcom.VARIANT_BOOL, agcom.DOUBLE)
        self.__dict__["_GetUseStopSlantRange"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+9, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetStopSlantRange"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__["_SetStopSlantRange"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+11, agcom.VARIANT_BOOL, agcom.DOUBLE)
        self.__dict__["_GetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+12, POINTER(agcom.BSTR))
        self.__dict__["_SetFunctionName"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+13, agcom.BSTR)
        self.__dict__["_IsFunctionPathValid"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+14, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+15, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetCheckForErrors"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+16, agcom.VARIANT_BOOL)
        self.__dict__["_GetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+17, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetDisplayOutput"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+18, agcom.VARIANT_BOOL)
        self.__dict__["_GetClosureMode"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+19, POINTER(agcom.LONG))
        self.__dict__["_SetClosureMode"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+20, agcom.LONG)
        self.__dict__["_GetHOBSMaxAngle"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+21, POINTER(agcom.VARIANT))
        self.__dict__["_SetHOBSMaxAngle"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+22, agcom.VARIANT)
        self.__dict__["_GetHOBSAngleTol"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+23, POINTER(agcom.VARIANT))
        self.__dict__["_SetHOBSAngleTol"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+24, agcom.VARIANT)
        self.__dict__["_GetComputeTASDot"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+25, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetComputeTASDot"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+26, agcom.VARIANT_BOOL)
        self.__dict__["_GetAirspeedOptions"] = IAGFUNCTYPE(pUnk, IID_IStrategyMATLAB3DGuidance, vtable_offset_local+27, POINTER(agcom.PVOID))
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
    
    @property
    def TargetName(self) -> str:
        """The target name."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetTargetName"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @TargetName.setter
    def TargetName(self, newVal:str) -> None:
        """The target name."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetTargetName"](arg_newVal.COM_val))

    @property
    def ValidTargetNames(self) -> list:
        """Returns the valid target names."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetValidTargetNames"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    @property
    def TargetResolution(self) -> float:
        """The target position/velocity sampling resolution."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetTargetResolution"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @TargetResolution.setter
    def TargetResolution(self, newVal:float) -> None:
        """The target position/velocity sampling resolution."""
        with agmarshall.DOUBLE_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetTargetResolution"](arg_newVal.COM_val))

    @property
    def UseStopTimeToGo(self) -> bool:
        """The option to specify a time to go stopping condition."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUseStopTimeToGo"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def StopTimeToGo(self) -> float:
        """The stop time from the target at which the maneuver will stop."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetStopTimeToGo"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetStopTimeToGo(self, enable:bool, time:float) -> None:
        """Set the option to use the stop time from target stopping condition and set the according value."""
        with agmarshall.VARIANT_BOOL_arg(enable) as arg_enable, \
             agmarshall.DOUBLE_arg(time) as arg_time:
            agcls.evaluate_hresult(self.__dict__["_SetStopTimeToGo"](arg_enable.COM_val, arg_time.COM_val))

    @property
    def UseStopSlantRange(self) -> bool:
        """The option to specify a range from target stopping condition."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUseStopSlantRange"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def StopSlantRange(self) -> float:
        """The range from the target at which the maneuver will stop."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetStopSlantRange"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetStopSlantRange(self, enable:bool, range:float) -> None:
        """Set the option to use the stop slant range stopping condition and set the according value."""
        with agmarshall.VARIANT_BOOL_arg(enable) as arg_enable, \
             agmarshall.DOUBLE_arg(range) as arg_range:
            agcls.evaluate_hresult(self.__dict__["_SetStopSlantRange"](arg_enable.COM_val, arg_range.COM_val))

    @property
    def FunctionName(self) -> str:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFunctionName"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FunctionName.setter
    def FunctionName(self, newVal:str) -> None:
        """The name of the MATLAB function."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFunctionName"](arg_newVal.COM_val))

    def IsFunctionPathValid(self) -> bool:
        """Check if the MATLAB function path is valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_IsFunctionPathValid"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def CheckForErrors(self) -> bool:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCheckForErrors"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @CheckForErrors.setter
    def CheckForErrors(self, newVal:bool) -> None:
        """The option to check the function for errors."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetCheckForErrors"](arg_newVal.COM_val))

    @property
    def DisplayOutput(self) -> bool:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetDisplayOutput"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @DisplayOutput.setter
    def DisplayOutput(self, newVal:bool) -> None:
        """The option to display the output from the MATLAB function."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetDisplayOutput"](arg_newVal.COM_val))

    @property
    def ClosureMode(self) -> "AgEAvtrClosureMode":
        """The closure mode for the guidance strategy."""
        with agmarshall.AgEnum_arg(AgEAvtrClosureMode) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetClosureMode"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @ClosureMode.setter
    def ClosureMode(self, newVal:"AgEAvtrClosureMode") -> None:
        """The closure mode for the guidance strategy."""
        with agmarshall.AgEnum_arg(AgEAvtrClosureMode, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetClosureMode"](arg_newVal.COM_val))

    @property
    def HOBSMaxAngle(self) -> typing.Any:
        """The closure high off boresight max angle."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetHOBSMaxAngle"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @HOBSMaxAngle.setter
    def HOBSMaxAngle(self, newVal:typing.Any) -> None:
        """The closure high off boresight max angle."""
        with agmarshall.VARIANT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetHOBSMaxAngle"](arg_newVal.COM_val))

    @property
    def HOBSAngleTol(self) -> typing.Any:
        """The closure high off boresight angle tolerance."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetHOBSAngleTol"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @HOBSAngleTol.setter
    def HOBSAngleTol(self, newVal:typing.Any) -> None:
        """The closure high off boresight angle tolerance."""
        with agmarshall.VARIANT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetHOBSAngleTol"](arg_newVal.COM_val))

    @property
    def ComputeTASDot(self) -> bool:
        """The option to allow MATLAB to compute the true airspeed for the aircraft."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetComputeTASDot"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @ComputeTASDot.setter
    def ComputeTASDot(self, newVal:bool) -> None:
        """The option to allow MATLAB to compute the true airspeed for the aircraft."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetComputeTASDot"](arg_newVal.COM_val))

    @property
    def AirspeedOptions(self) -> "IBasicManeuverAirspeedOptions":
        """Get the airspeed options."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetAirspeedOptions"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{fa4719ee-da5b-4845-af69-09ce61f4109e}", IStrategyMATLAB3DGuidance)
agcls.AgTypeNameMap["IStrategyMATLAB3DGuidance"] = IStrategyMATLAB3DGuidance



class StrategyMATLABNav(IStrategyMATLABNav, IBasicManeuverStrategy):
    """Class defining the MATLAB - Horizontal Plane strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLABNav.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IStrategyMATLABNav._private_init(self, pUnk)
        IBasicManeuverStrategy._private_init(self, pUnk)
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


class StrategyMATLABProfile(IStrategyMATLABProfile, IBasicManeuverStrategy):
    """Class defining the MATLAB - Vertical Plane strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLABProfile.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IStrategyMATLABProfile._private_init(self, pUnk)
        IBasicManeuverStrategy._private_init(self, pUnk)
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


class StrategyMATLABFull3D(IStrategyMATLABFull3D, IBasicManeuverStrategy):
    """Class defining the MATLAB - Full 3D strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLABFull3D.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IStrategyMATLABFull3D._private_init(self, pUnk)
        IBasicManeuverStrategy._private_init(self, pUnk)
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


class StrategyMATLAB3DGuidance(IStrategyMATLAB3DGuidance, IBasicManeuverStrategy):
    """Class defining the MATLAB - 3D Guidance strategy for a basic maneuver procedure."""
    def __init__(self, sourceObject=None):
        IStrategyMATLAB3DGuidance.__init__(self, sourceObject)
        IBasicManeuverStrategy.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IStrategyMATLAB3DGuidance._private_init(self, pUnk)
        IBasicManeuverStrategy._private_init(self, pUnk)
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


class BasicManeuverMATLABFactory(IAutomationStrategyFactory):
    """Class defining the factory to create the basic maneuver PropNav strategies."""
    def __init__(self, sourceObject=None):
        IAutomationStrategyFactory.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAutomationStrategyFactory._private_init(self, pUnk)
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



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
