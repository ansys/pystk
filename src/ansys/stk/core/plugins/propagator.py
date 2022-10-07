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

import agi.stk12.internal.comutil          as agcom
import agi.stk12.internal.coclassutil      as agcls
import agi.stk12.internal.marshall         as agmarshall
import agi.stk12.internal.dataanalysisutil as agdata
import agi.stk12.utilities.colors          as agcolor
from   agi.stk12.internal.comutil     import IUnknown, IDispatch, IPictureDisp, IAGFUNCTYPE, IEnumVARIANT
from   agi.stk12.internal.eventutil   import *
from   agi.stk12.utilities.exceptions import *


from agi.stk12.plugins.utplugin import *
from agi.stk12.plugins.hpopplugin import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError('Valid STK object model classes are returned from STK methods and should not be created independently.')

class AgEPropagatorWrapperPluginErrorCodes(IntEnum):
    '''
    Enumeration of AgPropagatorWrapperPlugin General Error Codes
    '''
    # Gator Plugin: An internal failure occurred.
    E_PROPAGATOR_WRAPPERS_PLUGIN_INTERNAL_FAILURE = (((1 << 31) | (4 << 16)) | 0x101),
    # Gator Plugin: Not configured properly.
    E_PROPAGATOR_WRAPPERS_PLUGIN_NOT_CONFIGURED = (((1 << 31) | (4 << 16)) | 0x102),
    # Gator Plugin: Central Body is undefined.
    E_PROPAGATOR_WRAPPERS_PLUGIN_CENTRALBODY_UNDEFINED = (((1 << 31) | (4 << 16)) | 0x103),
    # Gator Plugin: Sun Position Type SRP not supported.
    E_PROPAGATOR_WRAPPERS_PLUGIN_SUNPOSTYPE_SRP_NOT_SUPPORTED = (((1 << 31) | (4 << 16)) | 0x104),
    # Gator Plugin: The Square Root of an invalid value occurred.
    E_PROPAGATOR_WRAPPERS_PLUGIN_INVALID_SQR = (((1 << 31) | (4 << 16)) | 0x105),
    # Gator Plugin: Reference Axes Unavailable.
    E_PROPAGATOR_WRAPPERS_PLUGIN_REF_AXES_UNAVAILABLE = (((1 << 31) | (4 << 16)) | 0x106),
    # Gator Plugin: Color not valid.
    E_PROPAGATOR_WRAPPERS_PLUGIN_INVALID_COLOR = (((1 << 31) | (4 << 16)) | 0x107)

agcls.AgTypeNameMap['AgEPropagatorWrapperPluginErrorCodes'] = AgEPropagatorWrapperPluginErrorCodes
__all__.append('AgEPropagatorWrapperPluginErrorCodes')

class AgEEulerSequence(IntEnum):
    '''
    Enumeration AgEEulerSequence.
    '''
    # Sequence defined by rotation about x-axis, then about rotated y-axis, then about rotated x-axis.
    e121 = 121,
    # Sequence defined by rotation about x-axis, then about rotated y-axis, then about rotated z-axis.
    e123 = 123,
    # Sequence defined by rotation about x-axis, then about rotated z-axis, then about rotated x-axis.
    e131 = 131,
    # Sequence defined by rotation about x-axis, then about rotated z-axis, then about rotated y-axis.
    e132 = 132,
    # Sequence defined by rotation about y-axis, then about rotated x-axis, then about rotated y-axis.
    e212 = 212,
    # Sequence defined by rotation about y-axis, then about rotated x-axis, then about rotated z-axis.
    e213 = 213,
    # Sequence defined by rotation about y-axis, then about rotated z-axis, then about rotated x-axis.
    e231 = 231,
    # Sequence defined by rotation about y-axis, then about rotated z-axis, then about rotated y-axis.
    e232 = 232,
    # Sequence defined by rotation about z-axis, then about rotated x-axis, then about rotated y-axis.
    e312 = 312,
    # Sequence defined by rotation about z-axis, then about rotated x-axis, then about rotated z-axis.
    e313 = 313,
    # Sequence defined by rotation about z-axis, then about rotated y-axis, then about rotated x-axis.
    e321 = 321,
    # Sequence defined by rotation about z-axis, then about rotated y-axis, then about rotated x-axis.
    e323 = 323

agcls.AgTypeNameMap['AgEEulerSequence'] = AgEEulerSequence
__all__.append('AgEEulerSequence')


class IAgGatorPluginResultState(object):
    '''
    Astrogator plugin interface used to get state values. Supports IAgGatorState and IAgEpoch.
    '''
    _uuid = '{1FE7D2CB-DC59-4e05-A3C2-CBAB2C00EC45}'
    _num_methods = 28
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCd'] = _raise_uninitialized_error
        self.__dict__['_GetCr'] = _raise_uninitialized_error
        self.__dict__['_GetDragArea'] = _raise_uninitialized_error
        self.__dict__['_GetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_GetMass'] = _raise_uninitialized_error
        self.__dict__['_GetDryMass'] = _raise_uninitialized_error
        self.__dict__['_GetFuelMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_StopPropagation'] = _raise_uninitialized_error
        self.__dict__['_IndicateEvent'] = _raise_uninitialized_error
        self.__dict__['_SetMaxStep'] = _raise_uninitialized_error
        self.__dict__['_SetColor'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgGatorPluginResultState._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgGatorPluginResultState from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgGatorPluginResultState = agcom.GUID(IAgGatorPluginResultState._uuid)
        vtable_offset_local = IAgGatorPluginResultState._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCd'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCr'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__['_GetMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDryMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_GetFuelMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+14, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+16, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+17, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+18, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+19, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+20, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+21, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_StopPropagation'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+22, )
        self.__dict__['_IndicateEvent'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+23, agcom.LONG)
        self.__dict__['_SetMaxStep'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+24, agcom.DOUBLE)
        self.__dict__['_SetColor'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+25, agcom.BSTR)
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+26, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+27, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultState, vtable_offset_local+28, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGatorPluginResultState.__dict__ and type(IAgGatorPluginResultState.__dict__[attrname]) == property:
            return IAgGatorPluginResultState.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgGatorPluginResultState.')
    
    def Trace(self, numCalls:int) -> None:
        '''
        Set this interface to trace the next numCalls by outputting a message to the message viewer.
        '''
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def CbName(self) -> str:
        '''
        Name of the central body used as reference frame origin.
        '''
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    @property
    def Mu(self) -> float:
        '''
        Gravitational constant of the state central body
        '''
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def Cd(self) -> float:
        '''
        Drag Coefficient.
        '''
        with agmarshall.DOUBLE_arg() as arg_pCd:
            agcls.evaluate_hresult(self.__dict__['_GetCd'](byref(arg_pCd.COM_val)))
            return arg_pCd.python_val

    @property
    def Cr(self) -> float:
        '''
        SRP Coefficient.
        '''
        with agmarshall.DOUBLE_arg() as arg_pCr:
            agcls.evaluate_hresult(self.__dict__['_GetCr'](byref(arg_pCr.COM_val)))
            return arg_pCr.python_val

    @property
    def DragArea(self) -> float:
        '''
        Drag Area.
        '''
        with agmarshall.DOUBLE_arg() as arg_pDragArea:
            agcls.evaluate_hresult(self.__dict__['_GetDragArea'](byref(arg_pDragArea.COM_val)))
            return arg_pDragArea.python_val

    @property
    def SRPArea(self) -> float:
        '''
        SRP Area.
        '''
        with agmarshall.DOUBLE_arg() as arg_pSRPArea:
            agcls.evaluate_hresult(self.__dict__['_GetSRPArea'](byref(arg_pSRPArea.COM_val)))
            return arg_pSRPArea.python_val

    @property
    def Mass(self) -> float:
        '''
        Total Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pMass:
            agcls.evaluate_hresult(self.__dict__['_GetMass'](byref(arg_pMass.COM_val)))
            return arg_pMass.python_val

    @property
    def DryMass(self) -> float:
        '''
        Dry Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pDryMass:
            agcls.evaluate_hresult(self.__dict__['_GetDryMass'](byref(arg_pDryMass.COM_val)))
            return arg_pDryMass.python_val

    @property
    def FuelMass(self) -> float:
        '''
        Fuel Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pFuelMass:
            agcls.evaluate_hresult(self.__dict__['_GetFuelMass'](byref(arg_pFuelMass.COM_val)))
            return arg_pFuelMass.python_val

    @property
    def Altitude(self) -> float:
        '''
        Current altitude.
        '''
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        '''
        Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        '''
        Current position and velocity in the requested frame (in internal units) returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        '''
        Current detic latitude, detic longitude, and altitude(in internal units) returned as an array representing lat, lon, alt. Useful for scripting clients.
        '''
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        '''
        Position of the sun wrt the current satellite position, in the requested frame, computed in the requested manner, (in internal units) returned as an array representing x, y, z. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        '''
        Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def StopPropagation(self) -> None:
        '''
        Stops propagation.  For fatal errors.
        '''
        agcls.evaluate_hresult(self.__dict__['_StopPropagation']())

    def IndicateEvent(self, eEventIndicator:"AgEAsHpopPluginEventIndicators") -> None:
        '''
        Marks an event to the propagator.
        '''
        with agmarshall.AgEnum_arg(AgEAsHpopPluginEventIndicators, eEventIndicator) as arg_eEventIndicator:
            agcls.evaluate_hresult(self.__dict__['_IndicateEvent'](arg_eEventIndicator.COM_val))

    def SetMaxStep(self, maxStep:float) -> None:
        '''
        Sets the maximum step size for the propagator.
        '''
        with agmarshall.DOUBLE_arg(maxStep) as arg_maxStep:
            agcls.evaluate_hresult(self.__dict__['_SetMaxStep'](arg_maxStep.COM_val))

    def SetColor(self, color:str) -> None:
        '''
        Sets the segment color.
        '''
        with agmarshall.BSTR_arg(color) as arg_color:
            agcls.evaluate_hresult(self.__dict__['_SetColor'](arg_color.COM_val))

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        '''
        Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DateElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        '''
        Current epoch expressed using the date format abbreviation specified.
        '''
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__['_DateString'](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry('{1FE7D2CB-DC59-4e05-A3C2-CBAB2C00EC45}', IAgGatorPluginResultState)
agcls.AgTypeNameMap['IAgGatorPluginResultState'] = IAgGatorPluginResultState
__all__.append('IAgGatorPluginResultState')

class IAgGatorPluginResultEvalEngineModel(object):
    '''
    Astrogator plugin interface used to get/set engine model settings during the computation of a step. Supports IAgGatorState and IAgEpoch.
    '''
    _uuid = '{D120DA1E-B666-4a30-8D32-E59133C72B87}'
    _num_methods = 32
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCd'] = _raise_uninitialized_error
        self.__dict__['_GetCr'] = _raise_uninitialized_error
        self.__dict__['_GetDragArea'] = _raise_uninitialized_error
        self.__dict__['_GetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_GetMass'] = _raise_uninitialized_error
        self.__dict__['_GetDryMass'] = _raise_uninitialized_error
        self.__dict__['_GetFuelMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_GetThrust'] = _raise_uninitialized_error
        self.__dict__['_GetIsp'] = _raise_uninitialized_error
        self.__dict__['_GetMassFlowRate'] = _raise_uninitialized_error
        self.__dict__['_GetTimeSinceIgnition'] = _raise_uninitialized_error
        self.__dict__['_SetThrustAndIsp'] = _raise_uninitialized_error
        self.__dict__['_SetThrustAndMassFlowRate'] = _raise_uninitialized_error
        self.__dict__['_SetIspAndMassFlowRate'] = _raise_uninitialized_error
        self.__dict__['_StopPropagation'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgGatorPluginResultEvalEngineModel._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgGatorPluginResultEvalEngineModel from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgGatorPluginResultEvalEngineModel = agcom.GUID(IAgGatorPluginResultEvalEngineModel._uuid)
        vtable_offset_local = IAgGatorPluginResultEvalEngineModel._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCd'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCr'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__['_GetMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDryMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_GetFuelMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+14, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+16, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+17, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+18, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+19, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+20, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+21, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetThrust'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+22, POINTER(agcom.DOUBLE))
        self.__dict__['_GetIsp'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+23, POINTER(agcom.DOUBLE))
        self.__dict__['_GetMassFlowRate'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+24, POINTER(agcom.DOUBLE))
        self.__dict__['_GetTimeSinceIgnition'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+25, POINTER(agcom.DOUBLE))
        self.__dict__['_SetThrustAndIsp'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+26, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_SetThrustAndMassFlowRate'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+27, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_SetIspAndMassFlowRate'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+28, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_StopPropagation'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+29, )
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+30, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+31, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultEvalEngineModel, vtable_offset_local+32, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGatorPluginResultEvalEngineModel.__dict__ and type(IAgGatorPluginResultEvalEngineModel.__dict__[attrname]) == property:
            return IAgGatorPluginResultEvalEngineModel.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgGatorPluginResultEvalEngineModel.')
    
    def Trace(self, numCalls:int) -> None:
        '''
        Set this interface to trace the next numCalls by outputting a message to the message viewer.
        '''
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def CbName(self) -> str:
        '''
        Name of the central body used as reference frame origin.
        '''
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    @property
    def Mu(self) -> float:
        '''
        Gravitational constant of the state central body
        '''
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def Cd(self) -> float:
        '''
        Drag Coefficient.
        '''
        with agmarshall.DOUBLE_arg() as arg_pCd:
            agcls.evaluate_hresult(self.__dict__['_GetCd'](byref(arg_pCd.COM_val)))
            return arg_pCd.python_val

    @property
    def Cr(self) -> float:
        '''
        SRP Coefficient.
        '''
        with agmarshall.DOUBLE_arg() as arg_pCr:
            agcls.evaluate_hresult(self.__dict__['_GetCr'](byref(arg_pCr.COM_val)))
            return arg_pCr.python_val

    @property
    def DragArea(self) -> float:
        '''
        Drag Area.
        '''
        with agmarshall.DOUBLE_arg() as arg_pDragArea:
            agcls.evaluate_hresult(self.__dict__['_GetDragArea'](byref(arg_pDragArea.COM_val)))
            return arg_pDragArea.python_val

    @property
    def SRPArea(self) -> float:
        '''
        SRP Area.
        '''
        with agmarshall.DOUBLE_arg() as arg_pSRPArea:
            agcls.evaluate_hresult(self.__dict__['_GetSRPArea'](byref(arg_pSRPArea.COM_val)))
            return arg_pSRPArea.python_val

    @property
    def Mass(self) -> float:
        '''
        Total Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pMass:
            agcls.evaluate_hresult(self.__dict__['_GetMass'](byref(arg_pMass.COM_val)))
            return arg_pMass.python_val

    @property
    def DryMass(self) -> float:
        '''
        Dry Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pDryMass:
            agcls.evaluate_hresult(self.__dict__['_GetDryMass'](byref(arg_pDryMass.COM_val)))
            return arg_pDryMass.python_val

    @property
    def FuelMass(self) -> float:
        '''
        Fuel Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pFuelMass:
            agcls.evaluate_hresult(self.__dict__['_GetFuelMass'](byref(arg_pFuelMass.COM_val)))
            return arg_pFuelMass.python_val

    @property
    def Altitude(self) -> float:
        '''
        Current altitude.
        '''
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        '''
        Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        '''
        Current position and velocity in the requested frame (in internal units) returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        '''
        Current detic latitude, detic longitude, and altitude(in internal units) returned as an array representing lat, lon, alt. Useful for scripting clients.
        '''
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        '''
        Position of the sun wrt the current satellite position, in the requested frame, computed in the requested manner, (in internal units) returned as an array representing x, y, z. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        '''
        Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def Thrust(self) -> float:
        '''
        Current thrust (N).
        '''
        with agmarshall.DOUBLE_arg() as arg_pThrust:
            agcls.evaluate_hresult(self.__dict__['_GetThrust'](byref(arg_pThrust.COM_val)))
            return arg_pThrust.python_val

    @property
    def Isp(self) -> float:
        '''
        Current Isp (secs).
        '''
        with agmarshall.DOUBLE_arg() as arg_pIsp:
            agcls.evaluate_hresult(self.__dict__['_GetIsp'](byref(arg_pIsp.COM_val)))
            return arg_pIsp.python_val

    @property
    def MassFlowRate(self) -> float:
        '''
        Current mass flow rate (kg/sec).
        '''
        with agmarshall.DOUBLE_arg() as arg_pMassFlowRate:
            agcls.evaluate_hresult(self.__dict__['_GetMassFlowRate'](byref(arg_pMassFlowRate.COM_val)))
            return arg_pMassFlowRate.python_val

    @property
    def TimeSinceIgnition(self) -> float:
        '''
        Time since ignition (secs).
        '''
        with agmarshall.DOUBLE_arg() as arg_pTimeSinceIgnition:
            agcls.evaluate_hresult(self.__dict__['_GetTimeSinceIgnition'](byref(arg_pTimeSinceIgnition.COM_val)))
            return arg_pTimeSinceIgnition.python_val

    def SetThrustAndIsp(self, thrust:float, isp:float) -> bool:
        '''
        Sets the current thrust (N) and isp (secs). Computes the mass flow rate using the rocket equation. Returns false on an error.
        '''
        with agmarshall.DOUBLE_arg(thrust) as arg_thrust, \
             agmarshall.DOUBLE_arg(isp) as arg_isp, \
             agmarshall.VARIANT_BOOL_arg() as arg_pReturn:
            agcls.evaluate_hresult(self.__dict__['_SetThrustAndIsp'](arg_thrust.COM_val, arg_isp.COM_val, byref(arg_pReturn.COM_val)))
            return arg_pReturn.python_val

    def SetThrustAndMassFlowRate(self, thrust:float, massFlowRate:float) -> bool:
        '''
        Sets the current thrust(N) and mass flow rate (kg/sec). Computes the isp using the rocket equation. Returns false on an error.
        '''
        with agmarshall.DOUBLE_arg(thrust) as arg_thrust, \
             agmarshall.DOUBLE_arg(massFlowRate) as arg_massFlowRate, \
             agmarshall.VARIANT_BOOL_arg() as arg_pReturn:
            agcls.evaluate_hresult(self.__dict__['_SetThrustAndMassFlowRate'](arg_thrust.COM_val, arg_massFlowRate.COM_val, byref(arg_pReturn.COM_val)))
            return arg_pReturn.python_val

    def SetIspAndMassFlowRate(self, isp:float, massFlowRate:float) -> bool:
        '''
        Sets the current isp and mass flow rate. Computes the thrust using the rocket equation. Returns false on an error.
        '''
        with agmarshall.DOUBLE_arg(isp) as arg_isp, \
             agmarshall.DOUBLE_arg(massFlowRate) as arg_massFlowRate, \
             agmarshall.VARIANT_BOOL_arg() as arg_pReturn:
            agcls.evaluate_hresult(self.__dict__['_SetIspAndMassFlowRate'](arg_isp.COM_val, arg_massFlowRate.COM_val, byref(arg_pReturn.COM_val)))
            return arg_pReturn.python_val

    def StopPropagation(self) -> None:
        '''
        Stops propagation.  For fatal errors.
        '''
        agcls.evaluate_hresult(self.__dict__['_StopPropagation']())

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        '''
        Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DateElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        '''
        Current epoch expressed using the date format abbreviation specified.
        '''
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__['_DateString'](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry('{D120DA1E-B666-4a30-8D32-E59133C72B87}', IAgGatorPluginResultEvalEngineModel)
agcls.AgTypeNameMap['IAgGatorPluginResultEvalEngineModel'] = IAgGatorPluginResultEvalEngineModel
__all__.append('IAgGatorPluginResultEvalEngineModel')

class IAgGatorPluginResultAttCtrl(object):
    '''
    Astrogator plugin interface used to get/set attitude controller settings. Supports IAgGatorState and IAgEpoch.
    '''
    _uuid = '{96E6BDF6-C1C6-4a50-9A93-6782BFF9FE5F}'
    _num_methods = 33
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCd'] = _raise_uninitialized_error
        self.__dict__['_GetCr'] = _raise_uninitialized_error
        self.__dict__['_GetDragArea'] = _raise_uninitialized_error
        self.__dict__['_GetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_GetMass'] = _raise_uninitialized_error
        self.__dict__['_GetDryMass'] = _raise_uninitialized_error
        self.__dict__['_GetFuelMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_GetRefAxes'] = _raise_uninitialized_error
        self.__dict__['_SetRefAxes'] = _raise_uninitialized_error
        self.__dict__['_SetQuaternion'] = _raise_uninitialized_error
        self.__dict__['_EulerRotate'] = _raise_uninitialized_error
        self.__dict__['_GetQuaternion'] = _raise_uninitialized_error
        self.__dict__['_GetQuaternion_Array'] = _raise_uninitialized_error
        self.__dict__['_GetEulerRotation'] = _raise_uninitialized_error
        self.__dict__['_GetEulerRotation_Array'] = _raise_uninitialized_error
        self.__dict__['_StopPropagation'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgGatorPluginResultAttCtrl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgGatorPluginResultAttCtrl from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgGatorPluginResultAttCtrl = agcom.GUID(IAgGatorPluginResultAttCtrl._uuid)
        vtable_offset_local = IAgGatorPluginResultAttCtrl._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCd'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCr'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__['_GetMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDryMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_GetFuelMass'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+14, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+16, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+17, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+18, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+19, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+20, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+21, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetRefAxes'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+22, POINTER(agcom.BSTR))
        self.__dict__['_SetRefAxes'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+23, agcom.BSTR, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_SetQuaternion'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+24, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_EulerRotate'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+25, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_GetQuaternion'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+26, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetQuaternion_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+27, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetEulerRotation'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+28, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetEulerRotation_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+29, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_StopPropagation'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+30, )
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+31, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+32, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginResultAttCtrl, vtable_offset_local+33, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGatorPluginResultAttCtrl.__dict__ and type(IAgGatorPluginResultAttCtrl.__dict__[attrname]) == property:
            return IAgGatorPluginResultAttCtrl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgGatorPluginResultAttCtrl.')
    
    def Trace(self, numCalls:int) -> None:
        '''
        Set this interface to trace the next numCalls by outputting a message to the message viewer.
        '''
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def CbName(self) -> str:
        '''
        Name of the central body used as reference frame origin.
        '''
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    @property
    def Mu(self) -> float:
        '''
        Gravitational constant of the state central body
        '''
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def Cd(self) -> float:
        '''
        Drag Coefficient.
        '''
        with agmarshall.DOUBLE_arg() as arg_pCd:
            agcls.evaluate_hresult(self.__dict__['_GetCd'](byref(arg_pCd.COM_val)))
            return arg_pCd.python_val

    @property
    def Cr(self) -> float:
        '''
        SRP Coefficient.
        '''
        with agmarshall.DOUBLE_arg() as arg_pCr:
            agcls.evaluate_hresult(self.__dict__['_GetCr'](byref(arg_pCr.COM_val)))
            return arg_pCr.python_val

    @property
    def DragArea(self) -> float:
        '''
        Drag Area.
        '''
        with agmarshall.DOUBLE_arg() as arg_pDragArea:
            agcls.evaluate_hresult(self.__dict__['_GetDragArea'](byref(arg_pDragArea.COM_val)))
            return arg_pDragArea.python_val

    @property
    def SRPArea(self) -> float:
        '''
        SRP Area.
        '''
        with agmarshall.DOUBLE_arg() as arg_pSRPArea:
            agcls.evaluate_hresult(self.__dict__['_GetSRPArea'](byref(arg_pSRPArea.COM_val)))
            return arg_pSRPArea.python_val

    @property
    def Mass(self) -> float:
        '''
        Total Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pMass:
            agcls.evaluate_hresult(self.__dict__['_GetMass'](byref(arg_pMass.COM_val)))
            return arg_pMass.python_val

    @property
    def DryMass(self) -> float:
        '''
        Dry Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pDryMass:
            agcls.evaluate_hresult(self.__dict__['_GetDryMass'](byref(arg_pDryMass.COM_val)))
            return arg_pDryMass.python_val

    @property
    def FuelMass(self) -> float:
        '''
        Fuel Mass.
        '''
        with agmarshall.DOUBLE_arg() as arg_pFuelMass:
            agcls.evaluate_hresult(self.__dict__['_GetFuelMass'](byref(arg_pFuelMass.COM_val)))
            return arg_pFuelMass.python_val

    @property
    def Altitude(self) -> float:
        '''
        Current altitude.
        '''
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        '''
        Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        '''
        Current position and velocity in the requested frame (in internal units) returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        '''
        Current detic latitude, detic longitude, and altitude(in internal units) returned as an array representing lat, lon, alt. Useful for scripting clients.
        '''
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        '''
        Position of the sun wrt the current satellite position, in the requested frame, computed in the requested manner, (in internal units) returned as an array representing x, y, z. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        '''
        Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def RefAxes(self) -> str:
        '''
        Name of the reference axes.
        '''
        with agmarshall.BSTR_arg() as arg_pRefAxesName:
            agcls.evaluate_hresult(self.__dict__['_GetRefAxes'](byref(arg_pRefAxesName.COM_val)))
            return arg_pRefAxesName.python_val

    def SetRefAxes(self, name:str) -> bool:
        '''
        Sets the reference axes.
        '''
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__['_SetRefAxes'](arg_name.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    def SetQuaternion(self, q1:float, q2:float, q3:float, q4:float) -> None:
        '''
        Sets the current orientation using a quaternion.
        '''
        with agmarshall.DOUBLE_arg(q1) as arg_q1, \
             agmarshall.DOUBLE_arg(q2) as arg_q2, \
             agmarshall.DOUBLE_arg(q3) as arg_q3, \
             agmarshall.DOUBLE_arg(q4) as arg_q4:
            agcls.evaluate_hresult(self.__dict__['_SetQuaternion'](arg_q1.COM_val, arg_q2.COM_val, arg_q3.COM_val, arg_q4.COM_val))

    def EulerRotate(self, sequence:"AgEEulerSequence", first:float, second:float, third:float) -> None:
        '''
        Sets the current orientation using a sequence of euler rotations.
        '''
        with agmarshall.AgEnum_arg(AgEEulerSequence, sequence) as arg_sequence, \
             agmarshall.DOUBLE_arg(first) as arg_first, \
             agmarshall.DOUBLE_arg(second) as arg_second, \
             agmarshall.DOUBLE_arg(third) as arg_third:
            agcls.evaluate_hresult(self.__dict__['_EulerRotate'](arg_sequence.COM_val, arg_first.COM_val, arg_second.COM_val, arg_third.COM_val))

    def GetQuaternion(self) -> typing.Tuple[float, float, float, float]:
        '''
        Gets the current orientation as a quaternion.
        '''
        with agmarshall.DOUBLE_arg() as arg_q1, \
             agmarshall.DOUBLE_arg() as arg_q2, \
             agmarshall.DOUBLE_arg() as arg_q3, \
             agmarshall.DOUBLE_arg() as arg_q4:
            agcls.evaluate_hresult(self.__dict__['_GetQuaternion'](byref(arg_q1.COM_val), byref(arg_q2.COM_val), byref(arg_q3.COM_val), byref(arg_q4.COM_val)))
            return arg_q1.python_val, arg_q2.python_val, arg_q3.python_val, arg_q4.python_val

    def GetQuaternion_Array(self) -> list:
        '''
        Gets the current orientation as a quaternion returned as an array representing Q1, Q2, Q3, and Q4. Useful for scripting clients.
        '''
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_GetQuaternion_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def GetEulerRotation(self, sequence:"AgEEulerSequence") -> typing.Tuple[float, float, float]:
        '''
        Gets the current orientation as euler angles.
        '''
        with agmarshall.AgEnum_arg(AgEEulerSequence, sequence) as arg_sequence, \
             agmarshall.DOUBLE_arg() as arg_first, \
             agmarshall.DOUBLE_arg() as arg_second, \
             agmarshall.DOUBLE_arg() as arg_third:
            agcls.evaluate_hresult(self.__dict__['_GetEulerRotation'](arg_sequence.COM_val, byref(arg_first.COM_val), byref(arg_second.COM_val), byref(arg_third.COM_val)))
            return arg_first.python_val, arg_second.python_val, arg_third.python_val

    def GetEulerRotation_Array(self, sequence:"AgEEulerSequence") -> list:
        '''
        Gets the current orientation as euler rotations returned as an array. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEEulerSequence, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_GetEulerRotation_Array'](arg_sequence.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def StopPropagation(self) -> None:
        '''
        Stops propagation.  For fatal errors.
        '''
        agcls.evaluate_hresult(self.__dict__['_StopPropagation']())

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        '''
        Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients.
        '''
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DateElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        '''
        Current epoch expressed using the date format abbreviation specified.
        '''
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__['_DateString'](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry('{96E6BDF6-C1C6-4a50-9A93-6782BFF9FE5F}', IAgGatorPluginResultAttCtrl)
agcls.AgTypeNameMap['IAgGatorPluginResultAttCtrl'] = IAgGatorPluginResultAttCtrl
__all__.append('IAgGatorPluginResultAttCtrl')


class IAgGatorPluginEngineModel(object):
    '''
    Astrogator plugin engine model interface whose methods are called at certain events in the propagation process. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    '''
    def Name(self) -> str:
        '''
        Triggered to set the name of the plugin used in messages.
        '''
        raise STKPluginMethodNotImplementedError('Name was not implemented.')

    def Init(self, site:"IAgUtPluginSite") -> bool:
        '''
        Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin.
        '''
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def PrePropagate(self, resultState:"IAgGatorPluginResultState") -> bool:
        '''
        Triggered just before propagation starts. Use the input interface to access engine model settings.
        '''
        raise STKPluginMethodNotImplementedError('PrePropagate was not implemented.')

    def PreNextStep(self, resultState:"IAgGatorPluginResultState") -> bool:
        '''
        Triggered just before the next propagation step is attempted. Use the input interface to access engine model settings. Returning false will turn this callback off.
        '''
        raise STKPluginMethodNotImplementedError('PreNextStep was not implemented.')

    def Evaluate(self, resultEvalEngineModel:"IAgGatorPluginResultEvalEngineModel") -> bool:
        '''
        Triggered on every force model evaluation during the propagation of a step. Use the input interface to access engine model settings. Returning false will turn this callback off.
        '''
        raise STKPluginMethodNotImplementedError('Evaluate was not implemented.')

    def Free(self) -> None:
        '''
        Triggered just before the plugin is freed from use to allow for any additional cleanup.
        '''
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

__all__.append('IAgGatorPluginEngineModel')

class IAgGatorPluginAttCtrl(object):
    '''
    Astrogator plugin attitude controller interface whose methods are called at certain events in the propagation process. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    '''
    def Name(self) -> str:
        '''
        Triggered to set the name of the plugin used in messages.
        '''
        raise STKPluginMethodNotImplementedError('Name was not implemented.')

    def Init(self, site:"IAgUtPluginSite") -> bool:
        '''
        Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin.
        '''
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def PrePropagate(self, resultAttCtrl:"IAgGatorPluginResultAttCtrl") -> bool:
        '''
        Triggered just before propagation starts. Use the input interface to access attitude controller settings.
        '''
        raise STKPluginMethodNotImplementedError('PrePropagate was not implemented.')

    def PreNextStep(self, resultAttCtrl:"IAgGatorPluginResultAttCtrl") -> bool:
        '''
        Triggered just before the next propagation step is attempted. Use the input interface to access attitude controller settings. Returning false will turn this callback off.
        '''
        raise STKPluginMethodNotImplementedError('PreNextStep was not implemented.')

    def Evaluate(self, resultAttCtrl:"IAgGatorPluginResultAttCtrl") -> bool:
        '''
        Triggered on every force model evaluation during the propagation of a step. Use the input interface to access attitude controller settings. Returning false will turn this callback off.
        '''
        raise STKPluginMethodNotImplementedError('Evaluate was not implemented.')

    def Free(self) -> None:
        '''
        Triggered just before the plugin is freed from use to allow for any additional cleanup.
        '''
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

__all__.append('IAgGatorPluginAttCtrl')



class AgGatorPluginResultState(IAgGatorPluginResultState):
    '''
    Astrogator plugin class used to get state values
    '''
    def __init__(self, sourceObject=None):
        IAgGatorPluginResultState.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgGatorPluginResultState._private_init(self, pUnk)
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGatorPluginResultState._get_property(self, attrname) is not None: found_prop = IAgGatorPluginResultState._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgGatorPluginResultState.')
        
agcls.AgClassCatalog.add_catalog_entry('{55CC183B-F1DC-464E-B652-1366F5959234}', AgGatorPluginResultState)
__all__.append('AgGatorPluginResultState')


class AgGatorPluginResultEvalEngineModel(IAgGatorPluginResultEvalEngineModel):
    '''
    Astrogator plugin class used to get/set engine model settings during the propagation of a step
    '''
    def __init__(self, sourceObject=None):
        IAgGatorPluginResultEvalEngineModel.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgGatorPluginResultEvalEngineModel._private_init(self, pUnk)
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGatorPluginResultEvalEngineModel._get_property(self, attrname) is not None: found_prop = IAgGatorPluginResultEvalEngineModel._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgGatorPluginResultEvalEngineModel.')
        
agcls.AgClassCatalog.add_catalog_entry('{B98E0848-7BD4-4C6B-9260-19793ECB6EEA}', AgGatorPluginResultEvalEngineModel)
__all__.append('AgGatorPluginResultEvalEngineModel')


class AgGatorPluginResultAttCtrl(IAgGatorPluginResultAttCtrl):
    '''
    Astrogator plugin class used to get/set attitude controller settings during the propagation of a step
    '''
    def __init__(self, sourceObject=None):
        IAgGatorPluginResultAttCtrl.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgGatorPluginResultAttCtrl._private_init(self, pUnk)
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGatorPluginResultAttCtrl._get_property(self, attrname) is not None: found_prop = IAgGatorPluginResultAttCtrl._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgGatorPluginResultAttCtrl.')
        
agcls.AgClassCatalog.add_catalog_entry('{418797AC-061C-4574-8700-7FA73E02DD5F}', AgGatorPluginResultAttCtrl)
__all__.append('AgGatorPluginResultAttCtrl')



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
