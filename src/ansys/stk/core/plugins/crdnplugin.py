################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = []

import typing

from ctypes   import byref, POINTER
from datetime import datetime
from enum     import IntEnum, IntFlag

try:
    from numpy import ndarray
except ModuleNotFoundError:
    pass
    
try:
    from pandas import DataFrame
except ModuleNotFoundError:
    pass

from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal  import dataanalysisutil as agdata
from ..utilities import colors           as agcolor
from ..internal.comutil     import IUnknown, IDispatch, IPictureDisp, IAGFUNCTYPE, IEnumVARIANT
from ..internal.eventutil   import *
from ..utilities.exceptions import *


from ..plugins.utplugin import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgECrdnEulerSequence(IntEnum):
    """Enumeration AgECrdnEulerSequence."""
    # Sequence defined by rotation about x-axis, then about rotated y-axis, then about rotated x-axis.
    eCrdnEulerSequence121 = 121,
    # Sequence defined by rotation about x-axis, then about rotated y-axis, then about rotated z-axis.
    eCrdnEulerSequence123 = 123,
    # Sequence defined by rotation about x-axis, then about rotated z-axis, then about rotated x-axis.
    eCrdnEulerSequence131 = 131,
    # Sequence defined by rotation about x-axis, then about rotated z-axis, then about rotated y-axis.
    eCrdnEulerSequence132 = 132,
    # Sequence defined by rotation about y-axis, then about rotated x-axis, then about rotated y-axis.
    eCrdnEulerSequence212 = 212,
    # Sequence defined by rotation about y-axis, then about rotated x-axis, then about rotated z-axis.
    eCrdnEulerSequence213 = 213,
    # Sequence defined by rotation about y-axis, then about rotated z-axis, then about rotated x-axis.
    eCrdnEulerSequence231 = 231,
    # Sequence defined by rotation about y-axis, then about rotated z-axis, then about rotated y-axis.
    eCrdnEulerSequence232 = 232,
    # Sequence defined by rotation about z-axis, then about rotated x-axis, then about rotated y-axis.
    eCrdnEulerSequence312 = 312,
    # Sequence defined by rotation about z-axis, then about rotated x-axis, then about rotated z-axis.
    eCrdnEulerSequence313 = 313,
    # Sequence defined by rotation about z-axis, then about rotated y-axis, then about rotated x-axis.
    eCrdnEulerSequence321 = 321,
    # Sequence defined by rotation about z-axis, then about rotated y-axis, then about rotated x-axis.
    eCrdnEulerSequence323 = 323

agcls.AgTypeNameMap["AgECrdnEulerSequence"] = AgECrdnEulerSequence
__all__.append("AgECrdnEulerSequence")


class IAgCrdnConfiguredVector(object):
    """Crdn Vector object interface which computes its components."""
    _uuid = "{2ABB252C-9FFA-4f2b-BF41-4CC3A4E4DF84}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredVector._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredVector from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredVector = agcom.GUID(IAgCrdnConfiguredVector._uuid)
        vtable_offset_local = IAgCrdnConfiguredVector._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVector, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVector, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVector, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVector, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVector, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVector, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredVector.__dict__ and type(IAgCrdnConfiguredVector.__dict__[attrname]) == property:
            return IAgCrdnConfiguredVector.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredVector.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any."""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the Vector (in internal units) at the given time returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the Vector (in internal units) at the interface's current time, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{2ABB252C-9FFA-4f2b-BF41-4CC3A4E4DF84}", IAgCrdnConfiguredVector)
agcls.AgTypeNameMap["IAgCrdnConfiguredVector"] = IAgCrdnConfiguredVector
__all__.append("IAgCrdnConfiguredVector")

class IAgCrdnConfiguredVectorWithRate(object):
    """Crdn Vector object interface which computes its components and rates."""
    _uuid = "{3F126133-81A4-4126-95B5-3F832EB3D2A8}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredVectorWithRate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredVectorWithRate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredVectorWithRate = agcom.GUID(IAgCrdnConfiguredVectorWithRate._uuid)
        vtable_offset_local = IAgCrdnConfiguredVectorWithRate._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVectorWithRate, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVectorWithRate, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVectorWithRate, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVectorWithRate, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVectorWithRate, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredVectorWithRate, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredVectorWithRate.__dict__ and type(IAgCrdnConfiguredVectorWithRate.__dict__[attrname]) == property:
            return IAgCrdnConfiguredVectorWithRate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredVectorWithRate.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the Vector and its rate (in internal units) at the given time returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the Vector and its rate (in internal units) at the interface's current time, returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{3F126133-81A4-4126-95B5-3F832EB3D2A8}", IAgCrdnConfiguredVectorWithRate)
agcls.AgTypeNameMap["IAgCrdnConfiguredVectorWithRate"] = IAgCrdnConfiguredVectorWithRate
__all__.append("IAgCrdnConfiguredVectorWithRate")

class IAgCrdnConfiguredAxes(object):
    """Crdn Axes object interface which computes its quaternion."""
    _uuid = "{05D845F4-4C85-4e09-B03D-791FF9F130EE}"
    _num_methods = 10
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredAxes._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredAxes from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredAxes = agcom.GUID(IAgCrdnConfiguredAxes._uuid)
        vtable_offset_local = IAgCrdnConfiguredAxes._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponents"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+7, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponents_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+8, agcom.PVOID, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponentsAtEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+9, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponentsAtEpoch_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxes, vtable_offset_local+10, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredAxes.__dict__ and type(IAgCrdnConfiguredAxes.__dict__[attrname]) == property:
            return IAgCrdnConfiguredAxes.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredAxes.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the quaternion representing the Axes at the given time returned as an array representing q1, q2, q3, q4. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the quaternion representing the Axes at the interface's current time, returned as an array representing q1, q2, q3, q4. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponents_Array(self, dispInterface:"IDispatch", x:float, y:float, z:float) -> list:
        """Transforms vector components given wrt Axes into those wrt RefAxes at the interface's current time, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponents_Array"](arg_dispInterface.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponentsAtEpoch_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float, x:float, y:float, z:float) -> list:
        """Transforms vector components given wrt Axes into those wrt RefAxes at the given time, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponentsAtEpoch_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{05D845F4-4C85-4e09-B03D-791FF9F130EE}", IAgCrdnConfiguredAxes)
agcls.AgTypeNameMap["IAgCrdnConfiguredAxes"] = IAgCrdnConfiguredAxes
__all__.append("IAgCrdnConfiguredAxes")

class IAgCrdnConfiguredAxesWithRate(object):
    """Crdn Axes object interface which computes its quaternion and angular velocity."""
    _uuid = "{5B2F635E-140B-435c-8B39-CF0BE6D11C79}"
    _num_methods = 10
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredAxesWithRate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredAxesWithRate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredAxesWithRate = agcom.GUID(IAgCrdnConfiguredAxesWithRate._uuid)
        vtable_offset_local = IAgCrdnConfiguredAxesWithRate._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponents"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+7, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponents_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+8, agcom.PVOID, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponentsAtEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+9, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponentsAtEpoch_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAxesWithRate, vtable_offset_local+10, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredAxesWithRate.__dict__ and type(IAgCrdnConfiguredAxesWithRate.__dict__[attrname]) == property:
            return IAgCrdnConfiguredAxesWithRate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredAxesWithRate.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the quaternion representing the Axes and its angular rate in reference components at the given time returned as an array representing q1, q2, q3, q4, wx, wy, wz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the quaternion representing the Axes and its angular rate in reference components at the interface's current time, returned as an array representing q1, q2, q3, q4, wx, wy, wz. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponents_Array(self, dispInterface:"IDispatch", x:float, y:float, z:float, vx:float, vy:float, vz:float) -> list:
        """Transforms vector components given wrt Axes into those wrt RefAxes at the interface's current time, returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg(vx) as arg_vx, \
             agmarshall.DOUBLE_arg(vy) as arg_vy, \
             agmarshall.DOUBLE_arg(vz) as arg_vz, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponents_Array"](arg_dispInterface.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, arg_vx.COM_val, arg_vy.COM_val, arg_vz.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponentsAtEpoch_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float, x:float, y:float, z:float, vx:float, vy:float, vz:float) -> list:
        """Transforms vector components given wrt Axes into those wrt RefAxes at the given time, returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg(vx) as arg_vx, \
             agmarshall.DOUBLE_arg(vy) as arg_vy, \
             agmarshall.DOUBLE_arg(vz) as arg_vz, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponentsAtEpoch_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, arg_vx.COM_val, arg_vy.COM_val, arg_vz.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{5B2F635E-140B-435c-8B39-CF0BE6D11C79}", IAgCrdnConfiguredAxesWithRate)
agcls.AgTypeNameMap["IAgCrdnConfiguredAxesWithRate"] = IAgCrdnConfiguredAxesWithRate
__all__.append("IAgCrdnConfiguredAxesWithRate")

class IAgCrdnConfiguredAngle(object):
    """Crdn Angle object interface."""
    _uuid = "{1E5501EF-C66B-43ed-BD34-BFE573A36D3A}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_RetVal"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_RetVal"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredAngle._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredAngle from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredAngle = agcom.GUID(IAgCrdnConfiguredAngle._uuid)
        vtable_offset_local = IAgCrdnConfiguredAngle._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngle, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngle, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngle, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_RetVal"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngle, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngle, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_RetVal"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngle, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.DOUBLE))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredAngle.__dict__ and type(IAgCrdnConfiguredAngle.__dict__[attrname]) == property:
            return IAgCrdnConfiguredAngle.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredAngle.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_RetVal(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> float:
        """Computes the Angle (rad) at the given time"""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.DOUBLE_arg() as arg_pAngle:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_RetVal"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pAngle.COM_val)))
            return arg_pAngle.python_val

    def CurrentValue_RetVal(self, dispInterface:"IDispatch") -> float:
        """Computes the Angle (rad) at the interface's current time"""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.DOUBLE_arg() as arg_pAngle:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_RetVal"](arg_dispInterface.COM_val, byref(arg_pAngle.COM_val)))
            return arg_pAngle.python_val


agcls.AgClassCatalog.add_catalog_entry("{1E5501EF-C66B-43ed-BD34-BFE573A36D3A}", IAgCrdnConfiguredAngle)
agcls.AgTypeNameMap["IAgCrdnConfiguredAngle"] = IAgCrdnConfiguredAngle
__all__.append("IAgCrdnConfiguredAngle")

class IAgCrdnConfiguredAngleWithRate(object):
    """Crdn Angle object interface."""
    _uuid = "{933C8F8C-9D24-4b77-9F67-4DB1AB2725EA}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredAngleWithRate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredAngleWithRate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredAngleWithRate = agcom.GUID(IAgCrdnConfiguredAngleWithRate._uuid)
        vtable_offset_local = IAgCrdnConfiguredAngleWithRate._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngleWithRate, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngleWithRate, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngleWithRate, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngleWithRate, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngleWithRate, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredAngleWithRate, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredAngleWithRate.__dict__ and type(IAgCrdnConfiguredAngleWithRate.__dict__[attrname]) == property:
            return IAgCrdnConfiguredAngleWithRate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredAngleWithRate.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the Angle and its rate at the given time returned as an array representing angle, angeRate. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the Angle (rad) and its rate (rad/sec) at the interface's current time."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{933C8F8C-9D24-4b77-9F67-4DB1AB2725EA}", IAgCrdnConfiguredAngleWithRate)
agcls.AgTypeNameMap["IAgCrdnConfiguredAngleWithRate"] = IAgCrdnConfiguredAngleWithRate
__all__.append("IAgCrdnConfiguredAngleWithRate")

class IAgCrdnConfiguredPoint(object):
    """Crdn Point object interface which computes its components."""
    _uuid = "{186C9B1E-C3B1-4222-A05E-9177AB68FF69}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredPoint._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredPoint from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredPoint = agcom.GUID(IAgCrdnConfiguredPoint._uuid)
        vtable_offset_local = IAgCrdnConfiguredPoint._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPoint, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPoint, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPoint, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPoint, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPoint, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPoint, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredPoint.__dict__ and type(IAgCrdnConfiguredPoint.__dict__[attrname]) == property:
            return IAgCrdnConfiguredPoint.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredPoint.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the Point (in internal units) at the given time returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the Point (in internal units) at the interface's current time, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{186C9B1E-C3B1-4222-A05E-9177AB68FF69}", IAgCrdnConfiguredPoint)
agcls.AgTypeNameMap["IAgCrdnConfiguredPoint"] = IAgCrdnConfiguredPoint
__all__.append("IAgCrdnConfiguredPoint")

class IAgCrdnConfiguredPointWithRate(object):
    """Crdn Point object interface which computes its components and rates."""
    _uuid = "{0E587016-A94B-4919-BE0E-AFFDB53D4833}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredPointWithRate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredPointWithRate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredPointWithRate = agcom.GUID(IAgCrdnConfiguredPointWithRate._uuid)
        vtable_offset_local = IAgCrdnConfiguredPointWithRate._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPointWithRate, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPointWithRate, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPointWithRate, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPointWithRate, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPointWithRate, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredPointWithRate, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredPointWithRate.__dict__ and type(IAgCrdnConfiguredPointWithRate.__dict__[attrname]) == property:
            return IAgCrdnConfiguredPointWithRate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredPointWithRate.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the Point and its rate (in internal units) at the given time returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the Point and its rate (in internal units) at the interface's current time, returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{0E587016-A94B-4919-BE0E-AFFDB53D4833}", IAgCrdnConfiguredPointWithRate)
agcls.AgTypeNameMap["IAgCrdnConfiguredPointWithRate"] = IAgCrdnConfiguredPointWithRate
__all__.append("IAgCrdnConfiguredPointWithRate")

class IAgCrdnConfiguredSystem(object):
    """Crdn System object interface which computes its components."""
    _uuid = "{58B4303A-78BD-4715-A91F-ED28DBA1F32C}"
    _num_methods = 10
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredSystem._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredSystem from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredSystem = agcom.GUID(IAgCrdnConfiguredSystem._uuid)
        vtable_offset_local = IAgCrdnConfiguredSystem._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponents"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+7, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponents_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+8, agcom.PVOID, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponentsAtEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+9, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponentsAtEpoch_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystem, vtable_offset_local+10, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredSystem.__dict__ and type(IAgCrdnConfiguredSystem.__dict__[attrname]) == property:
            return IAgCrdnConfiguredSystem.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredSystem.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the System position (in internal units) and quaternion at the given time returned as an array representing x, y, z, q1, q2, q3, q4. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the System position (in internal units) and quaternion at the interface's current time, returned as an array representing x, y, z, q1, q2, q3, q4. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponents_Array(self, dispInterface:"IDispatch", x:float, y:float, z:float) -> list:
        """Transforms vector components given wrt System into those wrt RefSystem at the interface's current time, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponents_Array"](arg_dispInterface.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponentsAtEpoch_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float, x:float, y:float, z:float) -> list:
        """Transforms vector components given wrt System into those wrt RefSystem at the given time, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponentsAtEpoch_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{58B4303A-78BD-4715-A91F-ED28DBA1F32C}", IAgCrdnConfiguredSystem)
agcls.AgTypeNameMap["IAgCrdnConfiguredSystem"] = IAgCrdnConfiguredSystem
__all__.append("IAgCrdnConfiguredSystem")

class IAgCrdnConfiguredSystemWithRate(object):
    """Crdn System object interface which computes its components and rates."""
    _uuid = "{01D0AEC2-16CD-4bfd-B964-B420F66FBC35}"
    _num_methods = 10
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents"] = _raise_uninitialized_error
        self.__dict__["_TransformComponents_Array"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch"] = _raise_uninitialized_error
        self.__dict__["_TransformComponentsAtEpoch_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredSystemWithRate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredSystemWithRate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredSystemWithRate = agcom.GUID(IAgCrdnConfiguredSystemWithRate._uuid)
        vtable_offset_local = IAgCrdnConfiguredSystemWithRate._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponents"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+7, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponents_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+8, agcom.PVOID, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_TransformComponentsAtEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+9, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_TransformComponentsAtEpoch_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredSystemWithRate, vtable_offset_local+10, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredSystemWithRate.__dict__ and type(IAgCrdnConfiguredSystemWithRate.__dict__[attrname]) == property:
            return IAgCrdnConfiguredSystemWithRate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredSystemWithRate.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the System position and velocity, quaternion, and angular rate in reference components (in internal units) at the given time returned as an array representing x, y, z, vx, vy, vz, q1, q2, q3, q4, wx, wy, wz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the System position and velocity, quaternion, and angular rate in reference components (in internal units) at the interface's current time, returned as an array representing x, y, z, vx, vy, vz, q1, q2, q3, q4, wx, wy, wz."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponents_Array(self, dispInterface:"IDispatch", x:float, y:float, z:float, vx:float, vy:float, vz:float) -> list:
        """Transforms vector components given wrt System into those wrt RefSystem at the interface's current time, returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg(vx) as arg_vx, \
             agmarshall.DOUBLE_arg(vy) as arg_vy, \
             agmarshall.DOUBLE_arg(vz) as arg_vz, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponents_Array"](arg_dispInterface.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, arg_vx.COM_val, arg_vy.COM_val, arg_vz.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformComponentsAtEpoch_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float, x:float, y:float, z:float, vx:float, vy:float, vz:float) -> list:
        """Transforms vector components given wrt System into those wrt RefSystem at the given time, returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg(vx) as arg_vx, \
             agmarshall.DOUBLE_arg(vy) as arg_vy, \
             agmarshall.DOUBLE_arg(vz) as arg_vz, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_TransformComponentsAtEpoch_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, arg_vx.COM_val, arg_vy.COM_val, arg_vz.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{01D0AEC2-16CD-4bfd-B964-B420F66FBC35}", IAgCrdnConfiguredSystemWithRate)
agcls.AgTypeNameMap["IAgCrdnConfiguredSystemWithRate"] = IAgCrdnConfiguredSystemWithRate
__all__.append("IAgCrdnConfiguredSystemWithRate")

class IAgCrdnConfiguredCalcScalar(object):
    """Crdn Calc Scalar object interface."""
    _uuid = "{8129F3FC-A2C2-4671-B026-F4A36794CB9C}"
    _num_methods = 9
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetUnitAbbrv"] = _raise_uninitialized_error
        self.__dict__["_SetUnits"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredCalcScalar._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredCalcScalar from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredCalcScalar = agcom.GUID(IAgCrdnConfiguredCalcScalar._uuid)
        vtable_offset_local = IAgCrdnConfiguredCalcScalar._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+7, POINTER(agcom.BSTR))
        self.__dict__["_GetUnitAbbrv"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetUnits"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalar, vtable_offset_local+9, agcom.BSTR, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredCalcScalar.__dict__ and type(IAgCrdnConfiguredCalcScalar.__dict__[attrname]) == property:
            return IAgCrdnConfiguredCalcScalar.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredCalcScalar.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the Scalar value in internal units at the given time, returned as an array representing value, errFlag. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the Scalar value in internal units at the interface's current time, returned as an array representing value, errFlag. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def Dimension(self) -> str:
        """Name of the dimension of this calc scalar."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @property
    def UnitAbbrv(self) -> str:
        """Unit abbreviation for the current units used in the Evaluate and CurrentValue methods."""
        with agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetUnitAbbrv"](byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    def SetUnits(self, unitAbbrv:str) -> bool:
        """Sets the current units. Returns true for valid units, else returns false."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_SetUnits"](arg_unitAbbrv.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val


agcls.AgClassCatalog.add_catalog_entry("{8129F3FC-A2C2-4671-B026-F4A36794CB9C}", IAgCrdnConfiguredCalcScalar)
agcls.AgTypeNameMap["IAgCrdnConfiguredCalcScalar"] = IAgCrdnConfiguredCalcScalar
__all__.append("IAgCrdnConfiguredCalcScalar")

class IAgCrdnConfiguredCalcScalarWithRate(object):
    """Crdn Calc ScalarWithRate object interface."""
    _uuid = "{E8E2A828-56A7-4c0b-88E2-FF96268311BE}"
    _num_methods = 9
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetUnitAbbrv"] = _raise_uninitialized_error
        self.__dict__["_SetUnits"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredCalcScalarWithRate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredCalcScalarWithRate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredCalcScalarWithRate = agcom.GUID(IAgCrdnConfiguredCalcScalarWithRate._uuid)
        vtable_offset_local = IAgCrdnConfiguredCalcScalarWithRate._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+4, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+7, POINTER(agcom.BSTR))
        self.__dict__["_GetUnitAbbrv"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetUnits"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcScalarWithRate, vtable_offset_local+9, agcom.BSTR, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredCalcScalarWithRate.__dict__ and type(IAgCrdnConfiguredCalcScalarWithRate.__dict__[attrname]) == property:
            return IAgCrdnConfiguredCalcScalarWithRate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredCalcScalarWithRate.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the Scalar value and rate in internal units at the given time, returned as an array representing value, rate, errFlag. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the Scalar value and rate in internal units at the interface's current time, returned as an array representing value, rate, errFlag. Useful for scripting clients."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def Dimension(self) -> str:
        """Name of the dimension of this calc scalar."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @property
    def UnitAbbrv(self) -> str:
        """Unit abbreviation for the current units used in the Evaluate and CurrentValue methods."""
        with agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetUnitAbbrv"](byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    def SetUnits(self, unitAbbrv:str) -> bool:
        """Sets the current units. Returns true for valid units, else returns false. Rates are given in the current units per sec"""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_SetUnits"](arg_unitAbbrv.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val


agcls.AgClassCatalog.add_catalog_entry("{E8E2A828-56A7-4c0b-88E2-FF96268311BE}", IAgCrdnConfiguredCalcScalarWithRate)
agcls.AgTypeNameMap["IAgCrdnConfiguredCalcScalarWithRate"] = IAgCrdnConfiguredCalcScalarWithRate
__all__.append("IAgCrdnConfiguredCalcScalarWithRate")

class IAgCrdnConfiguredCalcParameterSet(object):
    """Crdn Calc ParameterSet object interface."""
    _uuid = "{F1B9B070-E89D-4b2b-BC10-A0976DA08F32}"
    _num_methods = 4
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredCalcParameterSet._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredCalcParameterSet from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredCalcParameterSet = agcom.GUID(IAgCrdnConfiguredCalcParameterSet._uuid)
        vtable_offset_local = IAgCrdnConfiguredCalcParameterSet._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSet, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSet, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSet, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSet, vtable_offset_local+4, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredCalcParameterSet.__dict__ and type(IAgCrdnConfiguredCalcParameterSet.__dict__[attrname]) == property:
            return IAgCrdnConfiguredCalcParameterSet.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredCalcParameterSet.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the set of parameters at the given time, returned as an array. The last element of the array is an error flag indicator."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the set of parameters at the interface's current time, returned as an array. The last element of the array is an error flag indicator."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{F1B9B070-E89D-4b2b-BC10-A0976DA08F32}", IAgCrdnConfiguredCalcParameterSet)
agcls.AgTypeNameMap["IAgCrdnConfiguredCalcParameterSet"] = IAgCrdnConfiguredCalcParameterSet
__all__.append("IAgCrdnConfiguredCalcParameterSet")

class IAgCrdnConfiguredCalcParameterSetWithRate(object):
    """Crdn Calc ParameterSetWithRate object interface."""
    _uuid = "{57516BE0-2EC5-4e0b-94DA-FFEE2906D418}"
    _num_methods = 4
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIsConfigured"] = _raise_uninitialized_error
        self.__dict__["_GetErrorText"] = _raise_uninitialized_error
        self.__dict__["_Evaluate_Array"] = _raise_uninitialized_error
        self.__dict__["_CurrentValue_Array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnConfiguredCalcParameterSetWithRate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnConfiguredCalcParameterSetWithRate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnConfiguredCalcParameterSetWithRate = agcom.GUID(IAgCrdnConfiguredCalcParameterSetWithRate._uuid)
        vtable_offset_local = IAgCrdnConfiguredCalcParameterSetWithRate._vtable_offset - 1
        self.__dict__["_GetIsConfigured"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSetWithRate, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetErrorText"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSetWithRate, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_Evaluate_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSetWithRate, vtable_offset_local+3, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_CurrentValue_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnConfiguredCalcParameterSetWithRate, vtable_offset_local+4, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnConfiguredCalcParameterSetWithRate.__dict__ and type(IAgCrdnConfiguredCalcParameterSetWithRate.__dict__[attrname]) == property:
            return IAgCrdnConfiguredCalcParameterSetWithRate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnConfiguredCalcParameterSetWithRate.")
    
    @property
    def IsConfigured(self) -> bool:
        """Flag indicating whether object is configured properly for use."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_GetIsConfigured"](byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    @property
    def ErrorText(self) -> str:
        """Text explaining configuration errors, if any"""
        with agmarshall.BSTR_arg() as arg_pErrorText:
            agcls.evaluate_hresult(self.__dict__["_GetErrorText"](byref(arg_pErrorText.COM_val)))
            return arg_pErrorText.python_val

    def Evaluate_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Computes the set of parameters and their rates at the given time, returned as an array. The last element of the array is an error flag indicator."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_Evaluate_Array"](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentValue_Array(self, dispInterface:"IDispatch") -> list:
        """Computes the set of parameters and their rates at the interface's current time, returned as an array. The last element of the array is an error flag indicator."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_CurrentValue_Array"](arg_dispInterface.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{57516BE0-2EC5-4e0b-94DA-FFEE2906D418}", IAgCrdnConfiguredCalcParameterSetWithRate)
agcls.AgTypeNameMap["IAgCrdnConfiguredCalcParameterSetWithRate"] = IAgCrdnConfiguredCalcParameterSetWithRate
__all__.append("IAgCrdnConfiguredCalcParameterSetWithRate")

class IAgCrdnPluginProvider(object):
    """Vector Tool plugin provider interface."""
    _uuid = "{F5373CD2-6AAF-48ab-B199-E170AD72D643}"
    _num_methods = 11
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetSourceNameDefault"] = _raise_uninitialized_error
        self.__dict__["_ConfigureVector"] = _raise_uninitialized_error
        self.__dict__["_ConfigureVectorWithRate"] = _raise_uninitialized_error
        self.__dict__["_ConfigureAxes"] = _raise_uninitialized_error
        self.__dict__["_ConfigureAxesWithRate"] = _raise_uninitialized_error
        self.__dict__["_ConfigureAngle"] = _raise_uninitialized_error
        self.__dict__["_ConfigureAngleWithRate"] = _raise_uninitialized_error
        self.__dict__["_ConfigurePoint"] = _raise_uninitialized_error
        self.__dict__["_ConfigurePointWithRate"] = _raise_uninitialized_error
        self.__dict__["_ConfigureSystem"] = _raise_uninitialized_error
        self.__dict__["_ConfigureSystemWithRate"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnPluginProvider._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnPluginProvider from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnPluginProvider = agcom.GUID(IAgCrdnPluginProvider._uuid)
        vtable_offset_local = IAgCrdnPluginProvider._vtable_offset - 1
        self.__dict__["_GetSourceNameDefault"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_ConfigureVector"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+2, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigureVectorWithRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+3, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigureAxes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+4, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigureAxesWithRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+5, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigureAngle"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+6, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigureAngleWithRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+7, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigurePoint"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+8, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigurePointWithRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+9, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigureSystem"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+10, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_ConfigureSystemWithRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginProvider, vtable_offset_local+11, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnPluginProvider.__dict__ and type(IAgCrdnPluginProvider.__dict__[attrname]) == property:
            return IAgCrdnPluginProvider.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnPluginProvider.")
    
    @property
    def SourceNameDefault(self) -> str:
        """Name of the instance path used by default for sourceName and refSourceName when creating IAgCrdn interfaces. Used when the input sourceName, refSourceName are input as null strings."""
        with agmarshall.BSTR_arg() as arg_pSourceNameDefault:
            agcls.evaluate_hresult(self.__dict__["_GetSourceNameDefault"](byref(arg_pSourceNameDefault.COM_val)))
            return arg_pSourceNameDefault.python_val

    def ConfigureVector(self, vectorName:str, sourceName:str, refAxesName:str, refAxesSourceName:str) -> "IAgCrdnConfiguredVector":
        """Creates an IAgCrdnConfiguredVector object from the given inputs."""
        with agmarshall.BSTR_arg(vectorName) as arg_vectorName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refAxesName) as arg_refAxesName, \
             agmarshall.BSTR_arg(refAxesSourceName) as arg_refAxesSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppVector:
            agcls.evaluate_hresult(self.__dict__["_ConfigureVector"](arg_vectorName.COM_val, arg_sourceName.COM_val, arg_refAxesName.COM_val, arg_refAxesSourceName.COM_val, byref(arg_ppVector.COM_val)))
            return arg_ppVector.python_val

    def ConfigureVectorWithRate(self, vectorName:str, sourceName:str, refAxesName:str, refAxesSourceName:str) -> "IAgCrdnConfiguredVectorWithRate":
        """Creates an IAgCrdnConfiguredVectorWithRate object from the given inputs."""
        with agmarshall.BSTR_arg(vectorName) as arg_vectorName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refAxesName) as arg_refAxesName, \
             agmarshall.BSTR_arg(refAxesSourceName) as arg_refAxesSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppVector:
            agcls.evaluate_hresult(self.__dict__["_ConfigureVectorWithRate"](arg_vectorName.COM_val, arg_sourceName.COM_val, arg_refAxesName.COM_val, arg_refAxesSourceName.COM_val, byref(arg_ppVector.COM_val)))
            return arg_ppVector.python_val

    def ConfigureAxes(self, axesName:str, sourceName:str, refAxesName:str, refAxesSourceName:str) -> "IAgCrdnConfiguredAxes":
        """Creates an IAgCrdnConfiguredAxes object from the given inputs."""
        with agmarshall.BSTR_arg(axesName) as arg_axesName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refAxesName) as arg_refAxesName, \
             agmarshall.BSTR_arg(refAxesSourceName) as arg_refAxesSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppAxes:
            agcls.evaluate_hresult(self.__dict__["_ConfigureAxes"](arg_axesName.COM_val, arg_sourceName.COM_val, arg_refAxesName.COM_val, arg_refAxesSourceName.COM_val, byref(arg_ppAxes.COM_val)))
            return arg_ppAxes.python_val

    def ConfigureAxesWithRate(self, axesName:str, sourceName:str, refAxesName:str, refAxesSourceName:str) -> "IAgCrdnConfiguredAxesWithRate":
        """Creates an IAgCrdnConfiguredAxesWithRate object from the given inputs."""
        with agmarshall.BSTR_arg(axesName) as arg_axesName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refAxesName) as arg_refAxesName, \
             agmarshall.BSTR_arg(refAxesSourceName) as arg_refAxesSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppAxes:
            agcls.evaluate_hresult(self.__dict__["_ConfigureAxesWithRate"](arg_axesName.COM_val, arg_sourceName.COM_val, arg_refAxesName.COM_val, arg_refAxesSourceName.COM_val, byref(arg_ppAxes.COM_val)))
            return arg_ppAxes.python_val

    def ConfigureAngle(self, angleName:str, sourceName:str) -> "IAgCrdnConfiguredAngle":
        """Creates an IAgCrdnConfiguredAngle object from the given inputs."""
        with agmarshall.BSTR_arg(angleName) as arg_angleName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppAngle:
            agcls.evaluate_hresult(self.__dict__["_ConfigureAngle"](arg_angleName.COM_val, arg_sourceName.COM_val, byref(arg_ppAngle.COM_val)))
            return arg_ppAngle.python_val

    def ConfigureAngleWithRate(self, angleName:str, sourceName:str) -> "IAgCrdnConfiguredAngleWithRate":
        """Creates an IAgCrdnConfiguredAngleWithRate object from the given inputs."""
        with agmarshall.BSTR_arg(angleName) as arg_angleName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppAngle:
            agcls.evaluate_hresult(self.__dict__["_ConfigureAngleWithRate"](arg_angleName.COM_val, arg_sourceName.COM_val, byref(arg_ppAngle.COM_val)))
            return arg_ppAngle.python_val

    def ConfigurePoint(self, pointName:str, sourceName:str, refSystemName:str, refSystemSourceName:str) -> "IAgCrdnConfiguredPoint":
        """Creates an IAgCrdnConfiguredPoint object from the given inputs."""
        with agmarshall.BSTR_arg(pointName) as arg_pointName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refSystemName) as arg_refSystemName, \
             agmarshall.BSTR_arg(refSystemSourceName) as arg_refSystemSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppPoint:
            agcls.evaluate_hresult(self.__dict__["_ConfigurePoint"](arg_pointName.COM_val, arg_sourceName.COM_val, arg_refSystemName.COM_val, arg_refSystemSourceName.COM_val, byref(arg_ppPoint.COM_val)))
            return arg_ppPoint.python_val

    def ConfigurePointWithRate(self, pointName:str, sourceName:str, refSystemName:str, refSystemSourceName:str) -> "IAgCrdnConfiguredPointWithRate":
        """Creates an IAgCrdnConfiguredPointWithRate object from the given inputs."""
        with agmarshall.BSTR_arg(pointName) as arg_pointName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refSystemName) as arg_refSystemName, \
             agmarshall.BSTR_arg(refSystemSourceName) as arg_refSystemSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppPoint:
            agcls.evaluate_hresult(self.__dict__["_ConfigurePointWithRate"](arg_pointName.COM_val, arg_sourceName.COM_val, arg_refSystemName.COM_val, arg_refSystemSourceName.COM_val, byref(arg_ppPoint.COM_val)))
            return arg_ppPoint.python_val

    def ConfigureSystem(self, systemName:str, sourceName:str, refSystemName:str, refSystemSourceName:str) -> "IAgCrdnConfiguredSystem":
        """Creates an IAgCrdnConfiguredSystem object from the given inputs."""
        with agmarshall.BSTR_arg(systemName) as arg_systemName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refSystemName) as arg_refSystemName, \
             agmarshall.BSTR_arg(refSystemSourceName) as arg_refSystemSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppSystem:
            agcls.evaluate_hresult(self.__dict__["_ConfigureSystem"](arg_systemName.COM_val, arg_sourceName.COM_val, arg_refSystemName.COM_val, arg_refSystemSourceName.COM_val, byref(arg_ppSystem.COM_val)))
            return arg_ppSystem.python_val

    def ConfigureSystemWithRate(self, systemName:str, sourceName:str, refSystemName:str, refSystemSourceName:str) -> "IAgCrdnConfiguredSystemWithRate":
        """Creates an IAgCrdnConfiguredSystemWithRate object from the given inputs."""
        with agmarshall.BSTR_arg(systemName) as arg_systemName, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.BSTR_arg(refSystemName) as arg_refSystemName, \
             agmarshall.BSTR_arg(refSystemSourceName) as arg_refSystemSourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppSystem:
            agcls.evaluate_hresult(self.__dict__["_ConfigureSystemWithRate"](arg_systemName.COM_val, arg_sourceName.COM_val, arg_refSystemName.COM_val, arg_refSystemSourceName.COM_val, byref(arg_ppSystem.COM_val)))
            return arg_ppSystem.python_val


agcls.AgClassCatalog.add_catalog_entry("{F5373CD2-6AAF-48ab-B199-E170AD72D643}", IAgCrdnPluginProvider)
agcls.AgTypeNameMap["IAgCrdnPluginProvider"] = IAgCrdnPluginProvider
__all__.append("IAgCrdnPluginProvider")

class IAgCrdnPluginCalcProvider(object):
    """Vector Tool plugin provider interface."""
    _uuid = "{A429EFEE-1973-4c8d-B35C-7BC629A2A75A}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetSourceNameDefault"] = _raise_uninitialized_error
        self.__dict__["_GetCalcScalar"] = _raise_uninitialized_error
        self.__dict__["_GetCalcScalarWithRate"] = _raise_uninitialized_error
        self.__dict__["_GetCalcParameterSet"] = _raise_uninitialized_error
        self.__dict__["_GetCalcParameterSetWithRate"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnPluginCalcProvider._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnPluginCalcProvider from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnPluginCalcProvider = agcom.GUID(IAgCrdnPluginCalcProvider._uuid)
        vtable_offset_local = IAgCrdnPluginCalcProvider._vtable_offset - 1
        self.__dict__["_GetSourceNameDefault"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginCalcProvider, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetCalcScalar"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginCalcProvider, vtable_offset_local+2, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcScalarWithRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginCalcProvider, vtable_offset_local+3, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcParameterSet"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginCalcProvider, vtable_offset_local+4, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcParameterSetWithRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPluginCalcProvider, vtable_offset_local+5, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnPluginCalcProvider.__dict__ and type(IAgCrdnPluginCalcProvider.__dict__[attrname]) == property:
            return IAgCrdnPluginCalcProvider.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnPluginCalcProvider.")
    
    @property
    def SourceNameDefault(self) -> str:
        """Name of the instance path used by default for sourceName and refSourceName when creating IAgCrdn interfaces. Used when the input sourceName, refSourceName are input as null strings."""
        with agmarshall.BSTR_arg() as arg_pSourceNameDefault:
            agcls.evaluate_hresult(self.__dict__["_GetSourceNameDefault"](byref(arg_pSourceNameDefault.COM_val)))
            return arg_pSourceNameDefault.python_val

    def GetCalcScalar(self, name:str, sourceName:str) -> "IAgCrdnConfiguredCalcScalar":
        """Creates an IAgCrdnConfiguredCalcScalar handle to the named Calc Scalar."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppCalcScalar:
            agcls.evaluate_hresult(self.__dict__["_GetCalcScalar"](arg_name.COM_val, arg_sourceName.COM_val, byref(arg_ppCalcScalar.COM_val)))
            return arg_ppCalcScalar.python_val

    def GetCalcScalarWithRate(self, name:str, sourceName:str) -> "IAgCrdnConfiguredCalcScalarWithRate":
        """Creates an IAgCrdnConfiguredCalcScalarWithRate handle to the named Calc Scalar."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppCalcScalarWithRate:
            agcls.evaluate_hresult(self.__dict__["_GetCalcScalarWithRate"](arg_name.COM_val, arg_sourceName.COM_val, byref(arg_ppCalcScalarWithRate.COM_val)))
            return arg_ppCalcScalarWithRate.python_val

    def GetCalcParameterSet(self, name:str, sourceName:str) -> "IAgCrdnConfiguredCalcParameterSet":
        """Creates an IAgCrdnConfiguredCalcParameterSet handle to the named Calc ParameterSet."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppCalcParameterSet:
            agcls.evaluate_hresult(self.__dict__["_GetCalcParameterSet"](arg_name.COM_val, arg_sourceName.COM_val, byref(arg_ppCalcParameterSet.COM_val)))
            return arg_ppCalcParameterSet.python_val

    def GetCalcParameterSetWithRate(self, name:str, sourceName:str) -> "IAgCrdnConfiguredCalcParameterSetWithRate":
        """Creates an IAgCrdnConfiguredCalcParameterSetWithRate handle to the named Calc ParameterSet."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(sourceName) as arg_sourceName, \
             agmarshall.AgInterface_out_arg() as arg_ppCalcParameterSetWithRate:
            agcls.evaluate_hresult(self.__dict__["_GetCalcParameterSetWithRate"](arg_name.COM_val, arg_sourceName.COM_val, byref(arg_ppCalcParameterSetWithRate.COM_val)))
            return arg_ppCalcParameterSetWithRate.python_val


agcls.AgClassCatalog.add_catalog_entry("{A429EFEE-1973-4c8d-B35C-7BC629A2A75A}", IAgCrdnPluginCalcProvider)
agcls.AgTypeNameMap["IAgCrdnPluginCalcProvider"] = IAgCrdnPluginCalcProvider
__all__.append("IAgCrdnPluginCalcProvider")

class IAgCrdnVectorPluginResultReg(object):
    """COM Plugin Result interface for the Register method of IAgCrdnVectorPlugin."""
    _uuid = "{23D36CFE-E264-45d2-BB9C-21121E38BC56}"
    _num_methods = 13
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetDimension"] = _raise_uninitialized_error
        self.__dict__["_SetRefAxes"] = _raise_uninitialized_error
        self.__dict__["_ClearAvailability"] = _raise_uninitialized_error
        self.__dict__["_AddAvailabilityInterval"] = _raise_uninitialized_error
        self.__dict__["_ClearSpecialTimes"] = _raise_uninitialized_error
        self.__dict__["_AddSpecialTime"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnVectorPluginResultReg._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnVectorPluginResultReg from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnVectorPluginResultReg = agcom.GUID(IAgCrdnVectorPluginResultReg._uuid)
        vtable_offset_local = IAgCrdnVectorPluginResultReg._vtable_offset - 1
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+5, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_SetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+8, agcom.BSTR)
        self.__dict__["_SetRefAxes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+9, agcom.BSTR, agcom.BSTR)
        self.__dict__["_ClearAvailability"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+10, )
        self.__dict__["_AddAvailabilityInterval"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+11, agcom.BSTR, agcom.BSTR, agcom.BSTR)
        self.__dict__["_ClearSpecialTimes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+12, )
        self.__dict__["_AddSpecialTime"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReg, vtable_offset_local+13, agcom.BSTR, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnVectorPluginResultReg.__dict__ and type(IAgCrdnVectorPluginResultReg.__dict__[attrname]) == property:
            return IAgCrdnVectorPluginResultReg.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnVectorPluginResultReg.")
    
    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    @property
    def Dimension(self) -> None:
        """Dimension is a write-only property."""
        raise RuntimeError("Dimension is a write-only property.")


    @Dimension.setter
    def Dimension(self, dimension:str) -> None:
        """Sets the dimension of the vector."""
        with agmarshall.BSTR_arg(dimension) as arg_dimension:
            agcls.evaluate_hresult(self.__dict__["_SetDimension"](arg_dimension.COM_val))

    def SetRefAxes(self, name:str, sourcePath:str) -> None:
        """Sets the reference axes of the vector."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(sourcePath) as arg_sourcePath:
            agcls.evaluate_hresult(self.__dict__["_SetRefAxes"](arg_name.COM_val, arg_sourcePath.COM_val))

    def ClearAvailability(self) -> None:
        """Clears any availability intervals that may have been set. Vector is considered available at all times."""
        agcls.evaluate_hresult(self.__dict__["_ClearAvailability"]())

    def AddAvailabilityInterval(self, dateAbbrv:str, startDate:str, stopDate:str) -> None:
        """Adds an availability interval. The Vector is available at a given time only if the time is within one of the vector's availability intervals."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(startDate) as arg_startDate, \
             agmarshall.BSTR_arg(stopDate) as arg_stopDate:
            agcls.evaluate_hresult(self.__dict__["_AddAvailabilityInterval"](arg_dateAbbrv.COM_val, arg_startDate.COM_val, arg_stopDate.COM_val))

    def ClearSpecialTimes(self) -> None:
        """Clears any special times that may have been set."""
        agcls.evaluate_hresult(self.__dict__["_ClearSpecialTimes"]())

    def AddSpecialTime(self, dateAbbrv:str, specialTime:str) -> None:
        """Adds a special time that will be incorporated during sampling of the vector's value."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(specialTime) as arg_specialTime:
            agcls.evaluate_hresult(self.__dict__["_AddSpecialTime"](arg_dateAbbrv.COM_val, arg_specialTime.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{23D36CFE-E264-45d2-BB9C-21121E38BC56}", IAgCrdnVectorPluginResultReg)
agcls.AgTypeNameMap["IAgCrdnVectorPluginResultReg"] = IAgCrdnVectorPluginResultReg
__all__.append("IAgCrdnVectorPluginResultReg")

class IAgCrdnVectorPluginResultReset(object):
    """COM Plugin Result interface for the Reset method of IAgCrdnVectorPlugin."""
    _uuid = "{BC419354-9340-4609-BD80-5799AD1868AA}"
    _num_methods = 14
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnVectorPluginResultReset._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnVectorPluginResultReset from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnVectorPluginResultReset = agcom.GUID(IAgCrdnVectorPluginResultReset._uuid)
        vtable_offset_local = IAgCrdnVectorPluginResultReset._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+10, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultReset, vtable_offset_local+14, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnVectorPluginResultReset.__dict__ and type(IAgCrdnVectorPluginResultReset.__dict__[attrname]) == property:
            return IAgCrdnVectorPluginResultReset.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnVectorPluginResultReset.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry("{BC419354-9340-4609-BD80-5799AD1868AA}", IAgCrdnVectorPluginResultReset)
agcls.AgTypeNameMap["IAgCrdnVectorPluginResultReset"] = IAgCrdnVectorPluginResultReset
__all__.append("IAgCrdnVectorPluginResultReset")

class IAgCrdnVectorPluginResultEval(object):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnVectorPlugin."""
    _uuid = "{2F83CE49-DE6E-4997-9D33-1A627D35ACD9}"
    _num_methods = 16
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetVectorComponents"] = _raise_uninitialized_error
        self.__dict__["_SetVectorRateComponents"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnVectorPluginResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnVectorPluginResultEval from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnVectorPluginResultEval = agcom.GUID(IAgCrdnVectorPluginResultEval._uuid)
        vtable_offset_local = IAgCrdnVectorPluginResultEval._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_SetVectorComponents"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+10, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_SetVectorRateComponents"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+11, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+14, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnVectorPluginResultEval, vtable_offset_local+16, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnVectorPluginResultEval.__dict__ and type(IAgCrdnVectorPluginResultEval.__dict__[attrname]) == property:
            return IAgCrdnVectorPluginResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnVectorPluginResultEval.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def SetVectorComponents(self, x:float, y:float, z:float) -> None:
        """Set the vector components in internal units."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetVectorComponents"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def SetVectorRateComponents(self, x:float, y:float, z:float) -> None:
        """Set the vector rate components in internal units."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetVectorRateComponents"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry("{2F83CE49-DE6E-4997-9D33-1A627D35ACD9}", IAgCrdnVectorPluginResultEval)
agcls.AgTypeNameMap["IAgCrdnVectorPluginResultEval"] = IAgCrdnVectorPluginResultEval
__all__.append("IAgCrdnVectorPluginResultEval")

class IAgCrdnPointPluginResultReg(object):
    """COM Plugin Result interface for the Register method of IAgCrdnPointPlugin."""
    _uuid = "{293955B9-7601-4791-98C4-1FE0CC7B1D2C}"
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetRefSystem"] = _raise_uninitialized_error
        self.__dict__["_ClearAvailability"] = _raise_uninitialized_error
        self.__dict__["_AddAvailabilityInterval"] = _raise_uninitialized_error
        self.__dict__["_ClearSpecialTimes"] = _raise_uninitialized_error
        self.__dict__["_AddSpecialTime"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnPointPluginResultReg._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnPointPluginResultReg from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnPointPluginResultReg = agcom.GUID(IAgCrdnPointPluginResultReg._uuid)
        vtable_offset_local = IAgCrdnPointPluginResultReg._vtable_offset - 1
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+5, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_SetRefSystem"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+8, agcom.BSTR, agcom.BSTR)
        self.__dict__["_ClearAvailability"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+9, )
        self.__dict__["_AddAvailabilityInterval"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+10, agcom.BSTR, agcom.BSTR, agcom.BSTR)
        self.__dict__["_ClearSpecialTimes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+11, )
        self.__dict__["_AddSpecialTime"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReg, vtable_offset_local+12, agcom.BSTR, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnPointPluginResultReg.__dict__ and type(IAgCrdnPointPluginResultReg.__dict__[attrname]) == property:
            return IAgCrdnPointPluginResultReg.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnPointPluginResultReg.")
    
    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def SetRefSystem(self, name:str, sourcePath:str) -> None:
        """Sets the reference system for the point."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(sourcePath) as arg_sourcePath:
            agcls.evaluate_hresult(self.__dict__["_SetRefSystem"](arg_name.COM_val, arg_sourcePath.COM_val))

    def ClearAvailability(self) -> None:
        """Clears any availability intervals that may have been set. Point is considered available at all times."""
        agcls.evaluate_hresult(self.__dict__["_ClearAvailability"]())

    def AddAvailabilityInterval(self, dateAbbrv:str, startDate:str, stopDate:str) -> None:
        """Adds an availability interval. The Point is available at a given time only if the time is within one of the point's availability intervals."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(startDate) as arg_startDate, \
             agmarshall.BSTR_arg(stopDate) as arg_stopDate:
            agcls.evaluate_hresult(self.__dict__["_AddAvailabilityInterval"](arg_dateAbbrv.COM_val, arg_startDate.COM_val, arg_stopDate.COM_val))

    def ClearSpecialTimes(self) -> None:
        """Clears any special times that may have been set."""
        agcls.evaluate_hresult(self.__dict__["_ClearSpecialTimes"]())

    def AddSpecialTime(self, dateAbbrv:str, specialTime:str) -> None:
        """Adds a special time that will be incorporated during sampling of the point's location."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(specialTime) as arg_specialTime:
            agcls.evaluate_hresult(self.__dict__["_AddSpecialTime"](arg_dateAbbrv.COM_val, arg_specialTime.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{293955B9-7601-4791-98C4-1FE0CC7B1D2C}", IAgCrdnPointPluginResultReg)
agcls.AgTypeNameMap["IAgCrdnPointPluginResultReg"] = IAgCrdnPointPluginResultReg
__all__.append("IAgCrdnPointPluginResultReg")

class IAgCrdnPointPluginResultReset(object):
    """COM Plugin Result interface for the Reset method of IAgCrdnPointPlugin."""
    _uuid = "{13D01153-A788-46c3-8045-BC38F8C8D385}"
    _num_methods = 14
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnPointPluginResultReset._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnPointPluginResultReset from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnPointPluginResultReset = agcom.GUID(IAgCrdnPointPluginResultReset._uuid)
        vtable_offset_local = IAgCrdnPointPluginResultReset._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+10, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultReset, vtable_offset_local+14, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnPointPluginResultReset.__dict__ and type(IAgCrdnPointPluginResultReset.__dict__[attrname]) == property:
            return IAgCrdnPointPluginResultReset.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnPointPluginResultReset.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry("{13D01153-A788-46c3-8045-BC38F8C8D385}", IAgCrdnPointPluginResultReset)
agcls.AgTypeNameMap["IAgCrdnPointPluginResultReset"] = IAgCrdnPointPluginResultReset
__all__.append("IAgCrdnPointPluginResultReset")

class IAgCrdnPointPluginResultEval(object):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnPointPlugin."""
    _uuid = "{B4FA32EA-53DD-4a97-A497-C2D97A631933}"
    _num_methods = 16
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetPosition"] = _raise_uninitialized_error
        self.__dict__["_SetVelocity"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnPointPluginResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnPointPluginResultEval from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnPointPluginResultEval = agcom.GUID(IAgCrdnPointPluginResultEval._uuid)
        vtable_offset_local = IAgCrdnPointPluginResultEval._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_SetPosition"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+10, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_SetVelocity"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+11, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+14, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnPointPluginResultEval, vtable_offset_local+16, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnPointPluginResultEval.__dict__ and type(IAgCrdnPointPluginResultEval.__dict__[attrname]) == property:
            return IAgCrdnPointPluginResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnPointPluginResultEval.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def SetPosition(self, x:float, y:float, z:float) -> None:
        """Set the position components in meters."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetPosition"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def SetVelocity(self, x:float, y:float, z:float) -> None:
        """Set the velocity components in meters/sec."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetVelocity"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry("{B4FA32EA-53DD-4a97-A497-C2D97A631933}", IAgCrdnPointPluginResultEval)
agcls.AgTypeNameMap["IAgCrdnPointPluginResultEval"] = IAgCrdnPointPluginResultEval
__all__.append("IAgCrdnPointPluginResultEval")

class IAgCrdnAxesPluginResultReg(object):
    """COM Plugin Result interface for the Register method of IAgCrdnAxesPlugin."""
    _uuid = "{DBFDD0C5-0F8B-4e2e-BAA0-38BB6CA4CD69}"
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetRefAxes"] = _raise_uninitialized_error
        self.__dict__["_ClearAvailability"] = _raise_uninitialized_error
        self.__dict__["_AddAvailabilityInterval"] = _raise_uninitialized_error
        self.__dict__["_ClearSpecialTimes"] = _raise_uninitialized_error
        self.__dict__["_AddSpecialTime"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnAxesPluginResultReg._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnAxesPluginResultReg from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnAxesPluginResultReg = agcom.GUID(IAgCrdnAxesPluginResultReg._uuid)
        vtable_offset_local = IAgCrdnAxesPluginResultReg._vtable_offset - 1
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+5, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_SetRefAxes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+8, agcom.BSTR, agcom.BSTR)
        self.__dict__["_ClearAvailability"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+9, )
        self.__dict__["_AddAvailabilityInterval"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+10, agcom.BSTR, agcom.BSTR, agcom.BSTR)
        self.__dict__["_ClearSpecialTimes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+11, )
        self.__dict__["_AddSpecialTime"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReg, vtable_offset_local+12, agcom.BSTR, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnAxesPluginResultReg.__dict__ and type(IAgCrdnAxesPluginResultReg.__dict__[attrname]) == property:
            return IAgCrdnAxesPluginResultReg.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnAxesPluginResultReg.")
    
    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def SetRefAxes(self, name:str, sourcePath:str) -> None:
        """Sets the reference axes of the vector."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(sourcePath) as arg_sourcePath:
            agcls.evaluate_hresult(self.__dict__["_SetRefAxes"](arg_name.COM_val, arg_sourcePath.COM_val))

    def ClearAvailability(self) -> None:
        """Clears any availability intervals that may have been set. Axes is considered available at all times."""
        agcls.evaluate_hresult(self.__dict__["_ClearAvailability"]())

    def AddAvailabilityInterval(self, dateAbbrv:str, startDate:str, stopDate:str) -> None:
        """Adds an availability interval. The Axes is available at a given time only if the time is within one of the vector's availability intervals."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(startDate) as arg_startDate, \
             agmarshall.BSTR_arg(stopDate) as arg_stopDate:
            agcls.evaluate_hresult(self.__dict__["_AddAvailabilityInterval"](arg_dateAbbrv.COM_val, arg_startDate.COM_val, arg_stopDate.COM_val))

    def ClearSpecialTimes(self) -> None:
        """Clears any special times that may have been set."""
        agcls.evaluate_hresult(self.__dict__["_ClearSpecialTimes"]())

    def AddSpecialTime(self, dateAbbrv:str, specialTime:str) -> None:
        """Adds a special time that will be incorporated during sampling of the vector's value."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(specialTime) as arg_specialTime:
            agcls.evaluate_hresult(self.__dict__["_AddSpecialTime"](arg_dateAbbrv.COM_val, arg_specialTime.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{DBFDD0C5-0F8B-4e2e-BAA0-38BB6CA4CD69}", IAgCrdnAxesPluginResultReg)
agcls.AgTypeNameMap["IAgCrdnAxesPluginResultReg"] = IAgCrdnAxesPluginResultReg
__all__.append("IAgCrdnAxesPluginResultReg")

class IAgCrdnAxesPluginResultReset(object):
    """COM Plugin Result interface for the Reset method of IAgCrdnAxesPlugin."""
    _uuid = "{8544B432-172C-420a-B0D0-0BD7958A67A1}"
    _num_methods = 14
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnAxesPluginResultReset._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnAxesPluginResultReset from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnAxesPluginResultReset = agcom.GUID(IAgCrdnAxesPluginResultReset._uuid)
        vtable_offset_local = IAgCrdnAxesPluginResultReset._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+10, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultReset, vtable_offset_local+14, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnAxesPluginResultReset.__dict__ and type(IAgCrdnAxesPluginResultReset.__dict__[attrname]) == property:
            return IAgCrdnAxesPluginResultReset.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnAxesPluginResultReset.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry("{8544B432-172C-420a-B0D0-0BD7958A67A1}", IAgCrdnAxesPluginResultReset)
agcls.AgTypeNameMap["IAgCrdnAxesPluginResultReset"] = IAgCrdnAxesPluginResultReset
__all__.append("IAgCrdnAxesPluginResultReset")

class IAgCrdnAxesPluginResultEval(object):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnAxesPlugin."""
    _uuid = "{E4707CDD-E425-40e1-AF3D-D6C22B36B71B}"
    _num_methods = 19
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        self.__dict__["_SetQuaternion"] = _raise_uninitialized_error
        self.__dict__["_EulerRotate"] = _raise_uninitialized_error
        self.__dict__["_SetDCM"] = _raise_uninitialized_error
        self.__dict__["_SetAngularVelocity"] = _raise_uninitialized_error
        self.__dict__["_SetAngularVelocityUsingRefAxes"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnAxesPluginResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnAxesPluginResultEval from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnAxesPluginResultEval = agcom.GUID(IAgCrdnAxesPluginResultEval._uuid)
        vtable_offset_local = IAgCrdnAxesPluginResultEval._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+10, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+14, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_SetQuaternion"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+15, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_EulerRotate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+16, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_SetDCM"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+17, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_SetAngularVelocity"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+18, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_SetAngularVelocityUsingRefAxes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnAxesPluginResultEval, vtable_offset_local+19, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnAxesPluginResultEval.__dict__ and type(IAgCrdnAxesPluginResultEval.__dict__[attrname]) == property:
            return IAgCrdnAxesPluginResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnAxesPluginResultEval.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val

    def SetQuaternion(self, q1:float, q2:float, q3:float, q4:float) -> None:
        """Set the orientation using a quaternion representing the rotation to these axes from the references axes. (q1,q2,q3) is the vector part; q4 is the scalar part."""
        with agmarshall.DOUBLE_arg(q1) as arg_q1, \
             agmarshall.DOUBLE_arg(q2) as arg_q2, \
             agmarshall.DOUBLE_arg(q3) as arg_q3, \
             agmarshall.DOUBLE_arg(q4) as arg_q4:
            agcls.evaluate_hresult(self.__dict__["_SetQuaternion"](arg_q1.COM_val, arg_q2.COM_val, arg_q3.COM_val, arg_q4.COM_val))

    def EulerRotate(self, sequence:"AgECrdnEulerSequence", first:float, second:float, third:float) -> None:
        """Sets the orientation using a sequence of euler rotations."""
        with agmarshall.AgEnum_arg(AgECrdnEulerSequence, sequence) as arg_sequence, \
             agmarshall.DOUBLE_arg(first) as arg_first, \
             agmarshall.DOUBLE_arg(second) as arg_second, \
             agmarshall.DOUBLE_arg(third) as arg_third:
            agcls.evaluate_hresult(self.__dict__["_EulerRotate"](arg_sequence.COM_val, arg_first.COM_val, arg_second.COM_val, arg_third.COM_val))

    def SetDCM(self, xx:float, xy:float, xz:float, yx:float, yy:float, yz:float, zx:float, zy:float, zz:float) -> None:
        """Sets the orientation using a direction cosine matrix representing the rotation to these axes from the references axes."""
        with agmarshall.DOUBLE_arg(xx) as arg_xx, \
             agmarshall.DOUBLE_arg(xy) as arg_xy, \
             agmarshall.DOUBLE_arg(xz) as arg_xz, \
             agmarshall.DOUBLE_arg(yx) as arg_yx, \
             agmarshall.DOUBLE_arg(yy) as arg_yy, \
             agmarshall.DOUBLE_arg(yz) as arg_yz, \
             agmarshall.DOUBLE_arg(zx) as arg_zx, \
             agmarshall.DOUBLE_arg(zy) as arg_zy, \
             agmarshall.DOUBLE_arg(zz) as arg_zz:
            agcls.evaluate_hresult(self.__dict__["_SetDCM"](arg_xx.COM_val, arg_xy.COM_val, arg_xz.COM_val, arg_yx.COM_val, arg_yy.COM_val, arg_yz.COM_val, arg_zx.COM_val, arg_zy.COM_val, arg_zz.COM_val))

    def SetAngularVelocity(self, wx:float, wy:float, wz:float) -> None:
        """Set the angular velocity in rad/sec. The components are to be specified with respect to this Axes object."""
        with agmarshall.DOUBLE_arg(wx) as arg_wx, \
             agmarshall.DOUBLE_arg(wy) as arg_wy, \
             agmarshall.DOUBLE_arg(wz) as arg_wz:
            agcls.evaluate_hresult(self.__dict__["_SetAngularVelocity"](arg_wx.COM_val, arg_wy.COM_val, arg_wz.COM_val))

    def SetAngularVelocityUsingRefAxes(self, wx:float, wy:float, wz:float) -> None:
        """Set the angular velocity in rad/sec. The components are to be specified with respect to the RefAxes."""
        with agmarshall.DOUBLE_arg(wx) as arg_wx, \
             agmarshall.DOUBLE_arg(wy) as arg_wy, \
             agmarshall.DOUBLE_arg(wz) as arg_wz:
            agcls.evaluate_hresult(self.__dict__["_SetAngularVelocityUsingRefAxes"](arg_wx.COM_val, arg_wy.COM_val, arg_wz.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{E4707CDD-E425-40e1-AF3D-D6C22B36B71B}", IAgCrdnAxesPluginResultEval)
agcls.AgTypeNameMap["IAgCrdnAxesPluginResultEval"] = IAgCrdnAxesPluginResultEval
__all__.append("IAgCrdnAxesPluginResultEval")

class IAgCrdnCalcScalarPluginResultReg(object):
    """COM Plugin Result interface for the Register method of IAgCrdnCalcScalarPlugin."""
    _uuid = "{8B84D52C-D688-4e44-98F2-A28D40E1C3DB}"
    _num_methods = 15
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_ClearAvailability"] = _raise_uninitialized_error
        self.__dict__["_AddAvailabilityInterval"] = _raise_uninitialized_error
        self.__dict__["_ClearSpecialTimes"] = _raise_uninitialized_error
        self.__dict__["_AddSpecialTime"] = _raise_uninitialized_error
        self.__dict__["_SetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetUnitAbbrv"] = _raise_uninitialized_error
        self.__dict__["_SetUnits"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnCalcScalarPluginResultReg._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnCalcScalarPluginResultReg from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnCalcScalarPluginResultReg = agcom.GUID(IAgCrdnCalcScalarPluginResultReg._uuid)
        vtable_offset_local = IAgCrdnCalcScalarPluginResultReg._vtable_offset - 1
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+5, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_ClearAvailability"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+8, )
        self.__dict__["_AddAvailabilityInterval"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+9, agcom.BSTR, agcom.BSTR, agcom.BSTR)
        self.__dict__["_ClearSpecialTimes"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+10, )
        self.__dict__["_AddSpecialTime"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+11, agcom.BSTR, agcom.BSTR)
        self.__dict__["_SetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+12, agcom.BSTR)
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+13, POINTER(agcom.BSTR))
        self.__dict__["_GetUnitAbbrv"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+14, POINTER(agcom.BSTR))
        self.__dict__["_SetUnits"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReg, vtable_offset_local+15, agcom.BSTR, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnCalcScalarPluginResultReg.__dict__ and type(IAgCrdnCalcScalarPluginResultReg.__dict__[attrname]) == property:
            return IAgCrdnCalcScalarPluginResultReg.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnCalcScalarPluginResultReg.")
    
    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Not supported by central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def ClearAvailability(self) -> None:
        """Clears any availability intervals that may have been set. Point is considered available at all times."""
        agcls.evaluate_hresult(self.__dict__["_ClearAvailability"]())

    def AddAvailabilityInterval(self, dateAbbrv:str, startDate:str, stopDate:str) -> None:
        """Adds an availability interval. The Point is available at a given time only if the time is within one of the point's availability intervals."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(startDate) as arg_startDate, \
             agmarshall.BSTR_arg(stopDate) as arg_stopDate:
            agcls.evaluate_hresult(self.__dict__["_AddAvailabilityInterval"](arg_dateAbbrv.COM_val, arg_startDate.COM_val, arg_stopDate.COM_val))

    def ClearSpecialTimes(self) -> None:
        """Clears any special times that may have been set."""
        agcls.evaluate_hresult(self.__dict__["_ClearSpecialTimes"]())

    def AddSpecialTime(self, dateAbbrv:str, specialTime:str) -> None:
        """Adds a special time that will be incorporated during sampling of the point's location."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(specialTime) as arg_specialTime:
            agcls.evaluate_hresult(self.__dict__["_AddSpecialTime"](arg_dateAbbrv.COM_val, arg_specialTime.COM_val))

    @property
    def Dimension(self) -> str:
        """Name of the dimension."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @Dimension.setter
    def Dimension(self, dimension:str) -> None:
        """Name of the dimension."""
        with agmarshall.BSTR_arg(dimension) as arg_dimension:
            agcls.evaluate_hresult(self.__dict__["_SetDimension"](arg_dimension.COM_val))

    @property
    def UnitAbbrv(self) -> str:
        """Unit abbreviation for the current units."""
        with agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetUnitAbbrv"](byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    def SetUnits(self, unitAbbrv:str) -> bool:
        """Sets the current units."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_SetUnits"](arg_unitAbbrv.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val


agcls.AgClassCatalog.add_catalog_entry("{8B84D52C-D688-4e44-98F2-A28D40E1C3DB}", IAgCrdnCalcScalarPluginResultReg)
agcls.AgTypeNameMap["IAgCrdnCalcScalarPluginResultReg"] = IAgCrdnCalcScalarPluginResultReg
__all__.append("IAgCrdnCalcScalarPluginResultReg")

class IAgCrdnCalcScalarPluginResultReset(object):
    """COM Plugin Result interface for the Reset method of IAgCrdnCalcScalarPlugin."""
    _uuid = "{D3934CCB-73BC-45a1-94FE-DA0C0D7701C8}"
    _num_methods = 17
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetUnitAbbrv"] = _raise_uninitialized_error
        self.__dict__["_SetUnits"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnCalcScalarPluginResultReset._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnCalcScalarPluginResultReset from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnCalcScalarPluginResultReset = agcom.GUID(IAgCrdnCalcScalarPluginResultReset._uuid)
        vtable_offset_local = IAgCrdnCalcScalarPluginResultReset._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+10, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+14, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+15, POINTER(agcom.BSTR))
        self.__dict__["_GetUnitAbbrv"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+16, POINTER(agcom.BSTR))
        self.__dict__["_SetUnits"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultReset, vtable_offset_local+17, agcom.BSTR, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnCalcScalarPluginResultReset.__dict__ and type(IAgCrdnCalcScalarPluginResultReset.__dict__[attrname]) == property:
            return IAgCrdnCalcScalarPluginResultReset.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnCalcScalarPluginResultReset.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val

    @property
    def Dimension(self) -> str:
        """Name of the dimension."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @property
    def UnitAbbrv(self) -> str:
        """Unit abbreviation for the current units."""
        with agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetUnitAbbrv"](byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    def SetUnits(self, unitAbbrv:str) -> bool:
        """Sets the current units."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_SetUnits"](arg_unitAbbrv.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val


agcls.AgClassCatalog.add_catalog_entry("{D3934CCB-73BC-45a1-94FE-DA0C0D7701C8}", IAgCrdnCalcScalarPluginResultReset)
agcls.AgTypeNameMap["IAgCrdnCalcScalarPluginResultReset"] = IAgCrdnCalcScalarPluginResultReset
__all__.append("IAgCrdnCalcScalarPluginResultReset")

class IAgCrdnCalcScalarPluginResultEval(object):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnCalcScalarPlugin."""
    _uuid = "{824518FA-47BD-4cb3-A0DB-CE2BCB269137}"
    _num_methods = 19
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVectorToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetCalcToolProvider"] = _raise_uninitialized_error
        self.__dict__["_GetObjectPath"] = _raise_uninitialized_error
        self.__dict__["_GetParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetGrandParentPath"] = _raise_uninitialized_error
        self.__dict__["_GetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_SetShortDescription"] = _raise_uninitialized_error
        self.__dict__["_GetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_SetLongDescription"] = _raise_uninitialized_error
        self.__dict__["_DayCount"] = _raise_uninitialized_error
        self.__dict__["_DayCount_Array"] = _raise_uninitialized_error
        self.__dict__["_DateElements"] = _raise_uninitialized_error
        self.__dict__["_DateElements_Array"] = _raise_uninitialized_error
        self.__dict__["_DateString"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetUnitAbbrv"] = _raise_uninitialized_error
        self.__dict__["_SetUnits"] = _raise_uninitialized_error
        self.__dict__["_SetValue"] = _raise_uninitialized_error
        self.__dict__["_SetValueAndRate"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCrdnCalcScalarPluginResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCrdnCalcScalarPluginResultEval from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCrdnCalcScalarPluginResultEval = agcom.GUID(IAgCrdnCalcScalarPluginResultEval._uuid)
        vtable_offset_local = IAgCrdnCalcScalarPluginResultEval._vtable_offset - 1
        self.__dict__["_GetVectorToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetCalcToolProvider"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetObjectPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_GetParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetGrandParentPath"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetShortDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_GetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetLongDescription"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_DayCount"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+10, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DayCount_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateElements"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__["_DateElements_Array"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_DateString"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+14, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+15, POINTER(agcom.BSTR))
        self.__dict__["_GetUnitAbbrv"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+16, POINTER(agcom.BSTR))
        self.__dict__["_SetUnits"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+17, agcom.BSTR, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetValue"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+18, agcom.DOUBLE)
        self.__dict__["_SetValueAndRate"] = IAGFUNCTYPE(pUnk, IID_IAgCrdnCalcScalarPluginResultEval, vtable_offset_local+19, agcom.DOUBLE, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCrdnCalcScalarPluginResultEval.__dict__ and type(IAgCrdnCalcScalarPluginResultEval.__dict__[attrname]) == property:
            return IAgCrdnCalcScalarPluginResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCrdnCalcScalarPluginResultEval.")
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetVectorToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginCalcProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__["_GetCalcToolProvider"](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectPath(self) -> str:
        """The object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetObjectPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ParentPath(self) -> str:
        """The object path of the parent of the object. Returns 'No Object Available' if the parent is the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def GrandParentPath(self) -> str:
        """The object path of the parent of the parent of the object. Returns 'No Object Available' if the grandparent is or above the scenario."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__["_GetGrandParentPath"](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetShortDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetShortDescription"](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__["_GetLongDescription"](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object. Cannot be set for central bodies."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__["_SetLongDescription"](arg_newDescription.COM_val))

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DayCount_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__["_DateElements_Array"](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__["_DateString"](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val

    @property
    def Dimension(self) -> str:
        """Name of the dimension."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @property
    def UnitAbbrv(self) -> str:
        """Unit abbreviation for the current units."""
        with agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetUnitAbbrv"](byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    def SetUnits(self, unitAbbrv:str) -> bool:
        """Sets the current units."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__["_SetUnits"](arg_unitAbbrv.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    def SetValue(self, value:float) -> None:
        """Sets the value in the current units."""
        with agmarshall.DOUBLE_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_SetValue"](arg_value.COM_val))

    def SetValueAndRate(self, value:float, valueRate:float) -> None:
        """Sets the value and valueRate in current units and current units per sec."""
        with agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.DOUBLE_arg(valueRate) as arg_valueRate:
            agcls.evaluate_hresult(self.__dict__["_SetValueAndRate"](arg_value.COM_val, arg_valueRate.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{824518FA-47BD-4cb3-A0DB-CE2BCB269137}", IAgCrdnCalcScalarPluginResultEval)
agcls.AgTypeNameMap["IAgCrdnCalcScalarPluginResultEval"] = IAgCrdnCalcScalarPluginResultEval
__all__.append("IAgCrdnCalcScalarPluginResultEval")


class IAgCrdnVectorPlugin(object):
    """
    COM Plugin interface for a Crdn Vector.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered just before the first computational event trigger."""
        raise STKPluginMethodNotImplementedError("Init was not implemented.")

    def Register(self, result:"IAgCrdnVectorPluginResultReg") -> None:
        """Triggered after Init() to allow setting for Dimension and Reference Axes."""
        raise STKPluginMethodNotImplementedError("Register was not implemented.")

    def Reset(self, result:"IAgCrdnVectorPluginResultReset") -> bool:
        """Triggered on a Reset event."""
        raise STKPluginMethodNotImplementedError("Reset was not implemented.")

    def Evaluate(self, result:"IAgCrdnVectorPluginResultEval") -> bool:
        """Triggered when the plugin is evaluated for the vector components"""
        raise STKPluginMethodNotImplementedError("Evaluate was not implemented.")

    def Free(self) -> None:
        """Triggered just before the plugin is destroyed."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgCrdnVectorPlugin")

class IAgCrdnPointPlugin(object):
    """
    COM Plugin interface for a Crdn Point.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered just before the first computational event trigger."""
        raise STKPluginMethodNotImplementedError("Init was not implemented.")

    def Register(self, result:"IAgCrdnPointPluginResultReg") -> None:
        """Triggered after Init() to allow setting of Reference System."""
        raise STKPluginMethodNotImplementedError("Register was not implemented.")

    def Reset(self, result:"IAgCrdnPointPluginResultReset") -> bool:
        """Triggered on a Reset event."""
        raise STKPluginMethodNotImplementedError("Reset was not implemented.")

    def Evaluate(self, result:"IAgCrdnPointPluginResultEval") -> bool:
        """Triggered when the plugin is evaluated for the position (and velocity) components"""
        raise STKPluginMethodNotImplementedError("Evaluate was not implemented.")

    def Free(self) -> None:
        """Triggered just before the plugin is destroyed."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgCrdnPointPlugin")

class IAgCrdnAxesPlugin(object):
    """
    COM Plugin interface for a Crdn Axes.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered just before the first computational event trigger."""
        raise STKPluginMethodNotImplementedError("Init was not implemented.")

    def Register(self, result:"IAgCrdnAxesPluginResultReg") -> None:
        """Triggered after Init() to allow setting of Reference Axes."""
        raise STKPluginMethodNotImplementedError("Register was not implemented.")

    def Reset(self, result:"IAgCrdnAxesPluginResultReset") -> bool:
        """Triggered on a Reset event."""
        raise STKPluginMethodNotImplementedError("Reset was not implemented.")

    def Evaluate(self, result:"IAgCrdnAxesPluginResultEval") -> bool:
        """Triggered when the plugin is evaluated for the axes orientation"""
        raise STKPluginMethodNotImplementedError("Evaluate was not implemented.")

    def Free(self) -> None:
        """Triggered just before the plugin is destroyed."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgCrdnAxesPlugin")

class IAgCrdnCalcScalarPlugin(object):
    """
    COM Plugin interface for a Crdn CalcScalar.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered just before the first computational event trigger."""
        raise STKPluginMethodNotImplementedError("Init was not implemented.")

    def Register(self, result:"IAgCrdnCalcScalarPluginResultReg") -> None:
        """Triggered after Init() to allow setting of any registration information."""
        raise STKPluginMethodNotImplementedError("Register was not implemented.")

    def Reset(self, result:"IAgCrdnCalcScalarPluginResultReset") -> bool:
        """Triggered on a Reset event."""
        raise STKPluginMethodNotImplementedError("Reset was not implemented.")

    def Evaluate(self, result:"IAgCrdnCalcScalarPluginResultEval") -> bool:
        """Triggered when the plugin is evaluated for the value and valueRate"""
        raise STKPluginMethodNotImplementedError("Evaluate was not implemented.")

    def Free(self) -> None:
        """Triggered just before the plugin is destroyed."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgCrdnCalcScalarPlugin")



class AgCrdnConfiguredVector(IAgCrdnConfiguredVector):
    """Crdn Vector object which computes its components"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredVector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredVector._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredVector._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredVector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredVector.")
        
agcls.AgClassCatalog.add_catalog_entry("{4994EDD5-2245-4421-8D3F-EE6476FECC52}", AgCrdnConfiguredVector)
__all__.append("AgCrdnConfiguredVector")


class AgCrdnConfiguredVectorWithRate(IAgCrdnConfiguredVectorWithRate):
    """Crdn Vector object which computes its components and rate"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredVectorWithRate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredVectorWithRate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredVectorWithRate._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredVectorWithRate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredVectorWithRate.")
        
agcls.AgClassCatalog.add_catalog_entry("{D9F73410-6898-4CB9-B1A5-4C43F030BC06}", AgCrdnConfiguredVectorWithRate)
__all__.append("AgCrdnConfiguredVectorWithRate")


class AgCrdnConfiguredAxes(IAgCrdnConfiguredAxes):
    """Crdn Axes object which computes its quaternion"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredAxes.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredAxes._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredAxes._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredAxes._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredAxes.")
        
agcls.AgClassCatalog.add_catalog_entry("{8AA921AD-0577-4E6E-97A0-84C2B0C62DDA}", AgCrdnConfiguredAxes)
__all__.append("AgCrdnConfiguredAxes")


class AgCrdnConfiguredAxesWithRate(IAgCrdnConfiguredAxesWithRate):
    """Crdn Axes object which computes its quaternion and angular velocity"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredAxesWithRate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredAxesWithRate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredAxesWithRate._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredAxesWithRate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredAxesWithRate.")
        
agcls.AgClassCatalog.add_catalog_entry("{3D56B181-3F36-41B1-959A-ED288C64F3E6}", AgCrdnConfiguredAxesWithRate)
__all__.append("AgCrdnConfiguredAxesWithRate")


class AgCrdnConfiguredAngle(IAgCrdnConfiguredAngle):
    """Crdn Angle object which computes its angle."""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredAngle.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredAngle._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredAngle._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredAngle._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredAngle.")
        
agcls.AgClassCatalog.add_catalog_entry("{9308E40E-4023-444F-B2D6-AC7EC89A615B}", AgCrdnConfiguredAngle)
__all__.append("AgCrdnConfiguredAngle")


class AgCrdnConfiguredAngleWithRate(IAgCrdnConfiguredAngleWithRate):
    """Crdn Angle object which computes its angle and rate."""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredAngleWithRate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredAngleWithRate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredAngleWithRate._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredAngleWithRate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredAngleWithRate.")
        
agcls.AgClassCatalog.add_catalog_entry("{7B8DE947-D2BE-4319-A038-797CAE1D52FD}", AgCrdnConfiguredAngleWithRate)
__all__.append("AgCrdnConfiguredAngleWithRate")


class AgCrdnConfiguredPoint(IAgCrdnConfiguredPoint):
    """Crdn Point object which computes its components"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredPoint.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredPoint._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredPoint._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredPoint._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredPoint.")
        
agcls.AgClassCatalog.add_catalog_entry("{03C0E4D7-EAD3-4BB4-BD7E-6BD6C9B5731B}", AgCrdnConfiguredPoint)
__all__.append("AgCrdnConfiguredPoint")


class AgCrdnConfiguredPointWithRate(IAgCrdnConfiguredPointWithRate):
    """Crdn Point object which computes its components and rate"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredPointWithRate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredPointWithRate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredPointWithRate._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredPointWithRate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredPointWithRate.")
        
agcls.AgClassCatalog.add_catalog_entry("{1F71F8C2-36F7-44DE-891C-8A4708CABEEF}", AgCrdnConfiguredPointWithRate)
__all__.append("AgCrdnConfiguredPointWithRate")


class AgCrdnConfiguredSystem(IAgCrdnConfiguredSystem):
    """Crdn System object which computes its components"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredSystem.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredSystem._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredSystem._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredSystem._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredSystem.")
        
agcls.AgClassCatalog.add_catalog_entry("{31C8BC52-E044-4048-8379-8BE9392F97BD}", AgCrdnConfiguredSystem)
__all__.append("AgCrdnConfiguredSystem")


class AgCrdnConfiguredSystemWithRate(IAgCrdnConfiguredSystemWithRate):
    """Crdn System object which computes its components and rate"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredSystemWithRate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredSystemWithRate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredSystemWithRate._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredSystemWithRate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredSystemWithRate.")
        
agcls.AgClassCatalog.add_catalog_entry("{FF28A49A-852C-4EE8-B9B2-848A2F85B2C3}", AgCrdnConfiguredSystemWithRate)
__all__.append("AgCrdnConfiguredSystemWithRate")


class AgCrdnPluginProvider(IAgCrdnPluginProvider):
    """Vector Tool plugin provider."""
    def __init__(self, sourceObject=None):
        IAgCrdnPluginProvider.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnPluginProvider._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnPluginProvider._get_property(self, attrname) is not None: found_prop = IAgCrdnPluginProvider._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnPluginProvider.")
        
agcls.AgClassCatalog.add_catalog_entry("{94A1EB61-41DE-4DCE-AE8D-C0EFCD875446}", AgCrdnPluginProvider)
__all__.append("AgCrdnPluginProvider")


class AgCrdnConfiguredCalcScalar(IAgCrdnConfiguredCalcScalar):
    """Crdn Calc Scalar object which computes its value"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredCalcScalar.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredCalcScalar._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredCalcScalar._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredCalcScalar._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredCalcScalar.")
        
agcls.AgClassCatalog.add_catalog_entry("{EC2EA481-6D41-40F3-BCA6-D10C10EF6928}", AgCrdnConfiguredCalcScalar)
__all__.append("AgCrdnConfiguredCalcScalar")


class AgCrdnConfiguredCalcScalarWithRate(IAgCrdnConfiguredCalcScalarWithRate):
    """Crdn Calc Scalar object which computes its value and rate"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredCalcScalarWithRate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredCalcScalarWithRate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredCalcScalarWithRate._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredCalcScalarWithRate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredCalcScalarWithRate.")
        
agcls.AgClassCatalog.add_catalog_entry("{158E1D01-EA49-40A1-8BD2-015F974F3228}", AgCrdnConfiguredCalcScalarWithRate)
__all__.append("AgCrdnConfiguredCalcScalarWithRate")


class AgCrdnConfiguredCalcParameterSet(IAgCrdnConfiguredCalcParameterSet):
    """Crdn Calc ParameterSet object which computes a set of scalar parameters"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredCalcParameterSet.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredCalcParameterSet._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredCalcParameterSet._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredCalcParameterSet._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredCalcParameterSet.")
        
agcls.AgClassCatalog.add_catalog_entry("{E3FF050B-B54B-4C21-A920-681B0F9898C3}", AgCrdnConfiguredCalcParameterSet)
__all__.append("AgCrdnConfiguredCalcParameterSet")


class AgCrdnConfiguredCalcParameterSetWithRate(IAgCrdnConfiguredCalcParameterSetWithRate):
    """Crdn Calc ParameterSet object which computes a set of scalar parameters and their rates"""
    def __init__(self, sourceObject=None):
        IAgCrdnConfiguredCalcParameterSetWithRate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnConfiguredCalcParameterSetWithRate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnConfiguredCalcParameterSetWithRate._get_property(self, attrname) is not None: found_prop = IAgCrdnConfiguredCalcParameterSetWithRate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnConfiguredCalcParameterSetWithRate.")
        
agcls.AgClassCatalog.add_catalog_entry("{B873149D-79C4-4618-A049-FC57BCE3F524}", AgCrdnConfiguredCalcParameterSetWithRate)
__all__.append("AgCrdnConfiguredCalcParameterSetWithRate")


class AgCrdnPluginCalcProvider(IAgCrdnPluginCalcProvider):
    """Calc Tool plugin provider."""
    def __init__(self, sourceObject=None):
        IAgCrdnPluginCalcProvider.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnPluginCalcProvider._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnPluginCalcProvider._get_property(self, attrname) is not None: found_prop = IAgCrdnPluginCalcProvider._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnPluginCalcProvider.")
        
agcls.AgClassCatalog.add_catalog_entry("{3279925D-E0F6-4654-B8B1-DF93DAD6AD44}", AgCrdnPluginCalcProvider)
__all__.append("AgCrdnPluginCalcProvider")


class AgCrdnVectorPluginResultReg(IAgCrdnVectorPluginResultReg):
    """COM Plugin Result interface for the Register method of IAgCrdnVectorPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnVectorPluginResultReg.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnVectorPluginResultReg._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnVectorPluginResultReg._get_property(self, attrname) is not None: found_prop = IAgCrdnVectorPluginResultReg._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnVectorPluginResultReg.")
        
agcls.AgClassCatalog.add_catalog_entry("{7F6EAF1E-160C-4E69-B74D-703B8DA432CD}", AgCrdnVectorPluginResultReg)
__all__.append("AgCrdnVectorPluginResultReg")


class AgCrdnVectorPluginResultReset(IAgCrdnVectorPluginResultReset):
    """COM Plugin Result interface for the Reset method of IAgCrdnVectorPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnVectorPluginResultReset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnVectorPluginResultReset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnVectorPluginResultReset._get_property(self, attrname) is not None: found_prop = IAgCrdnVectorPluginResultReset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnVectorPluginResultReset.")
        
agcls.AgClassCatalog.add_catalog_entry("{8392CA93-7847-42F5-BDEB-DAC782E0186D}", AgCrdnVectorPluginResultReset)
__all__.append("AgCrdnVectorPluginResultReset")


class AgCrdnVectorPluginResultEval(IAgCrdnVectorPluginResultEval):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnVectorPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnVectorPluginResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnVectorPluginResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnVectorPluginResultEval._get_property(self, attrname) is not None: found_prop = IAgCrdnVectorPluginResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnVectorPluginResultEval.")
        
agcls.AgClassCatalog.add_catalog_entry("{E0A7FAD4-6B42-4276-AD01-03EFC0571947}", AgCrdnVectorPluginResultEval)
__all__.append("AgCrdnVectorPluginResultEval")


class AgCrdnPointPluginResultReg(IAgCrdnPointPluginResultReg):
    """COM Plugin Result interface for the Register method of IAgCrdnPointPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnPointPluginResultReg.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnPointPluginResultReg._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnPointPluginResultReg._get_property(self, attrname) is not None: found_prop = IAgCrdnPointPluginResultReg._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnPointPluginResultReg.")
        
agcls.AgClassCatalog.add_catalog_entry("{09008755-CB97-4699-8A36-8302A6D5FCDD}", AgCrdnPointPluginResultReg)
__all__.append("AgCrdnPointPluginResultReg")


class AgCrdnPointPluginResultReset(IAgCrdnPointPluginResultReset):
    """COM Plugin Result interface for the Reset method of IAgCrdnPointPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnPointPluginResultReset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnPointPluginResultReset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnPointPluginResultReset._get_property(self, attrname) is not None: found_prop = IAgCrdnPointPluginResultReset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnPointPluginResultReset.")
        
agcls.AgClassCatalog.add_catalog_entry("{F772D4EE-4686-4623-8258-C3CAAE5BF259}", AgCrdnPointPluginResultReset)
__all__.append("AgCrdnPointPluginResultReset")


class AgCrdnPointPluginResultEval(IAgCrdnPointPluginResultEval):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnPointPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnPointPluginResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnPointPluginResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnPointPluginResultEval._get_property(self, attrname) is not None: found_prop = IAgCrdnPointPluginResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnPointPluginResultEval.")
        
agcls.AgClassCatalog.add_catalog_entry("{BC6DF6DA-8C53-48B3-BF48-B30EFDD2C794}", AgCrdnPointPluginResultEval)
__all__.append("AgCrdnPointPluginResultEval")


class AgCrdnAxesPluginResultReg(IAgCrdnAxesPluginResultReg):
    """COM Plugin Result interface for the Register method of IAgCrdnAxesPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnAxesPluginResultReg.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnAxesPluginResultReg._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnAxesPluginResultReg._get_property(self, attrname) is not None: found_prop = IAgCrdnAxesPluginResultReg._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnAxesPluginResultReg.")
        
agcls.AgClassCatalog.add_catalog_entry("{87663E10-C2D4-4878-B998-854C51A8C473}", AgCrdnAxesPluginResultReg)
__all__.append("AgCrdnAxesPluginResultReg")


class AgCrdnAxesPluginResultReset(IAgCrdnAxesPluginResultReset):
    """COM Plugin Result interface for the Reset method of IAgCrdnAxesPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnAxesPluginResultReset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnAxesPluginResultReset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnAxesPluginResultReset._get_property(self, attrname) is not None: found_prop = IAgCrdnAxesPluginResultReset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnAxesPluginResultReset.")
        
agcls.AgClassCatalog.add_catalog_entry("{9F4B5CD1-4BB3-4087-B809-F3CD605074EA}", AgCrdnAxesPluginResultReset)
__all__.append("AgCrdnAxesPluginResultReset")


class AgCrdnAxesPluginResultEval(IAgCrdnAxesPluginResultEval):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnAxesPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnAxesPluginResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnAxesPluginResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnAxesPluginResultEval._get_property(self, attrname) is not None: found_prop = IAgCrdnAxesPluginResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnAxesPluginResultEval.")
        
agcls.AgClassCatalog.add_catalog_entry("{9D108126-CA2E-4FBB-B60F-CBB81A64C08D}", AgCrdnAxesPluginResultEval)
__all__.append("AgCrdnAxesPluginResultEval")


class AgCrdnCalcScalarPluginResultReg(IAgCrdnCalcScalarPluginResultReg):
    """COM Plugin Result interface for the Register method of IAgCrdnCalcScalarPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnCalcScalarPluginResultReg.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnCalcScalarPluginResultReg._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnCalcScalarPluginResultReg._get_property(self, attrname) is not None: found_prop = IAgCrdnCalcScalarPluginResultReg._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnCalcScalarPluginResultReg.")
        
agcls.AgClassCatalog.add_catalog_entry("{CE7FE779-37DA-4C8C-8C68-B6D95AABC190}", AgCrdnCalcScalarPluginResultReg)
__all__.append("AgCrdnCalcScalarPluginResultReg")


class AgCrdnCalcScalarPluginResultReset(IAgCrdnCalcScalarPluginResultReset):
    """COM Plugin Result interface for the Reset method of IAgCrdnCalcScalarPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnCalcScalarPluginResultReset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnCalcScalarPluginResultReset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnCalcScalarPluginResultReset._get_property(self, attrname) is not None: found_prop = IAgCrdnCalcScalarPluginResultReset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnCalcScalarPluginResultReset.")
        
agcls.AgClassCatalog.add_catalog_entry("{968928A9-02E2-495C-9541-A5A69ABA56E5}", AgCrdnCalcScalarPluginResultReset)
__all__.append("AgCrdnCalcScalarPluginResultReset")


class AgCrdnCalcScalarPluginResultEval(IAgCrdnCalcScalarPluginResultEval):
    """COM Plugin Result interface for the Evaluate method of IAgCrdnCalcScalarPlugin."""
    def __init__(self, sourceObject=None):
        IAgCrdnCalcScalarPluginResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCrdnCalcScalarPluginResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCrdnCalcScalarPluginResultEval._get_property(self, attrname) is not None: found_prop = IAgCrdnCalcScalarPluginResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCrdnCalcScalarPluginResultEval.")
        
agcls.AgClassCatalog.add_catalog_entry("{BE8E4E5D-7BD0-4CD2-8355-9E485F9ACCA0}", AgCrdnCalcScalarPluginResultEval)
__all__.append("AgCrdnCalcScalarPluginResultEval")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
