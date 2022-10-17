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

from .internal  import comutil          as agcom
from .internal  import coclassutil      as agcls
from .internal  import marshall         as agmarshall
from .internal  import dataanalysisutil as agdata
from .utilities import colors           as agcolor
from .internal.comutil     import IUnknown, IDispatch, IPictureDisp, IAGFUNCTYPE, IEnumVARIANT
from .internal.eventutil   import *
from .utilities.exceptions import *



def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgEPositionType(IntEnum):
    """Facility/place/target position types."""
    # Cartesian: position specified in terms of the X, Y and Z components of the object's position vector, where the Z-axis points to the North pole, and the X-axis crosses 0 degrees latitude/0 degrees longitude.
    eCartesian = 0x0,
    # Cylindrical: position specified in terms of radius (polar), longitude (measured in degrees from -360.0 degrees to +360.0 degrees), and the Z component of the object's position vector.
    eCylindrical = 0x1,
    # Geocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude.
    eGeocentric = 0x2,
    # Geodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude.
    eGeodetic = 0x3,
    # Spherical: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and radius (distance of the object from the center of the Earth).
    eSpherical = 0x4,
    # Planetocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude.
    ePlanetocentric = 0x5,
    # Planetodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude.
    ePlanetodetic = 0x6

agcls.AgTypeNameMap["AgEPositionType"] = AgEPositionType
__all__.append("AgEPositionType")

class AgEEulerDirectionSequence(IntEnum):
    """Euler direction sequences."""
    # 12 sequence.
    e12 = 0,
    # 21 sequence.
    e21 = 1,
    # 31 sequence.
    e31 = 2,
    # 32 sequence.
    e32 = 3

agcls.AgTypeNameMap["AgEEulerDirectionSequence"] = AgEEulerDirectionSequence
__all__.append("AgEEulerDirectionSequence")

class AgEDirectionType(IntEnum):
    """Direction options for aligned and constrained vectors."""
    # Euler B and C angles.
    eDirEuler = 0,
    # Pitch and Roll angles.
    eDirPR = 1,
    # Spherical elements: Right Ascension and Declination.
    eDirRADec = 2,
    # Cartesian elements.
    eDirXYZ = 3

agcls.AgTypeNameMap["AgEDirectionType"] = AgEDirectionType
__all__.append("AgEDirectionType")

class AgEPRSequence(IntEnum):
    """Pitch-Roll (PR) direction sequences."""
    # PR sequence.
    ePR = 0

agcls.AgTypeNameMap["AgEPRSequence"] = AgEPRSequence
__all__.append("AgEPRSequence")

class AgEOrientationType(IntEnum):
    """Orientation methods."""
    # AzEl (azimuth-elevation) method.
    eAzEl = 0,
    # Euler angles method.
    eEulerAngles = 1,
    # Quaternion method.
    eQuaternion = 2,
    # YPR (yaw-pitch-roll) method.
    eYPRAngles = 3

agcls.AgTypeNameMap["AgEOrientationType"] = AgEOrientationType
__all__.append("AgEOrientationType")

class AgEAzElAboutBoresight(IntEnum):
    """About Boresight options for AzEl orientation method."""
    # Hold: rotation about the Y axis followed by rotation about the new X-axis.
    eAzElAboutBoresightHold = 0,
    # Rotate: rotation about the sensor's or antenna's Z axis by the azimuth angle, followed by rotation about the new Y axis by 90 degrees minus the elevation angle.
    eAzElAboutBoresightRotate = 1

agcls.AgTypeNameMap["AgEAzElAboutBoresight"] = AgEAzElAboutBoresight
__all__.append("AgEAzElAboutBoresight")

class AgEEulerOrientationSequence(IntEnum):
    """Euler rotation sequence options:"""
    # 121 rotation.
    e121 = 0,
    # 123 rotation.
    e123 = 1,
    # 131 rotation.
    e131 = 2,
    # 132 rotation.
    e132 = 3,
    # 212 rotation.
    e212 = 4,
    # 213 rotation.
    e213 = 5,
    # 231 rotation.
    e231 = 6,
    # 232 rotation.
    e232 = 7,
    # 312 rotation.
    e312 = 8,
    # 313 rotation.
    e313 = 9,
    # 321 rotation.
    e321 = 10,
    # 323 rotation.
    e323 = 11

agcls.AgTypeNameMap["AgEEulerOrientationSequence"] = AgEEulerOrientationSequence
__all__.append("AgEEulerOrientationSequence")

class AgEYPRAnglesSequence(IntEnum):
    """Yaw-Pitch-Roll (YPR) sequences."""
    # PRY sequence.
    ePRY = 0,
    # PYR sequence.
    ePYR = 1,
    # RPY sequence.
    eRPY = 2,
    # RYP sequence.
    eRYP = 3,
    # YPR sequence.
    eYPR = 4,
    # YRP sequence.
    eYRP = 5

agcls.AgTypeNameMap["AgEYPRAnglesSequence"] = AgEYPRAnglesSequence
__all__.append("AgEYPRAnglesSequence")

class AgEOrbitStateType(IntEnum):
    """Coordinate types used in specifying orbit state."""
    # Cartesian coordinate type.
    eOrbitStateCartesian = 0,
    # Classical (Keplerian) coordinate type.
    eOrbitStateClassical = 1,
    # Equinoctial coordinate type.
    eOrbitStateEquinoctial = 2,
    # Delaunay variables coordinate type.
    eOrbitStateDelaunay = 3,
    # Spherical coordinate type.
    eOrbitStateSpherical = 4,
    # Mixed spherical coordinate type.
    eOrbitStateMixedSpherical = 5,
    # Geodetic coordinate type.
    eOrbitStateGeodetic = 6

agcls.AgTypeNameMap["AgEOrbitStateType"] = AgEOrbitStateType
__all__.append("AgEOrbitStateType")

class AgECoordinateSystem(IntEnum):
    """Earth-centered coordinate systems for defining certain propagators."""
    # Represents coordinate system not supported by the Object Model
    eCoordinateSystemUnknown = -1,
    # Alignment at Epoch: an inertial system coincident with ECF at the Coord Epoch. Often used to specify launch trajectories.
    eCoordinateSystemAlignmentAtEpoch = 0,
    # B1950: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the beginning of the Besselian year 1950 and corresponds to 31 December 1949 22:09:07.2 or JD 2433282.423.
    eCoordinateSystemB1950 = 1,
    # Fixed: X is fixed at 0 deg longitude, Y is fixed at 90 deg longitude, and Z is directed toward the north pole.
    eCoordinateSystemFixed = 2,
    # J2000: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth on 1 Jan 2000 at 12:00:00.00 TDB, which corresponds to JD 2451545.0 TDB.
    eCoordinateSystemJ2000 = 3,
    # Mean of Date: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Orbit Epoch.
    eCoordinateSystemMeanOfDate = 4,
    # Mean of Epoch: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Coord Epoch.
    eCoordinateSystemMeanOfEpoch = 5,
    # TEME of Date: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch.
    eCoordinateSystemTEMEOfDate = 6,
    # TEME of Epoch: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch.
    eCoordinateSystemTEMEOfEpoch = 7,
    # True of Date: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch.
    eCoordinateSystemTrueOfDate = 8,
    # True of Epoch: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch.
    eCoordinateSystemTrueOfEpoch = 9,
    # True of Ref Date: A special case of True of Epoch. Instead of the Coord Epoch, this system uses a Reference Date defined in the Integration Control page of the scenario's PODS properties.
    eCoordinateSystemTrueOfRefDate = 10,
    # ICRF: International Celestial Reference Frame.
    eCoordinateSystemICRF = 11,
    # Mean Earth
    eCoordinateSystemMeanEarth = 13,
    # uses an analytic formula not modeling lunar libration
    eCoordinateSystemFixedNoLibration = 14,
    # Fixed_IAU2003
    eCoordinateSystemFixedIAU2003 = 15,
    # PrincipalAxes_421
    eCoordinateSystemPrincipalAxes421 = 16,
    # PrincipalAxes_403
    eCoordinateSystemPrincipalAxes403 = 17,
    # Inertial
    eCoordinateSystemInertial = 18,
    # The mean ecliptic system evaluated at the J2000 epoch. The mean ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the mean obliquity defined using FK5 IAU76 theory.
    eCoordinateSystemJ2000Ecliptic = 19,
    # The true ecliptic system, evaluated at each given time. The true ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the true obliquity defined using FK5 IAU76 theory.
    eCoordinateSystemTrueEclipticOfDate = 21,
    # PrincipalAxes_430
    eCoordinateSystemPrincipalAxes430 = 22,
    # TrueOfDateRotating: Like the Fixed system, but ignores pole wander. The XY plane is the same as the XY plane of the TrueOfDate system, and the system rotates about the TrueOfDate Z-axis.
    eCoordinateSystemTrueOfDateRotating = 23,
    # EclipticJ2000ICRF: An ecliptic system that is a fixed offset of the ICRF system, found by rotating the ICRF system about its X-axis by the mean obliquity at the J2000 epoch (i.e., 84381.448 arcSecs). The ecliptic plane is the XY-plane of this system.
    eCoordinateSystemEclipticJ2000ICRF = 24

agcls.AgTypeNameMap["AgECoordinateSystem"] = AgECoordinateSystem
__all__.append("AgECoordinateSystem")

class AgELogMsgType(IntEnum):
    """Log message types."""
    # Debugging message.
    eLogMsgDebug = 0,
    # Informational message.
    eLogMsgInfo = 1,
    # Informational message.
    eLogMsgForceInfo = 2,
    # Warning message.
    eLogMsgWarning = 3,
    # Alarm message.
    eLogMsgAlarm = 4

agcls.AgTypeNameMap["AgELogMsgType"] = AgELogMsgType
__all__.append("AgELogMsgType")

class AgELogMsgDispID(IntEnum):
    """Log message destination options."""
    # STK displays the message in all the log destination.
    eLogMsgDispAll = -1,
    # STK displays the message in the default log destination.
    eLogMsgDispDefault = 0,
    # STK displays the message in the message window.
    eLogMsgDispMsgWin = 1,
    # STK displays the message in the status bar.
    eLogMsgDispStatusBar = 2

agcls.AgTypeNameMap["AgELogMsgDispID"] = AgELogMsgDispID
__all__.append("AgELogMsgDispID")

class AgELineStyle(IntEnum):
    """Line Style"""
    # Specifies a solid line.
    eSolid = 0,
    # Specifies a dashed line.
    eDashed = 1,
    # Specifies a dotted line.
    eDotted = 2,
    # Dot-dashed line.
    eDotDashed = 3,
    # Specifies a long dashed line.
    eLongDashed = 4,
    # Specifies an alternating dash-dot-dot line.
    eDashDotDotted = 5,
    # Specifies a user configurable medium dashed line.
    eMDash = 6,
    # Specifies a user configurable long dashed line.
    eLDash = 7,
    # Specifies a user configurable small dash-dotted line.
    eSDashDot = 8,
    # Specifies a user configurable medium dash-dotted line.
    eMDashDot = 9,
    # Specifies a user configurable long dash-dotted line.
    eLDashDot = 10,
    # Specifies a user configurable medium followed by small dashed line.
    eMSDash = 11,
    # Specifies a user configurable long followed by small dashed line.
    eLSDash = 12,
    # Specifies a user configurable long followed by medium dashed line.
    eLMDash = 13,
    # Specifies a user configurable medium followed by small dashed line.
    eLMSDash = 14,
    # Specifies a dotted line.
    eDot = 15,
    # Specifies a long dashed line.
    eLongDash = 16,
    # Specifies an alternating dash-dot line.
    eSDash = 17

agcls.AgTypeNameMap["AgELineStyle"] = AgELineStyle
__all__.append("AgELineStyle")

class AgEExecMultiCmdResultAction(IntFlag):
    """Enumeration defines a set of actions when an error occurs while executing a command batch."""
    # Continue executing the remaining commands in the command batch.
    eContinueOnError = 0,
    # Terminate the execution of the command batch but do not throw an exception.
    eStopOnError = 1,
    # Terminate the execution of the command batch and throw an exception.
    eExceptionOnError = 2,
    # Ignore results returned by individual commands. The option must be used in combination with other flags.
    eIgnoreExecCmdResult = 0x8000

agcls.AgTypeNameMap["AgEExecMultiCmdResultAction"] = AgEExecMultiCmdResultAction
__all__.append("AgEExecMultiCmdResultAction")

class AgEFillStyle(IntEnum):
    """Fill Style"""
    # Specifies a solid fill style.
    eFillStyleSolid = 0,
    # Specifies a horizontally striped fill style.
    eFillStyleHorizontalStripe = 1,
    # Specifies a diagonally striped fill style.
    eFillStyleDiagonalStripe1 = 2,
    # Specifies a diagonally striped fill style.
    eFillStyleDiagonalStripe2 = 3,
    # Specifies a hatched fill style.
    eFillStyleHatch = 4,
    # Specifies a diagonally hatched fill style.
    eFillStyleDiagonalHatch = 5,
    # Specifies a special fill style where every other pixel is drawn.
    eFillStyleScreen = 6,
    # Specifies a vertically striped fill style.
    eFillStyleVerticalStripe = 7

agcls.AgTypeNameMap["AgEFillStyle"] = AgEFillStyle
__all__.append("AgEFillStyle")

class AgEPropertyInfoValueType(IntEnum):
    """The enumeration used to determine what type of property is being used."""
    # Property is of type int.
    ePropertyInfoValueTypeInt = 0,
    # Property is of type real.
    ePropertyInfoValueTypeReal = 1,
    # Property is of type IAgQuantity.
    ePropertyInfoValueTypeQuantity = 2,
    # Property is of type IAgDate.
    ePropertyInfoValueTypeDate = 3,
    # Property is of type string.
    ePropertyInfoValueTypeString = 4,
    # Property is of type bool.
    ePropertyInfoValueTypeBool = 5,
    # Property is an interface.
    ePropertyInfoValueTypeInterface = 6

agcls.AgTypeNameMap["AgEPropertyInfoValueType"] = AgEPropertyInfoValueType
__all__.append("AgEPropertyInfoValueType")


class IAgLocationData(object):
    """Base interface IAgLocationData. IAgPosition derives from this interface."""
    _uuid = "{C1E99EDA-C666-4971-AFD0-2259CB7E8452}"
    _num_methods = 0
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgLocationData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgLocationData from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgLocationData = agcom.GUID(IAgLocationData._uuid)
        vtable_offset_local = IAgLocationData._vtable_offset - 1
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgLocationData.__dict__ and type(IAgLocationData.__dict__[attrname]) == property:
            return IAgLocationData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgLocationData.")
    

agcls.AgClassCatalog.add_catalog_entry("{C1E99EDA-C666-4971-AFD0-2259CB7E8452}", IAgLocationData)
agcls.AgTypeNameMap["IAgLocationData"] = IAgLocationData
__all__.append("IAgLocationData")

class IAgPosition(object):
    """IAgPosition provides access to the position of the object"""
    _uuid = "{F25960CE-1D73-4BA0-A429-541DD6D808DE}"
    _num_methods = 21
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ConvertTo"] = _raise_uninitialized_error
        self.__dict__["_GetPosType"] = _raise_uninitialized_error
        self.__dict__["_Assign"] = _raise_uninitialized_error
        self.__dict__["_AssignGeocentric"] = _raise_uninitialized_error
        self.__dict__["_AssignGeodetic"] = _raise_uninitialized_error
        self.__dict__["_AssignSpherical"] = _raise_uninitialized_error
        self.__dict__["_AssignCylindrical"] = _raise_uninitialized_error
        self.__dict__["_AssignCartesian"] = _raise_uninitialized_error
        self.__dict__["_AssignPlanetocentric"] = _raise_uninitialized_error
        self.__dict__["_AssignPlanetodetic"] = _raise_uninitialized_error
        self.__dict__["_QueryPlanetocentric"] = _raise_uninitialized_error
        self.__dict__["_QueryPlanetodetic"] = _raise_uninitialized_error
        self.__dict__["_QuerySpherical"] = _raise_uninitialized_error
        self.__dict__["_QueryCylindrical"] = _raise_uninitialized_error
        self.__dict__["_QueryCartesian"] = _raise_uninitialized_error
        self.__dict__["_GetCentralBodyName"] = _raise_uninitialized_error
        self.__dict__["_QueryPlanetocentricArray"] = _raise_uninitialized_error
        self.__dict__["_QueryPlanetodeticArray"] = _raise_uninitialized_error
        self.__dict__["_QuerySphericalArray"] = _raise_uninitialized_error
        self.__dict__["_QueryCylindricalArray"] = _raise_uninitialized_error
        self.__dict__["_QueryCartesianArray"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPosition._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPosition from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgPosition = agcom.GUID(IAgPosition._uuid)
        vtable_offset_local = IAgPosition._vtable_offset - 1
        self.__dict__["_ConvertTo"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_GetPosType"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Assign"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_AssignGeocentric"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+4, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_AssignGeodetic"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+5, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_AssignSpherical"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+6, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_AssignCylindrical"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+7, agcom.DOUBLE, agcom.DOUBLE, agcom.VARIANT)
        self.__dict__["_AssignCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+8, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignPlanetocentric"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+9, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_AssignPlanetodetic"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+10, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_QueryPlanetocentric"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+11, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_QueryPlanetodetic"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+12, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_QuerySpherical"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+13, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_QueryCylindrical"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+14, POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_QueryCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+15, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_GetCentralBodyName"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+16, POINTER(agcom.BSTR))
        self.__dict__["_QueryPlanetocentricArray"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+17, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryPlanetodeticArray"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+18, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QuerySphericalArray"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+19, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryCylindricalArray"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+20, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryCartesianArray"] = IAGFUNCTYPE(pUnk, IID_IAgPosition, vtable_offset_local+21, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPosition.__dict__ and type(IAgPosition.__dict__[attrname]) == property:
            return IAgPosition.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgPosition.")
    
    def ConvertTo(self, type:"AgEPositionType") -> "IAgPosition":
        """Changes the position coordinates to type specified."""
        with agmarshall.AgEnum_arg(AgEPositionType, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgPosition:
            agcls.evaluate_hresult(self.__dict__["_ConvertTo"](arg_type.COM_val, byref(arg_ppIAgPosition.COM_val)))
            return arg_ppIAgPosition.python_val

    @property
    def PosType(self) -> "AgEPositionType":
        """Gets the type of position currently being used."""
        with agmarshall.AgEnum_arg(AgEPositionType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_GetPosType"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def Assign(self, pPosition:"IAgPosition") -> None:
        """This assigns the coordinates into the system."""
        with agmarshall.AgInterface_in_arg(pPosition, IAgPosition) as arg_pPosition:
            agcls.evaluate_hresult(self.__dict__["_Assign"](arg_pPosition.COM_val))

    def AssignGeocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Geocentric representation."""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_AssignGeocentric"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def AssignGeodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Geodetic representation."""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_AssignGeodetic"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def AssignSpherical(self, lat:typing.Any, lon:typing.Any, radius:float) -> None:
        """Helper method to assign the position using the Spherical representation"""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(radius) as arg_radius:
            agcls.evaluate_hresult(self.__dict__["_AssignSpherical"](arg_lat.COM_val, arg_lon.COM_val, arg_radius.COM_val))

    def AssignCylindrical(self, radius:float, z:float, lon:typing.Any) -> None:
        """Helper method to assign the position using the Cylindrical representation"""
        with agmarshall.DOUBLE_arg(radius) as arg_radius, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.VARIANT_arg(lon) as arg_lon:
            agcls.evaluate_hresult(self.__dict__["_AssignCylindrical"](arg_radius.COM_val, arg_z.COM_val, arg_lon.COM_val))

    def AssignCartesian(self, x:float, y:float, z:float) -> None:
        """Helper method to assign the position using the Cartesian representation"""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_AssignCartesian"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def AssignPlanetocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Planetocentric representation"""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_AssignPlanetocentric"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def AssignPlanetodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Planetodetic representation"""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_AssignPlanetodetic"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def QueryPlanetocentric(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Planetocentric representation"""
        with agmarshall.VARIANT_arg() as arg_lat, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_QueryPlanetocentric"](byref(arg_lat.COM_val), byref(arg_lon.COM_val), byref(arg_alt.COM_val)))
            return arg_lat.python_val, arg_lon.python_val, arg_alt.python_val

    def QueryPlanetodetic(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Planetodetic representation"""
        with agmarshall.VARIANT_arg() as arg_lat, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_QueryPlanetodetic"](byref(arg_lat.COM_val), byref(arg_lon.COM_val), byref(arg_alt.COM_val)))
            return arg_lat.python_val, arg_lon.python_val, arg_alt.python_val

    def QuerySpherical(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Spherical representation"""
        with agmarshall.VARIANT_arg() as arg_lat, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_radius:
            agcls.evaluate_hresult(self.__dict__["_QuerySpherical"](byref(arg_lat.COM_val), byref(arg_lon.COM_val), byref(arg_radius.COM_val)))
            return arg_lat.python_val, arg_lon.python_val, arg_radius.python_val

    def QueryCylindrical(self) -> typing.Tuple[float, typing.Any, float]:
        """Helper method to get the position using the Cylindrical representation"""
        with agmarshall.DOUBLE_arg() as arg_radius, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_QueryCylindrical"](byref(arg_radius.COM_val), byref(arg_lon.COM_val), byref(arg_z.COM_val)))
            return arg_radius.python_val, arg_lon.python_val, arg_z.python_val

    def QueryCartesian(self) -> typing.Tuple[float, float, float]:
        """Helper method to get the position using the Cartesian representation"""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_QueryCartesian"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def CentralBodyName(self) -> str:
        """Gets the central body."""
        with agmarshall.BSTR_arg() as arg_pCBName:
            agcls.evaluate_hresult(self.__dict__["_GetCentralBodyName"](byref(arg_pCBName.COM_val)))
            return arg_pCBName.python_val

    def QueryPlanetocentricArray(self) -> list:
        """Returns the Planetocentric elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryPlanetocentricArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryPlanetodeticArray(self) -> list:
        """Returns the Planetodetic elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryPlanetodeticArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QuerySphericalArray(self) -> list:
        """Returns the Spherical elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QuerySphericalArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryCylindricalArray(self) -> list:
        """Returns the Cylindrical elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryCylindricalArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryCartesianArray(self) -> list:
        """Returns the Cartesian elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryCartesianArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{F25960CE-1D73-4BA0-A429-541DD6D808DE}", IAgPosition)
agcls.AgTypeNameMap["IAgPosition"] = IAgPosition
__all__.append("IAgPosition")

class IAgPlanetocentric(IAgPosition):
    """Planetocentric Position Type."""
    _uuid = "{605061D3-5594-4B88-AC0A-D4EA90EFFAA1}"
    _num_methods = 6
    _vtable_offset = IAgPosition._vtable_offset + IAgPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetLat"] = _raise_uninitialized_error
        self.__dict__["_SetLat"] = _raise_uninitialized_error
        self.__dict__["_GetLon"] = _raise_uninitialized_error
        self.__dict__["_SetLon"] = _raise_uninitialized_error
        self.__dict__["_GetAlt"] = _raise_uninitialized_error
        self.__dict__["_SetAlt"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPlanetocentric._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPlanetocentric from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPosition._private_init(self, pUnk)
        IID_IAgPlanetocentric = agcom.GUID(IAgPlanetocentric._uuid)
        vtable_offset_local = IAgPlanetocentric._vtable_offset - 1
        self.__dict__["_GetLat"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetocentric, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetLat"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetocentric, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetLon"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetocentric, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetLon"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetocentric, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetocentric, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetocentric, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPlanetocentric.__dict__ and type(IAgPlanetocentric.__dict__[attrname]) == property:
            return IAgPlanetocentric.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgPosition.__setattr__(self, attrname, value)
    
    @property
    def Lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Lat.setter
    def Lat(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetLat"](arg_pVal.COM_val))

    @property
    def Lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Lon.setter
    def Lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetLon"](arg_pVal.COM_val))

    @property
    def Alt(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetAlt"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Alt.setter
    def Alt(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetAlt"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{605061D3-5594-4B88-AC0A-D4EA90EFFAA1}", IAgPlanetocentric)
agcls.AgTypeNameMap["IAgPlanetocentric"] = IAgPlanetocentric
__all__.append("IAgPlanetocentric")

class IAgGeocentric(IAgPosition):
    """Geocentric Position Type."""
    _uuid = "{7D22F2C8-81B1-452E-AA06-0AEEB1FDF0F9}"
    _num_methods = 6
    _vtable_offset = IAgPosition._vtable_offset + IAgPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetLat"] = _raise_uninitialized_error
        self.__dict__["_SetLat"] = _raise_uninitialized_error
        self.__dict__["_GetLon"] = _raise_uninitialized_error
        self.__dict__["_SetLon"] = _raise_uninitialized_error
        self.__dict__["_GetAlt"] = _raise_uninitialized_error
        self.__dict__["_SetAlt"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgGeocentric._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgGeocentric from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPosition._private_init(self, pUnk)
        IID_IAgGeocentric = agcom.GUID(IAgGeocentric._uuid)
        vtable_offset_local = IAgGeocentric._vtable_offset - 1
        self.__dict__["_GetLat"] = IAGFUNCTYPE(pUnk, IID_IAgGeocentric, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetLat"] = IAGFUNCTYPE(pUnk, IID_IAgGeocentric, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetLon"] = IAGFUNCTYPE(pUnk, IID_IAgGeocentric, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetLon"] = IAGFUNCTYPE(pUnk, IID_IAgGeocentric, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgGeocentric, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgGeocentric, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGeocentric.__dict__ and type(IAgGeocentric.__dict__[attrname]) == property:
            return IAgGeocentric.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgPosition.__setattr__(self, attrname, value)
    
    @property
    def Lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Lat.setter
    def Lat(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetLat"](arg_pVal.COM_val))

    @property
    def Lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Lon.setter
    def Lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetLon"](arg_pVal.COM_val))

    @property
    def Alt(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetAlt"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Alt.setter
    def Alt(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetAlt"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{7D22F2C8-81B1-452E-AA06-0AEEB1FDF0F9}", IAgGeocentric)
agcls.AgTypeNameMap["IAgGeocentric"] = IAgGeocentric
__all__.append("IAgGeocentric")

class IAgSpherical(IAgPosition):
    """Spherical Position Type."""
    _uuid = "{62B93DF1-C615-4363-B4D9-DAA1ACE56204}"
    _num_methods = 6
    _vtable_offset = IAgPosition._vtable_offset + IAgPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetLat"] = _raise_uninitialized_error
        self.__dict__["_SetLat"] = _raise_uninitialized_error
        self.__dict__["_GetLon"] = _raise_uninitialized_error
        self.__dict__["_SetLon"] = _raise_uninitialized_error
        self.__dict__["_GetRadius"] = _raise_uninitialized_error
        self.__dict__["_SetRadius"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSpherical._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSpherical from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPosition._private_init(self, pUnk)
        IID_IAgSpherical = agcom.GUID(IAgSpherical._uuid)
        vtable_offset_local = IAgSpherical._vtable_offset - 1
        self.__dict__["_GetLat"] = IAGFUNCTYPE(pUnk, IID_IAgSpherical, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetLat"] = IAGFUNCTYPE(pUnk, IID_IAgSpherical, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetLon"] = IAGFUNCTYPE(pUnk, IID_IAgSpherical, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetLon"] = IAGFUNCTYPE(pUnk, IID_IAgSpherical, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetRadius"] = IAGFUNCTYPE(pUnk, IID_IAgSpherical, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetRadius"] = IAGFUNCTYPE(pUnk, IID_IAgSpherical, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSpherical.__dict__ and type(IAgSpherical.__dict__[attrname]) == property:
            return IAgSpherical.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgPosition.__setattr__(self, attrname, value)
    
    @property
    def Lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Lat.setter
    def Lat(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetLat"](arg_pVal.COM_val))

    @property
    def Lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Lon.setter
    def Lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetLon"](arg_pVal.COM_val))

    @property
    def Radius(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetRadius"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Radius.setter
    def Radius(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetRadius"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{62B93DF1-C615-4363-B4D9-DAA1ACE56204}", IAgSpherical)
agcls.AgTypeNameMap["IAgSpherical"] = IAgSpherical
__all__.append("IAgSpherical")

class IAgCylindrical(IAgPosition):
    """Cylindrical Position Type."""
    _uuid = "{36F08499-F7C4-41DE-AB49-794EC65C5165}"
    _num_methods = 6
    _vtable_offset = IAgPosition._vtable_offset + IAgPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetRadius"] = _raise_uninitialized_error
        self.__dict__["_SetRadius"] = _raise_uninitialized_error
        self.__dict__["_GetZ"] = _raise_uninitialized_error
        self.__dict__["_SetZ"] = _raise_uninitialized_error
        self.__dict__["_GetLon"] = _raise_uninitialized_error
        self.__dict__["_SetLon"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCylindrical._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCylindrical from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPosition._private_init(self, pUnk)
        IID_IAgCylindrical = agcom.GUID(IAgCylindrical._uuid)
        vtable_offset_local = IAgCylindrical._vtable_offset - 1
        self.__dict__["_GetRadius"] = IAGFUNCTYPE(pUnk, IID_IAgCylindrical, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_SetRadius"] = IAGFUNCTYPE(pUnk, IID_IAgCylindrical, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_GetZ"] = IAGFUNCTYPE(pUnk, IID_IAgCylindrical, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_SetZ"] = IAGFUNCTYPE(pUnk, IID_IAgCylindrical, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_GetLon"] = IAGFUNCTYPE(pUnk, IID_IAgCylindrical, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_SetLon"] = IAGFUNCTYPE(pUnk, IID_IAgCylindrical, vtable_offset_local+6, agcom.VARIANT)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCylindrical.__dict__ and type(IAgCylindrical.__dict__[attrname]) == property:
            return IAgCylindrical.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgPosition.__setattr__(self, attrname, value)
    
    @property
    def Radius(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetRadius"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Radius.setter
    def Radius(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetRadius"](arg_pVal.COM_val))

    @property
    def Z(self) -> float:
        """Uses Angle Dimension."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetZ"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Z.setter
    def Z(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetZ"](arg_pVal.COM_val))

    @property
    def Lon(self) -> typing.Any:
        """Dimension depends on context."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Lon.setter
    def Lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetLon"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{36F08499-F7C4-41DE-AB49-794EC65C5165}", IAgCylindrical)
agcls.AgTypeNameMap["IAgCylindrical"] = IAgCylindrical
__all__.append("IAgCylindrical")

class IAgCartesian(IAgPosition):
    """IAgCartesian Interface used to access a position using Cartesian Coordinates"""
    _uuid = "{F6D3AD94-04C0-464E-8B95-8A859AA1BCA7}"
    _num_methods = 6
    _vtable_offset = IAgPosition._vtable_offset + IAgPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetX"] = _raise_uninitialized_error
        self.__dict__["_SetX"] = _raise_uninitialized_error
        self.__dict__["_GetY"] = _raise_uninitialized_error
        self.__dict__["_SetY"] = _raise_uninitialized_error
        self.__dict__["_GetZ"] = _raise_uninitialized_error
        self.__dict__["_SetZ"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCartesian._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCartesian from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPosition._private_init(self, pUnk)
        IID_IAgCartesian = agcom.GUID(IAgCartesian._uuid)
        vtable_offset_local = IAgCartesian._vtable_offset - 1
        self.__dict__["_GetX"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_SetX"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_GetY"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_SetY"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_GetZ"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetZ"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCartesian.__dict__ and type(IAgCartesian.__dict__[attrname]) == property:
            return IAgCartesian.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgPosition.__setattr__(self, attrname, value)
    
    @property
    def X(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetX"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @X.setter
    def X(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetX"](arg_pVal.COM_val))

    @property
    def Y(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetY"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Y.setter
    def Y(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetY"](arg_pVal.COM_val))

    @property
    def Z(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetZ"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Z.setter
    def Z(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetZ"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{F6D3AD94-04C0-464E-8B95-8A859AA1BCA7}", IAgCartesian)
agcls.AgTypeNameMap["IAgCartesian"] = IAgCartesian
__all__.append("IAgCartesian")

class IAgGeodetic(IAgPosition):
    """IAgGeodetic sets the position using Geodetic properties."""
    _uuid = "{93D3322B-C842-48D2-AFCF-BC42B59DB28E}"
    _num_methods = 6
    _vtable_offset = IAgPosition._vtable_offset + IAgPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetLat"] = _raise_uninitialized_error
        self.__dict__["_SetLat"] = _raise_uninitialized_error
        self.__dict__["_GetLon"] = _raise_uninitialized_error
        self.__dict__["_SetLon"] = _raise_uninitialized_error
        self.__dict__["_GetAlt"] = _raise_uninitialized_error
        self.__dict__["_SetAlt"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgGeodetic._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgGeodetic from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPosition._private_init(self, pUnk)
        IID_IAgGeodetic = agcom.GUID(IAgGeodetic._uuid)
        vtable_offset_local = IAgGeodetic._vtable_offset - 1
        self.__dict__["_GetLat"] = IAGFUNCTYPE(pUnk, IID_IAgGeodetic, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetLat"] = IAGFUNCTYPE(pUnk, IID_IAgGeodetic, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetLon"] = IAGFUNCTYPE(pUnk, IID_IAgGeodetic, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetLon"] = IAGFUNCTYPE(pUnk, IID_IAgGeodetic, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgGeodetic, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgGeodetic, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGeodetic.__dict__ and type(IAgGeodetic.__dict__[attrname]) == property:
            return IAgGeodetic.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgPosition.__setattr__(self, attrname, value)
    
    @property
    def Lat(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_GetLat"](byref(arg_pLat.COM_val)))
            return arg_pLat.python_val

    @Lat.setter
    def Lat(self, pLat:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLat) as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_SetLat"](arg_pLat.COM_val))

    @property
    def Lon(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_GetLon"](byref(arg_pLon.COM_val)))
            return arg_pLon.python_val

    @Lon.setter
    def Lon(self, pLon:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLon) as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_SetLon"](arg_pLon.COM_val))

    @property
    def Alt(self) -> float:
        """Altitude. Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_GetAlt"](byref(arg_pAlt.COM_val)))
            return arg_pAlt.python_val

    @Alt.setter
    def Alt(self, pAlt:float) -> None:
        with agmarshall.DOUBLE_arg(pAlt) as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_SetAlt"](arg_pAlt.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{93D3322B-C842-48D2-AFCF-BC42B59DB28E}", IAgGeodetic)
agcls.AgTypeNameMap["IAgGeodetic"] = IAgGeodetic
__all__.append("IAgGeodetic")

class IAgPlanetodetic(IAgPosition):
    """IAgPlanetodetic sets the position using Planetodetic properties."""
    _uuid = "{E0F982B1-7B17-40F7-B64B-AFD0D112A74C}"
    _num_methods = 6
    _vtable_offset = IAgPosition._vtable_offset + IAgPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetLat"] = _raise_uninitialized_error
        self.__dict__["_SetLat"] = _raise_uninitialized_error
        self.__dict__["_GetLon"] = _raise_uninitialized_error
        self.__dict__["_SetLon"] = _raise_uninitialized_error
        self.__dict__["_GetAlt"] = _raise_uninitialized_error
        self.__dict__["_SetAlt"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPlanetodetic._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPlanetodetic from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPosition._private_init(self, pUnk)
        IID_IAgPlanetodetic = agcom.GUID(IAgPlanetodetic._uuid)
        vtable_offset_local = IAgPlanetodetic._vtable_offset - 1
        self.__dict__["_GetLat"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetodetic, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetLat"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetodetic, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetLon"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetodetic, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetLon"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetodetic, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetodetic, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgPlanetodetic, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPlanetodetic.__dict__ and type(IAgPlanetodetic.__dict__[attrname]) == property:
            return IAgPlanetodetic.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgPosition.__setattr__(self, attrname, value)
    
    @property
    def Lat(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_GetLat"](byref(arg_pLat.COM_val)))
            return arg_pLat.python_val

    @Lat.setter
    def Lat(self, pLat:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLat) as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_SetLat"](arg_pLat.COM_val))

    @property
    def Lon(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_GetLon"](byref(arg_pLon.COM_val)))
            return arg_pLon.python_val

    @Lon.setter
    def Lon(self, pLon:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLon) as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_SetLon"](arg_pLon.COM_val))

    @property
    def Alt(self) -> float:
        """Altitude. Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_GetAlt"](byref(arg_pAlt.COM_val)))
            return arg_pAlt.python_val

    @Alt.setter
    def Alt(self, pAlt:float) -> None:
        with agmarshall.DOUBLE_arg(pAlt) as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_SetAlt"](arg_pAlt.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{E0F982B1-7B17-40F7-B64B-AFD0D112A74C}", IAgPlanetodetic)
agcls.AgTypeNameMap["IAgPlanetodetic"] = IAgPlanetodetic
__all__.append("IAgPlanetodetic")

class IAgDirection(object):
    """Interface to set and retrieve direction options for aligned and constrained vectors."""
    _uuid = "{8304507A-4915-453D-8944-2080659C0257}"
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ConvertTo"] = _raise_uninitialized_error
        self.__dict__["_GetDirectionType"] = _raise_uninitialized_error
        self.__dict__["_Assign"] = _raise_uninitialized_error
        self.__dict__["_AssignEuler"] = _raise_uninitialized_error
        self.__dict__["_AssignPR"] = _raise_uninitialized_error
        self.__dict__["_AssignRADec"] = _raise_uninitialized_error
        self.__dict__["_AssignXYZ"] = _raise_uninitialized_error
        self.__dict__["_QueryEuler"] = _raise_uninitialized_error
        self.__dict__["_QueryPR"] = _raise_uninitialized_error
        self.__dict__["_QueryRADec"] = _raise_uninitialized_error
        self.__dict__["_QueryXYZ"] = _raise_uninitialized_error
        self.__dict__["_QueryEulerArray"] = _raise_uninitialized_error
        self.__dict__["_QueryPRArray"] = _raise_uninitialized_error
        self.__dict__["_QueryRADecArray"] = _raise_uninitialized_error
        self.__dict__["_QueryXYZArray"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDirection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDirection from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgDirection = agcom.GUID(IAgDirection._uuid)
        vtable_offset_local = IAgDirection._vtable_offset - 1
        self.__dict__["_ConvertTo"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_GetDirectionType"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Assign"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_AssignEuler"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+4, agcom.VARIANT, agcom.VARIANT, agcom.LONG)
        self.__dict__["_AssignPR"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+5, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_AssignRADec"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+6, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_AssignXYZ"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+7, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_QueryEuler"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+8, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_QueryPR"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+9, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_QueryRADec"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+10, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_QueryXYZ"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+11, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_QueryEulerArray"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+12, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryPRArray"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryRADecArray"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+14, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryXYZArray"] = IAGFUNCTYPE(pUnk, IID_IAgDirection, vtable_offset_local+15, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDirection.__dict__ and type(IAgDirection.__dict__[attrname]) == property:
            return IAgDirection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgDirection.")
    
    def ConvertTo(self, type:"AgEDirectionType") -> "IAgDirection":
        """Method to changes the direction to the type specified."""
        with agmarshall.AgEnum_arg(AgEDirectionType, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgDirection:
            agcls.evaluate_hresult(self.__dict__["_ConvertTo"](arg_type.COM_val, byref(arg_ppIAgDirection.COM_val)))
            return arg_ppIAgDirection.python_val

    @property
    def DirectionType(self) -> "AgEDirectionType":
        """Returns the type of direction currently being used."""
        with agmarshall.AgEnum_arg(AgEDirectionType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_GetDirectionType"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def Assign(self, pDirection:"IAgDirection") -> None:
        """Assign a new direction."""
        with agmarshall.AgInterface_in_arg(pDirection, IAgDirection) as arg_pDirection:
            agcls.evaluate_hresult(self.__dict__["_Assign"](arg_pDirection.COM_val))

    def AssignEuler(self, b:typing.Any, c:typing.Any, sequence:"AgEEulerDirectionSequence") -> None:
        """Helper method to set direction using the Euler representation. Params B and C use Angle Dimension."""
        with agmarshall.VARIANT_arg(b) as arg_b, \
             agmarshall.VARIANT_arg(c) as arg_c, \
             agmarshall.AgEnum_arg(AgEEulerDirectionSequence, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_AssignEuler"](arg_b.COM_val, arg_c.COM_val, arg_sequence.COM_val))

    def AssignPR(self, pitch:typing.Any, roll:typing.Any) -> None:
        """Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        with agmarshall.VARIANT_arg(pitch) as arg_pitch, \
             agmarshall.VARIANT_arg(roll) as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_AssignPR"](arg_pitch.COM_val, arg_roll.COM_val))

    def AssignRADec(self, ra:typing.Any, dec:typing.Any) -> None:
        """Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        with agmarshall.VARIANT_arg(ra) as arg_ra, \
             agmarshall.VARIANT_arg(dec) as arg_dec:
            agcls.evaluate_hresult(self.__dict__["_AssignRADec"](arg_ra.COM_val, arg_dec.COM_val))

    def AssignXYZ(self, x:float, y:float, z:float) -> None:
        """Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_AssignXYZ"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def QueryEuler(self, sequence:"AgEEulerDirectionSequence") -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Euler representation. Params B and C use Angle Dimension."""
        with agmarshall.AgEnum_arg(AgEEulerDirectionSequence, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_b, \
             agmarshall.VARIANT_arg() as arg_c:
            agcls.evaluate_hresult(self.__dict__["_QueryEuler"](arg_sequence.COM_val, byref(arg_b.COM_val), byref(arg_c.COM_val)))
            return arg_b.python_val, arg_c.python_val

    def QueryPR(self, sequence:"AgEPRSequence") -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        with agmarshall.AgEnum_arg(AgEPRSequence, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_pitch, \
             agmarshall.VARIANT_arg() as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_QueryPR"](arg_sequence.COM_val, byref(arg_pitch.COM_val), byref(arg_roll.COM_val)))
            return arg_pitch.python_val, arg_roll.python_val

    def QueryRADec(self) -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        with agmarshall.VARIANT_arg() as arg_ra, \
             agmarshall.VARIANT_arg() as arg_dec:
            agcls.evaluate_hresult(self.__dict__["_QueryRADec"](byref(arg_ra.COM_val), byref(arg_dec.COM_val)))
            return arg_ra.python_val, arg_dec.python_val

    def QueryXYZ(self) -> typing.Tuple[float, float, float]:
        """Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_QueryXYZ"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    def QueryEulerArray(self, sequence:"AgEEulerDirectionSequence") -> list:
        """Returns the Euler elements in an array."""
        with agmarshall.AgEnum_arg(AgEEulerDirectionSequence, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryEulerArray"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryPRArray(self, sequence:"AgEPRSequence") -> list:
        """Returns the PR elements in an array."""
        with agmarshall.AgEnum_arg(AgEPRSequence, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryPRArray"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryRADecArray(self) -> list:
        """Returns the RADec elements in an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryRADecArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryXYZArray(self) -> list:
        """Returns the XYZ elements in an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryXYZArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{8304507A-4915-453D-8944-2080659C0257}", IAgDirection)
agcls.AgTypeNameMap["IAgDirection"] = IAgDirection
__all__.append("IAgDirection")

class IAgDirectionEuler(IAgDirection):
    """Interface for Euler direction sequence."""
    _uuid = "{9CBDC138-72D1-4734-8F95-2140266D37B5}"
    _num_methods = 6
    _vtable_offset = IAgDirection._vtable_offset + IAgDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetB"] = _raise_uninitialized_error
        self.__dict__["_SetB"] = _raise_uninitialized_error
        self.__dict__["_GetC"] = _raise_uninitialized_error
        self.__dict__["_SetC"] = _raise_uninitialized_error
        self.__dict__["_GetSequence"] = _raise_uninitialized_error
        self.__dict__["_SetSequence"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDirectionEuler._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDirectionEuler from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirection._private_init(self, pUnk)
        IID_IAgDirectionEuler = agcom.GUID(IAgDirectionEuler._uuid)
        vtable_offset_local = IAgDirectionEuler._vtable_offset - 1
        self.__dict__["_GetB"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionEuler, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetB"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionEuler, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetC"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionEuler, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetC"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionEuler, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionEuler, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_SetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionEuler, vtable_offset_local+6, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDirectionEuler.__dict__ and type(IAgDirectionEuler.__dict__[attrname]) == property:
            return IAgDirectionEuler.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgDirection.__setattr__(self, attrname, value)
    
    @property
    def B(self) -> typing.Any:
        """Euler B angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetB"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @B.setter
    def B(self, va:typing.Any) -> None:
        with agmarshall.VARIANT_arg(va) as arg_va:
            agcls.evaluate_hresult(self.__dict__["_SetB"](arg_va.COM_val))

    @property
    def C(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetC"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @C.setter
    def C(self, vb:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vb) as arg_vb:
            agcls.evaluate_hresult(self.__dict__["_SetC"](arg_vb.COM_val))

    @property
    def Sequence(self) -> "AgEEulerDirectionSequence":
        """Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(AgEEulerDirectionSequence) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetSequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Sequence.setter
    def Sequence(self, sequence:"AgEEulerDirectionSequence") -> None:
        with agmarshall.AgEnum_arg(AgEEulerDirectionSequence, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_SetSequence"](arg_sequence.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{9CBDC138-72D1-4734-8F95-2140266D37B5}", IAgDirectionEuler)
agcls.AgTypeNameMap["IAgDirectionEuler"] = IAgDirectionEuler
__all__.append("IAgDirectionEuler")

class IAgDirectionPR(IAgDirection):
    """Interface for Pitch-Roll (PR) direction sequence."""
    _uuid = "{5AC01BF1-2B95-4C13-8B69-09FDC485330E}"
    _num_methods = 6
    _vtable_offset = IAgDirection._vtable_offset + IAgDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetPitch"] = _raise_uninitialized_error
        self.__dict__["_SetPitch"] = _raise_uninitialized_error
        self.__dict__["_GetRoll"] = _raise_uninitialized_error
        self.__dict__["_SetRoll"] = _raise_uninitialized_error
        self.__dict__["_GetSequence"] = _raise_uninitialized_error
        self.__dict__["_SetSequence"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDirectionPR._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDirectionPR from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirection._private_init(self, pUnk)
        IID_IAgDirectionPR = agcom.GUID(IAgDirectionPR._uuid)
        vtable_offset_local = IAgDirectionPR._vtable_offset - 1
        self.__dict__["_GetPitch"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionPR, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetPitch"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionPR, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetRoll"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionPR, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetRoll"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionPR, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionPR, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_SetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionPR, vtable_offset_local+6, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDirectionPR.__dict__ and type(IAgDirectionPR.__dict__[attrname]) == property:
            return IAgDirectionPR.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgDirection.__setattr__(self, attrname, value)
    
    @property
    def Pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPitch"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Pitch.setter
    def Pitch(self, vPitch:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vPitch) as arg_vPitch:
            agcls.evaluate_hresult(self.__dict__["_SetPitch"](arg_vPitch.COM_val))

    @property
    def Roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetRoll"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Roll.setter
    def Roll(self, vRoll:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vRoll) as arg_vRoll:
            agcls.evaluate_hresult(self.__dict__["_SetRoll"](arg_vRoll.COM_val))

    @property
    def Sequence(self) -> "AgEPRSequence":
        """PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(AgEPRSequence) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetSequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Sequence.setter
    def Sequence(self, sequence:"AgEPRSequence") -> None:
        with agmarshall.AgEnum_arg(AgEPRSequence, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_SetSequence"](arg_sequence.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{5AC01BF1-2B95-4C13-8B69-09FDC485330E}", IAgDirectionPR)
agcls.AgTypeNameMap["IAgDirectionPR"] = IAgDirectionPR
__all__.append("IAgDirectionPR")

class IAgDirectionRADec(IAgDirection):
    """Interface for Spherical direction (Right Ascension and Declination)."""
    _uuid = "{A921E587-EC8A-4F1E-99BB-6E13B8E0D5E7}"
    _num_methods = 6
    _vtable_offset = IAgDirection._vtable_offset + IAgDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetDec"] = _raise_uninitialized_error
        self.__dict__["_SetDec"] = _raise_uninitialized_error
        self.__dict__["_GetRA"] = _raise_uninitialized_error
        self.__dict__["_SetRA"] = _raise_uninitialized_error
        self.__dict__["_GetMagnitude"] = _raise_uninitialized_error
        self.__dict__["_SetMagnitude"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDirectionRADec._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDirectionRADec from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirection._private_init(self, pUnk)
        IID_IAgDirectionRADec = agcom.GUID(IAgDirectionRADec._uuid)
        vtable_offset_local = IAgDirectionRADec._vtable_offset - 1
        self.__dict__["_GetDec"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionRADec, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetDec"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionRADec, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetRA"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionRADec, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetRA"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionRADec, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetMagnitude"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionRADec, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetMagnitude"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionRADec, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDirectionRADec.__dict__ and type(IAgDirectionRADec.__dict__[attrname]) == property:
            return IAgDirectionRADec.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgDirection.__setattr__(self, attrname, value)
    
    @property
    def Dec(self) -> typing.Any:
        """Declination: angle above the x-y plane. Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetDec"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Dec.setter
    def Dec(self, vLat:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vLat) as arg_vLat:
            agcls.evaluate_hresult(self.__dict__["_SetDec"](arg_vLat.COM_val))

    @property
    def RA(self) -> typing.Any:
        """Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetRA"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @RA.setter
    def RA(self, vLon:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vLon) as arg_vLon:
            agcls.evaluate_hresult(self.__dict__["_SetRA"](arg_vLon.COM_val))

    @property
    def Magnitude(self) -> float:
        """A unitless value that represents magnitude."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetMagnitude"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Magnitude.setter
    def Magnitude(self, magnitude:float) -> None:
        with agmarshall.DOUBLE_arg(magnitude) as arg_magnitude:
            agcls.evaluate_hresult(self.__dict__["_SetMagnitude"](arg_magnitude.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{A921E587-EC8A-4F1E-99BB-6E13B8E0D5E7}", IAgDirectionRADec)
agcls.AgTypeNameMap["IAgDirectionRADec"] = IAgDirectionRADec
__all__.append("IAgDirectionRADec")

class IAgDirectionXYZ(IAgDirection):
    """Interface for Cartesian direction."""
    _uuid = "{2B499A22-6662-4F20-8B82-AA7701CD87A4}"
    _num_methods = 6
    _vtable_offset = IAgDirection._vtable_offset + IAgDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetX"] = _raise_uninitialized_error
        self.__dict__["_SetX"] = _raise_uninitialized_error
        self.__dict__["_GetY"] = _raise_uninitialized_error
        self.__dict__["_SetY"] = _raise_uninitialized_error
        self.__dict__["_GetZ"] = _raise_uninitialized_error
        self.__dict__["_SetZ"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDirectionXYZ._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDirectionXYZ from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirection._private_init(self, pUnk)
        IID_IAgDirectionXYZ = agcom.GUID(IAgDirectionXYZ._uuid)
        vtable_offset_local = IAgDirectionXYZ._vtable_offset - 1
        self.__dict__["_GetX"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionXYZ, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_SetX"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionXYZ, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_GetY"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionXYZ, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_SetY"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionXYZ, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_GetZ"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionXYZ, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetZ"] = IAGFUNCTYPE(pUnk, IID_IAgDirectionXYZ, vtable_offset_local+6, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDirectionXYZ.__dict__ and type(IAgDirectionXYZ.__dict__[attrname]) == property:
            return IAgDirectionXYZ.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgDirection.__setattr__(self, attrname, value)
    
    @property
    def X(self) -> float:
        """X component. Dimensionless"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetX"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @X.setter
    def X(self, vx:float) -> None:
        with agmarshall.DOUBLE_arg(vx) as arg_vx:
            agcls.evaluate_hresult(self.__dict__["_SetX"](arg_vx.COM_val))

    @property
    def Y(self) -> float:
        """Y component. Dimensionless"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetY"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Y.setter
    def Y(self, vy:float) -> None:
        with agmarshall.DOUBLE_arg(vy) as arg_vy:
            agcls.evaluate_hresult(self.__dict__["_SetY"](arg_vy.COM_val))

    @property
    def Z(self) -> float:
        """Z component. Dimensionless"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetZ"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Z.setter
    def Z(self, vz:float) -> None:
        with agmarshall.DOUBLE_arg(vz) as arg_vz:
            agcls.evaluate_hresult(self.__dict__["_SetZ"](arg_vz.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{2B499A22-6662-4F20-8B82-AA7701CD87A4}", IAgDirectionXYZ)
agcls.AgTypeNameMap["IAgDirectionXYZ"] = IAgDirectionXYZ
__all__.append("IAgDirectionXYZ")

class IAgCartesian3Vector(object):
    """Represents a cartesian 3-D vector."""
    _uuid = "{7B741836-71F9-4115-97F8-EAB30362E5C7}"
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetX"] = _raise_uninitialized_error
        self.__dict__["_SetX"] = _raise_uninitialized_error
        self.__dict__["_GetY"] = _raise_uninitialized_error
        self.__dict__["_SetY"] = _raise_uninitialized_error
        self.__dict__["_GetZ"] = _raise_uninitialized_error
        self.__dict__["_SetZ"] = _raise_uninitialized_error
        self.__dict__["_Get"] = _raise_uninitialized_error
        self.__dict__["_Set"] = _raise_uninitialized_error
        self.__dict__["_ToArray"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCartesian3Vector._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCartesian3Vector from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCartesian3Vector = agcom.GUID(IAgCartesian3Vector._uuid)
        vtable_offset_local = IAgCartesian3Vector._vtable_offset - 1
        self.__dict__["_GetX"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_SetX"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_GetY"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_SetY"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_GetZ"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetZ"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__["_Get"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+7, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_Set"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+8, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_ToArray"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian3Vector, vtable_offset_local+9, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCartesian3Vector.__dict__ and type(IAgCartesian3Vector.__dict__[attrname]) == property:
            return IAgCartesian3Vector.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCartesian3Vector.")
    
    @property
    def X(self) -> float:
        """X coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetX"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @X.setter
    def X(self, x:float) -> None:
        with agmarshall.DOUBLE_arg(x) as arg_x:
            agcls.evaluate_hresult(self.__dict__["_SetX"](arg_x.COM_val))

    @property
    def Y(self) -> float:
        """Y coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetY"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @Y.setter
    def Y(self, y:float) -> None:
        with agmarshall.DOUBLE_arg(y) as arg_y:
            agcls.evaluate_hresult(self.__dict__["_SetY"](arg_y.COM_val))

    @property
    def Z(self) -> float:
        """Z coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetZ"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @Z.setter
    def Z(self, z:float) -> None:
        with agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_SetZ"](arg_z.COM_val))

    def Get(self) -> typing.Tuple[float, float, float]:
        """Returns cartesian vector"""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_Get"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    def Set(self, x:float, y:float, z:float) -> None:
        """Sets cartesian vector"""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_Set"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def ToArray(self) -> list:
        """Returns coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_ToArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{7B741836-71F9-4115-97F8-EAB30362E5C7}", IAgCartesian3Vector)
agcls.AgTypeNameMap["IAgCartesian3Vector"] = IAgCartesian3Vector
__all__.append("IAgCartesian3Vector")

class IAgOrientation(object):
    """Interface to set and retrieve the orientation method."""
    _uuid = "{8467175F-1BD8-4498-90FD-08C67072D120}"
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ConvertTo"] = _raise_uninitialized_error
        self.__dict__["_GetOrientationType"] = _raise_uninitialized_error
        self.__dict__["_Assign"] = _raise_uninitialized_error
        self.__dict__["_AssignAzEl"] = _raise_uninitialized_error
        self.__dict__["_AssignEulerAngles"] = _raise_uninitialized_error
        self.__dict__["_AssignQuaternion"] = _raise_uninitialized_error
        self.__dict__["_AssignYPRAngles"] = _raise_uninitialized_error
        self.__dict__["_QueryAzEl"] = _raise_uninitialized_error
        self.__dict__["_QueryEulerAngles"] = _raise_uninitialized_error
        self.__dict__["_QueryQuaternion"] = _raise_uninitialized_error
        self.__dict__["_QueryYPRAngles"] = _raise_uninitialized_error
        self.__dict__["_QueryAzElArray"] = _raise_uninitialized_error
        self.__dict__["_QueryEulerAnglesArray"] = _raise_uninitialized_error
        self.__dict__["_QueryQuaternionArray"] = _raise_uninitialized_error
        self.__dict__["_QueryYPRAnglesArray"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgOrientation._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgOrientation from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgOrientation = agcom.GUID(IAgOrientation._uuid)
        vtable_offset_local = IAgOrientation._vtable_offset - 1
        self.__dict__["_ConvertTo"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_GetOrientationType"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Assign"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_AssignAzEl"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+4, agcom.VARIANT, agcom.VARIANT, agcom.LONG)
        self.__dict__["_AssignEulerAngles"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+5, agcom.LONG, agcom.VARIANT, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_AssignQuaternion"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+6, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignYPRAngles"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+7, agcom.LONG, agcom.VARIANT, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_QueryAzEl"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+8, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.LONG))
        self.__dict__["_QueryEulerAngles"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+9, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_QueryQuaternion"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+10, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_QueryYPRAngles"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+11, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_QueryAzElArray"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+12, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryEulerAnglesArray"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryQuaternionArray"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+14, POINTER(agcom.SAFEARRAY))
        self.__dict__["_QueryYPRAnglesArray"] = IAGFUNCTYPE(pUnk, IID_IAgOrientation, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgOrientation.__dict__ and type(IAgOrientation.__dict__[attrname]) == property:
            return IAgOrientation.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgOrientation.")
    
    def ConvertTo(self, type:"AgEOrientationType") -> "IAgOrientation":
        """Method to change the orientation method to the type specified."""
        with agmarshall.AgEnum_arg(AgEOrientationType, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgOrientation:
            agcls.evaluate_hresult(self.__dict__["_ConvertTo"](arg_type.COM_val, byref(arg_ppIAgOrientation.COM_val)))
            return arg_ppIAgOrientation.python_val

    @property
    def OrientationType(self) -> "AgEOrientationType":
        """Returns the orientation method currently being used."""
        with agmarshall.AgEnum_arg(AgEOrientationType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_GetOrientationType"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def Assign(self, pOrientation:"IAgOrientation") -> None:
        """Assign a new orientation method."""
        with agmarshall.AgInterface_in_arg(pOrientation, IAgOrientation) as arg_pOrientation:
            agcls.evaluate_hresult(self.__dict__["_Assign"](arg_pOrientation.COM_val))

    def AssignAzEl(self, azimuth:typing.Any, elevation:typing.Any, aboutBoresight:"AgEAzElAboutBoresight") -> None:
        """Helper method to set orientation using the AzEl representation."""
        with agmarshall.VARIANT_arg(azimuth) as arg_azimuth, \
             agmarshall.VARIANT_arg(elevation) as arg_elevation, \
             agmarshall.AgEnum_arg(AgEAzElAboutBoresight, aboutBoresight) as arg_aboutBoresight:
            agcls.evaluate_hresult(self.__dict__["_AssignAzEl"](arg_azimuth.COM_val, arg_elevation.COM_val, arg_aboutBoresight.COM_val))

    def AssignEulerAngles(self, sequence:"AgEEulerOrientationSequence", a:typing.Any, b:typing.Any, c:typing.Any) -> None:
        """Helper method to set orientation using the Euler angles representation."""
        with agmarshall.AgEnum_arg(AgEEulerOrientationSequence, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg(a) as arg_a, \
             agmarshall.VARIANT_arg(b) as arg_b, \
             agmarshall.VARIANT_arg(c) as arg_c:
            agcls.evaluate_hresult(self.__dict__["_AssignEulerAngles"](arg_sequence.COM_val, arg_a.COM_val, arg_b.COM_val, arg_c.COM_val))

    def AssignQuaternion(self, qx:float, qy:float, qz:float, qs:float) -> None:
        """Helper method to set orientation using the Quaternion representation."""
        with agmarshall.DOUBLE_arg(qx) as arg_qx, \
             agmarshall.DOUBLE_arg(qy) as arg_qy, \
             agmarshall.DOUBLE_arg(qz) as arg_qz, \
             agmarshall.DOUBLE_arg(qs) as arg_qs:
            agcls.evaluate_hresult(self.__dict__["_AssignQuaternion"](arg_qx.COM_val, arg_qy.COM_val, arg_qz.COM_val, arg_qs.COM_val))

    def AssignYPRAngles(self, sequence:"AgEYPRAnglesSequence", yaw:typing.Any, pitch:typing.Any, roll:typing.Any) -> None:
        """Helper method to set orientation using the YPR angles representation."""
        with agmarshall.AgEnum_arg(AgEYPRAnglesSequence, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg(yaw) as arg_yaw, \
             agmarshall.VARIANT_arg(pitch) as arg_pitch, \
             agmarshall.VARIANT_arg(roll) as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_AssignYPRAngles"](arg_sequence.COM_val, arg_yaw.COM_val, arg_pitch.COM_val, arg_roll.COM_val))

    def QueryAzEl(self) -> typing.Tuple[typing.Any, typing.Any, AgEAzElAboutBoresight]:
        """Helper method to get orientation using the AzEl representation."""
        with agmarshall.VARIANT_arg() as arg_azimuth, \
             agmarshall.VARIANT_arg() as arg_elevation, \
             agmarshall.AgEnum_arg(AgEAzElAboutBoresight) as arg_aboutBoresight:
            agcls.evaluate_hresult(self.__dict__["_QueryAzEl"](byref(arg_azimuth.COM_val), byref(arg_elevation.COM_val), byref(arg_aboutBoresight.COM_val)))
            return arg_azimuth.python_val, arg_elevation.python_val, arg_aboutBoresight.python_val

    def QueryEulerAngles(self, sequence:"AgEEulerOrientationSequence") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Helper method to get orientation using the Euler angles representation."""
        with agmarshall.AgEnum_arg(AgEEulerOrientationSequence, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_a, \
             agmarshall.VARIANT_arg() as arg_b, \
             agmarshall.VARIANT_arg() as arg_c:
            agcls.evaluate_hresult(self.__dict__["_QueryEulerAngles"](arg_sequence.COM_val, byref(arg_a.COM_val), byref(arg_b.COM_val), byref(arg_c.COM_val)))
            return arg_a.python_val, arg_b.python_val, arg_c.python_val

    def QueryQuaternion(self) -> typing.Tuple[float, float, float, float]:
        """Helper method to get orientation using the Quaternion representation."""
        with agmarshall.DOUBLE_arg() as arg_qx, \
             agmarshall.DOUBLE_arg() as arg_qy, \
             agmarshall.DOUBLE_arg() as arg_qz, \
             agmarshall.DOUBLE_arg() as arg_qs:
            agcls.evaluate_hresult(self.__dict__["_QueryQuaternion"](byref(arg_qx.COM_val), byref(arg_qy.COM_val), byref(arg_qz.COM_val), byref(arg_qs.COM_val)))
            return arg_qx.python_val, arg_qy.python_val, arg_qz.python_val, arg_qs.python_val

    def QueryYPRAngles(self, sequence:"AgEYPRAnglesSequence") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Helper method to get orientation using the YPR angles representation."""
        with agmarshall.AgEnum_arg(AgEYPRAnglesSequence, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_yaw, \
             agmarshall.VARIANT_arg() as arg_pitch, \
             agmarshall.VARIANT_arg() as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_QueryYPRAngles"](arg_sequence.COM_val, byref(arg_yaw.COM_val), byref(arg_pitch.COM_val), byref(arg_roll.COM_val)))
            return arg_yaw.python_val, arg_pitch.python_val, arg_roll.python_val

    def QueryAzElArray(self) -> list:
        """Returns the AzEl elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryAzElArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryEulerAnglesArray(self, sequence:"AgEEulerOrientationSequence") -> list:
        """Returns the Euler elements as an array."""
        with agmarshall.AgEnum_arg(AgEEulerOrientationSequence, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryEulerAnglesArray"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryQuaternionArray(self) -> list:
        """Returns the Quaternion elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryQuaternionArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryYPRAnglesArray(self, sequence:"AgEYPRAnglesSequence") -> list:
        """Returns the YPR Angles elements as an array."""
        with agmarshall.AgEnum_arg(AgEYPRAnglesSequence, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryYPRAnglesArray"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{8467175F-1BD8-4498-90FD-08C67072D120}", IAgOrientation)
agcls.AgTypeNameMap["IAgOrientation"] = IAgOrientation
__all__.append("IAgOrientation")

class IAgOrientationAzEl(IAgOrientation):
    """Interface for AzEl orientation method."""
    _uuid = "{6A6B1D7D-6A7F-48B3-98CA-019CA46499FE}"
    _num_methods = 6
    _vtable_offset = IAgOrientation._vtable_offset + IAgOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetAzimuth"] = _raise_uninitialized_error
        self.__dict__["_SetAzimuth"] = _raise_uninitialized_error
        self.__dict__["_GetElevation"] = _raise_uninitialized_error
        self.__dict__["_SetElevation"] = _raise_uninitialized_error
        self.__dict__["_GetAboutBoresight"] = _raise_uninitialized_error
        self.__dict__["_SetAboutBoresight"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgOrientationAzEl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgOrientationAzEl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientation._private_init(self, pUnk)
        IID_IAgOrientationAzEl = agcom.GUID(IAgOrientationAzEl._uuid)
        vtable_offset_local = IAgOrientationAzEl._vtable_offset - 1
        self.__dict__["_GetAzimuth"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationAzEl, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_SetAzimuth"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationAzEl, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_GetElevation"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationAzEl, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetElevation"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationAzEl, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetAboutBoresight"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationAzEl, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_SetAboutBoresight"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationAzEl, vtable_offset_local+6, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgOrientationAzEl.__dict__ and type(IAgOrientationAzEl.__dict__[attrname]) == property:
            return IAgOrientationAzEl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgOrientation.__setattr__(self, attrname, value)
    
    @property
    def Azimuth(self) -> typing.Any:
        """Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetAzimuth"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Azimuth.setter
    def Azimuth(self, vAzimuth:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vAzimuth) as arg_vAzimuth:
            agcls.evaluate_hresult(self.__dict__["_SetAzimuth"](arg_vAzimuth.COM_val))

    @property
    def Elevation(self) -> typing.Any:
        """Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetElevation"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Elevation.setter
    def Elevation(self, vElevation:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vElevation) as arg_vElevation:
            agcls.evaluate_hresult(self.__dict__["_SetElevation"](arg_vElevation.COM_val))

    @property
    def AboutBoresight(self) -> "AgEAzElAboutBoresight":
        """Determines orientation of the X and Y axes with respect to the parent's reference frame."""
        with agmarshall.AgEnum_arg(AgEAzElAboutBoresight) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetAboutBoresight"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @AboutBoresight.setter
    def AboutBoresight(self, aboutBoresight:"AgEAzElAboutBoresight") -> None:
        with agmarshall.AgEnum_arg(AgEAzElAboutBoresight, aboutBoresight) as arg_aboutBoresight:
            agcls.evaluate_hresult(self.__dict__["_SetAboutBoresight"](arg_aboutBoresight.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{6A6B1D7D-6A7F-48B3-98CA-019CA46499FE}", IAgOrientationAzEl)
agcls.AgTypeNameMap["IAgOrientationAzEl"] = IAgOrientationAzEl
__all__.append("IAgOrientationAzEl")

class IAgOrientationEulerAngles(IAgOrientation):
    """Interface for Euler Angles orientation method."""
    _uuid = "{4204C7E1-EC21-40AD-A905-BB35A3FDF7BD}"
    _num_methods = 8
    _vtable_offset = IAgOrientation._vtable_offset + IAgOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetSequence"] = _raise_uninitialized_error
        self.__dict__["_SetSequence"] = _raise_uninitialized_error
        self.__dict__["_GetA"] = _raise_uninitialized_error
        self.__dict__["_SetA"] = _raise_uninitialized_error
        self.__dict__["_GetB"] = _raise_uninitialized_error
        self.__dict__["_SetB"] = _raise_uninitialized_error
        self.__dict__["_GetC"] = _raise_uninitialized_error
        self.__dict__["_SetC"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgOrientationEulerAngles._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgOrientationEulerAngles from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientation._private_init(self, pUnk)
        IID_IAgOrientationEulerAngles = agcom.GUID(IAgOrientationEulerAngles._uuid)
        vtable_offset_local = IAgOrientationEulerAngles._vtable_offset - 1
        self.__dict__["_GetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_SetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+2, agcom.LONG)
        self.__dict__["_GetA"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetA"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetB"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_SetB"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+6, agcom.VARIANT)
        self.__dict__["_GetC"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+7, POINTER(agcom.VARIANT))
        self.__dict__["_SetC"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationEulerAngles, vtable_offset_local+8, agcom.VARIANT)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgOrientationEulerAngles.__dict__ and type(IAgOrientationEulerAngles.__dict__[attrname]) == property:
            return IAgOrientationEulerAngles.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgOrientation.__setattr__(self, attrname, value)
    
    @property
    def Sequence(self) -> "AgEEulerOrientationSequence":
        """Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(AgEEulerOrientationSequence) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetSequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Sequence.setter
    def Sequence(self, ppVal:"AgEEulerOrientationSequence") -> None:
        with agmarshall.AgEnum_arg(AgEEulerOrientationSequence, ppVal) as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_SetSequence"](arg_ppVal.COM_val))

    @property
    def A(self) -> typing.Any:
        """Euler A angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetA"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @A.setter
    def A(self, va:typing.Any) -> None:
        with agmarshall.VARIANT_arg(va) as arg_va:
            agcls.evaluate_hresult(self.__dict__["_SetA"](arg_va.COM_val))

    @property
    def B(self) -> typing.Any:
        """Euler b angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetB"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @B.setter
    def B(self, vb:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vb) as arg_vb:
            agcls.evaluate_hresult(self.__dict__["_SetB"](arg_vb.COM_val))

    @property
    def C(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetC"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @C.setter
    def C(self, vc:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vc) as arg_vc:
            agcls.evaluate_hresult(self.__dict__["_SetC"](arg_vc.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{4204C7E1-EC21-40AD-A905-BB35A3FDF7BD}", IAgOrientationEulerAngles)
agcls.AgTypeNameMap["IAgOrientationEulerAngles"] = IAgOrientationEulerAngles
__all__.append("IAgOrientationEulerAngles")

class IAgOrientationQuaternion(IAgOrientation):
    """Interface for Quaternion orientation method."""
    _uuid = "{101FAC5C-8DDB-4D4F-9C73-58146CA8EB01}"
    _num_methods = 8
    _vtable_offset = IAgOrientation._vtable_offset + IAgOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetQX"] = _raise_uninitialized_error
        self.__dict__["_SetQX"] = _raise_uninitialized_error
        self.__dict__["_GetQY"] = _raise_uninitialized_error
        self.__dict__["_SetQY"] = _raise_uninitialized_error
        self.__dict__["_GetQZ"] = _raise_uninitialized_error
        self.__dict__["_SetQZ"] = _raise_uninitialized_error
        self.__dict__["_GetQS"] = _raise_uninitialized_error
        self.__dict__["_SetQS"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgOrientationQuaternion._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgOrientationQuaternion from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientation._private_init(self, pUnk)
        IID_IAgOrientationQuaternion = agcom.GUID(IAgOrientationQuaternion._uuid)
        vtable_offset_local = IAgOrientationQuaternion._vtable_offset - 1
        self.__dict__["_GetQX"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_SetQX"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_GetQY"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_SetQY"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_GetQZ"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetQZ"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__["_GetQS"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_SetQS"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationQuaternion, vtable_offset_local+8, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgOrientationQuaternion.__dict__ and type(IAgOrientationQuaternion.__dict__[attrname]) == property:
            return IAgOrientationQuaternion.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgOrientation.__setattr__(self, attrname, value)
    
    @property
    def QX(self) -> float:
        """The first element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QX = nx si..."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetQX"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @QX.setter
    def QX(self, vQX:float) -> None:
        with agmarshall.DOUBLE_arg(vQX) as arg_vQX:
            agcls.evaluate_hresult(self.__dict__["_SetQX"](arg_vQX.COM_val))

    @property
    def QY(self) -> float:
        """The second element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QY = ny s..."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetQY"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @QY.setter
    def QY(self, vQY:float) -> None:
        with agmarshall.DOUBLE_arg(vQY) as arg_vQY:
            agcls.evaluate_hresult(self.__dict__["_SetQY"](arg_vQY.COM_val))

    @property
    def QZ(self) -> float:
        """The third element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QZ = nz si..."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetQZ"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @QZ.setter
    def QZ(self, vQZ:float) -> None:
        with agmarshall.DOUBLE_arg(vQZ) as arg_vQZ:
            agcls.evaluate_hresult(self.__dict__["_SetQZ"](arg_vQZ.COM_val))

    @property
    def QS(self) -> float:
        """The scalar component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QS = cos(A/2). Dimensionless."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetQS"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @QS.setter
    def QS(self, vQS:float) -> None:
        with agmarshall.DOUBLE_arg(vQS) as arg_vQS:
            agcls.evaluate_hresult(self.__dict__["_SetQS"](arg_vQS.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{101FAC5C-8DDB-4D4F-9C73-58146CA8EB01}", IAgOrientationQuaternion)
agcls.AgTypeNameMap["IAgOrientationQuaternion"] = IAgOrientationQuaternion
__all__.append("IAgOrientationQuaternion")

class IAgOrientationYPRAngles(IAgOrientation):
    """Interface for Yaw-Pitch Roll (YPR) Angles orientation system."""
    _uuid = "{97A9D45D-E718-41FC-ACD2-CEBBEFD2011B}"
    _num_methods = 8
    _vtable_offset = IAgOrientation._vtable_offset + IAgOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetSequence"] = _raise_uninitialized_error
        self.__dict__["_SetSequence"] = _raise_uninitialized_error
        self.__dict__["_GetYaw"] = _raise_uninitialized_error
        self.__dict__["_SetYaw"] = _raise_uninitialized_error
        self.__dict__["_GetPitch"] = _raise_uninitialized_error
        self.__dict__["_SetPitch"] = _raise_uninitialized_error
        self.__dict__["_GetRoll"] = _raise_uninitialized_error
        self.__dict__["_SetRoll"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgOrientationYPRAngles._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgOrientationYPRAngles from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientation._private_init(self, pUnk)
        IID_IAgOrientationYPRAngles = agcom.GUID(IAgOrientationYPRAngles._uuid)
        vtable_offset_local = IAgOrientationYPRAngles._vtable_offset - 1
        self.__dict__["_GetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_SetSequence"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+2, agcom.LONG)
        self.__dict__["_GetYaw"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetYaw"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetPitch"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_SetPitch"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+6, agcom.VARIANT)
        self.__dict__["_GetRoll"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+7, POINTER(agcom.VARIANT))
        self.__dict__["_SetRoll"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationYPRAngles, vtable_offset_local+8, agcom.VARIANT)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgOrientationYPRAngles.__dict__ and type(IAgOrientationYPRAngles.__dict__[attrname]) == property:
            return IAgOrientationYPRAngles.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgOrientation.__setattr__(self, attrname, value)
    
    @property
    def Sequence(self) -> "AgEYPRAnglesSequence":
        """YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(AgEYPRAnglesSequence) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetSequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Sequence.setter
    def Sequence(self, sequence:"AgEYPRAnglesSequence") -> None:
        with agmarshall.AgEnum_arg(AgEYPRAnglesSequence, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_SetSequence"](arg_sequence.COM_val))

    @property
    def Yaw(self) -> typing.Any:
        """Yaw angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetYaw"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Yaw.setter
    def Yaw(self, vYaw:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vYaw) as arg_vYaw:
            agcls.evaluate_hresult(self.__dict__["_SetYaw"](arg_vYaw.COM_val))

    @property
    def Pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPitch"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Pitch.setter
    def Pitch(self, vPitch:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vPitch) as arg_vPitch:
            agcls.evaluate_hresult(self.__dict__["_SetPitch"](arg_vPitch.COM_val))

    @property
    def Roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetRoll"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Roll.setter
    def Roll(self, vRoll:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vRoll) as arg_vRoll:
            agcls.evaluate_hresult(self.__dict__["_SetRoll"](arg_vRoll.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{97A9D45D-E718-41FC-ACD2-CEBBEFD2011B}", IAgOrientationYPRAngles)
agcls.AgTypeNameMap["IAgOrientationYPRAngles"] = IAgOrientationYPRAngles
__all__.append("IAgOrientationYPRAngles")

class IAgOrientationPositionOffset(object):
    """Interface for defining the orientation origin position offset relative to the parent object."""
    _uuid = "{0DDA686C-559C-4BEA-969B-BF40708242B6}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetPositionOffset"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgOrientationPositionOffset._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgOrientationPositionOffset from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgOrientationPositionOffset = agcom.GUID(IAgOrientationPositionOffset._uuid)
        vtable_offset_local = IAgOrientationPositionOffset._vtable_offset - 1
        self.__dict__["_GetPositionOffset"] = IAGFUNCTYPE(pUnk, IID_IAgOrientationPositionOffset, vtable_offset_local+1, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgOrientationPositionOffset.__dict__ and type(IAgOrientationPositionOffset.__dict__[attrname]) == property:
            return IAgOrientationPositionOffset.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgOrientationPositionOffset.")
    
    @property
    def PositionOffset(self) -> "IAgCartesian3Vector":
        """Gets or sets the position offset cartesian vector."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetPositionOffset"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{0DDA686C-559C-4BEA-969B-BF40708242B6}", IAgOrientationPositionOffset)
agcls.AgTypeNameMap["IAgOrientationPositionOffset"] = IAgOrientationPositionOffset
__all__.append("IAgOrientationPositionOffset")

class IAgOrbitState(object):
    """Interface to set and retrieve the coordinate type used to specify the orbit state."""
    _uuid = "{42342AD2-F6C5-426B-AB2A-3688F05353C8}"
    _num_methods = 13
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ConvertTo"] = _raise_uninitialized_error
        self.__dict__["_GetOrbitStateType"] = _raise_uninitialized_error
        self.__dict__["_Assign"] = _raise_uninitialized_error
        self.__dict__["_AssignClassical"] = _raise_uninitialized_error
        self.__dict__["_AssignCartesian"] = _raise_uninitialized_error
        self.__dict__["_AssignGeodetic"] = _raise_uninitialized_error
        self.__dict__["_AssignEquinoctialPosigrade"] = _raise_uninitialized_error
        self.__dict__["_AssignEquinoctialRetrograde"] = _raise_uninitialized_error
        self.__dict__["_AssignMixedSpherical"] = _raise_uninitialized_error
        self.__dict__["_AssignSpherical"] = _raise_uninitialized_error
        self.__dict__["_GetCentralBodyName"] = _raise_uninitialized_error
        self.__dict__["_GetEpoch"] = _raise_uninitialized_error
        self.__dict__["_SetEpoch"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgOrbitState._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgOrbitState from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgOrbitState = agcom.GUID(IAgOrbitState._uuid)
        vtable_offset_local = IAgOrbitState._vtable_offset - 1
        self.__dict__["_ConvertTo"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_GetOrbitStateType"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Assign"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_AssignClassical"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+4, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignCartesian"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+5, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignGeodetic"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+6, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignEquinoctialPosigrade"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+7, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignEquinoctialRetrograde"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+8, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignMixedSpherical"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+9, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_AssignSpherical"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+10, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_GetCentralBodyName"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+11, POINTER(agcom.BSTR))
        self.__dict__["_GetEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+12, POINTER(agcom.VARIANT))
        self.__dict__["_SetEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgOrbitState, vtable_offset_local+13, agcom.VARIANT)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgOrbitState.__dict__ and type(IAgOrbitState.__dict__[attrname]) == property:
            return IAgOrbitState.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgOrbitState.")
    
    def ConvertTo(self, type:"AgEOrbitStateType") -> "IAgOrbitState":
        """Method to changes the coordinate type to the type specified."""
        with agmarshall.AgEnum_arg(AgEOrbitStateType, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgOrbitState:
            agcls.evaluate_hresult(self.__dict__["_ConvertTo"](arg_type.COM_val, byref(arg_ppIAgOrbitState.COM_val)))
            return arg_ppIAgOrbitState.python_val

    @property
    def OrbitStateType(self) -> "AgEOrbitStateType":
        """Returns the coordinate type currently being used."""
        with agmarshall.AgEnum_arg(AgEOrbitStateType) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_GetOrbitStateType"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def Assign(self, pOrbitState:"IAgOrbitState") -> None:
        """Assign a new coordinate type."""
        with agmarshall.AgInterface_in_arg(pOrbitState, IAgOrbitState) as arg_pOrbitState:
            agcls.evaluate_hresult(self.__dict__["_Assign"](arg_pOrbitState.COM_val))

    def AssignClassical(self, eCoordinateSystem:"AgECoordinateSystem", semiMajorAxis:float, eccentricity:float, inclination:float, argOfPerigee:float, rAAN:float, meanAnomaly:float) -> None:
        """Helper method to assign a new orbit state using Classical representation"""
        with agmarshall.AgEnum_arg(AgECoordinateSystem, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(semiMajorAxis) as arg_semiMajorAxis, \
             agmarshall.DOUBLE_arg(eccentricity) as arg_eccentricity, \
             agmarshall.DOUBLE_arg(inclination) as arg_inclination, \
             agmarshall.DOUBLE_arg(argOfPerigee) as arg_argOfPerigee, \
             agmarshall.DOUBLE_arg(rAAN) as arg_rAAN, \
             agmarshall.DOUBLE_arg(meanAnomaly) as arg_meanAnomaly:
            agcls.evaluate_hresult(self.__dict__["_AssignClassical"](arg_eCoordinateSystem.COM_val, arg_semiMajorAxis.COM_val, arg_eccentricity.COM_val, arg_inclination.COM_val, arg_argOfPerigee.COM_val, arg_rAAN.COM_val, arg_meanAnomaly.COM_val))

    def AssignCartesian(self, eCoordinateSystem:"AgECoordinateSystem", xPosition:float, yPosition:float, zPosition:float, xVelocity:float, yVelocity:float, zVelocity:float) -> None:
        """Helper method to assign a new orbit state using Cartesian representation"""
        with agmarshall.AgEnum_arg(AgECoordinateSystem, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(xPosition) as arg_xPosition, \
             agmarshall.DOUBLE_arg(yPosition) as arg_yPosition, \
             agmarshall.DOUBLE_arg(zPosition) as arg_zPosition, \
             agmarshall.DOUBLE_arg(xVelocity) as arg_xVelocity, \
             agmarshall.DOUBLE_arg(yVelocity) as arg_yVelocity, \
             agmarshall.DOUBLE_arg(zVelocity) as arg_zVelocity:
            agcls.evaluate_hresult(self.__dict__["_AssignCartesian"](arg_eCoordinateSystem.COM_val, arg_xPosition.COM_val, arg_yPosition.COM_val, arg_zPosition.COM_val, arg_xVelocity.COM_val, arg_yVelocity.COM_val, arg_zVelocity.COM_val))

    def AssignGeodetic(self, eCoordinateSystem:"AgECoordinateSystem", latitude:float, longitude:float, altitude:float, latitudeRate:float, longitudeRate:float, altitudeRate:float) -> None:
        """Helper method to assign a new orbit state using Geodetic representation"""
        with agmarshall.AgEnum_arg(AgECoordinateSystem, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg(altitude) as arg_altitude, \
             agmarshall.DOUBLE_arg(latitudeRate) as arg_latitudeRate, \
             agmarshall.DOUBLE_arg(longitudeRate) as arg_longitudeRate, \
             agmarshall.DOUBLE_arg(altitudeRate) as arg_altitudeRate:
            agcls.evaluate_hresult(self.__dict__["_AssignGeodetic"](arg_eCoordinateSystem.COM_val, arg_latitude.COM_val, arg_longitude.COM_val, arg_altitude.COM_val, arg_latitudeRate.COM_val, arg_longitudeRate.COM_val, arg_altitudeRate.COM_val))

    def AssignEquinoctialPosigrade(self, eCoordinateSystem:"AgECoordinateSystem", semiMajorAxis:float, h:float, k:float, p:float, q:float, meanLon:float) -> None:
        """Helper method to assign a new orbit state using Equinoctial representation"""
        with agmarshall.AgEnum_arg(AgECoordinateSystem, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(semiMajorAxis) as arg_semiMajorAxis, \
             agmarshall.DOUBLE_arg(h) as arg_h, \
             agmarshall.DOUBLE_arg(k) as arg_k, \
             agmarshall.DOUBLE_arg(p) as arg_p, \
             agmarshall.DOUBLE_arg(q) as arg_q, \
             agmarshall.DOUBLE_arg(meanLon) as arg_meanLon:
            agcls.evaluate_hresult(self.__dict__["_AssignEquinoctialPosigrade"](arg_eCoordinateSystem.COM_val, arg_semiMajorAxis.COM_val, arg_h.COM_val, arg_k.COM_val, arg_p.COM_val, arg_q.COM_val, arg_meanLon.COM_val))

    def AssignEquinoctialRetrograde(self, eCoordinateSystem:"AgECoordinateSystem", semiMajorAxis:float, h:float, k:float, p:float, q:float, meanLon:float) -> None:
        """Helper method to assign a new orbit state using Equinoctial representation"""
        with agmarshall.AgEnum_arg(AgECoordinateSystem, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(semiMajorAxis) as arg_semiMajorAxis, \
             agmarshall.DOUBLE_arg(h) as arg_h, \
             agmarshall.DOUBLE_arg(k) as arg_k, \
             agmarshall.DOUBLE_arg(p) as arg_p, \
             agmarshall.DOUBLE_arg(q) as arg_q, \
             agmarshall.DOUBLE_arg(meanLon) as arg_meanLon:
            agcls.evaluate_hresult(self.__dict__["_AssignEquinoctialRetrograde"](arg_eCoordinateSystem.COM_val, arg_semiMajorAxis.COM_val, arg_h.COM_val, arg_k.COM_val, arg_p.COM_val, arg_q.COM_val, arg_meanLon.COM_val))

    def AssignMixedSpherical(self, eCoordinateSystem:"AgECoordinateSystem", latitude:float, longitude:float, altitude:float, horFlightPathAngle:float, flightPathAzimuth:float, velocity:float) -> None:
        """Helper method to assign a new orbit state using Mixed Spherical representation"""
        with agmarshall.AgEnum_arg(AgECoordinateSystem, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg(altitude) as arg_altitude, \
             agmarshall.DOUBLE_arg(horFlightPathAngle) as arg_horFlightPathAngle, \
             agmarshall.DOUBLE_arg(flightPathAzimuth) as arg_flightPathAzimuth, \
             agmarshall.DOUBLE_arg(velocity) as arg_velocity:
            agcls.evaluate_hresult(self.__dict__["_AssignMixedSpherical"](arg_eCoordinateSystem.COM_val, arg_latitude.COM_val, arg_longitude.COM_val, arg_altitude.COM_val, arg_horFlightPathAngle.COM_val, arg_flightPathAzimuth.COM_val, arg_velocity.COM_val))

    def AssignSpherical(self, eCoordinateSystem:"AgECoordinateSystem", rightAscension:float, declination:float, radius:float, horFlightPathAngle:float, flightPathAzimuth:float, velocity:float) -> None:
        """Helper method to assign a new orbit state using Spherical representation"""
        with agmarshall.AgEnum_arg(AgECoordinateSystem, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(rightAscension) as arg_rightAscension, \
             agmarshall.DOUBLE_arg(declination) as arg_declination, \
             agmarshall.DOUBLE_arg(radius) as arg_radius, \
             agmarshall.DOUBLE_arg(horFlightPathAngle) as arg_horFlightPathAngle, \
             agmarshall.DOUBLE_arg(flightPathAzimuth) as arg_flightPathAzimuth, \
             agmarshall.DOUBLE_arg(velocity) as arg_velocity:
            agcls.evaluate_hresult(self.__dict__["_AssignSpherical"](arg_eCoordinateSystem.COM_val, arg_rightAscension.COM_val, arg_declination.COM_val, arg_radius.COM_val, arg_horFlightPathAngle.COM_val, arg_flightPathAzimuth.COM_val, arg_velocity.COM_val))

    @property
    def CentralBodyName(self) -> str:
        """Gets the central body."""
        with agmarshall.BSTR_arg() as arg_pCBName:
            agcls.evaluate_hresult(self.__dict__["_GetCentralBodyName"](byref(arg_pCBName.COM_val)))
            return arg_pCBName.python_val

    @property
    def Epoch(self) -> typing.Any:
        """The state epoch"""
        with agmarshall.VARIANT_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetEpoch"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @Epoch.setter
    def Epoch(self, epoch:typing.Any) -> None:
        with agmarshall.VARIANT_arg(epoch) as arg_epoch:
            agcls.evaluate_hresult(self.__dict__["_SetEpoch"](arg_epoch.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{42342AD2-F6C5-426B-AB2A-3688F05353C8}", IAgOrbitState)
agcls.AgTypeNameMap["IAgOrbitState"] = IAgOrbitState
__all__.append("IAgOrbitState")

class IAgCartesian2Vector(object):
    """Represents a cartesian 2-D vector."""
    _uuid = "{DA459BD7-5810-4B30-8397-21EDA9E52D2B}"
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetX"] = _raise_uninitialized_error
        self.__dict__["_SetX"] = _raise_uninitialized_error
        self.__dict__["_GetY"] = _raise_uninitialized_error
        self.__dict__["_SetY"] = _raise_uninitialized_error
        self.__dict__["_Get"] = _raise_uninitialized_error
        self.__dict__["_Set"] = _raise_uninitialized_error
        self.__dict__["_ToArray"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgCartesian2Vector._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgCartesian2Vector from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgCartesian2Vector = agcom.GUID(IAgCartesian2Vector._uuid)
        vtable_offset_local = IAgCartesian2Vector._vtable_offset - 1
        self.__dict__["_GetX"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian2Vector, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_SetX"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian2Vector, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_GetY"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian2Vector, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_SetY"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian2Vector, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_Get"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian2Vector, vtable_offset_local+5, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_Set"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian2Vector, vtable_offset_local+6, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_ToArray"] = IAGFUNCTYPE(pUnk, IID_IAgCartesian2Vector, vtable_offset_local+7, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgCartesian2Vector.__dict__ and type(IAgCartesian2Vector.__dict__[attrname]) == property:
            return IAgCartesian2Vector.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgCartesian2Vector.")
    
    @property
    def X(self) -> float:
        """X coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetX"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @X.setter
    def X(self, x:float) -> None:
        with agmarshall.DOUBLE_arg(x) as arg_x:
            agcls.evaluate_hresult(self.__dict__["_SetX"](arg_x.COM_val))

    @property
    def Y(self) -> float:
        """Y coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetY"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @Y.setter
    def Y(self, y:float) -> None:
        with agmarshall.DOUBLE_arg(y) as arg_y:
            agcls.evaluate_hresult(self.__dict__["_SetY"](arg_y.COM_val))

    def Get(self) -> typing.Tuple[float, float]:
        """Returns cartesian vector"""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y:
            agcls.evaluate_hresult(self.__dict__["_Get"](byref(arg_x.COM_val), byref(arg_y.COM_val)))
            return arg_x.python_val, arg_y.python_val

    def Set(self, x:float, y:float) -> None:
        """Sets cartesian vector"""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y:
            agcls.evaluate_hresult(self.__dict__["_Set"](arg_x.COM_val, arg_y.COM_val))

    def ToArray(self) -> list:
        """Returns coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_ToArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{DA459BD7-5810-4B30-8397-21EDA9E52D2B}", IAgCartesian2Vector)
agcls.AgTypeNameMap["IAgCartesian2Vector"] = IAgCartesian2Vector
__all__.append("IAgCartesian2Vector")

class IAgUnitPrefsDim(object):
    """Provides info on a Dimension from the global unit table."""
    _uuid = "{AA966FFD-1A99-45D8-9193-C519BBBA99FA}"
    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetId"] = _raise_uninitialized_error
        self.__dict__["_GetName"] = _raise_uninitialized_error
        self.__dict__["_GetAvailableUnits"] = _raise_uninitialized_error
        self.__dict__["_GetCurrentUnit"] = _raise_uninitialized_error
        self.__dict__["_SetCurrentUnit"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUnitPrefsDim._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUnitPrefsDim from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUnitPrefsDim = agcom.GUID(IAgUnitPrefsDim._uuid)
        vtable_offset_local = IAgUnitPrefsDim._vtable_offset - 1
        self.__dict__["_GetId"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDim, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_GetName"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDim, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetAvailableUnits"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDim, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_GetCurrentUnit"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDim, vtable_offset_local+4, POINTER(agcom.PVOID))
        self.__dict__["_SetCurrentUnit"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDim, vtable_offset_local+5, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUnitPrefsDim.__dict__ and type(IAgUnitPrefsDim.__dict__[attrname]) == property:
            return IAgUnitPrefsDim.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUnitPrefsDim.")
    
    @property
    def Id(self) -> int:
        """Returns the ID of the dimension."""
        with agmarshall.LONG_arg() as arg_pId:
            agcls.evaluate_hresult(self.__dict__["_GetId"](byref(arg_pId.COM_val)))
            return arg_pId.python_val

    @property
    def Name(self) -> str:
        """Returns the current Dimension's full name."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_GetName"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def AvailableUnits(self) -> "IAgUnitPrefsUnitCollection":
        """Returns collection of Units."""
        with agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnitCollection:
            agcls.evaluate_hresult(self.__dict__["_GetAvailableUnits"](byref(arg_ppUnitPrefsUnitCollection.COM_val)))
            return arg_ppUnitPrefsUnitCollection.python_val

    @property
    def CurrentUnit(self) -> "IAgUnitPrefsUnit":
        """Returns the current unit for this dimension."""
        with agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_GetCurrentUnit"](byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    def SetCurrentUnit(self, unitAbbrv:str) -> None:
        """Sets the Unit for this simple dimension."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_SetCurrentUnit"](arg_unitAbbrv.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{AA966FFD-1A99-45D8-9193-C519BBBA99FA}", IAgUnitPrefsDim)
agcls.AgTypeNameMap["IAgUnitPrefsDim"] = IAgUnitPrefsDim
__all__.append("IAgUnitPrefsDim")

class IAgPropertyInfo(object):
    """Property information."""
    _uuid = "{26A48B4B-BF6A-4F9D-9658-44A7A2DBBE2A}"
    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetName"] = _raise_uninitialized_error
        self.__dict__["_GetPropertyType"] = _raise_uninitialized_error
        self.__dict__["_GetValue"] = _raise_uninitialized_error
        self.__dict__["_SetValue"] = _raise_uninitialized_error
        self.__dict__["_GetHasMin"] = _raise_uninitialized_error
        self.__dict__["_GetHasMax"] = _raise_uninitialized_error
        self.__dict__["_GetMin"] = _raise_uninitialized_error
        self.__dict__["_GetMax"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPropertyInfo._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPropertyInfo from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgPropertyInfo = agcom.GUID(IAgPropertyInfo._uuid)
        vtable_offset_local = IAgPropertyInfo._vtable_offset - 1
        self.__dict__["_GetName"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetPropertyType"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_GetValue"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_SetValue"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_GetHasMin"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetHasMax"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetMin"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+7, POINTER(agcom.VARIANT))
        self.__dict__["_GetMax"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfo, vtable_offset_local+8, POINTER(agcom.VARIANT))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPropertyInfo.__dict__ and type(IAgPropertyInfo.__dict__[attrname]) == property:
            return IAgPropertyInfo.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgPropertyInfo.")
    
    @property
    def Name(self) -> str:
        """The name of the property."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetName"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def PropertyType(self) -> "AgEPropertyInfoValueType":
        """The type of property."""
        with agmarshall.AgEnum_arg(AgEPropertyInfoValueType) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPropertyType"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def GetValue(self) -> typing.Any:
        """The value of the property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetValue"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetValue(self, propertyInfo:typing.Any) -> None:
        """The value of the property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg(propertyInfo) as arg_propertyInfo:
            agcls.evaluate_hresult(self.__dict__["_SetValue"](arg_propertyInfo.COM_val))

    @property
    def HasMin(self) -> bool:
        """Used to determine if the property has a minimum value."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetHasMin"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def HasMax(self) -> bool:
        """Used to determine if the property has a maximum value."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetHasMax"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Min(self) -> typing.Any:
        """The minimum value of this property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetMin"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Max(self) -> typing.Any:
        """The maximum value of this property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetMax"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{26A48B4B-BF6A-4F9D-9658-44A7A2DBBE2A}", IAgPropertyInfo)
agcls.AgTypeNameMap["IAgPropertyInfo"] = IAgPropertyInfo
__all__.append("IAgPropertyInfo")

class IAgPropertyInfoCollection(object):
    """The collection of properties."""
    _uuid = "{198E6280-1D5A-4AED-9DE3-ACE354B95287}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_GetItemByIndex"] = _raise_uninitialized_error
        self.__dict__["_GetItemByName"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPropertyInfoCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPropertyInfoCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgPropertyInfoCollection = agcom.GUID(IAgPropertyInfoCollection._uuid)
        vtable_offset_local = IAgPropertyInfoCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfoCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfoCollection, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfoCollection, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__["_GetItemByIndex"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfoCollection, vtable_offset_local+4, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByName"] = IAGFUNCTYPE(pUnk, IID_IAgPropertyInfoCollection, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPropertyInfoCollection.__dict__ and type(IAgPropertyInfoCollection.__dict__[attrname]) == property:
            return IAgPropertyInfoCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgPropertyInfoCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgPropertyInfo":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, indexOrName:typing.Any) -> "IAgPropertyInfo":
        """Allows the user to iterate through the properties."""
        with agmarshall.VARIANT_arg(indexOrName) as arg_indexOrName, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_indexOrName.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates through the properties."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    @property
    def Count(self) -> int:
        """The number of properties available."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def GetItemByIndex(self, index:int) -> "IAgPropertyInfo":
        """Retrieve a property from the collection by Index."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetItemByIndex"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def GetItemByName(self, name:str) -> "IAgPropertyInfo":
        """Retrieve a property from the collection by Name."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetItemByName"](arg_name.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{198E6280-1D5A-4AED-9DE3-ACE354B95287}", IAgPropertyInfoCollection)
agcls.AgTypeNameMap["IAgPropertyInfoCollection"] = IAgPropertyInfoCollection
__all__.append("IAgPropertyInfoCollection")

class IAgRuntimeTypeInfo(object):
    """Interface used to retrieve the properties at runtime."""
    _uuid = "{01F8872C-9586-4131-A724-F97C6ADD083F}"
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetProperties"] = _raise_uninitialized_error
        self.__dict__["_GetIsCollection"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_GetItem"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgRuntimeTypeInfo._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgRuntimeTypeInfo from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgRuntimeTypeInfo = agcom.GUID(IAgRuntimeTypeInfo._uuid)
        vtable_offset_local = IAgRuntimeTypeInfo._vtable_offset - 1
        self.__dict__["_GetProperties"] = IAGFUNCTYPE(pUnk, IID_IAgRuntimeTypeInfo, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_GetIsCollection"] = IAGFUNCTYPE(pUnk, IID_IAgRuntimeTypeInfo, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgRuntimeTypeInfo, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__["_GetItem"] = IAGFUNCTYPE(pUnk, IID_IAgRuntimeTypeInfo, vtable_offset_local+4, agcom.LONG, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgRuntimeTypeInfo.__dict__ and type(IAgRuntimeTypeInfo.__dict__[attrname]) == property:
            return IAgRuntimeTypeInfo.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgRuntimeTypeInfo.")
    
    @property
    def Properties(self) -> "IAgPropertyInfoCollection":
        """The collection of properties."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetProperties"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    @property
    def IsCollection(self) -> bool:
        """Determines if the interface is a collection."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetIsCollection"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Count(self) -> int:
        """If the interface is a collection, returns the collection count."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def GetItem(self, index:int) -> "IAgPropertyInfo":
        """Returns the property of the collection at the given index."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetItem"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{01F8872C-9586-4131-A724-F97C6ADD083F}", IAgRuntimeTypeInfo)
agcls.AgTypeNameMap["IAgRuntimeTypeInfo"] = IAgRuntimeTypeInfo
__all__.append("IAgRuntimeTypeInfo")

class IAgRuntimeTypeInfoProvider(object):
    """Access point for IAgRuntimeTypeInfo."""
    _uuid = "{E9AD01B5-7892-4367-8EC7-60EA26CE0E11}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetProvideRuntimeTypeInfo"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgRuntimeTypeInfoProvider._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgRuntimeTypeInfoProvider from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgRuntimeTypeInfoProvider = agcom.GUID(IAgRuntimeTypeInfoProvider._uuid)
        vtable_offset_local = IAgRuntimeTypeInfoProvider._vtable_offset - 1
        self.__dict__["_GetProvideRuntimeTypeInfo"] = IAGFUNCTYPE(pUnk, IID_IAgRuntimeTypeInfoProvider, vtable_offset_local+1, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgRuntimeTypeInfoProvider.__dict__ and type(IAgRuntimeTypeInfoProvider.__dict__[attrname]) == property:
            return IAgRuntimeTypeInfoProvider.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgRuntimeTypeInfoProvider.")
    
    @property
    def ProvideRuntimeTypeInfo(self) -> "IAgRuntimeTypeInfo":
        """Returns the IAgRuntimeTypeInfo interface to access properties at runtime."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetProvideRuntimeTypeInfo"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{E9AD01B5-7892-4367-8EC7-60EA26CE0E11}", IAgRuntimeTypeInfoProvider)
agcls.AgTypeNameMap["IAgRuntimeTypeInfoProvider"] = IAgRuntimeTypeInfoProvider
__all__.append("IAgRuntimeTypeInfoProvider")

class IAgExecCmdResult(object):
    """Collection of strings returned by the ExecuteCommand."""
    _uuid = "{CC5C63BC-FF0A-4CC8-AD58-5A8D11DD9C60}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Range"] = _raise_uninitialized_error
        self.__dict__["_GetIsSucceeded"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgExecCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgExecCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgExecCmdResult = agcom.GUID(IAgExecCmdResult._uuid)
        vtable_offset_local = IAgExecCmdResult._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_Range"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+4, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetIsSucceeded"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgExecCmdResult.__dict__ and type(IAgExecCmdResult.__dict__[attrname]) == property:
            return IAgExecCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgExecCmdResult.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> str:
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    @property
    def Count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def Item(self, index:int) -> str:
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pItem:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pItem.COM_val)))
            return arg_pItem.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the strings in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    def Range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        with agmarshall.LONG_arg(startIndex) as arg_startIndex, \
             agmarshall.LONG_arg(stopIndex) as arg_stopIndex, \
             agmarshall.SAFEARRAY_arg() as arg_ppVar:
            agcls.evaluate_hresult(self.__dict__["_Range"](arg_startIndex.COM_val, arg_stopIndex.COM_val, byref(arg_ppVar.COM_val)))
            return arg_ppVar.python_val

    @property
    def IsSucceeded(self) -> bool:
        """Indicates whether the object contains valid results."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetIsSucceeded"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{CC5C63BC-FF0A-4CC8-AD58-5A8D11DD9C60}", IAgExecCmdResult)
agcls.AgTypeNameMap["IAgExecCmdResult"] = IAgExecCmdResult
__all__.append("IAgExecCmdResult")

class IAgExecMultiCmdResult(object):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    _uuid = "{ECEFEE1C-F623-4926-A738-3D95FC5E3DEE}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgExecMultiCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgExecMultiCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgExecMultiCmdResult = agcom.GUID(IAgExecMultiCmdResult._uuid)
        vtable_offset_local = IAgExecMultiCmdResult._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgExecMultiCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgExecMultiCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgExecMultiCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgExecMultiCmdResult.__dict__ and type(IAgExecMultiCmdResult.__dict__[attrname]) == property:
            return IAgExecMultiCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgExecMultiCmdResult.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgExecCmdResult":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    @property
    def Count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def Item(self, index:int) -> "IAgExecCmdResult":
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the objects in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{ECEFEE1C-F623-4926-A738-3D95FC5E3DEE}", IAgExecMultiCmdResult)
agcls.AgTypeNameMap["IAgExecMultiCmdResult"] = IAgExecMultiCmdResult
__all__.append("IAgExecMultiCmdResult")

class IAgUnitPrefsUnit(object):
    """Provides info about a unit."""
    _uuid = "{4B4E2F51-280F-4E35-AEA5-71CDAC7342C4}"
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFullName"] = _raise_uninitialized_error
        self.__dict__["_GetAbbrv"] = _raise_uninitialized_error
        self.__dict__["_GetId"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUnitPrefsUnit._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUnitPrefsUnit from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUnitPrefsUnit = agcom.GUID(IAgUnitPrefsUnit._uuid)
        vtable_offset_local = IAgUnitPrefsUnit._vtable_offset - 1
        self.__dict__["_GetFullName"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnit, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetAbbrv"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnit, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetId"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnit, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnit, vtable_offset_local+4, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUnitPrefsUnit.__dict__ and type(IAgUnitPrefsUnit.__dict__[attrname]) == property:
            return IAgUnitPrefsUnit.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUnitPrefsUnit.")
    
    @property
    def FullName(self) -> str:
        """Returns the fullname of the unit."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_GetFullName"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def Abbrv(self) -> str:
        """Returns the abbreviation of the unit."""
        with agmarshall.BSTR_arg() as arg_pAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetAbbrv"](byref(arg_pAbbrv.COM_val)))
            return arg_pAbbrv.python_val

    @property
    def Id(self) -> int:
        """Returns the ID of the unit."""
        with agmarshall.LONG_arg() as arg_pId:
            agcls.evaluate_hresult(self.__dict__["_GetId"](byref(arg_pId.COM_val)))
            return arg_pId.python_val

    @property
    def Dimension(self) -> "IAgUnitPrefsDim":
        """Returns the Dimension for this unit."""
        with agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_ppUnitPrefsDim.COM_val)))
            return arg_ppUnitPrefsDim.python_val


agcls.AgClassCatalog.add_catalog_entry("{4B4E2F51-280F-4E35-AEA5-71CDAC7342C4}", IAgUnitPrefsUnit)
agcls.AgTypeNameMap["IAgUnitPrefsUnit"] = IAgUnitPrefsUnit
__all__.append("IAgUnitPrefsUnit")

class IAgUnitPrefsUnitCollection(object):
    """Provides access to the Unit collection."""
    _uuid = "{C9A263F5-A021-4BEC-85F3-526FA41F1CB4}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_GetItemByIndex"] = _raise_uninitialized_error
        self.__dict__["_GetItemByName"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUnitPrefsUnitCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUnitPrefsUnitCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUnitPrefsUnitCollection = agcom.GUID(IAgUnitPrefsUnitCollection._uuid)
        vtable_offset_local = IAgUnitPrefsUnitCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnitCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnitCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnitCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByIndex"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnitCollection, vtable_offset_local+4, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByName"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsUnitCollection, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUnitPrefsUnitCollection.__dict__ and type(IAgUnitPrefsUnitCollection.__dict__[attrname]) == property:
            return IAgUnitPrefsUnitCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUnitPrefsUnitCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgUnitPrefsUnit":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, indexOrName:typing.Any) -> "IAgUnitPrefsUnit":
        """Returns the specific item in the collection given a unit identifier or an index."""
        with agmarshall.VARIANT_arg(indexOrName) as arg_indexOrName, \
             agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_indexOrName.COM_val, byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    @property
    def Count(self) -> int:
        """Returns the number of items in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an enumeration of AgUnitPrefsUnit."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def GetItemByIndex(self, index:int) -> "IAgUnitPrefsUnit":
        """Returns the specific item in the collection given an index."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_GetItemByIndex"](arg_index.COM_val, byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    def GetItemByName(self, name:str) -> "IAgUnitPrefsUnit":
        """Returns the specific item in the collection given a unit identifier."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_GetItemByName"](arg_name.COM_val, byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{C9A263F5-A021-4BEC-85F3-526FA41F1CB4}", IAgUnitPrefsUnitCollection)
agcls.AgTypeNameMap["IAgUnitPrefsUnitCollection"] = IAgUnitPrefsUnitCollection
__all__.append("IAgUnitPrefsUnitCollection")

class IAgUnitPrefsDimCollection(object):
    """Provides accesses to the global unit table."""
    _uuid = "{40AE1C29-E5F5-426A-AEB7-D02CC7D2873C}"
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_SetCurrentUnit"] = _raise_uninitialized_error
        self.__dict__["_GetCurrentUnitAbbrv"] = _raise_uninitialized_error
        self.__dict__["_GetMissionElapsedTime"] = _raise_uninitialized_error
        self.__dict__["_SetMissionElapsedTime"] = _raise_uninitialized_error
        self.__dict__["_GetJulianDateOffset"] = _raise_uninitialized_error
        self.__dict__["_SetJulianDateOffset"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_ResetUnits"] = _raise_uninitialized_error
        self.__dict__["_GetItemByIndex"] = _raise_uninitialized_error
        self.__dict__["_GetItemByName"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUnitPrefsDimCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUnitPrefsDimCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUnitPrefsDimCollection = agcom.GUID(IAgUnitPrefsDimCollection._uuid)
        vtable_offset_local = IAgUnitPrefsDimCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_SetCurrentUnit"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+3, agcom.BSTR, agcom.BSTR)
        self.__dict__["_GetCurrentUnitAbbrv"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+4, agcom.VARIANT, POINTER(agcom.BSTR))
        self.__dict__["_GetMissionElapsedTime"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_SetMissionElapsedTime"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+6, agcom.VARIANT)
        self.__dict__["_GetJulianDateOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_SetJulianDateOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+9, POINTER(agcom.PVOID))
        self.__dict__["_ResetUnits"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+10, )
        self.__dict__["_GetItemByIndex"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+11, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByName"] = IAGFUNCTYPE(pUnk, IID_IAgUnitPrefsDimCollection, vtable_offset_local+12, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUnitPrefsDimCollection.__dict__ and type(IAgUnitPrefsDimCollection.__dict__[attrname]) == property:
            return IAgUnitPrefsDimCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUnitPrefsDimCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgUnitPrefsDim":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, indexOrName:typing.Any) -> "IAgUnitPrefsDim":
        """Returns an IAgUnitPrefsDim given a Dimension name or an index."""
        with agmarshall.VARIANT_arg(indexOrName) as arg_indexOrName, \
             agmarshall.AgInterface_out_arg() as arg_ppAgUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_indexOrName.COM_val, byref(arg_ppAgUnitPrefsDim.COM_val)))
            return arg_ppAgUnitPrefsDim.python_val

    @property
    def Count(self) -> int:
        """Returns the number of items in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def SetCurrentUnit(self, dimension:str, unitAbbrv:str) -> None:
        """Returns the Current unit for a Dimension."""
        with agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_SetCurrentUnit"](arg_dimension.COM_val, arg_unitAbbrv.COM_val))

    def GetCurrentUnitAbbrv(self, indexOrDimName:typing.Any) -> str:
        """Returns the Current Unit for a Dimension."""
        with agmarshall.VARIANT_arg(indexOrDimName) as arg_indexOrDimName, \
             agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetCurrentUnitAbbrv"](arg_indexOrDimName.COM_val, byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    @property
    def MissionElapsedTime(self) -> typing.Any:
        """The MissionElapsedTime."""
        with agmarshall.VARIANT_arg() as arg_pMisElapTime:
            agcls.evaluate_hresult(self.__dict__["_GetMissionElapsedTime"](byref(arg_pMisElapTime.COM_val)))
            return arg_pMisElapTime.python_val

    @MissionElapsedTime.setter
    def MissionElapsedTime(self, pMisElapTime:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pMisElapTime) as arg_pMisElapTime:
            agcls.evaluate_hresult(self.__dict__["_SetMissionElapsedTime"](arg_pMisElapTime.COM_val))

    @property
    def JulianDateOffset(self) -> float:
        """The JulianDateOffset."""
        with agmarshall.DOUBLE_arg() as arg_pJDateOffset:
            agcls.evaluate_hresult(self.__dict__["_GetJulianDateOffset"](byref(arg_pJDateOffset.COM_val)))
            return arg_pJDateOffset.python_val

    @JulianDateOffset.setter
    def JulianDateOffset(self, pJDateOffset:float) -> None:
        with agmarshall.DOUBLE_arg(pJDateOffset) as arg_pJDateOffset:
            agcls.evaluate_hresult(self.__dict__["_SetJulianDateOffset"](arg_pJDateOffset.COM_val))

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns a collection of IAgUnitPrefsDim."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def ResetUnits(self) -> None:
        """Resets the unitpreferences to the Default units"""
        agcls.evaluate_hresult(self.__dict__["_ResetUnits"]())

    def GetItemByIndex(self, index:int) -> "IAgUnitPrefsDim":
        """Returns an IAgUnitPrefsDim given an index."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppAgUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_GetItemByIndex"](arg_index.COM_val, byref(arg_ppAgUnitPrefsDim.COM_val)))
            return arg_ppAgUnitPrefsDim.python_val

    def GetItemByName(self, name:str) -> "IAgUnitPrefsDim":
        """Returns an IAgUnitPrefsDim given a Dimension name ."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppAgUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_GetItemByName"](arg_name.COM_val, byref(arg_ppAgUnitPrefsDim.COM_val)))
            return arg_ppAgUnitPrefsDim.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{40AE1C29-E5F5-426A-AEB7-D02CC7D2873C}", IAgUnitPrefsDimCollection)
agcls.AgTypeNameMap["IAgUnitPrefsDimCollection"] = IAgUnitPrefsDimCollection
__all__.append("IAgUnitPrefsDimCollection")

class IAgQuantity(object):
    """Provides helper methods for a quantity."""
    _uuid = "{C0BBB39C-54E2-4344-B24E-58AA6AA4446B}"
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetUnit"] = _raise_uninitialized_error
        self.__dict__["_ConvertToUnit"] = _raise_uninitialized_error
        self.__dict__["_GetValue"] = _raise_uninitialized_error
        self.__dict__["_SetValue"] = _raise_uninitialized_error
        self.__dict__["_Add"] = _raise_uninitialized_error
        self.__dict__["_Subtract"] = _raise_uninitialized_error
        self.__dict__["_MultiplyQty"] = _raise_uninitialized_error
        self.__dict__["_DivideQty"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgQuantity._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgQuantity from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgQuantity = agcom.GUID(IAgQuantity._uuid)
        vtable_offset_local = IAgQuantity._vtable_offset - 1
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetUnit"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_ConvertToUnit"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+3, agcom.BSTR)
        self.__dict__["_GetValue"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_SetValue"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+5, agcom.DOUBLE)
        self.__dict__["_Add"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_Subtract"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+7, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_MultiplyQty"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+8, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_DivideQty"] = IAGFUNCTYPE(pUnk, IID_IAgQuantity, vtable_offset_local+9, agcom.PVOID, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgQuantity.__dict__ and type(IAgQuantity.__dict__[attrname]) == property:
            return IAgQuantity.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgQuantity.")
    
    @property
    def Dimension(self) -> str:
        """Gets the name of the dimension"""
        with agmarshall.BSTR_arg() as arg_pDimName:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimName.COM_val)))
            return arg_pDimName.python_val

    @property
    def Unit(self) -> str:
        """The current Unit abbreviation."""
        with agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_GetUnit"](byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    def ConvertToUnit(self, unitAbbrv:str) -> None:
        """Changes the value in this quantity to the specified unit."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_ConvertToUnit"](arg_unitAbbrv.COM_val))

    @property
    def Value(self) -> float:
        """The current value."""
        with agmarshall.DOUBLE_arg() as arg_pValue:
            agcls.evaluate_hresult(self.__dict__["_GetValue"](byref(arg_pValue.COM_val)))
            return arg_pValue.python_val

    @Value.setter
    def Value(self, value:float) -> None:
        with agmarshall.DOUBLE_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_SetValue"](arg_value.COM_val))

    def Add(self, quantity:"IAgQuantity") -> "IAgQuantity":
        """Adds the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IAgQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_Add"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def Subtract(self, quantity:"IAgQuantity") -> "IAgQuantity":
        """Subtracts the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IAgQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_Subtract"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def MultiplyQty(self, quantity:"IAgQuantity") -> "IAgQuantity":
        """Multiplies the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IAgQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_MultiplyQty"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def DivideQty(self, quantity:"IAgQuantity") -> "IAgQuantity":
        """Divides the value from the IAgQuantity interface to this interface. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IAgQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_DivideQty"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val


agcls.AgClassCatalog.add_catalog_entry("{C0BBB39C-54E2-4344-B24E-58AA6AA4446B}", IAgQuantity)
agcls.AgTypeNameMap["IAgQuantity"] = IAgQuantity
__all__.append("IAgQuantity")

class IAgDate(object):
    """Provides helper methods for a date."""
    _uuid = "{BFC8EA09-19BD-432A-923D-C553E8E37993}"
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Format"] = _raise_uninitialized_error
        self.__dict__["_SetDate"] = _raise_uninitialized_error
        self.__dict__["_GetOLEDate"] = _raise_uninitialized_error
        self.__dict__["_SetOLEDate"] = _raise_uninitialized_error
        self.__dict__["_GetWholeDays"] = _raise_uninitialized_error
        self.__dict__["_SetWholeDays"] = _raise_uninitialized_error
        self.__dict__["_GetSecIntoDay"] = _raise_uninitialized_error
        self.__dict__["_SetSecIntoDay"] = _raise_uninitialized_error
        self.__dict__["_GetWholeDaysUTC"] = _raise_uninitialized_error
        self.__dict__["_SetWholeDaysUTC"] = _raise_uninitialized_error
        self.__dict__["_GetSecIntoDayUTC"] = _raise_uninitialized_error
        self.__dict__["_SetSecIntoDayUTC"] = _raise_uninitialized_error
        self.__dict__["_Add"] = _raise_uninitialized_error
        self.__dict__["_Subtract"] = _raise_uninitialized_error
        self.__dict__["_Span"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgDate = agcom.GUID(IAgDate._uuid)
        vtable_offset_local = IAgDate._vtable_offset - 1
        self.__dict__["_Format"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+1, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_SetDate"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+2, agcom.BSTR, agcom.BSTR)
        self.__dict__["_GetOLEDate"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+3, POINTER(agcom.DATE))
        self.__dict__["_SetOLEDate"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+4, agcom.DATE)
        self.__dict__["_GetWholeDays"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_SetWholeDays"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+6, agcom.LONG)
        self.__dict__["_GetSecIntoDay"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_SetSecIntoDay"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__["_GetWholeDaysUTC"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+9, POINTER(agcom.LONG))
        self.__dict__["_SetWholeDaysUTC"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+10, agcom.LONG)
        self.__dict__["_GetSecIntoDayUTC"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__["_SetSecIntoDayUTC"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+12, agcom.DOUBLE)
        self.__dict__["_Add"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+13, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID))
        self.__dict__["_Subtract"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+14, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID))
        self.__dict__["_Span"] = IAGFUNCTYPE(pUnk, IID_IAgDate, vtable_offset_local+15, agcom.PVOID, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDate.__dict__ and type(IAgDate.__dict__[attrname]) == property:
            return IAgDate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgDate.")
    
    def Format(self, unit:str) -> str:
        """Returns the value of the date given the unit."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.BSTR_arg() as arg_pValue:
            agcls.evaluate_hresult(self.__dict__["_Format"](arg_unit.COM_val, byref(arg_pValue.COM_val)))
            return arg_pValue.python_val

    def SetDate(self, unit:str, value:str) -> None:
        """Sets this date with the given date value and unit type."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.BSTR_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_SetDate"](arg_unit.COM_val, arg_value.COM_val))

    @property
    def OLEDate(self) -> datetime:
        """The current time in OLE DATE Format."""
        with agmarshall.DATE_arg() as arg_pDate:
            agcls.evaluate_hresult(self.__dict__["_GetOLEDate"](byref(arg_pDate.COM_val)))
            return arg_pDate.python_val

    @OLEDate.setter
    def OLEDate(self, inVal:datetime) -> None:
        with agmarshall.DATE_arg(inVal) as arg_inVal:
            agcls.evaluate_hresult(self.__dict__["_SetOLEDate"](arg_inVal.COM_val))

    @property
    def WholeDays(self) -> int:
        """The Julian Day Number of the date of interest."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWholeDays"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @WholeDays.setter
    def WholeDays(self, wholeDays:int) -> None:
        with agmarshall.LONG_arg(wholeDays) as arg_wholeDays:
            agcls.evaluate_hresult(self.__dict__["_SetWholeDays"](arg_wholeDays.COM_val))

    @property
    def SecIntoDay(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetSecIntoDay"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @SecIntoDay.setter
    def SecIntoDay(self, secIntoDay:float) -> None:
        with agmarshall.DOUBLE_arg(secIntoDay) as arg_secIntoDay:
            agcls.evaluate_hresult(self.__dict__["_SetSecIntoDay"](arg_secIntoDay.COM_val))

    @property
    def WholeDaysUTC(self) -> int:
        """The UTC Day Number of the date of interest."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWholeDaysUTC"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @WholeDaysUTC.setter
    def WholeDaysUTC(self, wholeDays:int) -> None:
        with agmarshall.LONG_arg(wholeDays) as arg_wholeDays:
            agcls.evaluate_hresult(self.__dict__["_SetWholeDaysUTC"](arg_wholeDays.COM_val))

    @property
    def SecIntoDayUTC(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetSecIntoDayUTC"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @SecIntoDayUTC.setter
    def SecIntoDayUTC(self, secIntoDay:float) -> None:
        with agmarshall.DOUBLE_arg(secIntoDay) as arg_secIntoDay:
            agcls.evaluate_hresult(self.__dict__["_SetSecIntoDayUTC"](arg_secIntoDay.COM_val))

    def Add(self, unit:str, value:float) -> "IAgDate":
        """Adds the value in the given unit and returns a new date interface."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppDate:
            agcls.evaluate_hresult(self.__dict__["_Add"](arg_unit.COM_val, arg_value.COM_val, byref(arg_ppDate.COM_val)))
            return arg_ppDate.python_val

    def Subtract(self, unit:str, value:float) -> "IAgDate":
        """Subtracts the value in the given unit and returns a new date interface."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppDate:
            agcls.evaluate_hresult(self.__dict__["_Subtract"](arg_unit.COM_val, arg_value.COM_val, byref(arg_ppDate.COM_val)))
            return arg_ppDate.python_val

    def Span(self, date:"IAgDate") -> "IAgQuantity":
        """Subtracts the value from the IAgDate interface and returns an IAgQuantity."""
        with agmarshall.AgInterface_in_arg(date, IAgDate) as arg_date, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_Span"](arg_date.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val


agcls.AgClassCatalog.add_catalog_entry("{BFC8EA09-19BD-432A-923D-C553E8E37993}", IAgDate)
agcls.AgTypeNameMap["IAgDate"] = IAgDate
__all__.append("IAgDate")

class IAgConversionUtility(object):
    """Provides conversion utilities."""
    _uuid = "{2B04A4E2-C647-4920-88FF-DE0413252D1C}"
    _num_methods = 18
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ConvertQuantity"] = _raise_uninitialized_error
        self.__dict__["_ConvertDate"] = _raise_uninitialized_error
        self.__dict__["_ConvertQuantityArray"] = _raise_uninitialized_error
        self.__dict__["_ConvertDateArray"] = _raise_uninitialized_error
        self.__dict__["_NewQuantity"] = _raise_uninitialized_error
        self.__dict__["_NewDate"] = _raise_uninitialized_error
        self.__dict__["_NewPositionOnEarth"] = _raise_uninitialized_error
        self.__dict__["_ConvertPositionArray"] = _raise_uninitialized_error
        self.__dict__["_NewDirection"] = _raise_uninitialized_error
        self.__dict__["_NewOrientation"] = _raise_uninitialized_error
        self.__dict__["_NewOrbitStateOnEarth"] = _raise_uninitialized_error
        self.__dict__["_NewPositionOnCB"] = _raise_uninitialized_error
        self.__dict__["_NewOrbitStateOnCB"] = _raise_uninitialized_error
        self.__dict__["_QueryDirectionCosineMatrix"] = _raise_uninitialized_error
        self.__dict__["_QueryDirectionCosineMatrixArray"] = _raise_uninitialized_error
        self.__dict__["_NewCartesian3Vector"] = _raise_uninitialized_error
        self.__dict__["_NewCartesian3VectorFromDirection"] = _raise_uninitialized_error
        self.__dict__["_NewCartesian3VectorFromPosition"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgConversionUtility._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgConversionUtility from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgConversionUtility = agcom.GUID(IAgConversionUtility._uuid)
        vtable_offset_local = IAgConversionUtility._vtable_offset - 1
        self.__dict__["_ConvertQuantity"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+1, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.DOUBLE))
        self.__dict__["_ConvertDate"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+2, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_ConvertQuantityArray"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+3, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.SAFEARRAY), POINTER(agcom.SAFEARRAY))
        self.__dict__["_ConvertDateArray"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+4, agcom.BSTR, agcom.BSTR, POINTER(agcom.SAFEARRAY), POINTER(agcom.SAFEARRAY))
        self.__dict__["_NewQuantity"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+5, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID))
        self.__dict__["_NewDate"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+6, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_NewPositionOnEarth"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+7, POINTER(agcom.PVOID))
        self.__dict__["_ConvertPositionArray"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+8, agcom.LONG, POINTER(agcom.SAFEARRAY), agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_NewDirection"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+9, POINTER(agcom.PVOID))
        self.__dict__["_NewOrientation"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+10, POINTER(agcom.PVOID))
        self.__dict__["_NewOrbitStateOnEarth"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+11, POINTER(agcom.PVOID))
        self.__dict__["_NewPositionOnCB"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+12, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_NewOrbitStateOnCB"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+13, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_QueryDirectionCosineMatrix"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+14, agcom.PVOID, POINTER(agcom.PVOID), POINTER(agcom.PVOID), POINTER(agcom.PVOID))
        self.__dict__["_QueryDirectionCosineMatrixArray"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+15, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_NewCartesian3Vector"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+16, POINTER(agcom.PVOID))
        self.__dict__["_NewCartesian3VectorFromDirection"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+17, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_NewCartesian3VectorFromPosition"] = IAGFUNCTYPE(pUnk, IID_IAgConversionUtility, vtable_offset_local+18, agcom.PVOID, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgConversionUtility.__dict__ and type(IAgConversionUtility.__dict__[attrname]) == property:
            return IAgConversionUtility.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgConversionUtility.")
    
    def ConvertQuantity(self, dimensionName:str, fromUnit:str, toUnit:str, fromValue:float) -> float:
        """Converts the specified quantity value from a given unit to another unit."""
        with agmarshall.BSTR_arg(dimensionName) as arg_dimensionName, \
             agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.DOUBLE_arg(fromValue) as arg_fromValue, \
             agmarshall.DOUBLE_arg() as arg_pToValue:
            agcls.evaluate_hresult(self.__dict__["_ConvertQuantity"](arg_dimensionName.COM_val, arg_fromUnit.COM_val, arg_toUnit.COM_val, arg_fromValue.COM_val, byref(arg_pToValue.COM_val)))
            return arg_pToValue.python_val

    def ConvertDate(self, fromUnit:str, toUnit:str, fromValue:str) -> str:
        """Converts the specified date from a given unit to another unit."""
        with agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.BSTR_arg(fromValue) as arg_fromValue, \
             agmarshall.BSTR_arg() as arg_pToValue:
            agcls.evaluate_hresult(self.__dict__["_ConvertDate"](arg_fromUnit.COM_val, arg_toUnit.COM_val, arg_fromValue.COM_val, byref(arg_pToValue.COM_val)))
            return arg_pToValue.python_val

    def ConvertQuantityArray(self, dimensionName:str, fromUnit:str, toUnit:str, quantityValues:list) -> list:
        """Converts the specified quantity values from a given unit to another unit."""
        with agmarshall.BSTR_arg(dimensionName) as arg_dimensionName, \
             agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.SAFEARRAY_arg(quantityValues) as arg_quantityValues, \
             agmarshall.SAFEARRAY_arg() as arg_ppConvertedQuantityValues:
            agcls.evaluate_hresult(self.__dict__["_ConvertQuantityArray"](arg_dimensionName.COM_val, arg_fromUnit.COM_val, arg_toUnit.COM_val, byref(arg_quantityValues.COM_val), byref(arg_ppConvertedQuantityValues.COM_val)))
            return arg_ppConvertedQuantityValues.python_val

    def ConvertDateArray(self, fromUnit:str, toUnit:str, fromValues:list) -> list:
        """Converts the specified dates from a given unit to another unit."""
        with agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.SAFEARRAY_arg(fromValues) as arg_fromValues, \
             agmarshall.SAFEARRAY_arg() as arg_ppConvertedDateValues:
            agcls.evaluate_hresult(self.__dict__["_ConvertDateArray"](arg_fromUnit.COM_val, arg_toUnit.COM_val, byref(arg_fromValues.COM_val), byref(arg_ppConvertedDateValues.COM_val)))
            return arg_ppConvertedDateValues.python_val

    def NewQuantity(self, dimension:str, unitAbbrv:str, value:float) -> "IAgQuantity":
        """Creates an IAgQuantity interface with the given dimension, unit and value"""
        with agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_NewQuantity"](arg_dimension.COM_val, arg_unitAbbrv.COM_val, arg_value.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def NewDate(self, unitAbbrv:str, value:str) -> "IAgDate":
        """Creates an IAgDate interface with the given unit and value"""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.BSTR_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppDate:
            agcls.evaluate_hresult(self.__dict__["_NewDate"](arg_unitAbbrv.COM_val, arg_value.COM_val, byref(arg_ppDate.COM_val)))
            return arg_ppDate.python_val

    def NewPositionOnEarth(self) -> "IAgPosition":
        """Creates an IAgPosition interface with earth as its central body."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewPositionOnEarth"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def ConvertPositionArray(self, positionType:"AgEPositionType", positionArray:list, convertTo:"AgEPositionType") -> list:
        """Converts the specified position values from a given position type to another position type."""
        with agmarshall.AgEnum_arg(AgEPositionType, positionType) as arg_positionType, \
             agmarshall.SAFEARRAY_arg(positionArray) as arg_positionArray, \
             agmarshall.AgEnum_arg(AgEPositionType, convertTo) as arg_convertTo, \
             agmarshall.SAFEARRAY_arg() as arg_ppOutVal:
            agcls.evaluate_hresult(self.__dict__["_ConvertPositionArray"](arg_positionType.COM_val, byref(arg_positionArray.COM_val), arg_convertTo.COM_val, byref(arg_ppOutVal.COM_val)))
            return arg_ppOutVal.python_val

    def NewDirection(self) -> "IAgDirection":
        """Creates an IAgDirection interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewDirection"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def NewOrientation(self) -> "IAgOrientation":
        """Creates an IAgOrientation interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewOrientation"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def NewOrbitStateOnEarth(self) -> "IAgOrbitState":
        """Creates an IAgOrbitState interface with earth as its central body."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewOrbitStateOnEarth"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def NewPositionOnCB(self, centralBodyName:str) -> "IAgPosition":
        """Creates an IAgPosition interface using the supplied central body."""
        with agmarshall.BSTR_arg(centralBodyName) as arg_centralBodyName, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewPositionOnCB"](arg_centralBodyName.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def NewOrbitStateOnCB(self, centralBodyName:str) -> "IAgOrbitState":
        """Creates an IAgOrbitState interface using the supplied central body."""
        with agmarshall.BSTR_arg(centralBodyName) as arg_centralBodyName, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewOrbitStateOnCB"](arg_centralBodyName.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def QueryDirectionCosineMatrix(self, inputOrientation:"IAgOrientation") -> typing.Tuple[IAgCartesian3Vector, IAgCartesian3Vector, IAgCartesian3Vector]:
        """Returns a Direction Cosine Matrix (DCM)."""
        with agmarshall.AgInterface_in_arg(inputOrientation, IAgOrientation) as arg_inputOrientation, \
             agmarshall.AgInterface_out_arg() as arg_px, \
             agmarshall.AgInterface_out_arg() as arg_py, \
             agmarshall.AgInterface_out_arg() as arg_pz:
            agcls.evaluate_hresult(self.__dict__["_QueryDirectionCosineMatrix"](arg_inputOrientation.COM_val, byref(arg_px.COM_val), byref(arg_py.COM_val), byref(arg_pz.COM_val)))
            return arg_px.python_val, arg_py.python_val, arg_pz.python_val

    def QueryDirectionCosineMatrixArray(self, inputOrientation:"IAgOrientation") -> list:
        """Returns a Direction Cosine Matrix (DCM) as an array."""
        with agmarshall.AgInterface_in_arg(inputOrientation, IAgOrientation) as arg_inputOrientation, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_QueryDirectionCosineMatrixArray"](arg_inputOrientation.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def NewCartesian3Vector(self) -> "IAgCartesian3Vector":
        """Creates a cartesian vector."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewCartesian3Vector"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def NewCartesian3VectorFromDirection(self, inputDirection:"IAgDirection") -> "IAgCartesian3Vector":
        """Converts the direction to cartesian vector."""
        with agmarshall.AgInterface_in_arg(inputDirection, IAgDirection) as arg_inputDirection, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewCartesian3VectorFromDirection"](arg_inputDirection.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def NewCartesian3VectorFromPosition(self, inputPosition:"IAgPosition") -> "IAgCartesian3Vector":
        """Converts the position to cartesian vector."""
        with agmarshall.AgInterface_in_arg(inputPosition, IAgPosition) as arg_inputPosition, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_NewCartesian3VectorFromPosition"](arg_inputPosition.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{2B04A4E2-C647-4920-88FF-DE0413252D1C}", IAgConversionUtility)
agcls.AgTypeNameMap["IAgConversionUtility"] = IAgConversionUtility
__all__.append("IAgConversionUtility")

class IAgDoublesCollection(object):
    """Represents a collection of doubles."""
    _uuid = "{DEE2EB74-C19C-44C9-8825-09010A8F60BE}"
    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Add"] = _raise_uninitialized_error
        self.__dict__["_RemoveAt"] = _raise_uninitialized_error
        self.__dict__["_RemoveAll"] = _raise_uninitialized_error
        self.__dict__["_ToArray"] = _raise_uninitialized_error
        self.__dict__["_SetAt"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDoublesCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDoublesCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgDoublesCollection = agcom.GUID(IAgDoublesCollection._uuid)
        vtable_offset_local = IAgDoublesCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+1, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_Add"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_RemoveAt"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+5, agcom.LONG)
        self.__dict__["_RemoveAll"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+6, )
        self.__dict__["_ToArray"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+7, POINTER(agcom.SAFEARRAY))
        self.__dict__["_SetAt"] = IAGFUNCTYPE(pUnk, IID_IAgDoublesCollection, vtable_offset_local+8, agcom.LONG, agcom.DOUBLE)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDoublesCollection.__dict__ and type(IAgDoublesCollection.__dict__[attrname]) == property:
            return IAgDoublesCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgDoublesCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> float:
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, index:int) -> float:
        """Returns a double at a specified position."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Count(self) -> int:
        """Returns the number of items in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns a collection enumerator."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def Add(self, value:float) -> None:
        """Add a value to the collection of doubles."""
        with agmarshall.DOUBLE_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_Add"](arg_value.COM_val))

    def RemoveAt(self, index:int) -> None:
        """Remove an element from the collection at a specified position."""
        with agmarshall.LONG_arg(index) as arg_index:
            agcls.evaluate_hresult(self.__dict__["_RemoveAt"](arg_index.COM_val))

    def RemoveAll(self) -> None:
        """Clears the collection."""
        agcls.evaluate_hresult(self.__dict__["_RemoveAll"]())

    def ToArray(self) -> list:
        """Returns an array of the elements in the collection"""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_ToArray"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def SetAt(self, index:int, value:float) -> None:
        """Updates an element in the collection at a specified position."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_SetAt"](arg_index.COM_val, arg_value.COM_val))

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{DEE2EB74-C19C-44C9-8825-09010A8F60BE}", IAgDoublesCollection)
agcls.AgTypeNameMap["IAgDoublesCollection"] = IAgDoublesCollection
__all__.append("IAgDoublesCollection")



class AgExecCmdResult(IAgExecCmdResult):
    """Collection of strings returned by the ExecuteCommand."""
    def __init__(self, sourceObject=None):
        IAgExecCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgExecCmdResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgExecCmdResult._get_property(self, attrname) is not None: found_prop = IAgExecCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgExecCmdResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{92FE4418-FBA3-4D69-8F6E-9F600A1BA5E0}", AgExecCmdResult)
__all__.append("AgExecCmdResult")


class AgExecMultiCmdResult(IAgExecMultiCmdResult):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    def __init__(self, sourceObject=None):
        IAgExecMultiCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgExecMultiCmdResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgExecMultiCmdResult._get_property(self, attrname) is not None: found_prop = IAgExecMultiCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgExecMultiCmdResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{4B262721-FD3F-4DAD-BF32-4280752B7FE6}", AgExecMultiCmdResult)
__all__.append("AgExecMultiCmdResult")


class AgUnitPrefsUnit(IAgUnitPrefsUnit):
    """Object that contains info on the unit."""
    def __init__(self, sourceObject=None):
        IAgUnitPrefsUnit.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUnitPrefsUnit._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUnitPrefsUnit._get_property(self, attrname) is not None: found_prop = IAgUnitPrefsUnit._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUnitPrefsUnit.")
        
agcls.AgClassCatalog.add_catalog_entry("{4EDA384D-4C61-4756-92FF-1CD7C8049B96}", AgUnitPrefsUnit)
__all__.append("AgUnitPrefsUnit")


class AgUnitPrefsUnitCollection(IAgUnitPrefsUnitCollection):
    """Object that contains a collection of IAgUnitPrefsUnit."""
    def __init__(self, sourceObject=None):
        IAgUnitPrefsUnitCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUnitPrefsUnitCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUnitPrefsUnitCollection._get_property(self, attrname) is not None: found_prop = IAgUnitPrefsUnitCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUnitPrefsUnitCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{21AEACA4-B79D-455B-8DA4-89402A57A87B}", AgUnitPrefsUnitCollection)
__all__.append("AgUnitPrefsUnitCollection")


class AgUnitPrefsDim(IAgUnitPrefsDim):
    """Object that contains info on the Dimension."""
    def __init__(self, sourceObject=None):
        IAgUnitPrefsDim.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUnitPrefsDim._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUnitPrefsDim._get_property(self, attrname) is not None: found_prop = IAgUnitPrefsDim._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUnitPrefsDim.")
        
agcls.AgClassCatalog.add_catalog_entry("{5DB8F1AE-1240-4929-B7FD-75E0800970EB}", AgUnitPrefsDim)
__all__.append("AgUnitPrefsDim")


class AgUnitPrefsDimCollection(IAgUnitPrefsDimCollection):
    """Object that contains a collection of dimensions."""
    def __init__(self, sourceObject=None):
        IAgUnitPrefsDimCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUnitPrefsDimCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUnitPrefsDimCollection._get_property(self, attrname) is not None: found_prop = IAgUnitPrefsDimCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUnitPrefsDimCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{58562305-1D39-4B56-9FA8-AB49FEB68A37}", AgUnitPrefsDimCollection)
__all__.append("AgUnitPrefsDimCollection")


class AgConversionUtility(IAgConversionUtility):
    """Object that contains a unit conversion utility."""
    def __init__(self, sourceObject=None):
        IAgConversionUtility.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgConversionUtility._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgConversionUtility._get_property(self, attrname) is not None: found_prop = IAgConversionUtility._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgConversionUtility.")
        
agcls.AgClassCatalog.add_catalog_entry("{89E0FDC5-4016-47E9-96ED-0C1B05FFDADA}", AgConversionUtility)
__all__.append("AgConversionUtility")


class AgQuantity(IAgQuantity):
    """Object that contains a quantity."""
    def __init__(self, sourceObject=None):
        IAgQuantity.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgQuantity._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgQuantity._get_property(self, attrname) is not None: found_prop = IAgQuantity._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgQuantity.")
        
agcls.AgClassCatalog.add_catalog_entry("{59806B16-8D20-4EC3-8913-9457846AC0E5}", AgQuantity)
__all__.append("AgQuantity")


class AgDate(IAgDate):
    """Object that contains a date."""
    def __init__(self, sourceObject=None):
        IAgDate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDate._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDate._get_property(self, attrname) is not None: found_prop = IAgDate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDate.")
        
agcls.AgClassCatalog.add_catalog_entry("{CC2BA6FD-3A05-46D1-BAA0-68AC2D7896F1}", AgDate)
__all__.append("AgDate")


class AgPosition(IAgLocationData, IAgPosition):
    """The Position class."""
    def __init__(self, sourceObject=None):
        IAgLocationData.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgLocationData._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgLocationData._get_property(self, attrname) is not None: found_prop = IAgLocationData._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgPosition.")
        
agcls.AgClassCatalog.add_catalog_entry("{B3FE87C4-702C-4263-83D8-4E32C993E2D0}", AgPosition)
__all__.append("AgPosition")


class AgCartesian(IAgCartesian, IAgPosition):
    """Class used to access a position using Cartesian Coordinates."""
    def __init__(self, sourceObject=None):
        IAgCartesian.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCartesian._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCartesian._get_property(self, attrname) is not None: found_prop = IAgCartesian._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCartesian.")
        
agcls.AgClassCatalog.add_catalog_entry("{027F342E-5989-43D1-831B-BF2E313A1CBB}", AgCartesian)
__all__.append("AgCartesian")


class AgGeodetic(IAgGeodetic, IAgPosition):
    """Class defining Geodetic position."""
    def __init__(self, sourceObject=None):
        IAgGeodetic.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgGeodetic._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGeodetic._get_property(self, attrname) is not None: found_prop = IAgGeodetic._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgGeodetic.")
        
agcls.AgClassCatalog.add_catalog_entry("{F65DA479-6847-456B-8816-85FF3ECD4469}", AgGeodetic)
__all__.append("AgGeodetic")


class AgGeocentric(IAgGeocentric, IAgPosition):
    """Class defining Geocentric position."""
    def __init__(self, sourceObject=None):
        IAgGeocentric.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgGeocentric._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGeocentric._get_property(self, attrname) is not None: found_prop = IAgGeocentric._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgGeocentric.")
        
agcls.AgClassCatalog.add_catalog_entry("{1AC9E304-8DCE-4CD6-A5AA-B82738823556}", AgGeocentric)
__all__.append("AgGeocentric")


class AgPlanetodetic(IAgPlanetodetic, IAgPosition):
    """Class defining Planetodetic position."""
    def __init__(self, sourceObject=None):
        IAgPlanetodetic.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPlanetodetic._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgPlanetodetic._get_property(self, attrname) is not None: found_prop = IAgPlanetodetic._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgPlanetodetic.")
        
agcls.AgClassCatalog.add_catalog_entry("{E06625DF-EEB4-4384-B142-C1C501F522F8}", AgPlanetodetic)
__all__.append("AgPlanetodetic")


class AgPlanetocentric(IAgPlanetocentric, IAgPosition):
    """Class defining Planetocentric position."""
    def __init__(self, sourceObject=None):
        IAgPlanetocentric.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPlanetocentric._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgPlanetocentric._get_property(self, attrname) is not None: found_prop = IAgPlanetocentric._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgPlanetocentric.")
        
agcls.AgClassCatalog.add_catalog_entry("{DB009F3C-1FA7-4241-8A8D-D55E234CFF02}", AgPlanetocentric)
__all__.append("AgPlanetocentric")


class AgSpherical(IAgSpherical, IAgPosition):
    """Class defining spherical position."""
    def __init__(self, sourceObject=None):
        IAgSpherical.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSpherical._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSpherical._get_property(self, attrname) is not None: found_prop = IAgSpherical._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSpherical.")
        
agcls.AgClassCatalog.add_catalog_entry("{CD809FAC-48DF-46AB-A322-92947F84C7E6}", AgSpherical)
__all__.append("AgSpherical")


class AgCylindrical(IAgCylindrical, IAgPosition):
    """Class defining cylindrical position."""
    def __init__(self, sourceObject=None):
        IAgCylindrical.__init__(self, sourceObject)
        IAgPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCylindrical._private_init(self, pUnk)
        IAgPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCylindrical._get_property(self, attrname) is not None: found_prop = IAgCylindrical._get_property(self, attrname)
        if IAgPosition._get_property(self, attrname) is not None: found_prop = IAgPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCylindrical.")
        
agcls.AgClassCatalog.add_catalog_entry("{FF1B8082-F06B-4F7B-94B2-6D3C4D9A7D51}", AgCylindrical)
__all__.append("AgCylindrical")


class AgDirection(IAgDirection):
    """Class defining direction options for aligned and constrained vectors."""
    def __init__(self, sourceObject=None):
        IAgDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDirection._get_property(self, attrname) is not None: found_prop = IAgDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDirection.")
        
agcls.AgClassCatalog.add_catalog_entry("{9BC95D30-4E21-4502-ADE6-2AAE9ED89903}", AgDirection)
__all__.append("AgDirection")


class AgDirectionEuler(IAgDirectionEuler, IAgDirection):
    """Euler direction sequence."""
    def __init__(self, sourceObject=None):
        IAgDirectionEuler.__init__(self, sourceObject)
        IAgDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirectionEuler._private_init(self, pUnk)
        IAgDirection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDirectionEuler._get_property(self, attrname) is not None: found_prop = IAgDirectionEuler._get_property(self, attrname)
        if IAgDirection._get_property(self, attrname) is not None: found_prop = IAgDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDirectionEuler.")
        
agcls.AgClassCatalog.add_catalog_entry("{A14FAC2D-C055-4FB4-9AAD-67314E647717}", AgDirectionEuler)
__all__.append("AgDirectionEuler")


class AgDirectionPR(IAgDirectionPR, IAgDirection):
    """Pitch-Roll (PR) direction sequence."""
    def __init__(self, sourceObject=None):
        IAgDirectionPR.__init__(self, sourceObject)
        IAgDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirectionPR._private_init(self, pUnk)
        IAgDirection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDirectionPR._get_property(self, attrname) is not None: found_prop = IAgDirectionPR._get_property(self, attrname)
        if IAgDirection._get_property(self, attrname) is not None: found_prop = IAgDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDirectionPR.")
        
agcls.AgClassCatalog.add_catalog_entry("{3EEEDD8D-FB4C-442D-8A1F-28C7A3C2C9A6}", AgDirectionPR)
__all__.append("AgDirectionPR")


class AgDirectionRADec(IAgDirectionRADec, IAgDirection):
    """Spherical direction (Right Ascension and Declination)."""
    def __init__(self, sourceObject=None):
        IAgDirectionRADec.__init__(self, sourceObject)
        IAgDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirectionRADec._private_init(self, pUnk)
        IAgDirection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDirectionRADec._get_property(self, attrname) is not None: found_prop = IAgDirectionRADec._get_property(self, attrname)
        if IAgDirection._get_property(self, attrname) is not None: found_prop = IAgDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDirectionRADec.")
        
agcls.AgClassCatalog.add_catalog_entry("{EB70218F-18C4-41FE-90AC-99AFEB243666}", AgDirectionRADec)
__all__.append("AgDirectionRADec")


class AgDirectionXYZ(IAgDirectionXYZ, IAgDirection):
    """Cartesian direction."""
    def __init__(self, sourceObject=None):
        IAgDirectionXYZ.__init__(self, sourceObject)
        IAgDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDirectionXYZ._private_init(self, pUnk)
        IAgDirection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDirectionXYZ._get_property(self, attrname) is not None: found_prop = IAgDirectionXYZ._get_property(self, attrname)
        if IAgDirection._get_property(self, attrname) is not None: found_prop = IAgDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDirectionXYZ.")
        
agcls.AgClassCatalog.add_catalog_entry("{E1AB8359-28B7-468F-BD92-378267CA0998}", AgDirectionXYZ)
__all__.append("AgDirectionXYZ")


class AgOrientation(IAgOrientation):
    """Class defining the orientation of an orbit."""
    def __init__(self, sourceObject=None):
        IAgOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientation._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgOrientation.")
        
agcls.AgClassCatalog.add_catalog_entry("{97DF3B0E-D8E0-46B1-88CB-DC7A0AF934AE}", AgOrientation)
__all__.append("AgOrientation")


class AgOrientationAzEl(IAgOrientationAzEl, IAgOrientation):
    """AzEl orientation method."""
    def __init__(self, sourceObject=None):
        IAgOrientationAzEl.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationAzEl._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationAzEl._get_property(self, attrname) is not None: found_prop = IAgOrientationAzEl._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgOrientationAzEl.")
        
agcls.AgClassCatalog.add_catalog_entry("{3CF365C4-9B79-4B72-A479-16EF921F791C}", AgOrientationAzEl)
__all__.append("AgOrientationAzEl")


class AgOrientationEulerAngles(IAgOrientationEulerAngles, IAgOrientation):
    """Euler Angles orientation method."""
    def __init__(self, sourceObject=None):
        IAgOrientationEulerAngles.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationEulerAngles._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationEulerAngles._get_property(self, attrname) is not None: found_prop = IAgOrientationEulerAngles._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgOrientationEulerAngles.")
        
agcls.AgClassCatalog.add_catalog_entry("{C3DC0E0A-690B-4C20-9134-D6C57BE46D40}", AgOrientationEulerAngles)
__all__.append("AgOrientationEulerAngles")


class AgOrientationQuaternion(IAgOrientationQuaternion, IAgOrientation):
    """Quaternion orientation method."""
    def __init__(self, sourceObject=None):
        IAgOrientationQuaternion.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationQuaternion._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationQuaternion._get_property(self, attrname) is not None: found_prop = IAgOrientationQuaternion._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgOrientationQuaternion.")
        
agcls.AgClassCatalog.add_catalog_entry("{8AC57BB2-C7A7-4C05-9E35-7246956759D9}", AgOrientationQuaternion)
__all__.append("AgOrientationQuaternion")


class AgOrientationYPRAngles(IAgOrientationYPRAngles, IAgOrientation):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, sourceObject=None):
        IAgOrientationYPRAngles.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationYPRAngles._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationYPRAngles._get_property(self, attrname) is not None: found_prop = IAgOrientationYPRAngles._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgOrientationYPRAngles.")
        
agcls.AgClassCatalog.add_catalog_entry("{AE398C98-2D0D-4863-8097-9F7648CABC21}", AgOrientationYPRAngles)
__all__.append("AgOrientationYPRAngles")


class AgDoublesCollection(IAgDoublesCollection):
    """A collection of doubles."""
    def __init__(self, sourceObject=None):
        IAgDoublesCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDoublesCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDoublesCollection._get_property(self, attrname) is not None: found_prop = IAgDoublesCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDoublesCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{ECD576C3-0440-44D9-9D16-B88873C3A816}", AgDoublesCollection)
__all__.append("AgDoublesCollection")


class AgCartesian3Vector(IAgCartesian3Vector):
    """A 3-D cartesian vector."""
    def __init__(self, sourceObject=None):
        IAgCartesian3Vector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCartesian3Vector._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCartesian3Vector._get_property(self, attrname) is not None: found_prop = IAgCartesian3Vector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCartesian3Vector.")
        
agcls.AgClassCatalog.add_catalog_entry("{4A70BA75-BC1A-459D-9DAD-E174F3B94002}", AgCartesian3Vector)
__all__.append("AgCartesian3Vector")


class AgCartesian2Vector(IAgCartesian2Vector):
    """A 2-D cartesian vector."""
    def __init__(self, sourceObject=None):
        IAgCartesian2Vector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCartesian2Vector._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCartesian2Vector._get_property(self, attrname) is not None: found_prop = IAgCartesian2Vector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCartesian2Vector.")
        
agcls.AgClassCatalog.add_catalog_entry("{ECE2E7DF-CBF1-4124-AAAC-33700F16FAE2}", AgCartesian2Vector)
__all__.append("AgCartesian2Vector")


class AgPropertyInfo(IAgPropertyInfo):
    """Property Information coclass."""
    def __init__(self, sourceObject=None):
        IAgPropertyInfo.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPropertyInfo._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgPropertyInfo._get_property(self, attrname) is not None: found_prop = IAgPropertyInfo._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgPropertyInfo.")
        
agcls.AgClassCatalog.add_catalog_entry("{92498440-7C87-495C-A8BD-0A70F85D4DC8}", AgPropertyInfo)
__all__.append("AgPropertyInfo")


class AgPropertyInfoCollection(IAgPropertyInfoCollection):
    """Property Information Collection coclass."""
    def __init__(self, sourceObject=None):
        IAgPropertyInfoCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPropertyInfoCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgPropertyInfoCollection._get_property(self, attrname) is not None: found_prop = IAgPropertyInfoCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgPropertyInfoCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{113B1CA1-4DD4-4915-8D7F-E1F96E18A985}", AgPropertyInfoCollection)
__all__.append("AgPropertyInfoCollection")


class AgRuntimeTypeInfo(IAgRuntimeTypeInfo):
    """Runtime Type info coclass."""
    def __init__(self, sourceObject=None):
        IAgRuntimeTypeInfo.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgRuntimeTypeInfo._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgRuntimeTypeInfo._get_property(self, attrname) is not None: found_prop = IAgRuntimeTypeInfo._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgRuntimeTypeInfo.")
        
agcls.AgClassCatalog.add_catalog_entry("{D80F3E93-932A-49B3-8661-1A1627DCBDD1}", AgRuntimeTypeInfo)
__all__.append("AgRuntimeTypeInfo")


class AgCROrientationAzEl(IAgOrientationAzEl, IAgOrientation, IAgOrientationPositionOffset):
    """AzEl orientation method."""
    def __init__(self, sourceObject=None):
        IAgOrientationAzEl.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
        IAgOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationAzEl._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
        IAgOrientationPositionOffset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationAzEl._get_property(self, attrname) is not None: found_prop = IAgOrientationAzEl._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if IAgOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IAgOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCROrientationAzEl.")
        
agcls.AgClassCatalog.add_catalog_entry("{1E11E3CE-BCAA-4E1F-BAF9-B6AD3650F9BA}", AgCROrientationAzEl)
__all__.append("AgCROrientationAzEl")


class AgCROrientationEulerAngles(IAgOrientationEulerAngles, IAgOrientation, IAgOrientationPositionOffset):
    """Euler Angles orientation method."""
    def __init__(self, sourceObject=None):
        IAgOrientationEulerAngles.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
        IAgOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationEulerAngles._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
        IAgOrientationPositionOffset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationEulerAngles._get_property(self, attrname) is not None: found_prop = IAgOrientationEulerAngles._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if IAgOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IAgOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCROrientationEulerAngles.")
        
agcls.AgClassCatalog.add_catalog_entry("{D08A5BF9-5CBA-432D-8C48-3CD1CFC42636}", AgCROrientationEulerAngles)
__all__.append("AgCROrientationEulerAngles")


class AgCROrientationQuaternion(IAgOrientationQuaternion, IAgOrientation, IAgOrientationPositionOffset):
    """Quaternion orientation method."""
    def __init__(self, sourceObject=None):
        IAgOrientationQuaternion.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
        IAgOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationQuaternion._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
        IAgOrientationPositionOffset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationQuaternion._get_property(self, attrname) is not None: found_prop = IAgOrientationQuaternion._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if IAgOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IAgOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCROrientationQuaternion.")
        
agcls.AgClassCatalog.add_catalog_entry("{9D3BA3F8-B6F6-443B-A8AC-74C86A8B901A}", AgCROrientationQuaternion)
__all__.append("AgCROrientationQuaternion")


class AgCROrientationYPRAngles(IAgOrientationYPRAngles, IAgOrientation, IAgOrientationPositionOffset):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, sourceObject=None):
        IAgOrientationYPRAngles.__init__(self, sourceObject)
        IAgOrientation.__init__(self, sourceObject)
        IAgOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgOrientationYPRAngles._private_init(self, pUnk)
        IAgOrientation._private_init(self, pUnk)
        IAgOrientationPositionOffset._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgOrientationYPRAngles._get_property(self, attrname) is not None: found_prop = IAgOrientationYPRAngles._get_property(self, attrname)
        if IAgOrientation._get_property(self, attrname) is not None: found_prop = IAgOrientation._get_property(self, attrname)
        if IAgOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IAgOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCROrientationYPRAngles.")
        
agcls.AgClassCatalog.add_catalog_entry("{1FB88B69-1844-4CD9-BD44-09A9FCC4E06F}", AgCROrientationYPRAngles)
__all__.append("AgCROrientationYPRAngles")


class AgCROrientationOffsetCart(IAgCartesian3Vector):
    """Orientation offset cartesian."""
    def __init__(self, sourceObject=None):
        IAgCartesian3Vector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgCartesian3Vector._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgCartesian3Vector._get_property(self, attrname) is not None: found_prop = IAgCartesian3Vector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgCROrientationOffsetCart.")
        
agcls.AgClassCatalog.add_catalog_entry("{462F58AA-A74F-4E42-88B6-8F2790E85FEC}", AgCROrientationOffsetCart)
__all__.append("AgCROrientationOffsetCart")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
