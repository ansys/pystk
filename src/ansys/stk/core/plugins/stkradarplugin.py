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


from ..plugins.attrautomation import *
from ..plugins.utplugin import *
from ..plugins.crdnplugin import *
from ..plugins.commrdrfoundation import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgEStkRadarValidSystems(IntEnum):
    """Enumeration of valid radar systems."""
    # All radar systems.
    eStkRadarAllSystems = 1,
    # Monostatic radar system only.
    eStkRadarMonostaticSystemsOnly = 2,
    # Bistatic radar system only.
    eStkRadarBistaticSystemsOnly = 3

agcls.AgTypeNameMap["AgEStkRadarValidSystems"] = AgEStkRadarValidSystems
__all__.append("AgEStkRadarValidSystems")

class AgEStkRadarPosVelProviderRole(IntEnum):
    """Enumeration of the position and velocity providers roles."""
    # Transmitter
    eStkRadarTransmitterPosVelRole = 1,
    # Receiver
    eStkRadarReceiverPosVelRole = 2,
    # Target
    eStkRadarTargetPosVelRole = 3,
    # Clutter Patch
    eStkRadarClutterPatchPosVelRole = 4

agcls.AgTypeNameMap["AgEStkRadarPosVelProviderRole"] = AgEStkRadarPosVelProviderRole
__all__.append("AgEStkRadarPosVelProviderRole")

class AgEStkRadarTerrainInterpMethod(IntEnum):
    """Enumeration of terrain interpolation methods."""
    # Bilinear Interpolation
    eStkRadarBilinearTerrainInterp = 1,
    # Highest Post
    eStkRadarHighestPostTerrainInterp = 2,
    # Tri-Planar
    eStkRadarTriPlanarTerrainInterp = 3

agcls.AgTypeNameMap["AgEStkRadarTerrainInterpMethod"] = AgEStkRadarTerrainInterpMethod
__all__.append("AgEStkRadarTerrainInterpMethod")


class IAgStkRadarCBIntersectComputeParams(object):
    """Interface implemented by an object that represents the input parameters for a central body intersect computation."""
    _uuid = "{7C5B738D-7541-4881-A337-2731061BDB2E}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetBasePositionCBF"] = _raise_uninitialized_error
        self.__dict__["_GetBasePositionCBFArray"] = _raise_uninitialized_error
        self.__dict__["_SetBasePositionCBF"] = _raise_uninitialized_error
        self.__dict__["_GetDirectionCBF"] = _raise_uninitialized_error
        self.__dict__["_GetDirectionCBFArray"] = _raise_uninitialized_error
        self.__dict__["_SetDirectionCBF"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarCBIntersectComputeParams._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarCBIntersectComputeParams from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarCBIntersectComputeParams = agcom.GUID(IAgStkRadarCBIntersectComputeParams._uuid)
        vtable_offset_local = IAgStkRadarCBIntersectComputeParams._vtable_offset - 1
        self.__dict__["_GetBasePositionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeParams, vtable_offset_local+1, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetBasePositionCBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeParams, vtable_offset_local+2, POINTER(agcom.SAFEARRAY))
        self.__dict__["_SetBasePositionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeParams, vtable_offset_local+3, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_GetDirectionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeParams, vtable_offset_local+4, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetDirectionCBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeParams, vtable_offset_local+5, POINTER(agcom.SAFEARRAY))
        self.__dict__["_SetDirectionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeParams, vtable_offset_local+6, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarCBIntersectComputeParams.__dict__ and type(IAgStkRadarCBIntersectComputeParams.__dict__[attrname]) == property:
            return IAgStkRadarCBIntersectComputeParams.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarCBIntersectComputeParams.")
    
    def GetBasePositionCBF(self) -> typing.Tuple[float, float, float]:
        """Gets the base position vector in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetBasePositionCBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def BasePositionCBFArray(self) -> list:
        """Gets the base position vector in central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetBasePositionCBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def SetBasePositionCBF(self, x:float, y:float, z:float) -> None:
        """Sets the base position vector in the central body fixed frame."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetBasePositionCBF"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def GetDirectionCBF(self) -> typing.Tuple[float, float, float]:
        """Gets the direction vector in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetDirectionCBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def DirectionCBFArray(self) -> list:
        """Gets the direction vector in the central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetDirectionCBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def SetDirectionCBF(self, x:float, y:float, z:float) -> None:
        """Sets the direction vector in the central body fixed frame."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetDirectionCBF"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{7C5B738D-7541-4881-A337-2731061BDB2E}", IAgStkRadarCBIntersectComputeParams)
agcls.AgTypeNameMap["IAgStkRadarCBIntersectComputeParams"] = IAgStkRadarCBIntersectComputeParams
__all__.append("IAgStkRadarCBIntersectComputeParams")

class IAgStkRadarCBIntersectComputeResult(object):
    """Interface implemented by an object that represents the result of a central body computation."""
    _uuid = "{FA9A261B-0C93-41B8-A58C-B49D6DEDE879}"
    _num_methods = 11
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIntersectionFound"] = _raise_uninitialized_error
        self.__dict__["_GetIntercept1CBF"] = _raise_uninitialized_error
        self.__dict__["_GetIntercept1CBFArray"] = _raise_uninitialized_error
        self.__dict__["_GetIntercept2CBF"] = _raise_uninitialized_error
        self.__dict__["_GetIntercept2CBFArray"] = _raise_uninitialized_error
        self.__dict__["_GetMultiplier1"] = _raise_uninitialized_error
        self.__dict__["_GetMultiplier2"] = _raise_uninitialized_error
        self.__dict__["_GetBasePositionCBF"] = _raise_uninitialized_error
        self.__dict__["_GetBasePositionCBFArray"] = _raise_uninitialized_error
        self.__dict__["_GetDirectionCBF"] = _raise_uninitialized_error
        self.__dict__["_GetDirectionCBFArray"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarCBIntersectComputeResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarCBIntersectComputeResult from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarCBIntersectComputeResult = agcom.GUID(IAgStkRadarCBIntersectComputeResult._uuid)
        vtable_offset_local = IAgStkRadarCBIntersectComputeResult._vtable_offset - 1
        self.__dict__["_GetIntersectionFound"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetIntercept1CBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+2, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetIntercept1CBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+3, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetIntercept2CBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+4, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetIntercept2CBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+5, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetMultiplier1"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__["_GetMultiplier2"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_GetBasePositionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+8, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetBasePositionCBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+9, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetDirectionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+10, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetDirectionCBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarCBIntersectComputeResult, vtable_offset_local+11, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarCBIntersectComputeResult.__dict__ and type(IAgStkRadarCBIntersectComputeResult.__dict__[attrname]) == property:
            return IAgStkRadarCBIntersectComputeResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarCBIntersectComputeResult.")
    
    @property
    def IntersectionFound(self) -> bool:
        """Gets the intersection found indicator."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIntersectionFound:
            agcls.evaluate_hresult(self.__dict__["_GetIntersectionFound"](byref(arg_pIntersectionFound.COM_val)))
            return arg_pIntersectionFound.python_val

    def GetIntercept1CBF(self) -> typing.Tuple[float, float, float]:
        """Gets the position vector of the first point of intersection in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetIntercept1CBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def Intercept1CBFArray(self) -> list:
        """Gets the position vector  of the first point of intersection in the central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetIntercept1CBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetIntercept2CBF(self) -> typing.Tuple[float, float, float]:
        """Gets the position vector of the second point of intersection in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetIntercept2CBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def Intercept2CBFArray(self) -> list:
        """Gets the position vector of the second point of the intersection in the central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetIntercept2CBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    @property
    def Multiplier1(self) -> float:
        """Gets the first multiplier."""
        with agmarshall.DOUBLE_arg() as arg_pMultiplier1:
            agcls.evaluate_hresult(self.__dict__["_GetMultiplier1"](byref(arg_pMultiplier1.COM_val)))
            return arg_pMultiplier1.python_val

    @property
    def Multiplier2(self) -> float:
        """Gets the second multiplier."""
        with agmarshall.DOUBLE_arg() as arg_pMultiplier2:
            agcls.evaluate_hresult(self.__dict__["_GetMultiplier2"](byref(arg_pMultiplier2.COM_val)))
            return arg_pMultiplier2.python_val

    def GetBasePositionCBF(self) -> typing.Tuple[float, float, float]:
        """Gets the base position vector in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetBasePositionCBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def BasePositionCBFArray(self) -> list:
        """Gets the base position vector in the central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetBasePositionCBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetDirectionCBF(self) -> typing.Tuple[float, float, float]:
        """Gets the direction vector in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetDirectionCBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def DirectionCBFArray(self) -> list:
        """Gets the direction vector in the central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetDirectionCBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{FA9A261B-0C93-41B8-A58C-B49D6DEDE879}", IAgStkRadarCBIntersectComputeResult)
agcls.AgTypeNameMap["IAgStkRadarCBIntersectComputeResult"] = IAgStkRadarCBIntersectComputeResult
__all__.append("IAgStkRadarCBIntersectComputeResult")

class IAgStkRadarPosVelProvider(object):
    """Interface implemented by an object that provides the position and velocity for an STK radar object or radar target object."""
    _uuid = "{E675D82D-945C-46F9-9E26-0632D13884D4}"
    _num_methods = 34
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCurrentTime"] = _raise_uninitialized_error
        self.__dict__["_GetVelocityCBF"] = _raise_uninitialized_error
        self.__dict__["_GetVelocityCBFArray"] = _raise_uninitialized_error
        self.__dict__["_GetPositionCBF"] = _raise_uninitialized_error
        self.__dict__["_GetPositionCBFArray"] = _raise_uninitialized_error
        self.__dict__["_GetPositionLLA"] = _raise_uninitialized_error
        self.__dict__["_GetPositionLLAArray"] = _raise_uninitialized_error
        self.__dict__["_GetLocalRadiusDetic"] = _raise_uninitialized_error
        self.__dict__["_GetLocalRadiusCentric"] = _raise_uninitialized_error
        self.__dict__["_GetSurfaceNormalDetic"] = _raise_uninitialized_error
        self.__dict__["_GetSurfaceNormalDeticArray"] = _raise_uninitialized_error
        self.__dict__["_GetSurfaceNormalCentric"] = _raise_uninitialized_error
        self.__dict__["_GetSurfaceNormalCentricArray"] = _raise_uninitialized_error
        self.__dict__["_GetTerrainHeight"] = _raise_uninitialized_error
        self.__dict__["_GetTerrainHeightForLatLon"] = _raise_uninitialized_error
        self.__dict__["_ComputeLocalRadiusDetic"] = _raise_uninitialized_error
        self.__dict__["_ComputeLocalRadiusCentric"] = _raise_uninitialized_error
        self.__dict__["_ComputeSurfaceNormalDetic"] = _raise_uninitialized_error
        self.__dict__["_ComputeSurfaceNormalDeticArray"] = _raise_uninitialized_error
        self.__dict__["_ComputeSurfaceNormalCentric"] = _raise_uninitialized_error
        self.__dict__["_ComputeSurfaceNormalCentricArray"] = _raise_uninitialized_error
        self.__dict__["_ComputeCentralBodyIntersect"] = _raise_uninitialized_error
        self.__dict__["_ConvertCBFCartesianToLLA"] = _raise_uninitialized_error
        self.__dict__["_ConvertCBFCartesianToLLAArray"] = _raise_uninitialized_error
        self.__dict__["_ConvertLLAToCBFCartesian"] = _raise_uninitialized_error
        self.__dict__["_ConvertLLAToCBFCartesianArray"] = _raise_uninitialized_error
        self.__dict__["_ConvertCBFCartesianToVVLHCartesian"] = _raise_uninitialized_error
        self.__dict__["_ConvertCBFCartesianToVVLHCartesianArray"] = _raise_uninitialized_error
        self.__dict__["_ConvertBodyCartesianToCBFCartesian"] = _raise_uninitialized_error
        self.__dict__["_ConvertBodyCartesianToCBFCartesianArray"] = _raise_uninitialized_error
        self.__dict__["_ConvertCBFCartesianToBodyCartesian"] = _raise_uninitialized_error
        self.__dict__["_ConvertCBFCartesianToBodyCartesianArray"] = _raise_uninitialized_error
        self.__dict__["_GetRole"] = _raise_uninitialized_error
        self.__dict__["_ComputeCentralBodyIntersectInCBF"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarPosVelProvider._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarPosVelProvider from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarPosVelProvider = agcom.GUID(IAgStkRadarPosVelProvider._uuid)
        vtable_offset_local = IAgStkRadarPosVelProvider._vtable_offset - 1
        self.__dict__["_GetCurrentTime"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_GetVelocityCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+2, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetVelocityCBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+3, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetPositionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+4, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetPositionCBFArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+5, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetPositionLLA"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+6, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetPositionLLAArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+7, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetLocalRadiusDetic"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__["_GetLocalRadiusCentric"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__["_GetSurfaceNormalDetic"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+10, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetSurfaceNormalDeticArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+11, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetSurfaceNormalCentric"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+12, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetSurfaceNormalCentricArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+13, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetTerrainHeight"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+14, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__["_GetTerrainHeightForLatLon"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+15, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__["_ComputeLocalRadiusDetic"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+16, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE))
        self.__dict__["_ComputeLocalRadiusCentric"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+17, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE))
        self.__dict__["_ComputeSurfaceNormalDetic"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+18, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_ComputeSurfaceNormalDeticArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+19, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_ComputeSurfaceNormalCentric"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+20, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_ComputeSurfaceNormalCentricArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+21, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_ComputeCentralBodyIntersect"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+22, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_ConvertCBFCartesianToLLA"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+23, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_ConvertCBFCartesianToLLAArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+24, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_ConvertLLAToCBFCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+25, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_ConvertLLAToCBFCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+26, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_ConvertCBFCartesianToVVLHCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+27, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_ConvertCBFCartesianToVVLHCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+28, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_ConvertBodyCartesianToCBFCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+29, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_ConvertBodyCartesianToCBFCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+30, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_ConvertCBFCartesianToBodyCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+31, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_ConvertCBFCartesianToBodyCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+32, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetRole"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+33, POINTER(agcom.LONG))
        self.__dict__["_ComputeCentralBodyIntersectInCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarPosVelProvider, vtable_offset_local+34, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarPosVelProvider.__dict__ and type(IAgStkRadarPosVelProvider.__dict__[attrname]) == property:
            return IAgStkRadarPosVelProvider.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarPosVelProvider.")
    
    @property
    def CurrentTime(self) -> float:
        """Gets the current time in EpSec."""
        with agmarshall.DOUBLE_arg() as arg_pCurrentTime:
            agcls.evaluate_hresult(self.__dict__["_GetCurrentTime"](byref(arg_pCurrentTime.COM_val)))
            return arg_pCurrentTime.python_val

    def GetVelocityCBF(self) -> typing.Tuple[float, float, float]:
        """Gets velocity in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetVelocityCBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def VelocityCBFArray(self) -> list:
        """Gets velocity in the central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetVelocityCBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetPositionCBF(self) -> typing.Tuple[float, float, float]:
        """Gets position in the central body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetPositionCBF"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def PositionCBFArray(self) -> list:
        """Gets position in the central body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetPositionCBFArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetPositionLLA(self) -> typing.Tuple[float, float, float]:
        """Gets position in latitude, longitude, and altitude."""
        with agmarshall.DOUBLE_arg() as arg_latitude, \
             agmarshall.DOUBLE_arg() as arg_longitude, \
             agmarshall.DOUBLE_arg() as arg_altitude:
            agcls.evaluate_hresult(self.__dict__["_GetPositionLLA"](byref(arg_latitude.COM_val), byref(arg_longitude.COM_val), byref(arg_altitude.COM_val)))
            return arg_latitude.python_val, arg_longitude.python_val, arg_altitude.python_val

    @property
    def PositionLLAArray(self) -> list:
        """Gets position in latitude, longitude, and altitude as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetPositionLLAArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    @property
    def LocalRadiusDetic(self) -> float:
        """Gets the central body radius detic using the position/velocity provider's current latitude and longitude."""
        with agmarshall.DOUBLE_arg() as arg_pLocalRadiusDetic:
            agcls.evaluate_hresult(self.__dict__["_GetLocalRadiusDetic"](byref(arg_pLocalRadiusDetic.COM_val)))
            return arg_pLocalRadiusDetic.python_val

    @property
    def LocalRadiusCentric(self) -> float:
        """Gets the central body radius centric using the position/velocity provider's current latitude and longitude."""
        with agmarshall.DOUBLE_arg() as arg_pLocalRadiusCentric:
            agcls.evaluate_hresult(self.__dict__["_GetLocalRadiusCentric"](byref(arg_pLocalRadiusCentric.COM_val)))
            return arg_pLocalRadiusCentric.python_val

    def GetSurfaceNormalDetic(self) -> typing.Tuple[float, float, float]:
        """Gets the surface normal detic."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetSurfaceNormalDetic"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def SurfaceNormalDeticArray(self) -> list:
        """Gets the surface normal detic as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetSurfaceNormalDeticArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetSurfaceNormalCentric(self) -> typing.Tuple[float, float, float]:
        """Gets the surface normal centric as an array."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetSurfaceNormalCentric"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def SurfaceNormalCentricArray(self) -> list:
        """Gets the surface normal centric as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetSurfaceNormalCentricArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetTerrainHeight(self, interpMethod:"AgEStkRadarTerrainInterpMethod") -> float:
        """Gets the terrain height."""
        with agmarshall.AgEnum_arg(AgEStkRadarTerrainInterpMethod, interpMethod) as arg_interpMethod, \
             agmarshall.DOUBLE_arg() as arg_pTerrainHeight:
            agcls.evaluate_hresult(self.__dict__["_GetTerrainHeight"](arg_interpMethod.COM_val, byref(arg_pTerrainHeight.COM_val)))
            return arg_pTerrainHeight.python_val

    def GetTerrainHeightForLatLon(self, latitude:float, longitude:float, interpMethod:"AgEStkRadarTerrainInterpMethod") -> float:
        """Gets the terrain height for a specified latitude and longitude."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.AgEnum_arg(AgEStkRadarTerrainInterpMethod, interpMethod) as arg_interpMethod, \
             agmarshall.DOUBLE_arg() as arg_pTerrainHeight:
            agcls.evaluate_hresult(self.__dict__["_GetTerrainHeightForLatLon"](arg_latitude.COM_val, arg_longitude.COM_val, arg_interpMethod.COM_val, byref(arg_pTerrainHeight.COM_val)))
            return arg_pTerrainHeight.python_val

    def ComputeLocalRadiusDetic(self, latitude:float, longitude:float) -> float:
        """Computes the central body radius detic for a given latitude and longitude."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg() as arg_pLocalRadiusDetic:
            agcls.evaluate_hresult(self.__dict__["_ComputeLocalRadiusDetic"](arg_latitude.COM_val, arg_longitude.COM_val, byref(arg_pLocalRadiusDetic.COM_val)))
            return arg_pLocalRadiusDetic.python_val

    def ComputeLocalRadiusCentric(self, latitude:float, longitude:float) -> float:
        """Computes the central body radius centric for a given latitude and longitude."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg() as arg_pLocalRadiusCentric:
            agcls.evaluate_hresult(self.__dict__["_ComputeLocalRadiusCentric"](arg_latitude.COM_val, arg_longitude.COM_val, byref(arg_pLocalRadiusCentric.COM_val)))
            return arg_pLocalRadiusCentric.python_val

    def ComputeSurfaceNormalDetic(self, latitude:float, longitude:float) -> typing.Tuple[float, float, float]:
        """Computes the surface normal detic vector for a given latitude and longitude."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_ComputeSurfaceNormalDetic"](arg_latitude.COM_val, arg_longitude.COM_val, byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    def ComputeSurfaceNormalDeticArray(self, latitude:float, longitude:float) -> list:
        """Computes the surface normal detic vector for a given latitude and longitude as an array."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ComputeSurfaceNormalDeticArray"](arg_latitude.COM_val, arg_longitude.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def ComputeSurfaceNormalCentric(self, latitude:float, longitude:float) -> typing.Tuple[float, float, float]:
        """Computes the surface normal centric vector for a given latitude and longitude."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_ComputeSurfaceNormalCentric"](arg_latitude.COM_val, arg_longitude.COM_val, byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    def ComputeSurfaceNormalCentricArray(self, latitude:float, longitude:float) -> list:
        """Computes the surface normal centric vector for a given latitude and longitude as an array."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ComputeSurfaceNormalCentricArray"](arg_latitude.COM_val, arg_longitude.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def ConvertCBFCartesianToLLA(self, x:float, y:float, z:float) -> typing.Tuple[float, float, float]:
        """Converts central body fixed cartesian to latitude, longitude, and altitude."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg() as arg_latitude, \
             agmarshall.DOUBLE_arg() as arg_longitude, \
             agmarshall.DOUBLE_arg() as arg_altitude:
            agcls.evaluate_hresult(self.__dict__["_ConvertCBFCartesianToLLA"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_latitude.COM_val), byref(arg_longitude.COM_val), byref(arg_altitude.COM_val)))
            return arg_latitude.python_val, arg_longitude.python_val, arg_altitude.python_val

    def ConvertCBFCartesianToLLAArray(self, x:float, y:float, z:float) -> list:
        """Converts central body fixed cartesian to latitude, longitude, and altitude as an array."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ConvertCBFCartesianToLLAArray"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def ConvertLLAToCBFCartesian(self, latitude:float, longitude:float, altitude:float) -> typing.Tuple[float, float, float]:
        """Converts latitude, longitude, and altitude to central body fixed cartesian."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg(altitude) as arg_altitude, \
             agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_ConvertLLAToCBFCartesian"](arg_latitude.COM_val, arg_longitude.COM_val, arg_altitude.COM_val, byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    def ConvertLLAToCBFCartesianArray(self, latitude:float, longitude:float, altitude:float) -> list:
        """Converts latitude, longitude, and altitude to central body fixed cartesian as an array."""
        with agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg(altitude) as arg_altitude, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ConvertLLAToCBFCartesianArray"](arg_latitude.COM_val, arg_longitude.COM_val, arg_altitude.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def ConvertCBFCartesianToVVLHCartesian(self, xCbf:float, yCbf:float, zCbf:float) -> typing.Tuple[float, float, float]:
        """Converts a central body fixed cartesian into the VVLA frame."""
        with agmarshall.DOUBLE_arg(xCbf) as arg_xCbf, \
             agmarshall.DOUBLE_arg(yCbf) as arg_yCbf, \
             agmarshall.DOUBLE_arg(zCbf) as arg_zCbf, \
             agmarshall.DOUBLE_arg() as arg_xVvlh, \
             agmarshall.DOUBLE_arg() as arg_yVvlh, \
             agmarshall.DOUBLE_arg() as arg_zVvlh:
            agcls.evaluate_hresult(self.__dict__["_ConvertCBFCartesianToVVLHCartesian"](arg_xCbf.COM_val, arg_yCbf.COM_val, arg_zCbf.COM_val, byref(arg_xVvlh.COM_val), byref(arg_yVvlh.COM_val), byref(arg_zVvlh.COM_val)))
            return arg_xVvlh.python_val, arg_yVvlh.python_val, arg_zVvlh.python_val

    def ConvertCBFCartesianToVVLHCartesianArray(self, xCbf:float, yCbf:float, zCbf:float) -> list:
        """Converts a central body fixed cartesian into the VVLA frame as an array."""
        with agmarshall.DOUBLE_arg(xCbf) as arg_xCbf, \
             agmarshall.DOUBLE_arg(yCbf) as arg_yCbf, \
             agmarshall.DOUBLE_arg(zCbf) as arg_zCbf, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ConvertCBFCartesianToVVLHCartesianArray"](arg_xCbf.COM_val, arg_yCbf.COM_val, arg_zCbf.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def ConvertBodyCartesianToCBFCartesian(self, xBody:float, yBody:float, zBody:float) -> typing.Tuple[float, float, float]:
        """Converts a vector in body coordinates into CBF fixed coordinates"""
        with agmarshall.DOUBLE_arg(xBody) as arg_xBody, \
             agmarshall.DOUBLE_arg(yBody) as arg_yBody, \
             agmarshall.DOUBLE_arg(zBody) as arg_zBody, \
             agmarshall.DOUBLE_arg() as arg_xCbf, \
             agmarshall.DOUBLE_arg() as arg_yCbf, \
             agmarshall.DOUBLE_arg() as arg_zCbf:
            agcls.evaluate_hresult(self.__dict__["_ConvertBodyCartesianToCBFCartesian"](arg_xBody.COM_val, arg_yBody.COM_val, arg_zBody.COM_val, byref(arg_xCbf.COM_val), byref(arg_yCbf.COM_val), byref(arg_zCbf.COM_val)))
            return arg_xCbf.python_val, arg_yCbf.python_val, arg_zCbf.python_val

    def ConvertBodyCartesianToCBFCartesianArray(self, xBody:float, yBody:float, zBody:float) -> list:
        """Converts a vector in body coordinates into CBF fixed coordinates as an array."""
        with agmarshall.DOUBLE_arg(xBody) as arg_xBody, \
             agmarshall.DOUBLE_arg(yBody) as arg_yBody, \
             agmarshall.DOUBLE_arg(zBody) as arg_zBody, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ConvertBodyCartesianToCBFCartesianArray"](arg_xBody.COM_val, arg_yBody.COM_val, arg_zBody.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def ConvertCBFCartesianToBodyCartesian(self, xCbf:float, yCbf:float, zCbf:float) -> typing.Tuple[float, float, float]:
        """Converts a vector in CBF coordinates into body coordinates."""
        with agmarshall.DOUBLE_arg(xCbf) as arg_xCbf, \
             agmarshall.DOUBLE_arg(yCbf) as arg_yCbf, \
             agmarshall.DOUBLE_arg(zCbf) as arg_zCbf, \
             agmarshall.DOUBLE_arg() as arg_xBody, \
             agmarshall.DOUBLE_arg() as arg_yBody, \
             agmarshall.DOUBLE_arg() as arg_zBody:
            agcls.evaluate_hresult(self.__dict__["_ConvertCBFCartesianToBodyCartesian"](arg_xCbf.COM_val, arg_yCbf.COM_val, arg_zCbf.COM_val, byref(arg_xBody.COM_val), byref(arg_yBody.COM_val), byref(arg_zBody.COM_val)))
            return arg_xBody.python_val, arg_yBody.python_val, arg_zBody.python_val

    def ConvertCBFCartesianToBodyCartesianArray(self, xCbf:float, yCbf:float, zCbf:float) -> list:
        """Converts a vector in CBF coordinates into body coordinates as an array."""
        with agmarshall.DOUBLE_arg(xCbf) as arg_xCbf, \
             agmarshall.DOUBLE_arg(yCbf) as arg_yCbf, \
             agmarshall.DOUBLE_arg(zCbf) as arg_zCbf, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ConvertCBFCartesianToBodyCartesianArray"](arg_xCbf.COM_val, arg_yCbf.COM_val, arg_zCbf.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    @property
    def Role(self) -> "AgEStkRadarPosVelProviderRole":
        """Gets the IAgStkRadarPosVelProvider role."""
        with agmarshall.AgEnum_arg(AgEStkRadarPosVelProviderRole) as arg_pPosVelRole:
            agcls.evaluate_hresult(self.__dict__["_GetRole"](byref(arg_pPosVelRole.COM_val)))
            return arg_pPosVelRole.python_val

    def ComputeCentralBodyIntersectInCBF(self, baseX:float, baseY:float, baseZ:float, dirX:float, dirY:float, dirZ:float) -> "IAgStkRadarCBIntersectComputeResult":
        """Computes the central body intersection using central body fixed coordinates."""
        with agmarshall.DOUBLE_arg(baseX) as arg_baseX, \
             agmarshall.DOUBLE_arg(baseY) as arg_baseY, \
             agmarshall.DOUBLE_arg(baseZ) as arg_baseZ, \
             agmarshall.DOUBLE_arg(dirX) as arg_dirX, \
             agmarshall.DOUBLE_arg(dirY) as arg_dirY, \
             agmarshall.DOUBLE_arg(dirZ) as arg_dirZ, \
             agmarshall.AgInterface_out_arg() as arg_ppCBIntersectComputeResult:
            agcls.evaluate_hresult(self.__dict__["_ComputeCentralBodyIntersectInCBF"](arg_baseX.COM_val, arg_baseY.COM_val, arg_baseZ.COM_val, arg_dirX.COM_val, arg_dirY.COM_val, arg_dirZ.COM_val, byref(arg_ppCBIntersectComputeResult.COM_val)))
            return arg_ppCBIntersectComputeResult.python_val


agcls.AgClassCatalog.add_catalog_entry("{E675D82D-945C-46F9-9E26-0632D13884D4}", IAgStkRadarPosVelProvider)
agcls.AgTypeNameMap["IAgStkRadarPosVelProvider"] = IAgStkRadarPosVelProvider
__all__.append("IAgStkRadarPosVelProvider")

class IAgStkRadarLinkGeometry(object):
    """Interface implemented by an object that provides the geometry for a radar link."""
    _uuid = "{1BD6A448-FA3F-4774-AF3A-24FD7C8F972F}"
    _num_methods = 30
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetTargetPosVelProvider"] = _raise_uninitialized_error
        self.__dict__["_GetTransmitRadarPosVelProvider"] = _raise_uninitialized_error
        self.__dict__["_GetReceiveRadarPosVelProvider"] = _raise_uninitialized_error
        self.__dict__["_GetReceiveRadarRange"] = _raise_uninitialized_error
        self.__dict__["_GetReceiveRadarAngleRate"] = _raise_uninitialized_error
        self.__dict__["_GetReceiveRadarRangeRate"] = _raise_uninitialized_error
        self.__dict__["_GetReceiveRadarConeAngle"] = _raise_uninitialized_error
        self.__dict__["_GetReceiveRadarPropTime"] = _raise_uninitialized_error
        self.__dict__["_GetTransmitRadarRange"] = _raise_uninitialized_error
        self.__dict__["_GetTransmitRadarAngleRate"] = _raise_uninitialized_error
        self.__dict__["_GetTransmitRadarRangeRate"] = _raise_uninitialized_error
        self.__dict__["_GetTransmitRadarConeAngle"] = _raise_uninitialized_error
        self.__dict__["_GetTransmitRadarPropTime"] = _raise_uninitialized_error
        self.__dict__["_GetRangeSum"] = _raise_uninitialized_error
        self.__dict__["_GetClosure"] = _raise_uninitialized_error
        self.__dict__["_GetMLCVelocity"] = _raise_uninitialized_error
        self.__dict__["_GetBistaticAngle"] = _raise_uninitialized_error
        self.__dict__["_GetIncidentAzimuth"] = _raise_uninitialized_error
        self.__dict__["_GetIncidentElevation"] = _raise_uninitialized_error
        self.__dict__["_GetReflectedAzimuth"] = _raise_uninitialized_error
        self.__dict__["_GetReflectedElevation"] = _raise_uninitialized_error
        self.__dict__["_GetXYAngleRate"] = _raise_uninitialized_error
        self.__dict__["_GetTgt2XmtRdrRelPosCBFCartesian"] = _raise_uninitialized_error
        self.__dict__["_GetTgt2XmtRdrRelPosCBFCartesianArray"] = _raise_uninitialized_error
        self.__dict__["_GetTgt2RcvRdrRelPosCBFCartesian"] = _raise_uninitialized_error
        self.__dict__["_GetTgt2RcvRdrRelPosCBFCartesianArray"] = _raise_uninitialized_error
        self.__dict__["_GetXmtRdr2TgtRelPosCBFCartesian"] = _raise_uninitialized_error
        self.__dict__["_GetXmtRdr2TgtRelPosCBFCartesianArray"] = _raise_uninitialized_error
        self.__dict__["_GetRcvRdr2TgtRelPosCBFCartesian"] = _raise_uninitialized_error
        self.__dict__["_GetRcvRdr2TgtRelPosCBFCartesianArray"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarLinkGeometry._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarLinkGeometry from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarLinkGeometry = agcom.GUID(IAgStkRadarLinkGeometry._uuid)
        vtable_offset_local = IAgStkRadarLinkGeometry._vtable_offset - 1
        self.__dict__["_GetTargetPosVelProvider"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetTransmitRadarPosVelProvider"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetReceiveRadarPosVelProvider"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_GetReceiveRadarRange"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_GetReceiveRadarAngleRate"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_GetReceiveRadarRangeRate"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__["_GetReceiveRadarConeAngle"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_GetReceiveRadarPropTime"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__["_GetTransmitRadarRange"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__["_GetTransmitRadarAngleRate"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__["_GetTransmitRadarRangeRate"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__["_GetTransmitRadarConeAngle"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+12, POINTER(agcom.DOUBLE))
        self.__dict__["_GetTransmitRadarPropTime"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+13, POINTER(agcom.DOUBLE))
        self.__dict__["_GetRangeSum"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+14, POINTER(agcom.DOUBLE))
        self.__dict__["_GetClosure"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+15, POINTER(agcom.DOUBLE))
        self.__dict__["_GetMLCVelocity"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+16, POINTER(agcom.DOUBLE))
        self.__dict__["_GetBistaticAngle"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+17, POINTER(agcom.DOUBLE))
        self.__dict__["_GetIncidentAzimuth"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+18, POINTER(agcom.DOUBLE))
        self.__dict__["_GetIncidentElevation"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+19, POINTER(agcom.DOUBLE))
        self.__dict__["_GetReflectedAzimuth"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+20, POINTER(agcom.DOUBLE))
        self.__dict__["_GetReflectedElevation"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+21, POINTER(agcom.DOUBLE))
        self.__dict__["_GetXYAngleRate"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+22, POINTER(agcom.DOUBLE))
        self.__dict__["_GetTgt2XmtRdrRelPosCBFCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+23, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetTgt2XmtRdrRelPosCBFCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+24, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetTgt2RcvRdrRelPosCBFCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+25, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetTgt2RcvRdrRelPosCBFCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+26, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetXmtRdr2TgtRelPosCBFCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+27, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetXmtRdr2TgtRelPosCBFCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+28, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetRcvRdr2TgtRelPosCBFCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+29, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetRcvRdr2TgtRelPosCBFCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLinkGeometry, vtable_offset_local+30, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarLinkGeometry.__dict__ and type(IAgStkRadarLinkGeometry.__dict__[attrname]) == property:
            return IAgStkRadarLinkGeometry.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarLinkGeometry.")
    
    @property
    def TargetPosVelProvider(self) -> "IAgStkRadarPosVelProvider":
        """Gets the target position/velocity provider interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppTargetPosVelProvider:
            agcls.evaluate_hresult(self.__dict__["_GetTargetPosVelProvider"](byref(arg_ppTargetPosVelProvider.COM_val)))
            return arg_ppTargetPosVelProvider.python_val

    @property
    def TransmitRadarPosVelProvider(self) -> "IAgStkRadarPosVelProvider":
        """Gets the transmit radar position/velocity provider interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppTransmitRadarPosVelProvider:
            agcls.evaluate_hresult(self.__dict__["_GetTransmitRadarPosVelProvider"](byref(arg_ppTransmitRadarPosVelProvider.COM_val)))
            return arg_ppTransmitRadarPosVelProvider.python_val

    @property
    def ReceiveRadarPosVelProvider(self) -> "IAgStkRadarPosVelProvider":
        """Gets the receive radar position/velocity provider interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppReceiveRadarPosVelProvider:
            agcls.evaluate_hresult(self.__dict__["_GetReceiveRadarPosVelProvider"](byref(arg_ppReceiveRadarPosVelProvider.COM_val)))
            return arg_ppReceiveRadarPosVelProvider.python_val

    @property
    def ReceiveRadarRange(self) -> float:
        """Gets the receive radar range."""
        with agmarshall.DOUBLE_arg() as arg_pRange:
            agcls.evaluate_hresult(self.__dict__["_GetReceiveRadarRange"](byref(arg_pRange.COM_val)))
            return arg_pRange.python_val

    @property
    def ReceiveRadarAngleRate(self) -> float:
        """Gets the receive radar angle rate."""
        with agmarshall.DOUBLE_arg() as arg_pAngleRate:
            agcls.evaluate_hresult(self.__dict__["_GetReceiveRadarAngleRate"](byref(arg_pAngleRate.COM_val)))
            return arg_pAngleRate.python_val

    @property
    def ReceiveRadarRangeRate(self) -> float:
        """Gets the receive radar range rate."""
        with agmarshall.DOUBLE_arg() as arg_pRangeRate:
            agcls.evaluate_hresult(self.__dict__["_GetReceiveRadarRangeRate"](byref(arg_pRangeRate.COM_val)))
            return arg_pRangeRate.python_val

    @property
    def ReceiveRadarConeAngle(self) -> float:
        """Gets the receive radar cone angle."""
        with agmarshall.DOUBLE_arg() as arg_pConeAngle:
            agcls.evaluate_hresult(self.__dict__["_GetReceiveRadarConeAngle"](byref(arg_pConeAngle.COM_val)))
            return arg_pConeAngle.python_val

    @property
    def ReceiveRadarPropTime(self) -> float:
        """Gets the receive radar prop time."""
        with agmarshall.DOUBLE_arg() as arg_pPropTime:
            agcls.evaluate_hresult(self.__dict__["_GetReceiveRadarPropTime"](byref(arg_pPropTime.COM_val)))
            return arg_pPropTime.python_val

    @property
    def TransmitRadarRange(self) -> float:
        """Gets the transmit radar range."""
        with agmarshall.DOUBLE_arg() as arg_pRange:
            agcls.evaluate_hresult(self.__dict__["_GetTransmitRadarRange"](byref(arg_pRange.COM_val)))
            return arg_pRange.python_val

    @property
    def TransmitRadarAngleRate(self) -> float:
        """Gets the transmit radar angle rate."""
        with agmarshall.DOUBLE_arg() as arg_pAngleRate:
            agcls.evaluate_hresult(self.__dict__["_GetTransmitRadarAngleRate"](byref(arg_pAngleRate.COM_val)))
            return arg_pAngleRate.python_val

    @property
    def TransmitRadarRangeRate(self) -> float:
        """Gets the transmit radar range rate."""
        with agmarshall.DOUBLE_arg() as arg_pRangeRate:
            agcls.evaluate_hresult(self.__dict__["_GetTransmitRadarRangeRate"](byref(arg_pRangeRate.COM_val)))
            return arg_pRangeRate.python_val

    @property
    def TransmitRadarConeAngle(self) -> float:
        """Gets the transmit radar cone angle."""
        with agmarshall.DOUBLE_arg() as arg_pConeAngle:
            agcls.evaluate_hresult(self.__dict__["_GetTransmitRadarConeAngle"](byref(arg_pConeAngle.COM_val)))
            return arg_pConeAngle.python_val

    @property
    def TransmitRadarPropTime(self) -> float:
        """Gets the transmit radar prop time."""
        with agmarshall.DOUBLE_arg() as arg_pPropTime:
            agcls.evaluate_hresult(self.__dict__["_GetTransmitRadarPropTime"](byref(arg_pPropTime.COM_val)))
            return arg_pPropTime.python_val

    @property
    def RangeSum(self) -> float:
        """Gets the range sum."""
        with agmarshall.DOUBLE_arg() as arg_pRangeSum:
            agcls.evaluate_hresult(self.__dict__["_GetRangeSum"](byref(arg_pRangeSum.COM_val)))
            return arg_pRangeSum.python_val

    @property
    def Closure(self) -> float:
        """Gets the closure."""
        with agmarshall.DOUBLE_arg() as arg_pClosure:
            agcls.evaluate_hresult(self.__dict__["_GetClosure"](byref(arg_pClosure.COM_val)))
            return arg_pClosure.python_val

    @property
    def MLCVelocity(self) -> float:
        """Gets the main lobe clutter velocity."""
        with agmarshall.DOUBLE_arg() as arg_pMLCVelocity:
            agcls.evaluate_hresult(self.__dict__["_GetMLCVelocity"](byref(arg_pMLCVelocity.COM_val)))
            return arg_pMLCVelocity.python_val

    @property
    def BistaticAngle(self) -> float:
        """Gets the bistatic angle."""
        with agmarshall.DOUBLE_arg() as arg_pBistaticAngle:
            agcls.evaluate_hresult(self.__dict__["_GetBistaticAngle"](byref(arg_pBistaticAngle.COM_val)))
            return arg_pBistaticAngle.python_val

    @property
    def IncidentAzimuth(self) -> float:
        """Gets the incident azimuth."""
        with agmarshall.DOUBLE_arg() as arg_pIncidentAz:
            agcls.evaluate_hresult(self.__dict__["_GetIncidentAzimuth"](byref(arg_pIncidentAz.COM_val)))
            return arg_pIncidentAz.python_val

    @property
    def IncidentElevation(self) -> float:
        """Gets the incident elevation."""
        with agmarshall.DOUBLE_arg() as arg_pIncidentEl:
            agcls.evaluate_hresult(self.__dict__["_GetIncidentElevation"](byref(arg_pIncidentEl.COM_val)))
            return arg_pIncidentEl.python_val

    @property
    def ReflectedAzimuth(self) -> float:
        """Gets the reflected azimuth."""
        with agmarshall.DOUBLE_arg() as arg_pReflectedAz:
            agcls.evaluate_hresult(self.__dict__["_GetReflectedAzimuth"](byref(arg_pReflectedAz.COM_val)))
            return arg_pReflectedAz.python_val

    @property
    def ReflectedElevation(self) -> float:
        """Gets the reflected elevation."""
        with agmarshall.DOUBLE_arg() as arg_pReflectedEl:
            agcls.evaluate_hresult(self.__dict__["_GetReflectedElevation"](byref(arg_pReflectedEl.COM_val)))
            return arg_pReflectedEl.python_val

    @property
    def XYAngleRate(self) -> float:
        """Gets the xy angle rate."""
        with agmarshall.DOUBLE_arg() as arg_pXYAngleRate:
            agcls.evaluate_hresult(self.__dict__["_GetXYAngleRate"](byref(arg_pXYAngleRate.COM_val)))
            return arg_pXYAngleRate.python_val

    def GetTgt2XmtRdrRelPosCBFCartesian(self) -> typing.Tuple[float, float, float]:
        """Gets the relative position vector from the target to the transmitting radar in central body fixed coordinates"""
        with agmarshall.DOUBLE_arg() as arg_xCbf, \
             agmarshall.DOUBLE_arg() as arg_yCbf, \
             agmarshall.DOUBLE_arg() as arg_zCbf:
            agcls.evaluate_hresult(self.__dict__["_GetTgt2XmtRdrRelPosCBFCartesian"](byref(arg_xCbf.COM_val), byref(arg_yCbf.COM_val), byref(arg_zCbf.COM_val)))
            return arg_xCbf.python_val, arg_yCbf.python_val, arg_zCbf.python_val

    @property
    def Tgt2XmtRdrRelPosCBFCartesianArray(self) -> list:
        """Gets the relative position vector from the target to the transmitting radar in central body fixed coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetTgt2XmtRdrRelPosCBFCartesianArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetTgt2RcvRdrRelPosCBFCartesian(self) -> typing.Tuple[float, float, float]:
        """Gets the relative position vector from the target to the receiving radar in central body fixed coordinates."""
        with agmarshall.DOUBLE_arg() as arg_xCbf, \
             agmarshall.DOUBLE_arg() as arg_yCbf, \
             agmarshall.DOUBLE_arg() as arg_zCbf:
            agcls.evaluate_hresult(self.__dict__["_GetTgt2RcvRdrRelPosCBFCartesian"](byref(arg_xCbf.COM_val), byref(arg_yCbf.COM_val), byref(arg_zCbf.COM_val)))
            return arg_xCbf.python_val, arg_yCbf.python_val, arg_zCbf.python_val

    @property
    def Tgt2RcvRdrRelPosCBFCartesianArray(self) -> list:
        """Gets the relative position vector from the target to the receiving radar in central body fixed coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetTgt2RcvRdrRelPosCBFCartesianArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetXmtRdr2TgtRelPosCBFCartesian(self) -> typing.Tuple[float, float, float]:
        """Gets the relative position vector from the transmitting radar to the target in central body fixed coordinates."""
        with agmarshall.DOUBLE_arg() as arg_xCbf, \
             agmarshall.DOUBLE_arg() as arg_yCbf, \
             agmarshall.DOUBLE_arg() as arg_zCbf:
            agcls.evaluate_hresult(self.__dict__["_GetXmtRdr2TgtRelPosCBFCartesian"](byref(arg_xCbf.COM_val), byref(arg_yCbf.COM_val), byref(arg_zCbf.COM_val)))
            return arg_xCbf.python_val, arg_yCbf.python_val, arg_zCbf.python_val

    @property
    def XmtRdr2TgtRelPosCBFCartesianArray(self) -> list:
        """Gets the relative position vector from the transmitting radar to the target in central body fixed coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetXmtRdr2TgtRelPosCBFCartesianArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetRcvRdr2TgtRelPosCBFCartesian(self) -> typing.Tuple[float, float, float]:
        """Gets the relative position vector from the receiving radar to the target in central body fixed coordinates."""
        with agmarshall.DOUBLE_arg() as arg_xCbf, \
             agmarshall.DOUBLE_arg() as arg_yCbf, \
             agmarshall.DOUBLE_arg() as arg_zCbf:
            agcls.evaluate_hresult(self.__dict__["_GetRcvRdr2TgtRelPosCBFCartesian"](byref(arg_xCbf.COM_val), byref(arg_yCbf.COM_val), byref(arg_zCbf.COM_val)))
            return arg_xCbf.python_val, arg_yCbf.python_val, arg_zCbf.python_val

    @property
    def RcvRdr2TgtRelPosCBFCartesianArray(self) -> list:
        """Gets the relative position vector from the receiving radar to the target in central body fixed coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetRcvRdr2TgtRelPosCBFCartesianArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{1BD6A448-FA3F-4774-AF3A-24FD7C8F972F}", IAgStkRadarLinkGeometry)
agcls.AgTypeNameMap["IAgStkRadarLinkGeometry"] = IAgStkRadarLinkGeometry
__all__.append("IAgStkRadarLinkGeometry")

class IAgStkRadarLink(object):
    """Interface implemented by an object that represents the multi-hop link from a radar transmitter to the target, and back to the receive radar."""
    _uuid = "{7F15B06B-0F53-48DF-BA18-E1D28F7180F9}"
    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetGeometry"] = _raise_uninitialized_error
        self.__dict__["_ComputeDopplerResolution"] = _raise_uninitialized_error
        self.__dict__["_ComputeRangeResolution"] = _raise_uninitialized_error
        self.__dict__["_ComputeIsoDoppler"] = _raise_uninitialized_error
        self.__dict__["_ComputeIsoRange"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarLink._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarLink from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarLink = agcom.GUID(IAgStkRadarLink._uuid)
        vtable_offset_local = IAgStkRadarLink._vtable_offset - 1
        self.__dict__["_GetGeometry"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLink, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_ComputeDopplerResolution"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLink, vtable_offset_local+2, agcom.PVOID, POINTER(agcom.DOUBLE))
        self.__dict__["_ComputeRangeResolution"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLink, vtable_offset_local+3, agcom.PVOID, POINTER(agcom.DOUBLE))
        self.__dict__["_ComputeIsoDoppler"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLink, vtable_offset_local+4, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_ComputeIsoRange"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarLink, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarLink.__dict__ and type(IAgStkRadarLink.__dict__[attrname]) == property:
            return IAgStkRadarLink.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarLink.")
    
    @property
    def Geometry(self) -> "IAgStkRadarLinkGeometry":
        """Gets the link geometry."""
        with agmarshall.AgInterface_out_arg() as arg_ppLinkGeometry:
            agcls.evaluate_hresult(self.__dict__["_GetGeometry"](byref(arg_ppLinkGeometry.COM_val)))
            return arg_ppLinkGeometry.python_val

    def ComputeDopplerResolution(self, radarSignal:"IAgCRSignal") -> float:
        """Computes the doppler resolution for the supplied signal."""
        with agmarshall.AgInterface_in_arg(radarSignal, IAgCRSignal) as arg_radarSignal, \
             agmarshall.DOUBLE_arg() as arg_pDopplerResolution:
            agcls.evaluate_hresult(self.__dict__["_ComputeDopplerResolution"](arg_radarSignal.COM_val, byref(arg_pDopplerResolution.COM_val)))
            return arg_pDopplerResolution.python_val

    def ComputeRangeResolution(self, radarSignal:"IAgCRSignal") -> float:
        """Computes the range resolution for the supplied signal."""
        with agmarshall.AgInterface_in_arg(radarSignal, IAgCRSignal) as arg_radarSignal, \
             agmarshall.DOUBLE_arg() as arg_pRangeResolution:
            agcls.evaluate_hresult(self.__dict__["_ComputeRangeResolution"](arg_radarSignal.COM_val, byref(arg_pRangeResolution.COM_val)))
            return arg_pRangeResolution.python_val

    def ComputeIsoDoppler(self, radarSignal:"IAgCRSignal") -> list:
        """Computes the iso doppler array for the supplied signal."""
        with agmarshall.AgInterface_in_arg(radarSignal, IAgCRSignal) as arg_radarSignal, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ComputeIsoDoppler"](arg_radarSignal.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def ComputeIsoRange(self, radarSignal:"IAgCRSignal") -> list:
        """Computes the iso range array for the supplied signal."""
        with agmarshall.AgInterface_in_arg(radarSignal, IAgCRSignal) as arg_radarSignal, \
             agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_ComputeIsoRange"](arg_radarSignal.COM_val, byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{7F15B06B-0F53-48DF-BA18-E1D28F7180F9}", IAgStkRadarLink)
agcls.AgTypeNameMap["IAgStkRadarLink"] = IAgStkRadarLink
__all__.append("IAgStkRadarLink")

class IAgStkRadarSignal(object):
    """Interface implemented by an object that represents a radar signal."""
    _uuid = "{5F85A0C9-7DA4-4364-8934-8A21DEBF7AE1}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetPulseRepetitionFrequency"] = _raise_uninitialized_error
        self.__dict__["_GetPulseCompressionRatio"] = _raise_uninitialized_error
        self.__dict__["_GetPulseWidth"] = _raise_uninitialized_error
        self.__dict__["_GetNumberOfPulses"] = _raise_uninitialized_error
        self.__dict__["_GetRcs"] = _raise_uninitialized_error
        self.__dict__["_SetRcs"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarSignal._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarSignal from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarSignal = agcom.GUID(IAgStkRadarSignal._uuid)
        vtable_offset_local = IAgStkRadarSignal._vtable_offset - 1
        self.__dict__["_GetPulseRepetitionFrequency"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarSignal, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_GetPulseCompressionRatio"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarSignal, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_GetPulseWidth"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarSignal, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_GetNumberOfPulses"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarSignal, vtable_offset_local+4, POINTER(agcom.INT))
        self.__dict__["_GetRcs"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarSignal, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetRcs"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarSignal, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarSignal.__dict__ and type(IAgStkRadarSignal.__dict__[attrname]) == property:
            return IAgStkRadarSignal.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarSignal.")
    
    @property
    def PulseRepetitionFrequency(self) -> float:
        """Gets the signal pulse repetition frequency."""
        with agmarshall.DOUBLE_arg() as arg_pPrf:
            agcls.evaluate_hresult(self.__dict__["_GetPulseRepetitionFrequency"](byref(arg_pPrf.COM_val)))
            return arg_pPrf.python_val

    @property
    def PulseCompressionRatio(self) -> float:
        """Gets the signal pulse compression ratio."""
        with agmarshall.DOUBLE_arg() as arg_pPcr:
            agcls.evaluate_hresult(self.__dict__["_GetPulseCompressionRatio"](byref(arg_pPcr.COM_val)))
            return arg_pPcr.python_val

    @property
    def PulseWidth(self) -> float:
        """Gets the signal pulse width."""
        with agmarshall.DOUBLE_arg() as arg_pPulseWidth:
            agcls.evaluate_hresult(self.__dict__["_GetPulseWidth"](byref(arg_pPulseWidth.COM_val)))
            return arg_pPulseWidth.python_val

    @property
    def NumberOfPulses(self) -> int:
        """Gets the number of pulses."""
        with agmarshall.INT_arg() as arg_pNumPulses:
            agcls.evaluate_hresult(self.__dict__["_GetNumberOfPulses"](byref(arg_pNumPulses.COM_val)))
            return arg_pNumPulses.python_val

    @property
    def Rcs(self) -> float:
        """Gets or sets the signal RCS."""
        with agmarshall.DOUBLE_arg() as arg_pRcs:
            agcls.evaluate_hresult(self.__dict__["_GetRcs"](byref(arg_pRcs.COM_val)))
            return arg_pRcs.python_val

    @Rcs.setter
    def Rcs(self, rcs:float) -> None:
        """Gets or sets the signal RCS."""
        with agmarshall.DOUBLE_arg(rcs) as arg_rcs:
            agcls.evaluate_hresult(self.__dict__["_SetRcs"](arg_rcs.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{5F85A0C9-7DA4-4364-8934-8A21DEBF7AE1}", IAgStkRadarSignal)
agcls.AgTypeNameMap["IAgStkRadarSignal"] = IAgStkRadarSignal
__all__.append("IAgStkRadarSignal")

class IAgStkRadarClutterPatch(object):
    """Interface implemented by an object that represents a clutter patch."""
    _uuid = "{59DC586B-E3E3-49F3-8889-4631B472E13C}"
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetPosVelProvider"] = _raise_uninitialized_error
        self.__dict__["_SetPositionCBF"] = _raise_uninitialized_error
        self.__dict__["_SetVelocityCBF"] = _raise_uninitialized_error
        self.__dict__["_GetArea"] = _raise_uninitialized_error
        self.__dict__["_SetArea"] = _raise_uninitialized_error
        self.__dict__["_GetScatteringPointComponentName"] = _raise_uninitialized_error
        self.__dict__["_SetScatteringPointComponentName"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarClutterPatch._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarClutterPatch from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarClutterPatch = agcom.GUID(IAgStkRadarClutterPatch._uuid)
        vtable_offset_local = IAgStkRadarClutterPatch._vtable_offset - 1
        self.__dict__["_GetPosVelProvider"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatch, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_SetPositionCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatch, vtable_offset_local+2, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_SetVelocityCBF"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatch, vtable_offset_local+3, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_GetArea"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatch, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_SetArea"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatch, vtable_offset_local+5, agcom.DOUBLE)
        self.__dict__["_GetScatteringPointComponentName"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatch, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_SetScatteringPointComponentName"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatch, vtable_offset_local+7, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarClutterPatch.__dict__ and type(IAgStkRadarClutterPatch.__dict__[attrname]) == property:
            return IAgStkRadarClutterPatch.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarClutterPatch.")
    
    @property
    def PosVelProvider(self) -> "IAgStkRadarPosVelProvider":
        """Gets the patch position/velocity provider interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppPosVelProvider:
            agcls.evaluate_hresult(self.__dict__["_GetPosVelProvider"](byref(arg_ppPosVelProvider.COM_val)))
            return arg_ppPosVelProvider.python_val

    def SetPositionCBF(self, x:float, y:float, z:float) -> None:
        """Sets the patch position in the central body fixed frame."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetPositionCBF"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def SetVelocityCBF(self, x:float, y:float, z:float) -> None:
        """Sets the patch velocity in the central body fixed frame."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetVelocityCBF"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    @property
    def Area(self) -> float:
        """Gets or sets the patch area."""
        with agmarshall.DOUBLE_arg() as arg_pArea:
            agcls.evaluate_hresult(self.__dict__["_GetArea"](byref(arg_pArea.COM_val)))
            return arg_pArea.python_val

    @Area.setter
    def Area(self, area:float) -> None:
        """Gets or sets the patch area."""
        with agmarshall.DOUBLE_arg(area) as arg_area:
            agcls.evaluate_hresult(self.__dict__["_SetArea"](arg_area.COM_val))

    @property
    def ScatteringPointComponentName(self) -> str:
        """Gets or set the patch scattering point model by component name."""
        with agmarshall.BSTR_arg() as arg_pScatteringPoitnModelComponentName:
            agcls.evaluate_hresult(self.__dict__["_GetScatteringPointComponentName"](byref(arg_pScatteringPoitnModelComponentName.COM_val)))
            return arg_pScatteringPoitnModelComponentName.python_val

    @ScatteringPointComponentName.setter
    def ScatteringPointComponentName(self, scatteringPoitnModelComponentName:str) -> None:
        """Gets or sets the patch scattering point model by component name."""
        with agmarshall.BSTR_arg(scatteringPoitnModelComponentName) as arg_scatteringPoitnModelComponentName:
            agcls.evaluate_hresult(self.__dict__["_SetScatteringPointComponentName"](arg_scatteringPoitnModelComponentName.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{59DC586B-E3E3-49F3-8889-4631B472E13C}", IAgStkRadarClutterPatch)
agcls.AgTypeNameMap["IAgStkRadarClutterPatch"] = IAgStkRadarClutterPatch
__all__.append("IAgStkRadarClutterPatch")

class IAgStkRadarClutterPatchCollection(object):
    """Interface implemented by a collection of clutter patch objects."""
    _uuid = "{061AF1AD-821F-462D-BAA3-00E2389E1C59}"
    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Remove"] = _raise_uninitialized_error
        self.__dict__["_RemoveAt"] = _raise_uninitialized_error
        self.__dict__["_RemoveAll"] = _raise_uninitialized_error
        self.__dict__["_Add"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarClutterPatchCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarClutterPatchCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarClutterPatchCollection = agcom.GUID(IAgStkRadarClutterPatchCollection._uuid)
        vtable_offset_local = IAgStkRadarClutterPatchCollection._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatchCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatchCollection, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatchCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_Remove"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatchCollection, vtable_offset_local+4, agcom.PVOID)
        self.__dict__["_RemoveAt"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatchCollection, vtable_offset_local+5, agcom.LONG)
        self.__dict__["_RemoveAll"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatchCollection, vtable_offset_local+6, )
        self.__dict__["_Add"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterPatchCollection, vtable_offset_local+7, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarClutterPatchCollection.__dict__ and type(IAgStkRadarClutterPatchCollection.__dict__[attrname]) == property:
            return IAgStkRadarClutterPatchCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarClutterPatchCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgStkRadarClutterPatch":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    @property
    def Count(self) -> int:
        """Returns the number of elements in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def Item(self, index:int) -> "IAgStkRadarClutterPatch":
        """Given an index, returns an element in the collection."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppClutterPatch:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_ppClutterPatch.COM_val)))
            return arg_ppClutterPatch.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an enumerator that can iterate through the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    def Remove(self, item:"IAgStkRadarClutterPatch") -> None:
        """Removes the specified element from the collection."""
        with agmarshall.AgInterface_in_arg(item, IAgStkRadarClutterPatch) as arg_item:
            agcls.evaluate_hresult(self.__dict__["_Remove"](arg_item.COM_val))

    def RemoveAt(self, index:int) -> None:
        """Removes an element from the collection using specified index."""
        with agmarshall.LONG_arg(index) as arg_index:
            agcls.evaluate_hresult(self.__dict__["_RemoveAt"](arg_index.COM_val))

    def RemoveAll(self) -> None:
        """Removes all elements from the collection."""
        agcls.evaluate_hresult(self.__dict__["_RemoveAll"]())

    def Add(self) -> "IAgStkRadarClutterPatch":
        """Adds a new element to the collection."""
        with agmarshall.AgInterface_out_arg() as arg_ppClutterPatch:
            agcls.evaluate_hresult(self.__dict__["_Add"](byref(arg_ppClutterPatch.COM_val)))
            return arg_ppClutterPatch.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{061AF1AD-821F-462D-BAA3-00E2389E1C59}", IAgStkRadarClutterPatchCollection)
agcls.AgTypeNameMap["IAgStkRadarClutterPatchCollection"] = IAgStkRadarClutterPatchCollection
__all__.append("IAgStkRadarClutterPatchCollection")

class IAgStkRadarClutterGeometryPluginRegInfo(object):
    """Interface implemented by an object that represents the registration information for the clutter geometry plugin."""
    _uuid = "{CB97AE64-AFE6-4F78-A9E4-C56330720ECE}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_SetValidRadarSystems"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarClutterGeometryPluginRegInfo._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarClutterGeometryPluginRegInfo from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarClutterGeometryPluginRegInfo = agcom.GUID(IAgStkRadarClutterGeometryPluginRegInfo._uuid)
        vtable_offset_local = IAgStkRadarClutterGeometryPluginRegInfo._vtable_offset - 1
        self.__dict__["_SetValidRadarSystems"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterGeometryPluginRegInfo, vtable_offset_local+1, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarClutterGeometryPluginRegInfo.__dict__ and type(IAgStkRadarClutterGeometryPluginRegInfo.__dict__[attrname]) == property:
            return IAgStkRadarClutterGeometryPluginRegInfo.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarClutterGeometryPluginRegInfo.")
    
    @property
    def ValidRadarSystems(self) -> None:
        """ValidRadarSystems is a write-only property."""
        raise RuntimeError("ValidRadarSystems is a write-only property.")


    @ValidRadarSystems.setter
    def ValidRadarSystems(self, validRadarSystems:"AgEStkRadarValidSystems") -> None:
        """Sets the valid radar system mask."""
        with agmarshall.AgEnum_arg(AgEStkRadarValidSystems, validRadarSystems) as arg_validRadarSystems:
            agcls.evaluate_hresult(self.__dict__["_SetValidRadarSystems"](arg_validRadarSystems.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{CB97AE64-AFE6-4F78-A9E4-C56330720ECE}", IAgStkRadarClutterGeometryPluginRegInfo)
agcls.AgTypeNameMap["IAgStkRadarClutterGeometryPluginRegInfo"] = IAgStkRadarClutterGeometryPluginRegInfo
__all__.append("IAgStkRadarClutterGeometryPluginRegInfo")

class IAgStkRadarClutterGeometryComputeParams(object):
    """Interface implemented by an object that represents the parameters to be passed into the clutter geometry plugin Compute method."""
    _uuid = "{B5C1B0B7-838F-41AA-9C2E-2BDB00390E11}"
    _num_methods = 3
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetRadarLink"] = _raise_uninitialized_error
        self.__dict__["_GetSignal"] = _raise_uninitialized_error
        self.__dict__["_GetClutterPatches"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarClutterGeometryComputeParams._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarClutterGeometryComputeParams from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarClutterGeometryComputeParams = agcom.GUID(IAgStkRadarClutterGeometryComputeParams._uuid)
        vtable_offset_local = IAgStkRadarClutterGeometryComputeParams._vtable_offset - 1
        self.__dict__["_GetRadarLink"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterGeometryComputeParams, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetSignal"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterGeometryComputeParams, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetClutterPatches"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterGeometryComputeParams, vtable_offset_local+3, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarClutterGeometryComputeParams.__dict__ and type(IAgStkRadarClutterGeometryComputeParams.__dict__[attrname]) == property:
            return IAgStkRadarClutterGeometryComputeParams.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarClutterGeometryComputeParams.")
    
    @property
    def RadarLink(self) -> "IAgStkRadarLink":
        """Gets the radar link"""
        with agmarshall.AgInterface_out_arg() as arg_ppRadarLink:
            agcls.evaluate_hresult(self.__dict__["_GetRadarLink"](byref(arg_ppRadarLink.COM_val)))
            return arg_ppRadarLink.python_val

    @property
    def Signal(self) -> "IAgCRSignal":
        """Gets the transmit signal"""
        with agmarshall.AgInterface_out_arg() as arg_ppSignal:
            agcls.evaluate_hresult(self.__dict__["_GetSignal"](byref(arg_ppSignal.COM_val)))
            return arg_ppSignal.python_val

    @property
    def ClutterPatches(self) -> "IAgStkRadarClutterPatchCollection":
        """Gets the clutter patch collection"""
        with agmarshall.AgInterface_out_arg() as arg_ppClutterPatchCollection:
            agcls.evaluate_hresult(self.__dict__["_GetClutterPatches"](byref(arg_ppClutterPatchCollection.COM_val)))
            return arg_ppClutterPatchCollection.python_val


agcls.AgClassCatalog.add_catalog_entry("{B5C1B0B7-838F-41AA-9C2E-2BDB00390E11}", IAgStkRadarClutterGeometryComputeParams)
agcls.AgTypeNameMap["IAgStkRadarClutterGeometryComputeParams"] = IAgStkRadarClutterGeometryComputeParams
__all__.append("IAgStkRadarClutterGeometryComputeParams")

class IAgStkRadarClutterGeometryPluginScatteringModels(object):
    """Interface implemented by an object that represents a clutter geometry plugin that can configure clutter patches with scattering models."""
    _uuid = "{8C8FE438-C3BC-4B06-A8EF-A97BA63A7C43}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetScatteringModelComponentNames"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarClutterGeometryPluginScatteringModels._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarClutterGeometryPluginScatteringModels from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarClutterGeometryPluginScatteringModels = agcom.GUID(IAgStkRadarClutterGeometryPluginScatteringModels._uuid)
        vtable_offset_local = IAgStkRadarClutterGeometryPluginScatteringModels._vtable_offset - 1
        self.__dict__["_GetScatteringModelComponentNames"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterGeometryPluginScatteringModels, vtable_offset_local+1, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarClutterGeometryPluginScatteringModels.__dict__ and type(IAgStkRadarClutterGeometryPluginScatteringModels.__dict__[attrname]) == property:
            return IAgStkRadarClutterGeometryPluginScatteringModels.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarClutterGeometryPluginScatteringModels.")
    
    @property
    def ScatteringModelComponentNames(self) -> list:
        """Returns the list of scattering model component names which the plugin intends to set on the returned clutter patches."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetScatteringModelComponentNames"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val


agcls.AgClassCatalog.add_catalog_entry("{8C8FE438-C3BC-4B06-A8EF-A97BA63A7C43}", IAgStkRadarClutterGeometryPluginScatteringModels)
agcls.AgTypeNameMap["IAgStkRadarClutterGeometryPluginScatteringModels"] = IAgStkRadarClutterGeometryPluginScatteringModels
__all__.append("IAgStkRadarClutterGeometryPluginScatteringModels")

class IAgStkRadarClutterMapComputeParams(object):
    """Interface implemented by an object that represents the parameters to be passed into the clutter map plugin Compute method."""
    _uuid = "{D58CDC19-794D-4603-87B8-40B7783F730E}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetRadarLink"] = _raise_uninitialized_error
        self.__dict__["_GetClutterPatch"] = _raise_uninitialized_error
        self.__dict__["_GetSignal"] = _raise_uninitialized_error
        self.__dict__["_ConstructPolarization"] = _raise_uninitialized_error
        self.__dict__["_ConstructPolarizationCopy"] = _raise_uninitialized_error
        self.__dict__["_ConstructOrthogonalPolarization"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarClutterMapComputeParams._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarClutterMapComputeParams from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarClutterMapComputeParams = agcom.GUID(IAgStkRadarClutterMapComputeParams._uuid)
        vtable_offset_local = IAgStkRadarClutterMapComputeParams._vtable_offset - 1
        self.__dict__["_GetRadarLink"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterMapComputeParams, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetClutterPatch"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterMapComputeParams, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetSignal"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterMapComputeParams, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_ConstructPolarization"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterMapComputeParams, vtable_offset_local+4, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_ConstructPolarizationCopy"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterMapComputeParams, vtable_offset_local+5, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_ConstructOrthogonalPolarization"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarClutterMapComputeParams, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarClutterMapComputeParams.__dict__ and type(IAgStkRadarClutterMapComputeParams.__dict__[attrname]) == property:
            return IAgStkRadarClutterMapComputeParams.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarClutterMapComputeParams.")
    
    @property
    def RadarLink(self) -> "IAgStkRadarLink":
        """Gets the radar link."""
        with agmarshall.AgInterface_out_arg() as arg_ppRadarLink:
            agcls.evaluate_hresult(self.__dict__["_GetRadarLink"](byref(arg_ppRadarLink.COM_val)))
            return arg_ppRadarLink.python_val

    @property
    def ClutterPatch(self) -> "IAgStkRadarClutterPatch":
        """Gets the clutter patch."""
        with agmarshall.AgInterface_out_arg() as arg_ppClutterPatch:
            agcls.evaluate_hresult(self.__dict__["_GetClutterPatch"](byref(arg_ppClutterPatch.COM_val)))
            return arg_ppClutterPatch.python_val

    @property
    def Signal(self) -> "IAgCRSignal":
        """Gets the signal."""
        with agmarshall.AgInterface_out_arg() as arg_ppSignal:
            agcls.evaluate_hresult(self.__dict__["_GetSignal"](byref(arg_ppSignal.COM_val)))
            return arg_ppSignal.python_val

    def ConstructPolarization(self, polType:"AgECRPolarizationType") -> "IAgCRPolarization":
        """Constructs a new polarization object."""
        with agmarshall.AgEnum_arg(AgECRPolarizationType, polType) as arg_polType, \
             agmarshall.AgInterface_out_arg() as arg_ppPolarization:
            agcls.evaluate_hresult(self.__dict__["_ConstructPolarization"](arg_polType.COM_val, byref(arg_ppPolarization.COM_val)))
            return arg_ppPolarization.python_val

    def ConstructPolarizationCopy(self, polarizationToCopy:"IAgCRPolarization") -> "IAgCRPolarization":
        """Constructs a copy of the specified polarization."""
        with agmarshall.AgInterface_in_arg(polarizationToCopy, IAgCRPolarization) as arg_polarizationToCopy, \
             agmarshall.AgInterface_out_arg() as arg_ppPolarizationCopy:
            agcls.evaluate_hresult(self.__dict__["_ConstructPolarizationCopy"](arg_polarizationToCopy.COM_val, byref(arg_ppPolarizationCopy.COM_val)))
            return arg_ppPolarizationCopy.python_val

    def ConstructOrthogonalPolarization(self, polarizationToCopy:"IAgCRPolarization") -> "IAgCRPolarization":
        """Constructs an orthogonal instance of the specified polarization."""
        with agmarshall.AgInterface_in_arg(polarizationToCopy, IAgCRPolarization) as arg_polarizationToCopy, \
             agmarshall.AgInterface_out_arg() as arg_ppOrthoPolarization:
            agcls.evaluate_hresult(self.__dict__["_ConstructOrthogonalPolarization"](arg_polarizationToCopy.COM_val, byref(arg_ppOrthoPolarization.COM_val)))
            return arg_ppOrthoPolarization.python_val


agcls.AgClassCatalog.add_catalog_entry("{D58CDC19-794D-4603-87B8-40B7783F730E}", IAgStkRadarClutterMapComputeParams)
agcls.AgTypeNameMap["IAgStkRadarClutterMapComputeParams"] = IAgStkRadarClutterMapComputeParams
__all__.append("IAgStkRadarClutterMapComputeParams")

class IAgStkRadarRcsProcessSignalsParams(object):
    """Interface implemented by an object that represents the parameters to be passed into the RCS plugin ProcessSignals method."""
    _uuid = "{AF578053-2B0A-46CA-9C78-8F46C0A895D6}"
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetIncidentBodyFixedVector"] = _raise_uninitialized_error
        self.__dict__["_GetInicidentBodyFixedVectorArray"] = _raise_uninitialized_error
        self.__dict__["_GetReflectedBodyFixedVector"] = _raise_uninitialized_error
        self.__dict__["_GetReflectedBodyFixedVectorArray"] = _raise_uninitialized_error
        self.__dict__["_GetPrimaryPolChannelSignal"] = _raise_uninitialized_error
        self.__dict__["_GetOrthoPolChannelSignal"] = _raise_uninitialized_error
        self.__dict__["_ConstructPolarization"] = _raise_uninitialized_error
        self.__dict__["_ConstructPolarizationCopy"] = _raise_uninitialized_error
        self.__dict__["_ConstructOrthogonalPolarization"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarRcsProcessSignalsParams._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarRcsProcessSignalsParams from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarRcsProcessSignalsParams = agcom.GUID(IAgStkRadarRcsProcessSignalsParams._uuid)
        vtable_offset_local = IAgStkRadarRcsProcessSignalsParams._vtable_offset - 1
        self.__dict__["_GetIncidentBodyFixedVector"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+1, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetInicidentBodyFixedVectorArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+2, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetReflectedBodyFixedVector"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+3, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetReflectedBodyFixedVectorArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+4, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetPrimaryPolChannelSignal"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__["_GetOrthoPolChannelSignal"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+6, POINTER(agcom.PVOID))
        self.__dict__["_ConstructPolarization"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+7, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_ConstructPolarizationCopy"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+8, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_ConstructOrthogonalPolarization"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsProcessSignalsParams, vtable_offset_local+9, agcom.PVOID, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarRcsProcessSignalsParams.__dict__ and type(IAgStkRadarRcsProcessSignalsParams.__dict__[attrname]) == property:
            return IAgStkRadarRcsProcessSignalsParams.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarRcsProcessSignalsParams.")
    
    def GetIncidentBodyFixedVector(self) -> typing.Tuple[float, float, float]:
        """Gets the incident body fixed vector."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetIncidentBodyFixedVector"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def InicidentBodyFixedVectorArray(self) -> list:
        """Gets the incident body fixed vector as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetInicidentBodyFixedVectorArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetReflectedBodyFixedVector(self) -> typing.Tuple[float, float, float]:
        """Gets the reflected body fixed vector."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetReflectedBodyFixedVector"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def ReflectedBodyFixedVectorArray(self) -> list:
        """Gets the reflected body fixed vector as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetReflectedBodyFixedVectorArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    @property
    def PrimaryPolChannelSignal(self) -> "IAgCRSignal":
        """Gets the read-only signal."""
        with agmarshall.AgInterface_out_arg() as arg_ppSignal:
            agcls.evaluate_hresult(self.__dict__["_GetPrimaryPolChannelSignal"](byref(arg_ppSignal.COM_val)))
            return arg_ppSignal.python_val

    @property
    def OrthoPolChannelSignal(self) -> "IAgCRSignal":
        """Gets the read-only signal."""
        with agmarshall.AgInterface_out_arg() as arg_ppSignal:
            agcls.evaluate_hresult(self.__dict__["_GetOrthoPolChannelSignal"](byref(arg_ppSignal.COM_val)))
            return arg_ppSignal.python_val

    def ConstructPolarization(self, polType:"AgECRPolarizationType") -> "IAgCRPolarization":
        """Constructs a new polarization object."""
        with agmarshall.AgEnum_arg(AgECRPolarizationType, polType) as arg_polType, \
             agmarshall.AgInterface_out_arg() as arg_ppPolarization:
            agcls.evaluate_hresult(self.__dict__["_ConstructPolarization"](arg_polType.COM_val, byref(arg_ppPolarization.COM_val)))
            return arg_ppPolarization.python_val

    def ConstructPolarizationCopy(self, polarizationToCopy:"IAgCRPolarization") -> "IAgCRPolarization":
        """Constructs a copy of the specified polarization."""
        with agmarshall.AgInterface_in_arg(polarizationToCopy, IAgCRPolarization) as arg_polarizationToCopy, \
             agmarshall.AgInterface_out_arg() as arg_ppPolarizationCopy:
            agcls.evaluate_hresult(self.__dict__["_ConstructPolarizationCopy"](arg_polarizationToCopy.COM_val, byref(arg_ppPolarizationCopy.COM_val)))
            return arg_ppPolarizationCopy.python_val

    def ConstructOrthogonalPolarization(self, polarizationToCopy:"IAgCRPolarization") -> "IAgCRPolarization":
        """Constructs an orthogonal instance of the specified polarization."""
        with agmarshall.AgInterface_in_arg(polarizationToCopy, IAgCRPolarization) as arg_polarizationToCopy, \
             agmarshall.AgInterface_out_arg() as arg_ppOrthoPolarization:
            agcls.evaluate_hresult(self.__dict__["_ConstructOrthogonalPolarization"](arg_polarizationToCopy.COM_val, byref(arg_ppOrthoPolarization.COM_val)))
            return arg_ppOrthoPolarization.python_val


agcls.AgClassCatalog.add_catalog_entry("{AF578053-2B0A-46CA-9C78-8F46C0A895D6}", IAgStkRadarRcsProcessSignalsParams)
agcls.AgTypeNameMap["IAgStkRadarRcsProcessSignalsParams"] = IAgStkRadarRcsProcessSignalsParams
__all__.append("IAgStkRadarRcsProcessSignalsParams")

class IAgStkRadarRcsComputeParams(object):
    """Interface implemented by an object that represents the parameters to be passed into the RCS plugin Compute method."""
    _uuid = "{60F9C3C1-F3E2-4F03-906D-DB9A57EABE2C}"
    _num_methods = 10
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetTime"] = _raise_uninitialized_error
        self.__dict__["_GetFrequency"] = _raise_uninitialized_error
        self.__dict__["_GetIncidentBodyFixedVector"] = _raise_uninitialized_error
        self.__dict__["_GetInicidentBodyFixedVectorArray"] = _raise_uninitialized_error
        self.__dict__["_GetReflectedBodyFixedVector"] = _raise_uninitialized_error
        self.__dict__["_GetReflectedBodyFixedVectorArray"] = _raise_uninitialized_error
        self.__dict__["_SetPrimaryChannelRcs"] = _raise_uninitialized_error
        self.__dict__["_SetPrimaryChannelRcsCross"] = _raise_uninitialized_error
        self.__dict__["_SetOrthoChannelRcs"] = _raise_uninitialized_error
        self.__dict__["_SetOrthoChannelRcsCross"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarRcsComputeParams._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarRcsComputeParams from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarRcsComputeParams = agcom.GUID(IAgStkRadarRcsComputeParams._uuid)
        vtable_offset_local = IAgStkRadarRcsComputeParams._vtable_offset - 1
        self.__dict__["_GetTime"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_GetFrequency"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_GetIncidentBodyFixedVector"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+3, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetInicidentBodyFixedVectorArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+4, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetReflectedBodyFixedVector"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+5, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetReflectedBodyFixedVectorArray"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+6, POINTER(agcom.SAFEARRAY))
        self.__dict__["_SetPrimaryChannelRcs"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+7, agcom.DOUBLE)
        self.__dict__["_SetPrimaryChannelRcsCross"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__["_SetOrthoChannelRcs"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+9, agcom.DOUBLE)
        self.__dict__["_SetOrthoChannelRcsCross"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarRcsComputeParams, vtable_offset_local+10, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarRcsComputeParams.__dict__ and type(IAgStkRadarRcsComputeParams.__dict__[attrname]) == property:
            return IAgStkRadarRcsComputeParams.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarRcsComputeParams.")
    
    @property
    def Time(self) -> float:
        """Gets the current time."""
        with agmarshall.DOUBLE_arg() as arg_pTime:
            agcls.evaluate_hresult(self.__dict__["_GetTime"](byref(arg_pTime.COM_val)))
            return arg_pTime.python_val

    @property
    def Frequency(self) -> float:
        """Gets the signal frequency."""
        with agmarshall.DOUBLE_arg() as arg_pFrequency:
            agcls.evaluate_hresult(self.__dict__["_GetFrequency"](byref(arg_pFrequency.COM_val)))
            return arg_pFrequency.python_val

    def GetIncidentBodyFixedVector(self) -> typing.Tuple[float, float, float]:
        """Gets the incident body fixed vector."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetIncidentBodyFixedVector"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def InicidentBodyFixedVectorArray(self) -> list:
        """Gets the incident body fixed vector as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetInicidentBodyFixedVectorArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def GetReflectedBodyFixedVector(self) -> typing.Tuple[float, float, float]:
        """Gets the reflected body fixed vector."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetReflectedBodyFixedVector"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def ReflectedBodyFixedVectorArray(self) -> list:
        """Gets the reflected body fixed vector as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetReflectedBodyFixedVectorArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    @property
    def PrimaryChannelRcs(self) -> None:
        """PrimaryChannelRcs is a write-only property."""
        raise RuntimeError("PrimaryChannelRcs is a write-only property.")


    @PrimaryChannelRcs.setter
    def PrimaryChannelRcs(self, rcs:float) -> None:
        """Sets the primary channel RCS value"""
        with agmarshall.DOUBLE_arg(rcs) as arg_rcs:
            agcls.evaluate_hresult(self.__dict__["_SetPrimaryChannelRcs"](arg_rcs.COM_val))

    @property
    def PrimaryChannelRcsCross(self) -> None:
        """PrimaryChannelRcsCross is a write-only property."""
        raise RuntimeError("PrimaryChannelRcsCross is a write-only property.")


    @PrimaryChannelRcsCross.setter
    def PrimaryChannelRcsCross(self, rcsCross:float) -> None:
        """Sets the primary channel cross pol RCS value"""
        with agmarshall.DOUBLE_arg(rcsCross) as arg_rcsCross:
            agcls.evaluate_hresult(self.__dict__["_SetPrimaryChannelRcsCross"](arg_rcsCross.COM_val))

    @property
    def OrthoChannelRcs(self) -> None:
        """OrthoChannelRcs is a write-only property."""
        raise RuntimeError("OrthoChannelRcs is a write-only property.")


    @OrthoChannelRcs.setter
    def OrthoChannelRcs(self, rcs:float) -> None:
        """Sets the primary channel RCS value."""
        with agmarshall.DOUBLE_arg(rcs) as arg_rcs:
            agcls.evaluate_hresult(self.__dict__["_SetOrthoChannelRcs"](arg_rcs.COM_val))

    @property
    def OrthoChannelRcsCross(self) -> None:
        """OrthoChannelRcsCross is a write-only property."""
        raise RuntimeError("OrthoChannelRcsCross is a write-only property.")


    @OrthoChannelRcsCross.setter
    def OrthoChannelRcsCross(self, rcsCross:float) -> None:
        """Sets the primary channel cross pol RCS value."""
        with agmarshall.DOUBLE_arg(rcsCross) as arg_rcsCross:
            agcls.evaluate_hresult(self.__dict__["_SetOrthoChannelRcsCross"](arg_rcsCross.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{60F9C3C1-F3E2-4F03-906D-DB9A57EABE2C}", IAgStkRadarRcsComputeParams)
agcls.AgTypeNameMap["IAgStkRadarRcsComputeParams"] = IAgStkRadarRcsComputeParams
__all__.append("IAgStkRadarRcsComputeParams")

class IAgStkRadarFixedPRFProbabilityDetectionComputeParams(object):
    """Interface implemented by an object that represents the parameters to be passed into the Probability of Detection CFAR plugin Compute method."""
    _uuid = "{0D35F146-2F96-4486-BD49-0C69BA138052}"
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetSinglePulseSignaltoNoiseRatio"] = _raise_uninitialized_error
        self.__dict__["_GetIntegratedSignaltoNoiseRatio"] = _raise_uninitialized_error
        self.__dict__["_GetCoherentIntegration"] = _raise_uninitialized_error
        self.__dict__["_GetNoisePower"] = _raise_uninitialized_error
        self.__dict__["_GetNumberOfIntegratedPulses"] = _raise_uninitialized_error
        self.__dict__["_GetReceivedRadarSignal"] = _raise_uninitialized_error
        self.__dict__["_GetClutterSignals"] = _raise_uninitialized_error
        self.__dict__["_SetProbabilityOfDetectionSinglePulse"] = _raise_uninitialized_error
        self.__dict__["_SetProbabilityOfDetectionIntegrated"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarFixedPRFProbabilityDetectionComputeParams._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarFixedPRFProbabilityDetectionComputeParams from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams = agcom.GUID(IAgStkRadarFixedPRFProbabilityDetectionComputeParams._uuid)
        vtable_offset_local = IAgStkRadarFixedPRFProbabilityDetectionComputeParams._vtable_offset - 1
        self.__dict__["_GetSinglePulseSignaltoNoiseRatio"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_GetIntegratedSignaltoNoiseRatio"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_GetCoherentIntegration"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetNoisePower"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_GetNumberOfIntegratedPulses"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+5, POINTER(agcom.INT))
        self.__dict__["_GetReceivedRadarSignal"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+6, POINTER(agcom.PVOID))
        self.__dict__["_GetClutterSignals"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+7, POINTER(agcom.PVOID))
        self.__dict__["_SetProbabilityOfDetectionSinglePulse"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__["_SetProbabilityOfDetectionIntegrated"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionComputeParams, vtable_offset_local+9, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarFixedPRFProbabilityDetectionComputeParams.__dict__ and type(IAgStkRadarFixedPRFProbabilityDetectionComputeParams.__dict__[attrname]) == property:
            return IAgStkRadarFixedPRFProbabilityDetectionComputeParams.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarFixedPRFProbabilityDetectionComputeParams.")
    
    @property
    def SinglePulseSignaltoNoiseRatio(self) -> float:
        """Gets the radar link single pulse signal-to-noise ratio value."""
        with agmarshall.DOUBLE_arg() as arg_pSnrSinglePulse:
            agcls.evaluate_hresult(self.__dict__["_GetSinglePulseSignaltoNoiseRatio"](byref(arg_pSnrSinglePulse.COM_val)))
            return arg_pSnrSinglePulse.python_val

    @property
    def IntegratedSignaltoNoiseRatio(self) -> float:
        """Gets the radar link integrated signal-to-noise ratio value."""
        with agmarshall.DOUBLE_arg() as arg_pSnrIntegrated:
            agcls.evaluate_hresult(self.__dict__["_GetIntegratedSignaltoNoiseRatio"](byref(arg_pSnrIntegrated.COM_val)))
            return arg_pSnrIntegrated.python_val

    @property
    def CoherentIntegration(self) -> bool:
        """Gets a flag indicating whether or not the signal-to-noise ratio was integrated coherently."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pCoherentIntegration:
            agcls.evaluate_hresult(self.__dict__["_GetCoherentIntegration"](byref(arg_pCoherentIntegration.COM_val)))
            return arg_pCoherentIntegration.python_val

    @property
    def NoisePower(self) -> float:
        """Gets the radar receiver noise power."""
        with agmarshall.DOUBLE_arg() as arg_pNoisePower:
            agcls.evaluate_hresult(self.__dict__["_GetNoisePower"](byref(arg_pNoisePower.COM_val)))
            return arg_pNoisePower.python_val

    @property
    def NumberOfIntegratedPulses(self) -> int:
        """Gets the radar link number of pulse integrated."""
        with agmarshall.INT_arg() as arg_pNumberOfIntegratedPulses:
            agcls.evaluate_hresult(self.__dict__["_GetNumberOfIntegratedPulses"](byref(arg_pNumberOfIntegratedPulses.COM_val)))
            return arg_pNumberOfIntegratedPulses.python_val

    @property
    def ReceivedRadarSignal(self) -> "IAgCRSignal":
        """Gets the radar link signal data."""
        with agmarshall.AgInterface_out_arg() as arg_ppRadarSignal:
            agcls.evaluate_hresult(self.__dict__["_GetReceivedRadarSignal"](byref(arg_ppRadarSignal.COM_val)))
            return arg_ppRadarSignal.python_val

    @property
    def ClutterSignals(self) -> "IAgCRSignalCollection":
        """Gets the radar link clutter signal collection."""
        with agmarshall.AgInterface_out_arg() as arg_ppClutterSignals:
            agcls.evaluate_hresult(self.__dict__["_GetClutterSignals"](byref(arg_ppClutterSignals.COM_val)))
            return arg_ppClutterSignals.python_val

    def SetProbabilityOfDetectionSinglePulse(self, probDetSinglePulse:float) -> None:
        """Sets the probability of detection single pulse value."""
        with agmarshall.DOUBLE_arg(probDetSinglePulse) as arg_probDetSinglePulse:
            agcls.evaluate_hresult(self.__dict__["_SetProbabilityOfDetectionSinglePulse"](arg_probDetSinglePulse.COM_val))

    def SetProbabilityOfDetectionIntegrated(self, probDetIntegrated:float) -> None:
        """Sets the integrated probability of detection value."""
        with agmarshall.DOUBLE_arg(probDetIntegrated) as arg_probDetIntegrated:
            agcls.evaluate_hresult(self.__dict__["_SetProbabilityOfDetectionIntegrated"](arg_probDetIntegrated.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{0D35F146-2F96-4486-BD49-0C69BA138052}", IAgStkRadarFixedPRFProbabilityDetectionComputeParams)
agcls.AgTypeNameMap["IAgStkRadarFixedPRFProbabilityDetectionComputeParams"] = IAgStkRadarFixedPRFProbabilityDetectionComputeParams
__all__.append("IAgStkRadarFixedPRFProbabilityDetectionComputeParams")

class IAgStkRadarFixedPRFProbabilityDetectionPlugin(object):
    """Interface implemented by an object that represents a Probability of Detection CFAR plugin."""
    _uuid = "{AD4F24AB-0BEA-4EB2-8A07-F2C674846A3E}"
    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Initialize"] = _raise_uninitialized_error
        self.__dict__["_PreCompute"] = _raise_uninitialized_error
        self.__dict__["_Compute"] = _raise_uninitialized_error
        self.__dict__["_ComputeJamming"] = _raise_uninitialized_error
        self.__dict__["_ComputeJammingClutter"] = _raise_uninitialized_error
        self.__dict__["_PostCompute"] = _raise_uninitialized_error
        self.__dict__["_Free"] = _raise_uninitialized_error
        self.__dict__["_GetNumberOfConstantFalseAlarmRateCells"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgStkRadarFixedPRFProbabilityDetectionPlugin._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgStkRadarFixedPRFProbabilityDetectionPlugin from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin = agcom.GUID(IAgStkRadarFixedPRFProbabilityDetectionPlugin._uuid)
        vtable_offset_local = IAgStkRadarFixedPRFProbabilityDetectionPlugin._vtable_offset - 1
        self.__dict__["_Initialize"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+1, agcom.PVOID)
        self.__dict__["_PreCompute"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_Compute"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_ComputeJamming"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+4, agcom.PVOID)
        self.__dict__["_ComputeJammingClutter"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+5, agcom.PVOID)
        self.__dict__["_PostCompute"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+6, )
        self.__dict__["_Free"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+7, )
        self.__dict__["_GetNumberOfConstantFalseAlarmRateCells"] = IAGFUNCTYPE(pUnk, IID_IAgStkRadarFixedPRFProbabilityDetectionPlugin, vtable_offset_local+8, POINTER(agcom.INT))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkRadarFixedPRFProbabilityDetectionPlugin.__dict__ and type(IAgStkRadarFixedPRFProbabilityDetectionPlugin.__dict__[attrname]) == property:
            return IAgStkRadarFixedPRFProbabilityDetectionPlugin.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgStkRadarFixedPRFProbabilityDetectionPlugin.")
    
    def Initialize(self, site:"IAgUtPluginSite") -> None:
        """Initializes the plugin with the plugin site."""
        with agmarshall.AgInterface_in_arg(site, IAgUtPluginSite) as arg_site:
            agcls.evaluate_hresult(self.__dict__["_Initialize"](arg_site.COM_val))

    def PreCompute(self) -> bool:
        """Probability of Detection CFAR plugin pre-compute."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pValidPreCompute:
            agcls.evaluate_hresult(self.__dict__["_PreCompute"](byref(arg_pValidPreCompute.COM_val)))
            return arg_pValidPreCompute.python_val

    def Compute(self, computeParams:"IAgStkRadarFixedPRFProbabilityDetectionComputeParams") -> None:
        """Probability of Detection CFAR plugin compute with SNR."""
        with agmarshall.AgInterface_in_arg(computeParams, IAgStkRadarFixedPRFProbabilityDetectionComputeParams) as arg_computeParams:
            agcls.evaluate_hresult(self.__dict__["_Compute"](arg_computeParams.COM_val))

    def ComputeJamming(self, computeParams:"IAgStkRadarFixedPRFProbabilityDetectionComputeParams") -> None:
        """Probability of Detection CFAR plugin compute with S/(N+J)."""
        with agmarshall.AgInterface_in_arg(computeParams, IAgStkRadarFixedPRFProbabilityDetectionComputeParams) as arg_computeParams:
            agcls.evaluate_hresult(self.__dict__["_ComputeJamming"](arg_computeParams.COM_val))

    def ComputeJammingClutter(self, computeParams:"IAgStkRadarFixedPRFProbabilityDetectionComputeParams") -> None:
        """Probability of Detection CFAR plugin compute with S/(N+J+C)."""
        with agmarshall.AgInterface_in_arg(computeParams, IAgStkRadarFixedPRFProbabilityDetectionComputeParams) as arg_computeParams:
            agcls.evaluate_hresult(self.__dict__["_ComputeJammingClutter"](arg_computeParams.COM_val))

    def PostCompute(self) -> None:
        """Probability of Detection CFAR plugin post-compute."""
        agcls.evaluate_hresult(self.__dict__["_PostCompute"]())

    def Free(self) -> None:
        """Free Probability of Detection CFAR plugin."""
        agcls.evaluate_hresult(self.__dict__["_Free"]())

    @property
    def NumberOfConstantFalseAlarmRateCells(self) -> int:
        """Gets the number of constant false alarm rate cells."""
        with agmarshall.INT_arg() as arg_pNumberOfFalseAlarmRateCells:
            agcls.evaluate_hresult(self.__dict__["_GetNumberOfConstantFalseAlarmRateCells"](byref(arg_pNumberOfFalseAlarmRateCells.COM_val)))
            return arg_pNumberOfFalseAlarmRateCells.python_val


agcls.AgClassCatalog.add_catalog_entry("{AD4F24AB-0BEA-4EB2-8A07-F2C674846A3E}", IAgStkRadarFixedPRFProbabilityDetectionPlugin)
agcls.AgTypeNameMap["IAgStkRadarFixedPRFProbabilityDetectionPlugin"] = IAgStkRadarFixedPRFProbabilityDetectionPlugin
__all__.append("IAgStkRadarFixedPRFProbabilityDetectionPlugin")

class IAgSTKRadarSTCAttenComputeParams(object):
    """Interface implemented by an object that represents the parameters to be passed into the STC plugin Compute method."""
    _uuid = "{48F46A9F-659A-448A-8681-1FB26BD6749A}"
    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetTime"] = _raise_uninitialized_error
        self.__dict__["_GetFrequency"] = _raise_uninitialized_error
        self.__dict__["_GetRange"] = _raise_uninitialized_error
        self.__dict__["_GetAzimuthAngle"] = _raise_uninitialized_error
        self.__dict__["_GetElevationAngle"] = _raise_uninitialized_error
        self.__dict__["_GetDirection"] = _raise_uninitialized_error
        self.__dict__["_GetDirectionArray"] = _raise_uninitialized_error
        self.__dict__["_SetSTCAttenuation"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSTKRadarSTCAttenComputeParams._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSTKRadarSTCAttenComputeParams from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSTKRadarSTCAttenComputeParams = agcom.GUID(IAgSTKRadarSTCAttenComputeParams._uuid)
        vtable_offset_local = IAgSTKRadarSTCAttenComputeParams._vtable_offset - 1
        self.__dict__["_GetTime"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_GetFrequency"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_GetRange"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_GetAzimuthAngle"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_GetElevationAngle"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_GetDirection"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+6, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetDirectionArray"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+7, POINTER(agcom.SAFEARRAY))
        self.__dict__["_SetSTCAttenuation"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenComputeParams, vtable_offset_local+8, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSTKRadarSTCAttenComputeParams.__dict__ and type(IAgSTKRadarSTCAttenComputeParams.__dict__[attrname]) == property:
            return IAgSTKRadarSTCAttenComputeParams.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSTKRadarSTCAttenComputeParams.")
    
    @property
    def Time(self) -> float:
        """Gets the time value."""
        with agmarshall.DOUBLE_arg() as arg_pTime:
            agcls.evaluate_hresult(self.__dict__["_GetTime"](byref(arg_pTime.COM_val)))
            return arg_pTime.python_val

    @property
    def Frequency(self) -> float:
        """Gets the frequency value."""
        with agmarshall.DOUBLE_arg() as arg_pFrequency:
            agcls.evaluate_hresult(self.__dict__["_GetFrequency"](byref(arg_pFrequency.COM_val)))
            return arg_pFrequency.python_val

    @property
    def Range(self) -> float:
        """Gets the radar link range value."""
        with agmarshall.DOUBLE_arg() as arg_pRange:
            agcls.evaluate_hresult(self.__dict__["_GetRange"](byref(arg_pRange.COM_val)))
            return arg_pRange.python_val

    @property
    def AzimuthAngle(self) -> float:
        """Gets the radar link Azimuth angle value."""
        with agmarshall.DOUBLE_arg() as arg_pAzimuthAngle:
            agcls.evaluate_hresult(self.__dict__["_GetAzimuthAngle"](byref(arg_pAzimuthAngle.COM_val)))
            return arg_pAzimuthAngle.python_val

    @property
    def ElevationAngle(self) -> float:
        """Gets the radar link Elevation Angle value."""
        with agmarshall.DOUBLE_arg() as arg_pElevationAngle:
            agcls.evaluate_hresult(self.__dict__["_GetElevationAngle"](byref(arg_pElevationAngle.COM_val)))
            return arg_pElevationAngle.python_val

    def GetDirection(self) -> typing.Tuple[float, float, float]:
        """Gets the direction vector in the body fixed frame."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_GetDirection"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def DirectionArray(self) -> list:
        """Gets the direction vector in the body fixed frame as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppArray:
            agcls.evaluate_hresult(self.__dict__["_GetDirectionArray"](byref(arg_ppArray.COM_val)))
            return arg_ppArray.python_val

    def SetSTCAttenuation(self, sTCAttenuation:float) -> None:
        """Sets the STC attenuation value."""
        with agmarshall.DOUBLE_arg(sTCAttenuation) as arg_sTCAttenuation:
            agcls.evaluate_hresult(self.__dict__["_SetSTCAttenuation"](arg_sTCAttenuation.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{48F46A9F-659A-448A-8681-1FB26BD6749A}", IAgSTKRadarSTCAttenComputeParams)
agcls.AgTypeNameMap["IAgSTKRadarSTCAttenComputeParams"] = IAgSTKRadarSTCAttenComputeParams
__all__.append("IAgSTKRadarSTCAttenComputeParams")

class IAgSTKRadarSTCAttenPlugin(object):
    """Interface implemented by an object that represents a STC plugin."""
    _uuid = "{0532400A-A1A2-4E2B-BF49-60D7DA3E4750}"
    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Initialize"] = _raise_uninitialized_error
        self.__dict__["_PreCompute"] = _raise_uninitialized_error
        self.__dict__["_ComputeAttenuation"] = _raise_uninitialized_error
        self.__dict__["_PostCompute"] = _raise_uninitialized_error
        self.__dict__["_Free"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSTKRadarSTCAttenPlugin._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSTKRadarSTCAttenPlugin from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSTKRadarSTCAttenPlugin = agcom.GUID(IAgSTKRadarSTCAttenPlugin._uuid)
        vtable_offset_local = IAgSTKRadarSTCAttenPlugin._vtable_offset - 1
        self.__dict__["_Initialize"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenPlugin, vtable_offset_local+1, agcom.PVOID)
        self.__dict__["_PreCompute"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenPlugin, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_ComputeAttenuation"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenPlugin, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_PostCompute"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenPlugin, vtable_offset_local+4, )
        self.__dict__["_Free"] = IAGFUNCTYPE(pUnk, IID_IAgSTKRadarSTCAttenPlugin, vtable_offset_local+5, )
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSTKRadarSTCAttenPlugin.__dict__ and type(IAgSTKRadarSTCAttenPlugin.__dict__[attrname]) == property:
            return IAgSTKRadarSTCAttenPlugin.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSTKRadarSTCAttenPlugin.")
    
    def Initialize(self, site:"IAgUtPluginSite") -> None:
        """Initializes the plugin with the plugin site."""
        with agmarshall.AgInterface_in_arg(site, IAgUtPluginSite) as arg_site:
            agcls.evaluate_hresult(self.__dict__["_Initialize"](arg_site.COM_val))

    def PreCompute(self) -> bool:
        """STC plugin pre-compute."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pValidPreCompute:
            agcls.evaluate_hresult(self.__dict__["_PreCompute"](byref(arg_pValidPreCompute.COM_val)))
            return arg_pValidPreCompute.python_val

    def ComputeAttenuation(self, computeParams:"IAgSTKRadarSTCAttenComputeParams") -> None:
        """STC plugin compute attenuation."""
        with agmarshall.AgInterface_in_arg(computeParams, IAgSTKRadarSTCAttenComputeParams) as arg_computeParams:
            agcls.evaluate_hresult(self.__dict__["_ComputeAttenuation"](arg_computeParams.COM_val))

    def PostCompute(self) -> None:
        """STC plugin post-compute."""
        agcls.evaluate_hresult(self.__dict__["_PostCompute"]())

    def Free(self) -> None:
        """Free STC plugin."""
        agcls.evaluate_hresult(self.__dict__["_Free"]())


agcls.AgClassCatalog.add_catalog_entry("{0532400A-A1A2-4E2B-BF49-60D7DA3E4750}", IAgSTKRadarSTCAttenPlugin)
agcls.AgTypeNameMap["IAgSTKRadarSTCAttenPlugin"] = IAgSTKRadarSTCAttenPlugin
__all__.append("IAgSTKRadarSTCAttenPlugin")


class IAgStkRadarClutterGeometryPlugin(object):
    """
    Interface implemented by an object that represents a clutter geometry plugin.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Register(self, registrationInfo:"IAgStkRadarClutterGeometryPluginRegInfo") -> None:
        """Registers the plugin with the application."""
        raise STKPluginMethodNotImplementedError("Register was not implemented.")

    def Initialize(self, site:"IAgUtPluginSite") -> None:
        """Initializes the plugin with the plugin site."""
        raise STKPluginMethodNotImplementedError("Initialize was not implemented.")

    def PreCompute(self) -> bool:
        """Clutter geometry plugin pre-compute."""
        raise STKPluginMethodNotImplementedError("PreCompute was not implemented.")

    def Compute(self, computeParams:"IAgStkRadarClutterGeometryComputeParams") -> None:
        """Clutter geometry plugin compute."""
        raise STKPluginMethodNotImplementedError("Compute was not implemented.")

    def PostCompute(self) -> None:
        """Clutter geometry plugin post-compute."""
        raise STKPluginMethodNotImplementedError("PostCompute was not implemented.")

    def Free(self) -> None:
        """Free clutter geometry plugin."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgStkRadarClutterGeometryPlugin")

class IAgStkRadarClutterMapPlugin(object):
    """
    Interface implemented by an object that represents a clutter map plugin.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Initialize(self, site:"IAgUtPluginSite") -> None:
        """Initializes the plugin with the plugin site."""
        raise STKPluginMethodNotImplementedError("Initialize was not implemented.")

    def PreCompute(self) -> bool:
        """Clutter map plugin pre-compute."""
        raise STKPluginMethodNotImplementedError("PreCompute was not implemented.")

    def Compute(self, computeParams:"IAgStkRadarClutterMapComputeParams") -> None:
        """Clutter map plugin compute."""
        raise STKPluginMethodNotImplementedError("Compute was not implemented.")

    def PostCompute(self) -> None:
        """Clutter map plugin post-compute."""
        raise STKPluginMethodNotImplementedError("PostCompute was not implemented.")

    def Free(self) -> None:
        """Free clutter map plugin."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgStkRadarClutterMapPlugin")

class IAgStkRadarRcsPlugin(object):
    """
    Interface implemented by an object that represents an RCS plugin.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Initialize(self, site:"IAgUtPluginSite") -> None:
        """Initializes the plugin with the plugin site."""
        raise STKPluginMethodNotImplementedError("Initialize was not implemented.")

    def PreCompute(self) -> bool:
        """RCS plugin pre-compute."""
        raise STKPluginMethodNotImplementedError("PreCompute was not implemented.")

    def ProcessSignals(self, processSignalsParams:"IAgStkRadarRcsProcessSignalsParams") -> None:
        """Processes the incident primary and orthogonal channel signals."""
        raise STKPluginMethodNotImplementedError("ProcessSignals was not implemented.")

    def Compute(self, computeRcsParams:"IAgStkRadarRcsComputeParams") -> None:
        """RCS plugin compute."""
        raise STKPluginMethodNotImplementedError("Compute was not implemented.")

    def PostCompute(self) -> None:
        """RCS plugin post-compute"""
        raise STKPluginMethodNotImplementedError("PostCompute was not implemented.")

    def Free(self) -> None:
        """Free RCS plugin."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

    def IsDynamic(self) -> bool:
        """Gets a flag indicating whether or not the radar cross section is dynamic."""
        raise STKPluginMethodNotImplementedError("IsDynamic was not implemented.")

__all__.append("IAgStkRadarRcsPlugin")



class AgCRPolarizationCircular(IAgCRPolarization):
    """The CoClass for the IAgCRPolarization interface."""
    def __init__(self, sourceObject=None):
        IAgCRPolarization.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCRPolarization._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCRPolarization._get_property(self, attrname) is not None: found_prop = IAgCRPolarization._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCRPolarizationCircular.")
        
agcls.AgClassCatalog.add_catalog_entry("{EE15FC3E-E00B-4577-934F-110FBF33EBFE}", AgCRPolarizationCircular)
__all__.append("AgCRPolarizationCircular")


class AgCRPolarizationLinear(IAgCRPolarizationLinear, IAgCRPolarization):
    """The CoClass for the IAgCRPolarization and IAgCRPolarizationLinear interfaces."""
    def __init__(self, sourceObject=None):
        IAgCRPolarizationLinear.__init__(self, sourceObject)
        IAgCRPolarization.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCRPolarizationLinear._private_init(self, pUnk)
        IAgCRPolarization._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCRPolarizationLinear._get_property(self, attrname) is not None: found_prop = IAgCRPolarizationLinear._get_property(self, attrname)
        if IAgCRPolarization._get_property(self, attrname) is not None: found_prop = IAgCRPolarization._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCRPolarizationLinear.")
        
agcls.AgClassCatalog.add_catalog_entry("{3663C161-5F87-4587-A9B8-2B9FECB02E98}", AgCRPolarizationLinear)
__all__.append("AgCRPolarizationLinear")


class AgCRPolarizationElliptical(IAgCRPolarizationElliptical, IAgCRPolarization):
    """The CoClass for the IAgCRPolarization and IAgCRPolarizationElliptical interfaces."""
    def __init__(self, sourceObject=None):
        IAgCRPolarizationElliptical.__init__(self, sourceObject)
        IAgCRPolarization.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCRPolarizationElliptical._private_init(self, pUnk)
        IAgCRPolarization._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCRPolarizationElliptical._get_property(self, attrname) is not None: found_prop = IAgCRPolarizationElliptical._get_property(self, attrname)
        if IAgCRPolarization._get_property(self, attrname) is not None: found_prop = IAgCRPolarization._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCRPolarizationElliptical.")
        
agcls.AgClassCatalog.add_catalog_entry("{04110C7D-A709-4DE1-BB50-655AD9C68011}", AgCRPolarizationElliptical)
__all__.append("AgCRPolarizationElliptical")


class AgStkRadarCBIntersectComputeParams(IAgStkRadarCBIntersectComputeParams):
    """The CoClass for the IAgStkRadarCBIntersectComputeParams interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarCBIntersectComputeParams.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarCBIntersectComputeParams._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarCBIntersectComputeParams._get_property(self, attrname) is not None: found_prop = IAgStkRadarCBIntersectComputeParams._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarCBIntersectComputeParams.")
        
agcls.AgClassCatalog.add_catalog_entry("{1FC478C8-D340-4B11-B7B0-80F4171EE2BC}", AgStkRadarCBIntersectComputeParams)
__all__.append("AgStkRadarCBIntersectComputeParams")


class AgStkRadarCBIntersectComputeResult(IAgStkRadarCBIntersectComputeResult):
    """The CoClass for the IAgStkRadarCBIntersectComputeResult interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarCBIntersectComputeResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarCBIntersectComputeResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarCBIntersectComputeResult._get_property(self, attrname) is not None: found_prop = IAgStkRadarCBIntersectComputeResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarCBIntersectComputeResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{BB7B137F-71C2-4688-BE1F-1D27DC93B0AD}", AgStkRadarCBIntersectComputeResult)
__all__.append("AgStkRadarCBIntersectComputeResult")


class AgStkRadarPosVelProvider(IAgStkRadarPosVelProvider):
    """The CoClass for the IAgStkRadarPosVelProvider interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarPosVelProvider.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarPosVelProvider._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarPosVelProvider._get_property(self, attrname) is not None: found_prop = IAgStkRadarPosVelProvider._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarPosVelProvider.")
        
agcls.AgClassCatalog.add_catalog_entry("{A5882D19-A0D0-454B-88FD-014D5E1BA458}", AgStkRadarPosVelProvider)
__all__.append("AgStkRadarPosVelProvider")


class AgStkRadarPositionProvider(IAgStkRadarPosVelProvider):
    """The CoClass for the IAgStkRadarPosVelProvider interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarPosVelProvider.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarPosVelProvider._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarPosVelProvider._get_property(self, attrname) is not None: found_prop = IAgStkRadarPosVelProvider._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarPositionProvider.")
        
agcls.AgClassCatalog.add_catalog_entry("{D5E752F4-8940-47D5-86B4-637F9A4C53FA}", AgStkRadarPositionProvider)
__all__.append("AgStkRadarPositionProvider")


class AgStkRadarLinkGeometry(IAgStkRadarLinkGeometry):
    """The CoClass for the IAgStkRadarLinkGeometry interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarLinkGeometry.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarLinkGeometry._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarLinkGeometry._get_property(self, attrname) is not None: found_prop = IAgStkRadarLinkGeometry._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarLinkGeometry.")
        
agcls.AgClassCatalog.add_catalog_entry("{ED5DC287-DC5B-4C93-9DFA-861B2B00F110}", AgStkRadarLinkGeometry)
__all__.append("AgStkRadarLinkGeometry")


class AgStkRadarLink(IAgStkRadarLink):
    """The CoClass for the IAgStkRadarLink interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarLink.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarLink._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarLink._get_property(self, attrname) is not None: found_prop = IAgStkRadarLink._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarLink.")
        
agcls.AgClassCatalog.add_catalog_entry("{EE063CAD-F798-43B2-A583-20332DF10FA1}", AgStkRadarLink)
__all__.append("AgStkRadarLink")


class AgStkRadarSignal(IAgCRSignal, IAgStkRadarSignal):
    """The CoClass for the IAgCRSignal and IAgStkRadarSignal interfaces."""
    def __init__(self, sourceObject=None):
        IAgCRSignal.__init__(self, sourceObject)
        IAgStkRadarSignal.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCRSignal._private_init(self, pUnk)
        IAgStkRadarSignal._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCRSignal._get_property(self, attrname) is not None: found_prop = IAgCRSignal._get_property(self, attrname)
        if IAgStkRadarSignal._get_property(self, attrname) is not None: found_prop = IAgStkRadarSignal._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarSignal.")
        
agcls.AgClassCatalog.add_catalog_entry("{461900CE-31A8-4237-B260-688BC481B2F0}", AgStkRadarSignal)
__all__.append("AgStkRadarSignal")


class AgStkRadarClutterPatch(IAgStkRadarClutterPatch):
    """The CoClass for the IAgStkRadarClutterPatch interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarClutterPatch.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarClutterPatch._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarClutterPatch._get_property(self, attrname) is not None: found_prop = IAgStkRadarClutterPatch._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarClutterPatch.")
        
agcls.AgClassCatalog.add_catalog_entry("{605B5F91-308F-46D2-8D91-E5487F054101}", AgStkRadarClutterPatch)
__all__.append("AgStkRadarClutterPatch")


class AgStkRadarClutterPatchCollection(IAgStkRadarClutterPatchCollection):
    """The CoClass for the IAgStkRadarClutterPatchCollection interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarClutterPatchCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarClutterPatchCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarClutterPatchCollection._get_property(self, attrname) is not None: found_prop = IAgStkRadarClutterPatchCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarClutterPatchCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{5EE3E6D7-B6C9-4A35-BAAE-932306509C89}", AgStkRadarClutterPatchCollection)
__all__.append("AgStkRadarClutterPatchCollection")


class AgStkRadarClutterGeometryPluginRegInfo(IAgStkRadarClutterGeometryPluginRegInfo):
    """The CoClass for the IAgStkRadarClutterGeometryPluginRegInfo interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarClutterGeometryPluginRegInfo.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarClutterGeometryPluginRegInfo._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarClutterGeometryPluginRegInfo._get_property(self, attrname) is not None: found_prop = IAgStkRadarClutterGeometryPluginRegInfo._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarClutterGeometryPluginRegInfo.")
        
agcls.AgClassCatalog.add_catalog_entry("{33D73A96-7B01-4BA2-AF40-F10F3602057E}", AgStkRadarClutterGeometryPluginRegInfo)
__all__.append("AgStkRadarClutterGeometryPluginRegInfo")


class AgStkRadarClutterGeometryComputeParams(IAgStkRadarClutterGeometryComputeParams):
    """The CoClass for the IAgStkRadarClutterGeometryComputeParams interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarClutterGeometryComputeParams.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarClutterGeometryComputeParams._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarClutterGeometryComputeParams._get_property(self, attrname) is not None: found_prop = IAgStkRadarClutterGeometryComputeParams._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarClutterGeometryComputeParams.")
        
agcls.AgClassCatalog.add_catalog_entry("{B2AE8483-9895-4482-B5CF-5EC567B746F7}", AgStkRadarClutterGeometryComputeParams)
__all__.append("AgStkRadarClutterGeometryComputeParams")


class AgStkRadarClutterMapComputeParams(IAgStkRadarClutterMapComputeParams):
    """The CoClass for the IAgStkRadarClutterMapComputeParams interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarClutterMapComputeParams.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarClutterMapComputeParams._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarClutterMapComputeParams._get_property(self, attrname) is not None: found_prop = IAgStkRadarClutterMapComputeParams._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarClutterMapComputeParams.")
        
agcls.AgClassCatalog.add_catalog_entry("{41DB3BD4-BAF1-4BDC-8DC2-A9D4ABC94B99}", AgStkRadarClutterMapComputeParams)
__all__.append("AgStkRadarClutterMapComputeParams")


class AgStkRadarRcsProcessSignalsParams(IAgStkRadarRcsProcessSignalsParams):
    """The CoClass for the IAgStkRadarRcsProcessSignalsParams interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarRcsProcessSignalsParams.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarRcsProcessSignalsParams._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarRcsProcessSignalsParams._get_property(self, attrname) is not None: found_prop = IAgStkRadarRcsProcessSignalsParams._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarRcsProcessSignalsParams.")
        
agcls.AgClassCatalog.add_catalog_entry("{A7254B1F-2D04-4DEB-B59F-6406E38EADB9}", AgStkRadarRcsProcessSignalsParams)
__all__.append("AgStkRadarRcsProcessSignalsParams")


class AgStkRadarRcsComputeParams(IAgStkRadarRcsComputeParams):
    """The CoClass for the IAgStkRadarRcsComputeParams interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarRcsComputeParams.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarRcsComputeParams._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarRcsComputeParams._get_property(self, attrname) is not None: found_prop = IAgStkRadarRcsComputeParams._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarRcsComputeParams.")
        
agcls.AgClassCatalog.add_catalog_entry("{AE5048AB-6D17-4154-BCE3-CD988ED09B25}", AgStkRadarRcsComputeParams)
__all__.append("AgStkRadarRcsComputeParams")


class AgStkRadarFixedPRFProbabilityDetectionComputeParams(IAgStkRadarFixedPRFProbabilityDetectionComputeParams):
    """The CoClass for the IAgStkRadarFixedPRFProbabilityDetectionComputeParams interface."""
    def __init__(self, sourceObject=None):
        IAgStkRadarFixedPRFProbabilityDetectionComputeParams.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgStkRadarFixedPRFProbabilityDetectionComputeParams._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkRadarFixedPRFProbabilityDetectionComputeParams._get_property(self, attrname) is not None: found_prop = IAgStkRadarFixedPRFProbabilityDetectionComputeParams._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarFixedPRFProbabilityDetectionComputeParams.")
        
agcls.AgClassCatalog.add_catalog_entry("{86928B61-6B95-4ED2-8B5E-BB34ABF270D0}", AgStkRadarFixedPRFProbabilityDetectionComputeParams)
__all__.append("AgStkRadarFixedPRFProbabilityDetectionComputeParams")


class AgStkRadarSTCAttenComputeParams(IAgSTKRadarSTCAttenComputeParams):
    """The CoClass for the IAgSTKRadarSTCAttenComputeParams interface."""
    def __init__(self, sourceObject=None):
        IAgSTKRadarSTCAttenComputeParams.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSTKRadarSTCAttenComputeParams._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSTKRadarSTCAttenComputeParams._get_property(self, attrname) is not None: found_prop = IAgSTKRadarSTCAttenComputeParams._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgStkRadarSTCAttenComputeParams.")
        
agcls.AgClassCatalog.add_catalog_entry("{0233AA84-7C1A-49AB-837A-2E8CA5C92CC3}", AgStkRadarSTCAttenComputeParams)
__all__.append("AgStkRadarSTCAttenComputeParams")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
