################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

__all__ = ["AZ_EL_ABOUT_BORESIGHT", "COORDINATE_SYSTEM", "CROrientationAzEl", "CROrientationEulerAngles", "CROrientationOffsetCart", 
"CROrientationQuaternion", "CROrientationYPRAngles", "Cartesian", "Cartesian2Vector", "Cartesian3Vector", "ConversionUtility", 
"Cylindrical", "DELAUNAY_G_TYPE_TEMP", "DELAUNAY_H_TYPE_TEMP", "DELAUNAY_L_TYPE_TEMP", "DIRECTION_TYPE", "Date", "Direction", 
"DirectionEuler", "DirectionPR", "DirectionRADec", "DirectionXYZ", "DoublesCollection", "EULER_DIRECTION_SEQUENCE", "EULER_ORIENTATION_SEQUENCE", 
"EXEC_MULTI_CMD_RESULT_ACTION", "ExecCmdResult", "ExecMultiCmdResult", "FILL_STYLE", "Geocentric", "Geodetic", "ICartesian", 
"ICartesian2Vector", "ICartesian3Vector", "IConversionUtility", "ICylindrical", "IDate", "IDirection", "IDirectionEuler", 
"IDirectionPR", "IDirectionRADec", "IDirectionXYZ", "IDoublesCollection", "IExecCmdResult", "IExecMultiCmdResult", "IGeocentric", 
"IGeodetic", "ILocationData", "IOrbitState", "IOrientation", "IOrientationAzEl", "IOrientationEulerAngles", "IOrientationPositionOffset", 
"IOrientationQuaternion", "IOrientationYPRAngles", "IPlanetocentric", "IPlanetodetic", "IPosition", "IPropertyInfo", "IPropertyInfoCollection", 
"IQuantity", "IRuntimeTypeInfo", "IRuntimeTypeInfoProvider", "ISpherical", "IUnitPreferencesDimension", "IUnitPreferencesDimensionCollection", 
"IUnitPreferencesUnit", "IUnitPreferencesUnitCollection", "LINE_STYLE", "LOG_MSG_DISP_ID", "LOG_MSG_TYPE", "ORBIT_STATE_TYPE", 
"ORIENTATION_TYPE", "Orientation", "OrientationAzEl", "OrientationEulerAngles", "OrientationQuaternion", "OrientationYPRAngles", 
"POSITION_TYPE", "PROPERTY_INFO_VALUE_TYPE", "PR_SEQUENCE", "Planetocentric", "Planetodetic", "Position", "PropertyInfo", 
"PropertyInfoCollection", "Quantity", "RuntimeTypeInfo", "Spherical", "UnitPreferencesDimension", "UnitPreferencesDimensionCollection", 
"UnitPreferencesUnit", "UnitPreferencesUnitCollection", "YPR_ANGLES_SEQUENCE"]

from ctypes import POINTER
from datetime import datetime
from enum import IntEnum, IntFlag
import typing

try:
    from numpy import ndarray
except ModuleNotFoundError:
    pass
    
try:
    from pandas import DataFrame
except ModuleNotFoundError:
    pass

from .internal import coclassutil as agcls, comutil as agcom, marshall as agmarshall
from .internal.apiutil import enumerator_proxy, interface_proxy, out_arg
from .internal.comutil import IDispatch, IUnknown
from .internal.eventutil import *
from .utilities.exceptions import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class POSITION_TYPE(IntEnum):
    """Facility/place/target position types."""
    CARTESIAN = 0x0
    """Cartesian: position specified in terms of the X, Y and Z components of the object's position vector, where the Z-axis points to the North pole, and the X-axis crosses 0 degrees latitude/0 degrees longitude."""
    CYLINDRICAL = 0x1
    """Cylindrical: position specified in terms of radius (polar), longitude (measured in degrees from -360.0 degrees to +360.0 degrees), and the Z component of the object's position vector."""
    GEOCENTRIC = 0x2
    """Geocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude."""
    GEODETIC = 0x3
    """Geodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude."""
    SPHERICAL = 0x4
    """Spherical: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and radius (distance of the object from the center of the Earth)."""
    PLANETOCENTRIC = 0x5
    """Planetocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude."""
    PLANETODETIC = 0x6
    """Planetodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude."""

POSITION_TYPE.CARTESIAN.__doc__ = "Cartesian: position specified in terms of the X, Y and Z components of the object's position vector, where the Z-axis points to the North pole, and the X-axis crosses 0 degrees latitude/0 degrees longitude."
POSITION_TYPE.CYLINDRICAL.__doc__ = "Cylindrical: position specified in terms of radius (polar), longitude (measured in degrees from -360.0 degrees to +360.0 degrees), and the Z component of the object's position vector."
POSITION_TYPE.GEOCENTRIC.__doc__ = "Geocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude."
POSITION_TYPE.GEODETIC.__doc__ = "Geodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude."
POSITION_TYPE.SPHERICAL.__doc__ = "Spherical: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and radius (distance of the object from the center of the Earth)."
POSITION_TYPE.PLANETOCENTRIC.__doc__ = "Planetocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude."
POSITION_TYPE.PLANETODETIC.__doc__ = "Planetodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude."

agcls.AgTypeNameMap["POSITION_TYPE"] = POSITION_TYPE

class EULER_DIRECTION_SEQUENCE(IntEnum):
    """Euler direction sequences."""
    SEQUENCE_12 = 0
    """12 sequence."""
    SEQUENCE_21 = 1
    """21 sequence."""
    SEQUENCE_31 = 2
    """31 sequence."""
    SEQUENCE_32 = 3
    """32 sequence."""

EULER_DIRECTION_SEQUENCE.SEQUENCE_12.__doc__ = "12 sequence."
EULER_DIRECTION_SEQUENCE.SEQUENCE_21.__doc__ = "21 sequence."
EULER_DIRECTION_SEQUENCE.SEQUENCE_31.__doc__ = "31 sequence."
EULER_DIRECTION_SEQUENCE.SEQUENCE_32.__doc__ = "32 sequence."

agcls.AgTypeNameMap["EULER_DIRECTION_SEQUENCE"] = EULER_DIRECTION_SEQUENCE

class DIRECTION_TYPE(IntEnum):
    """Direction options for aligned and constrained vectors."""
    EULER = 0
    """Euler B and C angles."""
    PR = 1
    """Pitch and Roll angles."""
    RA_DEC = 2
    """Spherical elements: Right Ascension and Declination."""
    XYZ = 3
    """Cartesian elements."""

DIRECTION_TYPE.EULER.__doc__ = "Euler B and C angles."
DIRECTION_TYPE.PR.__doc__ = "Pitch and Roll angles."
DIRECTION_TYPE.RA_DEC.__doc__ = "Spherical elements: Right Ascension and Declination."
DIRECTION_TYPE.XYZ.__doc__ = "Cartesian elements."

agcls.AgTypeNameMap["DIRECTION_TYPE"] = DIRECTION_TYPE

class PR_SEQUENCE(IntEnum):
    """Pitch-Roll (PR) direction sequences."""
    PR = 0
    """PR sequence."""

PR_SEQUENCE.PR.__doc__ = "PR sequence."

agcls.AgTypeNameMap["PR_SEQUENCE"] = PR_SEQUENCE

class ORIENTATION_TYPE(IntEnum):
    """Orientation methods."""
    AZ_EL = 0
    """AzEl (azimuth-elevation) method."""
    EULER_ANGLES = 1
    """Euler angles method."""
    QUATERNION = 2
    """Quaternion method."""
    YPR_ANGLES = 3
    """YPR (yaw-pitch-roll) method."""

ORIENTATION_TYPE.AZ_EL.__doc__ = "AzEl (azimuth-elevation) method."
ORIENTATION_TYPE.EULER_ANGLES.__doc__ = "Euler angles method."
ORIENTATION_TYPE.QUATERNION.__doc__ = "Quaternion method."
ORIENTATION_TYPE.YPR_ANGLES.__doc__ = "YPR (yaw-pitch-roll) method."

agcls.AgTypeNameMap["ORIENTATION_TYPE"] = ORIENTATION_TYPE

class AZ_EL_ABOUT_BORESIGHT(IntEnum):
    """About Boresight options for AzEl orientation method."""
    HOLD = 0
    """Hold: rotation about the Y axis followed by rotation about the new X-axis."""
    ROTATE = 1
    """Rotate: rotation about the sensor's or antenna's Z axis by the azimuth angle, followed by rotation about the new Y axis by 90 degrees minus the elevation angle."""

AZ_EL_ABOUT_BORESIGHT.HOLD.__doc__ = "Hold: rotation about the Y axis followed by rotation about the new X-axis."
AZ_EL_ABOUT_BORESIGHT.ROTATE.__doc__ = "Rotate: rotation about the sensor's or antenna's Z axis by the azimuth angle, followed by rotation about the new Y axis by 90 degrees minus the elevation angle."

agcls.AgTypeNameMap["AZ_EL_ABOUT_BORESIGHT"] = AZ_EL_ABOUT_BORESIGHT

class EULER_ORIENTATION_SEQUENCE(IntEnum):
    """Euler rotation sequence options:"""
    SEQUENCE_121 = 0
    """121 rotation."""
    SEQUENCE_123 = 1
    """123 rotation."""
    SEQUENCE_131 = 2
    """131 rotation."""
    SEQUENCE_132 = 3
    """132 rotation."""
    SEQUENCE_212 = 4
    """212 rotation."""
    SEQUENCE_213 = 5
    """213 rotation."""
    SEQUENCE_231 = 6
    """231 rotation."""
    SEQUENCE_232 = 7
    """232 rotation."""
    SEQUENCE_312 = 8
    """312 rotation."""
    SEQUENCE_313 = 9
    """313 rotation."""
    SEQUENCE_321 = 10
    """321 rotation."""
    SEQUENCE_323 = 11
    """323 rotation."""

EULER_ORIENTATION_SEQUENCE.SEQUENCE_121.__doc__ = "121 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_123.__doc__ = "123 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_131.__doc__ = "131 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_132.__doc__ = "132 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_212.__doc__ = "212 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_213.__doc__ = "213 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_231.__doc__ = "231 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_232.__doc__ = "232 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_312.__doc__ = "312 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_313.__doc__ = "313 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_321.__doc__ = "321 rotation."
EULER_ORIENTATION_SEQUENCE.SEQUENCE_323.__doc__ = "323 rotation."

agcls.AgTypeNameMap["EULER_ORIENTATION_SEQUENCE"] = EULER_ORIENTATION_SEQUENCE

class YPR_ANGLES_SEQUENCE(IntEnum):
    """Yaw-Pitch-Roll (YPR) sequences."""
    PRY = 0
    """PRY sequence."""
    PYR = 1
    """PYR sequence."""
    RPY = 2
    """RPY sequence."""
    RYP = 3
    """RYP sequence."""
    YPR = 4
    """YPR sequence."""
    YRP = 5
    """YRP sequence."""

YPR_ANGLES_SEQUENCE.PRY.__doc__ = "PRY sequence."
YPR_ANGLES_SEQUENCE.PYR.__doc__ = "PYR sequence."
YPR_ANGLES_SEQUENCE.RPY.__doc__ = "RPY sequence."
YPR_ANGLES_SEQUENCE.RYP.__doc__ = "RYP sequence."
YPR_ANGLES_SEQUENCE.YPR.__doc__ = "YPR sequence."
YPR_ANGLES_SEQUENCE.YRP.__doc__ = "YRP sequence."

agcls.AgTypeNameMap["YPR_ANGLES_SEQUENCE"] = YPR_ANGLES_SEQUENCE

class ORBIT_STATE_TYPE(IntEnum):
    """Coordinate types used in specifying orbit state."""
    CARTESIAN = 0
    """Cartesian coordinate type."""
    CLASSICAL = 1
    """Classical (Keplerian) coordinate type."""
    EQUINOCTIAL = 2
    """Equinoctial coordinate type."""
    DELAUNAY = 3
    """Delaunay variables coordinate type."""
    SPHERICAL = 4
    """Spherical coordinate type."""
    MIXED_SPHERICAL = 5
    """Mixed spherical coordinate type."""
    GEODETIC = 6
    """Geodetic coordinate type."""

ORBIT_STATE_TYPE.CARTESIAN.__doc__ = "Cartesian coordinate type."
ORBIT_STATE_TYPE.CLASSICAL.__doc__ = "Classical (Keplerian) coordinate type."
ORBIT_STATE_TYPE.EQUINOCTIAL.__doc__ = "Equinoctial coordinate type."
ORBIT_STATE_TYPE.DELAUNAY.__doc__ = "Delaunay variables coordinate type."
ORBIT_STATE_TYPE.SPHERICAL.__doc__ = "Spherical coordinate type."
ORBIT_STATE_TYPE.MIXED_SPHERICAL.__doc__ = "Mixed spherical coordinate type."
ORBIT_STATE_TYPE.GEODETIC.__doc__ = "Geodetic coordinate type."

agcls.AgTypeNameMap["ORBIT_STATE_TYPE"] = ORBIT_STATE_TYPE

class COORDINATE_SYSTEM(IntEnum):
    """Earth-centered coordinate systems for defining certain propagators."""
    UNKNOWN = -1
    """Represents coordinate system not supported by the Object Model"""
    ALIGNMENT_AT_EPOCH = 0
    """Alignment at Epoch: an inertial system coincident with ECF at the Coord Epoch. Often used to specify launch trajectories."""
    B1950 = 1
    """B1950: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the beginning of the Besselian year 1950 and corresponds to 31 December 1949 22:09:07.2 or JD 2433282.423."""
    FIXED = 2
    """Fixed: X is fixed at 0 deg longitude, Y is fixed at 90 deg longitude, and Z is directed toward the north pole."""
    J2000 = 3
    """J2000: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth on 1 Jan 2000 at 12:00:00.00 TDB, which corresponds to JD 2451545.0 TDB."""
    MEAN_OF_DATE = 4
    """Mean of Date: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Orbit Epoch."""
    MEAN_OF_EPOCH = 5
    """Mean of Epoch: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Coord Epoch."""
    TEME_OF_DATE = 6
    """TEME of Date: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch."""
    TEME_OF_EPOCH = 7
    """TEME of Epoch: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch."""
    TRUE_OF_DATE = 8
    """True of Date: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch."""
    TRUE_OF_EPOCH = 9
    """True of Epoch: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch."""
    TRUE_OF_REFERENCE_DATE = 10
    """True of Ref Date: A special case of True of Epoch. Instead of the Coord Epoch, this system uses a Reference Date defined in the Integration Control page of the scenario's PODS properties."""
    ICRF = 11
    """ICRF: International Celestial Reference Frame."""
    MEAN_EARTH = 13
    """Mean Earth"""
    FIXED_NO_LIBRATION = 14
    """uses an analytic formula not modeling lunar libration"""
    FIXED_IAU2003 = 15
    """Fixed_IAU2003"""
    PRINCIPAL_AXES421 = 16
    """PrincipalAxes_421"""
    PRINCIPAL_AXES403 = 17
    """PrincipalAxes_403"""
    INERTIAL = 18
    """Inertial"""
    J2000_ECLIPTIC = 19
    """The mean ecliptic system evaluated at the J2000 epoch. The mean ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the mean obliquity defined using FK5 IAU76 theory."""
    TRUE_ECLIPTIC_OF_DATE = 21
    """The true ecliptic system, evaluated at each given time. The true ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the true obliquity defined using FK5 IAU76 theory."""
    PRINCIPAL_AXES430 = 22
    """PrincipalAxes_430"""
    TRUE_OF_DATE_ROTATING = 23
    """TrueOfDateRotating: Like the Fixed system, but ignores pole wander. The XY plane is the same as the XY plane of the TrueOfDate system, and the system rotates about the TrueOfDate Z-axis."""
    ECLIPTIC_J2000ICRF = 24
    """EclipticJ2000ICRF: An ecliptic system that is a fixed offset of the ICRF system, found by rotating the ICRF system about its X-axis by the mean obliquity at the J2000 epoch (i.e., 84381.448 arcSecs). The ecliptic plane is the XY-plane of this system."""

COORDINATE_SYSTEM.UNKNOWN.__doc__ = "Represents coordinate system not supported by the Object Model"
COORDINATE_SYSTEM.ALIGNMENT_AT_EPOCH.__doc__ = "Alignment at Epoch: an inertial system coincident with ECF at the Coord Epoch. Often used to specify launch trajectories."
COORDINATE_SYSTEM.B1950.__doc__ = "B1950: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the beginning of the Besselian year 1950 and corresponds to 31 December 1949 22:09:07.2 or JD 2433282.423."
COORDINATE_SYSTEM.FIXED.__doc__ = "Fixed: X is fixed at 0 deg longitude, Y is fixed at 90 deg longitude, and Z is directed toward the north pole."
COORDINATE_SYSTEM.J2000.__doc__ = "J2000: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth on 1 Jan 2000 at 12:00:00.00 TDB, which corresponds to JD 2451545.0 TDB."
COORDINATE_SYSTEM.MEAN_OF_DATE.__doc__ = "Mean of Date: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Orbit Epoch."
COORDINATE_SYSTEM.MEAN_OF_EPOCH.__doc__ = "Mean of Epoch: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Coord Epoch."
COORDINATE_SYSTEM.TEME_OF_DATE.__doc__ = "TEME of Date: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch."
COORDINATE_SYSTEM.TEME_OF_EPOCH.__doc__ = "TEME of Epoch: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch."
COORDINATE_SYSTEM.TRUE_OF_DATE.__doc__ = "True of Date: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch."
COORDINATE_SYSTEM.TRUE_OF_EPOCH.__doc__ = "True of Epoch: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch."
COORDINATE_SYSTEM.TRUE_OF_REFERENCE_DATE.__doc__ = "True of Ref Date: A special case of True of Epoch. Instead of the Coord Epoch, this system uses a Reference Date defined in the Integration Control page of the scenario's PODS properties."
COORDINATE_SYSTEM.ICRF.__doc__ = "ICRF: International Celestial Reference Frame."
COORDINATE_SYSTEM.MEAN_EARTH.__doc__ = "Mean Earth"
COORDINATE_SYSTEM.FIXED_NO_LIBRATION.__doc__ = "uses an analytic formula not modeling lunar libration"
COORDINATE_SYSTEM.FIXED_IAU2003.__doc__ = "Fixed_IAU2003"
COORDINATE_SYSTEM.PRINCIPAL_AXES421.__doc__ = "PrincipalAxes_421"
COORDINATE_SYSTEM.PRINCIPAL_AXES403.__doc__ = "PrincipalAxes_403"
COORDINATE_SYSTEM.INERTIAL.__doc__ = "Inertial"
COORDINATE_SYSTEM.J2000_ECLIPTIC.__doc__ = "The mean ecliptic system evaluated at the J2000 epoch. The mean ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the mean obliquity defined using FK5 IAU76 theory."
COORDINATE_SYSTEM.TRUE_ECLIPTIC_OF_DATE.__doc__ = "The true ecliptic system, evaluated at each given time. The true ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the true obliquity defined using FK5 IAU76 theory."
COORDINATE_SYSTEM.PRINCIPAL_AXES430.__doc__ = "PrincipalAxes_430"
COORDINATE_SYSTEM.TRUE_OF_DATE_ROTATING.__doc__ = "TrueOfDateRotating: Like the Fixed system, but ignores pole wander. The XY plane is the same as the XY plane of the TrueOfDate system, and the system rotates about the TrueOfDate Z-axis."
COORDINATE_SYSTEM.ECLIPTIC_J2000ICRF.__doc__ = "EclipticJ2000ICRF: An ecliptic system that is a fixed offset of the ICRF system, found by rotating the ICRF system about its X-axis by the mean obliquity at the J2000 epoch (i.e., 84381.448 arcSecs). The ecliptic plane is the XY-plane of this system."

agcls.AgTypeNameMap["COORDINATE_SYSTEM"] = COORDINATE_SYSTEM

class DELAUNAY_L_TYPE_TEMP(IntEnum):
    """Select whether to use the default representation of Delaunay L or L/SQRT(mu)."""
    UNKNOWN_TEMP = -1
    """Represents a value not supported by the Object Model"""
    L_TEMP = 0
    """Use the default representation of L."""
    L_OVER_SQRT_MU_TEMP = 1
    """Use L/SQRT(mu)."""

DELAUNAY_L_TYPE_TEMP.UNKNOWN_TEMP.__doc__ = "Represents a value not supported by the Object Model"
DELAUNAY_L_TYPE_TEMP.L_TEMP.__doc__ = "Use the default representation of L."
DELAUNAY_L_TYPE_TEMP.L_OVER_SQRT_MU_TEMP.__doc__ = "Use L/SQRT(mu)."

agcls.AgTypeNameMap["DELAUNAY_L_TYPE_TEMP"] = DELAUNAY_L_TYPE_TEMP

class DELAUNAY_H_TYPE_TEMP(IntEnum):
    """Select whether to use the default representation of Delaunay H or H/SQRT(mu)."""
    UNKNOWN_TEMP = -1
    """Represents a value not supported by the Object Model"""
    H_TEMP = 0
    """Use the default representation of H."""
    H_OVER_SQRT_MU_TEMP = 1
    """H/SQRT(mu)."""

DELAUNAY_H_TYPE_TEMP.UNKNOWN_TEMP.__doc__ = "Represents a value not supported by the Object Model"
DELAUNAY_H_TYPE_TEMP.H_TEMP.__doc__ = "Use the default representation of H."
DELAUNAY_H_TYPE_TEMP.H_OVER_SQRT_MU_TEMP.__doc__ = "H/SQRT(mu)."

agcls.AgTypeNameMap["DELAUNAY_H_TYPE_TEMP"] = DELAUNAY_H_TYPE_TEMP

class DELAUNAY_G_TYPE_TEMP(IntEnum):
    """Select whether to use the default representation of Delaunay G or G/SQRT(mu)."""
    UNKNOWN_TEMP = -1
    """Represents a value not supported by the Object Model"""
    G_TEMP = 0
    """Use the default representation of G."""
    G_OVER_SQRT_MU_TEMP = 1
    """Use G/SQRT(mu)."""

DELAUNAY_G_TYPE_TEMP.UNKNOWN_TEMP.__doc__ = "Represents a value not supported by the Object Model"
DELAUNAY_G_TYPE_TEMP.G_TEMP.__doc__ = "Use the default representation of G."
DELAUNAY_G_TYPE_TEMP.G_OVER_SQRT_MU_TEMP.__doc__ = "Use G/SQRT(mu)."

agcls.AgTypeNameMap["DELAUNAY_G_TYPE_TEMP"] = DELAUNAY_G_TYPE_TEMP

class LOG_MSG_TYPE(IntEnum):
    """Log message types."""
    DEBUG = 0
    """Debugging message."""
    INFO = 1
    """Informational message."""
    FORCE_INFO = 2
    """Informational message."""
    WARNING = 3
    """Warning message."""
    ALARM = 4
    """Alarm message."""

LOG_MSG_TYPE.DEBUG.__doc__ = "Debugging message."
LOG_MSG_TYPE.INFO.__doc__ = "Informational message."
LOG_MSG_TYPE.FORCE_INFO.__doc__ = "Informational message."
LOG_MSG_TYPE.WARNING.__doc__ = "Warning message."
LOG_MSG_TYPE.ALARM.__doc__ = "Alarm message."

agcls.AgTypeNameMap["LOG_MSG_TYPE"] = LOG_MSG_TYPE

class LOG_MSG_DISP_ID(IntEnum):
    """Log message destination options."""
    ALL = -1
    """STK displays the message in all the log destination."""
    DEFAULT = 0
    """STK displays the message in the default log destination."""
    MSG_WIN = 1
    """STK displays the message in the message window."""
    STATUS_BAR = 2
    """STK displays the message in the status bar."""

LOG_MSG_DISP_ID.ALL.__doc__ = "STK displays the message in all the log destination."
LOG_MSG_DISP_ID.DEFAULT.__doc__ = "STK displays the message in the default log destination."
LOG_MSG_DISP_ID.MSG_WIN.__doc__ = "STK displays the message in the message window."
LOG_MSG_DISP_ID.STATUS_BAR.__doc__ = "STK displays the message in the status bar."

agcls.AgTypeNameMap["LOG_MSG_DISP_ID"] = LOG_MSG_DISP_ID

class LINE_STYLE(IntEnum):
    """Line Style"""
    SOLID = 0
    """Specifies a solid line."""
    DASHED = 1
    """Specifies a dashed line."""
    DOTTED = 2
    """Specifies a dotted line."""
    DOT_DASHED = 3
    """Dot-dashed line."""
    LONG_DASHED = 4
    """Specifies a long dashed line."""
    DASH_DOT_DOTTED = 5
    """Specifies an alternating dash-dot-dot line."""
    M_DASH = 6
    """Specifies a user configurable medium dashed line."""
    L_DASH = 7
    """Specifies a user configurable long dashed line."""
    S_DASH_DOT = 8
    """Specifies a user configurable small dash-dotted line."""
    M_DASH_DOT = 9
    """Specifies a user configurable medium dash-dotted line."""
    DASH_DOT = 10
    """Specifies a user configurable long dash-dotted line."""
    MS_DASH = 11
    """Specifies a user configurable medium followed by small dashed line."""
    LS_DASH = 12
    """Specifies a user configurable long followed by small dashed line."""
    LM_DASH = 13
    """Specifies a user configurable long followed by medium dashed line."""
    LMS_DASH = 14
    """Specifies a user configurable medium followed by small dashed line."""
    DOT = 15
    """Specifies a dotted line."""
    LONG_DASH = 16
    """Specifies a long dashed line."""
    S_DASH = 17
    """Specifies an alternating dash-dot line."""

LINE_STYLE.SOLID.__doc__ = "Specifies a solid line."
LINE_STYLE.DASHED.__doc__ = "Specifies a dashed line."
LINE_STYLE.DOTTED.__doc__ = "Specifies a dotted line."
LINE_STYLE.DOT_DASHED.__doc__ = "Dot-dashed line."
LINE_STYLE.LONG_DASHED.__doc__ = "Specifies a long dashed line."
LINE_STYLE.DASH_DOT_DOTTED.__doc__ = "Specifies an alternating dash-dot-dot line."
LINE_STYLE.M_DASH.__doc__ = "Specifies a user configurable medium dashed line."
LINE_STYLE.L_DASH.__doc__ = "Specifies a user configurable long dashed line."
LINE_STYLE.S_DASH_DOT.__doc__ = "Specifies a user configurable small dash-dotted line."
LINE_STYLE.M_DASH_DOT.__doc__ = "Specifies a user configurable medium dash-dotted line."
LINE_STYLE.DASH_DOT.__doc__ = "Specifies a user configurable long dash-dotted line."
LINE_STYLE.MS_DASH.__doc__ = "Specifies a user configurable medium followed by small dashed line."
LINE_STYLE.LS_DASH.__doc__ = "Specifies a user configurable long followed by small dashed line."
LINE_STYLE.LM_DASH.__doc__ = "Specifies a user configurable long followed by medium dashed line."
LINE_STYLE.LMS_DASH.__doc__ = "Specifies a user configurable medium followed by small dashed line."
LINE_STYLE.DOT.__doc__ = "Specifies a dotted line."
LINE_STYLE.LONG_DASH.__doc__ = "Specifies a long dashed line."
LINE_STYLE.S_DASH.__doc__ = "Specifies an alternating dash-dot line."

agcls.AgTypeNameMap["LINE_STYLE"] = LINE_STYLE

class EXEC_MULTI_CMD_RESULT_ACTION(IntFlag):
    """Enumeration defines a set of actions when an error occurs while executing a command batch."""
    CONTINUE_ON_ERROR = 0
    """Continue executing the remaining commands in the command batch."""
    STOP_ON_ERROR = 1
    """Terminate the execution of the command batch but do not throw an exception."""
    EXCEPTION_ON_ERROR = 2
    """Terminate the execution of the command batch and throw an exception."""
    IGNORE_EXEC_CMD_RESULT = 0x8000
    """Ignore results returned by individual commands. The option must be used in combination with other flags."""

EXEC_MULTI_CMD_RESULT_ACTION.CONTINUE_ON_ERROR.__doc__ = "Continue executing the remaining commands in the command batch."
EXEC_MULTI_CMD_RESULT_ACTION.STOP_ON_ERROR.__doc__ = "Terminate the execution of the command batch but do not throw an exception."
EXEC_MULTI_CMD_RESULT_ACTION.EXCEPTION_ON_ERROR.__doc__ = "Terminate the execution of the command batch and throw an exception."
EXEC_MULTI_CMD_RESULT_ACTION.IGNORE_EXEC_CMD_RESULT.__doc__ = "Ignore results returned by individual commands. The option must be used in combination with other flags."

agcls.AgTypeNameMap["EXEC_MULTI_CMD_RESULT_ACTION"] = EXEC_MULTI_CMD_RESULT_ACTION

class FILL_STYLE(IntEnum):
    """Fill Style"""
    SOLID = 0
    """Specifies a solid fill style."""
    HORIZONTAL_STRIPE = 1
    """Specifies a horizontally striped fill style."""
    DIAGONAL_STRIPE1 = 2
    """Specifies a diagonally striped fill style."""
    DIAGONAL_STRIPE2 = 3
    """Specifies a diagonally striped fill style."""
    HATCH = 4
    """Specifies a hatched fill style."""
    DIAGONAL_HATCH = 5
    """Specifies a diagonally hatched fill style."""
    SCREEN = 6
    """Specifies a special fill style where every other pixel is drawn."""
    VERTICAL_STRIPE = 7
    """Specifies a vertically striped fill style."""

FILL_STYLE.SOLID.__doc__ = "Specifies a solid fill style."
FILL_STYLE.HORIZONTAL_STRIPE.__doc__ = "Specifies a horizontally striped fill style."
FILL_STYLE.DIAGONAL_STRIPE1.__doc__ = "Specifies a diagonally striped fill style."
FILL_STYLE.DIAGONAL_STRIPE2.__doc__ = "Specifies a diagonally striped fill style."
FILL_STYLE.HATCH.__doc__ = "Specifies a hatched fill style."
FILL_STYLE.DIAGONAL_HATCH.__doc__ = "Specifies a diagonally hatched fill style."
FILL_STYLE.SCREEN.__doc__ = "Specifies a special fill style where every other pixel is drawn."
FILL_STYLE.VERTICAL_STRIPE.__doc__ = "Specifies a vertically striped fill style."

agcls.AgTypeNameMap["FILL_STYLE"] = FILL_STYLE

class PROPERTY_INFO_VALUE_TYPE(IntEnum):
    """The enumeration used to determine what type of property is being used."""
    INT = 0
    """Property is of type int."""
    REAL = 1
    """Property is of type real."""
    QUANTITY = 2
    """Property is of type Quantity."""
    DATE = 3
    """Property is of type Date."""
    STRING = 4
    """Property is of type string."""
    BOOL = 5
    """Property is of type bool."""
    INTERFACE = 6
    """Property is an interface."""

PROPERTY_INFO_VALUE_TYPE.INT.__doc__ = "Property is of type int."
PROPERTY_INFO_VALUE_TYPE.REAL.__doc__ = "Property is of type real."
PROPERTY_INFO_VALUE_TYPE.QUANTITY.__doc__ = "Property is of type Quantity."
PROPERTY_INFO_VALUE_TYPE.DATE.__doc__ = "Property is of type Date."
PROPERTY_INFO_VALUE_TYPE.STRING.__doc__ = "Property is of type string."
PROPERTY_INFO_VALUE_TYPE.BOOL.__doc__ = "Property is of type bool."
PROPERTY_INFO_VALUE_TYPE.INTERFACE.__doc__ = "Property is an interface."

agcls.AgTypeNameMap["PROPERTY_INFO_VALUE_TYPE"] = PROPERTY_INFO_VALUE_TYPE


class ILocationData(object):
    """Base interface Position. IPosition derives from this interface."""
    _num_methods = 0
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{C1E99EDA-C666-4971-AFD0-2259CB7E8452}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : {  }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ILocationData._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ILocationData from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ILocationData.__dict__ and type(ILocationData.__dict__[attrname]) == property:
            return ILocationData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ILocationData.")
    

agcls.AgClassCatalog.add_catalog_entry("{C1E99EDA-C666-4971-AFD0-2259CB7E8452}", ILocationData)
agcls.AgTypeNameMap["ILocationData"] = ILocationData

class IPosition(object):
    """IPosition provides access to the position of the object"""
    _num_methods = 21
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{F25960CE-1D73-4BA0-A429-541DD6D808DE}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "convert_to" : 1,
                             "get_position_type" : 2,
                             "assign" : 3,
                             "assign_geocentric" : 4,
                             "assign_geodetic" : 5,
                             "assign_spherical" : 6,
                             "assign_cylindrical" : 7,
                             "assign_cartesian" : 8,
                             "assign_planetocentric" : 9,
                             "assign_planetodetic" : 10,
                             "query_planetocentric" : 11,
                             "query_planetodetic" : 12,
                             "query_spherical" : 13,
                             "query_cylindrical" : 14,
                             "query_cartesian" : 15,
                             "get_central_body_name" : 16,
                             "query_planetocentric_array" : 17,
                             "query_planetodetic_array" : 18,
                             "query_spherical_array" : 19,
                             "query_cylindrical_array" : 20,
                             "query_cartesian_array" : 21, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IPosition._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IPosition from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IPosition.__dict__ and type(IPosition.__dict__[attrname]) == property:
            return IPosition.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IPosition.")
    
    _convert_to_metadata = { "name" : "convert_to",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgEnum_arg(POSITION_TYPE), agmarshall.AgInterface_out_arg,) }
    def convert_to(self, type:"POSITION_TYPE") -> "IPosition":
        """Changes the position coordinates to type specified."""
        return self._intf.invoke(IPosition._metadata, IPosition._convert_to_metadata, type, out_arg())

    _get_position_type_metadata = { "name" : "position_type",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(POSITION_TYPE),) }
    @property
    def position_type(self) -> "POSITION_TYPE":
        """Gets the type of position currently being used."""
        return self._intf.get_property(IPosition._metadata, IPosition._get_position_type_metadata)

    _assign_metadata = { "name" : "assign",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.AgInterface_in_arg("IPosition"),) }
    def assign(self, pPosition:"IPosition") -> None:
        """This assigns the coordinates into the system."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_metadata, pPosition)

    _assign_geocentric_metadata = { "name" : "assign_geocentric",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def assign_geocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Geocentric representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_geocentric_metadata, lat, lon, alt)

    _assign_geodetic_metadata = { "name" : "assign_geodetic",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def assign_geodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Geodetic representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_geodetic_metadata, lat, lon, alt)

    _assign_spherical_metadata = { "name" : "assign_spherical",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def assign_spherical(self, lat:typing.Any, lon:typing.Any, radius:float) -> None:
        """Helper method to assign the position using the Spherical representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_spherical_metadata, lat, lon, radius)

    _assign_cylindrical_metadata = { "name" : "assign_cylindrical",
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.VARIANT,),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.VARIANT_arg,) }
    def assign_cylindrical(self, radius:float, z:float, lon:typing.Any) -> None:
        """Helper method to assign the position using the Cylindrical representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_cylindrical_metadata, radius, z, lon)

    _assign_cartesian_metadata = { "name" : "assign_cartesian",
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_cartesian(self, x:float, y:float, z:float) -> None:
        """Helper method to assign the position using the Cartesian representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_cartesian_metadata, x, y, z)

    _assign_planetocentric_metadata = { "name" : "assign_planetocentric",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def assign_planetocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Planetocentric representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_planetocentric_metadata, lat, lon, alt)

    _assign_planetodetic_metadata = { "name" : "assign_planetodetic",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def assign_planetodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Planetodetic representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_planetodetic_metadata, lat, lon, alt)

    _query_planetocentric_metadata = { "name" : "query_planetocentric",
            "arg_types" : (POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def query_planetocentric(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Planetocentric representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetocentric_metadata, out_arg(), out_arg(), out_arg())

    _query_planetodetic_metadata = { "name" : "query_planetodetic",
            "arg_types" : (POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def query_planetodetic(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Planetodetic representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetodetic_metadata, out_arg(), out_arg(), out_arg())

    _query_spherical_metadata = { "name" : "query_spherical",
            "arg_types" : (POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def query_spherical(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Spherical representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._query_spherical_metadata, out_arg(), out_arg(), out_arg())

    _query_cylindrical_metadata = { "name" : "query_cylindrical",
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.VARIANT_arg, agmarshall.DOUBLE_arg,) }
    def query_cylindrical(self) -> typing.Tuple[float, typing.Any, float]:
        """Helper method to get the position using the Cylindrical representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cylindrical_metadata, out_arg(), out_arg(), out_arg())

    _query_cartesian_metadata = { "name" : "query_cartesian",
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def query_cartesian(self) -> typing.Tuple[float, float, float]:
        """Helper method to get the position using the Cartesian representation"""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cartesian_metadata, out_arg(), out_arg(), out_arg())

    _get_central_body_name_metadata = { "name" : "central_body_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def central_body_name(self) -> str:
        """Gets the central body."""
        return self._intf.get_property(IPosition._metadata, IPosition._get_central_body_name_metadata)

    _query_planetocentric_array_metadata = { "name" : "query_planetocentric_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_planetocentric_array(self) -> list:
        """Returns the Planetocentric elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetocentric_array_metadata, out_arg())

    _query_planetodetic_array_metadata = { "name" : "query_planetodetic_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_planetodetic_array(self) -> list:
        """Returns the Planetodetic elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetodetic_array_metadata, out_arg())

    _query_spherical_array_metadata = { "name" : "query_spherical_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_spherical_array(self) -> list:
        """Returns the Spherical elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_spherical_array_metadata, out_arg())

    _query_cylindrical_array_metadata = { "name" : "query_cylindrical_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_cylindrical_array(self) -> list:
        """Returns the Cylindrical elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cylindrical_array_metadata, out_arg())

    _query_cartesian_array_metadata = { "name" : "query_cartesian_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_cartesian_array(self) -> list:
        """Returns the Cartesian elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cartesian_array_metadata, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{F25960CE-1D73-4BA0-A429-541DD6D808DE}", IPosition)
agcls.AgTypeNameMap["IPosition"] = IPosition

class IPlanetocentric(IPosition):
    """Planetocentric Position Type."""
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _metadata = {
        "uuid" : "{605061D3-5594-4B88-AC0A-D4EA90EFFAA1}",
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
        "method_offsets" : { "get_lat" : 1,
                             "set_lat" : 2,
                             "get_lon" : 3,
                             "set_lon" : 4,
                             "get_altitude" : 5,
                             "set_altitude" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IPlanetocentric._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IPlanetocentric from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IPlanetocentric.__dict__ and type(IPlanetocentric.__dict__[attrname]) == property:
            return IPlanetocentric.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IPosition.__setattr__(self, attrname, value)
    
    _get_lat_metadata = { "name" : "lat",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        return self._intf.get_property(IPlanetocentric._metadata, IPlanetocentric._get_lat_metadata)

    _set_lat_metadata = { "name" : "lat",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lat.setter
    def lat(self, pVal:typing.Any) -> None:
        return self._intf.set_property(IPlanetocentric._metadata, IPlanetocentric._set_lat_metadata, pVal)

    _get_lon_metadata = { "name" : "lon",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        return self._intf.get_property(IPlanetocentric._metadata, IPlanetocentric._get_lon_metadata)

    _set_lon_metadata = { "name" : "lon",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        return self._intf.set_property(IPlanetocentric._metadata, IPlanetocentric._set_lon_metadata, pVal)

    _get_altitude_metadata = { "name" : "altitude",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def altitude(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(IPlanetocentric._metadata, IPlanetocentric._get_altitude_metadata)

    _set_altitude_metadata = { "name" : "altitude",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @altitude.setter
    def altitude(self, pVal:float) -> None:
        return self._intf.set_property(IPlanetocentric._metadata, IPlanetocentric._set_altitude_metadata, pVal)


agcls.AgClassCatalog.add_catalog_entry("{605061D3-5594-4B88-AC0A-D4EA90EFFAA1}", IPlanetocentric)
agcls.AgTypeNameMap["IPlanetocentric"] = IPlanetocentric

class IGeocentric(IPosition):
    """Geocentric Position Type."""
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _metadata = {
        "uuid" : "{7D22F2C8-81B1-452E-AA06-0AEEB1FDF0F9}",
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
        "method_offsets" : { "get_lat" : 1,
                             "set_lat" : 2,
                             "get_lon" : 3,
                             "set_lon" : 4,
                             "get_altitude" : 5,
                             "set_altitude" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IGeocentric._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IGeocentric from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IGeocentric.__dict__ and type(IGeocentric.__dict__[attrname]) == property:
            return IGeocentric.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IPosition.__setattr__(self, attrname, value)
    
    _get_lat_metadata = { "name" : "lat",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        return self._intf.get_property(IGeocentric._metadata, IGeocentric._get_lat_metadata)

    _set_lat_metadata = { "name" : "lat",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lat.setter
    def lat(self, pVal:typing.Any) -> None:
        return self._intf.set_property(IGeocentric._metadata, IGeocentric._set_lat_metadata, pVal)

    _get_lon_metadata = { "name" : "lon",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        return self._intf.get_property(IGeocentric._metadata, IGeocentric._get_lon_metadata)

    _set_lon_metadata = { "name" : "lon",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        return self._intf.set_property(IGeocentric._metadata, IGeocentric._set_lon_metadata, pVal)

    _get_altitude_metadata = { "name" : "altitude",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def altitude(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(IGeocentric._metadata, IGeocentric._get_altitude_metadata)

    _set_altitude_metadata = { "name" : "altitude",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @altitude.setter
    def altitude(self, pVal:float) -> None:
        return self._intf.set_property(IGeocentric._metadata, IGeocentric._set_altitude_metadata, pVal)


agcls.AgClassCatalog.add_catalog_entry("{7D22F2C8-81B1-452E-AA06-0AEEB1FDF0F9}", IGeocentric)
agcls.AgTypeNameMap["IGeocentric"] = IGeocentric

class ISpherical(IPosition):
    """Spherical Position Type."""
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _metadata = {
        "uuid" : "{62B93DF1-C615-4363-B4D9-DAA1ACE56204}",
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
        "method_offsets" : { "get_lat" : 1,
                             "set_lat" : 2,
                             "get_lon" : 3,
                             "set_lon" : 4,
                             "get_radius" : 5,
                             "set_radius" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ISpherical._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ISpherical from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ISpherical.__dict__ and type(ISpherical.__dict__[attrname]) == property:
            return ISpherical.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IPosition.__setattr__(self, attrname, value)
    
    _get_lat_metadata = { "name" : "lat",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        return self._intf.get_property(ISpherical._metadata, ISpherical._get_lat_metadata)

    _set_lat_metadata = { "name" : "lat",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lat.setter
    def lat(self, pVal:typing.Any) -> None:
        return self._intf.set_property(ISpherical._metadata, ISpherical._set_lat_metadata, pVal)

    _get_lon_metadata = { "name" : "lon",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        return self._intf.get_property(ISpherical._metadata, ISpherical._get_lon_metadata)

    _set_lon_metadata = { "name" : "lon",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        return self._intf.set_property(ISpherical._metadata, ISpherical._set_lon_metadata, pVal)

    _get_radius_metadata = { "name" : "radius",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def radius(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(ISpherical._metadata, ISpherical._get_radius_metadata)

    _set_radius_metadata = { "name" : "radius",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @radius.setter
    def radius(self, pVal:float) -> None:
        return self._intf.set_property(ISpherical._metadata, ISpherical._set_radius_metadata, pVal)


agcls.AgClassCatalog.add_catalog_entry("{62B93DF1-C615-4363-B4D9-DAA1ACE56204}", ISpherical)
agcls.AgTypeNameMap["ISpherical"] = ISpherical

class ICylindrical(IPosition):
    """Cylindrical Position Type."""
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _metadata = {
        "uuid" : "{36F08499-F7C4-41DE-AB49-794EC65C5165}",
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
        "method_offsets" : { "get_radius" : 1,
                             "set_radius" : 2,
                             "get_z" : 3,
                             "set_z" : 4,
                             "get_lon" : 5,
                             "set_lon" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ICylindrical._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ICylindrical from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ICylindrical.__dict__ and type(ICylindrical.__dict__[attrname]) == property:
            return ICylindrical.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IPosition.__setattr__(self, attrname, value)
    
    _get_radius_metadata = { "name" : "radius",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def radius(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(ICylindrical._metadata, ICylindrical._get_radius_metadata)

    _set_radius_metadata = { "name" : "radius",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @radius.setter
    def radius(self, pVal:float) -> None:
        return self._intf.set_property(ICylindrical._metadata, ICylindrical._set_radius_metadata, pVal)

    _get_z_metadata = { "name" : "z",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def z(self) -> float:
        """Uses Angle Dimension."""
        return self._intf.get_property(ICylindrical._metadata, ICylindrical._get_z_metadata)

    _set_z_metadata = { "name" : "z",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @z.setter
    def z(self, pVal:float) -> None:
        return self._intf.set_property(ICylindrical._metadata, ICylindrical._set_z_metadata, pVal)

    _get_lon_metadata = { "name" : "lon",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lon(self) -> typing.Any:
        """Dimension depends on context."""
        return self._intf.get_property(ICylindrical._metadata, ICylindrical._get_lon_metadata)

    _set_lon_metadata = { "name" : "lon",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        return self._intf.set_property(ICylindrical._metadata, ICylindrical._set_lon_metadata, pVal)


agcls.AgClassCatalog.add_catalog_entry("{36F08499-F7C4-41DE-AB49-794EC65C5165}", ICylindrical)
agcls.AgTypeNameMap["ICylindrical"] = ICylindrical

class ICartesian(IPosition):
    """Cartesian Interface used to access a position using Cartesian Coordinates"""
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _metadata = {
        "uuid" : "{F6D3AD94-04C0-464E-8B95-8A859AA1BCA7}",
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
        "method_offsets" : { "get_x" : 1,
                             "set_x" : 2,
                             "get_y" : 3,
                             "set_y" : 4,
                             "get_z" : 5,
                             "set_z" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ICartesian._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ICartesian from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ICartesian.__dict__ and type(ICartesian.__dict__[attrname]) == property:
            return ICartesian.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IPosition.__setattr__(self, attrname, value)
    
    _get_x_metadata = { "name" : "x",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def x(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(ICartesian._metadata, ICartesian._get_x_metadata)

    _set_x_metadata = { "name" : "x",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @x.setter
    def x(self, pVal:float) -> None:
        return self._intf.set_property(ICartesian._metadata, ICartesian._set_x_metadata, pVal)

    _get_y_metadata = { "name" : "y",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def y(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(ICartesian._metadata, ICartesian._get_y_metadata)

    _set_y_metadata = { "name" : "y",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @y.setter
    def y(self, pVal:float) -> None:
        return self._intf.set_property(ICartesian._metadata, ICartesian._set_y_metadata, pVal)

    _get_z_metadata = { "name" : "z",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def z(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(ICartesian._metadata, ICartesian._get_z_metadata)

    _set_z_metadata = { "name" : "z",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @z.setter
    def z(self, pVal:float) -> None:
        return self._intf.set_property(ICartesian._metadata, ICartesian._set_z_metadata, pVal)


agcls.AgClassCatalog.add_catalog_entry("{F6D3AD94-04C0-464E-8B95-8A859AA1BCA7}", ICartesian)
agcls.AgTypeNameMap["ICartesian"] = ICartesian

class IGeodetic(IPosition):
    """Geodetic sets the position using Geodetic properties."""
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _metadata = {
        "uuid" : "{93D3322B-C842-48D2-AFCF-BC42B59DB28E}",
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
        "method_offsets" : { "get_lat" : 1,
                             "set_lat" : 2,
                             "get_lon" : 3,
                             "set_lon" : 4,
                             "get_altitude" : 5,
                             "set_altitude" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IGeodetic._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IGeodetic from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IGeodetic.__dict__ and type(IGeodetic.__dict__[attrname]) == property:
            return IGeodetic.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IPosition.__setattr__(self, attrname, value)
    
    _get_lat_metadata = { "name" : "lat",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lat(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        return self._intf.get_property(IGeodetic._metadata, IGeodetic._get_lat_metadata)

    _set_lat_metadata = { "name" : "lat",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lat.setter
    def lat(self, pLat:typing.Any) -> None:
        return self._intf.set_property(IGeodetic._metadata, IGeodetic._set_lat_metadata, pLat)

    _get_lon_metadata = { "name" : "lon",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lon(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        return self._intf.get_property(IGeodetic._metadata, IGeodetic._get_lon_metadata)

    _set_lon_metadata = { "name" : "lon",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lon.setter
    def lon(self, pLon:typing.Any) -> None:
        return self._intf.set_property(IGeodetic._metadata, IGeodetic._set_lon_metadata, pLon)

    _get_altitude_metadata = { "name" : "altitude",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def altitude(self) -> float:
        """Altitude. Dimension depends on context."""
        return self._intf.get_property(IGeodetic._metadata, IGeodetic._get_altitude_metadata)

    _set_altitude_metadata = { "name" : "altitude",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @altitude.setter
    def altitude(self, pAlt:float) -> None:
        return self._intf.set_property(IGeodetic._metadata, IGeodetic._set_altitude_metadata, pAlt)


agcls.AgClassCatalog.add_catalog_entry("{93D3322B-C842-48D2-AFCF-BC42B59DB28E}", IGeodetic)
agcls.AgTypeNameMap["IGeodetic"] = IGeodetic

class IPlanetodetic(IPosition):
    """Planetodetic sets the position using Planetodetic properties."""
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _metadata = {
        "uuid" : "{E0F982B1-7B17-40F7-B64B-AFD0D112A74C}",
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
        "method_offsets" : { "get_lat" : 1,
                             "set_lat" : 2,
                             "get_lon" : 3,
                             "set_lon" : 4,
                             "get_altitude" : 5,
                             "set_altitude" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IPlanetodetic._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IPlanetodetic from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IPlanetodetic.__dict__ and type(IPlanetodetic.__dict__[attrname]) == property:
            return IPlanetodetic.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IPosition.__setattr__(self, attrname, value)
    
    _get_lat_metadata = { "name" : "lat",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lat(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        return self._intf.get_property(IPlanetodetic._metadata, IPlanetodetic._get_lat_metadata)

    _set_lat_metadata = { "name" : "lat",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lat.setter
    def lat(self, pLat:typing.Any) -> None:
        return self._intf.set_property(IPlanetodetic._metadata, IPlanetodetic._set_lat_metadata, pLat)

    _get_lon_metadata = { "name" : "lon",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def lon(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        return self._intf.get_property(IPlanetodetic._metadata, IPlanetodetic._get_lon_metadata)

    _set_lon_metadata = { "name" : "lon",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @lon.setter
    def lon(self, pLon:typing.Any) -> None:
        return self._intf.set_property(IPlanetodetic._metadata, IPlanetodetic._set_lon_metadata, pLon)

    _get_altitude_metadata = { "name" : "altitude",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def altitude(self) -> float:
        """Altitude. Dimension depends on context."""
        return self._intf.get_property(IPlanetodetic._metadata, IPlanetodetic._get_altitude_metadata)

    _set_altitude_metadata = { "name" : "altitude",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @altitude.setter
    def altitude(self, pAlt:float) -> None:
        return self._intf.set_property(IPlanetodetic._metadata, IPlanetodetic._set_altitude_metadata, pAlt)


agcls.AgClassCatalog.add_catalog_entry("{E0F982B1-7B17-40F7-B64B-AFD0D112A74C}", IPlanetodetic)
agcls.AgTypeNameMap["IPlanetodetic"] = IPlanetodetic

class IDirection(object):
    """Interface to set and retrieve direction options for aligned and constrained vectors."""
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{8304507A-4915-453D-8944-2080659C0257}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "convert_to" : 1,
                             "get_direction_type" : 2,
                             "assign" : 3,
                             "assign_euler" : 4,
                             "assign_pr" : 5,
                             "assign_ra_dec" : 6,
                             "assign_xyz" : 7,
                             "query_euler" : 8,
                             "query_pr" : 9,
                             "query_ra_dec" : 10,
                             "query_xyz" : 11,
                             "query_euler_array" : 12,
                             "query_pr_array" : 13,
                             "query_ra_dec_array" : 14,
                             "query_xyz_array" : 15, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDirection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDirection from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDirection.__dict__ and type(IDirection.__dict__[attrname]) == property:
            return IDirection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IDirection.")
    
    _convert_to_metadata = { "name" : "convert_to",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgEnum_arg(DIRECTION_TYPE), agmarshall.AgInterface_out_arg,) }
    def convert_to(self, type:"DIRECTION_TYPE") -> "IDirection":
        """Method to changes the direction to the type specified."""
        return self._intf.invoke(IDirection._metadata, IDirection._convert_to_metadata, type, out_arg())

    _get_direction_type_metadata = { "name" : "direction_type",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(DIRECTION_TYPE),) }
    @property
    def direction_type(self) -> "DIRECTION_TYPE":
        """Returns the type of direction currently being used."""
        return self._intf.get_property(IDirection._metadata, IDirection._get_direction_type_metadata)

    _assign_metadata = { "name" : "assign",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.AgInterface_in_arg("IDirection"),) }
    def assign(self, pDirection:"IDirection") -> None:
        """Assign a new direction."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_metadata, pDirection)

    _assign_euler_metadata = { "name" : "assign_euler",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT, agcom.LONG,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE),) }
    def assign_euler(self, b:typing.Any, c:typing.Any, sequence:"EULER_DIRECTION_SEQUENCE") -> None:
        """Helper method to set direction using the Euler representation. Params B and C use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_euler_metadata, b, c, sequence)

    _assign_pr_metadata = { "name" : "assign_pr",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def assign_pr(self, pitch:typing.Any, roll:typing.Any) -> None:
        """Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_pr_metadata, pitch, roll)

    _assign_ra_dec_metadata = { "name" : "assign_ra_dec",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def assign_ra_dec(self, ra:typing.Any, dec:typing.Any) -> None:
        """Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_ra_dec_metadata, ra, dec)

    _assign_xyz_metadata = { "name" : "assign_xyz",
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_xyz(self, x:float, y:float, z:float) -> None:
        """Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_xyz_metadata, x, y, z)

    _query_euler_metadata = { "name" : "query_euler",
            "arg_types" : (agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE), agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def query_euler(self, sequence:"EULER_DIRECTION_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Euler representation. Params B and C use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_euler_metadata, sequence, out_arg(), out_arg())

    _query_pr_metadata = { "name" : "query_pr",
            "arg_types" : (agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.AgEnum_arg(PR_SEQUENCE), agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def query_pr(self, sequence:"PR_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_pr_metadata, sequence, out_arg(), out_arg())

    _query_ra_dec_metadata = { "name" : "query_ra_dec",
            "arg_types" : (POINTER(agcom.VARIANT), POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def query_ra_dec(self) -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_ra_dec_metadata, out_arg(), out_arg())

    _query_xyz_metadata = { "name" : "query_xyz",
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def query_xyz(self) -> typing.Tuple[float, float, float]:
        """Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_xyz_metadata, out_arg(), out_arg(), out_arg())

    _query_euler_array_metadata = { "name" : "query_euler_array",
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE), agmarshall.LPSAFEARRAY_arg,) }
    def query_euler_array(self, sequence:"EULER_DIRECTION_SEQUENCE") -> list:
        """Returns the Euler elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_euler_array_metadata, sequence, out_arg())

    _query_pr_array_metadata = { "name" : "query_pr_array",
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.AgEnum_arg(PR_SEQUENCE), agmarshall.LPSAFEARRAY_arg,) }
    def query_pr_array(self, sequence:"PR_SEQUENCE") -> list:
        """Returns the PR elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_pr_array_metadata, sequence, out_arg())

    _query_ra_dec_array_metadata = { "name" : "query_ra_dec_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_ra_dec_array(self) -> list:
        """Returns the RADec elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_ra_dec_array_metadata, out_arg())

    _query_xyz_array_metadata = { "name" : "query_xyz_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_xyz_array(self) -> list:
        """Returns the XYZ elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_xyz_array_metadata, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{8304507A-4915-453D-8944-2080659C0257}", IDirection)
agcls.AgTypeNameMap["IDirection"] = IDirection

class IDirectionEuler(IDirection):
    """Interface for Euler direction sequence."""
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _metadata = {
        "uuid" : "{9CBDC138-72D1-4734-8F95-2140266D37B5}",
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
        "method_offsets" : { "get_b" : 1,
                             "set_b" : 2,
                             "get_c" : 3,
                             "set_c" : 4,
                             "get_sequence" : 5,
                             "set_sequence" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDirectionEuler._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDirectionEuler from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDirectionEuler.__dict__ and type(IDirectionEuler.__dict__[attrname]) == property:
            return IDirectionEuler.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IDirection.__setattr__(self, attrname, value)
    
    _get_b_metadata = { "name" : "b",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def b(self) -> typing.Any:
        """Euler B angle. Uses Angle Dimension."""
        return self._intf.get_property(IDirectionEuler._metadata, IDirectionEuler._get_b_metadata)

    _set_b_metadata = { "name" : "b",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @b.setter
    def b(self, va:typing.Any) -> None:
        return self._intf.set_property(IDirectionEuler._metadata, IDirectionEuler._set_b_metadata, va)

    _get_c_metadata = { "name" : "c",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def c(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        return self._intf.get_property(IDirectionEuler._metadata, IDirectionEuler._get_c_metadata)

    _set_c_metadata = { "name" : "c",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @c.setter
    def c(self, vb:typing.Any) -> None:
        return self._intf.set_property(IDirectionEuler._metadata, IDirectionEuler._set_c_metadata, vb)

    _get_sequence_metadata = { "name" : "sequence",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE),) }
    @property
    def sequence(self) -> "EULER_DIRECTION_SEQUENCE":
        """Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified."""
        return self._intf.get_property(IDirectionEuler._metadata, IDirectionEuler._get_sequence_metadata)

    _set_sequence_metadata = { "name" : "sequence",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE),) }
    @sequence.setter
    def sequence(self, sequence:"EULER_DIRECTION_SEQUENCE") -> None:
        return self._intf.set_property(IDirectionEuler._metadata, IDirectionEuler._set_sequence_metadata, sequence)


agcls.AgClassCatalog.add_catalog_entry("{9CBDC138-72D1-4734-8F95-2140266D37B5}", IDirectionEuler)
agcls.AgTypeNameMap["IDirectionEuler"] = IDirectionEuler

class IDirectionPR(IDirection):
    """Interface for Pitch-Roll (PR) direction sequence."""
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _metadata = {
        "uuid" : "{5AC01BF1-2B95-4C13-8B69-09FDC485330E}",
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
        "method_offsets" : { "get_pitch" : 1,
                             "set_pitch" : 2,
                             "get_roll" : 3,
                             "set_roll" : 4,
                             "get_sequence" : 5,
                             "set_sequence" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDirectionPR._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDirectionPR from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDirectionPR.__dict__ and type(IDirectionPR.__dict__[attrname]) == property:
            return IDirectionPR.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IDirection.__setattr__(self, attrname, value)
    
    _get_pitch_metadata = { "name" : "pitch",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        return self._intf.get_property(IDirectionPR._metadata, IDirectionPR._get_pitch_metadata)

    _set_pitch_metadata = { "name" : "pitch",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @pitch.setter
    def pitch(self, vPitch:typing.Any) -> None:
        return self._intf.set_property(IDirectionPR._metadata, IDirectionPR._set_pitch_metadata, vPitch)

    _get_roll_metadata = { "name" : "roll",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        return self._intf.get_property(IDirectionPR._metadata, IDirectionPR._get_roll_metadata)

    _set_roll_metadata = { "name" : "roll",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @roll.setter
    def roll(self, vRoll:typing.Any) -> None:
        return self._intf.set_property(IDirectionPR._metadata, IDirectionPR._set_roll_metadata, vRoll)

    _get_sequence_metadata = { "name" : "sequence",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(PR_SEQUENCE),) }
    @property
    def sequence(self) -> "PR_SEQUENCE":
        """PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified."""
        return self._intf.get_property(IDirectionPR._metadata, IDirectionPR._get_sequence_metadata)

    _set_sequence_metadata = { "name" : "sequence",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(PR_SEQUENCE),) }
    @sequence.setter
    def sequence(self, sequence:"PR_SEQUENCE") -> None:
        return self._intf.set_property(IDirectionPR._metadata, IDirectionPR._set_sequence_metadata, sequence)


agcls.AgClassCatalog.add_catalog_entry("{5AC01BF1-2B95-4C13-8B69-09FDC485330E}", IDirectionPR)
agcls.AgTypeNameMap["IDirectionPR"] = IDirectionPR

class IDirectionRADec(IDirection):
    """Interface for Spherical direction (Right Ascension and Declination)."""
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _metadata = {
        "uuid" : "{A921E587-EC8A-4F1E-99BB-6E13B8E0D5E7}",
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
        "method_offsets" : { "get_dec" : 1,
                             "set_dec" : 2,
                             "get_ra" : 3,
                             "set_ra" : 4,
                             "get_magnitude" : 5,
                             "set_magnitude" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDirectionRADec._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDirectionRADec from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDirectionRADec.__dict__ and type(IDirectionRADec.__dict__[attrname]) == property:
            return IDirectionRADec.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IDirection.__setattr__(self, attrname, value)
    
    _get_dec_metadata = { "name" : "dec",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def dec(self) -> typing.Any:
        """Declination: angle above the x-y plane. Uses Latitude Dimension."""
        return self._intf.get_property(IDirectionRADec._metadata, IDirectionRADec._get_dec_metadata)

    _set_dec_metadata = { "name" : "dec",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @dec.setter
    def dec(self, vLat:typing.Any) -> None:
        return self._intf.set_property(IDirectionRADec._metadata, IDirectionRADec._set_dec_metadata, vLat)

    _get_ra_metadata = { "name" : "ra",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def ra(self) -> typing.Any:
        """Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension."""
        return self._intf.get_property(IDirectionRADec._metadata, IDirectionRADec._get_ra_metadata)

    _set_ra_metadata = { "name" : "ra",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @ra.setter
    def ra(self, vLon:typing.Any) -> None:
        return self._intf.set_property(IDirectionRADec._metadata, IDirectionRADec._set_ra_metadata, vLon)

    _get_magnitude_metadata = { "name" : "magnitude",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def magnitude(self) -> float:
        """A unitless value that represents magnitude."""
        return self._intf.get_property(IDirectionRADec._metadata, IDirectionRADec._get_magnitude_metadata)

    _set_magnitude_metadata = { "name" : "magnitude",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @magnitude.setter
    def magnitude(self, magnitude:float) -> None:
        return self._intf.set_property(IDirectionRADec._metadata, IDirectionRADec._set_magnitude_metadata, magnitude)


agcls.AgClassCatalog.add_catalog_entry("{A921E587-EC8A-4F1E-99BB-6E13B8E0D5E7}", IDirectionRADec)
agcls.AgTypeNameMap["IDirectionRADec"] = IDirectionRADec

class IDirectionXYZ(IDirection):
    """Interface for Cartesian direction."""
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _metadata = {
        "uuid" : "{2B499A22-6662-4F20-8B82-AA7701CD87A4}",
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
        "method_offsets" : { "get_x" : 1,
                             "set_x" : 2,
                             "get_y" : 3,
                             "set_y" : 4,
                             "get_z" : 5,
                             "set_z" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDirectionXYZ._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDirectionXYZ from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDirectionXYZ.__dict__ and type(IDirectionXYZ.__dict__[attrname]) == property:
            return IDirectionXYZ.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IDirection.__setattr__(self, attrname, value)
    
    _get_x_metadata = { "name" : "x",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def x(self) -> float:
        """X component. Dimensionless"""
        return self._intf.get_property(IDirectionXYZ._metadata, IDirectionXYZ._get_x_metadata)

    _set_x_metadata = { "name" : "x",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @x.setter
    def x(self, vx:float) -> None:
        return self._intf.set_property(IDirectionXYZ._metadata, IDirectionXYZ._set_x_metadata, vx)

    _get_y_metadata = { "name" : "y",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def y(self) -> float:
        """Y component. Dimensionless"""
        return self._intf.get_property(IDirectionXYZ._metadata, IDirectionXYZ._get_y_metadata)

    _set_y_metadata = { "name" : "y",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @y.setter
    def y(self, vy:float) -> None:
        return self._intf.set_property(IDirectionXYZ._metadata, IDirectionXYZ._set_y_metadata, vy)

    _get_z_metadata = { "name" : "z",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def z(self) -> float:
        """Z component. Dimensionless"""
        return self._intf.get_property(IDirectionXYZ._metadata, IDirectionXYZ._get_z_metadata)

    _set_z_metadata = { "name" : "z",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @z.setter
    def z(self, vz:float) -> None:
        return self._intf.set_property(IDirectionXYZ._metadata, IDirectionXYZ._set_z_metadata, vz)


agcls.AgClassCatalog.add_catalog_entry("{2B499A22-6662-4F20-8B82-AA7701CD87A4}", IDirectionXYZ)
agcls.AgTypeNameMap["IDirectionXYZ"] = IDirectionXYZ

class ICartesian3Vector(object):
    """Represents a cartesian 3-D vector."""
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{7B741836-71F9-4115-97F8-EAB30362E5C7}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_x" : 1,
                             "set_x" : 2,
                             "get_y" : 3,
                             "set_y" : 4,
                             "get_z" : 5,
                             "set_z" : 6,
                             "get" : 7,
                             "set" : 8,
                             "to_array" : 9, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ICartesian3Vector._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ICartesian3Vector from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ICartesian3Vector.__dict__ and type(ICartesian3Vector.__dict__[attrname]) == property:
            return ICartesian3Vector.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ICartesian3Vector.")
    
    _get_x_metadata = { "name" : "x",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def x(self) -> float:
        """X coordinate"""
        return self._intf.get_property(ICartesian3Vector._metadata, ICartesian3Vector._get_x_metadata)

    _set_x_metadata = { "name" : "x",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @x.setter
    def x(self, x:float) -> None:
        return self._intf.set_property(ICartesian3Vector._metadata, ICartesian3Vector._set_x_metadata, x)

    _get_y_metadata = { "name" : "y",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def y(self) -> float:
        """Y coordinate"""
        return self._intf.get_property(ICartesian3Vector._metadata, ICartesian3Vector._get_y_metadata)

    _set_y_metadata = { "name" : "y",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @y.setter
    def y(self, y:float) -> None:
        return self._intf.set_property(ICartesian3Vector._metadata, ICartesian3Vector._set_y_metadata, y)

    _get_z_metadata = { "name" : "z",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def z(self) -> float:
        """Z coordinate"""
        return self._intf.get_property(ICartesian3Vector._metadata, ICartesian3Vector._get_z_metadata)

    _set_z_metadata = { "name" : "z",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @z.setter
    def z(self, z:float) -> None:
        return self._intf.set_property(ICartesian3Vector._metadata, ICartesian3Vector._set_z_metadata, z)

    _get_metadata = { "name" : "get",
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def get(self) -> typing.Tuple[float, float, float]:
        """Returns cartesian vector"""
        return self._intf.invoke(ICartesian3Vector._metadata, ICartesian3Vector._get_metadata, out_arg(), out_arg(), out_arg())

    _set_metadata = { "name" : "set",
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def set(self, x:float, y:float, z:float) -> None:
        """Sets cartesian vector"""
        return self._intf.invoke(ICartesian3Vector._metadata, ICartesian3Vector._set_metadata, x, y, z)

    _to_array_metadata = { "name" : "to_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def to_array(self) -> list:
        """Returns coordinates as an array."""
        return self._intf.invoke(ICartesian3Vector._metadata, ICartesian3Vector._to_array_metadata, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{7B741836-71F9-4115-97F8-EAB30362E5C7}", ICartesian3Vector)
agcls.AgTypeNameMap["ICartesian3Vector"] = ICartesian3Vector

class IOrientation(object):
    """Interface to set and retrieve the orientation method."""
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{8467175F-1BD8-4498-90FD-08C67072D120}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "convert_to" : 1,
                             "get_orientation_type" : 2,
                             "assign" : 3,
                             "assign_az_el" : 4,
                             "assign_euler_angles" : 5,
                             "assign_quaternion" : 6,
                             "assign_ypr_angles" : 7,
                             "query_az_el" : 8,
                             "query_euler_angles" : 9,
                             "query_quaternion" : 10,
                             "query_ypr_angles" : 11,
                             "query_az_el_array" : 12,
                             "query_euler_angles_array" : 13,
                             "query_quaternion_array" : 14,
                             "query_ypr_angles_array" : 15, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IOrientation._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IOrientation from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IOrientation.__dict__ and type(IOrientation.__dict__[attrname]) == property:
            return IOrientation.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IOrientation.")
    
    _convert_to_metadata = { "name" : "convert_to",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgEnum_arg(ORIENTATION_TYPE), agmarshall.AgInterface_out_arg,) }
    def convert_to(self, type:"ORIENTATION_TYPE") -> "IOrientation":
        """Method to change the orientation method to the type specified."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._convert_to_metadata, type, out_arg())

    _get_orientation_type_metadata = { "name" : "orientation_type",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(ORIENTATION_TYPE),) }
    @property
    def orientation_type(self) -> "ORIENTATION_TYPE":
        """Returns the orientation method currently being used."""
        return self._intf.get_property(IOrientation._metadata, IOrientation._get_orientation_type_metadata)

    _assign_metadata = { "name" : "assign",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.AgInterface_in_arg("IOrientation"),) }
    def assign(self, pOrientation:"IOrientation") -> None:
        """Assign a new orientation method."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_metadata, pOrientation)

    _assign_az_el_metadata = { "name" : "assign_az_el",
            "arg_types" : (agcom.VARIANT, agcom.VARIANT, agcom.LONG,),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT),) }
    def assign_az_el(self, azimuth:typing.Any, elevation:typing.Any, aboutBoresight:"AZ_EL_ABOUT_BORESIGHT") -> None:
        """Helper method to set orientation using the AzEl representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_az_el_metadata, azimuth, elevation, aboutBoresight)

    _assign_euler_angles_metadata = { "name" : "assign_euler_angles",
            "arg_types" : (agcom.LONG, agcom.VARIANT, agcom.VARIANT, agcom.VARIANT,),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE), agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def assign_euler_angles(self, sequence:"EULER_ORIENTATION_SEQUENCE", a:typing.Any, b:typing.Any, c:typing.Any) -> None:
        """Helper method to set orientation using the Euler angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_euler_angles_metadata, sequence, a, b, c)

    _assign_quaternion_metadata = { "name" : "assign_quaternion",
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_quaternion(self, qx:float, qy:float, qz:float, qs:float) -> None:
        """Helper method to set orientation using the Quaternion representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_quaternion_metadata, qx, qy, qz, qs)

    _assign_ypr_angles_metadata = { "name" : "assign_ypr_angles",
            "arg_types" : (agcom.LONG, agcom.VARIANT, agcom.VARIANT, agcom.VARIANT,),
            "marshallers" : (agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE), agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def assign_ypr_angles(self, sequence:"YPR_ANGLES_SEQUENCE", yaw:typing.Any, pitch:typing.Any, roll:typing.Any) -> None:
        """Helper method to set orientation using the YPR angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_ypr_angles_metadata, sequence, yaw, pitch, roll)

    _query_az_el_metadata = { "name" : "query_az_el",
            "arg_types" : (POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT),) }
    def query_az_el(self) -> typing.Tuple[typing.Any, typing.Any, AZ_EL_ABOUT_BORESIGHT]:
        """Helper method to get orientation using the AzEl representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_az_el_metadata, out_arg(), out_arg(), out_arg())

    _query_euler_angles_metadata = { "name" : "query_euler_angles",
            "arg_types" : (agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE), agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def query_euler_angles(self, sequence:"EULER_ORIENTATION_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Helper method to get orientation using the Euler angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_euler_angles_metadata, sequence, out_arg(), out_arg(), out_arg())

    _query_quaternion_metadata = { "name" : "query_quaternion",
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def query_quaternion(self) -> typing.Tuple[float, float, float, float]:
        """Helper method to get orientation using the Quaternion representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_quaternion_metadata, out_arg(), out_arg(), out_arg(), out_arg())

    _query_ypr_angles_metadata = { "name" : "query_ypr_angles",
            "arg_types" : (agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE), agmarshall.VARIANT_arg, agmarshall.VARIANT_arg, agmarshall.VARIANT_arg,) }
    def query_ypr_angles(self, sequence:"YPR_ANGLES_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Helper method to get orientation using the YPR angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_ypr_angles_metadata, sequence, out_arg(), out_arg(), out_arg())

    _query_az_el_array_metadata = { "name" : "query_az_el_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_az_el_array(self) -> list:
        """Returns the AzEl elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_az_el_array_metadata, out_arg())

    _query_euler_angles_array_metadata = { "name" : "query_euler_angles_array",
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE), agmarshall.LPSAFEARRAY_arg,) }
    def query_euler_angles_array(self, sequence:"EULER_ORIENTATION_SEQUENCE") -> list:
        """Returns the Euler elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_euler_angles_array_metadata, sequence, out_arg())

    _query_quaternion_array_metadata = { "name" : "query_quaternion_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def query_quaternion_array(self) -> list:
        """Returns the Quaternion elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_quaternion_array_metadata, out_arg())

    _query_ypr_angles_array_metadata = { "name" : "query_ypr_angles_array",
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE), agmarshall.LPSAFEARRAY_arg,) }
    def query_ypr_angles_array(self, sequence:"YPR_ANGLES_SEQUENCE") -> list:
        """Returns the YPR Angles elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_ypr_angles_array_metadata, sequence, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{8467175F-1BD8-4498-90FD-08C67072D120}", IOrientation)
agcls.AgTypeNameMap["IOrientation"] = IOrientation

class IOrientationAzEl(IOrientation):
    """Interface for AzEl orientation method."""
    _num_methods = 6
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _metadata = {
        "uuid" : "{6A6B1D7D-6A7F-48B3-98CA-019CA46499FE}",
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
        "method_offsets" : { "get_azimuth" : 1,
                             "set_azimuth" : 2,
                             "get_elevation" : 3,
                             "set_elevation" : 4,
                             "get_about_boresight" : 5,
                             "set_about_boresight" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IOrientationAzEl._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IOrientationAzEl from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IOrientationAzEl.__dict__ and type(IOrientationAzEl.__dict__[attrname]) == property:
            return IOrientationAzEl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IOrientation.__setattr__(self, attrname, value)
    
    _get_azimuth_metadata = { "name" : "azimuth",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def azimuth(self) -> typing.Any:
        """Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationAzEl._metadata, IOrientationAzEl._get_azimuth_metadata)

    _set_azimuth_metadata = { "name" : "azimuth",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @azimuth.setter
    def azimuth(self, vAzimuth:typing.Any) -> None:
        return self._intf.set_property(IOrientationAzEl._metadata, IOrientationAzEl._set_azimuth_metadata, vAzimuth)

    _get_elevation_metadata = { "name" : "elevation",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def elevation(self) -> typing.Any:
        """Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationAzEl._metadata, IOrientationAzEl._get_elevation_metadata)

    _set_elevation_metadata = { "name" : "elevation",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @elevation.setter
    def elevation(self, vElevation:typing.Any) -> None:
        return self._intf.set_property(IOrientationAzEl._metadata, IOrientationAzEl._set_elevation_metadata, vElevation)

    _get_about_boresight_metadata = { "name" : "about_boresight",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT),) }
    @property
    def about_boresight(self) -> "AZ_EL_ABOUT_BORESIGHT":
        """Determines orientation of the X and Y axes with respect to the parent's reference frame."""
        return self._intf.get_property(IOrientationAzEl._metadata, IOrientationAzEl._get_about_boresight_metadata)

    _set_about_boresight_metadata = { "name" : "about_boresight",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT),) }
    @about_boresight.setter
    def about_boresight(self, aboutBoresight:"AZ_EL_ABOUT_BORESIGHT") -> None:
        return self._intf.set_property(IOrientationAzEl._metadata, IOrientationAzEl._set_about_boresight_metadata, aboutBoresight)


agcls.AgClassCatalog.add_catalog_entry("{6A6B1D7D-6A7F-48B3-98CA-019CA46499FE}", IOrientationAzEl)
agcls.AgTypeNameMap["IOrientationAzEl"] = IOrientationAzEl

class IOrientationEulerAngles(IOrientation):
    """Interface for Euler Angles orientation method."""
    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _metadata = {
        "uuid" : "{4204C7E1-EC21-40AD-A905-BB35A3FDF7BD}",
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
        "method_offsets" : { "get_sequence" : 1,
                             "set_sequence" : 2,
                             "get_a" : 3,
                             "set_a" : 4,
                             "get_b" : 5,
                             "set_b" : 6,
                             "get_c" : 7,
                             "set_c" : 8, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IOrientationEulerAngles._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IOrientationEulerAngles from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IOrientationEulerAngles.__dict__ and type(IOrientationEulerAngles.__dict__[attrname]) == property:
            return IOrientationEulerAngles.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IOrientation.__setattr__(self, attrname, value)
    
    _get_sequence_metadata = { "name" : "sequence",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE),) }
    @property
    def sequence(self) -> "EULER_ORIENTATION_SEQUENCE":
        """Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_sequence_metadata)

    _set_sequence_metadata = { "name" : "sequence",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE),) }
    @sequence.setter
    def sequence(self, ppVal:"EULER_ORIENTATION_SEQUENCE") -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_sequence_metadata, ppVal)

    _get_a_metadata = { "name" : "a",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def a(self) -> typing.Any:
        """Euler A angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_a_metadata)

    _set_a_metadata = { "name" : "a",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @a.setter
    def a(self, va:typing.Any) -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_a_metadata, va)

    _get_b_metadata = { "name" : "b",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def b(self) -> typing.Any:
        """Euler b angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_b_metadata)

    _set_b_metadata = { "name" : "b",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @b.setter
    def b(self, vb:typing.Any) -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_b_metadata, vb)

    _get_c_metadata = { "name" : "c",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def c(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_c_metadata)

    _set_c_metadata = { "name" : "c",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @c.setter
    def c(self, vc:typing.Any) -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_c_metadata, vc)


agcls.AgClassCatalog.add_catalog_entry("{4204C7E1-EC21-40AD-A905-BB35A3FDF7BD}", IOrientationEulerAngles)
agcls.AgTypeNameMap["IOrientationEulerAngles"] = IOrientationEulerAngles

class IOrientationQuaternion(IOrientation):
    """Interface for Quaternion orientation method."""
    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _metadata = {
        "uuid" : "{101FAC5C-8DDB-4D4F-9C73-58146CA8EB01}",
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
        "method_offsets" : { "get_qx" : 1,
                             "set_qx" : 2,
                             "get_qy" : 3,
                             "set_qy" : 4,
                             "get_qz" : 5,
                             "set_qz" : 6,
                             "get_qs" : 7,
                             "set_qs" : 8, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IOrientationQuaternion._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IOrientationQuaternion from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IOrientationQuaternion.__dict__ and type(IOrientationQuaternion.__dict__[attrname]) == property:
            return IOrientationQuaternion.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IOrientation.__setattr__(self, attrname, value)
    
    _get_qx_metadata = { "name" : "qx",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def qx(self) -> float:
        """The first element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QX = nx si..."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qx_metadata)

    _set_qx_metadata = { "name" : "qx",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @qx.setter
    def qx(self, vQX:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qx_metadata, vQX)

    _get_qy_metadata = { "name" : "qy",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def qy(self) -> float:
        """The second element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QY = ny s..."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qy_metadata)

    _set_qy_metadata = { "name" : "qy",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @qy.setter
    def qy(self, vQY:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qy_metadata, vQY)

    _get_qz_metadata = { "name" : "qz",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def qz(self) -> float:
        """The third element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QZ = nz si..."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qz_metadata)

    _set_qz_metadata = { "name" : "qz",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @qz.setter
    def qz(self, vQZ:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qz_metadata, vQZ)

    _get_qs_metadata = { "name" : "qs",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def qs(self) -> float:
        """The scalar component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QS = cos(A/2). Dimensionless."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qs_metadata)

    _set_qs_metadata = { "name" : "qs",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @qs.setter
    def qs(self, vQS:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qs_metadata, vQS)


agcls.AgClassCatalog.add_catalog_entry("{101FAC5C-8DDB-4D4F-9C73-58146CA8EB01}", IOrientationQuaternion)
agcls.AgTypeNameMap["IOrientationQuaternion"] = IOrientationQuaternion

class IOrientationYPRAngles(IOrientation):
    """Interface for Yaw-Pitch Roll (YPR) Angles orientation system."""
    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _metadata = {
        "uuid" : "{97A9D45D-E718-41FC-ACD2-CEBBEFD2011B}",
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
        "method_offsets" : { "get_sequence" : 1,
                             "set_sequence" : 2,
                             "get_yaw" : 3,
                             "set_yaw" : 4,
                             "get_pitch" : 5,
                             "set_pitch" : 6,
                             "get_roll" : 7,
                             "set_roll" : 8, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IOrientationYPRAngles._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IOrientationYPRAngles from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IOrientationYPRAngles.__dict__ and type(IOrientationYPRAngles.__dict__[attrname]) == property:
            return IOrientationYPRAngles.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IOrientation.__setattr__(self, attrname, value)
    
    _get_sequence_metadata = { "name" : "sequence",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE),) }
    @property
    def sequence(self) -> "YPR_ANGLES_SEQUENCE":
        """YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_sequence_metadata)

    _set_sequence_metadata = { "name" : "sequence",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE),) }
    @sequence.setter
    def sequence(self, sequence:"YPR_ANGLES_SEQUENCE") -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_sequence_metadata, sequence)

    _get_yaw_metadata = { "name" : "yaw",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def yaw(self) -> typing.Any:
        """Yaw angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_yaw_metadata)

    _set_yaw_metadata = { "name" : "yaw",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @yaw.setter
    def yaw(self, vYaw:typing.Any) -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_yaw_metadata, vYaw)

    _get_pitch_metadata = { "name" : "pitch",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_pitch_metadata)

    _set_pitch_metadata = { "name" : "pitch",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @pitch.setter
    def pitch(self, vPitch:typing.Any) -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_pitch_metadata, vPitch)

    _get_roll_metadata = { "name" : "roll",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_roll_metadata)

    _set_roll_metadata = { "name" : "roll",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @roll.setter
    def roll(self, vRoll:typing.Any) -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_roll_metadata, vRoll)


agcls.AgClassCatalog.add_catalog_entry("{97A9D45D-E718-41FC-ACD2-CEBBEFD2011B}", IOrientationYPRAngles)
agcls.AgTypeNameMap["IOrientationYPRAngles"] = IOrientationYPRAngles

class IOrientationPositionOffset(object):
    """Interface for defining the orientation origin position offset relative to the parent object."""
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{0DDA686C-559C-4BEA-969B-BF40708242B6}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_position_offset" : 1, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IOrientationPositionOffset._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IOrientationPositionOffset from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IOrientationPositionOffset.__dict__ and type(IOrientationPositionOffset.__dict__[attrname]) == property:
            return IOrientationPositionOffset.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IOrientationPositionOffset.")
    
    _get_position_offset_metadata = { "name" : "position_offset",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def position_offset(self) -> "ICartesian3Vector":
        """Gets or sets the position offset cartesian vector."""
        return self._intf.get_property(IOrientationPositionOffset._metadata, IOrientationPositionOffset._get_position_offset_metadata)


agcls.AgClassCatalog.add_catalog_entry("{0DDA686C-559C-4BEA-969B-BF40708242B6}", IOrientationPositionOffset)
agcls.AgTypeNameMap["IOrientationPositionOffset"] = IOrientationPositionOffset

class IOrbitState(object):
    """Interface to set and retrieve the coordinate type used to specify the orbit state."""
    _num_methods = 14
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{42342AD2-F6C5-426B-AB2A-3688F05353C8}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "convert_to" : 1,
                             "get_orbit_state_type" : 2,
                             "assign" : 3,
                             "assign_classical" : 4,
                             "assign_cartesian" : 5,
                             "assign_geodetic" : 6,
                             "assign_equinoctial_posigrade" : 7,
                             "assign_equinoctial_retrograde" : 8,
                             "assign_mixed_spherical" : 9,
                             "assign_spherical" : 10,
                             "get_central_body_name" : 11,
                             "get_epoch" : 12,
                             "set_epoch" : 13,
                             "assign_delaunay" : 14, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IOrbitState._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IOrbitState from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IOrbitState.__dict__ and type(IOrbitState.__dict__[attrname]) == property:
            return IOrbitState.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IOrbitState.")
    
    _convert_to_metadata = { "name" : "convert_to",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgEnum_arg(ORBIT_STATE_TYPE), agmarshall.AgInterface_out_arg,) }
    def convert_to(self, type:"ORBIT_STATE_TYPE") -> "IOrbitState":
        """Method to changes the coordinate type to the type specified."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._convert_to_metadata, type, out_arg())

    _get_orbit_state_type_metadata = { "name" : "orbit_state_type",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(ORBIT_STATE_TYPE),) }
    @property
    def orbit_state_type(self) -> "ORBIT_STATE_TYPE":
        """Returns the coordinate type currently being used."""
        return self._intf.get_property(IOrbitState._metadata, IOrbitState._get_orbit_state_type_metadata)

    _assign_metadata = { "name" : "assign",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.AgInterface_in_arg("IOrbitState"),) }
    def assign(self, pOrbitState:"IOrbitState") -> None:
        """Assign a new coordinate type."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_metadata, pOrbitState)

    _assign_classical_metadata = { "name" : "assign_classical",
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_classical(self, eCoordinateSystem:"COORDINATE_SYSTEM", semiMajorAxis:float, eccentricity:float, inclination:float, argOfPerigee:float, rAAN:float, meanAnomaly:float) -> None:
        """Helper method to assign a new orbit state using Classical representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_classical_metadata, eCoordinateSystem, semiMajorAxis, eccentricity, inclination, argOfPerigee, rAAN, meanAnomaly)

    _assign_cartesian_metadata = { "name" : "assign_cartesian",
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_cartesian(self, eCoordinateSystem:"COORDINATE_SYSTEM", xPosition:float, yPosition:float, zPosition:float, xVelocity:float, yVelocity:float, zVelocity:float) -> None:
        """Helper method to assign a new orbit state using Cartesian representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_cartesian_metadata, eCoordinateSystem, xPosition, yPosition, zPosition, xVelocity, yVelocity, zVelocity)

    _assign_geodetic_metadata = { "name" : "assign_geodetic",
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_geodetic(self, eCoordinateSystem:"COORDINATE_SYSTEM", latitude:float, longitude:float, altitude:float, latitudeRate:float, longitudeRate:float, altitudeRate:float) -> None:
        """Helper method to assign a new orbit state using Geodetic representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_geodetic_metadata, eCoordinateSystem, latitude, longitude, altitude, latitudeRate, longitudeRate, altitudeRate)

    _assign_equinoctial_posigrade_metadata = { "name" : "assign_equinoctial_posigrade",
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_equinoctial_posigrade(self, eCoordinateSystem:"COORDINATE_SYSTEM", semiMajorAxis:float, h:float, k:float, p:float, q:float, meanLon:float) -> None:
        """Helper method to assign a new orbit state using Equinoctial representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_equinoctial_posigrade_metadata, eCoordinateSystem, semiMajorAxis, h, k, p, q, meanLon)

    _assign_equinoctial_retrograde_metadata = { "name" : "assign_equinoctial_retrograde",
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_equinoctial_retrograde(self, eCoordinateSystem:"COORDINATE_SYSTEM", semiMajorAxis:float, h:float, k:float, p:float, q:float, meanLon:float) -> None:
        """Helper method to assign a new orbit state using Equinoctial representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_equinoctial_retrograde_metadata, eCoordinateSystem, semiMajorAxis, h, k, p, q, meanLon)

    _assign_mixed_spherical_metadata = { "name" : "assign_mixed_spherical",
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_mixed_spherical(self, eCoordinateSystem:"COORDINATE_SYSTEM", latitude:float, longitude:float, altitude:float, horFlightPathAngle:float, flightPathAzimuth:float, velocity:float) -> None:
        """Helper method to assign a new orbit state using Mixed Spherical representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_mixed_spherical_metadata, eCoordinateSystem, latitude, longitude, altitude, horFlightPathAngle, flightPathAzimuth, velocity)

    _assign_spherical_metadata = { "name" : "assign_spherical",
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_spherical(self, eCoordinateSystem:"COORDINATE_SYSTEM", rightAscension:float, declination:float, radius:float, horFlightPathAngle:float, flightPathAzimuth:float, velocity:float) -> None:
        """Helper method to assign a new orbit state using Spherical representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_spherical_metadata, eCoordinateSystem, rightAscension, declination, radius, horFlightPathAngle, flightPathAzimuth, velocity)

    _get_central_body_name_metadata = { "name" : "central_body_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def central_body_name(self) -> str:
        """Gets the central body."""
        return self._intf.get_property(IOrbitState._metadata, IOrbitState._get_central_body_name_metadata)

    _get_epoch_metadata = { "name" : "epoch",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def epoch(self) -> typing.Any:
        """The state epoch"""
        return self._intf.get_property(IOrbitState._metadata, IOrbitState._get_epoch_metadata)

    _set_epoch_metadata = { "name" : "epoch",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @epoch.setter
    def epoch(self, epoch:typing.Any) -> None:
        return self._intf.set_property(IOrbitState._metadata, IOrbitState._set_epoch_metadata, epoch)

    _assign_delaunay_metadata = { "name" : "assign_delaunay",
            "arg_types" : (agcom.LONG, agcom.LONG, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.AgEnum_arg(COORDINATE_SYSTEM), agmarshall.AgEnum_arg(DELAUNAY_L_TYPE_TEMP), agmarshall.AgEnum_arg(DELAUNAY_H_TYPE_TEMP), agmarshall.AgEnum_arg(DELAUNAY_G_TYPE_TEMP), agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def assign_delaunay(self, eCoordinateSystem:"COORDINATE_SYSTEM", lType:"DELAUNAY_L_TYPE_TEMP", hType:"DELAUNAY_H_TYPE_TEMP", gType:"DELAUNAY_G_TYPE_TEMP", meanAnomaly:float, argOfPeriapsis:float, rAAN:float) -> None:
        """Helper method to assign a new orbit state using Delaunay representation"""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_delaunay_metadata, eCoordinateSystem, lType, hType, gType, meanAnomaly, argOfPeriapsis, rAAN)


agcls.AgClassCatalog.add_catalog_entry("{42342AD2-F6C5-426B-AB2A-3688F05353C8}", IOrbitState)
agcls.AgTypeNameMap["IOrbitState"] = IOrbitState

class ICartesian2Vector(object):
    """Represents a cartesian 2-D vector."""
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{DA459BD7-5810-4B30-8397-21EDA9E52D2B}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_x" : 1,
                             "set_x" : 2,
                             "get_y" : 3,
                             "set_y" : 4,
                             "get" : 5,
                             "set" : 6,
                             "to_array" : 7, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ICartesian2Vector._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ICartesian2Vector from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ICartesian2Vector.__dict__ and type(ICartesian2Vector.__dict__[attrname]) == property:
            return ICartesian2Vector.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ICartesian2Vector.")
    
    _get_x_metadata = { "name" : "x",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def x(self) -> float:
        """X coordinate"""
        return self._intf.get_property(ICartesian2Vector._metadata, ICartesian2Vector._get_x_metadata)

    _set_x_metadata = { "name" : "x",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @x.setter
    def x(self, x:float) -> None:
        return self._intf.set_property(ICartesian2Vector._metadata, ICartesian2Vector._set_x_metadata, x)

    _get_y_metadata = { "name" : "y",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def y(self) -> float:
        """Y coordinate"""
        return self._intf.get_property(ICartesian2Vector._metadata, ICartesian2Vector._get_y_metadata)

    _set_y_metadata = { "name" : "y",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @y.setter
    def y(self, y:float) -> None:
        return self._intf.set_property(ICartesian2Vector._metadata, ICartesian2Vector._set_y_metadata, y)

    _get_metadata = { "name" : "get",
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def get(self) -> typing.Tuple[float, float]:
        """Returns cartesian vector"""
        return self._intf.invoke(ICartesian2Vector._metadata, ICartesian2Vector._get_metadata, out_arg(), out_arg())

    _set_metadata = { "name" : "set",
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def set(self, x:float, y:float) -> None:
        """Sets cartesian vector"""
        return self._intf.invoke(ICartesian2Vector._metadata, ICartesian2Vector._set_metadata, x, y)

    _to_array_metadata = { "name" : "to_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def to_array(self) -> list:
        """Returns coordinates as an array."""
        return self._intf.invoke(ICartesian2Vector._metadata, ICartesian2Vector._to_array_metadata, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{DA459BD7-5810-4B30-8397-21EDA9E52D2B}", ICartesian2Vector)
agcls.AgTypeNameMap["ICartesian2Vector"] = ICartesian2Vector

class IUnitPreferencesDimension(object):
    """Provides info on a Dimension from the global unit table."""
    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{AA966FFD-1A99-45D8-9193-C519BBBA99FA}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_id" : 1,
                             "get_name" : 2,
                             "get_available_units" : 3,
                             "get_current_unit" : 4,
                             "set_current_unit" : 5, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUnitPreferencesDimension._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesDimension from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUnitPreferencesDimension.__dict__ and type(IUnitPreferencesDimension.__dict__[attrname]) == property:
            return IUnitPreferencesDimension.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUnitPreferencesDimension.")
    
    _get_id_metadata = { "name" : "id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def id(self) -> int:
        """Returns the ID of the dimension."""
        return self._intf.get_property(IUnitPreferencesDimension._metadata, IUnitPreferencesDimension._get_id_metadata)

    _get_name_metadata = { "name" : "name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def name(self) -> str:
        """Returns the current Dimension's full name."""
        return self._intf.get_property(IUnitPreferencesDimension._metadata, IUnitPreferencesDimension._get_name_metadata)

    _get_available_units_metadata = { "name" : "available_units",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def available_units(self) -> "UnitPreferencesUnitCollection":
        """Returns collection of Units."""
        return self._intf.get_property(IUnitPreferencesDimension._metadata, IUnitPreferencesDimension._get_available_units_metadata)

    _get_current_unit_metadata = { "name" : "current_unit",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def current_unit(self) -> "UnitPreferencesUnit":
        """Returns the current unit for this dimension."""
        return self._intf.get_property(IUnitPreferencesDimension._metadata, IUnitPreferencesDimension._get_current_unit_metadata)

    _set_current_unit_metadata = { "name" : "set_current_unit",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    def set_current_unit(self, unitAbbrv:str) -> None:
        """Sets the Unit for this simple dimension."""
        return self._intf.invoke(IUnitPreferencesDimension._metadata, IUnitPreferencesDimension._set_current_unit_metadata, unitAbbrv)


agcls.AgClassCatalog.add_catalog_entry("{AA966FFD-1A99-45D8-9193-C519BBBA99FA}", IUnitPreferencesDimension)
agcls.AgTypeNameMap["IUnitPreferencesDimension"] = IUnitPreferencesDimension

class IPropertyInfo(object):
    """Property information."""
    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{26A48B4B-BF6A-4F9D-9658-44A7A2DBBE2A}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_name" : 1,
                             "get_property_type" : 2,
                             "get_value" : 3,
                             "set_value" : 4,
                             "get_has_min" : 5,
                             "get_has_max" : 6,
                             "get_min" : 7,
                             "get_max" : 8, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IPropertyInfo._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IPropertyInfo from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IPropertyInfo.__dict__ and type(IPropertyInfo.__dict__[attrname]) == property:
            return IPropertyInfo.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IPropertyInfo.")
    
    _get_name_metadata = { "name" : "name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def name(self) -> str:
        """The name of the property."""
        return self._intf.get_property(IPropertyInfo._metadata, IPropertyInfo._get_name_metadata)

    _get_property_type_metadata = { "name" : "property_type",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(PROPERTY_INFO_VALUE_TYPE),) }
    @property
    def property_type(self) -> "PROPERTY_INFO_VALUE_TYPE":
        """The type of property."""
        return self._intf.get_property(IPropertyInfo._metadata, IPropertyInfo._get_property_type_metadata)

    _get_value_metadata = { "name" : "get_value",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    def get_value(self) -> typing.Any:
        """The value of the property. Use PropertyType to determine the type to cast to."""
        return self._intf.invoke(IPropertyInfo._metadata, IPropertyInfo._get_value_metadata, out_arg())

    _set_value_metadata = { "name" : "set_value",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    def set_value(self, propertyInfo:typing.Any) -> None:
        """The value of the property. Use PropertyType to determine the type to cast to."""
        return self._intf.invoke(IPropertyInfo._metadata, IPropertyInfo._set_value_metadata, propertyInfo)

    _get_has_min_metadata = { "name" : "has_min",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def has_min(self) -> bool:
        """Used to determine if the property has a minimum value."""
        return self._intf.get_property(IPropertyInfo._metadata, IPropertyInfo._get_has_min_metadata)

    _get_has_max_metadata = { "name" : "has_max",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def has_max(self) -> bool:
        """Used to determine if the property has a maximum value."""
        return self._intf.get_property(IPropertyInfo._metadata, IPropertyInfo._get_has_max_metadata)

    _get_min_metadata = { "name" : "min",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def min(self) -> typing.Any:
        """The minimum value of this property. Use PropertyType to determine the type to cast to."""
        return self._intf.get_property(IPropertyInfo._metadata, IPropertyInfo._get_min_metadata)

    _get_max_metadata = { "name" : "max",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def max(self) -> typing.Any:
        """The maximum value of this property. Use PropertyType to determine the type to cast to."""
        return self._intf.get_property(IPropertyInfo._metadata, IPropertyInfo._get_max_metadata)


agcls.AgClassCatalog.add_catalog_entry("{26A48B4B-BF6A-4F9D-9658-44A7A2DBBE2A}", IPropertyInfo)
agcls.AgTypeNameMap["IPropertyInfo"] = IPropertyInfo

class IPropertyInfoCollection(object):
    """The collection of properties."""
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{198E6280-1D5A-4AED-9DE3-ACE354B95287}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "item" : 1,
                             "get__NewEnum" : 2,
                             "get_count" : 3,
                             "get_item_by_index" : 4,
                             "get_item_by_name" : 5, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IPropertyInfoCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IPropertyInfoCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IPropertyInfoCollection.__dict__ and type(IPropertyInfoCollection.__dict__[attrname]) == property:
            return IPropertyInfoCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IPropertyInfoCollection.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IPropertyInfo":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.VARIANT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.AgInterface_out_arg,) }
    def item(self, indexOrName:typing.Any) -> "PropertyInfo":
        """Allows the user to iterate through the properties."""
        return self._intf.invoke(IPropertyInfoCollection._metadata, IPropertyInfoCollection._item_metadata, indexOrName, out_arg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Enumerates through the properties."""
        return self._intf.get_property(IPropertyInfoCollection._metadata, IPropertyInfoCollection._get__NewEnum_metadata)

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """The number of properties available."""
        return self._intf.get_property(IPropertyInfoCollection._metadata, IPropertyInfoCollection._get_count_metadata)

    _get_item_by_index_metadata = { "name" : "get_item_by_index",
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.INT_arg, agmarshall.AgInterface_out_arg,) }
    def get_item_by_index(self, index:int) -> "PropertyInfo":
        """Retrieves a property from the collection by index."""
        return self._intf.invoke(IPropertyInfoCollection._metadata, IPropertyInfoCollection._get_item_by_index_metadata, index, out_arg())

    _get_item_by_name_metadata = { "name" : "get_item_by_name",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def get_item_by_name(self, name:str) -> "PropertyInfo":
        """Retrieves a property from the collection by name."""
        return self._intf.invoke(IPropertyInfoCollection._metadata, IPropertyInfoCollection._get_item_by_name_metadata, name, out_arg())

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{198E6280-1D5A-4AED-9DE3-ACE354B95287}", IPropertyInfoCollection)
agcls.AgTypeNameMap["IPropertyInfoCollection"] = IPropertyInfoCollection

class IRuntimeTypeInfo(object):
    """Interface used to retrieve the properties at runtime."""
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{01F8872C-9586-4131-A724-F97C6ADD083F}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_properties" : 1,
                             "get_is_collection" : 2,
                             "get_count" : 3,
                             "get_item" : 4, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IRuntimeTypeInfo._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IRuntimeTypeInfo from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IRuntimeTypeInfo.__dict__ and type(IRuntimeTypeInfo.__dict__[attrname]) == property:
            return IRuntimeTypeInfo.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IRuntimeTypeInfo.")
    
    _get_properties_metadata = { "name" : "properties",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def properties(self) -> "PropertyInfoCollection":
        """The collection of properties."""
        return self._intf.get_property(IRuntimeTypeInfo._metadata, IRuntimeTypeInfo._get_properties_metadata)

    _get_is_collection_metadata = { "name" : "is_collection",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_collection(self) -> bool:
        """Determines if the interface is a collection."""
        return self._intf.get_property(IRuntimeTypeInfo._metadata, IRuntimeTypeInfo._get_is_collection_metadata)

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """If the interface is a collection, returns the collection count."""
        return self._intf.get_property(IRuntimeTypeInfo._metadata, IRuntimeTypeInfo._get_count_metadata)

    _get_item_metadata = { "name" : "get_item",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.AgInterface_out_arg,) }
    def get_item(self, index:int) -> "PropertyInfo":
        """Returns the property of the collection at the given index."""
        return self._intf.invoke(IRuntimeTypeInfo._metadata, IRuntimeTypeInfo._get_item_metadata, index, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{01F8872C-9586-4131-A724-F97C6ADD083F}", IRuntimeTypeInfo)
agcls.AgTypeNameMap["IRuntimeTypeInfo"] = IRuntimeTypeInfo

class IRuntimeTypeInfoProvider(object):
    """Access point for RuntimeTypeInfo."""
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{E9AD01B5-7892-4367-8EC7-60EA26CE0E11}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_provide_runtime_type_info" : 1, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IRuntimeTypeInfoProvider._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IRuntimeTypeInfoProvider from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IRuntimeTypeInfoProvider.__dict__ and type(IRuntimeTypeInfoProvider.__dict__[attrname]) == property:
            return IRuntimeTypeInfoProvider.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IRuntimeTypeInfoProvider.")
    
    _get_provide_runtime_type_info_metadata = { "name" : "provide_runtime_type_info",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def provide_runtime_type_info(self) -> "RuntimeTypeInfo":
        """Returns the RuntimeTypeInfo interface to access properties at runtime."""
        return self._intf.get_property(IRuntimeTypeInfoProvider._metadata, IRuntimeTypeInfoProvider._get_provide_runtime_type_info_metadata)


agcls.AgClassCatalog.add_catalog_entry("{E9AD01B5-7892-4367-8EC7-60EA26CE0E11}", IRuntimeTypeInfoProvider)
agcls.AgTypeNameMap["IRuntimeTypeInfoProvider"] = IRuntimeTypeInfoProvider

class IExecCmdResult(object):
    """Collection of strings returned by the ExecuteCommand."""
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{CC5C63BC-FF0A-4CC8-AD58-5A8D11DD9C60}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_count" : 1,
                             "item" : 2,
                             "get__NewEnum" : 3,
                             "range" : 4,
                             "get_is_succeeded" : 5, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IExecCmdResult._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IExecCmdResult from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IExecCmdResult.__dict__ and type(IExecCmdResult.__dict__[attrname]) == property:
            return IExecCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IExecCmdResult.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(IExecCmdResult._metadata, IExecCmdResult._get_count_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.BSTR_arg,) }
    def item(self, index:int) -> str:
        """Gets the element at the specified index (0-based)."""
        return self._intf.invoke(IExecCmdResult._metadata, IExecCmdResult._item_metadata, index, out_arg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Returns an object that can be used to iterate through all the strings in the collection."""
        return self._intf.get_property(IExecCmdResult._metadata, IExecCmdResult._get__NewEnum_metadata)

    _range_metadata = { "name" : "range",
            "arg_types" : (agcom.LONG, agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.LONG_arg, agmarshall.LPSAFEARRAY_arg,) }
    def range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        return self._intf.invoke(IExecCmdResult._metadata, IExecCmdResult._range_metadata, startIndex, stopIndex, out_arg())

    _get_is_succeeded_metadata = { "name" : "is_succeeded",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_succeeded(self) -> bool:
        """Indicates whether the object contains valid results."""
        return self._intf.get_property(IExecCmdResult._metadata, IExecCmdResult._get_is_succeeded_metadata)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{CC5C63BC-FF0A-4CC8-AD58-5A8D11DD9C60}", IExecCmdResult)
agcls.AgTypeNameMap["IExecCmdResult"] = IExecCmdResult

class IExecMultiCmdResult(object):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{ECEFEE1C-F623-4926-A738-3D95FC5E3DEE}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_count" : 1,
                             "item" : 2,
                             "get__NewEnum" : 3, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IExecMultiCmdResult._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IExecMultiCmdResult from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IExecMultiCmdResult.__dict__ and type(IExecMultiCmdResult.__dict__[attrname]) == property:
            return IExecMultiCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IExecMultiCmdResult.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IExecCmdResult":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(IExecMultiCmdResult._metadata, IExecMultiCmdResult._get_count_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.AgInterface_out_arg,) }
    def item(self, index:int) -> "ExecCmdResult":
        """Gets the element at the specified index (0-based)."""
        return self._intf.invoke(IExecMultiCmdResult._metadata, IExecMultiCmdResult._item_metadata, index, out_arg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Returns an object that can be used to iterate through all the objects in the collection."""
        return self._intf.get_property(IExecMultiCmdResult._metadata, IExecMultiCmdResult._get__NewEnum_metadata)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{ECEFEE1C-F623-4926-A738-3D95FC5E3DEE}", IExecMultiCmdResult)
agcls.AgTypeNameMap["IExecMultiCmdResult"] = IExecMultiCmdResult

class IUnitPreferencesUnit(object):
    """Provides info about a unit."""
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{4B4E2F51-280F-4E35-AEA5-71CDAC7342C4}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_full_name" : 1,
                             "get_abbrv" : 2,
                             "get_id" : 3,
                             "get_dimension" : 4, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUnitPreferencesUnit._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesUnit from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUnitPreferencesUnit.__dict__ and type(IUnitPreferencesUnit.__dict__[attrname]) == property:
            return IUnitPreferencesUnit.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUnitPreferencesUnit.")
    
    _get_full_name_metadata = { "name" : "full_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def full_name(self) -> str:
        """Returns the fullname of the unit."""
        return self._intf.get_property(IUnitPreferencesUnit._metadata, IUnitPreferencesUnit._get_full_name_metadata)

    _get_abbrv_metadata = { "name" : "abbrv",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def abbrv(self) -> str:
        """Returns the abbreviation of the unit."""
        return self._intf.get_property(IUnitPreferencesUnit._metadata, IUnitPreferencesUnit._get_abbrv_metadata)

    _get_id_metadata = { "name" : "id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def id(self) -> int:
        """Returns the ID of the unit."""
        return self._intf.get_property(IUnitPreferencesUnit._metadata, IUnitPreferencesUnit._get_id_metadata)

    _get_dimension_metadata = { "name" : "dimension",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def dimension(self) -> "UnitPreferencesDimension":
        """Returns the Dimension for this unit."""
        return self._intf.get_property(IUnitPreferencesUnit._metadata, IUnitPreferencesUnit._get_dimension_metadata)


agcls.AgClassCatalog.add_catalog_entry("{4B4E2F51-280F-4E35-AEA5-71CDAC7342C4}", IUnitPreferencesUnit)
agcls.AgTypeNameMap["IUnitPreferencesUnit"] = IUnitPreferencesUnit

class IUnitPreferencesUnitCollection(object):
    """Provides access to the Unit collection."""
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{C9A263F5-A021-4BEC-85F3-526FA41F1CB4}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "item" : 1,
                             "get_count" : 2,
                             "get__NewEnum" : 3,
                             "get_item_by_index" : 4,
                             "get_item_by_name" : 5, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUnitPreferencesUnitCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesUnitCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUnitPreferencesUnitCollection.__dict__ and type(IUnitPreferencesUnitCollection.__dict__[attrname]) == property:
            return IUnitPreferencesUnitCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUnitPreferencesUnitCollection.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IUnitPreferencesUnit":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.VARIANT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.AgInterface_out_arg,) }
    def item(self, indexOrName:typing.Any) -> "UnitPreferencesUnit":
        """Returns the specific item in the collection given a unit identifier or an index."""
        return self._intf.invoke(IUnitPreferencesUnitCollection._metadata, IUnitPreferencesUnitCollection._item_metadata, indexOrName, out_arg())

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Returns the number of items in the collection."""
        return self._intf.get_property(IUnitPreferencesUnitCollection._metadata, IUnitPreferencesUnitCollection._get_count_metadata)

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Returns an enumeration of UnitPreferencesUnit."""
        return self._intf.get_property(IUnitPreferencesUnitCollection._metadata, IUnitPreferencesUnitCollection._get__NewEnum_metadata)

    _get_item_by_index_metadata = { "name" : "get_item_by_index",
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.INT_arg, agmarshall.AgInterface_out_arg,) }
    def get_item_by_index(self, index:int) -> "UnitPreferencesUnit":
        """Retrieves a unit from the collection by index."""
        return self._intf.invoke(IUnitPreferencesUnitCollection._metadata, IUnitPreferencesUnitCollection._get_item_by_index_metadata, index, out_arg())

    _get_item_by_name_metadata = { "name" : "get_item_by_name",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def get_item_by_name(self, name:str) -> "UnitPreferencesUnit":
        """Retrieves a unit from the collection by name."""
        return self._intf.invoke(IUnitPreferencesUnitCollection._metadata, IUnitPreferencesUnitCollection._get_item_by_name_metadata, name, out_arg())

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{C9A263F5-A021-4BEC-85F3-526FA41F1CB4}", IUnitPreferencesUnitCollection)
agcls.AgTypeNameMap["IUnitPreferencesUnitCollection"] = IUnitPreferencesUnitCollection

class IUnitPreferencesDimensionCollection(object):
    """Provides accesses to the global unit table."""
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{40AE1C29-E5F5-426A-AEB7-D02CC7D2873C}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "item" : 1,
                             "get_count" : 2,
                             "set_current_unit" : 3,
                             "get_current_unit_abbrv" : 4,
                             "get_mission_elapsed_time" : 5,
                             "set_mission_elapsed_time" : 6,
                             "get_julian_date_offset" : 7,
                             "set_julian_date_offset" : 8,
                             "get__NewEnum" : 9,
                             "reset_units" : 10,
                             "get_item_by_index" : 11,
                             "get_item_by_name" : 12, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUnitPreferencesDimensionCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesDimensionCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUnitPreferencesDimensionCollection.__dict__ and type(IUnitPreferencesDimensionCollection.__dict__[attrname]) == property:
            return IUnitPreferencesDimensionCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUnitPreferencesDimensionCollection.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IUnitPreferencesDimension":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.VARIANT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.AgInterface_out_arg,) }
    def item(self, indexOrName:typing.Any) -> "UnitPreferencesDimension":
        """Returns an UnitPreferencesDimension given a Dimension name or an index."""
        return self._intf.invoke(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._item_metadata, indexOrName, out_arg())

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Returns the number of items in the collection."""
        return self._intf.get_property(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._get_count_metadata)

    _set_current_unit_metadata = { "name" : "set_current_unit",
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def set_current_unit(self, dimension:str, unitAbbrv:str) -> None:
        """Returns the Current unit for a Dimension."""
        return self._intf.invoke(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._set_current_unit_metadata, dimension, unitAbbrv)

    _get_current_unit_abbrv_metadata = { "name" : "get_current_unit_abbrv",
            "arg_types" : (agcom.VARIANT, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.BSTR_arg,) }
    def get_current_unit_abbrv(self, indexOrDimName:typing.Any) -> str:
        """Returns the Current Unit for a Dimension."""
        return self._intf.invoke(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._get_current_unit_abbrv_metadata, indexOrDimName, out_arg())

    _get_mission_elapsed_time_metadata = { "name" : "mission_elapsed_time",
            "arg_types" : (POINTER(agcom.VARIANT),),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @property
    def mission_elapsed_time(self) -> typing.Any:
        """The MissionElapsedTime."""
        return self._intf.get_property(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._get_mission_elapsed_time_metadata)

    _set_mission_elapsed_time_metadata = { "name" : "mission_elapsed_time",
            "arg_types" : (agcom.VARIANT,),
            "marshallers" : (agmarshall.VARIANT_arg,) }
    @mission_elapsed_time.setter
    def mission_elapsed_time(self, pMisElapTime:typing.Any) -> None:
        return self._intf.set_property(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._set_mission_elapsed_time_metadata, pMisElapTime)

    _get_julian_date_offset_metadata = { "name" : "julian_date_offset",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def julian_date_offset(self) -> float:
        """The JulianDateOffset."""
        return self._intf.get_property(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._get_julian_date_offset_metadata)

    _set_julian_date_offset_metadata = { "name" : "julian_date_offset",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @julian_date_offset.setter
    def julian_date_offset(self, pJDateOffset:float) -> None:
        return self._intf.set_property(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._set_julian_date_offset_metadata, pJDateOffset)

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Returns a collection of UnitPreferencesDimension."""
        return self._intf.get_property(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._get__NewEnum_metadata)

    _reset_units_metadata = { "name" : "reset_units",
            "arg_types" : (),
            "marshallers" : () }
    def reset_units(self) -> None:
        """Resets the unitpreferences to the Default units"""
        return self._intf.invoke(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._reset_units_metadata, )

    _get_item_by_index_metadata = { "name" : "get_item_by_index",
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.INT_arg, agmarshall.AgInterface_out_arg,) }
    def get_item_by_index(self, index:int) -> "UnitPreferencesDimension":
        """Retrieves a dimension from the collection by index."""
        return self._intf.invoke(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._get_item_by_index_metadata, index, out_arg())

    _get_item_by_name_metadata = { "name" : "get_item_by_name",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def get_item_by_name(self, name:str) -> "UnitPreferencesDimension":
        """Retrieves a dimension from the collection by name."""
        return self._intf.invoke(IUnitPreferencesDimensionCollection._metadata, IUnitPreferencesDimensionCollection._get_item_by_name_metadata, name, out_arg())

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{40AE1C29-E5F5-426A-AEB7-D02CC7D2873C}", IUnitPreferencesDimensionCollection)
agcls.AgTypeNameMap["IUnitPreferencesDimensionCollection"] = IUnitPreferencesDimensionCollection

class IQuantity(object):
    """Provides helper methods for a quantity."""
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{C0BBB39C-54E2-4344-B24E-58AA6AA4446B}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_dimension" : 1,
                             "get_unit" : 2,
                             "convert_to_unit" : 3,
                             "get_value" : 4,
                             "set_value" : 5,
                             "add" : 6,
                             "subtract" : 7,
                             "multiply_qty" : 8,
                             "divide_qty" : 9, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IQuantity._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IQuantity from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IQuantity.__dict__ and type(IQuantity.__dict__[attrname]) == property:
            return IQuantity.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IQuantity.")
    
    _get_dimension_metadata = { "name" : "dimension",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def dimension(self) -> str:
        """Gets the name of the dimension"""
        return self._intf.get_property(IQuantity._metadata, IQuantity._get_dimension_metadata)

    _get_unit_metadata = { "name" : "unit",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def unit(self) -> str:
        """The current Unit abbreviation."""
        return self._intf.get_property(IQuantity._metadata, IQuantity._get_unit_metadata)

    _convert_to_unit_metadata = { "name" : "convert_to_unit",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    def convert_to_unit(self, unitAbbrv:str) -> None:
        """Changes the value in this quantity to the specified unit."""
        return self._intf.invoke(IQuantity._metadata, IQuantity._convert_to_unit_metadata, unitAbbrv)

    _get_value_metadata = { "name" : "value",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def value(self) -> float:
        """The current value."""
        return self._intf.get_property(IQuantity._metadata, IQuantity._get_value_metadata)

    _set_value_metadata = { "name" : "value",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @value.setter
    def value(self, value:float) -> None:
        return self._intf.set_property(IQuantity._metadata, IQuantity._set_value_metadata, value)

    _add_metadata = { "name" : "add",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IQuantity"), agmarshall.AgInterface_out_arg,) }
    def add(self, quantity:"IQuantity") -> "Quantity":
        """Adds the value from the Quantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        return self._intf.invoke(IQuantity._metadata, IQuantity._add_metadata, quantity, out_arg())

    _subtract_metadata = { "name" : "subtract",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IQuantity"), agmarshall.AgInterface_out_arg,) }
    def subtract(self, quantity:"IQuantity") -> "Quantity":
        """Subtracts the value from the Quantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        return self._intf.invoke(IQuantity._metadata, IQuantity._subtract_metadata, quantity, out_arg())

    _multiply_qty_metadata = { "name" : "multiply_qty",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IQuantity"), agmarshall.AgInterface_out_arg,) }
    def multiply_qty(self, quantity:"IQuantity") -> "Quantity":
        """Multiplies the value from the Quantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        return self._intf.invoke(IQuantity._metadata, IQuantity._multiply_qty_metadata, quantity, out_arg())

    _divide_qty_metadata = { "name" : "divide_qty",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IQuantity"), agmarshall.AgInterface_out_arg,) }
    def divide_qty(self, quantity:"IQuantity") -> "Quantity":
        """Divides the value from the Quantity interface to this interface. The dimensions must be similar."""
        return self._intf.invoke(IQuantity._metadata, IQuantity._divide_qty_metadata, quantity, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{C0BBB39C-54E2-4344-B24E-58AA6AA4446B}", IQuantity)
agcls.AgTypeNameMap["IQuantity"] = IQuantity

class IDate(object):
    """Provides helper methods for a date."""
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{BFC8EA09-19BD-432A-923D-C553E8E37993}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "format" : 1,
                             "set_date" : 2,
                             "get_ole_date" : 3,
                             "set_ole_date" : 4,
                             "get_whole_days" : 5,
                             "set_whole_days" : 6,
                             "get_sec_into_day" : 7,
                             "set_sec_into_day" : 8,
                             "get_whole_days_utc" : 9,
                             "set_whole_days_utc" : 10,
                             "get_sec_into_day_utc" : 11,
                             "set_sec_into_day_utc" : 12,
                             "add" : 13,
                             "subtract" : 14,
                             "span" : 15, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDate._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDate from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDate.__dict__ and type(IDate.__dict__[attrname]) == property:
            return IDate.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IDate.")
    
    _format_metadata = { "name" : "format",
            "arg_types" : (agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def format(self, unit:str) -> str:
        """Returns the value of the date given the unit."""
        return self._intf.invoke(IDate._metadata, IDate._format_metadata, unit, out_arg())

    _set_date_metadata = { "name" : "set_date",
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def set_date(self, unit:str, value:str) -> None:
        """Sets this date with the given date value and unit type."""
        return self._intf.invoke(IDate._metadata, IDate._set_date_metadata, unit, value)

    _get_ole_date_metadata = { "name" : "ole_date",
            "arg_types" : (POINTER(agcom.DATE),),
            "marshallers" : (agmarshall.DATE_arg,) }
    @property
    def ole_date(self) -> datetime:
        """The current time in OLE DATE Format."""
        return self._intf.get_property(IDate._metadata, IDate._get_ole_date_metadata)

    _set_ole_date_metadata = { "name" : "ole_date",
            "arg_types" : (agcom.DATE,),
            "marshallers" : (agmarshall.DATE_arg,) }
    @ole_date.setter
    def ole_date(self, inVal:datetime) -> None:
        return self._intf.set_property(IDate._metadata, IDate._set_ole_date_metadata, inVal)

    _get_whole_days_metadata = { "name" : "whole_days",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def whole_days(self) -> int:
        """The Julian Day Number of the date of interest."""
        return self._intf.get_property(IDate._metadata, IDate._get_whole_days_metadata)

    _set_whole_days_metadata = { "name" : "whole_days",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @whole_days.setter
    def whole_days(self, wholeDays:int) -> None:
        return self._intf.set_property(IDate._metadata, IDate._set_whole_days_metadata, wholeDays)

    _get_sec_into_day_metadata = { "name" : "sec_into_day",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def sec_into_day(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0"""
        return self._intf.get_property(IDate._metadata, IDate._get_sec_into_day_metadata)

    _set_sec_into_day_metadata = { "name" : "sec_into_day",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @sec_into_day.setter
    def sec_into_day(self, secIntoDay:float) -> None:
        return self._intf.set_property(IDate._metadata, IDate._set_sec_into_day_metadata, secIntoDay)

    _get_whole_days_utc_metadata = { "name" : "whole_days_utc",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def whole_days_utc(self) -> int:
        """The UTC Day Number of the date of interest."""
        return self._intf.get_property(IDate._metadata, IDate._get_whole_days_utc_metadata)

    _set_whole_days_utc_metadata = { "name" : "whole_days_utc",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @whole_days_utc.setter
    def whole_days_utc(self, wholeDays:int) -> None:
        return self._intf.set_property(IDate._metadata, IDate._set_whole_days_utc_metadata, wholeDays)

    _get_sec_into_day_utc_metadata = { "name" : "sec_into_day_utc",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def sec_into_day_utc(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0"""
        return self._intf.get_property(IDate._metadata, IDate._get_sec_into_day_utc_metadata)

    _set_sec_into_day_utc_metadata = { "name" : "sec_into_day_utc",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @sec_into_day_utc.setter
    def sec_into_day_utc(self, secIntoDay:float) -> None:
        return self._intf.set_property(IDate._metadata, IDate._set_sec_into_day_utc_metadata, secIntoDay)

    _add_metadata = { "name" : "add",
            "arg_types" : (agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.DOUBLE_arg, agmarshall.AgInterface_out_arg,) }
    def add(self, unit:str, value:float) -> "Date":
        """Adds the value in the given unit and returns a new date interface."""
        return self._intf.invoke(IDate._metadata, IDate._add_metadata, unit, value, out_arg())

    _subtract_metadata = { "name" : "subtract",
            "arg_types" : (agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.DOUBLE_arg, agmarshall.AgInterface_out_arg,) }
    def subtract(self, unit:str, value:float) -> "Date":
        """Subtracts the value in the given unit and returns a new date interface."""
        return self._intf.invoke(IDate._metadata, IDate._subtract_metadata, unit, value, out_arg())

    _span_metadata = { "name" : "span",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IDate"), agmarshall.AgInterface_out_arg,) }
    def span(self, date:"IDate") -> "Quantity":
        """Subtracts the value from the Date interface and returns an Quantity."""
        return self._intf.invoke(IDate._metadata, IDate._span_metadata, date, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{BFC8EA09-19BD-432A-923D-C553E8E37993}", IDate)
agcls.AgTypeNameMap["IDate"] = IDate

class IConversionUtility(object):
    """Provides conversion utilities."""
    _num_methods = 18
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{2B04A4E2-C647-4920-88FF-DE0413252D1C}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "convert_quantity" : 1,
                             "convert_date" : 2,
                             "convert_quantity_array" : 3,
                             "convert_date_array" : 4,
                             "new_quantity" : 5,
                             "new_date" : 6,
                             "new_position_on_earth" : 7,
                             "convert_position_array" : 8,
                             "new_direction" : 9,
                             "new_orientation" : 10,
                             "new_orbit_state_on_earth" : 11,
                             "new_position_on_cb" : 12,
                             "new_orbit_state_on_cb" : 13,
                             "query_direction_cosine_matrix" : 14,
                             "query_direction_cosine_matrix_array" : 15,
                             "new_cartesian3_vector" : 16,
                             "new_cartesian3_vector_from_direction" : 17,
                             "new_cartesian3_vector_from_position" : 18, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IConversionUtility._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IConversionUtility from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IConversionUtility.__dict__ and type(IConversionUtility.__dict__[attrname]) == property:
            return IConversionUtility.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IConversionUtility.")
    
    _convert_quantity_metadata = { "name" : "convert_quantity",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg,) }
    def convert_quantity(self, dimensionName:str, fromUnit:str, toUnit:str, fromValue:float) -> float:
        """Converts the specified quantity value from a given unit to another unit."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._convert_quantity_metadata, dimensionName, fromUnit, toUnit, fromValue, out_arg())

    _convert_date_metadata = { "name" : "convert_date",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def convert_date(self, fromUnit:str, toUnit:str, fromValue:str) -> str:
        """Converts the specified date from a given unit to another unit."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._convert_date_metadata, fromUnit, toUnit, fromValue, out_arg())

    _convert_quantity_array_metadata = { "name" : "convert_quantity_array",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.LPSAFEARRAY), POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.LPSAFEARRAY_arg, agmarshall.LPSAFEARRAY_arg,) }
    def convert_quantity_array(self, dimensionName:str, fromUnit:str, toUnit:str, quantityValues:list) -> list:
        """Converts the specified quantity values from a given unit to another unit."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._convert_quantity_array_metadata, dimensionName, fromUnit, toUnit, quantityValues, out_arg())

    _convert_date_array_metadata = { "name" : "convert_date_array",
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.LPSAFEARRAY), POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.LPSAFEARRAY_arg, agmarshall.LPSAFEARRAY_arg,) }
    def convert_date_array(self, fromUnit:str, toUnit:str, fromValues:list) -> list:
        """Converts the specified dates from a given unit to another unit."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._convert_date_array_metadata, fromUnit, toUnit, fromValues, out_arg())

    _new_quantity_metadata = { "name" : "new_quantity",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.DOUBLE_arg, agmarshall.AgInterface_out_arg,) }
    def new_quantity(self, dimension:str, unitAbbrv:str, value:float) -> "Quantity":
        """Creates an Quantity interface with the given dimension, unit and value"""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_quantity_metadata, dimension, unitAbbrv, value, out_arg())

    _new_date_metadata = { "name" : "new_date",
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def new_date(self, unitAbbrv:str, value:str) -> "Date":
        """Creates an Date interface with the given unit and value"""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_date_metadata, unitAbbrv, value, out_arg())

    _new_position_on_earth_metadata = { "name" : "new_position_on_earth",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    def new_position_on_earth(self) -> "IPosition":
        """Creates an IPosition interface with earth as its central body."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_position_on_earth_metadata, out_arg())

    _convert_position_array_metadata = { "name" : "convert_position_array",
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY), agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.AgEnum_arg(POSITION_TYPE), agmarshall.LPSAFEARRAY_arg, agmarshall.AgEnum_arg(POSITION_TYPE), agmarshall.LPSAFEARRAY_arg,) }
    def convert_position_array(self, positionType:"POSITION_TYPE", positionArray:list, convertTo:"POSITION_TYPE") -> list:
        """Converts the specified position values from a given position type to another position type."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._convert_position_array_metadata, positionType, positionArray, convertTo, out_arg())

    _new_direction_metadata = { "name" : "new_direction",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    def new_direction(self) -> "IDirection":
        """Creates an IDirection interface."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_direction_metadata, out_arg())

    _new_orientation_metadata = { "name" : "new_orientation",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    def new_orientation(self) -> "IOrientation":
        """Creates an IOrientation interface."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_orientation_metadata, out_arg())

    _new_orbit_state_on_earth_metadata = { "name" : "new_orbit_state_on_earth",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    def new_orbit_state_on_earth(self) -> "IOrbitState":
        """Creates an IOrbitState interface with earth as its central body."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_orbit_state_on_earth_metadata, out_arg())

    _new_position_on_cb_metadata = { "name" : "new_position_on_cb",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def new_position_on_cb(self, centralBodyName:str) -> "IPosition":
        """Creates an IPosition interface using the supplied central body."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_position_on_cb_metadata, centralBodyName, out_arg())

    _new_orbit_state_on_cb_metadata = { "name" : "new_orbit_state_on_cb",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def new_orbit_state_on_cb(self, centralBodyName:str) -> "IOrbitState":
        """Creates an IOrbitState interface using the supplied central body."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_orbit_state_on_cb_metadata, centralBodyName, out_arg())

    _query_direction_cosine_matrix_metadata = { "name" : "query_direction_cosine_matrix",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID), POINTER(agcom.PVOID), POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IOrientation"), agmarshall.AgInterface_out_arg, agmarshall.AgInterface_out_arg, agmarshall.AgInterface_out_arg,) }
    def query_direction_cosine_matrix(self, inputOrientation:"IOrientation") -> typing.Tuple[ICartesian3Vector, ICartesian3Vector, ICartesian3Vector]:
        """Returns a Direction Cosine Matrix (DCM)."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._query_direction_cosine_matrix_metadata, inputOrientation, out_arg(), out_arg(), out_arg())

    _query_direction_cosine_matrix_array_metadata = { "name" : "query_direction_cosine_matrix_array",
            "arg_types" : (agcom.PVOID, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IOrientation"), agmarshall.LPSAFEARRAY_arg,) }
    def query_direction_cosine_matrix_array(self, inputOrientation:"IOrientation") -> list:
        """Returns a Direction Cosine Matrix (DCM) as an array."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._query_direction_cosine_matrix_array_metadata, inputOrientation, out_arg())

    _new_cartesian3_vector_metadata = { "name" : "new_cartesian3_vector",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    def new_cartesian3_vector(self) -> "ICartesian3Vector":
        """Creates a cartesian vector."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_cartesian3_vector_metadata, out_arg())

    _new_cartesian3_vector_from_direction_metadata = { "name" : "new_cartesian3_vector_from_direction",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IDirection"), agmarshall.AgInterface_out_arg,) }
    def new_cartesian3_vector_from_direction(self, inputDirection:"IDirection") -> "ICartesian3Vector":
        """Converts the direction to cartesian vector."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_cartesian3_vector_from_direction_metadata, inputDirection, out_arg())

    _new_cartesian3_vector_from_position_metadata = { "name" : "new_cartesian3_vector_from_position",
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_in_arg("IPosition"), agmarshall.AgInterface_out_arg,) }
    def new_cartesian3_vector_from_position(self, inputPosition:"IPosition") -> "ICartesian3Vector":
        """Converts the position to cartesian vector."""
        return self._intf.invoke(IConversionUtility._metadata, IConversionUtility._new_cartesian3_vector_from_position_metadata, inputPosition, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{2B04A4E2-C647-4920-88FF-DE0413252D1C}", IConversionUtility)
agcls.AgTypeNameMap["IConversionUtility"] = IConversionUtility

class IDoublesCollection(object):
    """Represents a collection of doubles."""
    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{DEE2EB74-C19C-44C9-8825-09010A8F60BE}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "item" : 1,
                             "get_count" : 2,
                             "get__NewEnum" : 3,
                             "add" : 4,
                             "remove_at" : 5,
                             "remove_all" : 6,
                             "to_array" : 7,
                             "set_at" : 8, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDoublesCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDoublesCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDoublesCollection.__dict__ and type(IDoublesCollection.__dict__[attrname]) == property:
            return IDoublesCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IDoublesCollection.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> float:
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.DOUBLE_arg,) }
    def item(self, index:int) -> float:
        """Returns a double at a specified position."""
        return self._intf.invoke(IDoublesCollection._metadata, IDoublesCollection._item_metadata, index, out_arg())

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Returns the number of items in the collection."""
        return self._intf.get_property(IDoublesCollection._metadata, IDoublesCollection._get_count_metadata)

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Returns a collection enumerator."""
        return self._intf.get_property(IDoublesCollection._metadata, IDoublesCollection._get__NewEnum_metadata)

    _add_metadata = { "name" : "add",
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    def add(self, value:float) -> None:
        """Add a value to the collection of doubles."""
        return self._intf.invoke(IDoublesCollection._metadata, IDoublesCollection._add_metadata, value)

    _remove_at_metadata = { "name" : "remove_at",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    def remove_at(self, index:int) -> None:
        """Remove an element from the collection at a specified position."""
        return self._intf.invoke(IDoublesCollection._metadata, IDoublesCollection._remove_at_metadata, index)

    _remove_all_metadata = { "name" : "remove_all",
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clears the collection."""
        return self._intf.invoke(IDoublesCollection._metadata, IDoublesCollection._remove_all_metadata, )

    _to_array_metadata = { "name" : "to_array",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg,) }
    def to_array(self) -> list:
        """Returns an array of the elements in the collection"""
        return self._intf.invoke(IDoublesCollection._metadata, IDoublesCollection._to_array_metadata, out_arg())

    _set_at_metadata = { "name" : "set_at",
            "arg_types" : (agcom.LONG, agcom.DOUBLE,),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.DOUBLE_arg,) }
    def set_at(self, index:int, value:float) -> None:
        """Updates an element in the collection at a specified position."""
        return self._intf.invoke(IDoublesCollection._metadata, IDoublesCollection._set_at_metadata, index, value)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{DEE2EB74-C19C-44C9-8825-09010A8F60BE}", IDoublesCollection)
agcls.AgTypeNameMap["IDoublesCollection"] = IDoublesCollection



class ExecCmdResult(IExecCmdResult):
    """Collection of strings returned by the ExecuteCommand."""
    def __init__(self, sourceObject=None):
        IExecCmdResult.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IExecCmdResult._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IExecCmdResult._get_property(self, attrname) is not None: found_prop = IExecCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ExecCmdResult.")

agcls.AgClassCatalog.add_catalog_entry("{92FE4418-FBA3-4D69-8F6E-9F600A1BA5E0}", ExecCmdResult)
agcls.AgTypeNameMap["ExecCmdResult"] = ExecCmdResult

class ExecMultiCmdResult(IExecMultiCmdResult):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    def __init__(self, sourceObject=None):
        IExecMultiCmdResult.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IExecMultiCmdResult._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IExecMultiCmdResult._get_property(self, attrname) is not None: found_prop = IExecMultiCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ExecMultiCmdResult.")

agcls.AgClassCatalog.add_catalog_entry("{4B262721-FD3F-4DAD-BF32-4280752B7FE6}", ExecMultiCmdResult)
agcls.AgTypeNameMap["ExecMultiCmdResult"] = ExecMultiCmdResult

class UnitPreferencesUnit(IUnitPreferencesUnit):
    """Object that contains info on the unit."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesUnit.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUnitPreferencesUnit._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUnitPreferencesUnit._get_property(self, attrname) is not None: found_prop = IUnitPreferencesUnit._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UnitPreferencesUnit.")

agcls.AgClassCatalog.add_catalog_entry("{4EDA384D-4C61-4756-92FF-1CD7C8049B96}", UnitPreferencesUnit)
agcls.AgTypeNameMap["UnitPreferencesUnit"] = UnitPreferencesUnit

class UnitPreferencesUnitCollection(IUnitPreferencesUnitCollection):
    """Object that contains a collection of UnitPreferencesUnit."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesUnitCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUnitPreferencesUnitCollection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUnitPreferencesUnitCollection._get_property(self, attrname) is not None: found_prop = IUnitPreferencesUnitCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UnitPreferencesUnitCollection.")

agcls.AgClassCatalog.add_catalog_entry("{21AEACA4-B79D-455B-8DA4-89402A57A87B}", UnitPreferencesUnitCollection)
agcls.AgTypeNameMap["UnitPreferencesUnitCollection"] = UnitPreferencesUnitCollection

class UnitPreferencesDimension(IUnitPreferencesDimension):
    """Object that contains info on the Dimension."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesDimension.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUnitPreferencesDimension._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUnitPreferencesDimension._get_property(self, attrname) is not None: found_prop = IUnitPreferencesDimension._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UnitPreferencesDimension.")

agcls.AgClassCatalog.add_catalog_entry("{5DB8F1AE-1240-4929-B7FD-75E0800970EB}", UnitPreferencesDimension)
agcls.AgTypeNameMap["UnitPreferencesDimension"] = UnitPreferencesDimension

class UnitPreferencesDimensionCollection(IUnitPreferencesDimensionCollection):
    """Object that contains a collection of dimensions."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesDimensionCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUnitPreferencesDimensionCollection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUnitPreferencesDimensionCollection._get_property(self, attrname) is not None: found_prop = IUnitPreferencesDimensionCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UnitPreferencesDimensionCollection.")

agcls.AgClassCatalog.add_catalog_entry("{58562305-1D39-4B56-9FA8-AB49FEB68A37}", UnitPreferencesDimensionCollection)
agcls.AgTypeNameMap["UnitPreferencesDimensionCollection"] = UnitPreferencesDimensionCollection

class ConversionUtility(IConversionUtility):
    """Object that contains a unit conversion utility."""
    def __init__(self, sourceObject=None):
        IConversionUtility.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IConversionUtility._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IConversionUtility._get_property(self, attrname) is not None: found_prop = IConversionUtility._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ConversionUtility.")

agcls.AgClassCatalog.add_catalog_entry("{89E0FDC5-4016-47E9-96ED-0C1B05FFDADA}", ConversionUtility)
agcls.AgTypeNameMap["ConversionUtility"] = ConversionUtility

class Quantity(IQuantity):
    """Object that contains a quantity."""
    def __init__(self, sourceObject=None):
        IQuantity.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IQuantity._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IQuantity._get_property(self, attrname) is not None: found_prop = IQuantity._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Quantity.")

agcls.AgClassCatalog.add_catalog_entry("{59806B16-8D20-4EC3-8913-9457846AC0E5}", Quantity)
agcls.AgTypeNameMap["Quantity"] = Quantity

class Date(IDate):
    """Object that contains a date."""
    def __init__(self, sourceObject=None):
        IDate.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDate._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDate._get_property(self, attrname) is not None: found_prop = IDate._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Date.")

agcls.AgClassCatalog.add_catalog_entry("{CC2BA6FD-3A05-46D1-BAA0-68AC2D7896F1}", Date)
agcls.AgTypeNameMap["Date"] = Date

class Position(ILocationData, IPosition):
    """The Position class."""
    def __init__(self, sourceObject=None):
        ILocationData.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ILocationData._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ILocationData._get_property(self, attrname) is not None: found_prop = ILocationData._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Position.")

agcls.AgClassCatalog.add_catalog_entry("{B3FE87C4-702C-4263-83D8-4E32C993E2D0}", Position)
agcls.AgTypeNameMap["Position"] = Position

class Cartesian(ICartesian, IPosition):
    """Class used to access a position using Cartesian Coordinates."""
    def __init__(self, sourceObject=None):
        ICartesian.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ICartesian._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ICartesian._get_property(self, attrname) is not None: found_prop = ICartesian._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Cartesian.")

agcls.AgClassCatalog.add_catalog_entry("{027F342E-5989-43D1-831B-BF2E313A1CBB}", Cartesian)
agcls.AgTypeNameMap["Cartesian"] = Cartesian

class Geodetic(IGeodetic, IPosition):
    """Class defining Geodetic position."""
    def __init__(self, sourceObject=None):
        IGeodetic.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IGeodetic._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IGeodetic._get_property(self, attrname) is not None: found_prop = IGeodetic._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Geodetic.")

agcls.AgClassCatalog.add_catalog_entry("{F65DA479-6847-456B-8816-85FF3ECD4469}", Geodetic)
agcls.AgTypeNameMap["Geodetic"] = Geodetic

class Geocentric(IGeocentric, IPosition):
    """Class defining Geocentric position."""
    def __init__(self, sourceObject=None):
        IGeocentric.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IGeocentric._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IGeocentric._get_property(self, attrname) is not None: found_prop = IGeocentric._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Geocentric.")

agcls.AgClassCatalog.add_catalog_entry("{1AC9E304-8DCE-4CD6-A5AA-B82738823556}", Geocentric)
agcls.AgTypeNameMap["Geocentric"] = Geocentric

class Planetodetic(IPlanetodetic, IPosition):
    """Class defining Planetodetic position."""
    def __init__(self, sourceObject=None):
        IPlanetodetic.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPlanetodetic._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IPlanetodetic._get_property(self, attrname) is not None: found_prop = IPlanetodetic._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Planetodetic.")

agcls.AgClassCatalog.add_catalog_entry("{E06625DF-EEB4-4384-B142-C1C501F522F8}", Planetodetic)
agcls.AgTypeNameMap["Planetodetic"] = Planetodetic

class Planetocentric(IPlanetocentric, IPosition):
    """Class defining Planetocentric position."""
    def __init__(self, sourceObject=None):
        IPlanetocentric.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPlanetocentric._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IPlanetocentric._get_property(self, attrname) is not None: found_prop = IPlanetocentric._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Planetocentric.")

agcls.AgClassCatalog.add_catalog_entry("{DB009F3C-1FA7-4241-8A8D-D55E234CFF02}", Planetocentric)
agcls.AgTypeNameMap["Planetocentric"] = Planetocentric

class Spherical(ISpherical, IPosition):
    """Class defining spherical position."""
    def __init__(self, sourceObject=None):
        ISpherical.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ISpherical._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ISpherical._get_property(self, attrname) is not None: found_prop = ISpherical._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Spherical.")

agcls.AgClassCatalog.add_catalog_entry("{CD809FAC-48DF-46AB-A322-92947F84C7E6}", Spherical)
agcls.AgTypeNameMap["Spherical"] = Spherical

class Cylindrical(ICylindrical, IPosition):
    """Class defining cylindrical position."""
    def __init__(self, sourceObject=None):
        ICylindrical.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ICylindrical._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ICylindrical._get_property(self, attrname) is not None: found_prop = ICylindrical._get_property(self, attrname)
        if IPosition._get_property(self, attrname) is not None: found_prop = IPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Cylindrical.")

agcls.AgClassCatalog.add_catalog_entry("{FF1B8082-F06B-4F7B-94B2-6D3C4D9A7D51}", Cylindrical)
agcls.AgTypeNameMap["Cylindrical"] = Cylindrical

class Direction(IDirection):
    """Class defining direction options for aligned and constrained vectors."""
    def __init__(self, sourceObject=None):
        IDirection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDirection._get_property(self, attrname) is not None: found_prop = IDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Direction.")

agcls.AgClassCatalog.add_catalog_entry("{9BC95D30-4E21-4502-ADE6-2AAE9ED89903}", Direction)
agcls.AgTypeNameMap["Direction"] = Direction

class DirectionEuler(IDirectionEuler, IDirection):
    """Euler direction sequence."""
    def __init__(self, sourceObject=None):
        IDirectionEuler.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirectionEuler._private_init(self, intf)
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDirectionEuler._get_property(self, attrname) is not None: found_prop = IDirectionEuler._get_property(self, attrname)
        if IDirection._get_property(self, attrname) is not None: found_prop = IDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DirectionEuler.")

agcls.AgClassCatalog.add_catalog_entry("{A14FAC2D-C055-4FB4-9AAD-67314E647717}", DirectionEuler)
agcls.AgTypeNameMap["DirectionEuler"] = DirectionEuler

class DirectionPR(IDirectionPR, IDirection):
    """Pitch-Roll (PR) direction sequence."""
    def __init__(self, sourceObject=None):
        IDirectionPR.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirectionPR._private_init(self, intf)
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDirectionPR._get_property(self, attrname) is not None: found_prop = IDirectionPR._get_property(self, attrname)
        if IDirection._get_property(self, attrname) is not None: found_prop = IDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DirectionPR.")

agcls.AgClassCatalog.add_catalog_entry("{3EEEDD8D-FB4C-442D-8A1F-28C7A3C2C9A6}", DirectionPR)
agcls.AgTypeNameMap["DirectionPR"] = DirectionPR

class DirectionRADec(IDirectionRADec, IDirection):
    """Spherical direction (Right Ascension and Declination)."""
    def __init__(self, sourceObject=None):
        IDirectionRADec.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirectionRADec._private_init(self, intf)
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDirectionRADec._get_property(self, attrname) is not None: found_prop = IDirectionRADec._get_property(self, attrname)
        if IDirection._get_property(self, attrname) is not None: found_prop = IDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DirectionRADec.")

agcls.AgClassCatalog.add_catalog_entry("{EB70218F-18C4-41FE-90AC-99AFEB243666}", DirectionRADec)
agcls.AgTypeNameMap["DirectionRADec"] = DirectionRADec

class DirectionXYZ(IDirectionXYZ, IDirection):
    """Cartesian direction."""
    def __init__(self, sourceObject=None):
        IDirectionXYZ.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDirectionXYZ._private_init(self, intf)
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDirectionXYZ._get_property(self, attrname) is not None: found_prop = IDirectionXYZ._get_property(self, attrname)
        if IDirection._get_property(self, attrname) is not None: found_prop = IDirection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DirectionXYZ.")

agcls.AgClassCatalog.add_catalog_entry("{E1AB8359-28B7-468F-BD92-378267CA0998}", DirectionXYZ)
agcls.AgTypeNameMap["DirectionXYZ"] = DirectionXYZ

class Orientation(IOrientation):
    """Class defining the orientation of an orbit."""
    def __init__(self, sourceObject=None):
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Orientation.")

agcls.AgClassCatalog.add_catalog_entry("{97DF3B0E-D8E0-46B1-88CB-DC7A0AF934AE}", Orientation)
agcls.AgTypeNameMap["Orientation"] = Orientation

class OrientationAzEl(IOrientationAzEl, IOrientation):
    """AzEl orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationAzEl.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationAzEl._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationAzEl._get_property(self, attrname) is not None: found_prop = IOrientationAzEl._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in OrientationAzEl.")

agcls.AgClassCatalog.add_catalog_entry("{3CF365C4-9B79-4B72-A479-16EF921F791C}", OrientationAzEl)
agcls.AgTypeNameMap["OrientationAzEl"] = OrientationAzEl

class OrientationEulerAngles(IOrientationEulerAngles, IOrientation):
    """Euler Angles orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationEulerAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationEulerAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationEulerAngles._get_property(self, attrname) is not None: found_prop = IOrientationEulerAngles._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in OrientationEulerAngles.")

agcls.AgClassCatalog.add_catalog_entry("{C3DC0E0A-690B-4C20-9134-D6C57BE46D40}", OrientationEulerAngles)
agcls.AgTypeNameMap["OrientationEulerAngles"] = OrientationEulerAngles

class OrientationQuaternion(IOrientationQuaternion, IOrientation):
    """Quaternion orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationQuaternion.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationQuaternion._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationQuaternion._get_property(self, attrname) is not None: found_prop = IOrientationQuaternion._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in OrientationQuaternion.")

agcls.AgClassCatalog.add_catalog_entry("{8AC57BB2-C7A7-4C05-9E35-7246956759D9}", OrientationQuaternion)
agcls.AgTypeNameMap["OrientationQuaternion"] = OrientationQuaternion

class OrientationYPRAngles(IOrientationYPRAngles, IOrientation):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, sourceObject=None):
        IOrientationYPRAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationYPRAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationYPRAngles._get_property(self, attrname) is not None: found_prop = IOrientationYPRAngles._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in OrientationYPRAngles.")

agcls.AgClassCatalog.add_catalog_entry("{AE398C98-2D0D-4863-8097-9F7648CABC21}", OrientationYPRAngles)
agcls.AgTypeNameMap["OrientationYPRAngles"] = OrientationYPRAngles

class DoublesCollection(IDoublesCollection):
    """A collection of doubles."""
    def __init__(self, sourceObject=None):
        IDoublesCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDoublesCollection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDoublesCollection._get_property(self, attrname) is not None: found_prop = IDoublesCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DoublesCollection.")

agcls.AgClassCatalog.add_catalog_entry("{ECD576C3-0440-44D9-9D16-B88873C3A816}", DoublesCollection)
agcls.AgTypeNameMap["DoublesCollection"] = DoublesCollection

class Cartesian3Vector(ICartesian3Vector):
    """A 3-D cartesian vector."""
    def __init__(self, sourceObject=None):
        ICartesian3Vector.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ICartesian3Vector._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ICartesian3Vector._get_property(self, attrname) is not None: found_prop = ICartesian3Vector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Cartesian3Vector.")

agcls.AgClassCatalog.add_catalog_entry("{4A70BA75-BC1A-459D-9DAD-E174F3B94002}", Cartesian3Vector)
agcls.AgTypeNameMap["Cartesian3Vector"] = Cartesian3Vector

class Cartesian2Vector(ICartesian2Vector):
    """A 2-D cartesian vector."""
    def __init__(self, sourceObject=None):
        ICartesian2Vector.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ICartesian2Vector._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ICartesian2Vector._get_property(self, attrname) is not None: found_prop = ICartesian2Vector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Cartesian2Vector.")

agcls.AgClassCatalog.add_catalog_entry("{ECE2E7DF-CBF1-4124-AAAC-33700F16FAE2}", Cartesian2Vector)
agcls.AgTypeNameMap["Cartesian2Vector"] = Cartesian2Vector

class PropertyInfo(IPropertyInfo):
    """Property Information coclass."""
    def __init__(self, sourceObject=None):
        IPropertyInfo.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPropertyInfo._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IPropertyInfo._get_property(self, attrname) is not None: found_prop = IPropertyInfo._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in PropertyInfo.")

agcls.AgClassCatalog.add_catalog_entry("{92498440-7C87-495C-A8BD-0A70F85D4DC8}", PropertyInfo)
agcls.AgTypeNameMap["PropertyInfo"] = PropertyInfo

class PropertyInfoCollection(IPropertyInfoCollection):
    """Property Information Collection coclass."""
    def __init__(self, sourceObject=None):
        IPropertyInfoCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPropertyInfoCollection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IPropertyInfoCollection._get_property(self, attrname) is not None: found_prop = IPropertyInfoCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in PropertyInfoCollection.")

agcls.AgClassCatalog.add_catalog_entry("{113B1CA1-4DD4-4915-8D7F-E1F96E18A985}", PropertyInfoCollection)
agcls.AgTypeNameMap["PropertyInfoCollection"] = PropertyInfoCollection

class RuntimeTypeInfo(IRuntimeTypeInfo):
    """Runtime Type info coclass."""
    def __init__(self, sourceObject=None):
        IRuntimeTypeInfo.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IRuntimeTypeInfo._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IRuntimeTypeInfo._get_property(self, attrname) is not None: found_prop = IRuntimeTypeInfo._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in RuntimeTypeInfo.")

agcls.AgClassCatalog.add_catalog_entry("{D80F3E93-932A-49B3-8661-1A1627DCBDD1}", RuntimeTypeInfo)
agcls.AgTypeNameMap["RuntimeTypeInfo"] = RuntimeTypeInfo

class CROrientationAzEl(IOrientationAzEl, IOrientation, IOrientationPositionOffset):
    """AzEl orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationAzEl.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationAzEl._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationAzEl._get_property(self, attrname) is not None: found_prop = IOrientationAzEl._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if IOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in CROrientationAzEl.")

agcls.AgClassCatalog.add_catalog_entry("{1E11E3CE-BCAA-4E1F-BAF9-B6AD3650F9BA}", CROrientationAzEl)
agcls.AgTypeNameMap["CROrientationAzEl"] = CROrientationAzEl

class CROrientationEulerAngles(IOrientationEulerAngles, IOrientation, IOrientationPositionOffset):
    """Euler Angles orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationEulerAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationEulerAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationEulerAngles._get_property(self, attrname) is not None: found_prop = IOrientationEulerAngles._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if IOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in CROrientationEulerAngles.")

agcls.AgClassCatalog.add_catalog_entry("{D08A5BF9-5CBA-432D-8C48-3CD1CFC42636}", CROrientationEulerAngles)
agcls.AgTypeNameMap["CROrientationEulerAngles"] = CROrientationEulerAngles

class CROrientationQuaternion(IOrientationQuaternion, IOrientation, IOrientationPositionOffset):
    """Quaternion orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationQuaternion.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationQuaternion._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationQuaternion._get_property(self, attrname) is not None: found_prop = IOrientationQuaternion._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if IOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in CROrientationQuaternion.")

agcls.AgClassCatalog.add_catalog_entry("{9D3BA3F8-B6F6-443B-A8AC-74C86A8B901A}", CROrientationQuaternion)
agcls.AgTypeNameMap["CROrientationQuaternion"] = CROrientationQuaternion

class CROrientationYPRAngles(IOrientationYPRAngles, IOrientation, IOrientationPositionOffset):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, sourceObject=None):
        IOrientationYPRAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IOrientationYPRAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IOrientationYPRAngles._get_property(self, attrname) is not None: found_prop = IOrientationYPRAngles._get_property(self, attrname)
        if IOrientation._get_property(self, attrname) is not None: found_prop = IOrientation._get_property(self, attrname)
        if IOrientationPositionOffset._get_property(self, attrname) is not None: found_prop = IOrientationPositionOffset._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in CROrientationYPRAngles.")

agcls.AgClassCatalog.add_catalog_entry("{1FB88B69-1844-4CD9-BD44-09A9FCC4E06F}", CROrientationYPRAngles)
agcls.AgTypeNameMap["CROrientationYPRAngles"] = CROrientationYPRAngles

class CROrientationOffsetCart(ICartesian3Vector):
    """Orientation offset cartesian."""
    def __init__(self, sourceObject=None):
        ICartesian3Vector.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ICartesian3Vector._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ICartesian3Vector._get_property(self, attrname) is not None: found_prop = ICartesian3Vector._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in CROrientationOffsetCart.")

agcls.AgClassCatalog.add_catalog_entry("{462F58AA-A74F-4E42-88B6-8F2790E85FEC}", CROrientationOffsetCart)
agcls.AgTypeNameMap["CROrientationOffsetCart"] = CROrientationOffsetCart


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
