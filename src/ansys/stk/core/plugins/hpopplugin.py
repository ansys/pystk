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


def _raise_uninitialized_error(*args):
    raise STKRuntimeError('Valid STK object model classes are returned from STK methods and should not be created independently.')

class AgEForceModelType(IntEnum):
    """Enumeration of force model contributors"""
    # Gravity.
    eGravityModel = 0,
    # Solid tides.
    eSolidTidesModel = 1,
    # Ocean Tides.
    eOceanTidesModel = 2,
    # Atmospheric drag.
    eDragModel = 3,
    # Solar radiation pressure.
    eSRPModel = 4,
    # Third bodies.
    eThirdBodyModel = 5,
    # General relativity effects.
    eGenRelativityModel = 6,
    # Albedo (solar radiation reflected from central body).
    eAlbedoModel = 7,
    # Thermal radiation pressure from central body.
    eThermalRadiationPressureModel = 8,
    # Atmospheric Density.
    eDensityModel = 9

agcls.AgTypeNameMap['AgEForceModelType'] = AgEForceModelType
__all__.append('AgEForceModelType')

class AgEAsHpopPluginErrorCodes(IntEnum):
    """Enumeration of AgAsHpopPlugin General Error Codes"""
    # Hpop Plugin: An internal failure occurred.
    eHpopPluginErrorInternalFailure = (((1 << 31) | (4 << 16)) | 0x101),
    # Hpop Plugin: Not configured properly.
    eHpopPluginErrorNotConfigured = (((1 << 31) | (4 << 16)) | 0x102),
    # Hpop Plugin: SRP is turned off.
    eHpopPluginErrorSRPIsOff = (((1 << 31) | (4 << 16)) | 0x103),
    # Hpop Plugin: Drag is turned off.
    eHpopPluginErrorDragIsOff = (((1 << 31) | (4 << 16)) | 0x104),
    # Hpop Plugin: Gravity field is undefined.
    eHpopPluginErrorGravityFieldUndefined = (((1 << 31) | (4 << 16)) | 0x105),
    # Hpop Plugin: Force Model Type was not found.
    eHpopPluginErrorForceModelTypeNotFound = (((1 << 31) | (4 << 16)) | 0x106),
    # Hpop Plugin: The Square Root of an invalid value occurred.
    eHpopPluginErrorInvalidSquareRoot = (((1 << 31) | (4 << 16)) | 0x107),
    # Hpop Plugin: Density model does not provide temperature.
    eHpopPluginErrorTemperatureUnavailable = (((1 << 31) | (4 << 16)) | 0x108),
    # Hpop Plugin: Density model does not provide pressure.
    eHpopPluginErrorPressureUnavailable = (((1 << 31) | (4 << 16)) | 0x109),
    # Hpop Plugin: The acceleration type provided as input was invalid. Valid values range from 0 to 10.
    eHpopPluginErrorInvalidAccelerationType = (((1 << 31) | (4 << 16)) | 0x10A),
    # Hpop Plugin: Both albedo and thermal radiation pressure accelerations are off.
    eHpopPluginErrorRadiationPressureIsOff = (((1 << 31) | (4 << 16)) | 0x10B),
    # Hpop Plugin: Fuel mass is not available in HPOP.
    eHpopPluginErrorNoFuel = (((1 << 31) | (4 << 16)) | 0x10C),
    # Hpop Plugin: Not using a flux file.
    eHpopPluginErrorNotUsingFluxFile = (((1 << 31) | (4 << 16)) | 0x10D),
    # Hpop Plugin: Can't set total mass in Astrogator.  Set dry mass or fuel mass.
    eHpopPluginErrorSetTotalMassInvalid = (((1 << 31) | (4 << 16)) | 0x10E)

agcls.AgTypeNameMap['AgEAsHpopPluginErrorCodes'] = AgEAsHpopPluginErrorCodes
__all__.append('AgEAsHpopPluginErrorCodes')

class AgEAsHpopPluginEventIndicators(IntEnum):
    """Enumeration of AgAsHpopPlugin Event Indicators"""
    # Stops propagation.
    eHpopPluginEventIndicatorsStopPropagation = 0,
    # Ends current segment.
    eHpopPluginEventIndicatorsStopSegment = 1,
    # Marks a discontinuity.
    eHpopPluginEventIndicatorsMarkDiscontinuity = 2

agcls.AgTypeNameMap['AgEAsHpopPluginEventIndicators'] = AgEAsHpopPluginEventIndicators
__all__.append('AgEAsHpopPluginEventIndicators')

class AgEAccelType(IntEnum):
    """Enumeration of contributions to the total force model acceleration"""
    # Total accleration.
    eTotalAccel = 0,
    # Two body contribution.
    eTwoBodyAccel = 1,
    # Contribution of the total gravity field.
    eGravityAccel = 2,
    # Contribution of the total gravity field minus the two body contribution.
    ePerturbedGravityAccel = 3,
    # Contribution of solid tides.  Will be zero if the force model is not set to consider this effect.
    eSolidTidesAccel = 4,
    # Contribution of ocean tides.  Will be zero if the force model is not set to consider this effect.
    eOceanTidesAccel = 5,
    # Contribution of atmospheric drag.  Will be zero if the force model is not set to consider this effect.
    eDragAccel = 6,
    # Contribution of solar radiation pressure.  Will be zero if the force model is not set to consider this effect.
    eSRPAccel = 7,
    # Contribution of all third bodies.  Will be zero if the force model is not considering any third body forces.
    eThirdBodyAccel = 8,
    # Contribution of general relativity effects.  Will be zero if the force model is not set to consider this effect.
    eGenRelativityAccel = 9,
    # Contribution of any additional acceleration, say by a plugin.
    eAddedAccel = 10,
    # Contribution of albedo (reflected solar radiation pressure).
    eAlbedoAccel = 11,
    # Contribution of thermal radiation pressure.
    eThermalRadiationPressureAccel = 12

agcls.AgTypeNameMap['AgEAccelType'] = AgEAccelType
__all__.append('AgEAccelType')

class AgEAsLightReflectionErrorCodes(IntEnum):
    """Enumeration of AgAsLightReflectionPlugin General Error Codes"""
    # LightReflection Plugin: An internal failure occurred.
    eLightReflectionErrorInternalFailure = (((1 << 31) | (4 << 16)) | 0x101),
    # LightReflection Plugin: Not configured properly.
    eLightReflectionErrorNotConfigured = (((1 << 31) | (4 << 16)) | 0x102),
    # LightReflection Plugin: Cannot transform vector from requested frame to specified frame.
    eLightReflectionErrorTransformFailure = (((1 << 31) | (4 << 16)) | 0x103),
    # LightReflection Plugin: Cannot set reflectance.
    eLightReflectionErrorSetReflectanceFailure = (((1 << 31) | (4 << 16)) | 0x104),
    # LightReflection Plugin: Cannot set reflectance partials.
    eLightReflectionErrorSetReflectancePartialsFailure = (((1 << 31) | (4 << 16)) | 0x105),
    # LightReflection Plugin: The index number for the parameter is out of range.
    eLightReflectionErrorParameterIndexOutOfRange = (((1 << 31) | (4 << 16)) | 0x106),
    # LightReflection Plugin:  Cannot set parameter partials.
    eLightReflectionErrorParameterPartialsFailure = (((1 << 31) | (4 << 16)) | 0x107),
    # LightReflection Plugin: Input value is not a real number.  Check for divide by zero.
    eLightReflectionErrorPluginInputNotReal = (((1 << 31) | (4 << 16)) | 0x108),
    # LightReflection Plugin: The parameter cannot be found.
    eLightReflectionErrorParameterNotFound = (((1 << 31) | (4 << 16)) | 0x109)

agcls.AgTypeNameMap['AgEAsLightReflectionErrorCodes'] = AgEAsLightReflectionErrorCodes
__all__.append('AgEAsLightReflectionErrorCodes')

class AgEAsDragModelErrorCodes(IntEnum):
    """Enumeration of AgAsDragModelPlugin General Error Codes"""
    # DragModel Plugin: An internal failure occurred.
    eDragModelErrorInternalFailure = (((1 << 31) | (4 << 16)) | 0x101),
    # DragModel Plugin: Not configured properly.
    eDragModelErrorNotConfigured = (((1 << 31) | (4 << 16)) | 0x102),
    # DragModel Plugin: Cannot transform vector from requested frame to specified frame.
    eDragModelErrorTransformFailure = (((1 << 31) | (4 << 16)) | 0x103),
    # DragModel Plugin: Cannot set reflectance.
    eDragModelErrorSetReflectanceFailure = (((1 << 31) | (4 << 16)) | 0x104),
    # DragModel Plugin: Cannot set reflectance partials.
    eDragModelErrorSetReflectancePartialsFailure = (((1 << 31) | (4 << 16)) | 0x105),
    # DragModel Plugin: The index number for the parameter is out of range.
    eDragModelErrorParameterIndexOutOfRange = (((1 << 31) | (4 << 16)) | 0x106),
    # DragModel Plugin:  Cannot set parameter partials.
    eDragModelErrorParameterPartialsFailure = (((1 << 31) | (4 << 16)) | 0x107),
    # DensityModel Plugin: Input value is not a real number.  Check for divide by zero.
    eDragModelErrorInputNotReal = (((1 << 31) | (4 << 16)) | 0x108),
    # DragModel Plugin: The parameter cannot be found.
    eDragModelErrorParameterNotFound = (((1 << 31) | (4 << 16)) | 0x109)

agcls.AgTypeNameMap['AgEAsDragModelErrorCodes'] = AgEAsDragModelErrorCodes
__all__.append('AgEAsDragModelErrorCodes')

class AgEAsEOMFuncPluginErrorCodes(IntEnum):
    """Enumeration of AgAsEOMFuncPlugin General Error Codes"""
    # EOMFunc Plugin: An internal failure occurred.
    eEOMFuncPluginErrorInternalFailure = (((1 << 31) | (4 << 16)) | 0x101),
    # EOMFunc Plugin: Not configured properly.
    eEOMFuncPluginErrorNotConfigured = (((1 << 31) | (4 << 16)) | 0x102),
    # EOMFunc Plugin: Index out of valid range.
    eEOMFuncPluginErrorIndexOutOfRange = (((1 << 31) | (4 << 16)) | 0x103),
    # EOMFunc Plugin: Variable not registered as input.
    eEOMFuncPluginErrorInputNotRegistered = (((1 << 31) | (4 << 16)) | 0x104),
    # EOMFunc Plugin: Variable not registered as parameter output.
    eEOMFuncPluginErrorParamOutputNotRegistered = (((1 << 31) | (4 << 16)) | 0x105),
    # EOMFunc Plugin: Variable not registered as derivative output.
    eEOMFuncPluginErrorDerivOutputNotRegistered = (((1 << 31) | (4 << 16)) | 0x106),
    # EOMFunc Plugin: Invalid state variable.
    eEOMFuncPluginErrorInvalidStateVariable = (((1 << 31) | (4 << 16)) | 0x107),
    # EOMFunc Plugin: Invalid event type.
    eEOMFuncPluginErrorInvalidEventType = (((1 << 31) | (4 << 16)) | 0x108),
    # EOMFunc Plugin: Input value is not a real number.  Check for divide by zero.
    eEOMFuncPluginErrorInputNotReal = (((1 << 31) | (4 << 16)) | 0x109)

agcls.AgTypeNameMap['AgEAsEOMFuncPluginErrorCodes'] = AgEAsEOMFuncPluginErrorCodes
__all__.append('AgEAsEOMFuncPluginErrorCodes')

class AgEAsEOMFuncPluginInputStateValues(IntEnum):
    """Enumeration of state vector input values"""
    # X-component of position (inertial).
    eEOMFuncPluginInputStateValuesPosX = 0,
    # Y-component of position (inertial).
    eEOMFuncPluginInputStateValuesPosY = 1,
    # Z-component of position (inertial).
    eEOMFuncPluginInputStateValuesPosZ = 2,
    # X-component of velocity (inertial).
    eEOMFuncPluginInputStateValuesVelX = 3,
    # Y-component of velocity (inertial).
    eEOMFuncPluginInputStateValuesVelY = 4,
    # Z-component of velocity (inertial).
    eEOMFuncPluginInputStateValuesVelZ = 5,
    # X-component of position (fixed).
    eEOMFuncPluginInputStateValuesPosCBFX = 6,
    # Y-component of position (fixed)
    eEOMFuncPluginInputStateValuesPosCBFY = 7,
    # Z-component of position (fixed)
    eEOMFuncPluginInputStateValuesPosCBFZ = 8,
    # X-component of velocity (fixed)
    eEOMFuncPluginInputStateValuesVelCBFX = 9,
    # Y-component of velocity (fixed)
    eEOMFuncPluginInputStateValuesVelCBFY = 10,
    # Z-component of velocity (fixed)
    eEOMFuncPluginInputStateValuesVelCBFZ = 11,
    # X-component of inertial velocity expressed in fixed frame
    eEOMFuncPluginInputStateValuesCBIVelInCBFX = 12,
    # Y-component of inertial velocity expressed in fixed frame
    eEOMFuncPluginInputStateValuesCBIVelInCBFY = 13,
    # Z-component of inertial velocity expressed in fixed frame
    eEOMFuncPluginInputStateValuesCBIVelInCBFZ = 14,
    # Quaternion1
    eEOMFuncPluginInputStateValuesQuat1 = 15,
    # Quaternion2
    eEOMFuncPluginInputStateValuesQuat2 = 16,
    # Quaternion3
    eEOMFuncPluginInputStateValuesQuat3 = 17,
    # Quaternion4
    eEOMFuncPluginInputStateValuesQuat4 = 18,
    # 0,0 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF00 = 19,
    # 0,1 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF01 = 20,
    # 0,2 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF02 = 21,
    # 1,0 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF10 = 22,
    # 1,1 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF11 = 23,
    # 1,2 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF12 = 24,
    # 2,0 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF20 = 25,
    # 2,1 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF21 = 26,
    # 2,2 entry of CBI to CBF rotation matrix
    eEOMFuncPluginInputStateValuesCBIToCBF22 = 27,
    # X-component of angular velocity in fixed frame
    eEOMFuncPluginInputStateValuesAngVelCBFX = 28,
    # Y-component of angular velocity in fixed frame
    eEOMFuncPluginInputStateValuesAngVelCBFY = 29,
    # Z-component of angular velocity in fixed frame
    eEOMFuncPluginInputStateValuesAngVelCBFZ = 30,
    # Altitude
    eEOMFuncPluginInputStateValuesAltitude = 31,
    # Latitude
    eEOMFuncPluginInputStateValuesLatitude = 32,
    # Longitude
    eEOMFuncPluginInputStateValuesLongitude = 33,
    # Total mass.
    eEOMFuncPluginInputStateValuesTotalMass = 34,
    # Dry mass.
    eEOMFuncPluginInputStateValuesDryMass = 35,
    # Fuel mass.
    eEOMFuncPluginInputStateValuesFuelMass = 36,
    # Drag coefficient (Cd).
    eEOMFuncPluginInputStateValuesCd = 37,
    # Drag area.
    eEOMFuncPluginInputStateValuesDragArea = 38,
    # Atmospheric density
    eEOMFuncPluginInputStateValuesAtmosphericDensity = 39,
    # Atmospheric altitude
    eEOMFuncPluginInputStateValuesAtmosphericAltitude = 40,
    # SRP coefficient (Cr).
    eEOMFuncPluginInputStateValuesCr = 41,
    # SRP area.
    eEOMFuncPluginInputStateValuesSRPArea = 42,
    # Kr1 parameter of GPS SRP models
    eEOMFuncPluginInputStateValuesKr1 = 43,
    # Kr2 parameter of GPS SRP models
    eEOMFuncPluginInputStateValuesKr2 = 44,
    # ApparentToTrueCbSunPosCBFX
    eEOMFuncPluginInputStateValuesApparentToTrueCbSunPosCBFX = 45,
    # ApparentToTrueCbSunPosCBFY
    eEOMFuncPluginInputStateValuesApparentToTrueCbSunPosCBFY = 46,
    # ApparentToTrueCbSunPosCBFZ
    eEOMFuncPluginInputStateValuesApparentToTrueCbSunPosCBFZ = 47,
    # ApparentToTrueCbSatPosCBFX
    eEOMFuncPluginInputStateValuesApparentToTrueCbSatPosCBFX = 48,
    # ApparentToTrueCbSatPosCBFY
    eEOMFuncPluginInputStateValuesApparentToTrueCbSatPosCBFY = 49,
    # ApparentToTrueCbSatPosCBFZ
    eEOMFuncPluginInputStateValuesApparentToTrueCbSatPosCBFZ = 50,
    # ApparentToTrueCbSatToSunCBIPosX
    eEOMFuncPluginInputStateValuesApparentToTrueCbSatToSunCBIPosX = 51,
    # ApparentToTrueCbSatToSunCBIPosY
    eEOMFuncPluginInputStateValuesApparentToTrueCbSatToSunCBIPosY = 52,
    # ApparentToTrueCbSatToSunCBIPosZ
    eEOMFuncPluginInputStateValuesApparentToTrueCbSatToSunCBIPosZ = 53,
    # ApparentSunPosCBFX
    eEOMFuncPluginInputStateValuesApparentSunPosCBFX = 54,
    # ApparentSunPosCBFY
    eEOMFuncPluginInputStateValuesApparentSunPosCBFY = 55,
    # ApparentSunPosCBFZ
    eEOMFuncPluginInputStateValuesApparentSunPosCBFZ = 56,
    # ApparentSatPosCBFX
    eEOMFuncPluginInputStateValuesApparentSatPosCBFX = 57,
    # ApparentSatPosCBFY
    eEOMFuncPluginInputStateValuesApparentSatPosCBFY = 58,
    # ApparentSatPosCBFZ
    eEOMFuncPluginInputStateValuesApparentSatPosCBFZ = 59,
    # ApparentSatToSunCBIPosX
    eEOMFuncPluginInputStateValuesApparentSatToSunCBIPosX = 60,
    # ApparentSatToSunCBIPosY
    eEOMFuncPluginInputStateValuesApparentSatToSunCBIPosY = 61,
    # ApparentSatToSunCBIPosZ
    eEOMFuncPluginInputStateValuesApparentSatToSunCBIPosZ = 62,
    # TrueSunPosCBFX
    eEOMFuncPluginInputStateValuesTrueSunPosCBFX = 63,
    # TrueSunPosCBFY
    eEOMFuncPluginInputStateValuesTrueSunPosCBFY = 64,
    # TrueSunPosCBFZ
    eEOMFuncPluginInputStateValuesTrueSunPosCBFZ = 65,
    # TrueSatPosCBFX
    eEOMFuncPluginInputStateValuesTrueSatPosCBFX = 66,
    # TrueSatPosCBFY
    eEOMFuncPluginInputStateValuesTrueSatPosCBFY = 67,
    # TrueSatPosCBFZ
    eEOMFuncPluginInputStateValuesTrueSatPosCBFZ = 68,
    # TrueSatToSunCBIPosX
    eEOMFuncPluginInputStateValuesTrueSatToSunCBIPosX = 69,
    # TrueSatToSunCBIPosY
    eEOMFuncPluginInputStateValuesTrueSatToSunCBIPosY = 70,
    # TrueSatToSunCBIPosZ
    eEOMFuncPluginInputStateValuesTrueSatToSunCBIPosZ = 71,
    # Solar intensity
    eEOMFuncPluginInputStateValuesSolarIntensity = 72,
    # Radiation pressure coefficient.
    eEOMFuncPluginInputStateValuesRadPressureCoefficient = 73,
    # Radiation pressure area.
    eEOMFuncPluginInputStateValuesRadPressureArea = 74,
    # Mass flow rate.
    eEOMFuncPluginInputStateValuesMassFlowRate = 75,
    # Tank pressure.
    eEOMFuncPluginInputStateValuesTankPressure = 76,
    # Tank temperature.
    eEOMFuncPluginInputStateValuesTankTemperature = 77,
    # Fuel density.
    eEOMFuncPluginInputStateValuesFuelDensity = 78,
    # x-component of thrust
    eEOMFuncPluginInputStateValuesThrustX = 79,
    # y-component of thrust.
    eEOMFuncPluginInputStateValuesThrustY = 80,
    # z-component of thrust.
    eEOMFuncPluginInputStateValuesThrustZ = 81,
    # Delta-V (integrated).
    eEOMFuncPluginInputStateValuesDeltaV = 82,
    # GravityAccelX
    eEOMFuncPluginInputStateValuesGravityAccelX = 83,
    # GravityAccelY
    eEOMFuncPluginInputStateValuesGravityAccelY = 84,
    # GravityAccelZ
    eEOMFuncPluginInputStateValuesGravityAccelZ = 85,
    # TwoBodyAccelX
    eEOMFuncPluginInputStateValuesTwoBodyAccelX = 86,
    # TwoBodyAccelY
    eEOMFuncPluginInputStateValuesTwoBodyAccelY = 87,
    # TwoBodyAccelZ
    eEOMFuncPluginInputStateValuesTwoBodyAccelZ = 88,
    # GravityPertAccelX
    eEOMFuncPluginInputStateValuesGravityPertAccelX = 89,
    # GravityPertAccelY
    eEOMFuncPluginInputStateValuesGravityPertAccelY = 90,
    # GravityPertAccelZ
    eEOMFuncPluginInputStateValuesGravityPertAccelZ = 91,
    # SolidTidesAccelX
    eEOMFuncPluginInputStateValuesSolidTidesAccelX = 92,
    # SolidTidesAccelY
    eEOMFuncPluginInputStateValuesSolidTidesAccelY = 93,
    # SolidTidesAccelZ
    eEOMFuncPluginInputStateValuesSolidTidesAccelZ = 94,
    # OceanTidesAccelX
    eEOMFuncPluginInputStateValuesOceanTidesAccelX = 95,
    # OceanTidesAccelY
    eEOMFuncPluginInputStateValuesOceanTidesAccelY = 96,
    # OceanTidesAccelZ
    eEOMFuncPluginInputStateValuesOceanTidesAccelZ = 97,
    # DragAccelX
    eEOMFuncPluginInputStateValuesDragAccelX = 98,
    # DragAccelY
    eEOMFuncPluginInputStateValuesDragAccelY = 99,
    # DragAccelZ
    eEOMFuncPluginInputStateValuesDragAccelZ = 100,
    # ThirdBodyAccelX
    eEOMFuncPluginInputStateValuesThirdBodyAccelX = 101,
    # ThirdBodyAccelY
    eEOMFuncPluginInputStateValuesThirdBodyAccelY = 102,
    # ThirdBodyAccelZ
    eEOMFuncPluginInputStateValuesThirdBodyAccelZ = 103,
    # SRPAccelX
    eEOMFuncPluginInputStateValuesSRPAccelX = 104,
    # SRPAccelY
    eEOMFuncPluginInputStateValuesSRPAccelY = 105,
    # SRPAccelZ
    eEOMFuncPluginInputStateValuesSRPAccelZ = 106,
    # X-component of SRP acceleration without accounting for shadow
    eEOMFuncPluginInputStateValuesNoShadowSRPAccelX = 107,
    # Y-component of SRP acceleration without accounting for shadow
    eEOMFuncPluginInputStateValuesNoShadowSRPAccelY = 108,
    # Z-component of SRP acceleration without accounting for shadow
    eEOMFuncPluginInputStateValuesNoShadowSRPAccelZ = 109,
    # GenRelAccelX
    eEOMFuncPluginInputStateValuesGenRelAccelX = 110,
    # GenRelAccelY
    eEOMFuncPluginInputStateValuesGenRelAccelY = 111,
    # GenRelAccelZ
    eEOMFuncPluginInputStateValuesGenRelAccelZ = 112,
    # AlbedoAccelX
    eEOMFuncPluginInputStateValuesAlbedoAccelX = 113,
    # AlbedoAccelY
    eEOMFuncPluginInputStateValuesAlbedoAccelY = 114,
    # AlbedoAccelZ
    eEOMFuncPluginInputStateValuesAlbedoAccelZ = 115,
    # ThermalPressureAccelX
    eEOMFuncPluginInputStateValuesThermalPressureAccelX = 116,
    # ThermalPressureAccelY
    eEOMFuncPluginInputStateValuesThermalPressureAccelY = 117,
    # ThermalPressureAccelZ
    eEOMFuncPluginInputStateValuesThermalPressureAccelZ = 118,
    # X-component of acceleration added by plugins
    eEOMFuncPluginInputStateValuesAddedAccelX = 119,
    # Y-component of acceleration added by plugins
    eEOMFuncPluginInputStateValuesAddedAccelY = 120,
    # Z-component of acceleration added by plugins
    eEOMFuncPluginInputStateValuesAddedAccelZ = 121,
    # StateTransPosXPosX
    eEOMFuncPluginInputStateValuesStateTransPosXPosX = 122,
    # StateTransPosXPosY
    eEOMFuncPluginInputStateValuesStateTransPosXPosY = 123,
    # StateTransPosXPosZ
    eEOMFuncPluginInputStateValuesStateTransPosXPosZ = 124,
    # StateTransPosXVelX
    eEOMFuncPluginInputStateValuesStateTransPosXVelX = 125,
    # StateTransPosXVelY
    eEOMFuncPluginInputStateValuesStateTransPosXVelY = 126,
    # StateTransPosXVelZ
    eEOMFuncPluginInputStateValuesStateTransPosXVelZ = 127,
    # StateTransPosYPosX
    eEOMFuncPluginInputStateValuesStateTransPosYPosX = 128,
    # StateTransPosYPosY
    eEOMFuncPluginInputStateValuesStateTransPosYPosY = 129,
    # StateTransPosYPosZ
    eEOMFuncPluginInputStateValuesStateTransPosYPosZ = 130,
    # StateTransPosYVelX
    eEOMFuncPluginInputStateValuesStateTransPosYVelX = 131,
    # StateTransPosYVelY
    eEOMFuncPluginInputStateValuesStateTransPosYVelY = 132,
    # StateTransPosYVelZ
    eEOMFuncPluginInputStateValuesStateTransPosYVelZ = 133,
    # StateTransPosZPosX
    eEOMFuncPluginInputStateValuesStateTransPosZPosX = 134,
    # StateTransPosZPosY
    eEOMFuncPluginInputStateValuesStateTransPosZPosY = 135,
    # StateTransPosZPosZ
    eEOMFuncPluginInputStateValuesStateTransPosZPosZ = 136,
    # StateTransPosZVelX
    eEOMFuncPluginInputStateValuesStateTransPosZVelX = 137,
    # StateTransPosZVelY
    eEOMFuncPluginInputStateValuesStateTransPosZVelY = 138,
    # StateTransPosZVelZ
    eEOMFuncPluginInputStateValuesStateTransPosZVelZ = 139,
    # StateTransVelXPosX
    eEOMFuncPluginInputStateValuesStateTransVelXPosX = 140,
    # StateTransVelXPosY
    eEOMFuncPluginInputStateValuesStateTransVelXPosY = 141,
    # StateTransVelXPosZ
    eEOMFuncPluginInputStateValuesStateTransVelXPosZ = 142,
    # StateTransVelXVelX
    eEOMFuncPluginInputStateValuesStateTransVelXVelX = 143,
    # StateTransVelXVelY
    eEOMFuncPluginInputStateValuesStateTransVelXVelY = 144,
    # StateTransVelXVelZ
    eEOMFuncPluginInputStateValuesStateTransVelXVelZ = 145,
    # StateTransVelYPosX
    eEOMFuncPluginInputStateValuesStateTransVelYPosX = 146,
    # StateTransVelYPosY
    eEOMFuncPluginInputStateValuesStateTransVelYPosY = 147,
    # StateTransVelYPosZ
    eEOMFuncPluginInputStateValuesStateTransVelYPosZ = 148,
    # StateTransVelYVelX
    eEOMFuncPluginInputStateValuesStateTransVelYVelX = 149,
    # StateTransVelYVelY
    eEOMFuncPluginInputStateValuesStateTransVelYVelY = 150,
    # StateTransVelYVelZ
    eEOMFuncPluginInputStateValuesStateTransVelYVelZ = 151,
    # StateTransVelZPosX
    eEOMFuncPluginInputStateValuesStateTransVelZPosX = 152,
    # StateTransVelZPosY
    eEOMFuncPluginInputStateValuesStateTransVelZPosY = 153,
    # StateTransVelZPosZ
    eEOMFuncPluginInputStateValuesStateTransVelZPosZ = 154,
    # StateTransVelZVelX
    eEOMFuncPluginInputStateValuesStateTransVelZVelX = 155,
    # StateTransVelZVelY
    eEOMFuncPluginInputStateValuesStateTransVelZVelY = 156,
    # StateTransVelZVelZ
    eEOMFuncPluginInputStateValuesStateTransVelZVelZ = 157

agcls.AgTypeNameMap['AgEAsEOMFuncPluginInputStateValues'] = AgEAsEOMFuncPluginInputStateValues
__all__.append('AgEAsEOMFuncPluginInputStateValues')

class AgEAsEOMFuncPluginOutputStateValues(IntEnum):
    """Enumeration of state vector output values"""
    # Dry mass.
    eEOMFuncPluginOutputStateValuesDryMass = 0,
    # Fuel mass.
    eEOMFuncPluginOutputStateValuesFuelMass = 1,
    # Drag coefficient (Cd).
    eEOMFuncPluginOutputStateValuesCd = 2,
    # Drag area.
    eEOMFuncPluginOutputStateValuesDragArea = 3,
    # Atmospheric density
    eEOMFuncPluginOutputStateValuesAtmosphericDensity = 4,
    # Atmospheric altitude
    eEOMFuncPluginOutputStateValuesAtmosphericAltitude = 5,
    # SRP coefficient (Cr).
    eEOMFuncPluginOutputStateValuesCr = 6,
    # SRP area.
    eEOMFuncPluginOutputStateValuesSRPArea = 7,
    # Kr1 parameter of GPS SRP models
    eEOMFuncPluginOutputStateValuesKr1 = 8,
    # Kr2 parameter of GPS SRP models
    eEOMFuncPluginOutputStateValuesKr2 = 9,
    # Solar intensity
    eEOMFuncPluginOutputStateValuesSolarIntensity = 10,
    # Radiation pressure coefficient.
    eEOMFuncPluginOutputStateValuesRadPressureCoefficient = 11,
    # Radiation pressure area.
    eEOMFuncPluginOutputStateValuesRadPressureArea = 12

agcls.AgTypeNameMap['AgEAsEOMFuncPluginOutputStateValues'] = AgEAsEOMFuncPluginOutputStateValues
__all__.append('AgEAsEOMFuncPluginOutputStateValues')

class AgEAsEOMFuncPluginEventTypes(IntEnum):
    """Enumeration of event types"""
    # Pre-propagate
    eEOMFuncPluginEventTypesPrePropagate = 0,
    # Pre-next step
    eEOMFuncPluginEventTypesPreNextStep = 1,
    # Evaluate
    eEOMFuncPluginEventTypesEvaluate = 2,
    # Post-propagate
    eEOMFuncPluginEventTypesPostPropagate = 3

agcls.AgTypeNameMap['AgEAsEOMFuncPluginEventTypes'] = AgEAsEOMFuncPluginEventTypes
__all__.append('AgEAsEOMFuncPluginEventTypes')

class AgEAsDensityModelErrorCodes(IntEnum):
    """Enumeration of AgAsDensityModelPlugin General Error Codes"""
    # DensityModel Plugin: An internal failure occurred.
    eDensityModelPluginInternalFailure = (((1 << 31) | (4 << 16)) | 0x101),
    # DensityModel Plugin: Not configured properly.
    eDensityModelPluginNotConfigured = (((1 << 31) | (4 << 16)) | 0x102),
    # DensityModel Plugin: Cannot set density.
    eDensityModelPluginSetDensityFailure = (((1 << 31) | (4 << 16)) | 0x103),
    # DensityModel Plugin: Cannot set temperature.
    eDensityModelPluginSetTemperatureFailure = (((1 << 31) | (4 << 16)) | 0x104),
    # DensityModel Plugin: Cannot set pressure.
    eDensityModelPluginSetPressureFailure = (((1 << 31) | (4 << 16)) | 0x105),
    # DensityModel Plugin: The index number for the parameter is out of range.
    eDensityModelPluginParameterIndexOutOfRange = (((1 << 31) | (4 << 16)) | 0x106),
    # DensityModel Plugin: Input value is not a real number.  Check for divide by zero.
    eDensityModelPluginInputNotReal = (((1 << 31) | (4 << 16)) | 0x107),
    # DensityModel Plugin: Not using a flux file.
    eDensityModelPluginNotUsingFluxFile = (((1 << 31) | (4 << 16)) | 0x108),
    # DensityModel Plugin: Data file or some indicies null.
    eDensityModelPluginNullData = (((1 << 31) | (4 << 16)) | 0x109),
    # DensityModel Plugin: The parameter cannot be found.
    eDensityModelPluginParameterNotFound = (((1 << 31) | (4 << 16)) | 0x10A)

agcls.AgTypeNameMap['AgEAsDensityModelErrorCodes'] = AgEAsDensityModelErrorCodes
__all__.append('AgEAsDensityModelErrorCodes')


class IAgAsHpopPluginResult(object):
    """HPOP plugin interface used to get/set force model settings. Supports the IAgEpoch interface."""
    _uuid = '{33922BCB-FA7A-40B6-B94F-AE9C18A928FA}'
    _num_methods = 52
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_GetCd'] = _raise_uninitialized_error
        self.__dict__['_SetCd'] = _raise_uninitialized_error
        self.__dict__['_GetCr'] = _raise_uninitialized_error
        self.__dict__['_SetCr'] = _raise_uninitialized_error
        self.__dict__['_GetDragArea'] = _raise_uninitialized_error
        self.__dict__['_SetDragArea'] = _raise_uninitialized_error
        self.__dict__['_GetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_SetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_GetTimeSinceRefEpoch'] = _raise_uninitialized_error
        self.__dict__['_SetAtmFluxLags'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetLightSpeed'] = _raise_uninitialized_error
        self.__dict__['_GetSolarFlux'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags_Array'] = _raise_uninitialized_error
        self.__dict__['_IsForceModelOn'] = _raise_uninitialized_error
        self.__dict__['_ForceModelName'] = _raise_uninitialized_error
        self.__dict__['_GetRadPressureCoefficient'] = _raise_uninitialized_error
        self.__dict__['_SetRadPressureCoefficient'] = _raise_uninitialized_error
        self.__dict__['_GetRadPressureArea'] = _raise_uninitialized_error
        self.__dict__['_SetRadPressureArea'] = _raise_uninitialized_error
        self.__dict__['_GetDryMass'] = _raise_uninitialized_error
        self.__dict__['_SetDryMass'] = _raise_uninitialized_error
        self.__dict__['_GetFuelMass'] = _raise_uninitialized_error
        self.__dict__['_SetFuelMass'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_StopPropagation'] = _raise_uninitialized_error
        self.__dict__['_IndicateEvent'] = _raise_uninitialized_error
        self.__dict__['_SetMaxStep'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements_Array'] = _raise_uninitialized_error
        self.__dict__['_RefEpochString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsHpopPluginResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsHpopPluginResult from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsHpopPluginResult = agcom.GUID(IAgAsHpopPluginResult._uuid)
        vtable_offset_local = IAgAsHpopPluginResult._vtable_offset - 1
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetCd'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_SetCd'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__['_GetCr'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_SetCr'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__['_GetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__['_SetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__['_GetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_SetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+10, agcom.DOUBLE)
        self.__dict__['_GetTimeSinceRefEpoch'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__['_SetAtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+12, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+13, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+14, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+15, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+16, POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+17, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+18, agcom.LONG)
        self.__dict__['_GetLightSpeed'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+19, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+20, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+21, POINTER(agcom.BSTR))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+22, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+23, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+24, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+25, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+26, POINTER(agcom.SAFEARRAY))
        self.__dict__['_CurrentAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+27, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_CurrentAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+28, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+29, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+30, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+31, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFluxLags_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+32, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IsForceModelOn'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+33, agcom.LONG, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_ForceModelName'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+34, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__['_GetRadPressureCoefficient'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+35, POINTER(agcom.DOUBLE))
        self.__dict__['_SetRadPressureCoefficient'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+36, agcom.DOUBLE)
        self.__dict__['_GetRadPressureArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+37, POINTER(agcom.DOUBLE))
        self.__dict__['_SetRadPressureArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+38, agcom.DOUBLE)
        self.__dict__['_GetDryMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+39, POINTER(agcom.DOUBLE))
        self.__dict__['_SetDryMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+40, agcom.DOUBLE)
        self.__dict__['_GetFuelMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+41, POINTER(agcom.DOUBLE))
        self.__dict__['_SetFuelMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+42, agcom.DOUBLE)
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+43, POINTER(agcom.DOUBLE))
        self.__dict__['_StopPropagation'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+44, )
        self.__dict__['_IndicateEvent'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+45, agcom.LONG)
        self.__dict__['_SetMaxStep'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+46, agcom.DOUBLE)
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+47, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+48, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+49, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_RefEpochElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+50, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_RefEpochElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+51, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_RefEpochString'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResult, vtable_offset_local+52, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsHpopPluginResult.__dict__ and type(IAgAsHpopPluginResult.__dict__[attrname]) == property:
            return IAgAsHpopPluginResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsHpopPluginResult.')
    
    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def Cd(self) -> float:
        """Drag Coefficient. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pCd:
            agcls.evaluate_hresult(self.__dict__['_GetCd'](byref(arg_pCd.COM_val)))
            return arg_pCd.python_val

    @Cd.setter
    def Cd(self, newCd:float) -> None:
        """Drag Coefficient. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg(newCd) as arg_newCd:
            agcls.evaluate_hresult(self.__dict__['_SetCd'](arg_newCd.COM_val))

    @property
    def Cr(self) -> float:
        """SRP Coefficient. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pCr:
            agcls.evaluate_hresult(self.__dict__['_GetCr'](byref(arg_pCr.COM_val)))
            return arg_pCr.python_val

    @Cr.setter
    def Cr(self, newCr:float) -> None:
        """SRP Coefficient. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg(newCr) as arg_newCr:
            agcls.evaluate_hresult(self.__dict__['_SetCr'](arg_newCr.COM_val))

    @property
    def DragArea(self) -> float:
        """Drag Area in meters^2. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pDragArea:
            agcls.evaluate_hresult(self.__dict__['_GetDragArea'](byref(arg_pDragArea.COM_val)))
            return arg_pDragArea.python_val

    @DragArea.setter
    def DragArea(self, newDragArea:float) -> None:
        """Drag Area in meters^2. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg(newDragArea) as arg_newDragArea:
            agcls.evaluate_hresult(self.__dict__['_SetDragArea'](arg_newDragArea.COM_val))

    @property
    def SRPArea(self) -> float:
        """SRP Area in meters^2. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSRPArea:
            agcls.evaluate_hresult(self.__dict__['_GetSRPArea'](byref(arg_pSRPArea.COM_val)))
            return arg_pSRPArea.python_val

    @SRPArea.setter
    def SRPArea(self, newSRPArea:float) -> None:
        """SRP Area in meters^2. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg(newSRPArea) as arg_newSRPArea:
            agcls.evaluate_hresult(self.__dict__['_SetSRPArea'](arg_newSRPArea.COM_val))

    @property
    def TimeSinceRefEpoch(self) -> float:
        """Current epoch expressed in seconds since reference epoch."""
        with agmarshall.DOUBLE_arg() as arg_pTimeSinceRefEpoch:
            agcls.evaluate_hresult(self.__dict__['_GetTimeSinceRefEpoch'](byref(arg_pTimeSinceRefEpoch.COM_val)))
            return arg_pTimeSinceRefEpoch.python_val

    def SetAtmFluxLags(self, f10p7Lag:float, geoFluxLag:float) -> None:
        """Sets the lag times (in secs) used when evaluating the density flux values (F10.7 / Avg F10.7, ap / kp)."""
        with agmarshall.DOUBLE_arg(f10p7Lag) as arg_f10p7Lag, \
             agmarshall.DOUBLE_arg(geoFluxLag) as arg_geoFluxLag:
            agcls.evaluate_hresult(self.__dict__['_SetAtmFluxLags'](arg_f10p7Lag.COM_val, arg_geoFluxLag.COM_val))

    @property
    def Altitude(self) -> float:
        """Current altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def LightSpeed(self) -> float:
        """Speed of light in meters/second."""
        with agmarshall.DOUBLE_arg() as arg_pLightSpeed:
            agcls.evaluate_hresult(self.__dict__['_GetLightSpeed'](byref(arg_pLightSpeed.COM_val)))
            return arg_pLightSpeed.python_val

    @property
    def SolarFlux(self) -> float:
        """Current solar flux in watts/meter^2. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarFlux:
            agcls.evaluate_hresult(self.__dict__['_GetSolarFlux'](byref(arg_pSolarFlux.COM_val)))
            return arg_pSolarFlux.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude(meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentAtmFlux_Array(self) -> list:
        """Flux values used by the density model, evaluated at the current time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_CurrentAtmFlux_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFlux_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Flux values used by density models, evaluated at the requested time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp. No time lags are incorporated."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFlux_Array'](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFluxLags_Array(self) -> list:
        """The lag times (in secs), relative to the current epoch, at which the density flux values are evaluated, returned as an array of F10.7 lag, geo flux lag."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFluxLags_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IsForceModelOn(self, type:"AgEForceModelType") -> bool:
        """Indicates whether a particular force model contributor is being considered."""
        with agmarshall.AgEnum_arg(AgEForceModelType, type) as arg_type, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__['_IsForceModelOn'](arg_type.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    def ForceModelName(self, type:"AgEForceModelType") -> str:
        """A translation of the enumerated type into a string."""
        with agmarshall.AgEnum_arg(AgEForceModelType, type) as arg_type, \
             agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__['_ForceModelName'](arg_type.COM_val, byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def RadPressureCoefficient(self) -> float:
        """Radiation pressure coefficient, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg() as arg_pCoef:
            agcls.evaluate_hresult(self.__dict__['_GetRadPressureCoefficient'](byref(arg_pCoef.COM_val)))
            return arg_pCoef.python_val

    @RadPressureCoefficient.setter
    def RadPressureCoefficient(self, newCoef:float) -> None:
        """Radiation pressure coefficient, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg(newCoef) as arg_newCoef:
            agcls.evaluate_hresult(self.__dict__['_SetRadPressureCoefficient'](arg_newCoef.COM_val))

    @property
    def RadPressureArea(self) -> float:
        """Radiation pressure area in meters^2, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg() as arg_pArea:
            agcls.evaluate_hresult(self.__dict__['_GetRadPressureArea'](byref(arg_pArea.COM_val)))
            return arg_pArea.python_val

    @RadPressureArea.setter
    def RadPressureArea(self, newArea:float) -> None:
        """Radiation pressure area in meters^2, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg(newArea) as arg_newArea:
            agcls.evaluate_hresult(self.__dict__['_SetRadPressureArea'](arg_newArea.COM_val))

    @property
    def DryMass(self) -> float:
        """Dry Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pDryMass:
            agcls.evaluate_hresult(self.__dict__['_GetDryMass'](byref(arg_pDryMass.COM_val)))
            return arg_pDryMass.python_val

    @DryMass.setter
    def DryMass(self, newDryMass:float) -> None:
        """Dry Mass in kilograms."""
        with agmarshall.DOUBLE_arg(newDryMass) as arg_newDryMass:
            agcls.evaluate_hresult(self.__dict__['_SetDryMass'](arg_newDryMass.COM_val))

    @property
    def FuelMass(self) -> float:
        """Fuel Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pFuelMass:
            agcls.evaluate_hresult(self.__dict__['_GetFuelMass'](byref(arg_pFuelMass.COM_val)))
            return arg_pFuelMass.python_val

    @FuelMass.setter
    def FuelMass(self, newFuelMass:float) -> None:
        """Fuel Mass in kilograms."""
        with agmarshall.DOUBLE_arg(newFuelMass) as arg_newFuelMass:
            agcls.evaluate_hresult(self.__dict__['_SetFuelMass'](arg_newFuelMass.COM_val))

    @property
    def TotalMass(self) -> float:
        """Total Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    def StopPropagation(self) -> None:
        """Stops propagation.  For fatal errors."""
        agcls.evaluate_hresult(self.__dict__['_StopPropagation']())

    def IndicateEvent(self, eventIndicator:"AgEAsHpopPluginEventIndicators") -> None:
        """Marks an event to the propagator."""
        with agmarshall.AgEnum_arg(AgEAsHpopPluginEventIndicators, eventIndicator) as arg_eventIndicator:
            agcls.evaluate_hresult(self.__dict__['_IndicateEvent'](arg_eventIndicator.COM_val))

    def SetMaxStep(self, maxStep:float) -> None:
        """Sets the maximum step size in seconds for the propagator."""
        with agmarshall.DOUBLE_arg(maxStep) as arg_maxStep:
            agcls.evaluate_hresult(self.__dict__['_SetMaxStep'](arg_maxStep.COM_val))

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def RefEpochElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Reference epoch expressed in requested time scale in day count and date formats as the array: WholeDays, SecsIntoDay, Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_RefEpochElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def RefEpochString(self, dateAbbrv:str) -> str:
        """Reference epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pRefEpochString:
            agcls.evaluate_hresult(self.__dict__['_RefEpochString'](arg_dateAbbrv.COM_val, byref(arg_pRefEpochString.COM_val)))
            return arg_pRefEpochString.python_val


agcls.AgClassCatalog.add_catalog_entry('{33922BCB-FA7A-40B6-B94F-AE9C18A928FA}', IAgAsHpopPluginResult)
agcls.AgTypeNameMap['IAgAsHpopPluginResult'] = IAgAsHpopPluginResult
__all__.append('IAgAsHpopPluginResult')

class IAgAsHpopPluginResultEval(object):
    """HPOP plugin interface used to get/set force model settings during the computation of a step. Supports the IAgEpoch interface."""
    _uuid = '{4518FC76-4B7D-4926-9CB5-E36AF7D94733}'
    _num_methods = 56
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_GetCd'] = _raise_uninitialized_error
        self.__dict__['_SetCd'] = _raise_uninitialized_error
        self.__dict__['_GetCr'] = _raise_uninitialized_error
        self.__dict__['_SetCr'] = _raise_uninitialized_error
        self.__dict__['_GetDragArea'] = _raise_uninitialized_error
        self.__dict__['_SetDragArea'] = _raise_uninitialized_error
        self.__dict__['_GetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_SetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_GetTimeSinceRefEpoch'] = _raise_uninitialized_error
        self.__dict__['_SetAtmFluxLags'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_GetDragAltitude'] = _raise_uninitialized_error
        self.__dict__['_GetAtmTemperature'] = _raise_uninitialized_error
        self.__dict__['_GetAtmPressure'] = _raise_uninitialized_error
        self.__dict__['_GetDensity'] = _raise_uninitialized_error
        self.__dict__['_SetDensity'] = _raise_uninitialized_error
        self.__dict__['_GetSolarIntensity'] = _raise_uninitialized_error
        self.__dict__['_SetSolarIntensity'] = _raise_uninitialized_error
        self.__dict__['_AddAcceleration'] = _raise_uninitialized_error
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetLightSpeed'] = _raise_uninitialized_error
        self.__dict__['_GetSolarFlux'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags_Array'] = _raise_uninitialized_error
        self.__dict__['_IsForceModelOn'] = _raise_uninitialized_error
        self.__dict__['_ForceModelName'] = _raise_uninitialized_error
        self.__dict__['_GetRadPressureCoefficient'] = _raise_uninitialized_error
        self.__dict__['_SetRadPressureCoefficient'] = _raise_uninitialized_error
        self.__dict__['_GetRadPressureArea'] = _raise_uninitialized_error
        self.__dict__['_SetRadPressureArea'] = _raise_uninitialized_error
        self.__dict__['_GetDryMass'] = _raise_uninitialized_error
        self.__dict__['_GetFuelMass'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_StopPropagation'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements_Array'] = _raise_uninitialized_error
        self.__dict__['_RefEpochString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsHpopPluginResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsHpopPluginResultEval from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsHpopPluginResultEval = agcom.GUID(IAgAsHpopPluginResultEval._uuid)
        vtable_offset_local = IAgAsHpopPluginResultEval._vtable_offset - 1
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+2, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetCd'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_SetCd'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__['_GetCr'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_SetCr'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__['_GetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__['_SetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__['_GetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_SetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+10, agcom.DOUBLE)
        self.__dict__['_GetTimeSinceRefEpoch'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__['_SetAtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+12, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+13, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+14, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+15, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+16, POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+17, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetDragAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+18, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAtmTemperature'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+19, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAtmPressure'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+20, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+21, POINTER(agcom.DOUBLE))
        self.__dict__['_SetDensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+22, agcom.DOUBLE)
        self.__dict__['_GetSolarIntensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+23, POINTER(agcom.DOUBLE))
        self.__dict__['_SetSolarIntensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+24, agcom.DOUBLE)
        self.__dict__['_AddAcceleration'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+25, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+26, agcom.LONG)
        self.__dict__['_GetLightSpeed'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+27, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+28, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+29, POINTER(agcom.BSTR))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+30, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+31, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+32, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+33, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+34, POINTER(agcom.SAFEARRAY))
        self.__dict__['_CurrentAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+35, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_CurrentAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+36, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+37, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+38, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+39, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFluxLags_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+40, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IsForceModelOn'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+41, agcom.LONG, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_ForceModelName'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+42, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__['_GetRadPressureCoefficient'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+43, POINTER(agcom.DOUBLE))
        self.__dict__['_SetRadPressureCoefficient'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+44, agcom.DOUBLE)
        self.__dict__['_GetRadPressureArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+45, POINTER(agcom.DOUBLE))
        self.__dict__['_SetRadPressureArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+46, agcom.DOUBLE)
        self.__dict__['_GetDryMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+47, POINTER(agcom.DOUBLE))
        self.__dict__['_GetFuelMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+48, POINTER(agcom.DOUBLE))
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+49, POINTER(agcom.DOUBLE))
        self.__dict__['_StopPropagation'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+50, )
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+51, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+52, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+53, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_RefEpochElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+54, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_RefEpochElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+55, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_RefEpochString'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultEval, vtable_offset_local+56, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsHpopPluginResultEval.__dict__ and type(IAgAsHpopPluginResultEval.__dict__[attrname]) == property:
            return IAgAsHpopPluginResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsHpopPluginResultEval.')
    
    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def Cd(self) -> float:
        """Drag Coefficient. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pCd:
            agcls.evaluate_hresult(self.__dict__['_GetCd'](byref(arg_pCd.COM_val)))
            return arg_pCd.python_val

    @Cd.setter
    def Cd(self, newCd:float) -> None:
        """Drag Coefficient. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg(newCd) as arg_newCd:
            agcls.evaluate_hresult(self.__dict__['_SetCd'](arg_newCd.COM_val))

    @property
    def Cr(self) -> float:
        """SRP Coefficient. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pCr:
            agcls.evaluate_hresult(self.__dict__['_GetCr'](byref(arg_pCr.COM_val)))
            return arg_pCr.python_val

    @Cr.setter
    def Cr(self, newCr:float) -> None:
        """SRP Coefficient. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg(newCr) as arg_newCr:
            agcls.evaluate_hresult(self.__dict__['_SetCr'](arg_newCr.COM_val))

    @property
    def DragArea(self) -> float:
        """Drag Area in meters^2. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pDragArea:
            agcls.evaluate_hresult(self.__dict__['_GetDragArea'](byref(arg_pDragArea.COM_val)))
            return arg_pDragArea.python_val

    @DragArea.setter
    def DragArea(self, newDragArea:float) -> None:
        """Drag Area in meters^2. Can only be set if Drag is on."""
        with agmarshall.DOUBLE_arg(newDragArea) as arg_newDragArea:
            agcls.evaluate_hresult(self.__dict__['_SetDragArea'](arg_newDragArea.COM_val))

    @property
    def SRPArea(self) -> float:
        """SRP Area in meters^2. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSRPArea:
            agcls.evaluate_hresult(self.__dict__['_GetSRPArea'](byref(arg_pSRPArea.COM_val)))
            return arg_pSRPArea.python_val

    @SRPArea.setter
    def SRPArea(self, newSRPArea:float) -> None:
        """SRP Area in meters^2. Can only be set if SRP is on."""
        with agmarshall.DOUBLE_arg(newSRPArea) as arg_newSRPArea:
            agcls.evaluate_hresult(self.__dict__['_SetSRPArea'](arg_newSRPArea.COM_val))

    @property
    def TimeSinceRefEpoch(self) -> float:
        """Current epoch expressed in seconds since reference epoch."""
        with agmarshall.DOUBLE_arg() as arg_pTimeSinceRefEpoch:
            agcls.evaluate_hresult(self.__dict__['_GetTimeSinceRefEpoch'](byref(arg_pTimeSinceRefEpoch.COM_val)))
            return arg_pTimeSinceRefEpoch.python_val

    def SetAtmFluxLags(self, f10p7Lag:float, geoFluxLag:float) -> None:
        """Sets the lag times (in secs) used when evaluating the density flux values (F10.7 / Avg F10.7, ap / kp)."""
        with agmarshall.DOUBLE_arg(f10p7Lag) as arg_f10p7Lag, \
             agmarshall.DOUBLE_arg(geoFluxLag) as arg_geoFluxLag:
            agcls.evaluate_hresult(self.__dict__['_SetAtmFluxLags'](arg_f10p7Lag.COM_val, arg_geoFluxLag.COM_val))

    @property
    def Altitude(self) -> float:
        """Current altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    @property
    def DragAltitude(self) -> float:
        """Current altitude in meters used by density model. Available only if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pDragAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetDragAltitude'](byref(arg_pDragAltitude.COM_val)))
            return arg_pDragAltitude.python_val

    @property
    def AtmTemperature(self) -> float:
        """Current atmospheric temperature in Kelvin. Available only if Drag is on and the density model can provide this data."""
        with agmarshall.DOUBLE_arg() as arg_pAtmTemperature:
            agcls.evaluate_hresult(self.__dict__['_GetAtmTemperature'](byref(arg_pAtmTemperature.COM_val)))
            return arg_pAtmTemperature.python_val

    @property
    def AtmPressure(self) -> float:
        """Current atmospheric pressure in Pascals. Available only if Drag is on and the density model can provide this data."""
        with agmarshall.DOUBLE_arg() as arg_pAtmPressure:
            agcls.evaluate_hresult(self.__dict__['_GetAtmPressure'](byref(arg_pAtmPressure.COM_val)))
            return arg_pAtmPressure.python_val

    @property
    def Density(self) -> float:
        """Current density in kilograms/meter^3. Available only if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pDensity:
            agcls.evaluate_hresult(self.__dict__['_GetDensity'](byref(arg_pDensity.COM_val)))
            return arg_pDensity.python_val

    @Density.setter
    def Density(self, newDensity:float) -> None:
        """Current density in kilograms/meter^3. Available only if Drag is on."""
        with agmarshall.DOUBLE_arg(newDensity) as arg_newDensity:
            agcls.evaluate_hresult(self.__dict__['_SetDensity'](arg_newDensity.COM_val))

    @property
    def SolarIntensity(self) -> float:
        """Current solar intensity. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarIntensity:
            agcls.evaluate_hresult(self.__dict__['_GetSolarIntensity'](byref(arg_pSolarIntensity.COM_val)))
            return arg_pSolarIntensity.python_val

    @SolarIntensity.setter
    def SolarIntensity(self, newSolarIntensity:float) -> None:
        """Current solar intensity. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg(newSolarIntensity) as arg_newSolarIntensity:
            agcls.evaluate_hresult(self.__dict__['_SetSolarIntensity'](arg_newSolarIntensity.COM_val))

    def AddAcceleration(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> None:
        """Add the acceleration in meters/second^2 in the given frame to the force model."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__['_AddAcceleration'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def LightSpeed(self) -> float:
        """Speed of light in meters/second."""
        with agmarshall.DOUBLE_arg() as arg_pLightSpeed:
            agcls.evaluate_hresult(self.__dict__['_GetLightSpeed'](byref(arg_pLightSpeed.COM_val)))
            return arg_pLightSpeed.python_val

    @property
    def SolarFlux(self) -> float:
        """Current solar flux in watts/meter^2. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarFlux:
            agcls.evaluate_hresult(self.__dict__['_GetSolarFlux'](byref(arg_pSolarFlux.COM_val)))
            return arg_pSolarFlux.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude (meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentAtmFlux_Array(self) -> list:
        """Flux values used by the density model, evaluated at the current time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_CurrentAtmFlux_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFlux_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Flux values used by density models, evaluated at the requested time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp. No time lags are incorporated."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFlux_Array'](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFluxLags_Array(self) -> list:
        """The lag times (in secs), relative to the current epoch, at which the density flux values are evaluated, returned as an array of F10.7 lag, geo flux lag."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFluxLags_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IsForceModelOn(self, type:"AgEForceModelType") -> bool:
        """Indicates whether a particular force model contributor is being considered."""
        with agmarshall.AgEnum_arg(AgEForceModelType, type) as arg_type, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__['_IsForceModelOn'](arg_type.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    def ForceModelName(self, type:"AgEForceModelType") -> str:
        """A translation of the enumerated type into a string."""
        with agmarshall.AgEnum_arg(AgEForceModelType, type) as arg_type, \
             agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__['_ForceModelName'](arg_type.COM_val, byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def RadPressureCoefficient(self) -> float:
        """Radiation pressure coefficient, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg() as arg_pCoef:
            agcls.evaluate_hresult(self.__dict__['_GetRadPressureCoefficient'](byref(arg_pCoef.COM_val)))
            return arg_pCoef.python_val

    @RadPressureCoefficient.setter
    def RadPressureCoefficient(self, newCoef:float) -> None:
        """Radiation pressure coefficient, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg(newCoef) as arg_newCoef:
            agcls.evaluate_hresult(self.__dict__['_SetRadPressureCoefficient'](arg_newCoef.COM_val))

    @property
    def RadPressureArea(self) -> float:
        """Radiation pressure area in meters^2, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg() as arg_pArea:
            agcls.evaluate_hresult(self.__dict__['_GetRadPressureArea'](byref(arg_pArea.COM_val)))
            return arg_pArea.python_val

    @RadPressureArea.setter
    def RadPressureArea(self, newArea:float) -> None:
        """Radiation pressure area in meters^2, used by albedo and thermal radiation pressure. Can only be set if albedo or thermal radiation pressure is on."""
        with agmarshall.DOUBLE_arg(newArea) as arg_newArea:
            agcls.evaluate_hresult(self.__dict__['_SetRadPressureArea'](arg_newArea.COM_val))

    @property
    def DryMass(self) -> float:
        """Dry Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pDryMass:
            agcls.evaluate_hresult(self.__dict__['_GetDryMass'](byref(arg_pDryMass.COM_val)))
            return arg_pDryMass.python_val

    @property
    def FuelMass(self) -> float:
        """Fuel Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pFuelMass:
            agcls.evaluate_hresult(self.__dict__['_GetFuelMass'](byref(arg_pFuelMass.COM_val)))
            return arg_pFuelMass.python_val

    @property
    def TotalMass(self) -> float:
        """Total Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    def StopPropagation(self) -> None:
        """Stops propagation.  For fatal errors."""
        agcls.evaluate_hresult(self.__dict__['_StopPropagation']())

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def RefEpochElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Reference epoch expressed in requested time scale in day count and date formats as the array: WholeDays, SecsIntoDay, Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_RefEpochElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def RefEpochString(self, dateAbbrv:str) -> str:
        """Reference epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pRefEpochString:
            agcls.evaluate_hresult(self.__dict__['_RefEpochString'](arg_dateAbbrv.COM_val, byref(arg_pRefEpochString.COM_val)))
            return arg_pRefEpochString.python_val


agcls.AgClassCatalog.add_catalog_entry('{4518FC76-4B7D-4926-9CB5-E36AF7D94733}', IAgAsHpopPluginResultEval)
agcls.AgTypeNameMap['IAgAsHpopPluginResultEval'] = IAgAsHpopPluginResultEval
__all__.append('IAgAsHpopPluginResultEval')

class IAgAsHpopPluginResultPostEval(object):
    """HPOP plugin interface used to get/set force model settings. Supports the IAgEpoch interface."""
    _uuid = '{11317870-1AE0-416a-9E15-E00B71DFD5D9}'
    _num_methods = 50
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_GetCd'] = _raise_uninitialized_error
        self.__dict__['_GetCr'] = _raise_uninitialized_error
        self.__dict__['_GetDragArea'] = _raise_uninitialized_error
        self.__dict__['_GetSRPArea'] = _raise_uninitialized_error
        self.__dict__['_GetTimeSinceRefEpoch'] = _raise_uninitialized_error
        self.__dict__['_AccelName'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetLightSpeed'] = _raise_uninitialized_error
        self.__dict__['_GetSolarFlux'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags_Array'] = _raise_uninitialized_error
        self.__dict__['_GetDragAltitude'] = _raise_uninitialized_error
        self.__dict__['_GetAtmTemperature'] = _raise_uninitialized_error
        self.__dict__['_GetAtmPressure'] = _raise_uninitialized_error
        self.__dict__['_GetDensity'] = _raise_uninitialized_error
        self.__dict__['_GetSolarIntensity'] = _raise_uninitialized_error
        self.__dict__['_AddAcceleration'] = _raise_uninitialized_error
        self.__dict__['_GetAcceleration'] = _raise_uninitialized_error
        self.__dict__['_GetAcceleration_Array'] = _raise_uninitialized_error
        self.__dict__['_IsForceModelOn'] = _raise_uninitialized_error
        self.__dict__['_ForceModelName'] = _raise_uninitialized_error
        self.__dict__['_GetRadPressureCoefficient'] = _raise_uninitialized_error
        self.__dict__['_GetRadPressureArea'] = _raise_uninitialized_error
        self.__dict__['_GetDryMass'] = _raise_uninitialized_error
        self.__dict__['_GetFuelMass'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_StopPropagation'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements_Array'] = _raise_uninitialized_error
        self.__dict__['_RefEpochString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsHpopPluginResultPostEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsHpopPluginResultPostEval from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsHpopPluginResultPostEval = agcom.GUID(IAgAsHpopPluginResultPostEval._uuid)
        vtable_offset_local = IAgAsHpopPluginResultPostEval._vtable_offset - 1
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+2, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetCd'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCr'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDragArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSRPArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_GetTimeSinceRefEpoch'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__['_AccelName'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+8, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+9, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+10, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+11, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+12, POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+13, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+14, agcom.LONG)
        self.__dict__['_GetLightSpeed'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+15, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+16, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+17, POINTER(agcom.BSTR))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+18, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+19, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+20, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+21, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+22, POINTER(agcom.SAFEARRAY))
        self.__dict__['_CurrentAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+23, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_CurrentAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+24, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+25, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+26, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+27, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFluxLags_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+28, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetDragAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+29, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAtmTemperature'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+30, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAtmPressure'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+31, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+32, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarIntensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+33, POINTER(agcom.DOUBLE))
        self.__dict__['_AddAcceleration'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+34, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_GetAcceleration'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+35, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_GetAcceleration_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+36, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IsForceModelOn'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+37, agcom.LONG, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_ForceModelName'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+38, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__['_GetRadPressureCoefficient'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+39, POINTER(agcom.DOUBLE))
        self.__dict__['_GetRadPressureArea'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+40, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDryMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+41, POINTER(agcom.DOUBLE))
        self.__dict__['_GetFuelMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+42, POINTER(agcom.DOUBLE))
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+43, POINTER(agcom.DOUBLE))
        self.__dict__['_StopPropagation'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+44, )
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+45, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+46, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+47, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_RefEpochElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+48, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_RefEpochElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+49, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_RefEpochString'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginResultPostEval, vtable_offset_local+50, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsHpopPluginResultPostEval.__dict__ and type(IAgAsHpopPluginResultPostEval.__dict__[attrname]) == property:
            return IAgAsHpopPluginResultPostEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsHpopPluginResultPostEval.')
    
    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def Cd(self) -> float:
        """Drag Coefficient."""
        with agmarshall.DOUBLE_arg() as arg_pCd:
            agcls.evaluate_hresult(self.__dict__['_GetCd'](byref(arg_pCd.COM_val)))
            return arg_pCd.python_val

    @property
    def Cr(self) -> float:
        """SRP Coefficient."""
        with agmarshall.DOUBLE_arg() as arg_pCr:
            agcls.evaluate_hresult(self.__dict__['_GetCr'](byref(arg_pCr.COM_val)))
            return arg_pCr.python_val

    @property
    def DragArea(self) -> float:
        """Drag Area in meters^2."""
        with agmarshall.DOUBLE_arg() as arg_pDragArea:
            agcls.evaluate_hresult(self.__dict__['_GetDragArea'](byref(arg_pDragArea.COM_val)))
            return arg_pDragArea.python_val

    @property
    def SRPArea(self) -> float:
        """SRP Area in meters^2."""
        with agmarshall.DOUBLE_arg() as arg_pSRPArea:
            agcls.evaluate_hresult(self.__dict__['_GetSRPArea'](byref(arg_pSRPArea.COM_val)))
            return arg_pSRPArea.python_val

    @property
    def TimeSinceRefEpoch(self) -> float:
        """Current epoch expressed in seconds since reference epoch."""
        with agmarshall.DOUBLE_arg() as arg_pTimeSinceRefEpoch:
            agcls.evaluate_hresult(self.__dict__['_GetTimeSinceRefEpoch'](byref(arg_pTimeSinceRefEpoch.COM_val)))
            return arg_pTimeSinceRefEpoch.python_val

    def AccelName(self, type:"AgEAccelType") -> str:
        """A translation of the enumerated type into a string."""
        with agmarshall.AgEnum_arg(AgEAccelType, type) as arg_type, \
             agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__['_AccelName'](arg_type.COM_val, byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def Altitude(self) -> float:
        """Current altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def LightSpeed(self) -> float:
        """Speed of light in meters/second."""
        with agmarshall.DOUBLE_arg() as arg_pLightSpeed:
            agcls.evaluate_hresult(self.__dict__['_GetLightSpeed'](byref(arg_pLightSpeed.COM_val)))
            return arg_pLightSpeed.python_val

    @property
    def SolarFlux(self) -> float:
        """Current solar flux in watts/meter^2. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarFlux:
            agcls.evaluate_hresult(self.__dict__['_GetSolarFlux'](byref(arg_pSolarFlux.COM_val)))
            return arg_pSolarFlux.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude (meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentAtmFlux_Array(self) -> list:
        """Flux values used by the density model, evaluated at the current time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_CurrentAtmFlux_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFlux_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Flux values used by density models, evaluated at the requested time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp. No time lags are incorporated."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFlux_Array'](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFluxLags_Array(self) -> list:
        """The lag times (in secs), relative to the current epoch, at which the density flux values are evaluated, returned as an array of F10.7 lag, geo flux lag."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFluxLags_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def DragAltitude(self) -> float:
        """Current altitude in meters used by density model. Available only if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pDragAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetDragAltitude'](byref(arg_pDragAltitude.COM_val)))
            return arg_pDragAltitude.python_val

    @property
    def AtmTemperature(self) -> float:
        """Current atmospheric temperature in Kelvin. Available only if Drag is on and the density model can provide this data."""
        with agmarshall.DOUBLE_arg() as arg_pAtmTemperature:
            agcls.evaluate_hresult(self.__dict__['_GetAtmTemperature'](byref(arg_pAtmTemperature.COM_val)))
            return arg_pAtmTemperature.python_val

    @property
    def AtmPressure(self) -> float:
        """Current atmospheric pressure in Pascals. Available only if Drag is on and the density model can provide this data."""
        with agmarshall.DOUBLE_arg() as arg_pAtmPressure:
            agcls.evaluate_hresult(self.__dict__['_GetAtmPressure'](byref(arg_pAtmPressure.COM_val)))
            return arg_pAtmPressure.python_val

    @property
    def Density(self) -> float:
        """Current density in kilograms/meter^3. Available only if Drag is on."""
        with agmarshall.DOUBLE_arg() as arg_pDensity:
            agcls.evaluate_hresult(self.__dict__['_GetDensity'](byref(arg_pDensity.COM_val)))
            return arg_pDensity.python_val

    @property
    def SolarIntensity(self) -> float:
        """Current solar intensity. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarIntensity:
            agcls.evaluate_hresult(self.__dict__['_GetSolarIntensity'](byref(arg_pSolarIntensity.COM_val)))
            return arg_pSolarIntensity.python_val

    def AddAcceleration(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> None:
        """Add the acceleration in meters/second^2 in the given frame to the force model."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__['_AddAcceleration'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def GetAcceleration_Array(self, type:"AgEAccelType", frame:"AgEUtFrame") -> list:
        """The acceleration in meters/second^2 contribution of the indicated Type, returned as cartesian components in the specified frame as the array X, Y, Z."""
        with agmarshall.AgEnum_arg(AgEAccelType, type) as arg_type, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_GetAcceleration_Array'](arg_type.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IsForceModelOn(self, type:"AgEForceModelType") -> bool:
        """Indicates whether a particular force model contributor is being considered."""
        with agmarshall.AgEnum_arg(AgEForceModelType, type) as arg_type, \
             agmarshall.VARIANT_BOOL_arg() as arg_pResult:
            agcls.evaluate_hresult(self.__dict__['_IsForceModelOn'](arg_type.COM_val, byref(arg_pResult.COM_val)))
            return arg_pResult.python_val

    def ForceModelName(self, type:"AgEForceModelType") -> str:
        """A translation of the enumerated type into a string."""
        with agmarshall.AgEnum_arg(AgEForceModelType, type) as arg_type, \
             agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__['_ForceModelName'](arg_type.COM_val, byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def RadPressureCoefficient(self) -> float:
        """Radiation pressure coefficient, used by albedo and thermal radiation pressure."""
        with agmarshall.DOUBLE_arg() as arg_pCoef:
            agcls.evaluate_hresult(self.__dict__['_GetRadPressureCoefficient'](byref(arg_pCoef.COM_val)))
            return arg_pCoef.python_val

    @property
    def RadPressureArea(self) -> float:
        """Radiation pressure area in meters^2, used by albedo and thermal radiation pressure."""
        with agmarshall.DOUBLE_arg() as arg_pArea:
            agcls.evaluate_hresult(self.__dict__['_GetRadPressureArea'](byref(arg_pArea.COM_val)))
            return arg_pArea.python_val

    @property
    def DryMass(self) -> float:
        """Dry Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pDryMass:
            agcls.evaluate_hresult(self.__dict__['_GetDryMass'](byref(arg_pDryMass.COM_val)))
            return arg_pDryMass.python_val

    @property
    def FuelMass(self) -> float:
        """Fuel Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pFuelMass:
            agcls.evaluate_hresult(self.__dict__['_GetFuelMass'](byref(arg_pFuelMass.COM_val)))
            return arg_pFuelMass.python_val

    @property
    def TotalMass(self) -> float:
        """Total Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    def StopPropagation(self) -> None:
        """Stops propagation.  For fatal errors."""
        agcls.evaluate_hresult(self.__dict__['_StopPropagation']())

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def RefEpochElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Reference epoch expressed in requested time scale in day count and date formats as the array: WholeDays, SecsIntoDay, Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_RefEpochElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def RefEpochString(self, dateAbbrv:str) -> str:
        """Reference epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pRefEpochString:
            agcls.evaluate_hresult(self.__dict__['_RefEpochString'](arg_dateAbbrv.COM_val, byref(arg_pRefEpochString.COM_val)))
            return arg_pRefEpochString.python_val


agcls.AgClassCatalog.add_catalog_entry('{11317870-1AE0-416a-9E15-E00B71DFD5D9}', IAgAsHpopPluginResultPostEval)
agcls.AgTypeNameMap['IAgAsHpopPluginResultPostEval'] = IAgAsHpopPluginResultPostEval
__all__.append('IAgAsHpopPluginResultPostEval')

class IAgAsHpopPluginSampleEngine(object):
    """HPOP sample plugin"""
    _uuid = '{04F3121D-439F-4618-A6DC-4B0EC3D94C68}'
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetAccel'] = _raise_uninitialized_error
        self.__dict__['_SetAccel'] = _raise_uninitialized_error
        self.__dict__['_GetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_SetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_GetDebugMode'] = _raise_uninitialized_error
        self.__dict__['_SetDebugMode'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsHpopPluginSampleEngine._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsHpopPluginSampleEngine from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsHpopPluginSampleEngine = agcom.GUID(IAgAsHpopPluginSampleEngine._uuid)
        vtable_offset_local = IAgAsHpopPluginSampleEngine._vtable_offset - 1
        self.__dict__['_GetAccel'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginSampleEngine, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__['_SetAccel'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginSampleEngine, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__['_GetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginSampleEngine, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__['_SetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginSampleEngine, vtable_offset_local+4, agcom.LONG)
        self.__dict__['_GetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginSampleEngine, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_SetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsHpopPluginSampleEngine, vtable_offset_local+6, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsHpopPluginSampleEngine.__dict__ and type(IAgAsHpopPluginSampleEngine.__dict__[attrname]) == property:
            return IAgAsHpopPluginSampleEngine.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsHpopPluginSampleEngine.')
    
    @property
    def Accel(self) -> float:
        """Thrust acceleration value, in m/sec^2."""
        with agmarshall.DOUBLE_arg() as arg_pAccel:
            agcls.evaluate_hresult(self.__dict__['_GetAccel'](byref(arg_pAccel.COM_val)))
            return arg_pAccel.python_val

    @Accel.setter
    def Accel(self, newAccel:float) -> None:
        """Thrust acceleration value, in m/sec^2."""
        with agmarshall.DOUBLE_arg(newAccel) as arg_newAccel:
            agcls.evaluate_hresult(self.__dict__['_SetAccel'](arg_newAccel.COM_val))

    @property
    def ReportFrequency(self) -> int:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg() as arg_pFreq:
            agcls.evaluate_hresult(self.__dict__['_GetReportFrequency'](byref(arg_pFreq.COM_val)))
            return arg_pFreq.python_val

    @ReportFrequency.setter
    def ReportFrequency(self, newFreq:int) -> None:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg(newFreq) as arg_newFreq:
            agcls.evaluate_hresult(self.__dict__['_SetReportFrequency'](arg_newFreq.COM_val))

    @property
    def DebugMode(self) -> bool:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pDebugMode:
            agcls.evaluate_hresult(self.__dict__['_GetDebugMode'](byref(arg_pDebugMode.COM_val)))
            return arg_pDebugMode.python_val

    @DebugMode.setter
    def DebugMode(self, newDebugMode:bool) -> None:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg(newDebugMode) as arg_newDebugMode:
            agcls.evaluate_hresult(self.__dict__['_SetDebugMode'](arg_newDebugMode.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{04F3121D-439F-4618-A6DC-4B0EC3D94C68}', IAgAsHpopPluginSampleEngine)
agcls.AgTypeNameMap['IAgAsHpopPluginSampleEngine'] = IAgAsHpopPluginSampleEngine
__all__.append('IAgAsHpopPluginSampleEngine')

class IAgAsLightReflectionResultRegister(object):
    """LightReflection plugin interface used to register parameters that may be estimated."""
    _uuid = '{EF4CBEC2-8BC9-4e4f-811E-1CC9B2209D37}'
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_RegisterParameter'] = _raise_uninitialized_error
        self.__dict__['_Message'] = _raise_uninitialized_error
        self.__dict__['_GetInstallDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetConfigDirectory'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserInput'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserParameterOutput'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsLightReflectionResultRegister._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsLightReflectionResultRegister from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsLightReflectionResultRegister = agcom.GUID(IAgAsLightReflectionResultRegister._uuid)
        vtable_offset_local = IAgAsLightReflectionResultRegister._vtable_offset - 1
        self.__dict__['_RegisterParameter'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultRegister, vtable_offset_local+1, agcom.BSTR, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.BSTR, POINTER(agcom.LONG))
        self.__dict__['_Message'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultRegister, vtable_offset_local+2, agcom.LONG, agcom.BSTR)
        self.__dict__['_GetInstallDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultRegister, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_GetConfigDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultRegister, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__['_RegisterUserInput'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultRegister, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.LONG))
        self.__dict__['_RegisterUserParameterOutput'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultRegister, vtable_offset_local+6, agcom.BSTR, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsLightReflectionResultRegister.__dict__ and type(IAgAsLightReflectionResultRegister.__dict__[attrname]) == property:
            return IAgAsLightReflectionResultRegister.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsLightReflectionResultRegister.')
    
    def RegisterParameter(self, name:str, defaultValue:float, minValue:float, maxValue:float, dimension:str) -> int:
        """Registers a parameter of the computation that may be estimated. Returns an index identifier of the parameter used by other interfaces."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.DOUBLE_arg(defaultValue) as arg_defaultValue, \
             agmarshall.DOUBLE_arg(minValue) as arg_minValue, \
             agmarshall.DOUBLE_arg(maxValue) as arg_maxValue, \
             agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterParameter'](arg_name.COM_val, arg_defaultValue.COM_val, arg_minValue.COM_val, arg_maxValue.COM_val, arg_dimension.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val

    def Message(self, msgType:"AgEUtLogMsgType", message:str) -> None:
        """Send a message to the message viewer."""
        with agmarshall.AgEnum_arg(AgEUtLogMsgType, msgType) as arg_msgType, \
             agmarshall.BSTR_arg(message) as arg_message:
            agcls.evaluate_hresult(self.__dict__['_Message'](arg_msgType.COM_val, arg_message.COM_val))

    @property
    def InstallDirectory(self) -> str:
        """The directory path of the installation of the application."""
        with agmarshall.BSTR_arg() as arg_dirPath:
            agcls.evaluate_hresult(self.__dict__['_GetInstallDirectory'](byref(arg_dirPath.COM_val)))
            return arg_dirPath.python_val

    @property
    def ConfigDirectory(self) -> str:
        """The directory path of the user configuration area."""
        with agmarshall.BSTR_arg() as arg_dirPath:
            agcls.evaluate_hresult(self.__dict__['_GetConfigDirectory'](byref(arg_dirPath.COM_val)))
            return arg_dirPath.python_val

    def RegisterUserInput(self, userValue:str) -> int:
        """Registers as input to the plugin a user value in the state vector."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserInput'](arg_userValue.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val

    def RegisterUserParameterOutput(self, userValue:str) -> int:
        """Registers a user value in the state vector as a parameter output of the plugin."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserParameterOutput'](arg_userValue.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val


agcls.AgClassCatalog.add_catalog_entry('{EF4CBEC2-8BC9-4e4f-811E-1CC9B2209D37}', IAgAsLightReflectionResultRegister)
agcls.AgTypeNameMap['IAgAsLightReflectionResultRegister'] = IAgAsLightReflectionResultRegister
__all__.append('IAgAsLightReflectionResultRegister')

class IAgAsLightReflectionResult(object):
    """LightReflection plugin interface used to get/set settings. Supports the IAgEpoch interface."""
    _uuid = '{4825C756-3384-4028-AC6B-9C492CF54298}'
    _num_methods = 31
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_GetLightSpeed'] = _raise_uninitialized_error
        self.__dict__['_GetSolarIntensity'] = _raise_uninitialized_error
        self.__dict__['_GetSolarFlux'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_GetInputValue'] = _raise_uninitialized_error
        self.__dict__['_SetParameterOutputValue'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsLightReflectionResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsLightReflectionResult from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsLightReflectionResult = agcom.GUID(IAgAsLightReflectionResult._uuid)
        vtable_offset_local = IAgAsLightReflectionResult._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_GetLightSpeed'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarIntensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+7, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+8, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+11, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+12, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+13, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+14, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+15, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+16, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+17, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+18, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirection'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+19, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirection_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+20, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVectorToBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+21, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorToBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+22, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVectorFromBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+23, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorFromBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+24, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+25, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+26, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+27, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+28, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+29, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_GetInputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+30, agcom.INT, POINTER(agcom.DOUBLE))
        self.__dict__['_SetParameterOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResult, vtable_offset_local+31, agcom.INT, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsLightReflectionResult.__dict__ and type(IAgAsLightReflectionResult.__dict__[attrname]) == property:
            return IAgAsLightReflectionResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsLightReflectionResult.')
    
    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    @property
    def LightSpeed(self) -> float:
        """Speed of light in meters/second."""
        with agmarshall.DOUBLE_arg() as arg_pLightSpeed:
            agcls.evaluate_hresult(self.__dict__['_GetLightSpeed'](byref(arg_pLightSpeed.COM_val)))
            return arg_pLightSpeed.python_val

    @property
    def SolarIntensity(self) -> float:
        """Current solar intensity. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarIntensity:
            agcls.evaluate_hresult(self.__dict__['_GetSolarIntensity'](byref(arg_pSolarIntensity.COM_val)))
            return arg_pSolarIntensity.python_val

    @property
    def SolarFlux(self) -> float:
        """Current solar flux in watts/meter^2. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarFlux:
            agcls.evaluate_hresult(self.__dict__['_GetSolarFlux'](byref(arg_pSolarFlux.COM_val)))
            return arg_pSolarFlux.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def TotalMass(self) -> float:
        """Total Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    @property
    def Altitude(self) -> float:
        """Current altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude(meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirection_Array(self, frame:"AgEUtFrame") -> list:
        """Incident light direction (unitless) on the body, in the requested frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirection_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVectorToBody_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float) -> list:
        """Transforms a vector from the input frame to the body frame returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorToBody_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVectorFromBody_Array(self, xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the body frame to the output frame returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorFromBody_Array'](arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionInBody_Array(self) -> list:
        """Incident light direction (unitless) on the body, in the body frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionInBody_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def GetInputValue(self, index:int) -> float:
        """Gets the value of an input to the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetInputValue'](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetParameterOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a parameter output of the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetParameterOutputValue'](arg_index.COM_val, arg_val.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{4825C756-3384-4028-AC6B-9C492CF54298}', IAgAsLightReflectionResult)
agcls.AgTypeNameMap['IAgAsLightReflectionResult'] = IAgAsLightReflectionResult
__all__.append('IAgAsLightReflectionResult')

class IAgAsLightReflectionResultEval(object):
    """LightReflection plugin interface used to get/set settings during evaluation. Used to set reflectance vector (and optionally its partial derivs) used in computation of the srp force. Supports the IAgEpoch interface."""
    _uuid = '{18153B47-D0B5-46c1-8F58-FCC8EBDEBD19}'
    _num_methods = 61
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_GetLightSpeed'] = _raise_uninitialized_error
        self.__dict__['_GetSolarIntensity'] = _raise_uninitialized_error
        self.__dict__['_GetSolarFlux'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection_Array'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceInBody'] = _raise_uninitialized_error
        self.__dict__['_SetReflectance'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecInBodyPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecInBodyPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceBodyCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceBodyCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorPosPartials'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorPosPartials'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorVelPartials'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorVelPartials'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_ParameterValue'] = _raise_uninitialized_error
        self.__dict__['_GetParameterValue_Array'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceInBodyParamPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceParamPartials'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_GetInputValue'] = _raise_uninitialized_error
        self.__dict__['_SetParameterOutputValue'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsLightReflectionResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsLightReflectionResultEval from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsLightReflectionResultEval = agcom.GUID(IAgAsLightReflectionResultEval._uuid)
        vtable_offset_local = IAgAsLightReflectionResultEval._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_GetLightSpeed'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarIntensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__['_GetSolarFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+7, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+8, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+11, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+12, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+13, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+14, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+15, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+16, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+17, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+18, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirection'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+19, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirection_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+20, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetReflectanceInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+21, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectance'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+22, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_IncidentDirectionVecInBodyPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+23, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionVecInBodyPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+24, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionVecPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+25, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionVecPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+26, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionBodyCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+27, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionBodyCompPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+28, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+29, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionCompPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+30, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionBodyCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+31, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionBodyCompVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+32, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+33, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionCompVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+34, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetReflectanceBodyCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+35, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+36, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceBodyCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+37, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+38, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_BodyFixedVectorPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+39, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_BodyFixedVectorPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+40, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_FrameFixedVectorPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+41, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_FrameFixedVectorPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+42, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_BodyFixedVectorVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+43, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_BodyFixedVectorVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+44, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_FrameFixedVectorVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+45, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_FrameFixedVectorVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+46, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_ParameterValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+47, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__['_GetParameterValue_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+48, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetReflectanceInBodyParamPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+49, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceParamPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+50, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_TransformVectorToBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+51, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorToBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+52, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVectorFromBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+53, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorFromBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+54, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+55, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+56, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+57, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+58, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+59, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_GetInputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+60, agcom.INT, POINTER(agcom.DOUBLE))
        self.__dict__['_SetParameterOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionResultEval, vtable_offset_local+61, agcom.INT, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsLightReflectionResultEval.__dict__ and type(IAgAsLightReflectionResultEval.__dict__[attrname]) == property:
            return IAgAsLightReflectionResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsLightReflectionResultEval.')
    
    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    @property
    def LightSpeed(self) -> float:
        """Speed of light in meters/second."""
        with agmarshall.DOUBLE_arg() as arg_pLightSpeed:
            agcls.evaluate_hresult(self.__dict__['_GetLightSpeed'](byref(arg_pLightSpeed.COM_val)))
            return arg_pLightSpeed.python_val

    @property
    def SolarIntensity(self) -> float:
        """Current solar intensity. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarIntensity:
            agcls.evaluate_hresult(self.__dict__['_GetSolarIntensity'](byref(arg_pSolarIntensity.COM_val)))
            return arg_pSolarIntensity.python_val

    @property
    def SolarFlux(self) -> float:
        """Current solar flux in watts/meter^2. Available only if SRP is on."""
        with agmarshall.DOUBLE_arg() as arg_pSolarFlux:
            agcls.evaluate_hresult(self.__dict__['_GetSolarFlux'](byref(arg_pSolarFlux.COM_val)))
            return arg_pSolarFlux.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def TotalMass(self) -> float:
        """Total Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    @property
    def Altitude(self) -> float:
        """Current altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude(meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirection_Array(self, frame:"AgEUtFrame") -> list:
        """Incident light direction (unitless) on the body, in the requested framereturned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirection_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetReflectanceInBody(self, x:float, y:float, z:float) -> None:
        """Sets reflectance (in m^2) in body components. Force = solarIntensity*luminosity/(4*pi*speedOfLight*distanceToSun^2)*reflectanceVec. reflectanceVec = sum of surface contributions where each surface N is cr_N*area_N*unitDirection_N."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceInBody'](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def SetReflectance(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> None:
        """Sets reflectance (in m^2) in specified frame. Force = solarIntensity*luminosity/(4*pi*speedOfLight*distanceToSun^2)*reflectanceVec. reflectanceVec = sum of surface contributions where each surface N is cr_N*area_N*unitDirection_N."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__['_SetReflectance'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def IncidentDirectionVecInBodyPosPartials_Array(self) -> list:
        """The partial derivatives in meters^-1 of the incident direction wrt inertial position coordinates, expressed in body components, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionVecInBodyPosPartials_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionVecPosPartials_Array(self, frame:"AgEUtFrame") -> list:
        """The partial derivatives in meters^-1 of the incident direction wrt inertial position coordinates, expressed in components of the requested frame, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionVecPosPartials_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionBodyCompPosPartials_Array(self) -> list:
        """The partial derivatives in meters^-1 of the incident direction body components wrt inertial position coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionBodyCompPosPartials_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionCompPosPartials_Array(self, frame:"AgEUtFrame") -> list:
        """The partial derivatives in meters^-1 of the incident direction components, expressed in the requested frame, wrt inertial position coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionCompPosPartials_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionBodyCompVelPartials_Array(self) -> list:
        """The partial derivatives in seconds/meter of the incident direction body components wrt inertial velocity coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionBodyCompVelPartials_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionCompVelPartials_Array(self, frame:"AgEUtFrame") -> list:
        """The partial derivatives in seconds/meter of the incident direction components, expressed in the requested frame, wrt inertial velocity coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionCompVelPartials_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetReflectanceBodyCompPosPartials(self, reflectXwrtX:float, reflectXwrtY:float, reflectXwrtZ:float, reflectYwrtX:float, reflectYwrtY:float, reflectYwrtZ:float, reflectZwrtX:float, reflectZwrtY:float, reflectZwrtZ:float) -> None:
        """Sets the partial derivatives in meters of the body components of reflectance wrt inertial position coordinates."""
        with agmarshall.DOUBLE_arg(reflectXwrtX) as arg_reflectXwrtX, \
             agmarshall.DOUBLE_arg(reflectXwrtY) as arg_reflectXwrtY, \
             agmarshall.DOUBLE_arg(reflectXwrtZ) as arg_reflectXwrtZ, \
             agmarshall.DOUBLE_arg(reflectYwrtX) as arg_reflectYwrtX, \
             agmarshall.DOUBLE_arg(reflectYwrtY) as arg_reflectYwrtY, \
             agmarshall.DOUBLE_arg(reflectYwrtZ) as arg_reflectYwrtZ, \
             agmarshall.DOUBLE_arg(reflectZwrtX) as arg_reflectZwrtX, \
             agmarshall.DOUBLE_arg(reflectZwrtY) as arg_reflectZwrtY, \
             agmarshall.DOUBLE_arg(reflectZwrtZ) as arg_reflectZwrtZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceBodyCompPosPartials'](arg_reflectXwrtX.COM_val, arg_reflectXwrtY.COM_val, arg_reflectXwrtZ.COM_val, arg_reflectYwrtX.COM_val, arg_reflectYwrtY.COM_val, arg_reflectYwrtZ.COM_val, arg_reflectZwrtX.COM_val, arg_reflectZwrtY.COM_val, arg_reflectZwrtZ.COM_val))

    def SetReflectanceCompPosPartials(self, frame:"AgEUtFrame", reflectXwrtX:float, reflectXwrtY:float, reflectXwrtZ:float, reflectYwrtX:float, reflectYwrtY:float, reflectYwrtZ:float, reflectZwrtX:float, reflectZwrtY:float, reflectZwrtZ:float) -> None:
        """Sets the partial derivatives in meters of the components of reflectance (expressed in the specified frame) wrt inertial position coordinates."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(reflectXwrtX) as arg_reflectXwrtX, \
             agmarshall.DOUBLE_arg(reflectXwrtY) as arg_reflectXwrtY, \
             agmarshall.DOUBLE_arg(reflectXwrtZ) as arg_reflectXwrtZ, \
             agmarshall.DOUBLE_arg(reflectYwrtX) as arg_reflectYwrtX, \
             agmarshall.DOUBLE_arg(reflectYwrtY) as arg_reflectYwrtY, \
             agmarshall.DOUBLE_arg(reflectYwrtZ) as arg_reflectYwrtZ, \
             agmarshall.DOUBLE_arg(reflectZwrtX) as arg_reflectZwrtX, \
             agmarshall.DOUBLE_arg(reflectZwrtY) as arg_reflectZwrtY, \
             agmarshall.DOUBLE_arg(reflectZwrtZ) as arg_reflectZwrtZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceCompPosPartials'](arg_frame.COM_val, arg_reflectXwrtX.COM_val, arg_reflectXwrtY.COM_val, arg_reflectXwrtZ.COM_val, arg_reflectYwrtX.COM_val, arg_reflectYwrtY.COM_val, arg_reflectYwrtZ.COM_val, arg_reflectZwrtX.COM_val, arg_reflectZwrtY.COM_val, arg_reflectZwrtZ.COM_val))

    def SetReflectanceBodyCompVelPartials(self, reflectXwrtVX:float, reflectXwrtVY:float, reflectXwrtVZ:float, reflectYwrtVX:float, reflectYwrtVY:float, reflectYwrtVZ:float, reflectZwrtVX:float, reflectZwrtVY:float, reflectZwrtVZ:float) -> None:
        """Sets the partial derivatives in meter-seconds of the body components of reflectance wrt inertial velocity coordinates."""
        with agmarshall.DOUBLE_arg(reflectXwrtVX) as arg_reflectXwrtVX, \
             agmarshall.DOUBLE_arg(reflectXwrtVY) as arg_reflectXwrtVY, \
             agmarshall.DOUBLE_arg(reflectXwrtVZ) as arg_reflectXwrtVZ, \
             agmarshall.DOUBLE_arg(reflectYwrtVX) as arg_reflectYwrtVX, \
             agmarshall.DOUBLE_arg(reflectYwrtVY) as arg_reflectYwrtVY, \
             agmarshall.DOUBLE_arg(reflectYwrtVZ) as arg_reflectYwrtVZ, \
             agmarshall.DOUBLE_arg(reflectZwrtVX) as arg_reflectZwrtVX, \
             agmarshall.DOUBLE_arg(reflectZwrtVY) as arg_reflectZwrtVY, \
             agmarshall.DOUBLE_arg(reflectZwrtVZ) as arg_reflectZwrtVZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceBodyCompVelPartials'](arg_reflectXwrtVX.COM_val, arg_reflectXwrtVY.COM_val, arg_reflectXwrtVZ.COM_val, arg_reflectYwrtVX.COM_val, arg_reflectYwrtVY.COM_val, arg_reflectYwrtVZ.COM_val, arg_reflectZwrtVX.COM_val, arg_reflectZwrtVY.COM_val, arg_reflectZwrtVZ.COM_val))

    def SetReflectanceCompVelPartials(self, frame:"AgEUtFrame", reflectXwrtVX:float, reflectXwrtVY:float, reflectXwrtVZ:float, reflectYwrtVX:float, reflectYwrtVY:float, reflectYwrtVZ:float, reflectZwrtVX:float, reflectZwrtVY:float, reflectZwrtVZ:float) -> None:
        """Sets the partial derivatives in meter-seconds of the components of reflectance (expressed in the specified frame) wrt inertial velocity coordinates."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(reflectXwrtVX) as arg_reflectXwrtVX, \
             agmarshall.DOUBLE_arg(reflectXwrtVY) as arg_reflectXwrtVY, \
             agmarshall.DOUBLE_arg(reflectXwrtVZ) as arg_reflectXwrtVZ, \
             agmarshall.DOUBLE_arg(reflectYwrtVX) as arg_reflectYwrtVX, \
             agmarshall.DOUBLE_arg(reflectYwrtVY) as arg_reflectYwrtVY, \
             agmarshall.DOUBLE_arg(reflectYwrtVZ) as arg_reflectYwrtVZ, \
             agmarshall.DOUBLE_arg(reflectZwrtVX) as arg_reflectZwrtVX, \
             agmarshall.DOUBLE_arg(reflectZwrtVY) as arg_reflectZwrtVY, \
             agmarshall.DOUBLE_arg(reflectZwrtVZ) as arg_reflectZwrtVZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceCompVelPartials'](arg_frame.COM_val, arg_reflectXwrtVX.COM_val, arg_reflectXwrtVY.COM_val, arg_reflectXwrtVZ.COM_val, arg_reflectYwrtVX.COM_val, arg_reflectYwrtVY.COM_val, arg_reflectYwrtVZ.COM_val, arg_reflectZwrtVX.COM_val, arg_reflectZwrtVY.COM_val, arg_reflectZwrtVZ.COM_val))

    def BodyFixedVectorPosPartials_Array(self, x:float, y:float, z:float) -> list:
        """The partial derivatives of the given body-fixed vector wrt inertial position coordinates in internal units, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_BodyFixedVectorPosPartials_Array'](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def FrameFixedVectorPosPartials_Array(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> list:
        """The partial derivatives of the given frame-fixed vector wrt inertial position coordinates in internal units, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_FrameFixedVectorPosPartials_Array'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def BodyFixedVectorVelPartials_Array(self, x:float, y:float, z:float) -> list:
        """The partial derivatives of the given body-fixed vector wrt inertial velocity coordinates in internal units, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_BodyFixedVectorVelPartials_Array'](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def FrameFixedVectorVelPartials_Array(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> list:
        """The partial derivatives of the given frame-fixed vector wrt inertial velocity coordinates in internal units, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_FrameFixedVectorVelPartials_Array'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def ParameterValue(self, index:int) -> float:
        """Parameter value in internal units for a registered parameter with indicated index."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_value:
            agcls.evaluate_hresult(self.__dict__['_ParameterValue'](arg_index.COM_val, byref(arg_value.COM_val)))
            return arg_value.python_val

    @property
    def ParameterValue_Array(self) -> list:
        """Parameter values in internal units for all registered parameters, returned in index order."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_GetParameterValue_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetReflectanceInBodyParamPartials(self, index:int, reflectXwrtParam:float, reflectYwrtParam:float, reflectZwrtParam:float) -> None:
        """Sets the partial derivatives of the body components of reflectance wrt the registered parameter specified by Index.  Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(reflectXwrtParam) as arg_reflectXwrtParam, \
             agmarshall.DOUBLE_arg(reflectYwrtParam) as arg_reflectYwrtParam, \
             agmarshall.DOUBLE_arg(reflectZwrtParam) as arg_reflectZwrtParam:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceInBodyParamPartials'](arg_index.COM_val, arg_reflectXwrtParam.COM_val, arg_reflectYwrtParam.COM_val, arg_reflectZwrtParam.COM_val))

    def SetReflectanceParamPartials(self, index:int, frame:"AgEUtFrame", reflectXwrtParam:float, reflectYwrtParam:float, reflectZwrtParam:float) -> None:
        """Sets the partial derivatives of the components of reflectance (expressed in the specified frame) wrt the registered parameter specified by Index.  Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(reflectXwrtParam) as arg_reflectXwrtParam, \
             agmarshall.DOUBLE_arg(reflectYwrtParam) as arg_reflectYwrtParam, \
             agmarshall.DOUBLE_arg(reflectZwrtParam) as arg_reflectZwrtParam:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceParamPartials'](arg_index.COM_val, arg_frame.COM_val, arg_reflectXwrtParam.COM_val, arg_reflectYwrtParam.COM_val, arg_reflectZwrtParam.COM_val))

    def TransformVectorToBody_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float) -> list:
        """Transforms a vector from the input frame to the body frame returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorToBody_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVectorFromBody_Array(self, xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the body frame to the output frame returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorFromBody_Array'](arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionInBody_Array(self) -> list:
        """Incident light direction (unitless) on the body, in the body frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionInBody_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def GetInputValue(self, index:int) -> float:
        """Gets the value of an input to the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetInputValue'](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetParameterOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a parameter output of the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetParameterOutputValue'](arg_index.COM_val, arg_val.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{18153B47-D0B5-46c1-8F58-FCC8EBDEBD19}', IAgAsLightReflectionResultEval)
agcls.AgTypeNameMap['IAgAsLightReflectionResultEval'] = IAgAsLightReflectionResultEval
__all__.append('IAgAsLightReflectionResultEval')

class IAgAsLightReflectionPluginSample(object):
    """Light Reflection sample plugin"""
    _uuid = '{597D4D2B-FCDD-479f-88CC-2026F011F5CF}'
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_SetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_GetDebugMode'] = _raise_uninitialized_error
        self.__dict__['_SetDebugMode'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsLightReflectionPluginSample._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsLightReflectionPluginSample from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsLightReflectionPluginSample = agcom.GUID(IAgAsLightReflectionPluginSample._uuid)
        vtable_offset_local = IAgAsLightReflectionPluginSample._vtable_offset - 1
        self.__dict__['_GetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionPluginSample, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__['_SetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionPluginSample, vtable_offset_local+2, agcom.LONG)
        self.__dict__['_GetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionPluginSample, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_SetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsLightReflectionPluginSample, vtable_offset_local+4, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsLightReflectionPluginSample.__dict__ and type(IAgAsLightReflectionPluginSample.__dict__[attrname]) == property:
            return IAgAsLightReflectionPluginSample.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsLightReflectionPluginSample.')
    
    @property
    def ReportFrequency(self) -> int:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg() as arg_pFreq:
            agcls.evaluate_hresult(self.__dict__['_GetReportFrequency'](byref(arg_pFreq.COM_val)))
            return arg_pFreq.python_val

    @ReportFrequency.setter
    def ReportFrequency(self, newFreq:int) -> None:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg(newFreq) as arg_newFreq:
            agcls.evaluate_hresult(self.__dict__['_SetReportFrequency'](arg_newFreq.COM_val))

    @property
    def DebugMode(self) -> bool:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pDebugMode:
            agcls.evaluate_hresult(self.__dict__['_GetDebugMode'](byref(arg_pDebugMode.COM_val)))
            return arg_pDebugMode.python_val

    @DebugMode.setter
    def DebugMode(self, newDebugMode:bool) -> None:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg(newDebugMode) as arg_newDebugMode:
            agcls.evaluate_hresult(self.__dict__['_SetDebugMode'](arg_newDebugMode.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{597D4D2B-FCDD-479f-88CC-2026F011F5CF}', IAgAsLightReflectionPluginSample)
agcls.AgTypeNameMap['IAgAsLightReflectionPluginSample'] = IAgAsLightReflectionPluginSample
__all__.append('IAgAsLightReflectionPluginSample')

class IAgAsDragModelResultRegister(object):
    """DragModel plugin interface used to register parameters that may be estimated."""
    _uuid = '{9788104C-76AD-4349-B2E7-BB07BE622BCB}'
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_RegisterParameter'] = _raise_uninitialized_error
        self.__dict__['_Message'] = _raise_uninitialized_error
        self.__dict__['_GetInstallDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetConfigDirectory'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserInput'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserParameterOutput'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDragModelResultRegister._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDragModelResultRegister from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDragModelResultRegister = agcom.GUID(IAgAsDragModelResultRegister._uuid)
        vtable_offset_local = IAgAsDragModelResultRegister._vtable_offset - 1
        self.__dict__['_RegisterParameter'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultRegister, vtable_offset_local+1, agcom.BSTR, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.BSTR, POINTER(agcom.LONG))
        self.__dict__['_Message'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultRegister, vtable_offset_local+2, agcom.LONG, agcom.BSTR)
        self.__dict__['_GetInstallDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultRegister, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_GetConfigDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultRegister, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__['_RegisterUserInput'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultRegister, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.LONG))
        self.__dict__['_RegisterUserParameterOutput'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultRegister, vtable_offset_local+6, agcom.BSTR, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDragModelResultRegister.__dict__ and type(IAgAsDragModelResultRegister.__dict__[attrname]) == property:
            return IAgAsDragModelResultRegister.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDragModelResultRegister.')
    
    def RegisterParameter(self, name:str, defaultValue:float, minValue:float, maxValue:float, dimension:str) -> int:
        """Registers a parameter of the computation that may be estimated. Returns an index identifier of the parameter used by other interfaces."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.DOUBLE_arg(defaultValue) as arg_defaultValue, \
             agmarshall.DOUBLE_arg(minValue) as arg_minValue, \
             agmarshall.DOUBLE_arg(maxValue) as arg_maxValue, \
             agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterParameter'](arg_name.COM_val, arg_defaultValue.COM_val, arg_minValue.COM_val, arg_maxValue.COM_val, arg_dimension.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val

    def Message(self, msgType:"AgEUtLogMsgType", message:str) -> None:
        """Send a message to the message viewer."""
        with agmarshall.AgEnum_arg(AgEUtLogMsgType, msgType) as arg_msgType, \
             agmarshall.BSTR_arg(message) as arg_message:
            agcls.evaluate_hresult(self.__dict__['_Message'](arg_msgType.COM_val, arg_message.COM_val))

    @property
    def InstallDirectory(self) -> str:
        """The directory path of the installation of the application."""
        with agmarshall.BSTR_arg() as arg_dirPath:
            agcls.evaluate_hresult(self.__dict__['_GetInstallDirectory'](byref(arg_dirPath.COM_val)))
            return arg_dirPath.python_val

    @property
    def ConfigDirectory(self) -> str:
        """The directory path of the user configuration area."""
        with agmarshall.BSTR_arg() as arg_dirPath:
            agcls.evaluate_hresult(self.__dict__['_GetConfigDirectory'](byref(arg_dirPath.COM_val)))
            return arg_dirPath.python_val

    def RegisterUserInput(self, userValue:str) -> int:
        """Registers as input to the plugin a user value in the state vector."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserInput'](arg_userValue.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val

    def RegisterUserParameterOutput(self, userValue:str) -> int:
        """Registers a user value in the state vector as a parameter output of the plugin."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserParameterOutput'](arg_userValue.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val


agcls.AgClassCatalog.add_catalog_entry('{9788104C-76AD-4349-B2E7-BB07BE622BCB}', IAgAsDragModelResultRegister)
agcls.AgTypeNameMap['IAgAsDragModelResultRegister'] = IAgAsDragModelResultRegister
__all__.append('IAgAsDragModelResultRegister')

class IAgAsDragModelResult(object):
    """DragModel plugin interface used to get/set settings. Supports the IAgEpoch interface."""
    _uuid = '{448B43F7-3B38-4bab-90C0-02679BAB34CB}'
    _num_methods = 36
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_Date'] = _raise_uninitialized_error
        self.__dict__['_Date_Array'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentVector'] = _raise_uninitialized_error
        self.__dict__['_IncidentVector_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentVectorInBody'] = _raise_uninitialized_error
        self.__dict__['_IncidentVectorInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPositionInBody'] = _raise_uninitialized_error
        self.__dict__['_SunPositionInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_GetInputValue'] = _raise_uninitialized_error
        self.__dict__['_SetParameterOutputValue'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDragModelResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDragModelResult from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDragModelResult = agcom.GUID(IAgAsDragModelResult._uuid)
        vtable_offset_local = IAgAsDragModelResult._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+4, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+5, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Date'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+6, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_Date_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+7, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+10, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+12, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+13, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+14, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+15, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirection'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+16, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirection_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+17, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVectorToBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+18, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorToBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+19, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVectorFromBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+20, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorFromBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+21, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+22, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+23, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+24, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+25, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentVectorInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+26, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentVectorInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+27, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+28, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+29, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPositionInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+30, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPositionInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+31, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+32, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+33, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+34, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_GetInputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+35, agcom.INT, POINTER(agcom.DOUBLE))
        self.__dict__['_SetParameterOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResult, vtable_offset_local+36, agcom.INT, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDragModelResult.__dict__ and type(IAgAsDragModelResult.__dict__[attrname]) == property:
            return IAgAsDragModelResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDragModelResult.')
    
    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Date_Array(self, scale:"AgEUtTimeScale") -> list:
        """This method is deprecated. Use DateElements instead. Current epoch in requested time scale expressed in date format returned as an array representing year [yyyy], dayOfYear, month [0-11], hour [0-23], minute [0-59], seconds. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Date_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def TotalMass(self) -> float:
        """Total Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    @property
    def Altitude(self) -> float:
        """Current altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude(meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirection_Array(self, frame:"AgEUtFrame") -> list:
        """Incident particle direction (unitless) on the body, in the requested frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirection_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVectorToBody_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float) -> list:
        """Transforms a vector from the input frame to the body frame returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorToBody_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVectorFromBody_Array(self, xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the body frame to the output frame returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorFromBody_Array'](arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionInBody_Array(self) -> list:
        """Incident particle direction (unitless) on the body, in the body frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionInBody_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentVector_Array(self, frame:"AgEUtFrame") -> list:
        """Incident particle vector on the body in meters/second, in the requested frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentVector_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentVectorInBody_Array(self) -> list:
        """Incident particle vector on the body in meters/second, in the body frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentVectorInBody_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPositionInBody_Array(self, sunPosType:"AgEUtSunPosType") -> list:
        """Position of the sun in meters wrt the current satellite position, in the body frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPositionInBody_Array'](arg_sunPosType.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def GetInputValue(self, index:int) -> float:
        """Gets the value of an input to the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetInputValue'](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetParameterOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a parameter output of the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetParameterOutputValue'](arg_index.COM_val, arg_val.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{448B43F7-3B38-4bab-90C0-02679BAB34CB}', IAgAsDragModelResult)
agcls.AgTypeNameMap['IAgAsDragModelResult'] = IAgAsDragModelResult
__all__.append('IAgAsDragModelResult')

class IAgAsDragModelResultEval(object):
    """DragModel plugin interface used to get/set settings during evaluation. Used to set reflectance vector (and optionally its partial derivs) used in computation of the drag/lift/side force. Supports the IAgEpoch interface."""
    _uuid = '{446E6858-5D1E-4bac-89D1-E5DC42343F2B}'
    _num_methods = 71
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_Date'] = _raise_uninitialized_error
        self.__dict__['_Date_Array'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirection_Array'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceInBody'] = _raise_uninitialized_error
        self.__dict__['_SetReflectance'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecInBodyPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecInBodyPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionVecPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionBodyCompVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionCompVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceBodyCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceCompPosPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceBodyCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceCompVelPartials'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorPosPartials'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorPosPartials'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorPosPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorVelPartials'] = _raise_uninitialized_error
        self.__dict__['_BodyFixedVectorVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorVelPartials'] = _raise_uninitialized_error
        self.__dict__['_FrameFixedVectorVelPartials_Array'] = _raise_uninitialized_error
        self.__dict__['_ParameterValue'] = _raise_uninitialized_error
        self.__dict__['_GetParameterValue_Array'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceInBodyParamPartials'] = _raise_uninitialized_error
        self.__dict__['_SetReflectanceParamPartials'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorToBody_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody'] = _raise_uninitialized_error
        self.__dict__['_TransformVectorFromBody_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody'] = _raise_uninitialized_error
        self.__dict__['_IncidentDirectionInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentVector'] = _raise_uninitialized_error
        self.__dict__['_IncidentVector_Array'] = _raise_uninitialized_error
        self.__dict__['_IncidentVectorInBody'] = _raise_uninitialized_error
        self.__dict__['_IncidentVectorInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPositionInBody'] = _raise_uninitialized_error
        self.__dict__['_SunPositionInBody_Array'] = _raise_uninitialized_error
        self.__dict__['_GetDensity'] = _raise_uninitialized_error
        self.__dict__['_GetAtmPressure'] = _raise_uninitialized_error
        self.__dict__['_GetAtmTemperature'] = _raise_uninitialized_error
        self.__dict__['_GetDragAltitude'] = _raise_uninitialized_error
        self.__dict__['_GetMeanMolecularMass'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_GetInputValue'] = _raise_uninitialized_error
        self.__dict__['_SetParameterOutputValue'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDragModelResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDragModelResultEval from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDragModelResultEval = agcom.GUID(IAgAsDragModelResultEval._uuid)
        vtable_offset_local = IAgAsDragModelResultEval._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+4, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+5, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Date'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+6, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_Date_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+7, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+10, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+11, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+12, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+13, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+14, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+15, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+16, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+17, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirection'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+18, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirection_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+19, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetReflectanceInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+20, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectance'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+21, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_IncidentDirectionVecInBodyPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+22, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionVecInBodyPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+23, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionVecPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+24, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionVecPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+25, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionBodyCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+26, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionBodyCompPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+27, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+28, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionCompPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+29, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionBodyCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+30, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionBodyCompVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+31, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+32, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionCompVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+33, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetReflectanceBodyCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+34, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceCompPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+35, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceBodyCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+36, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceCompVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+37, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_BodyFixedVectorPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+38, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_BodyFixedVectorPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+39, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_FrameFixedVectorPosPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+40, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_FrameFixedVectorPosPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+41, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_BodyFixedVectorVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+42, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_BodyFixedVectorVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+43, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_FrameFixedVectorVelPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+44, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_FrameFixedVectorVelPartials_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+45, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_ParameterValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+46, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__['_GetParameterValue_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+47, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetReflectanceInBodyParamPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+48, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_SetReflectanceParamPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+49, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_TransformVectorToBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+50, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorToBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+51, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVectorFromBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+52, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVectorFromBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+53, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentDirectionInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+54, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentDirectionInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+55, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+56, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+57, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_IncidentVectorInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+58, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_IncidentVectorInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+59, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPositionInBody'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+60, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPositionInBody_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+61, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetDensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+62, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAtmPressure'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+63, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAtmTemperature'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+64, POINTER(agcom.DOUBLE))
        self.__dict__['_GetDragAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+65, POINTER(agcom.DOUBLE))
        self.__dict__['_GetMeanMolecularMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+66, POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+67, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+68, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+69, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_GetInputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+70, agcom.INT, POINTER(agcom.DOUBLE))
        self.__dict__['_SetParameterOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelResultEval, vtable_offset_local+71, agcom.INT, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDragModelResultEval.__dict__ and type(IAgAsDragModelResultEval.__dict__[attrname]) == property:
            return IAgAsDragModelResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDragModelResultEval.')
    
    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Date_Array(self, scale:"AgEUtTimeScale") -> list:
        """This method is deprecated. Use DateElements instead. Current epoch in requested time scale expressed in date format returned as an array representing year [yyyy], dayOfYear, month [0-11], hour [0-23], minute [0-59], seconds. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Date_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def TotalMass(self) -> float:
        """Total Mass in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    @property
    def Altitude(self) -> float:
        """Current altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude(meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirection_Array(self, frame:"AgEUtFrame") -> list:
        """Incident particle direction (unitless) on the body, in the requested frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirection_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetReflectanceInBody(self, x:float, y:float, z:float) -> None:
        """Sets reflectance (in m^2) in body components. Force = 0.5*density*velCBF^2*reflectanceVec. reflectanceVec = sum of surface contributions where each surface N is cd_N*area_N*unitDirection_N."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceInBody'](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def SetReflectance(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> None:
        """Sets reflectance (in m^2) in specified frame. Force = 0.5*density*velCBF^2*reflectanceVec. reflectanceVec = sum of surface contributions where each surface N is cd_N*area_N*unitDirection_N."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__['_SetReflectance'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def IncidentDirectionVecInBodyPosPartials_Array(self) -> list:
        """The partial derivatives in meters^-1 of the incident direction wrt inertial position coordinates, expressed in body components, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionVecInBodyPosPartials_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionVecPosPartials_Array(self, frame:"AgEUtFrame") -> list:
        """The partial derivatives in meters^-1 of the incident direction wrt inertial position coordinates, expressed in components of the requested frame, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionVecPosPartials_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionBodyCompPosPartials_Array(self) -> list:
        """The partial derivatives in meters^-1 of the incident direction body components wrt inertial position coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionBodyCompPosPartials_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionCompPosPartials_Array(self, frame:"AgEUtFrame") -> list:
        """The partial derivatives in meters^-1 of the incident direction components, expressed in the requested frame, wrt inertial position coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionCompPosPartials_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionBodyCompVelPartials_Array(self) -> list:
        """The partial derivatives in seconds/meter of the incident direction body components wrt inertial velocity coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionBodyCompVelPartials_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionCompVelPartials_Array(self, frame:"AgEUtFrame") -> list:
        """The partial derivatives in seconds/meter of the incident direction components, expressed in the requested frame, wrt inertial velocity coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionCompVelPartials_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetReflectanceBodyCompPosPartials(self, reflectXwrtX:float, reflectXwrtY:float, reflectXwrtZ:float, reflectYwrtX:float, reflectYwrtY:float, reflectYwrtZ:float, reflectZwrtX:float, reflectZwrtY:float, reflectZwrtZ:float) -> None:
        """Sets the partial derivatives in meters of the body components of reflectance wrt inertial position coordinates."""
        with agmarshall.DOUBLE_arg(reflectXwrtX) as arg_reflectXwrtX, \
             agmarshall.DOUBLE_arg(reflectXwrtY) as arg_reflectXwrtY, \
             agmarshall.DOUBLE_arg(reflectXwrtZ) as arg_reflectXwrtZ, \
             agmarshall.DOUBLE_arg(reflectYwrtX) as arg_reflectYwrtX, \
             agmarshall.DOUBLE_arg(reflectYwrtY) as arg_reflectYwrtY, \
             agmarshall.DOUBLE_arg(reflectYwrtZ) as arg_reflectYwrtZ, \
             agmarshall.DOUBLE_arg(reflectZwrtX) as arg_reflectZwrtX, \
             agmarshall.DOUBLE_arg(reflectZwrtY) as arg_reflectZwrtY, \
             agmarshall.DOUBLE_arg(reflectZwrtZ) as arg_reflectZwrtZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceBodyCompPosPartials'](arg_reflectXwrtX.COM_val, arg_reflectXwrtY.COM_val, arg_reflectXwrtZ.COM_val, arg_reflectYwrtX.COM_val, arg_reflectYwrtY.COM_val, arg_reflectYwrtZ.COM_val, arg_reflectZwrtX.COM_val, arg_reflectZwrtY.COM_val, arg_reflectZwrtZ.COM_val))

    def SetReflectanceCompPosPartials(self, frame:"AgEUtFrame", reflectXwrtX:float, reflectXwrtY:float, reflectXwrtZ:float, reflectYwrtX:float, reflectYwrtY:float, reflectYwrtZ:float, reflectZwrtX:float, reflectZwrtY:float, reflectZwrtZ:float) -> None:
        """Sets the partial derivatives in meters of the components of reflectance (expressed in the specified frame) wrt inertial position coordinates."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(reflectXwrtX) as arg_reflectXwrtX, \
             agmarshall.DOUBLE_arg(reflectXwrtY) as arg_reflectXwrtY, \
             agmarshall.DOUBLE_arg(reflectXwrtZ) as arg_reflectXwrtZ, \
             agmarshall.DOUBLE_arg(reflectYwrtX) as arg_reflectYwrtX, \
             agmarshall.DOUBLE_arg(reflectYwrtY) as arg_reflectYwrtY, \
             agmarshall.DOUBLE_arg(reflectYwrtZ) as arg_reflectYwrtZ, \
             agmarshall.DOUBLE_arg(reflectZwrtX) as arg_reflectZwrtX, \
             agmarshall.DOUBLE_arg(reflectZwrtY) as arg_reflectZwrtY, \
             agmarshall.DOUBLE_arg(reflectZwrtZ) as arg_reflectZwrtZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceCompPosPartials'](arg_frame.COM_val, arg_reflectXwrtX.COM_val, arg_reflectXwrtY.COM_val, arg_reflectXwrtZ.COM_val, arg_reflectYwrtX.COM_val, arg_reflectYwrtY.COM_val, arg_reflectYwrtZ.COM_val, arg_reflectZwrtX.COM_val, arg_reflectZwrtY.COM_val, arg_reflectZwrtZ.COM_val))

    def SetReflectanceBodyCompVelPartials(self, reflectXwrtVX:float, reflectXwrtVY:float, reflectXwrtVZ:float, reflectYwrtVX:float, reflectYwrtVY:float, reflectYwrtVZ:float, reflectZwrtVX:float, reflectZwrtVY:float, reflectZwrtVZ:float) -> None:
        """Sets the partial derivatives in meter-seconds of the body components of reflectance wrt inertial velocity coordinates."""
        with agmarshall.DOUBLE_arg(reflectXwrtVX) as arg_reflectXwrtVX, \
             agmarshall.DOUBLE_arg(reflectXwrtVY) as arg_reflectXwrtVY, \
             agmarshall.DOUBLE_arg(reflectXwrtVZ) as arg_reflectXwrtVZ, \
             agmarshall.DOUBLE_arg(reflectYwrtVX) as arg_reflectYwrtVX, \
             agmarshall.DOUBLE_arg(reflectYwrtVY) as arg_reflectYwrtVY, \
             agmarshall.DOUBLE_arg(reflectYwrtVZ) as arg_reflectYwrtVZ, \
             agmarshall.DOUBLE_arg(reflectZwrtVX) as arg_reflectZwrtVX, \
             agmarshall.DOUBLE_arg(reflectZwrtVY) as arg_reflectZwrtVY, \
             agmarshall.DOUBLE_arg(reflectZwrtVZ) as arg_reflectZwrtVZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceBodyCompVelPartials'](arg_reflectXwrtVX.COM_val, arg_reflectXwrtVY.COM_val, arg_reflectXwrtVZ.COM_val, arg_reflectYwrtVX.COM_val, arg_reflectYwrtVY.COM_val, arg_reflectYwrtVZ.COM_val, arg_reflectZwrtVX.COM_val, arg_reflectZwrtVY.COM_val, arg_reflectZwrtVZ.COM_val))

    def SetReflectanceCompVelPartials(self, frame:"AgEUtFrame", reflectXwrtVX:float, reflectXwrtVY:float, reflectXwrtVZ:float, reflectYwrtVX:float, reflectYwrtVY:float, reflectYwrtVZ:float, reflectZwrtVX:float, reflectZwrtVY:float, reflectZwrtVZ:float) -> None:
        """Sets the partial derivatives in meter-seconds of the components of reflectance (expressed in the specified frame) wrt inertial velocity coordinates."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(reflectXwrtVX) as arg_reflectXwrtVX, \
             agmarshall.DOUBLE_arg(reflectXwrtVY) as arg_reflectXwrtVY, \
             agmarshall.DOUBLE_arg(reflectXwrtVZ) as arg_reflectXwrtVZ, \
             agmarshall.DOUBLE_arg(reflectYwrtVX) as arg_reflectYwrtVX, \
             agmarshall.DOUBLE_arg(reflectYwrtVY) as arg_reflectYwrtVY, \
             agmarshall.DOUBLE_arg(reflectYwrtVZ) as arg_reflectYwrtVZ, \
             agmarshall.DOUBLE_arg(reflectZwrtVX) as arg_reflectZwrtVX, \
             agmarshall.DOUBLE_arg(reflectZwrtVY) as arg_reflectZwrtVY, \
             agmarshall.DOUBLE_arg(reflectZwrtVZ) as arg_reflectZwrtVZ:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceCompVelPartials'](arg_frame.COM_val, arg_reflectXwrtVX.COM_val, arg_reflectXwrtVY.COM_val, arg_reflectXwrtVZ.COM_val, arg_reflectYwrtVX.COM_val, arg_reflectYwrtVY.COM_val, arg_reflectYwrtVZ.COM_val, arg_reflectZwrtVX.COM_val, arg_reflectZwrtVY.COM_val, arg_reflectZwrtVZ.COM_val))

    def BodyFixedVectorPosPartials_Array(self, x:float, y:float, z:float) -> list:
        """The partial derivatives of the given body-fixed vector wrt inertial position coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients.  Uses internal units."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_BodyFixedVectorPosPartials_Array'](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def FrameFixedVectorPosPartials_Array(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> list:
        """The partial derivatives of the given frame-fixed vector wrt inertial position coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients.  Uses internal units."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_FrameFixedVectorPosPartials_Array'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def BodyFixedVectorVelPartials_Array(self, x:float, y:float, z:float) -> list:
        """The partial derivatives of the given body-fixed vector wrt inertial velocity coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients.  Uses internal units."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_BodyFixedVectorVelPartials_Array'](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def FrameFixedVectorVelPartials_Array(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> list:
        """The partial derivatives of the given frame-fixed vector wrt inertial velocity coordinates, returned as an array representing the rows of the matrix. Useful for scripting clients.  Uses internal units."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_FrameFixedVectorVelPartials_Array'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def ParameterValue(self, index:int) -> float:
        """Parameter value for a registered parameter with indicated index.  Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_value:
            agcls.evaluate_hresult(self.__dict__['_ParameterValue'](arg_index.COM_val, byref(arg_value.COM_val)))
            return arg_value.python_val

    @property
    def ParameterValue_Array(self) -> list:
        """Parameter values for all registered parameters, returned in index order.  Uses internal units."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_GetParameterValue_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetReflectanceInBodyParamPartials(self, index:int, reflectXwrtParam:float, reflectYwrtParam:float, reflectZwrtParam:float) -> None:
        """Sets the partial derivatives of the body components of reflectance wrt the registered parameter specified by Index.  Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(reflectXwrtParam) as arg_reflectXwrtParam, \
             agmarshall.DOUBLE_arg(reflectYwrtParam) as arg_reflectYwrtParam, \
             agmarshall.DOUBLE_arg(reflectZwrtParam) as arg_reflectZwrtParam:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceInBodyParamPartials'](arg_index.COM_val, arg_reflectXwrtParam.COM_val, arg_reflectYwrtParam.COM_val, arg_reflectZwrtParam.COM_val))

    def SetReflectanceParamPartials(self, index:int, frame:"AgEUtFrame", reflectXwrtParam:float, reflectYwrtParam:float, reflectZwrtParam:float) -> None:
        """Sets the partial derivatives of the components of reflectance (expressed in the specified frame) wrt the registered parameter specified by Index.  Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(reflectXwrtParam) as arg_reflectXwrtParam, \
             agmarshall.DOUBLE_arg(reflectYwrtParam) as arg_reflectYwrtParam, \
             agmarshall.DOUBLE_arg(reflectZwrtParam) as arg_reflectZwrtParam:
            agcls.evaluate_hresult(self.__dict__['_SetReflectanceParamPartials'](arg_index.COM_val, arg_frame.COM_val, arg_reflectXwrtParam.COM_val, arg_reflectYwrtParam.COM_val, arg_reflectZwrtParam.COM_val))

    def TransformVectorToBody_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float) -> list:
        """Transforms a vector from the input frame to the body frame returned as an array representing x, y, z. Useful for scripting clients.  Uses internal units."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorToBody_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVectorFromBody_Array(self, xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the body frame to the output frame returned as an array representing x, y, z. Useful for scripting clients.  Uses internal units."""
        with agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVectorFromBody_Array'](arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentDirectionInBody_Array(self) -> list:
        """Incident particle direction (unitless) on the body, in the body frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentDirectionInBody_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentVector_Array(self, frame:"AgEUtFrame") -> list:
        """Incident particle vector on the body in meters/second, in the requested frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentVector_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def IncidentVectorInBody_Array(self) -> list:
        """Incident particle vector on the body in meters/second, in the body frame, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_IncidentVectorInBody_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPositionInBody_Array(self, sunPosType:"AgEUtSunPosType") -> list:
        """Position of the sun in meters wrt the current satellite position, in the body frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPositionInBody_Array'](arg_sunPosType.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def Density(self) -> float:
        """Current atmospheric density in kg/meter^3."""
        with agmarshall.DOUBLE_arg() as arg_pDensity:
            agcls.evaluate_hresult(self.__dict__['_GetDensity'](byref(arg_pDensity.COM_val)))
            return arg_pDensity.python_val

    @property
    def AtmPressure(self) -> float:
        """Current atmospheric pressure in pascals (N/m^2). Available if supported by atm density model (MSIS)."""
        with agmarshall.DOUBLE_arg() as arg_pPressure:
            agcls.evaluate_hresult(self.__dict__['_GetAtmPressure'](byref(arg_pPressure.COM_val)))
            return arg_pPressure.python_val

    @property
    def AtmTemperature(self) -> float:
        """Current atmospheric temperature in K. Available if supported by atm density model (MSIS)."""
        with agmarshall.DOUBLE_arg() as arg_pTemperature:
            agcls.evaluate_hresult(self.__dict__['_GetAtmTemperature'](byref(arg_pTemperature.COM_val)))
            return arg_pTemperature.python_val

    @property
    def DragAltitude(self) -> float:
        """Altitude used for current atmospheric density computation in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__['_GetDragAltitude'](byref(arg_pAlt.COM_val)))
            return arg_pAlt.python_val

    @property
    def MeanMolecularMass(self) -> float:
        """Mean molecular mass from current atmospheric density computation in kg/kmol. Available if supported by atm density model (MSIS)."""
        with agmarshall.DOUBLE_arg() as arg_pMMM:
            agcls.evaluate_hresult(self.__dict__['_GetMeanMolecularMass'](byref(arg_pMMM.COM_val)))
            return arg_pMMM.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def GetInputValue(self, index:int) -> float:
        """Gets the value of an input to the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetInputValue'](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetParameterOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a parameter output of the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetParameterOutputValue'](arg_index.COM_val, arg_val.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{446E6858-5D1E-4bac-89D1-E5DC42343F2B}', IAgAsDragModelResultEval)
agcls.AgTypeNameMap['IAgAsDragModelResultEval'] = IAgAsDragModelResultEval
__all__.append('IAgAsDragModelResultEval')

class IAgAsDragModelPluginSample(object):
    """Drag model sample plugin"""
    _uuid = '{E3A2A809-6F1E-41f2-809C-237D1D5929DB}'
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_SetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_GetDebugMode'] = _raise_uninitialized_error
        self.__dict__['_SetDebugMode'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDragModelPluginSample._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDragModelPluginSample from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDragModelPluginSample = agcom.GUID(IAgAsDragModelPluginSample._uuid)
        vtable_offset_local = IAgAsDragModelPluginSample._vtable_offset - 1
        self.__dict__['_GetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelPluginSample, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__['_SetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelPluginSample, vtable_offset_local+2, agcom.LONG)
        self.__dict__['_GetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelPluginSample, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_SetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsDragModelPluginSample, vtable_offset_local+4, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDragModelPluginSample.__dict__ and type(IAgAsDragModelPluginSample.__dict__[attrname]) == property:
            return IAgAsDragModelPluginSample.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDragModelPluginSample.')
    
    @property
    def ReportFrequency(self) -> int:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg() as arg_pFreq:
            agcls.evaluate_hresult(self.__dict__['_GetReportFrequency'](byref(arg_pFreq.COM_val)))
            return arg_pFreq.python_val

    @ReportFrequency.setter
    def ReportFrequency(self, newFreq:int) -> None:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg(newFreq) as arg_newFreq:
            agcls.evaluate_hresult(self.__dict__['_SetReportFrequency'](arg_newFreq.COM_val))

    @property
    def DebugMode(self) -> bool:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pDebugMode:
            agcls.evaluate_hresult(self.__dict__['_GetDebugMode'](byref(arg_pDebugMode.COM_val)))
            return arg_pDebugMode.python_val

    @DebugMode.setter
    def DebugMode(self, newDebugMode:bool) -> None:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg(newDebugMode) as arg_newDebugMode:
            agcls.evaluate_hresult(self.__dict__['_SetDebugMode'](arg_newDebugMode.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{E3A2A809-6F1E-41f2-809C-237D1D5929DB}', IAgAsDragModelPluginSample)
agcls.AgTypeNameMap['IAgAsDragModelPluginSample'] = IAgAsDragModelPluginSample
__all__.append('IAgAsDragModelPluginSample')

class IAgAsEOMFuncPluginRegisterHandler(object):
    """EOM func plugin interface used to register the plugin's inputs, outputs, and events."""
    _uuid = '{7B7AAACB-773C-4c5d-BD88-62D0A9F05663}'
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_RegisterInput'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserInput'] = _raise_uninitialized_error
        self.__dict__['_RegisterParameterOutput'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserParameterOutput'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserDerivativeOutput'] = _raise_uninitialized_error
        self.__dict__['_ExcludeEvent'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsEOMFuncPluginRegisterHandler._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsEOMFuncPluginRegisterHandler from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsEOMFuncPluginRegisterHandler = agcom.GUID(IAgAsEOMFuncPluginRegisterHandler._uuid)
        vtable_offset_local = IAgAsEOMFuncPluginRegisterHandler._vtable_offset - 1
        self.__dict__['_RegisterInput'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginRegisterHandler, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_RegisterUserInput'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginRegisterHandler, vtable_offset_local+2, agcom.BSTR)
        self.__dict__['_RegisterParameterOutput'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginRegisterHandler, vtable_offset_local+3, agcom.LONG)
        self.__dict__['_RegisterUserParameterOutput'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginRegisterHandler, vtable_offset_local+4, agcom.BSTR)
        self.__dict__['_RegisterUserDerivativeOutput'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginRegisterHandler, vtable_offset_local+5, agcom.BSTR)
        self.__dict__['_ExcludeEvent'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginRegisterHandler, vtable_offset_local+6, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsEOMFuncPluginRegisterHandler.__dict__ and type(IAgAsEOMFuncPluginRegisterHandler.__dict__[attrname]) == property:
            return IAgAsEOMFuncPluginRegisterHandler.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsEOMFuncPluginRegisterHandler.')
    
    def RegisterInput(self, stateValue:"AgEAsEOMFuncPluginInputStateValues") -> None:
        """Registers as input to the plugin a built-in value in the state vector."""
        with agmarshall.AgEnum_arg(AgEAsEOMFuncPluginInputStateValues, stateValue) as arg_stateValue:
            agcls.evaluate_hresult(self.__dict__['_RegisterInput'](arg_stateValue.COM_val))

    def RegisterUserInput(self, userValue:str) -> None:
        """Registers as input to the plugin a user value in the state vector."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserInput'](arg_userValue.COM_val))

    def RegisterParameterOutput(self, stateValue:"AgEAsEOMFuncPluginOutputStateValues") -> None:
        """Registers a built-in value in the state vector as a parameter output of the plugin."""
        with agmarshall.AgEnum_arg(AgEAsEOMFuncPluginOutputStateValues, stateValue) as arg_stateValue:
            agcls.evaluate_hresult(self.__dict__['_RegisterParameterOutput'](arg_stateValue.COM_val))

    def RegisterUserParameterOutput(self, userValue:str) -> None:
        """Registers a user value in the state vector as a parameter output of the plugin."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserParameterOutput'](arg_userValue.COM_val))

    def RegisterUserDerivativeOutput(self, userValue:str) -> None:
        """Registers a user value in the state vector of which the plugin will give the 1st derivative."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserDerivativeOutput'](arg_userValue.COM_val))

    def ExcludeEvent(self, eventType:"AgEAsEOMFuncPluginEventTypes") -> None:
        """Registers an event on which the plugin should not be run."""
        with agmarshall.AgEnum_arg(AgEAsEOMFuncPluginEventTypes, eventType) as arg_eventType:
            agcls.evaluate_hresult(self.__dict__['_ExcludeEvent'](arg_eventType.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{7B7AAACB-773C-4c5d-BD88-62D0A9F05663}', IAgAsEOMFuncPluginRegisterHandler)
agcls.AgTypeNameMap['IAgAsEOMFuncPluginRegisterHandler'] = IAgAsEOMFuncPluginRegisterHandler
__all__.append('IAgAsEOMFuncPluginRegisterHandler')

class IAgAsEOMFuncPluginSetIndicesHandler(object):
    """EOM func plugin interface used to set the indices of the plugin's input and output."""
    _uuid = '{C0B4C47F-9292-4f13-BA9B-7DC4117E6720}'
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetInputIndex'] = _raise_uninitialized_error
        self.__dict__['_GetUserInputIndex'] = _raise_uninitialized_error
        self.__dict__['_GetParameterOutputIndex'] = _raise_uninitialized_error
        self.__dict__['_GetUserParameterOutputIndex'] = _raise_uninitialized_error
        self.__dict__['_GetUserDerivativeOutputIndex'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsEOMFuncPluginSetIndicesHandler._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsEOMFuncPluginSetIndicesHandler from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsEOMFuncPluginSetIndicesHandler = agcom.GUID(IAgAsEOMFuncPluginSetIndicesHandler._uuid)
        vtable_offset_local = IAgAsEOMFuncPluginSetIndicesHandler._vtable_offset - 1
        self.__dict__['_GetInputIndex'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginSetIndicesHandler, vtable_offset_local+1, agcom.LONG, POINTER(agcom.INT))
        self.__dict__['_GetUserInputIndex'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginSetIndicesHandler, vtable_offset_local+2, agcom.BSTR, POINTER(agcom.INT))
        self.__dict__['_GetParameterOutputIndex'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginSetIndicesHandler, vtable_offset_local+3, agcom.LONG, POINTER(agcom.INT))
        self.__dict__['_GetUserParameterOutputIndex'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginSetIndicesHandler, vtable_offset_local+4, agcom.BSTR, POINTER(agcom.INT))
        self.__dict__['_GetUserDerivativeOutputIndex'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginSetIndicesHandler, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.INT))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsEOMFuncPluginSetIndicesHandler.__dict__ and type(IAgAsEOMFuncPluginSetIndicesHandler.__dict__[attrname]) == property:
            return IAgAsEOMFuncPluginSetIndicesHandler.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsEOMFuncPluginSetIndicesHandler.')
    
    def GetInputIndex(self, stateValue:"AgEAsEOMFuncPluginInputStateValues") -> int:
        """Gets the index of an input to the plugin of a built-in value in the state vector."""
        with agmarshall.AgEnum_arg(AgEAsEOMFuncPluginInputStateValues, stateValue) as arg_stateValue, \
             agmarshall.INT_arg() as arg_pIndex:
            agcls.evaluate_hresult(self.__dict__['_GetInputIndex'](arg_stateValue.COM_val, byref(arg_pIndex.COM_val)))
            return arg_pIndex.python_val

    def GetUserInputIndex(self, userValue:str) -> int:
        """Gets the index of an input to the plugin of a user value in the state vector."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.INT_arg() as arg_pIndex:
            agcls.evaluate_hresult(self.__dict__['_GetUserInputIndex'](arg_userValue.COM_val, byref(arg_pIndex.COM_val)))
            return arg_pIndex.python_val

    def GetParameterOutputIndex(self, stateValue:"AgEAsEOMFuncPluginOutputStateValues") -> int:
        """Gets the index of parameter output of the plugin of a built-in value in the state vector."""
        with agmarshall.AgEnum_arg(AgEAsEOMFuncPluginOutputStateValues, stateValue) as arg_stateValue, \
             agmarshall.INT_arg() as arg_pIndex:
            agcls.evaluate_hresult(self.__dict__['_GetParameterOutputIndex'](arg_stateValue.COM_val, byref(arg_pIndex.COM_val)))
            return arg_pIndex.python_val

    def GetUserParameterOutputIndex(self, userValue:str) -> int:
        """Gets the index of parameter output of the plugin of a built-in value in the state vector."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.INT_arg() as arg_pIndex:
            agcls.evaluate_hresult(self.__dict__['_GetUserParameterOutputIndex'](arg_userValue.COM_val, byref(arg_pIndex.COM_val)))
            return arg_pIndex.python_val

    def GetUserDerivativeOutputIndex(self, userValue:str) -> int:
        """Gets the index of a user value in the state vector of which the plugin will give the 1st derivative."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.INT_arg() as arg_pIndex:
            agcls.evaluate_hresult(self.__dict__['_GetUserDerivativeOutputIndex'](arg_userValue.COM_val, byref(arg_pIndex.COM_val)))
            return arg_pIndex.python_val


agcls.AgClassCatalog.add_catalog_entry('{C0B4C47F-9292-4f13-BA9B-7DC4117E6720}', IAgAsEOMFuncPluginSetIndicesHandler)
agcls.AgTypeNameMap['IAgAsEOMFuncPluginSetIndicesHandler'] = IAgAsEOMFuncPluginSetIndicesHandler
__all__.append('IAgAsEOMFuncPluginSetIndicesHandler')

class IAgAsEOMFuncPluginStateVector(object):
    """State vector interface for EOM func plugins."""
    _uuid = '{0BCCB4E4-1CA6-4919-9F24-DCA7B7407FAD}'
    _num_methods = 22
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetInputValue'] = _raise_uninitialized_error
        self.__dict__['_SetParameterOutputValue'] = _raise_uninitialized_error
        self.__dict__['_AddDerivativeOutputValue'] = _raise_uninitialized_error
        self.__dict__['_GetTimeSinceRefEpoch'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_TransformVector'] = _raise_uninitialized_error
        self.__dict__['_TransformVector_Array'] = _raise_uninitialized_error
        self.__dict__['_AddAcceleration'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_StopPropagation'] = _raise_uninitialized_error
        self.__dict__['_IndicateEvent'] = _raise_uninitialized_error
        self.__dict__['_SetMaxStep'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements'] = _raise_uninitialized_error
        self.__dict__['_RefEpochElements_Array'] = _raise_uninitialized_error
        self.__dict__['_RefEpochString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsEOMFuncPluginStateVector._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsEOMFuncPluginStateVector from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsEOMFuncPluginStateVector = agcom.GUID(IAgAsEOMFuncPluginStateVector._uuid)
        vtable_offset_local = IAgAsEOMFuncPluginStateVector._vtable_offset - 1
        self.__dict__['_GetInputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+1, agcom.INT, POINTER(agcom.DOUBLE))
        self.__dict__['_SetParameterOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+2, agcom.INT, agcom.DOUBLE)
        self.__dict__['_AddDerivativeOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+3, agcom.INT, agcom.DOUBLE)
        self.__dict__['_GetTimeSinceRefEpoch'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+5, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+7, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+8, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+9, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_TransformVector'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+10, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_TransformVector_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+11, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AddAcceleration'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+12, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+13, POINTER(agcom.DOUBLE))
        self.__dict__['_StopPropagation'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+14, )
        self.__dict__['_IndicateEvent'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+15, agcom.LONG)
        self.__dict__['_SetMaxStep'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+16, agcom.DOUBLE)
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+17, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+18, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+19, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_RefEpochElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+20, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_RefEpochElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+21, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_RefEpochString'] = IAGFUNCTYPE(pUnk, IID_IAgAsEOMFuncPluginStateVector, vtable_offset_local+22, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsEOMFuncPluginStateVector.__dict__ and type(IAgAsEOMFuncPluginStateVector.__dict__[attrname]) == property:
            return IAgAsEOMFuncPluginStateVector.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsEOMFuncPluginStateVector.')
    
    def GetInputValue(self, index:int) -> float:
        """Gets the value of an input to the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetInputValue'](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetParameterOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a parameter output of the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetParameterOutputValue'](arg_index.COM_val, arg_val.COM_val))

    def AddDerivativeOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a first derivative in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_AddDerivativeOutputValue'](arg_index.COM_val, arg_val.COM_val))

    @property
    def TimeSinceRefEpoch(self) -> float:
        """Current epoch expressed in seconds since reference epoch."""
        with agmarshall.DOUBLE_arg() as arg_pTimeSinceRefEpoch:
            agcls.evaluate_hresult(self.__dict__['_GetTimeSinceRefEpoch'](byref(arg_pTimeSinceRefEpoch.COM_val)))
            return arg_pTimeSinceRefEpoch.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) in the requested frame returned as an array representing x, y, z, vx, vy, vz. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def TransformVector_Array(self, frameFrom:"AgEUtFrame", xFrom:float, yFrom:float, zFrom:float, frameTo:"AgEUtFrame") -> list:
        """Transforms a vector from the input frame to the output frame (in internal units) returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frameFrom) as arg_frameFrom, \
             agmarshall.DOUBLE_arg(xFrom) as arg_xFrom, \
             agmarshall.DOUBLE_arg(yFrom) as arg_yFrom, \
             agmarshall.DOUBLE_arg(zFrom) as arg_zFrom, \
             agmarshall.AgEnum_arg(AgEUtFrame, frameTo) as arg_frameTo, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_TransformVector_Array'](arg_frameFrom.COM_val, arg_xFrom.COM_val, arg_yFrom.COM_val, arg_zFrom.COM_val, arg_frameTo.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AddAcceleration(self, frame:"AgEUtFrame", x:float, y:float, z:float) -> None:
        """Add the acceleration in meters/second^2 in the given frame to the force model."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__['_AddAcceleration'](arg_frame.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    def StopPropagation(self) -> None:
        """Stops propagation.  For fatal errors."""
        agcls.evaluate_hresult(self.__dict__['_StopPropagation']())

    def IndicateEvent(self, eventIndicator:"AgEAsHpopPluginEventIndicators") -> None:
        """Marks an event to the propagator."""
        with agmarshall.AgEnum_arg(AgEAsHpopPluginEventIndicators, eventIndicator) as arg_eventIndicator:
            agcls.evaluate_hresult(self.__dict__['_IndicateEvent'](arg_eventIndicator.COM_val))

    def SetMaxStep(self, maxStep:float) -> None:
        """Sets the maximum step size in seconds for the propagator."""
        with agmarshall.DOUBLE_arg(maxStep) as arg_maxStep:
            agcls.evaluate_hresult(self.__dict__['_SetMaxStep'](arg_maxStep.COM_val))

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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

    def RefEpochElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Reference epoch expressed in requested time scale in day count and date formats as the array: WholeDays, SecsIntoDay, Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_RefEpochElements_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def RefEpochString(self, dateAbbrv:str) -> str:
        """Reference epoch expressed using the date format abbreviation specified."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pRefEpochString:
            agcls.evaluate_hresult(self.__dict__['_RefEpochString'](arg_dateAbbrv.COM_val, byref(arg_pRefEpochString.COM_val)))
            return arg_pRefEpochString.python_val


agcls.AgClassCatalog.add_catalog_entry('{0BCCB4E4-1CA6-4919-9F24-DCA7B7407FAD}', IAgAsEOMFuncPluginStateVector)
agcls.AgTypeNameMap['IAgAsEOMFuncPluginStateVector'] = IAgAsEOMFuncPluginStateVector
__all__.append('IAgAsEOMFuncPluginStateVector')

class IAgAsDensityModelResultRegister(object):
    """DensityModel plugin interface used to register parameters that may be estimated."""
    _uuid = '{9788104C-76AD-4349-B2E7-BB07BE622BCA}'
    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_RegisterParameter'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserInput'] = _raise_uninitialized_error
        self.__dict__['_RegisterUserParameterOutput'] = _raise_uninitialized_error
        self.__dict__['_Message'] = _raise_uninitialized_error
        self.__dict__['_GetInstallDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetConfigDirectory'] = _raise_uninitialized_error
        self.__dict__['_SetParameterizationName'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDensityModelResultRegister._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDensityModelResultRegister from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDensityModelResultRegister = agcom.GUID(IAgAsDensityModelResultRegister._uuid)
        vtable_offset_local = IAgAsDensityModelResultRegister._vtable_offset - 1
        self.__dict__['_RegisterParameter'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultRegister, vtable_offset_local+1, agcom.BSTR, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.BSTR, POINTER(agcom.LONG))
        self.__dict__['_RegisterUserInput'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultRegister, vtable_offset_local+2, agcom.BSTR, POINTER(agcom.LONG))
        self.__dict__['_RegisterUserParameterOutput'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultRegister, vtable_offset_local+3, agcom.BSTR, POINTER(agcom.LONG))
        self.__dict__['_Message'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultRegister, vtable_offset_local+4, agcom.LONG, agcom.BSTR)
        self.__dict__['_GetInstallDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultRegister, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__['_GetConfigDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultRegister, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__['_SetParameterizationName'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultRegister, vtable_offset_local+7, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDensityModelResultRegister.__dict__ and type(IAgAsDensityModelResultRegister.__dict__[attrname]) == property:
            return IAgAsDensityModelResultRegister.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDensityModelResultRegister.')
    
    def RegisterParameter(self, name:str, defaultValue:float, minValue:float, maxValue:float, dimension:str) -> int:
        """Registers a parameter of the computation that may be estimated. Returns an index identifier of the parameter used by other interfaces."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.DOUBLE_arg(defaultValue) as arg_defaultValue, \
             agmarshall.DOUBLE_arg(minValue) as arg_minValue, \
             agmarshall.DOUBLE_arg(maxValue) as arg_maxValue, \
             agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterParameter'](arg_name.COM_val, arg_defaultValue.COM_val, arg_minValue.COM_val, arg_maxValue.COM_val, arg_dimension.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val

    def RegisterUserInput(self, userValue:str) -> int:
        """Registers as input to the plugin a user value in the state vector."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserInput'](arg_userValue.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val

    def RegisterUserParameterOutput(self, userValue:str) -> int:
        """Registers a user value in the state vector as a parameter output of the plugin."""
        with agmarshall.BSTR_arg(userValue) as arg_userValue, \
             agmarshall.LONG_arg() as arg_index:
            agcls.evaluate_hresult(self.__dict__['_RegisterUserParameterOutput'](arg_userValue.COM_val, byref(arg_index.COM_val)))
            return arg_index.python_val

    def Message(self, msgType:"AgEUtLogMsgType", message:str) -> None:
        """Send a message to the message viewer."""
        with agmarshall.AgEnum_arg(AgEUtLogMsgType, msgType) as arg_msgType, \
             agmarshall.BSTR_arg(message) as arg_message:
            agcls.evaluate_hresult(self.__dict__['_Message'](arg_msgType.COM_val, arg_message.COM_val))

    @property
    def InstallDirectory(self) -> str:
        """The directory path of the installation of the application."""
        with agmarshall.BSTR_arg() as arg_dirPath:
            agcls.evaluate_hresult(self.__dict__['_GetInstallDirectory'](byref(arg_dirPath.COM_val)))
            return arg_dirPath.python_val

    @property
    def ConfigDirectory(self) -> str:
        """The directory path of the user configuration area."""
        with agmarshall.BSTR_arg() as arg_dirPath:
            agcls.evaluate_hresult(self.__dict__['_GetConfigDirectory'](byref(arg_dirPath.COM_val)))
            return arg_dirPath.python_val

    def SetParameterizationName(self, name:str) -> None:
        """Registers a name for the estimation parameterization. This name is used during the selection of estimation parameters and to validate files of pre-computed corrections."""
        with agmarshall.BSTR_arg(name) as arg_name:
            agcls.evaluate_hresult(self.__dict__['_SetParameterizationName'](arg_name.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{9788104C-76AD-4349-B2E7-BB07BE622BCA}', IAgAsDensityModelResultRegister)
agcls.AgTypeNameMap['IAgAsDensityModelResultRegister'] = IAgAsDensityModelResultRegister
__all__.append('IAgAsDensityModelResultRegister')

class IAgAsDensityModelResult(object):
    """DensityModel plugin interface used to get settings during numerical integration events. Supports the IAgEpoch interface."""
    _uuid = '{1672791D-FE81-459A-B8F4-26B7E68C7063}'
    _num_methods = 30
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_ParameterValue'] = _raise_uninitialized_error
        self.__dict__['_GetParameterValue_Array'] = _raise_uninitialized_error
        self.__dict__['_GetInputValue'] = _raise_uninitialized_error
        self.__dict__['_SetParameterOutputValue'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags_Array'] = _raise_uninitialized_error
        self.__dict__['_CurrentAugmentedAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_CurrentAugmentedAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AugmentedAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_AugmentedAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_GetComputeParameterPartials'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDensityModelResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDensityModelResult from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDensityModelResult = agcom.GUID(IAgAsDensityModelResult._uuid)
        vtable_offset_local = IAgAsDensityModelResult._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+4, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+5, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+7, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+8, POINTER(agcom.SAFEARRAY))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+9, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+10, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+11, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+12, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_ParameterValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+13, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__['_GetParameterValue_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+14, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetInputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+15, agcom.INT, POINTER(agcom.DOUBLE))
        self.__dict__['_SetParameterOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+16, agcom.INT, agcom.DOUBLE)
        self.__dict__['_CurrentAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+17, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_CurrentAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+18, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+19, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+20, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+21, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFluxLags_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+22, POINTER(agcom.SAFEARRAY))
        self.__dict__['_CurrentAugmentedAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+23, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_CurrentAugmentedAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+24, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AugmentedAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+25, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AugmentedAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+26, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetComputeParameterPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+27, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+28, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+29, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResult, vtable_offset_local+30, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDensityModelResult.__dict__ and type(IAgAsDensityModelResult.__dict__[attrname]) == property:
            return IAgAsDensityModelResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDensityModelResult.')
    
    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def Altitude(self) -> float:
        """Current detic altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude(meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) returned as an array representing X, Y, Z, VX, VY, VZ. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def ParameterValue(self, index:int) -> float:
        """Parameter value for a registered parameter with indicated index.  Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_value:
            agcls.evaluate_hresult(self.__dict__['_ParameterValue'](arg_index.COM_val, byref(arg_value.COM_val)))
            return arg_value.python_val

    @property
    def ParameterValue_Array(self) -> list:
        """Parameter values for all registered parameters, returned in index order.  Uses internal units."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_GetParameterValue_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def GetInputValue(self, index:int) -> float:
        """Gets the value of an input to the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetInputValue'](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetParameterOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a parameter output of the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetParameterOutputValue'](arg_index.COM_val, arg_val.COM_val))

    def CurrentAtmFlux_Array(self) -> list:
        """Flux values used by the density model, evaluated at the current time using model supplied time lags, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_CurrentAtmFlux_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFlux_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Flux values used by density models, evaluated at the requested time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp. No time lags are incorporated."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFlux_Array'](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFluxLags_Array(self) -> list:
        """The lag times (in secs), relative to the current epoch, at which the density flux values are evaluated, returned as an array of F10.7 lag, geo flux lag."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFluxLags_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentAugmentedAtmFlux_Array(self) -> list:
        """Augmented flux values used by the density model, evaluated at the current time using model supplied time lags, returned as an array representing M10.7, AvgM10.7, S10.7, AvgS10.7, Y10.7, AvgY10.7, DstDTc."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_CurrentAugmentedAtmFlux_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AugmentedAtmFlux_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Augmented flux values used by density models, evaluated at the requested time, returned as an array representing F10.7, AvgF10.7, M10.7, AvgM10.7, S10.7, AvgS10.7, Y10.7, AvgY10.7, DstDTc. No time lags are incorporated."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AugmentedAtmFlux_Array'](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def ComputeParameterPartials(self) -> bool:
        """Indicates if registered density model parameters are being estimated. If the returned value is false, parameter partials need not be computed"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pComputeParameterPartials:
            agcls.evaluate_hresult(self.__dict__['_GetComputeParameterPartials'](byref(arg_pComputeParameterPartials.COM_val)))
            return arg_pComputeParameterPartials.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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


agcls.AgClassCatalog.add_catalog_entry('{1672791D-FE81-459A-B8F4-26B7E68C7063}', IAgAsDensityModelResult)
agcls.AgTypeNameMap['IAgAsDensityModelResult'] = IAgAsDensityModelResult
__all__.append('IAgAsDensityModelResult')

class IAgAsDensityModelResultEval(object):
    """DensityModel plugin interface used to get/set settings during evaluation. Supports the IAgEpoch interface."""
    _uuid = '{446E6858-5D1E-4bac-89D1-E5DC42343F2C}'
    _num_methods = 38
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_Trace'] = _raise_uninitialized_error
        self.__dict__['_GetMu'] = _raise_uninitialized_error
        self.__dict__['_GetCbName'] = _raise_uninitialized_error
        self.__dict__['_DayCount'] = _raise_uninitialized_error
        self.__dict__['_DayCount_Array'] = _raise_uninitialized_error
        self.__dict__['_Date'] = _raise_uninitialized_error
        self.__dict__['_Date_Array'] = _raise_uninitialized_error
        self.__dict__['_GetTotalMass'] = _raise_uninitialized_error
        self.__dict__['_GetAltitude'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt'] = _raise_uninitialized_error
        self.__dict__['_LatLonAlt_Array'] = _raise_uninitialized_error
        self.__dict__['_PosVel'] = _raise_uninitialized_error
        self.__dict__['_PosVel_Array'] = _raise_uninitialized_error
        self.__dict__['_SunPosition'] = _raise_uninitialized_error
        self.__dict__['_SunPosition_Array'] = _raise_uninitialized_error
        self.__dict__['_ParameterValue'] = _raise_uninitialized_error
        self.__dict__['_GetParameterValue_Array'] = _raise_uninitialized_error
        self.__dict__['_SetDensity'] = _raise_uninitialized_error
        self.__dict__['_SetTemperature'] = _raise_uninitialized_error
        self.__dict__['_SetPressure'] = _raise_uninitialized_error
        self.__dict__['_GetInputValue'] = _raise_uninitialized_error
        self.__dict__['_SetParameterOutputValue'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_CurrentAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux'] = _raise_uninitialized_error
        self.__dict__['_AtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags'] = _raise_uninitialized_error
        self.__dict__['_AtmFluxLags_Array'] = _raise_uninitialized_error
        self.__dict__['_CurrentAugmentedAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_CurrentAugmentedAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_AugmentedAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_AugmentedAtmFlux_Array'] = _raise_uninitialized_error
        self.__dict__['_SetParameterPartialDerivative'] = _raise_uninitialized_error
        self.__dict__['_GetComputeParameterPartials'] = _raise_uninitialized_error
        self.__dict__['_ConstAugAtmFlux'] = _raise_uninitialized_error
        self.__dict__['_DateElements'] = _raise_uninitialized_error
        self.__dict__['_DateElements_Array'] = _raise_uninitialized_error
        self.__dict__['_DateString'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDensityModelResultEval._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDensityModelResultEval from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDensityModelResultEval = agcom.GUID(IAgAsDensityModelResultEval._uuid)
        vtable_offset_local = IAgAsDensityModelResultEval._vtable_offset - 1
        self.__dict__['_Trace'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+1, agcom.LONG)
        self.__dict__['_GetMu'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_GetCbName'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_DayCount'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+4, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DayCount_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+5, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_Date'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+6, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_Date_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+7, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_GetTotalMass'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_GetAltitude'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+9, POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+10, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_LatLonAlt_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+11, POINTER(agcom.SAFEARRAY))
        self.__dict__['_PosVel'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+12, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_PosVel_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SunPosition'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+14, agcom.LONG, agcom.LONG, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_SunPosition_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+15, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_ParameterValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+16, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__['_GetParameterValue_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+17, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetDensity'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+18, agcom.DOUBLE)
        self.__dict__['_SetTemperature'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+19, agcom.DOUBLE)
        self.__dict__['_SetPressure'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+20, agcom.DOUBLE)
        self.__dict__['_GetInputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+21, agcom.INT, POINTER(agcom.DOUBLE))
        self.__dict__['_SetParameterOutputValue'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+22, agcom.INT, agcom.DOUBLE)
        self.__dict__['_CurrentAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+23, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_CurrentAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+24, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+25, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+26, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+27, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AtmFluxLags_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+28, POINTER(agcom.SAFEARRAY))
        self.__dict__['_CurrentAugmentedAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+29, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_CurrentAugmentedAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+30, POINTER(agcom.SAFEARRAY))
        self.__dict__['_AugmentedAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+31, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_AugmentedAtmFlux_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+32, agcom.LONG, agcom.LONG, agcom.DOUBLE, POINTER(agcom.SAFEARRAY))
        self.__dict__['_SetParameterPartialDerivative'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+33, agcom.LONG, agcom.DOUBLE)
        self.__dict__['_GetComputeParameterPartials'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+34, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_ConstAugAtmFlux'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+35, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+36, agcom.LONG, POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.LONG), POINTER(agcom.DOUBLE))
        self.__dict__['_DateElements_Array'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+37, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__['_DateString'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelResultEval, vtable_offset_local+38, agcom.BSTR, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDensityModelResultEval.__dict__ and type(IAgAsDensityModelResultEval.__dict__[attrname]) == property:
            return IAgAsDensityModelResultEval.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDensityModelResultEval.')
    
    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__['_Trace'](arg_numCalls.COM_val))

    @property
    def Mu(self) -> float:
        """Gravitational constant in meters^3/second^2."""
        with agmarshall.DOUBLE_arg() as arg_pMu:
            agcls.evaluate_hresult(self.__dict__['_GetMu'](byref(arg_pMu.COM_val)))
            return arg_pMu.python_val

    @property
    def CbName(self) -> str:
        """Name of the central body used as reference frame origin."""
        with agmarshall.BSTR_arg() as arg_pCbName:
            agcls.evaluate_hresult(self.__dict__['_GetCbName'](byref(arg_pCbName.COM_val)))
            return arg_pCbName.python_val

    def DayCount_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in day count format returned as an array representing wholeDays, secsIntoDay. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_DayCount_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def Date_Array(self, scale:"AgEUtTimeScale") -> list:
        """This method is deprecated. Use DateElements_Array instead. Current epoch in requested time scale expressed in date format returned as an array representing year [yyyy], dayOfYear, month [0-11], hour [0-23], minute [0-59], seconds."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_Date_Array'](arg_scale.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    @property
    def TotalMass(self) -> float:
        """This property is deprecated. Total Mass of the satellite in kilograms."""
        with agmarshall.DOUBLE_arg() as arg_pTotalMass:
            agcls.evaluate_hresult(self.__dict__['_GetTotalMass'](byref(arg_pTotalMass.COM_val)))
            return arg_pTotalMass.python_val

    @property
    def Altitude(self) -> float:
        """Current detic altitude in meters."""
        with agmarshall.DOUBLE_arg() as arg_pAltitude:
            agcls.evaluate_hresult(self.__dict__['_GetAltitude'](byref(arg_pAltitude.COM_val)))
            return arg_pAltitude.python_val

    def LatLonAlt_Array(self) -> list:
        """Current detic latitude (radians), detic longitude (radians), and altitude(meters) returned as an array representing lat, lon, alt. Useful for scripting clients."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_LatLonAlt_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def PosVel_Array(self, frame:"AgEUtFrame") -> list:
        """Current position (meters) and velocity (meters/second) returned as an array representing X, Y, Z, VX, VY, VZ. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_PosVel_Array'](arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SunPosition_Array(self, sunPosType:"AgEUtSunPosType", frame:"AgEUtFrame") -> list:
        """Position of the sun in meters wrt the current satellite position, in the requested frame, computed in the requested manner, returned as an array representing x, y, z. Useful for scripting clients."""
        with agmarshall.AgEnum_arg(AgEUtSunPosType, sunPosType) as arg_sunPosType, \
             agmarshall.AgEnum_arg(AgEUtFrame, frame) as arg_frame, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_SunPosition_Array'](arg_sunPosType.COM_val, arg_frame.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def ParameterValue(self, index:int) -> float:
        """Parameter value for a registered parameter with indicated index.  Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_value:
            agcls.evaluate_hresult(self.__dict__['_ParameterValue'](arg_index.COM_val, byref(arg_value.COM_val)))
            return arg_value.python_val

    @property
    def ParameterValue_Array(self) -> list:
        """Parameter values for all registered parameters, returned in index order.  Uses internal units."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_GetParameterValue_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetDensity(self, density:float) -> None:
        """Sets the Density for the model"""
        with agmarshall.DOUBLE_arg(density) as arg_density:
            agcls.evaluate_hresult(self.__dict__['_SetDensity'](arg_density.COM_val))

    def SetTemperature(self, temperature:float) -> None:
        """Sets the Temperature for the model in Kelvin"""
        with agmarshall.DOUBLE_arg(temperature) as arg_temperature:
            agcls.evaluate_hresult(self.__dict__['_SetTemperature'](arg_temperature.COM_val))

    def SetPressure(self, pressure:float) -> None:
        """Sets the Pressure for the model"""
        with agmarshall.DOUBLE_arg(pressure) as arg_pressure:
            agcls.evaluate_hresult(self.__dict__['_SetPressure'](arg_pressure.COM_val))

    def GetInputValue(self, index:int) -> float:
        """Gets the value of an input to the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetInputValue'](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetParameterOutputValue(self, index:int, val:float) -> None:
        """Sets the value of a parameter output of the plugin in internal units."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetParameterOutputValue'](arg_index.COM_val, arg_val.COM_val))

    def CurrentAtmFlux_Array(self) -> list:
        """Flux values used by the density model, evaluated at the current time using model supplied time lags, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_CurrentAtmFlux_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFlux_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Flux values used by density models, evaluated at the requested time, returned as an array representing F10.7, AvgF10.7, Ap, DailyAp, Kp, DailyKp. No time lags are incorporated."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFlux_Array'](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AtmFluxLags_Array(self) -> list:
        """The lag times (in secs), relative to the current epoch, at which the density flux values are evaluated, returned as an array of F10.7 lag, geo flux lag."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AtmFluxLags_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def CurrentAugmentedAtmFlux_Array(self) -> list:
        """Augmented flux values used by the density model, evaluated at the current time using model supplied time lags, returned as an array representing M10.7, AvgM10.7, S10.7, AvgS10.7, Y10.7, AvgY10.7, DstDTc."""
        with agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_CurrentAugmentedAtmFlux_Array'](byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def AugmentedAtmFlux_Array(self, scale:"AgEUtTimeScale", wholeDays:int, secsIntoDay:float) -> list:
        """Augmented flux values used by density models, evaluated at the requested time, returned as an array representing F10.7, AvgF10.7, M10.7, AvgM10.7, S10.7, AvgS10.7, Y10.7, AvgY10.7, DstDTc. No time lags are incorporated."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(wholeDays) as arg_wholeDays, \
             agmarshall.DOUBLE_arg(secsIntoDay) as arg_secsIntoDay, \
             agmarshall.SAFEARRAY_arg() as arg_pArray:
            agcls.evaluate_hresult(self.__dict__['_AugmentedAtmFlux_Array'](arg_scale.COM_val, arg_wholeDays.COM_val, arg_secsIntoDay.COM_val, byref(arg_pArray.COM_val)))
            return arg_pArray.python_val

    def SetParameterPartialDerivative(self, index:int, partialDeriv:float) -> None:
        """Set value of partial derivative of density with respect to parameter value for a registered parameter with indicated index. Required for parameter estimation. Uses internal units."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(partialDeriv) as arg_partialDeriv:
            agcls.evaluate_hresult(self.__dict__['_SetParameterPartialDerivative'](arg_index.COM_val, arg_partialDeriv.COM_val))

    @property
    def ComputeParameterPartials(self) -> bool:
        """Indicates if registered density model parameters are being estimated. If the returned value is false, parameter partials need not be computed"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pComputeParameterPartials:
            agcls.evaluate_hresult(self.__dict__['_GetComputeParameterPartials'](byref(arg_pComputeParameterPartials.COM_val)))
            return arg_pComputeParameterPartials.python_val

    def DateElements_Array(self, scale:"AgEUtTimeScale") -> list:
        """Current epoch in requested time scale expressed in date format returned as the array: Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]. Useful for scripting clients."""
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


agcls.AgClassCatalog.add_catalog_entry('{446E6858-5D1E-4bac-89D1-E5DC42343F2C}', IAgAsDensityModelResultEval)
agcls.AgTypeNameMap['IAgAsDensityModelResultEval'] = IAgAsDensityModelResultEval
__all__.append('IAgAsDensityModelResultEval')

class IAgAsDensityModelPluginAtmFluxLagsConfig(object):
    """DensityModel plugin interface used to get/set AtmFluxLag values"""
    _uuid = '{E7C297CE-097E-463D-83F0-5D7E0DC3A68C}'
    _num_methods = 20
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_SetF10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_GetF10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_SetF10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_GetF10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_SetGeoFluxLag'] = _raise_uninitialized_error
        self.__dict__['_GetGeoFluxLag'] = _raise_uninitialized_error
        self.__dict__['_SetM10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_GetM10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_SetM10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_GetM10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_SetS10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_GetS10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_SetS10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_GetS10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_SetY10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_GetY10p7Lag'] = _raise_uninitialized_error
        self.__dict__['_SetY10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_GetY10p7MeanLag'] = _raise_uninitialized_error
        self.__dict__['_SetDstDTcLag'] = _raise_uninitialized_error
        self.__dict__['_GetDstDTcLag'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDensityModelPluginAtmFluxLagsConfig._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDensityModelPluginAtmFluxLagsConfig from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDensityModelPluginAtmFluxLagsConfig = agcom.GUID(IAgAsDensityModelPluginAtmFluxLagsConfig._uuid)
        vtable_offset_local = IAgAsDensityModelPluginAtmFluxLagsConfig._vtable_offset - 1
        self.__dict__['_SetF10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+1, agcom.DOUBLE)
        self.__dict__['_GetF10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__['_SetF10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+3, agcom.DOUBLE)
        self.__dict__['_GetF10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__['_SetGeoFluxLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+5, agcom.DOUBLE)
        self.__dict__['_GetGeoFluxLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+6, POINTER(agcom.DOUBLE))
        self.__dict__['_SetM10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+7, agcom.DOUBLE)
        self.__dict__['_GetM10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+8, POINTER(agcom.DOUBLE))
        self.__dict__['_SetM10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+9, agcom.DOUBLE)
        self.__dict__['_GetM10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+10, POINTER(agcom.DOUBLE))
        self.__dict__['_SetS10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+11, agcom.DOUBLE)
        self.__dict__['_GetS10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+12, POINTER(agcom.DOUBLE))
        self.__dict__['_SetS10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+13, agcom.DOUBLE)
        self.__dict__['_GetS10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+14, POINTER(agcom.DOUBLE))
        self.__dict__['_SetY10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+15, agcom.DOUBLE)
        self.__dict__['_GetY10p7Lag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+16, POINTER(agcom.DOUBLE))
        self.__dict__['_SetY10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+17, agcom.DOUBLE)
        self.__dict__['_GetY10p7MeanLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+18, POINTER(agcom.DOUBLE))
        self.__dict__['_SetDstDTcLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+19, agcom.DOUBLE)
        self.__dict__['_GetDstDTcLag'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLagsConfig, vtable_offset_local+20, POINTER(agcom.DOUBLE))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDensityModelPluginAtmFluxLagsConfig.__dict__ and type(IAgAsDensityModelPluginAtmFluxLagsConfig.__dict__[attrname]) == property:
            return IAgAsDensityModelPluginAtmFluxLagsConfig.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDensityModelPluginAtmFluxLagsConfig.')
    
    @property
    def F10p7Lag(self) -> float:
        """Gets or sets the F10p7Lag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetF10p7Lag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @F10p7Lag.setter
    def F10p7Lag(self, val:float) -> None:
        """Gets or sets the F10p7Lag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetF10p7Lag'](arg_val.COM_val))

    @property
    def F10p7MeanLag(self) -> float:
        """Gets or sets the F10p7MeanLag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetF10p7MeanLag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @F10p7MeanLag.setter
    def F10p7MeanLag(self, val:float) -> None:
        """Gets or sets the F10p7MeanLag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetF10p7MeanLag'](arg_val.COM_val))

    @property
    def GeoFluxLag(self) -> float:
        """Gets or sets the GeoFluxLag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetGeoFluxLag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @GeoFluxLag.setter
    def GeoFluxLag(self, val:float) -> None:
        """Gets or sets the GeoFluxLag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetGeoFluxLag'](arg_val.COM_val))

    @property
    def M10p7Lag(self) -> float:
        """Gets or sets the M10p7Lag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetM10p7Lag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @M10p7Lag.setter
    def M10p7Lag(self, val:float) -> None:
        """Gets or sets the M10p7Lag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetM10p7Lag'](arg_val.COM_val))

    @property
    def M10p7MeanLag(self) -> float:
        """Gets or sets the M10p7MeanLag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetM10p7MeanLag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @M10p7MeanLag.setter
    def M10p7MeanLag(self, val:float) -> None:
        """Gets or sets the M10p7MeanLag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetM10p7MeanLag'](arg_val.COM_val))

    @property
    def S10p7Lag(self) -> float:
        """Gets or sets the S10p7Lag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetS10p7Lag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @S10p7Lag.setter
    def S10p7Lag(self, val:float) -> None:
        """Gets or sets the S10p7Lag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetS10p7Lag'](arg_val.COM_val))

    @property
    def S10p7MeanLag(self) -> float:
        """Gets or sets the S10p7MeanLag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetS10p7MeanLag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @S10p7MeanLag.setter
    def S10p7MeanLag(self, val:float) -> None:
        """Gets or sets the S10p7MeanLag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetS10p7MeanLag'](arg_val.COM_val))

    @property
    def Y10p7Lag(self) -> float:
        """Gets or sets the Y10p7Lag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetY10p7Lag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Y10p7Lag.setter
    def Y10p7Lag(self, val:float) -> None:
        """Gets or sets the Y10p7Lag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetY10p7Lag'](arg_val.COM_val))

    @property
    def Y10p7MeanLag(self) -> float:
        """Gets or sets the Y10p7MeanLag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetY10p7MeanLag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Y10p7MeanLag.setter
    def Y10p7MeanLag(self, val:float) -> None:
        """Gets or sets the Y10p7MeanLag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetY10p7MeanLag'](arg_val.COM_val))

    @property
    def DstDTcLag(self) -> float:
        """Gets or sets the DstDTcLag"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__['_GetDstDTcLag'](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @DstDTcLag.setter
    def DstDTcLag(self, val:float) -> None:
        """Gets or sets the DstDTcLag"""
        with agmarshall.DOUBLE_arg(val) as arg_val:
            agcls.evaluate_hresult(self.__dict__['_SetDstDTcLag'](arg_val.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{E7C297CE-097E-463D-83F0-5D7E0DC3A68C}', IAgAsDensityModelPluginAtmFluxLagsConfig)
agcls.AgTypeNameMap['IAgAsDensityModelPluginAtmFluxLagsConfig'] = IAgAsDensityModelPluginAtmFluxLagsConfig
__all__.append('IAgAsDensityModelPluginAtmFluxLagsConfig')

class IAgAsDensityModelPluginAtmFluxLags(object):
    """Density Model plugin interface that handles the getting/setting of AtmFluxLags"""
    _uuid = '{81378D5F-EDE9-4EEE-82AD-AB010C2DD06D}'
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_OverrideAtmFluxLags'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDensityModelPluginAtmFluxLags._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDensityModelPluginAtmFluxLags from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDensityModelPluginAtmFluxLags = agcom.GUID(IAgAsDensityModelPluginAtmFluxLags._uuid)
        vtable_offset_local = IAgAsDensityModelPluginAtmFluxLags._vtable_offset - 1
        self.__dict__['_OverrideAtmFluxLags'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginAtmFluxLags, vtable_offset_local+1, agcom.PVOID)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDensityModelPluginAtmFluxLags.__dict__ and type(IAgAsDensityModelPluginAtmFluxLags.__dict__[attrname]) == property:
            return IAgAsDensityModelPluginAtmFluxLags.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDensityModelPluginAtmFluxLags.')
    
    def OverrideAtmFluxLags(self, fluxLags:"IAgAsDensityModelPluginAtmFluxLagsConfig") -> None:
        """The lag times (in secs), relative to the current epoch, at which the density flux values are evaluated."""
        with agmarshall.AgInterface_in_arg(fluxLags, IAgAsDensityModelPluginAtmFluxLagsConfig) as arg_fluxLags:
            agcls.evaluate_hresult(self.__dict__['_OverrideAtmFluxLags'](arg_fluxLags.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{81378D5F-EDE9-4EEE-82AD-AB010C2DD06D}', IAgAsDensityModelPluginAtmFluxLags)
agcls.AgTypeNameMap['IAgAsDensityModelPluginAtmFluxLags'] = IAgAsDensityModelPluginAtmFluxLags
__all__.append('IAgAsDensityModelPluginAtmFluxLags')

class IAgAsDensityModelPluginSample(object):
    """Density model sample plugin"""
    _uuid = '{E3A2A809-6F1E-41f2-809C-237D1D5929DC}'
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_SetReportFrequency'] = _raise_uninitialized_error
        self.__dict__['_GetDebugMode'] = _raise_uninitialized_error
        self.__dict__['_SetDebugMode'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgAsDensityModelPluginSample._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgAsDensityModelPluginSample from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IID_IAgAsDensityModelPluginSample = agcom.GUID(IAgAsDensityModelPluginSample._uuid)
        vtable_offset_local = IAgAsDensityModelPluginSample._vtable_offset - 1
        self.__dict__['_GetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginSample, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__['_SetReportFrequency'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginSample, vtable_offset_local+2, agcom.LONG)
        self.__dict__['_GetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginSample, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__['_SetDebugMode'] = IAGFUNCTYPE(pUnk, IID_IAgAsDensityModelPluginSample, vtable_offset_local+4, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsDensityModelPluginSample.__dict__ and type(IAgAsDensityModelPluginSample.__dict__[attrname]) == property:
            return IAgAsDensityModelPluginSample.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in IAgAsDensityModelPluginSample.')
    
    @property
    def ReportFrequency(self) -> int:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg() as arg_pFreq:
            agcls.evaluate_hresult(self.__dict__['_GetReportFrequency'](byref(arg_pFreq.COM_val)))
            return arg_pFreq.python_val

    @ReportFrequency.setter
    def ReportFrequency(self, newFreq:int) -> None:
        """Frequency of output of debug messages, in number of integration steps."""
        with agmarshall.LONG_arg(newFreq) as arg_newFreq:
            agcls.evaluate_hresult(self.__dict__['_SetReportFrequency'](arg_newFreq.COM_val))

    @property
    def DebugMode(self) -> bool:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pDebugMode:
            agcls.evaluate_hresult(self.__dict__['_GetDebugMode'](byref(arg_pDebugMode.COM_val)))
            return arg_pDebugMode.python_val

    @DebugMode.setter
    def DebugMode(self, newDebugMode:bool) -> None:
        """Flag to turn debug mode on/off. When on, messages are reported to message viewer at the ReportFrequency."""
        with agmarshall.VARIANT_BOOL_arg(newDebugMode) as arg_newDebugMode:
            agcls.evaluate_hresult(self.__dict__['_SetDebugMode'](arg_newDebugMode.COM_val))


agcls.AgClassCatalog.add_catalog_entry('{E3A2A809-6F1E-41f2-809C-237D1D5929DC}', IAgAsDensityModelPluginSample)
agcls.AgTypeNameMap['IAgAsDensityModelPluginSample'] = IAgAsDensityModelPluginSample
__all__.append('IAgAsDensityModelPluginSample')


class IAgAsHpopPlugin(object):
    """
    HPOP plugin engine interface whose methods are called at certain events in the propagation process. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin."""
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def Free(self) -> None:
        """Triggered just before the plugin is freed from use to allow for any additional cleanup."""
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

    def PrePropagate(self, result:"IAgAsHpopPluginResult") -> bool:
        """Triggered just before propagation starts. Use the input interface to access force model settings. Set initial values for parameters and variables in this method."""
        raise STKPluginMethodNotImplementedError('PrePropagate was not implemented.')

    def PostPropagate(self, result:"IAgAsHpopPluginResult") -> bool:
        """Triggered just after the last propagation step has been taken. Use the input interface to access force model settings."""
        raise STKPluginMethodNotImplementedError('PostPropagate was not implemented.')

    def PreNextStep(self, result:"IAgAsHpopPluginResult") -> bool:
        """Triggered just before the next propagation step is attempted. Use the input interface to access force model settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('PreNextStep was not implemented.')

    def Evaluate(self, resultEval:"IAgAsHpopPluginResultEval") -> bool:
        """Triggered on every force model evaluation during the propagation of a step. Use the input interface to access force model settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('Evaluate was not implemented.')

    def PostEvaluate(self, resultPostEval:"IAgAsHpopPluginResultPostEval") -> bool:
        """Triggered on every force model evaluation during the propagation of a step, but after the individual force model components have been computed. The components can be obtained from the input interface. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('PostEvaluate was not implemented.')

    def Name(self) -> str:
        """Triggered after initialization to set the name of the plugin used in messages."""
        raise STKPluginMethodNotImplementedError('Name was not implemented.')

__all__.append('IAgAsHpopPlugin')

class IAgAsLightReflectionPlugin(object):
    """
    This interface is deprecated. Use IAgAsLightReflectionPlugin2 instead. Used to set reflectance vector (and optionally its partial derivs) used in computation of the srp force. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Register(self, result:"IAgAsLightReflectionResultRegister") -> None:
        """Triggered before computation starts, when configuration settings are sought. Used to used to register parameters that may be estimated."""
        raise STKPluginMethodNotImplementedError('Register was not implemented.')

    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin."""
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def Free(self) -> None:
        """Triggered just before the plugin is freed from use to allow for any additional cleanup."""
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

    def PreCompute(self, result:"IAgAsLightReflectionResult") -> bool:
        """Triggered just before the computation starts. Use the input interface to access settings."""
        raise STKPluginMethodNotImplementedError('PreCompute was not implemented.')

    def PostCompute(self, result:"IAgAsLightReflectionResult") -> bool:
        """Triggered after the last evaluation before the plugin calls Free(). Use the input interface to access settings."""
        raise STKPluginMethodNotImplementedError('PostCompute was not implemented.')

    def Evaluate(self, resultEval:"IAgAsLightReflectionResultEval") -> bool:
        """Triggered on every force model evaluation during the propagation of a step. Use the input interface to access force model settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('Evaluate was not implemented.')

__all__.append('IAgAsLightReflectionPlugin')

class IAgAsLightReflectionPlugin2(IAgAsLightReflectionPlugin):
    """
    Light Reflection plugin interface. Inherits from IAgAsLightReflectionPlugin. Used to set reflectance vector (and optionally its partial derivs) used in computation of the srp force. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def PreNextStep(self, result:"IAgAsLightReflectionResult") -> bool:
        """Triggered just before the next propagation step is attempted. Use the input interface to access settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('PreNextStep was not implemented.')

__all__.append('IAgAsLightReflectionPlugin2')

class IAgAsDragModelPlugin(object):
    """
    This interface is deprecated. Use IAgAsDragModelPlugin2 instead. Used to set reflectance vector (and optionally its partial derivs) used in computation of the drag/lift/side force. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Register(self, result:"IAgAsDragModelResultRegister") -> None:
        """Triggered before computation starts, when configuration settings are sought. Used to used to register parameters that may be estimated."""
        raise STKPluginMethodNotImplementedError('Register was not implemented.')

    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin."""
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def Free(self) -> None:
        """Triggered just before the plugin is freed from use to allow for any additional cleanup."""
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

    def PreCompute(self, result:"IAgAsDragModelResult") -> bool:
        """Triggered just before the computation starts. Use the input interface to access settings."""
        raise STKPluginMethodNotImplementedError('PreCompute was not implemented.')

    def PostCompute(self, result:"IAgAsDragModelResult") -> bool:
        """Triggered after the last evaluation before the plugin calls Free(). Use the input interface to access settings."""
        raise STKPluginMethodNotImplementedError('PostCompute was not implemented.')

    def Evaluate(self, resultEval:"IAgAsDragModelResultEval") -> bool:
        """Triggered on every force model evaluation during the propagation of a step. Use the input interface to access force model settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('Evaluate was not implemented.')

__all__.append('IAgAsDragModelPlugin')

class IAgAsDragModelPlugin2(IAgAsDragModelPlugin):
    """
    Drag model plugin interface. Inherits from IAgAsDragModelPlugin. Used to set reflectance vector (and optionally its partial derivs) used in computation of the drag/lift/side force. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def PreNextStep(self, result:"IAgAsDragModelResult") -> bool:
        """Triggered just before the next propagation step is attempted. Use the input interface to access settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('PreNextStep was not implemented.')

__all__.append('IAgAsDragModelPlugin2')

class IAgAsEOMFuncPlugin(object):
    """
    HPOP plugin engine interface for user-defined equations of motion.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin."""
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def Free(self) -> None:
        """Triggered just before the plugin is freed from use to allow for any additional cleanup."""
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

    def Register(self, pRegisterHandler:"IAgAsEOMFuncPluginRegisterHandler") -> bool:
        """Method to register the plugin's inputs, outputs, and events"""
        raise STKPluginMethodNotImplementedError('Register was not implemented.')

    def SetIndices(self, pSetIndicesHandler:"IAgAsEOMFuncPluginSetIndicesHandler") -> bool:
        """Gives the plugin the indices into the state vector for its inputs/outputs"""
        raise STKPluginMethodNotImplementedError('SetIndices was not implemented.')

    def Calc(self, eventType:"AgEAsEOMFuncPluginEventTypes", pStateVector:"IAgAsEOMFuncPluginStateVector") -> bool:
        """Calculate method for plugin"""
        raise STKPluginMethodNotImplementedError('Calc was not implemented.')

    def Name(self) -> str:
        """Triggered after initialization to set the name of the plugin used in messages."""
        raise STKPluginMethodNotImplementedError('Name was not implemented.')

__all__.append('IAgAsEOMFuncPlugin')

class IAgAsDensityModelPlugin(object):
    """
    Density model plugin interface. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Register(self, result:"IAgAsDensityModelResultRegister") -> None:
        """Triggered before computation starts, when configuration settings are sought. Used to used to register parameters that may be estimated."""
        raise STKPluginMethodNotImplementedError('Register was not implemented.')

    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin."""
        raise STKPluginMethodNotImplementedError('Init was not implemented.')

    def Free(self) -> None:
        """Triggered just before the plugin is freed from use to allow for any additional cleanup."""
        raise STKPluginMethodNotImplementedError('Free was not implemented.')

    def Evaluate(self, resultEval:"IAgAsDensityModelResultEval") -> bool:
        """Triggered on every force model evaluation during the propagation of a step. Use the input interface to access force model settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('Evaluate was not implemented.')

    def CentralBody(self) -> str:
        """Triggered on every density plugin before evaluation to determine the central body for which the atmosphere model applies."""
        raise STKPluginMethodNotImplementedError('CentralBody was not implemented.')

    def ComputesTemperature(self) -> bool:
        """Triggered on every density plugin before evaluation to check if the plugin computes temperature."""
        raise STKPluginMethodNotImplementedError('ComputesTemperature was not implemented.')

    def ComputesPressure(self) -> bool:
        """Triggered on every density plugin before evaluation to check if the plugin computes pressure."""
        raise STKPluginMethodNotImplementedError('ComputesPressure was not implemented.')

    def UsesAugmentedSpaceWeather(self) -> bool:
        """Triggered on every density plugin before evaluation to check if the plugin uses augmented space weather data such as M10, S10, Y10 and DstDTc."""
        raise STKPluginMethodNotImplementedError('UsesAugmentedSpaceWeather was not implemented.')

    def GetLowestValidAltitude(self) -> float:
        """The lowest valid altitude for input to atmospheric density model in meters."""
        raise STKPluginMethodNotImplementedError('GetLowestValidAltitude was not implemented.')

__all__.append('IAgAsDensityModelPlugin')

class IAgAsDensityModelPluginExtended(IAgAsDensityModelPlugin):
    """
    Extends the IAgAsDensityModelPlugin interface for use with numerical integration events.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def PreCompute(self, result:"IAgAsDensityModelResult") -> bool:
        """Triggered just before numerical integration starts. Use the input interface to access settings."""
        raise STKPluginMethodNotImplementedError('PreCompute was not implemented.')

    def PreNextStep(self, result:"IAgAsDensityModelResult") -> bool:
        """Triggered just before the next propagation step is attempted during numerical integration. Use the input interface to access settings. Returning false will turn this callback off."""
        raise STKPluginMethodNotImplementedError('PreNextStep was not implemented.')

    def PostCompute(self, result:"IAgAsDensityModelResult") -> bool:
        """Triggered after the last evaluation of numerical integration before the plugin calls Free(). Use the input interface to access settings."""
        raise STKPluginMethodNotImplementedError('PostCompute was not implemented.')

__all__.append('IAgAsDensityModelPluginExtended')



class AgAsHpopPluginResult(IAgAsHpopPluginResult):
    """HPOP plugin class used to get/set force model settings"""
    def __init__(self, sourceObject=None):
        IAgAsHpopPluginResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsHpopPluginResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsHpopPluginResult._get_property(self, attrname) is not None: found_prop = IAgAsHpopPluginResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsHpopPluginResult.')
        
agcls.AgClassCatalog.add_catalog_entry('{DD7D4E1B-EBB0-4553-9EB9-0210A3E274E6}', AgAsHpopPluginResult)
__all__.append('AgAsHpopPluginResult')


class AgAsHpopPluginResultEval(IAgAsHpopPluginResultEval):
    """HPOP plugin class used to get/set force model settings during the propagation of a step"""
    def __init__(self, sourceObject=None):
        IAgAsHpopPluginResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsHpopPluginResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsHpopPluginResultEval._get_property(self, attrname) is not None: found_prop = IAgAsHpopPluginResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsHpopPluginResultEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{847426ED-CC7C-4FE6-BE07-1FAD4B226E65}', AgAsHpopPluginResultEval)
__all__.append('AgAsHpopPluginResultEval')


class AgAsHpopPluginResultPostEval(IAgAsHpopPluginResultPostEval):
    """HPOP plugin class used to get/set force model settings during the propagation of a step"""
    def __init__(self, sourceObject=None):
        IAgAsHpopPluginResultPostEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsHpopPluginResultPostEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsHpopPluginResultPostEval._get_property(self, attrname) is not None: found_prop = IAgAsHpopPluginResultPostEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsHpopPluginResultPostEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{C52ADE9F-B554-436B-8EEC-E5D45C298C71}', AgAsHpopPluginResultPostEval)
__all__.append('AgAsHpopPluginResultPostEval')


class AgAsHpopPluginSampleEngine(IAgAsHpopPluginSampleEngine, IAgAsHpopPlugin, IAgUtPluginConfig):
    """Sample HPOP Plugin Class"""
    def __init__(self, sourceObject=None):
        IAgAsHpopPluginSampleEngine.__init__(self, sourceObject)
        IAgAsHpopPlugin.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsHpopPluginSampleEngine._private_init(self, pUnk)
        IAgAsHpopPlugin._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsHpopPluginSampleEngine._get_property(self, attrname) is not None: found_prop = IAgAsHpopPluginSampleEngine._get_property(self, attrname)
        if IAgAsHpopPlugin._get_property(self, attrname) is not None: found_prop = IAgAsHpopPlugin._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsHpopPluginSampleEngine.')
        
agcls.AgClassCatalog.add_catalog_entry('{7A5E09B3-E7AD-4402-90B8-105C8F9AE80E}', AgAsHpopPluginSampleEngine)
__all__.append('AgAsHpopPluginSampleEngine')


class AgAsLightReflectionResultRegister(IAgAsLightReflectionResultRegister):
    """LightReflection plugin interface used to register parameters that may be estimated."""
    def __init__(self, sourceObject=None):
        IAgAsLightReflectionResultRegister.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsLightReflectionResultRegister._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsLightReflectionResultRegister._get_property(self, attrname) is not None: found_prop = IAgAsLightReflectionResultRegister._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsLightReflectionResultRegister.')
        
agcls.AgClassCatalog.add_catalog_entry('{AC010B1C-A968-4788-9229-18EB4A96C6EC}', AgAsLightReflectionResultRegister)
__all__.append('AgAsLightReflectionResultRegister')


class AgAsLightReflectionResult(IAgAsLightReflectionResult):
    """Light reflection plugin class used to get/set reflection settings"""
    def __init__(self, sourceObject=None):
        IAgAsLightReflectionResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsLightReflectionResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsLightReflectionResult._get_property(self, attrname) is not None: found_prop = IAgAsLightReflectionResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsLightReflectionResult.')
        
agcls.AgClassCatalog.add_catalog_entry('{0D9E5F17-EFB8-4870-A53A-6B10FCDBC5ED}', AgAsLightReflectionResult)
__all__.append('AgAsLightReflectionResult')


class AgAsLightReflectionResultEval(IAgAsLightReflectionResultEval):
    """Light reflection plugin class used to get/set reflection settings during Evaluation call"""
    def __init__(self, sourceObject=None):
        IAgAsLightReflectionResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsLightReflectionResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsLightReflectionResultEval._get_property(self, attrname) is not None: found_prop = IAgAsLightReflectionResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsLightReflectionResultEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{123A3ED7-50DA-4421-A999-D44AE2E81048}', AgAsLightReflectionResultEval)
__all__.append('AgAsLightReflectionResultEval')


class AgAsLightReflectionPluginSample(IAgAsLightReflectionPluginSample, IAgAsLightReflectionPlugin2, IAgUtPluginConfig):
    """Sample Light Reflection Plugin Class"""
    def __init__(self, sourceObject=None):
        IAgAsLightReflectionPluginSample.__init__(self, sourceObject)
        IAgAsLightReflectionPlugin2.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsLightReflectionPluginSample._private_init(self, pUnk)
        IAgAsLightReflectionPlugin2._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsLightReflectionPluginSample._get_property(self, attrname) is not None: found_prop = IAgAsLightReflectionPluginSample._get_property(self, attrname)
        if IAgAsLightReflectionPlugin2._get_property(self, attrname) is not None: found_prop = IAgAsLightReflectionPlugin2._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsLightReflectionPluginSample.')
        
agcls.AgClassCatalog.add_catalog_entry('{A58423AD-5B51-4F16-9034-E0FE202EBEC5}', AgAsLightReflectionPluginSample)
__all__.append('AgAsLightReflectionPluginSample')


class AgAsDragModelResultRegister(IAgAsDragModelResultRegister):
    """DragModel plugin interface used to register parameters that may be estimated."""
    def __init__(self, sourceObject=None):
        IAgAsDragModelResultRegister.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDragModelResultRegister._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDragModelResultRegister._get_property(self, attrname) is not None: found_prop = IAgAsDragModelResultRegister._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDragModelResultRegister.')
        
agcls.AgClassCatalog.add_catalog_entry('{4F8F235E-DBD6-49AD-921E-27874060F8FC}', AgAsDragModelResultRegister)
__all__.append('AgAsDragModelResultRegister')


class AgAsDragModelResult(IAgAsDragModelResult):
    """DragModel plugin class used to get/set particle reflection settings"""
    def __init__(self, sourceObject=None):
        IAgAsDragModelResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDragModelResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDragModelResult._get_property(self, attrname) is not None: found_prop = IAgAsDragModelResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDragModelResult.')
        
agcls.AgClassCatalog.add_catalog_entry('{9A244900-B650-49DB-9775-00898AE5B690}', AgAsDragModelResult)
__all__.append('AgAsDragModelResult')


class AgAsDragModelResultEval(IAgAsDragModelResultEval):
    """DragModel plugin class used to get/set particle reflection settings during Evaluation call"""
    def __init__(self, sourceObject=None):
        IAgAsDragModelResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDragModelResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDragModelResultEval._get_property(self, attrname) is not None: found_prop = IAgAsDragModelResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDragModelResultEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{2BB3A39D-15E5-4FA9-A66F-941F0321FD7B}', AgAsDragModelResultEval)
__all__.append('AgAsDragModelResultEval')


class AgAsDragModelPluginSample(IAgAsDragModelPluginSample, IAgAsDragModelPlugin2, IAgUtPluginConfig):
    """Sample DragModel Plugin Class"""
    def __init__(self, sourceObject=None):
        IAgAsDragModelPluginSample.__init__(self, sourceObject)
        IAgAsDragModelPlugin2.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDragModelPluginSample._private_init(self, pUnk)
        IAgAsDragModelPlugin2._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDragModelPluginSample._get_property(self, attrname) is not None: found_prop = IAgAsDragModelPluginSample._get_property(self, attrname)
        if IAgAsDragModelPlugin2._get_property(self, attrname) is not None: found_prop = IAgAsDragModelPlugin2._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDragModelPluginSample.')
        
agcls.AgClassCatalog.add_catalog_entry('{53080FE5-49EB-4576-8B4B-28832B28B7FA}', AgAsDragModelPluginSample)
__all__.append('AgAsDragModelPluginSample')


class AgAsDensityModelResultRegister(IAgAsDensityModelResultRegister):
    """DensityModel plugin interface used to register parameters that may be estimated."""
    def __init__(self, sourceObject=None):
        IAgAsDensityModelResultRegister.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDensityModelResultRegister._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDensityModelResultRegister._get_property(self, attrname) is not None: found_prop = IAgAsDensityModelResultRegister._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDensityModelResultRegister.')
        
agcls.AgClassCatalog.add_catalog_entry('{99E7AD88-8F9F-4139-861C-685F8B5CA669}', AgAsDensityModelResultRegister)
__all__.append('AgAsDensityModelResultRegister')


class AgAsDensityModelResult(IAgAsDensityModelResult):
    """DensityModel plugin class used to get settings during numerical integration events."""
    def __init__(self, sourceObject=None):
        IAgAsDensityModelResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDensityModelResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDensityModelResult._get_property(self, attrname) is not None: found_prop = IAgAsDensityModelResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDensityModelResult.')
        
agcls.AgClassCatalog.add_catalog_entry('{6CBB98CF-CA56-4B03-AA30-713720792ED9}', AgAsDensityModelResult)
__all__.append('AgAsDensityModelResult')


class AgAsDensityModelResultEval(IAgAsDensityModelResultEval):
    """DensityModel plugin class used to get/set density settings during Evaluation call"""
    def __init__(self, sourceObject=None):
        IAgAsDensityModelResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDensityModelResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDensityModelResultEval._get_property(self, attrname) is not None: found_prop = IAgAsDensityModelResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDensityModelResultEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{678C8419-F550-4D84-91AA-7A3F86E6C1C7}', AgAsDensityModelResultEval)
__all__.append('AgAsDensityModelResultEval')


class AgAsDensityModelPluginAtmFluxLagsConfig(IAgAsDensityModelPluginAtmFluxLagsConfig):
    """DensityModel plugin class used to get/set AtmFluxLag values"""
    def __init__(self, sourceObject=None):
        IAgAsDensityModelPluginAtmFluxLagsConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDensityModelPluginAtmFluxLagsConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDensityModelPluginAtmFluxLagsConfig._get_property(self, attrname) is not None: found_prop = IAgAsDensityModelPluginAtmFluxLagsConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDensityModelPluginAtmFluxLagsConfig.')
        
agcls.AgClassCatalog.add_catalog_entry('{07663D49-80FD-43BB-A254-B9AE1E7F0D93}', AgAsDensityModelPluginAtmFluxLagsConfig)
__all__.append('AgAsDensityModelPluginAtmFluxLagsConfig')


class AgAsDensityModelPluginSample(IAgAsDensityModelPluginExtended, IAgAsDensityModelPluginSample, IAgAsDensityModelPlugin, IAgUtPluginConfig):
    """Sample DensityModel Plugin Class"""
    def __init__(self, sourceObject=None):
        IAgAsDensityModelPluginExtended.__init__(self, sourceObject)
        IAgAsDensityModelPluginSample.__init__(self, sourceObject)
        IAgAsDensityModelPlugin.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsDensityModelPluginExtended._private_init(self, pUnk)
        IAgAsDensityModelPluginSample._private_init(self, pUnk)
        IAgAsDensityModelPlugin._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsDensityModelPluginExtended._get_property(self, attrname) is not None: found_prop = IAgAsDensityModelPluginExtended._get_property(self, attrname)
        if IAgAsDensityModelPluginSample._get_property(self, attrname) is not None: found_prop = IAgAsDensityModelPluginSample._get_property(self, attrname)
        if IAgAsDensityModelPlugin._get_property(self, attrname) is not None: found_prop = IAgAsDensityModelPlugin._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsDensityModelPluginSample.')
        
agcls.AgClassCatalog.add_catalog_entry('{EE200959-9913-4E04-8726-4ACA3B2EC945}', AgAsDensityModelPluginSample)
__all__.append('AgAsDensityModelPluginSample')


class AgEOMFuncHPOPPluginResult(IAgAsHpopPluginResult):
    """Plugin class used to get/set propagator settings with EOM Manager"""
    def __init__(self, sourceObject=None):
        IAgAsHpopPluginResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsHpopPluginResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsHpopPluginResult._get_property(self, attrname) is not None: found_prop = IAgAsHpopPluginResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgEOMFuncHPOPPluginResult.')
        
agcls.AgClassCatalog.add_catalog_entry('{8E893111-BEF2-4B94-A7DA-312562D553BA}', AgEOMFuncHPOPPluginResult)
__all__.append('AgEOMFuncHPOPPluginResult')


class AgEOMFuncHPOPPluginResultEval(IAgAsHpopPluginResultEval):
    """APlugin class used to get/set propagator settings during the propagation of a step with EOM Manager"""
    def __init__(self, sourceObject=None):
        IAgAsHpopPluginResultEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsHpopPluginResultEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsHpopPluginResultEval._get_property(self, attrname) is not None: found_prop = IAgAsHpopPluginResultEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgEOMFuncHPOPPluginResultEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{32C32D0A-872C-4F90-88D1-DB5C725FDA6F}', AgEOMFuncHPOPPluginResultEval)
__all__.append('AgEOMFuncHPOPPluginResultEval')


class AgEOMFuncHPOPPluginResultPostEval(IAgAsHpopPluginResultPostEval):
    """Plugin class used to get/set propagator settings during the propagation of a step with EOM Manager"""
    def __init__(self, sourceObject=None):
        IAgAsHpopPluginResultPostEval.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsHpopPluginResultPostEval._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsHpopPluginResultPostEval._get_property(self, attrname) is not None: found_prop = IAgAsHpopPluginResultPostEval._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgEOMFuncHPOPPluginResultPostEval.')
        
agcls.AgClassCatalog.add_catalog_entry('{F9E0A5E9-C4FF-4BF0-A096-294AC0718FAD}', AgEOMFuncHPOPPluginResultPostEval)
__all__.append('AgEOMFuncHPOPPluginResultPostEval')


class AgAsEOMFuncPluginRegisterHandler(IAgAsEOMFuncPluginRegisterHandler):
    """Plugin class used to register plugin's inputs and outputs"""
    def __init__(self, sourceObject=None):
        IAgAsEOMFuncPluginRegisterHandler.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsEOMFuncPluginRegisterHandler._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEOMFuncPluginRegisterHandler._get_property(self, attrname) is not None: found_prop = IAgAsEOMFuncPluginRegisterHandler._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsEOMFuncPluginRegisterHandler.')
        
agcls.AgClassCatalog.add_catalog_entry('{8F104CA8-66A9-4F44-957C-91CDCF76E737}', AgAsEOMFuncPluginRegisterHandler)
__all__.append('AgAsEOMFuncPluginRegisterHandler')


class AgAsEOMFuncPluginSetIndicesHandler(IAgAsEOMFuncPluginSetIndicesHandler):
    """Plugin class used to set plugin's indices"""
    def __init__(self, sourceObject=None):
        IAgAsEOMFuncPluginSetIndicesHandler.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsEOMFuncPluginSetIndicesHandler._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEOMFuncPluginSetIndicesHandler._get_property(self, attrname) is not None: found_prop = IAgAsEOMFuncPluginSetIndicesHandler._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsEOMFuncPluginSetIndicesHandler.')
        
agcls.AgClassCatalog.add_catalog_entry('{580ED44B-086D-4DC7-9F94-A2B59942562C}', AgAsEOMFuncPluginSetIndicesHandler)
__all__.append('AgAsEOMFuncPluginSetIndicesHandler')


class AgAsEOMFuncPluginStateVector(IAgAsEOMFuncPluginStateVector):
    """Plugin class used to get and set state values during propagation in plugin's calc method"""
    def __init__(self, sourceObject=None):
        IAgAsEOMFuncPluginStateVector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgAsEOMFuncPluginStateVector._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEOMFuncPluginStateVector._get_property(self, attrname) is not None: found_prop = IAgAsEOMFuncPluginStateVector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgAsEOMFuncPluginStateVector.')
        
agcls.AgClassCatalog.add_catalog_entry('{3B502170-4076-4223-85CE-94A1FC293707}', AgAsEOMFuncPluginStateVector)
__all__.append('AgAsEOMFuncPluginStateVector')



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
