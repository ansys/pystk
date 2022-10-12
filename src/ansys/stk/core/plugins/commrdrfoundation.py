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


from agi.stk12.plugins.attrautomation import *
from agi.stk12.plugins.utplugin import *
from agi.stk12.plugins.crdnplugin import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError('Valid STK object model classes are returned from STK methods and should not be created independently.')

class AgECRPolarizationRefAxis(IntEnum):
    """Enumeration of polarization reference axes."""
    # X Axis
    eCRPolRefXAxis = 1,
    # Y Axis
    eCRPolRefYAxis = 2,
    # Z Axis
    eCRPolRefZAxis = 3

agcls.AgTypeNameMap['AgECRPolarizationRefAxis'] = AgECRPolarizationRefAxis
__all__.append('AgECRPolarizationRefAxis')

class AgECRPolarizationType(IntEnum):
    """Enumeration of polarization types."""
    # Linear
    eCRLinearPol = 1,
    # Left-hand Circular
    eCRLHCPol = 2,
    # Right-hand Circular
    eCRRHCPol = 3,
    # Elliptical
    eCREllipticalPol = 4

agcls.AgTypeNameMap['AgECRPolarizationType'] = AgECRPolarizationType
__all__.append('AgECRPolarizationType')


class IAgCRPolarization(object):
    """Polarization object interface used to represent a signal polarization."""
    _uuid = '{AE821EF4-7233-4E11-B05D-C0807BB36901}'
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetType'] = _raise_uninitialized_error
        self.__dict__['_GetTiltAngle'] = _raise_uninitialized_error
        self.__dict__['_GetAxialRatio'] = _raise_uninitialized_error
        self.__dict__['_GetReferenceAxis'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgCRPolarization._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgCRPolarization from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgCRPolarization = agcom.GUID(IAgCRPolarization._uuid)
        vtable_offset_local = IAgCRPolarization._vtable_offset - 1
        self.__dict__['_GetType'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarization, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__['_GetTiltAngle'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarization, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAxialRatio'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarization, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_GetReferenceAxis'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarization, vtable_offset_local+4, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCRPolarization.__dict__ and type(IAgCRPolarization.__dict__[attrname]) == property:
            return IAgCRPolarization.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgCRPolarization.')
    
    @property
    def Type(self) -> "AgECRPolarizationType":
        """Gets the polarizatoin type."""
        with agmarshall.AgEnum_arg(AgECRPolarizationType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__['_GetType'](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    @property
    def TiltAngle(self) -> float:
        """Gets the tilt angle."""
        with agmarshall.DOUBLE_arg() as arg_pTiltAngle:
            agcls.evaluate_hresult(self.__dict__['_GetTiltAngle'](byref(arg_pTiltAngle.COM_val)))
            return arg_pTiltAngle.python_val

    @property
    def AxialRatio(self) -> float:
        """Gets the axial ratio."""
        with agmarshall.DOUBLE_arg() as arg_pAxialRatio:
            agcls.evaluate_hresult(self.__dict__['_GetAxialRatio'](byref(arg_pAxialRatio.COM_val)))
            return arg_pAxialRatio.python_val

    @property
    def ReferenceAxis(self) -> "AgECRPolarizationRefAxis":
        """Gets the reference axis"""
        with agmarshall.AgEnum_arg(AgECRPolarizationRefAxis) as arg_pReferenceAxis:
            agcls.evaluate_hresult(self.__dict__['_GetReferenceAxis'](byref(arg_pReferenceAxis.COM_val)))
            return arg_pReferenceAxis.python_val


agcls.AgClassCatalog.add_catalog_entry('{AE821EF4-7233-4E11-B05D-C0807BB36901}', IAgCRPolarization)
agcls.AgTypeNameMap['IAgCRPolarization'] = IAgCRPolarization
__all__.append('IAgCRPolarization')

class IAgCRPolarizationLinear(object):
    """Linear polarization object interface used to represent linear signal polarization."""
    _uuid = '{E5E3284C-8C6C-478B-92DF-E374A192AAED}'
    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_SetTiltAngle'] = _raise_uninitialized_error
        self.__dict__['_SetReferenceAxis'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgCRPolarizationLinear._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgCRPolarizationLinear from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgCRPolarizationLinear = agcom.GUID(IAgCRPolarizationLinear._uuid)
        vtable_offset_local = IAgCRPolarizationLinear._vtable_offset - 1
        self.__dict__['_SetTiltAngle'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarizationLinear, vtable_offset_local+1, agcom.DOUBLE)
        self.__dict__['_SetReferenceAxis'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarizationLinear, vtable_offset_local+2, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCRPolarizationLinear.__dict__ and type(IAgCRPolarizationLinear.__dict__[attrname]) == property:
            return IAgCRPolarizationLinear.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgCRPolarizationLinear.')
    
    @property
    def TiltAngle(self) -> None:
        """TiltAngle is a write-only property."""
        raise RuntimeError('TiltAngle is a write-only property.')


    @TiltAngle.setter
    def TiltAngle(self, tiltAngle:float) -> None:
        """Sets the tilt angle."""
        with agmarshall.DOUBLE_arg(tiltAngle) as arg_tiltAngle:
            agcls.evaluate_hresult(self.__dict__['_SetTiltAngle'](arg_tiltAngle.COM_val))

    @property
    def ReferenceAxis(self) -> None:
        """ReferenceAxis is a write-only property."""
        raise RuntimeError('ReferenceAxis is a write-only property.')


    @ReferenceAxis.setter
    def ReferenceAxis(self, referenceAxis:"AgECRPolarizationRefAxis") -> None:
        """Sets the reference axis"""
        with agmarshall.AgEnum_arg(AgECRPolarizationRefAxis, referenceAxis) as arg_referenceAxis:
            agcls.evaluate_hresult(self.__dict__['_SetReferenceAxis'](arg_referenceAxis.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{E5E3284C-8C6C-478B-92DF-E374A192AAED}', IAgCRPolarizationLinear)
agcls.AgTypeNameMap['IAgCRPolarizationLinear'] = IAgCRPolarizationLinear
__all__.append('IAgCRPolarizationLinear')

class IAgCRPolarizationElliptical(object):
    """Elliptical polarization object interface used to represent elliptical signal polarization."""
    _uuid = '{698655C0-9BB6-4D8F-A785-9E0ED2880D17}'
    _num_methods = 3
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_SetTiltAngle'] = _raise_uninitialized_error
        self.__dict__['_SetAxialRatio'] = _raise_uninitialized_error
        self.__dict__['_SetReferenceAxis'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgCRPolarizationElliptical._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgCRPolarizationElliptical from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgCRPolarizationElliptical = agcom.GUID(IAgCRPolarizationElliptical._uuid)
        vtable_offset_local = IAgCRPolarizationElliptical._vtable_offset - 1
        self.__dict__['_SetTiltAngle'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarizationElliptical, vtable_offset_local+1, agcom.DOUBLE)
        self.__dict__['_SetAxialRatio'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarizationElliptical, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__['_SetReferenceAxis'] = IAGFUNCTYPE(pUnk, IID_IAgCRPolarizationElliptical, vtable_offset_local+3, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCRPolarizationElliptical.__dict__ and type(IAgCRPolarizationElliptical.__dict__[attrname]) == property:
            return IAgCRPolarizationElliptical.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgCRPolarizationElliptical.')
    
    @property
    def TiltAngle(self) -> None:
        """TiltAngle is a write-only property."""
        raise RuntimeError('TiltAngle is a write-only property.')


    @TiltAngle.setter
    def TiltAngle(self, tiltAngle:float) -> None:
        """Sets the tilt angle."""
        with agmarshall.DOUBLE_arg(tiltAngle) as arg_tiltAngle:
            agcls.evaluate_hresult(self.__dict__['_SetTiltAngle'](arg_tiltAngle.COM_val))

    @property
    def AxialRatio(self) -> None:
        """AxialRatio is a write-only property."""
        raise RuntimeError('AxialRatio is a write-only property.')


    @AxialRatio.setter
    def AxialRatio(self, axialRatio:float) -> None:
        """Sets the axial ratio."""
        with agmarshall.DOUBLE_arg(axialRatio) as arg_axialRatio:
            agcls.evaluate_hresult(self.__dict__['_SetAxialRatio'](arg_axialRatio.COM_val))

    @property
    def ReferenceAxis(self) -> None:
        """ReferenceAxis is a write-only property."""
        raise RuntimeError('ReferenceAxis is a write-only property.')


    @ReferenceAxis.setter
    def ReferenceAxis(self, referenceAxis:"AgECRPolarizationRefAxis") -> None:
        """Sets the reference axis"""
        with agmarshall.AgEnum_arg(AgECRPolarizationRefAxis, referenceAxis) as arg_referenceAxis:
            agcls.evaluate_hresult(self.__dict__['_SetReferenceAxis'](arg_referenceAxis.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{698655C0-9BB6-4D8F-A785-9E0ED2880D17}', IAgCRPolarizationElliptical)
agcls.AgTypeNameMap['IAgCRPolarizationElliptical'] = IAgCRPolarizationElliptical
__all__.append('IAgCRPolarizationElliptical')

class IAgCRSignal(object):
    """Signal object interface used to represent an electromagnetic signal."""
    _uuid = '{AD51AE42-C2D9-4F06-BD0D-D4D5B895F117}'
    _num_methods = 13
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetTime'] = _raise_uninitialized_error
        self.__dict__['_GetFrequency'] = _raise_uninitialized_error
        self.__dict__['_SetFrequency'] = _raise_uninitialized_error
        self.__dict__['_GetUpperBandLimit'] = _raise_uninitialized_error
        self.__dict__['_SetUpperBandLimit'] = _raise_uninitialized_error
        self.__dict__['_GetLowerBandLimit'] = _raise_uninitialized_error
        self.__dict__['_SetLowerBandLimit'] = _raise_uninitialized_error
        self.__dict__['_GetPower'] = _raise_uninitialized_error
        self.__dict__['_SetPower'] = _raise_uninitialized_error
        self.__dict__['_GetPolarization'] = _raise_uninitialized_error
        self.__dict__['_SetPolarization'] = _raise_uninitialized_error
        self.__dict__['_ComputePolLoss'] = _raise_uninitialized_error
        self.__dict__['_ComputePolRotationAngle'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgCRSignal._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgCRSignal from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgCRSignal = agcom.GUID(IAgCRSignal._uuid)
        vtable_offset_local = IAgCRSignal._vtable_offset - 1
        self.__dict__['_GetTime'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__['_GetFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_SetFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+3, agcom.DOUBLE)
        self.__dict__['_GetUpperBandLimit'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_SetUpperBandLimit'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+5, agcom.DOUBLE)
        self.__dict__['_GetLowerBandLimit'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_SetLowerBandLimit'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+7, agcom.DOUBLE)
        self.__dict__['_GetPower'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_SetPower'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+9, agcom.DOUBLE)
        self.__dict__['_GetPolarization'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+10, POINTER(agcom.PVOID))
        self.__dict__['_SetPolarization'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+11, agcom.PVOID)
        self.__dict__['_ComputePolLoss'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+12, agcom.PVOID, POINTER(agcom.DOUBLE))
        self.__dict__['_ComputePolRotationAngle'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignal, vtable_offset_local+13, agcom.PVOID, POINTER(agcom.DOUBLE))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCRSignal.__dict__ and type(IAgCRSignal.__dict__[attrname]) == property:
            return IAgCRSignal.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgCRSignal.')
    
    @property
    def Time(self) -> float:
        """Gets the signal time in epoch seconds."""
        with agmarshall.DOUBLE_arg() as arg_pTime:
            agcls.evaluate_hresult(self.__dict__['_GetTime'](byref(arg_pTime.COM_val)))
            return arg_pTime.python_val

    @property
    def Frequency(self) -> float:
        """Gets or sets the signal frequency in Hz."""
        with agmarshall.DOUBLE_arg() as arg_pFrequency:
            agcls.evaluate_hresult(self.__dict__['_GetFrequency'](byref(arg_pFrequency.COM_val)))
            return arg_pFrequency.python_val

    @Frequency.setter
    def Frequency(self, frequency:float) -> None:
        """Gets or sets the signal frequency in Hz."""
        with agmarshall.DOUBLE_arg(frequency) as arg_frequency:
            agcls.evaluate_hresult(self.__dict__['_SetFrequency'](arg_frequency.COM_val))

    @property
    def UpperBandLimit(self) -> float:
        """Gets or sets the signal upper bandwidth limit in Hz."""
        with agmarshall.DOUBLE_arg() as arg_pUpperLimit:
            agcls.evaluate_hresult(self.__dict__['_GetUpperBandLimit'](byref(arg_pUpperLimit.COM_val)))
            return arg_pUpperLimit.python_val

    @UpperBandLimit.setter
    def UpperBandLimit(self, upperLimit:float) -> None:
        """Gets or sets the signal upper bandwidth limit in Hz."""
        with agmarshall.DOUBLE_arg(upperLimit) as arg_upperLimit:
            agcls.evaluate_hresult(self.__dict__['_SetUpperBandLimit'](arg_upperLimit.COM_val))

    @property
    def LowerBandLimit(self) -> float:
        """Gets or sets the signal lower bandwidth limit in Hz."""
        with agmarshall.DOUBLE_arg() as arg_pLowerLimit:
            agcls.evaluate_hresult(self.__dict__['_GetLowerBandLimit'](byref(arg_pLowerLimit.COM_val)))
            return arg_pLowerLimit.python_val

    @LowerBandLimit.setter
    def LowerBandLimit(self, lowerLimit:float) -> None:
        """Gets or sets the signal lower bandwidth limit in Hz."""
        with agmarshall.DOUBLE_arg(lowerLimit) as arg_lowerLimit:
            agcls.evaluate_hresult(self.__dict__['_SetLowerBandLimit'](arg_lowerLimit.COM_val))

    @property
    def Power(self) -> float:
        """Gets or sets the signal power in Watts."""
        with agmarshall.DOUBLE_arg() as arg_pPower:
            agcls.evaluate_hresult(self.__dict__['_GetPower'](byref(arg_pPower.COM_val)))
            return arg_pPower.python_val

    @Power.setter
    def Power(self, power:float) -> None:
        """Gets or sets the signal power in Watts."""
        with agmarshall.DOUBLE_arg(power) as arg_power:
            agcls.evaluate_hresult(self.__dict__['_SetPower'](arg_power.COM_val))

    @property
    def Polarization(self) -> "IAgCRPolarization":
        """Gets or sets the signal polarization"""
        with agmarshall.AgInterface_out_arg() as arg_ppPolarization:
            agcls.evaluate_hresult(self.__dict__['_GetPolarization'](byref(arg_ppPolarization.COM_val)))
            return arg_ppPolarization.python_val

    @Polarization.setter
    def Polarization(self, polarization:"IAgCRPolarization") -> None:
        """Gets or sets the signal polarization"""
        with agmarshall.AgInterface_in_arg(polarization, IAgCRPolarization) as arg_polarization:
            agcls.evaluate_hresult(self.__dict__['_SetPolarization'](arg_polarization.COM_val))

    def ComputePolLoss(self, rcvSidePolarization:"IAgCRPolarization") -> float:
        """Computes the rotation angle for the receive side polarization."""
        with agmarshall.AgInterface_in_arg(rcvSidePolarization, IAgCRPolarization) as arg_rcvSidePolarization, \
             agmarshall.DOUBLE_arg() as arg_pPolLoss:
            agcls.evaluate_hresult(self.__dict__['_ComputePolLoss'](arg_rcvSidePolarization.COM_val, byref(arg_pPolLoss.COM_val)))
            return arg_pPolLoss.python_val

    def ComputePolRotationAngle(self, rcvSidePolarization:"IAgCRPolarization") -> float:
        """Computes the rotation angle for the receive side polarization."""
        with agmarshall.AgInterface_in_arg(rcvSidePolarization, IAgCRPolarization) as arg_rcvSidePolarization, \
             agmarshall.DOUBLE_arg() as arg_pRotationAngle:
            agcls.evaluate_hresult(self.__dict__['_ComputePolRotationAngle'](arg_rcvSidePolarization.COM_val, byref(arg_pRotationAngle.COM_val)))
            return arg_pRotationAngle.python_val


agcls.AgClassCatalog.add_catalog_entry('{AD51AE42-C2D9-4F06-BD0D-D4D5B895F117}', IAgCRSignal)
agcls.AgTypeNameMap['IAgCRSignal'] = IAgCRSignal
__all__.append('IAgCRSignal')

class IAgCRSignalCollection(object):
    """Interface implemented by a collection of signal objects."""
    _uuid = '{3E1095D7-D4F2-496C-B27C-0E1F23FCCA54}'
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetCount'] = _raise_uninitialized_error
        self.__dict__['_Item'] = _raise_uninitialized_error
        self.__dict__['_Get_NewEnum'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgCRSignalCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgCRSignalCollection from source object.')
        self.__dict__['enumerator'] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgCRSignalCollection = agcom.GUID(IAgCRSignalCollection._uuid)
        vtable_offset_local = IAgCRSignalCollection._vtable_offset - 1
        self.__dict__['_GetCount'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignalCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__['_Item'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignalCollection, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__['_Get_NewEnum'] = IAGFUNCTYPE(pUnk, IID_IAgCRSignalCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCRSignalCollection.__dict__ and type(IAgCRSignalCollection.__dict__[attrname]) == property:
            return IAgCRSignalCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgCRSignalCollection.')
    def __iter__(self):
        self.__dict__['enumerator'] = self._NewEnum
        self.__dict__['enumerator'].Reset()
        return self
    def __next__(self) -> "IAgCRSignal":
        if self.__dict__['enumerator'] is None:
            raise StopIteration
        nextval = self.__dict__['enumerator'].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    @property
    def Count(self) -> int:
        """Returns the number of elements in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__['_GetCount'](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def Item(self, index:int) -> "IAgCRSignal":
        """Given an index, returns an element in the collection."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppSignal:
            agcls.evaluate_hresult(self.__dict__['_Item'](arg_index.COM_val, byref(arg_ppSignal.COM_val)))
            return arg_ppSignal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an enumerator that can iterate through the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__['_Get_NewEnum'](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry('{3E1095D7-D4F2-496C-B27C-0E1F23FCCA54}', IAgCRSignalCollection)
agcls.AgTypeNameMap['IAgCRSignalCollection'] = IAgCRSignalCollection
__all__.append('IAgCRSignalCollection')



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
