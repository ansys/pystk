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

class AgEAccessConstraintPluginErrorCodes(IntEnum):
    """Enumeration of AgAccessConstraintPlugin General Error Codes"""
    # Access Constraint Plugin: An internal failure occurred.
    eAccessConstraintPluginErrorInternalFailure = (((1 << 31) | (4 << 16)) | 0x101),
    # Access Constraint Plugin: Object path unavailable.
    eAccessConstraintPluginErrorObjectPathUnavailable = (((1 << 31) | (4 << 16)) | 0x102),
    # Access Constraint Plugin: Central Body Name unavailable.
    eAccessConstraintPluginErrorObjectCentralBodyNameUnavailable = (((1 << 31) | (4 << 16)) | 0x103),
    # Access Constraint Plugin: Implementation not yet complete, please contact AGI for more information.
    eAccessConstraintPluginErrorImplementationIncompleteError = (((1 << 31) | (4 << 16)) | 0x104),
    # Access Constraint Plugin: Plugin initialization failure.
    eAccessConstraintPluginErrorPluginInitializationError = (((1 << 31) | (4 << 16)) | 0x105),
    # Access Constraint Plugin: Plugin uninitialization failure.
    eAccessConstraintPluginErrorPluginUninitializationError = (((1 << 31) | (4 << 16)) | 0x106),
    # Access Constraint Plugin: Invalid AgEAccessConstraintObjectType enum.
    eAccessConstraintPluginErrorObjectTypeInvalid = (((1 << 31) | (4 << 16)) | 0x107),
    # Access Constraint Plugin: No targets have been specified for registration.
    eAccessConstraintPluginErrorRegisterNoTargets = (((1 << 31) | (4 << 16)) | 0x108),
    # Access Constraint Plugin: Bad Frame request. Only eUtFrameInertial and eUtFrameFixed are supported.
    eAccessConstraintPluginErrorBadRequestFrame = (((1 << 31) | (4 << 16)) | 0x109),
    # Access Constraint Plugin: Geometrical value not computed. Check registration dependency flags.
    eAccessConstraintPluginErrorGeometryNotComputed = (((1 << 31) | (4 << 16)) | 0x10A),
    # Access Constraint Plugin: Invalid AgEAltitudeReference enum.
    eAccessConstraintPluginErrorInvalidAltitudeReference = (((1 << 31) | (4 << 16)) | 0x10B),
    # Access Constraint Plugin: Invalid AgEAccessApparentPositionType enum.
    eAccessConstraintPluginErrorInvalidApparentPositionType = (((1 << 31) | (4 << 16)) | 0x10C),
    # Access Constraint Plugin: Invalid dimension name.
    eAccessConstraintPluginErrorInvalidDimension = (((1 << 31) | (4 << 16)) | 0x10D),
    # Access Constraint Plugin: Invalid computational weight value. Must be positive.
    eAccessConstraintPluginErrorInvalidWeight = (((1 << 31) | (4 << 16)) | 0x10E)

agcls.AgTypeNameMap['AgEAccessConstraintPluginErrorCodes'] = AgEAccessConstraintPluginErrorCodes
__all__.append('AgEAccessConstraintPluginErrorCodes')

class AgEAccessConstraintObjectType(IntEnum):
    """Enumeration of valid objects for access constraint plugins."""
    # Aircraft.
    eAircraft = 1,
    # Facility.
    eFacility = 8,
    # Ground Vehicle.
    eGroundVehicle = 9,
    # Launch Vehicle.
    eLaunchVehicle = 10,
    # Missile.
    eMissile = 13,
    # Planet.
    ePlanet = 15,
    # Place.
    ePlace = 25,
    # Radar.
    eRadar = 16,
    # Receiver.
    eReceiver = 17,
    # Satellite.
    eSatellite = 18,
    # Sensor.
    eSensor = 20,
    # Ship.
    eShip = 21,
    # Star.
    eStar = 22,
    # Submarine.
    eSubmarine = 30,
    # Target.
    eTarget = 23,
    # Transmitter.
    eTransmitter = 24

agcls.AgTypeNameMap['AgEAccessConstraintObjectType'] = AgEAccessConstraintObjectType
__all__.append('AgEAccessConstraintObjectType')

class AgEAccessConstraintDependencyFlags(IntEnum):
    """Enumeration of Access Constraint Dependency Flags"""
    # Relative position and velocity
    eDependencyRelativePosVel = 0x0001,
    # Relative acceleration
    eDependencyRelativeAcc = 0x0002,
    # Position and velocity
    eDependencyPosVel = 0x0004,
    # Acceleration
    eDependencyAcc = 0x0008,
    # Attitude
    eDependencyAttitude = 0x0010,
    # Relative position of Sun
    eDependencyRelSun = 0x0020,
    # No dependencies nor light time delay effects computed
    eDependencyNone = 0x1000

agcls.AgTypeNameMap['AgEAccessConstraintDependencyFlags'] = AgEAccessConstraintDependencyFlags
__all__.append('AgEAccessConstraintDependencyFlags')

class AgEAccessLightTimeDelayFrame(IntEnum):
    """Enumeration of frames used in Access to compute light time delay."""
    # CentralBody Inertial frame.
    eLightTimeDelayFrameCBI = 1,
    # Solar system barycenter frame.
    eLightTimeDelayFrameSSBary = 2

agcls.AgTypeNameMap['AgEAccessLightTimeDelayFrame'] = AgEAccessLightTimeDelayFrame
__all__.append('AgEAccessLightTimeDelayFrame')

class AgEApparentPositionSignalSense(IntEnum):
    """Enumeration of the signal sense of the apparent position computation."""
    # Transmit signal.
    eTransmitSignal = 1,
    # Receive signal.
    eReceiveSignal = 2

agcls.AgTypeNameMap['AgEApparentPositionSignalSense'] = AgEApparentPositionSignalSense
__all__.append('AgEApparentPositionSignalSense')

class AgEApparentPositionAberrationType(IntEnum):
    """Enumeration of methods of incorporating aberration into the apparent position computation."""
    # The total effect of aberration.
    eAberrationTotal = 1,
    # The annual effect of aberration.
    eAberrationAnnual = 2,
    # No aberration.
    eAberrationNone = 3

agcls.AgTypeNameMap['AgEApparentPositionAberrationType'] = AgEApparentPositionAberrationType
__all__.append('AgEApparentPositionAberrationType')

class AgEAccessApparentPositionType(IntEnum):
    """Enumeration of types of apparent positions computed by Access."""
    # Light path apparent position. Accounts for the light time delay (if applied) between objects.
    eLightPathApparentPosition = 1,
    # Refracted apparent position. Accounts for refraction effects (if applied) on the light path apparent position.
    eRefractedApparentPosition = 2,
    # Proper Apparent position. Accounts for aberration effects (depending on the aberration type applied) on the refracted apparent position.
    eProperApparentPosition = 3

agcls.AgTypeNameMap['AgEAccessApparentPositionType'] = AgEAccessApparentPositionType
__all__.append('AgEAccessApparentPositionType')

class AgEAltitudeReference(IntEnum):
    """Enumeration of references used for reporting altitude."""
    # Central body ellipsoid.
    eEllispoidReference = 1,
    # Mean sea level. Only available for objects whose central body is Earth.
    eMSLReference = 2,
    # Terrain.
    eTerrainReference = 3

agcls.AgTypeNameMap['AgEAltitudeReference'] = AgEAltitudeReference
__all__.append('AgEAltitudeReference')


class IAgAccessConstraintPluginResultRegister(object):
    """Access Constraint Registration interface for the Register method."""
    _uuid = '{A9513408-7B86-4331-AEF2-A12848DC0C94}'
    _num_methods = 27
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Reset'] = _raise_uninitialized_error
        self.__dict__['_ClearTargets'] = _raise_uninitialized_error
        self.__dict__['_AddTarget'] = _raise_uninitialized_error
        self.__dict__['_Targets'] = _raise_uninitialized_error
        self.__dict__['_ObjectTypeName'] = _raise_uninitialized_error
        self.__dict__['_Register'] = _raise_uninitialized_error
        self.__dict__['_GetBaseObjectType'] = _raise_uninitialized_error
        self.__dict__['_SetBaseObjectType'] = _raise_uninitialized_error
        self.__dict__['_GetBaseDependency'] = _raise_uninitialized_error
        self.__dict__['_SetBaseDependency'] = _raise_uninitialized_error
        self.__dict__['_GetTargetDependency'] = _raise_uninitialized_error
        self.__dict__['_SetTargetDependency'] = _raise_uninitialized_error
        self.__dict__['_GetDimension'] = _raise_uninitialized_error
        self.__dict__['_SetDimension'] = _raise_uninitialized_error
        self.__dict__['_GetMinValue'] = _raise_uninitialized_error
        self.__dict__['_SetMinValue'] = _raise_uninitialized_error
        self.__dict__['_GetMaxValue'] = _raise_uninitialized_error
        self.__dict__['_SetMaxValue'] = _raise_uninitialized_error
        self.__dict__['_GetMaxRelMotion'] = _raise_uninitialized_error
        self.__dict__['_SetMaxRelMotion'] = _raise_uninitialized_error
        self.__dict__['_GetInstallDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetConfigDirectory'] = _raise_uninitialized_error
        self.__dict__['_Message'] = _raise_uninitialized_error
        self.__dict__['_GetWeight'] = _raise_uninitialized_error
        self.__dict__['_SetWeight'] = _raise_uninitialized_error
        self.__dict__['_GetMaxTimeStep'] = _raise_uninitialized_error
        self.__dict__['_SetMaxTimeStep'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAccessConstraintPluginResultRegister._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAccessConstraintPluginResultRegister from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAccessConstraintPluginResultRegister = agcom.GUID(IAgAccessConstraintPluginResultRegister._uuid)
        vtable_offset_local = IAgAccessConstraintPluginResultRegister._vtable_offset - 1
        self.__dict__['_Reset'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+1, )
        self.__dict__['_ClearTargets'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+2, )
        self.__dict__['_AddTarget'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+3, agcom.LONG)
        self.__dict__['_Targets'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+4, POINTER(agcom.SAFEARRAY))
        self.__dict__['_ObjectTypeName'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+5, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__['_Register'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+6, )
        self.__dict__['_GetBaseObjectType'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+7, POINTER(agcom.LONG))
        self.__dict__['_SetBaseObjectType'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+8, agcom.LONG)
        self.__dict__['_GetBaseDependency'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+9, POINTER(agcom.LONG))
        self.__dict__['_SetBaseDependency'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+10, agcom.LONG)
        self.__dict__['_GetTargetDependency'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+11, POINTER(agcom.LONG))
        self.__dict__['_SetTargetDependency'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+12, agcom.LONG)
        self.__dict__['_GetDimension'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+13, POINTER(agcom.BSTR))
        self.__dict__['_SetDimension'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+14, agcom.BSTR)
        self.__dict__['_GetMinValue'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+15, POINTER(agcom.DOUBLE))
        self.__dict__['_SetMinValue'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+16, agcom.DOUBLE)
        self.__dict__['_GetMaxValue'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+17, POINTER(agcom.DOUBLE))
        self.__dict__['_SetMaxValue'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+18, agcom.DOUBLE)
        self.__dict__['_GetMaxRelMotion'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+19, POINTER(agcom.DOUBLE))
        self.__dict__['_SetMaxRelMotion'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+20, agcom.DOUBLE)
        self.__dict__['_GetInstallDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+21, POINTER(agcom.BSTR))
        self.__dict__['_GetConfigDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+22, POINTER(agcom.BSTR))
        self.__dict__['_Message'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+23, agcom.LONG, agcom.BSTR)
        self.__dict__['_GetWeight'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+24, POINTER(agcom.LONG))
        self.__dict__['_SetWeight'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+25, agcom.LONG)
        self.__dict__['_GetMaxTimeStep'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+26, POINTER(agcom.DOUBLE))
        self.__dict__['_SetMaxTimeStep'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultRegister, vtable_offset_local+27, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAccessConstraintPluginResultRegister.__dict__ and type(IAgAccessConstraintPluginResultRegister.__dict__[attrname]) == property:
            return IAgAccessConstraintPluginResultRegister.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAccessConstraintPluginResultRegister.')
    
    def Reset(self) -> None:
        """Resets property values to defaults values and clears targets."""
        agcls.evaluate_hresult(self.__dict__['_Reset']())

    def ClearTargets(self) -> None:
        """Clears the target list."""
        agcls.evaluate_hresult(self.__dict__['_ClearTargets']())

    def AddTarget(self, type:"AgEAccessConstraintObjectType") -> None:
        """Adds a target to the target list."""
        with agmarshall.AgEnum_arg(AgEAccessConstraintObjectType, type) as arg_type:
            agcls.evaluate_hresult(self.__dict__['_AddTarget'](arg_type.COM_val))

    def Targets(self) -> list:
        """Returns the current target list."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Targets'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def ObjectTypeName(self, type:"AgEAccessConstraintObjectType") -> str:
        """Returns the name of associated object type."""
        with agmarshall.AgEnum_arg(AgEAccessConstraintObjectType, type) as arg_type, \
             agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__['_ObjectTypeName'](arg_type.COM_val, byref(arg_pName.COM_val)))
            return arg_pName.python_val

    def Register(self) -> None:
        """Registers the constraint using the current settings."""
        agcls.evaluate_hresult(self.__dict__['_Register']())

    @property
    def BaseObjectType(self) -> "AgEAccessConstraintObjectType":
        """This object type is permitted to own this constraint."""
        with agmarshall.AgEnum_arg(AgEAccessConstraintObjectType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__['_GetBaseObjectType'](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    @BaseObjectType.setter
    def BaseObjectType(self, type:"AgEAccessConstraintObjectType") -> None:
        """This object type is permitted to own this constraint."""
        with agmarshall.AgEnum_arg(AgEAccessConstraintObjectType, type) as arg_type:
            agcls.evaluate_hresult(self.__dict__['_SetBaseObjectType'](arg_type.COM_val))

    @property
    def BaseDependency(self) -> int:
        """Dependency mask of the Base object indicating the geometric dependencies of the constraint computation."""
        with agmarshall.LONG_arg() as arg_pDepMask:
            agcls.evaluate_hresult(self.__dict__['_GetBaseDependency'](byref(arg_pDepMask.COM_val)))
            return arg_pDepMask.python_val

    @BaseDependency.setter
    def BaseDependency(self, newDepMask:int) -> None:
        """Dependency mask of the Base object indicating the geometric dependencies of the constraint computation."""
        with agmarshall.LONG_arg(newDepMask) as arg_newDepMask:
            agcls.evaluate_hresult(self.__dict__['_SetBaseDependency'](arg_newDepMask.COM_val))

    @property
    def TargetDependency(self) -> int:
        """Dependency mask of the Target object indicating the geometric dependencies of the constraint computation."""
        with agmarshall.LONG_arg() as arg_pDepMask:
            agcls.evaluate_hresult(self.__dict__['_GetTargetDependency'](byref(arg_pDepMask.COM_val)))
            return arg_pDepMask.python_val

    @TargetDependency.setter
    def TargetDependency(self, newDepMask:int) -> None:
        """Dependency mask of the Target object indicating the geometric dependencies of the constraint computation."""
        with agmarshall.LONG_arg(newDepMask) as arg_newDepMask:
            agcls.evaluate_hresult(self.__dict__['_SetTargetDependency'](arg_newDepMask.COM_val))

    @property
    def Dimension(self) -> str:
        """Dimension of the computed constraint value."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__['_GetDimension'](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @Dimension.setter
    def Dimension(self, newDimension:str) -> None:
        """Dimension of the computed constraint value."""
        with agmarshall.BSTR_arg(newDimension) as arg_newDimension:
            agcls.evaluate_hresult(self.__dict__['_SetDimension'](arg_newDimension.COM_val))

    @property
    def MinValue(self) -> float:
        """Minimum value of the computed constraint value."""
        with agmarshall.DOUBLE_arg() as arg_pMinValue:
            agcls.evaluate_hresult(self.__dict__['_GetMinValue'](byref(arg_pMinValue.COM_val)))
            return arg_pMinValue.python_val

    @MinValue.setter
    def MinValue(self, newMinValue:float) -> None:
        """Minimum value of the computed constraint value."""
        with agmarshall.DOUBLE_arg(newMinValue) as arg_newMinValue:
            agcls.evaluate_hresult(self.__dict__['_SetMinValue'](arg_newMinValue.COM_val))

    @property
    def MaxValue(self) -> float:
        """Maximum value of the computed constraint value."""
        with agmarshall.DOUBLE_arg() as arg_pMaxValue:
            agcls.evaluate_hresult(self.__dict__['_GetMaxValue'](byref(arg_pMaxValue.COM_val)))
            return arg_pMaxValue.python_val

    @MaxValue.setter
    def MaxValue(self, newMaxValue:float) -> None:
        """Maximum value of the computed constraint value."""
        with agmarshall.DOUBLE_arg(newMaxValue) as arg_newMaxValue:
            agcls.evaluate_hresult(self.__dict__['_SetMaxValue'](arg_newMaxValue.COM_val))

    @property
    def MaxRelMotion(self) -> float:
        """Maximum relative motion (in degrees) allowed between constraint samples."""
        with agmarshall.DOUBLE_arg() as arg_pMaxRelMotion:
            agcls.evaluate_hresult(self.__dict__['_GetMaxRelMotion'](byref(arg_pMaxRelMotion.COM_val)))
            return arg_pMaxRelMotion.python_val

    @MaxRelMotion.setter
    def MaxRelMotion(self, newMaxRelMotion:float) -> None:
        """Maximum relative motion (in dgerees) allowed between constraint samples."""
        with agmarshall.DOUBLE_arg(newMaxRelMotion) as arg_newMaxRelMotion:
            agcls.evaluate_hresult(self.__dict__['_SetMaxRelMotion'](arg_newMaxRelMotion.COM_val))

    @property
    def InstallDirectory(self) -> str:
        """The directory path of the installation of the application."""
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetInstallDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    @property
    def ConfigDirectory(self) -> str:
        """The directory path of the user configuration area."""
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetConfigDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    def Message(self, msgType:"AgEUtLogMsgType", message:str) -> None:
        """Send a message to the message viewer."""
        with agmarshall.AgEnum_arg(AgEUtLogMsgType, msgType) as arg_msgType, \
             agmarshall.BSTR_arg(message) as arg_message:
            agcls.evaluate_hresult(self.__dict__['_Message'](arg_msgType.COM_val, arg_message.COM_val))

    @property
    def Weight(self) -> int:
        """Computational weight of the constraint. Must be positive."""
        with agmarshall.LONG_arg() as arg_pWeight:
            agcls.evaluate_hresult(self.__dict__['_GetWeight'](byref(arg_pWeight.COM_val)))
            return arg_pWeight.python_val

    @Weight.setter
    def Weight(self, newWeight:int) -> None:
        """Computational weight of the constraint. Must be positive."""
        with agmarshall.LONG_arg(newWeight) as arg_newWeight:
            agcls.evaluate_hresult(self.__dict__['_SetWeight'](arg_newWeight.COM_val))

    @property
    def MaxTimeStep(self) -> float:
        """Maximum time step (in secs) allowed between constraint samples."""
        with agmarshall.DOUBLE_arg() as arg_pMaxTimeStep:
            agcls.evaluate_hresult(self.__dict__['_GetMaxTimeStep'](byref(arg_pMaxTimeStep.COM_val)))
            return arg_pMaxTimeStep.python_val

    @MaxTimeStep.setter
    def MaxTimeStep(self, newMaxTimeStep:float) -> None:
        """Maximum time step (in secs) allowed between constraint samples."""
        with agmarshall.DOUBLE_arg(newMaxTimeStep) as arg_newMaxTimeStep:
            agcls.evaluate_hresult(self.__dict__['_SetMaxTimeStep'](arg_newMaxTimeStep.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{A9513408-7B86-4331-AEF2-A12848DC0C94}', IAgAccessConstraintPluginResultRegister)
agcls.AgTypeNameMap['IAgAccessConstraintPluginResultRegister'] = IAgAccessConstraintPluginResultRegister
__all__.append('IAgAccessConstraintPluginResultRegister')

class IAgAccessConstraintPluginObjectDescriptor(object):
    """Access Constraint Plugin Object Descriptor interface."""
    _uuid = '{2E7CB866-8F43-4331-84AD-3C843B8957CD}'
    _num_methods = 10
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetIsValid'] = _raise_uninitialized_error
        self.__dict__['_GetVectorToolProvider'] = _raise_uninitialized_error
        self.__dict__['_GetObjectType'] = _raise_uninitialized_error
        self.__dict__['_GetObjectPath'] = _raise_uninitialized_error
        self.__dict__['_GetShortDescription'] = _raise_uninitialized_error
        self.__dict__['_SetShortDescription'] = _raise_uninitialized_error
        self.__dict__['_GetLongDescription'] = _raise_uninitialized_error
        self.__dict__['_SetLongDescription'] = _raise_uninitialized_error
        self.__dict__['_GetCentralBodyName'] = _raise_uninitialized_error
        self.__dict__['_GetCalcToolProvider'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAccessConstraintPluginObjectDescriptor._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAccessConstraintPluginObjectDescriptor from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAccessConstraintPluginObjectDescriptor = agcom.GUID(IAgAccessConstraintPluginObjectDescriptor._uuid)
        vtable_offset_local = IAgAccessConstraintPluginObjectDescriptor._vtable_offset - 1
        self.__dict__['_GetIsValid'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_GetVectorToolProvider'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__['_GetObjectType'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__['_GetObjectPath'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__['_GetShortDescription'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__['_SetShortDescription'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+6, agcom.BSTR)
        self.__dict__['_GetLongDescription'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+7, POINTER(agcom.BSTR))
        self.__dict__['_SetLongDescription'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+8, agcom.BSTR)
        self.__dict__['_GetCentralBodyName'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+9, POINTER(agcom.BSTR))
        self.__dict__['_GetCalcToolProvider'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectDescriptor, vtable_offset_local+10, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAccessConstraintPluginObjectDescriptor.__dict__ and type(IAgAccessConstraintPluginObjectDescriptor.__dict__[attrname]) == property:
            return IAgAccessConstraintPluginObjectDescriptor.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAccessConstraintPluginObjectDescriptor.')
    
    @property
    def IsValid(self) -> bool:
        """True when the object is a valid object. If false, none of the other methods return valid data."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__['_GetIsValid'](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val

    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__['_GetVectorToolProvider'](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ObjectType(self) -> "AgEAccessConstraintObjectType":
        """The object type of the object."""
        with agmarshall.AgEnum_arg(AgEAccessConstraintObjectType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__['_GetObjectType'](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    @property
    def ObjectPath(self) -> str:
        """The STK object path of the object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__['_GetObjectPath'](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def ShortDescription(self) -> str:
        """The short description of the object."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__['_GetShortDescription'](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @ShortDescription.setter
    def ShortDescription(self, newDescription:str) -> None:
        """The short description of the object."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__['_SetShortDescription'](arg_newDescription.COM_val))

    @property
    def LongDescription(self) -> str:
        """The long description of the object."""
        with agmarshall.BSTR_arg() as arg_pDescription:
            agcls.evaluate_hresult(self.__dict__['_GetLongDescription'](byref(arg_pDescription.COM_val)))
            return arg_pDescription.python_val

    @LongDescription.setter
    def LongDescription(self, newDescription:str) -> None:
        """The long description of the object."""
        with agmarshall.BSTR_arg(newDescription) as arg_newDescription:
            agcls.evaluate_hresult(self.__dict__['_SetLongDescription'](arg_newDescription.COM_val))

    @property
    def CentralBodyName(self) -> str:
        """The name of the central body for this object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__['_GetCentralBodyName'](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        """Creates an IAgCrdnPluginProvider object."""
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__['_GetCalcToolProvider'](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val


agcls.AgClassCatalog.add_catalog_entry('{2E7CB866-8F43-4331-84AD-3C843B8957CD}', IAgAccessConstraintPluginObjectDescriptor)
agcls.AgTypeNameMap['IAgAccessConstraintPluginObjectDescriptor'] = IAgAccessConstraintPluginObjectDescriptor
__all__.append('IAgAccessConstraintPluginObjectDescriptor')

class IAgAccessConstraintPluginResultPreCompute(object):
    """Access Constraint Plugin Result interface for the PreCompute method."""
    _uuid = '{FD05D93E-871D-43b5-BC9D-AEA3BE0FAA46}'
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetBase'] = _raise_uninitialized_error
        self.__dict__['_GetTarget'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAccessConstraintPluginResultPreCompute._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAccessConstraintPluginResultPreCompute from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAccessConstraintPluginResultPreCompute = agcom.GUID(IAgAccessConstraintPluginResultPreCompute._uuid)
        vtable_offset_local = IAgAccessConstraintPluginResultPreCompute._vtable_offset - 1
        self.__dict__['_GetBase'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultPreCompute, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__['_GetTarget'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultPreCompute, vtable_offset_local+2, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAccessConstraintPluginResultPreCompute.__dict__ and type(IAgAccessConstraintPluginResultPreCompute.__dict__[attrname]) == property:
            return IAgAccessConstraintPluginResultPreCompute.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAccessConstraintPluginResultPreCompute.')
    
    @property
    def Base(self) -> "IAgAccessConstraintPluginObjectDescriptor":
        """An interface to a description of the object that owns this constraint."""
        with agmarshall.AgInterface_out_arg() as arg_ppObjectDescriptor:
            agcls.evaluate_hresult(self.__dict__['_GetBase'](byref(arg_ppObjectDescriptor.COM_val)))
            return arg_ppObjectDescriptor.python_val

    @property
    def Target(self) -> "IAgAccessConstraintPluginObjectDescriptor":
        """An interface to a description of the other object involved with this constraint."""
        with agmarshall.AgInterface_out_arg() as arg_ppObjectDescriptor:
            agcls.evaluate_hresult(self.__dict__['_GetTarget'](byref(arg_ppObjectDescriptor.COM_val)))
            return arg_ppObjectDescriptor.python_val


agcls.AgClassCatalog.add_catalog_entry('{FD05D93E-871D-43b5-BC9D-AEA3BE0FAA46}', IAgAccessConstraintPluginResultPreCompute)
agcls.AgTypeNameMap['IAgAccessConstraintPluginResultPreCompute'] = IAgAccessConstraintPluginResultPreCompute
__all__.append('IAgAccessConstraintPluginResultPreCompute')

class IAgAccessConstraintPluginResultPostCompute(object):
    """Access Constraint Plugin Result interface for the PostCompute method."""
    _uuid = '{E3138BF9-8A16-4829-A9DA-07CD62683590}'
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetBase'] = _raise_uninitialized_error
        self.__dict__['_GetTarget'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAccessConstraintPluginResultPostCompute._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAccessConstraintPluginResultPostCompute from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAccessConstraintPluginResultPostCompute = agcom.GUID(IAgAccessConstraintPluginResultPostCompute._uuid)
        vtable_offset_local = IAgAccessConstraintPluginResultPostCompute._vtable_offset - 1
        self.__dict__['_GetBase'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultPostCompute, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__['_GetTarget'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultPostCompute, vtable_offset_local+2, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAccessConstraintPluginResultPostCompute.__dict__ and type(IAgAccessConstraintPluginResultPostCompute.__dict__[attrname]) == property:
            return IAgAccessConstraintPluginResultPostCompute.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAccessConstraintPluginResultPostCompute.')
    
    @property
    def Base(self) -> "IAgAccessConstraintPluginObjectDescriptor":
        """An interface to a description of the object that owns this constraint."""
        with agmarshall.AgInterface_out_arg() as arg_ppObjectDescriptor:
            agcls.evaluate_hresult(self.__dict__['_GetBase'](byref(arg_ppObjectDescriptor.COM_val)))
            return arg_ppObjectDescriptor.python_val

    @property
    def Target(self) -> "IAgAccessConstraintPluginObjectDescriptor":
        """An interface to a description of the other object involved with this constraint."""
        with agmarshall.AgInterface_out_arg() as arg_ppObjectDescriptor:
            agcls.evaluate_hresult(self.__dict__['_GetTarget'](byref(arg_ppObjectDescriptor.COM_val)))
            return arg_ppObjectDescriptor.python_val


agcls.AgClassCatalog.add_catalog_entry('{E3138BF9-8A16-4829-A9DA-07CD62683590}', IAgAccessConstraintPluginResultPostCompute)
agcls.AgTypeNameMap['IAgAccessConstraintPluginResultPostCompute'] = IAgAccessConstraintPluginResultPostCompute
__all__.append('IAgAccessConstraintPluginResultPostCompute')

class IAgAccessConstraintPluginObjectData(object):
    """Access Constraint Plugin Object Data interface used to get inputs and outputs during the Evaluate method call."""
    _uuid = '{71D28592-CF66-4a67-A5AC-9E30FA6CF0DB}'
    _num_methods = 33
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetDescriptor'] = _raise_uninitialized_error
        self.__dict__['_GetCentralBodyName'] = _raise_uninitialized_error
        self.__dict__['_GetSignalSense'] = _raise_uninitialized_error
        self.__dict__['_GetIsClockHost'] = _raise_uninitialized_error
        self.__dict__['_GetIsRefractionComputed'] = _raise_uninitialized_error
        self.__dict__['_GetGeometryMask'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_Position'] = _raise_uninitialized_error
        self.__dict__['_Position_Array'] = _raise_uninitialized_error
        self.__dict__['_Velocity'] = _raise_uninitialized_error
        self.__dict__['_Velocity_Array'] = _raise_uninitialized_error
        self.__dict__['_Acceleration'] = _raise_uninitialized_error
        self.__dict__['_Acceleration_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_Altitude'] = _raise_uninitialized_error
        self.__dict__['_Range'] = _raise_uninitialized_error
        self.__dict__['_RelativePosition'] = _raise_uninitialized_error
        self.__dict__['_RelativePosition_Array'] = _raise_uninitialized_error
        self.__dict__['_RelativeVelocity'] = _raise_uninitialized_error
        self.__dict__['_RelativeVelocity_Array'] = _raise_uninitialized_error
        self.__dict__['_RelativeAcceleration'] = _raise_uninitialized_error
        self.__dict__['_RelativeAcceleration_Array'] = _raise_uninitialized_error
        self.__dict__['_ApparentSunPosition'] = _raise_uninitialized_error
        self.__dict__['_ApparentSunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_Attitude'] = _raise_uninitialized_error
        self.__dict__['_Attitude_Array'] = _raise_uninitialized_error
        self.__dict__['_AngularVelocity'] = _raise_uninitialized_error
        self.__dict__['_AngularVelocity_Array'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAccessConstraintPluginObjectData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAccessConstraintPluginObjectData from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAccessConstraintPluginObjectData = agcom.GUID(IAgAccessConstraintPluginObjectData._uuid)
        vtable_offset_local = IAgAccessConstraintPluginObjectData._vtable_offset - 1
        self.__dict__['_GetDescriptor'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__['_GetCentralBodyName'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__['_GetSignalSense'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__['_GetIsClockHost'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+4, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_GetIsRefractionComputed'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_GetGeometryMask'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+6, POINTER(agcom.LONG))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+7, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+8, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Position'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+9, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_Position_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+10, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Velocity'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+11, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_Velocity_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+12, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Acceleration'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+13, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_Acceleration_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+14, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+15, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+16, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Altitude'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+17, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__['_Range'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+18, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__['_RelativePosition'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+19, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_RelativePosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+20, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_RelativeVelocity'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+21, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_RelativeVelocity_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+22, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_RelativeAcceleration'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+23, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_RelativeAcceleration_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+24, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_ApparentSunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+25, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_ApparentSunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+26, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Attitude'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+27, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_Attitude_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+28, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AngularVelocity'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+29, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AngularVelocity_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+30, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+31, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+32, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginObjectData, vtable_offset_local+33, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAccessConstraintPluginObjectData.__dict__ and type(IAgAccessConstraintPluginObjectData.__dict__[attrname]) == property:
            return IAgAccessConstraintPluginObjectData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAccessConstraintPluginObjectData.')
    
    @property
    def Descriptor(self) -> "IAgAccessConstraintPluginObjectDescriptor":
        """An interface to a description of the object."""
        with agmarshall.AgInterface_out_arg() as arg_ppObjectDescriptor:
            agcls.evaluate_hresult(self.__dict__['_GetDescriptor'](byref(arg_ppObjectDescriptor.COM_val)))
            return arg_ppObjectDescriptor.python_val

    @property
    def CentralBodyName(self) -> str:
        """The name of the central body for this object."""
        with agmarshall.BSTR_arg() as arg_pPath:
            agcls.evaluate_hresult(self.__dict__['_GetCentralBodyName'](byref(arg_pPath.COM_val)))
            return arg_pPath.python_val

    @property
    def SignalSense(self) -> "AgEApparentPositionSignalSense":
        """The signal sense for this object."""
        with agmarshall.AgEnum_arg(AgEApparentPositionSignalSense) as arg_pSignalSense:
            agcls.evaluate_hresult(self.__dict__['_GetSignalSense'](byref(arg_pSignalSense.COM_val)))
            return arg_pSignalSense.python_val

    @property
    def IsClockHost(self) -> bool:
        """True if this object is the clock host for the access computation."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsClockHost:
            agcls.evaluate_hresult(self.__dict__['_GetIsClockHost'](byref(arg_pIsClockHost.COM_val)))
            return arg_pIsClockHost.python_val

    @property
    def IsRefractionComputed(self) -> bool:
        """True if refraction was computed for the apparent relative position of the other object."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsComputed:
            agcls.evaluate_hresult(self.__dict__['_GetIsRefractionComputed'](byref(arg_pIsComputed.COM_val)))
            return arg_pIsComputed.python_val

    @property
    def GeometryMask(self) -> int:
        """A bit mask of AgEAccessConstraintDependencyFlags indicating which geometrical data was computed."""
        with agmarshall.LONG_arg() as arg_pMask:
            agcls.evaluate_hresult(self.__dict__['_GetGeometryMask'](byref(arg_pMask.COM_val)))
            return arg_pMask.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """The current time in requested time scale of the object expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Position_Array(self, frame:"AgEUtFrame") -> list:
        """The object position in the requested frame, returned as an array representing x, y, z. Only eUtFrameInertial and eUtFrameFixed are supported. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Position_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Velocity_Array(self, frame:"AgEUtFrame") -> list:
        """The object velocity in the requested frame, returned as an array representing vx, vy, vz. Only eUtFrameInertial and eUtFrameFixed are supported. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Velocity_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Acceleration_Array(self, frame:"AgEUtFrame") -> list:
        """The object acceleration in the requested frame, returned as an array representing ax, ay, az. Only eUtFrameInertial and eUtFrameFixed are supported. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Acceleration_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """The detic latitude, detic longitude, and altitude of the object, returned as an array representing latitude, longitude, altitude. Altitude is measured wrt the central body ellispoid of the object. (eg. Earth uses WGS84)"""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Altitude(self, altRef:"AgEAltitudeReference") -> float:
        """The altitude of the object wrt the requested reference."""
        with agmarshall.AgEnum_arg(AgEAltitudeReference, altRef) as arg_altRef, \
             agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_Altitude'](arg_altRef.COM_val, byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def Range(self, type:"AgEAccessApparentPositionType") -> float:
        """Apparent range between the objects."""
        with agmarshall.AgEnum_arg(AgEAccessApparentPositionType, type) as arg_type, \
             agmarshall.DOUBLE_arg() as arg_pRange:
            agcls.evaluate_hresult(self.__dict__['_Range'](arg_type.COM_val, byref(arg_pRange.COM_val)))
            return arg_pRange.python_val

    def RelativePosition_Array(self, type:"AgEAccessApparentPositionType", frame:"AgEUtFrame") -> list:
        """The apparent relative position of the other object with respect to this object, in the requested frame, returned as an array representing x, y, z. Only eUtFrameInertial and eUtFrameFixed are supported."""
        with agmarshall.AgEnum_arg(AgEAccessApparentPositionType, type) as arg_type, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_RelativePosition_Array'](arg_type.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def RelativeVelocity_Array(self, type:"AgEAccessApparentPositionType", frame:"AgEUtFrame") -> list:
        """The apparent relative velocity of the other object with respect to this object, in the requested frame, returned as an array representing vx, vy, vz. Only eUtFrameInertial and eUtFrameFixed are supported."""
        with agmarshall.AgEnum_arg(AgEAccessApparentPositionType, type) as arg_type, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_RelativeVelocity_Array'](arg_type.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def RelativeAcceleration_Array(self, type:"AgEAccessApparentPositionType", frame:"AgEUtFrame") -> list:
        """The apparent relative acceleration of the other object with respect to this object, in the requested frame, returned as an array representing ax, ay, az. Only eUtFrameInertial and eUtFrameFixed are supported."""
        with agmarshall.AgEnum_arg(AgEAccessApparentPositionType, type) as arg_type, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_RelativeAcceleration_Array'](arg_type.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def ApparentSunPosition_Array(self, frame:"AgEUtFrame") -> list:
        """The apparent sun position with respect to the object in the requested frame, returned as an array representing x, y, z. Only eUtFrameInertial and eUtFrameFixed are supported. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_ApparentSunPosition_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Attitude_Array(self, frame:"AgEUtFrame") -> list:
        """The attitude of the body frame of the object wrt the requested frame, returned as an array representing Q1, Q2, Q3 Q4. Only eUtFrameInertial and eUtFrameFixed are supported."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Attitude_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AngularVelocity_Array(self, frame:"AgEUtFrame") -> list:
        """The angular velocity of the body frame of the object wrt the requested frame, returned as an array representing wx, wy, wz. Only eUtFrameInertial and eUtFrameFixed are supported."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AngularVelocity_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """The current time of the object in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DateElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__['_DateString'](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry('{71D28592-CF66-4a67-A5AC-9E30FA6CF0DB}', IAgAccessConstraintPluginObjectData)
agcls.AgTypeNameMap['IAgAccessConstraintPluginObjectData'] = IAgAccessConstraintPluginObjectData
__all__.append('IAgAccessConstraintPluginObjectData')

class IAgAccessConstraintPluginResultEval(object):
    """Access Constraint Plugin Result interface for the Evaluate method."""
    _uuid = '{D7C3529C-5F6F-409a-93C9-E4D4DC36CFE9}'
    _num_methods = 16
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetValue'] = _raise_uninitialized_error
        self.__dict__['_SetValue'] = _raise_uninitialized_error
        self.__dict__['_GetMaxRelMotion'] = _raise_uninitialized_error
        self.__dict__['_SetMaxRelMotion'] = _raise_uninitialized_error
        self.__dict__['_GetStepSize'] = _raise_uninitialized_error
        self.__dict__['_SetStepSize'] = _raise_uninitialized_error
        self.__dict__['_GetIsLightTimeDelayConsidered'] = _raise_uninitialized_error
        self.__dict__['_GetLightTimeDelayFrame'] = _raise_uninitialized_error
        self.__dict__['_GetAberrationType'] = _raise_uninitialized_error
        self.__dict__['_GetLightTimeDelay'] = _raise_uninitialized_error
        self.__dict__['_GetLightPathRange'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAccessConstraintPluginResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAccessConstraintPluginResultEval from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAccessConstraintPluginResultEval = agcom.GUID(IAgAccessConstraintPluginResultEval._uuid)
        vtable_offset_local = IAgAccessConstraintPluginResultEval._vtable_offset - 1
        self.__dict__['_GetValue'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__['_SetValue'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__['_GetMaxRelMotion'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_SetMaxRelMotion'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__['_GetStepSize'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_SetStepSize'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__['_GetIsLightTimeDelayConsidered'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+7, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_GetLightTimeDelayFrame'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+8, POINTER(agcom.LONG))
        self.__dict__['_GetAberrationType'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+9, POINTER(agcom.LONG))
        self.__dict__['_GetLightTimeDelay'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__['_GetLightPathRange'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+12, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+14, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAccessConstraintPluginResultEval, vtable_offset_local+16, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAccessConstraintPluginResultEval.__dict__ and type(IAgAccessConstraintPluginResultEval.__dict__[attrname]) == property:
            return IAgAccessConstraintPluginResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAccessConstraintPluginResultEval.')
    
    @property
    def Value(self) -> float:
        """The current value of the constraint."""
        with agmarshall.DOUBLE_arg() as arg_pValue:
            agcls.evaluate_hresult(self.__dict__['_GetValue'](byref(arg_pValue.COM_val)))
            return arg_pValue.python_val

    @Value.setter
    def Value(self, newValue:float) -> None:
        """The current value of the constraint."""
        with agmarshall.DOUBLE_arg(newValue) as arg_newValue:
            agcls.evaluate_hresult(self.__dict__['_SetValue'](arg_newValue.COM_val))

    @property
    def MaxRelMotion(self) -> float:
        """Maximum relative motion (in degrees) allowed between constraint samples."""
        with agmarshall.DOUBLE_arg() as arg_pMaxRelMotion:
            agcls.evaluate_hresult(self.__dict__['_GetMaxRelMotion'](byref(arg_pMaxRelMotion.COM_val)))
            return arg_pMaxRelMotion.python_val

    @MaxRelMotion.setter
    def MaxRelMotion(self, newMaxRelMotion:float) -> None:
        """Maximum relative motion (in degrees) allowed between constraint samples."""
        with agmarshall.DOUBLE_arg(newMaxRelMotion) as arg_newMaxRelMotion:
            agcls.evaluate_hresult(self.__dict__['_SetMaxRelMotion'](arg_newMaxRelMotion.COM_val))

    @property
    def StepSize(self) -> float:
        """The current time step taken (secs)."""
        with agmarshall.DOUBLE_arg() as arg_pStepSize:
            agcls.evaluate_hresult(self.__dict__['_GetStepSize'](byref(arg_pStepSize.COM_val)))
            return arg_pStepSize.python_val

    @StepSize.setter
    def StepSize(self, newRequestedStepSize:float) -> None:
        """The requested next time step to take (secs)."""
        with agmarshall.DOUBLE_arg(newRequestedStepSize) as arg_newRequestedStepSize:
            agcls.evaluate_hresult(self.__dict__['_SetStepSize'](arg_newRequestedStepSize.COM_val))

    @property
    def IsLightTimeDelayConsidered(self) -> bool:
        """True when light time delay is considered."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__['_GetIsLightTimeDelayConsidered'](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val

    @property
    def LightTimeDelayFrame(self) -> "AgEAccessLightTimeDelayFrame":
        """Frame in which light time delay is computed."""
        with agmarshall.AgEnum_arg(AgEAccessLightTimeDelayFrame) as arg_pFrame:
            agcls.evaluate_hresult(self.__dict__['_GetLightTimeDelayFrame'](byref(arg_pFrame.COM_val)))
            return arg_pFrame.python_val

    @property
    def AberrationType(self) -> "AgEApparentPositionAberrationType":
        """The type of aberration applied"""
        with agmarshall.AgEnum_arg(AgEApparentPositionAberrationType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__['_GetAberrationType'](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    @property
    def LightTimeDelay(self) -> float:
        """Light time delay in seconds."""
        with agmarshall.DOUBLE_arg() as arg_pTimeDelayValue:
            agcls.evaluate_hresult(self.__dict__['_GetLightTimeDelay'](byref(arg_pTimeDelayValue.COM_val)))
            return arg_pTimeDelayValue.python_val

    @property
    def LightPathRange(self) -> float:
        """The range in meters between the Base and Target objects only accounting for light time delay if applied (not refraction nor aberration)."""
        with agmarshall.DOUBLE_arg() as arg_pRange:
            agcls.evaluate_hresult(self.__dict__['_GetLightPathRange'](byref(arg_pRange.COM_val)))
            return arg_pRange.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """The current time in requested time scale of the object that is the clock host expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """The current time of the object in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DateElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateString(self, dateAbbrv:str) -> str:
        """Current epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pDateString:
            agcls.evaluate_hresult(self.__dict__['_DateString'](arg_dateAbbrv.COM_val, byref(arg_pDateString.COM_val)))
            return arg_pDateString.python_val


agcls.AgClassCatalog.add_catalog_entry('{D7C3529C-5F6F-409a-93C9-E4D4DC36CFE9}', IAgAccessConstraintPluginResultEval)
agcls.AgTypeNameMap['IAgAccessConstraintPluginResultEval'] = IAgAccessConstraintPluginResultEval
__all__.append('IAgAccessConstraintPluginResultEval')


class IAgAccessConstraintPlugin(object):
    """
    Access Constraint plugin interface for an  Access Constraint.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def DisplayName(self) -> str:
        """Triggered when the plugin is being registered. This is the name of the constraint used by STK."""
        raise STKPluginMethodNotImplementedError('DisplayName was not implemented.')

    def Register(self, result:"IAgAccessConstraintPluginResultRegister") -> None:
        """Triggered after application start-up, in order to register the constraint for specific STK object pairs for which this constraint is applicable."""
        raise STKPluginMethodNotImplementedError('Register was not implemented.')

    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered just before the first computational event trigger."""
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def PreCompute(self, result:"IAgAccessConstraintPluginResultPreCompute") -> bool:
        """Triggered prior to the calls to the Evaluate method, to allow for any required initialization."""
        raise STKPluginMethodNotImplementedError('PreCompute was not implemented.')

    def Evaluate(self, result:"IAgAccessConstraintPluginResultEval", baseData:"IAgAccessConstraintPluginObjectData", targetData:"IAgAccessConstraintPluginObjectData") -> bool:
        """Triggered when the plugin is evaluated for an access constraint value"""
        raise STKPluginMethodNotImplementedError('Evaluate was not implemented.')

    def PostCompute(self, result:"IAgAccessConstraintPluginResultPostCompute") -> bool:
        """Triggered after the calls to the Evaluate method, to allow for any required clean up."""
        raise STKPluginMethodNotImplementedError('PostCompute was not implemented.')

    def Free(self) -> None:
        """Triggered just before the plugin is destroyed."""
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

__all__.append('IAgAccessConstraintPlugin')



class AgAccessConstraintPluginResultRegister(IAgAccessConstraintPluginResultRegister):
    """Access Constraint Registration interface for the Register method."""
    def __init__(self, sourceObject=None):
        IAgAccessConstraintPluginResultRegister.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAccessConstraintPluginResultRegister._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAccessConstraintPluginResultRegister._get_property(self, attrname) is not None: found_prop = IAgAccessConstraintPluginResultRegister._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAccessConstraintPluginResultRegister.')
        
agcls.AgClassCatalog.add_catalog_entry('{18D5B422-C74C-4DDE-9810-82CAE663753B}', AgAccessConstraintPluginResultRegister)
__all__.append('AgAccessConstraintPluginResultRegister')


class AgAccessConstraintPluginObjectData(IAgAccessConstraintPluginObjectData):
    """Access Constraint Plugin Object Data interface used to get inputs and outputs during the Evaluate method call."""
    def __init__(self, sourceObject=None):
        IAgAccessConstraintPluginObjectData.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAccessConstraintPluginObjectData._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAccessConstraintPluginObjectData._get_property(self, attrname) is not None: found_prop = IAgAccessConstraintPluginObjectData._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAccessConstraintPluginObjectData.')
        
agcls.AgClassCatalog.add_catalog_entry('{BF083607-3516-4F1E-9591-BB2E962266D4}', AgAccessConstraintPluginObjectData)
__all__.append('AgAccessConstraintPluginObjectData')


class AgAccessConstraintPluginObjectDescriptor(IAgAccessConstraintPluginObjectDescriptor):
    """Access Constraint Plugin Object Descriptor interface."""
    def __init__(self, sourceObject=None):
        IAgAccessConstraintPluginObjectDescriptor.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAccessConstraintPluginObjectDescriptor._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAccessConstraintPluginObjectDescriptor._get_property(self, attrname) is not None: found_prop = IAgAccessConstraintPluginObjectDescriptor._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAccessConstraintPluginObjectDescriptor.')
        
agcls.AgClassCatalog.add_catalog_entry('{62B3AC51-4E29-4721-9833-52522D028DA3}', AgAccessConstraintPluginObjectDescriptor)
__all__.append('AgAccessConstraintPluginObjectDescriptor')


class AgAccessConstraintPluginResultPreCompute(IAgAccessConstraintPluginResultPreCompute):
    """Access Constraint Plugin Result interface for the PreCompute method."""
    def __init__(self, sourceObject=None):
        IAgAccessConstraintPluginResultPreCompute.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAccessConstraintPluginResultPreCompute._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAccessConstraintPluginResultPreCompute._get_property(self, attrname) is not None: found_prop = IAgAccessConstraintPluginResultPreCompute._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAccessConstraintPluginResultPreCompute.')
        
agcls.AgClassCatalog.add_catalog_entry('{FB57C0E4-6DEC-4D30-8C0A-169640250392}', AgAccessConstraintPluginResultPreCompute)
__all__.append('AgAccessConstraintPluginResultPreCompute')


class AgAccessConstraintPluginResultEval(IAgAccessConstraintPluginResultEval):
    """Access Constraint Plugin Result interface for the Evaluate method."""
    def __init__(self, sourceObject=None):
        IAgAccessConstraintPluginResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAccessConstraintPluginResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAccessConstraintPluginResultEval._get_property(self, attrname) is not None: found_prop = IAgAccessConstraintPluginResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAccessConstraintPluginResultEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{700080FC-AD4D-4A7B-85D5-567647DE4ABC}', AgAccessConstraintPluginResultEval)
__all__.append('AgAccessConstraintPluginResultEval')


class AgAccessConstraintPluginResultPostCompute(IAgAccessConstraintPluginResultPostCompute):
    """Access Constraint Plugin Result interface for the PostCompute method."""
    def __init__(self, sourceObject=None):
        IAgAccessConstraintPluginResultPostCompute.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAccessConstraintPluginResultPostCompute._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAccessConstraintPluginResultPostCompute._get_property(self, attrname) is not None: found_prop = IAgAccessConstraintPluginResultPostCompute._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAccessConstraintPluginResultPostCompute.')
        
agcls.AgClassCatalog.add_catalog_entry('{8C0E2421-7B95-4B10-8B01-110E03559054}', AgAccessConstraintPluginResultPostCompute)
__all__.append('AgAccessConstraintPluginResultPostCompute')



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
