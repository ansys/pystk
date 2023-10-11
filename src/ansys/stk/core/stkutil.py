################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["AZ_EL_ABOUT_BORESIGHT", "COORDINATE_SYSTEM", "CROrientationAzEl", "CROrientationEulerAngles", "CROrientationOffsetCart", 
"CROrientationQuaternion", "CROrientationYPRAngles", "Cartesian", "Cartesian2Vector", "Cartesian3Vector", "ConversionUtility", 
"Cylindrical", "DIRECTION_TYPE", "Date", "Direction", "DirectionEuler", "DirectionPR", "DirectionRADec", "DirectionXYZ", 
"DoublesCollection", "EULER_DIRECTION_SEQUENCE", "EULER_ORIENTATION_SEQUENCE", "EXEC_MULTI_CMD_RESULT_ACTION", "ExecCmdResult", 
"ExecMultiCmdResult", "FILL_STYLE", "Geocentric", "Geodetic", "ICartesian", "ICartesian2Vector", "ICartesian3Vector", "IConversionUtility", 
"ICylindrical", "IDate", "IDirection", "IDirectionEuler", "IDirectionPR", "IDirectionRADec", "IDirectionXYZ", "IDoublesCollection", 
"IExecCmdResult", "IExecMultiCmdResult", "IGeocentric", "IGeodetic", "ILocationData", "IOrbitState", "IOrientation", "IOrientationAzEl", 
"IOrientationEulerAngles", "IOrientationPositionOffset", "IOrientationQuaternion", "IOrientationYPRAngles", "IPlanetocentric", 
"IPlanetodetic", "IPosition", "IPropertyInfo", "IPropertyInfoCollection", "IQuantity", "IRuntimeTypeInfo", "IRuntimeTypeInfoProvider", 
"ISpherical", "IUnitPreferencesDimension", "IUnitPreferencesDimensionCollection", "IUnitPreferencesUnit", "IUnitPreferencesUnitCollection", 
"LINE_STYLE", "LOG_MSG_DISP_ID", "LOG_MSG_TYPE", "ORBIT_STATE_TYPE", "ORIENTATION_TYPE", "Orientation", "OrientationAzEl", 
"OrientationEulerAngles", "OrientationQuaternion", "OrientationYPRAngles", "POSITION_TYPE", "PROPERTY_INFO_VALUE_TYPE", 
"PR_SEQUENCE", "Planetocentric", "Planetodetic", "Position", "PropertyInfo", "PropertyInfoCollection", "Quantity", "RuntimeTypeInfo", 
"Spherical", "UnitPreferencesDimension", "UnitPreferencesDimensionCollection", "UnitPreferencesUnit", "UnitPreferencesUnitCollection", 
"YPR_ANGLES_SEQUENCE"]

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
from .internal.comutil     import IUnknown, IDispatch, IAGFUNCTYPE, IEnumVARIANT
from .internal.eventutil   import *
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
    """Property is of type IQuantity."""
    DATE = 3
    """Property is of type IDate."""
    STRING = 4
    """Property is of type string."""
    BOOL = 5
    """Property is of type bool."""
    INTERFACE = 6
    """Property is an interface."""

PROPERTY_INFO_VALUE_TYPE.INT.__doc__ = "Property is of type int."
PROPERTY_INFO_VALUE_TYPE.REAL.__doc__ = "Property is of type real."
PROPERTY_INFO_VALUE_TYPE.QUANTITY.__doc__ = "Property is of type IQuantity."
PROPERTY_INFO_VALUE_TYPE.DATE.__doc__ = "Property is of type IDate."
PROPERTY_INFO_VALUE_TYPE.STRING.__doc__ = "Property is of type string."
PROPERTY_INFO_VALUE_TYPE.BOOL.__doc__ = "Property is of type bool."
PROPERTY_INFO_VALUE_TYPE.INTERFACE.__doc__ = "Property is an interface."

agcls.AgTypeNameMap["PROPERTY_INFO_VALUE_TYPE"] = PROPERTY_INFO_VALUE_TYPE


class ILocationData(object):
    """Base interface ILocationData. IPosition derives from this interface."""
    _uuid = "{C1E99EDA-C666-4971-AFD0-2259CB7E8452}"
    _num_methods = 0
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ILocationData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ILocationData from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_ILocationData = agcom.GUID(ILocationData._uuid)
        vtable_offset_local = ILocationData._vtable_offset - 1
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
    _uuid = "{F25960CE-1D73-4BA0-A429-541DD6D808DE}"
    _num_methods = 21
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_convert_to"] = _raise_uninitialized_error
        self.__dict__["_get_position_type"] = _raise_uninitialized_error
        self.__dict__["_assign"] = _raise_uninitialized_error
        self.__dict__["_assign_geocentric"] = _raise_uninitialized_error
        self.__dict__["_assign_geodetic"] = _raise_uninitialized_error
        self.__dict__["_assign_spherical"] = _raise_uninitialized_error
        self.__dict__["_assign_cylindrical"] = _raise_uninitialized_error
        self.__dict__["_assign_cartesian"] = _raise_uninitialized_error
        self.__dict__["_assign_planetocentric"] = _raise_uninitialized_error
        self.__dict__["_assign_planetodetic"] = _raise_uninitialized_error
        self.__dict__["_query_planetocentric"] = _raise_uninitialized_error
        self.__dict__["_query_planetodetic"] = _raise_uninitialized_error
        self.__dict__["_query_spherical"] = _raise_uninitialized_error
        self.__dict__["_query_cylindrical"] = _raise_uninitialized_error
        self.__dict__["_query_cartesian"] = _raise_uninitialized_error
        self.__dict__["_get_central_body_name"] = _raise_uninitialized_error
        self.__dict__["_query_planetocentric_array"] = _raise_uninitialized_error
        self.__dict__["_query_planetodetic_array"] = _raise_uninitialized_error
        self.__dict__["_query_spherical_array"] = _raise_uninitialized_error
        self.__dict__["_query_cylindrical_array"] = _raise_uninitialized_error
        self.__dict__["_query_cartesian_array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IPosition._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IPosition from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IPosition = agcom.GUID(IPosition._uuid)
        vtable_offset_local = IPosition._vtable_offset - 1
        self.__dict__["_convert_to"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get_position_type"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_assign"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_assign_geocentric"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+4, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_assign_geodetic"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+5, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_assign_spherical"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+6, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_assign_cylindrical"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+7, agcom.DOUBLE, agcom.DOUBLE, agcom.VARIANT)
        self.__dict__["_assign_cartesian"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+8, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_planetocentric"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+9, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_assign_planetodetic"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+10, agcom.VARIANT, agcom.VARIANT, agcom.DOUBLE)
        self.__dict__["_query_planetocentric"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+11, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_query_planetodetic"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+12, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_query_spherical"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+13, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_query_cylindrical"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+14, POINTER(agcom.DOUBLE), POINTER(agcom.VARIANT), POINTER(agcom.DOUBLE))
        self.__dict__["_query_cartesian"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+15, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_get_central_body_name"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+16, POINTER(agcom.BSTR))
        self.__dict__["_query_planetocentric_array"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+17, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_planetodetic_array"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+18, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_spherical_array"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+19, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_cylindrical_array"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+20, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_cartesian_array"] = IAGFUNCTYPE(pUnk, IID_IPosition, vtable_offset_local+21, POINTER(agcom.SAFEARRAY))
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
    
    def convert_to(self, type:"POSITION_TYPE") -> "IPosition":
        """Changes the position coordinates to type specified."""
        with agmarshall.AgEnum_arg(POSITION_TYPE, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgPosition:
            agcls.evaluate_hresult(self.__dict__["_convert_to"](arg_type.COM_val, byref(arg_ppIAgPosition.COM_val)))
            return arg_ppIAgPosition.python_val

    @property
    def position_type(self) -> "POSITION_TYPE":
        """Gets the type of position currently being used."""
        with agmarshall.AgEnum_arg(POSITION_TYPE) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_get_position_type"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def assign(self, pPosition:"IPosition") -> None:
        """This assigns the coordinates into the system."""
        with agmarshall.AgInterface_in_arg(pPosition, IPosition) as arg_pPosition:
            agcls.evaluate_hresult(self.__dict__["_assign"](arg_pPosition.COM_val))

    def assign_geocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Geocentric representation."""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_assign_geocentric"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def assign_geodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Geodetic representation."""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_assign_geodetic"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def assign_spherical(self, lat:typing.Any, lon:typing.Any, radius:float) -> None:
        """Helper method to assign the position using the Spherical representation"""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(radius) as arg_radius:
            agcls.evaluate_hresult(self.__dict__["_assign_spherical"](arg_lat.COM_val, arg_lon.COM_val, arg_radius.COM_val))

    def assign_cylindrical(self, radius:float, z:float, lon:typing.Any) -> None:
        """Helper method to assign the position using the Cylindrical representation"""
        with agmarshall.DOUBLE_arg(radius) as arg_radius, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.VARIANT_arg(lon) as arg_lon:
            agcls.evaluate_hresult(self.__dict__["_assign_cylindrical"](arg_radius.COM_val, arg_z.COM_val, arg_lon.COM_val))

    def assign_cartesian(self, x:float, y:float, z:float) -> None:
        """Helper method to assign the position using the Cartesian representation"""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_assign_cartesian"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def assign_planetocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Planetocentric representation"""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_assign_planetocentric"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def assign_planetodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Helper method to assign the position using the Planetodetic representation"""
        with agmarshall.VARIANT_arg(lat) as arg_lat, \
             agmarshall.VARIANT_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_assign_planetodetic"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val))

    def query_planetocentric(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Planetocentric representation"""
        with agmarshall.VARIANT_arg() as arg_lat, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_query_planetocentric"](byref(arg_lat.COM_val), byref(arg_lon.COM_val), byref(arg_alt.COM_val)))
            return arg_lat.python_val, arg_lon.python_val, arg_alt.python_val

    def query_planetodetic(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Planetodetic representation"""
        with agmarshall.VARIANT_arg() as arg_lat, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_alt:
            agcls.evaluate_hresult(self.__dict__["_query_planetodetic"](byref(arg_lat.COM_val), byref(arg_lon.COM_val), byref(arg_alt.COM_val)))
            return arg_lat.python_val, arg_lon.python_val, arg_alt.python_val

    def query_spherical(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Helper method to get the position using the Spherical representation"""
        with agmarshall.VARIANT_arg() as arg_lat, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_radius:
            agcls.evaluate_hresult(self.__dict__["_query_spherical"](byref(arg_lat.COM_val), byref(arg_lon.COM_val), byref(arg_radius.COM_val)))
            return arg_lat.python_val, arg_lon.python_val, arg_radius.python_val

    def query_cylindrical(self) -> typing.Tuple[float, typing.Any, float]:
        """Helper method to get the position using the Cylindrical representation"""
        with agmarshall.DOUBLE_arg() as arg_radius, \
             agmarshall.VARIANT_arg() as arg_lon, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_query_cylindrical"](byref(arg_radius.COM_val), byref(arg_lon.COM_val), byref(arg_z.COM_val)))
            return arg_radius.python_val, arg_lon.python_val, arg_z.python_val

    def query_cartesian(self) -> typing.Tuple[float, float, float]:
        """Helper method to get the position using the Cartesian representation"""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_query_cartesian"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    @property
    def central_body_name(self) -> str:
        """Gets the central body."""
        with agmarshall.BSTR_arg() as arg_pCBName:
            agcls.evaluate_hresult(self.__dict__["_get_central_body_name"](byref(arg_pCBName.COM_val)))
            return arg_pCBName.python_val

    def query_planetocentric_array(self) -> list:
        """Returns the Planetocentric elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_planetocentric_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_planetodetic_array(self) -> list:
        """Returns the Planetodetic elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_planetodetic_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_spherical_array(self) -> list:
        """Returns the Spherical elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_spherical_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_cylindrical_array(self) -> list:
        """Returns the Cylindrical elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_cylindrical_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_cartesian_array(self) -> list:
        """Returns the Cartesian elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_cartesian_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{F25960CE-1D73-4BA0-A429-541DD6D808DE}", IPosition)
agcls.AgTypeNameMap["IPosition"] = IPosition

class IPlanetocentric(IPosition):
    """Planetocentric Position Type."""
    _uuid = "{605061D3-5594-4B88-AC0A-D4EA90EFFAA1}"
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_lat"] = _raise_uninitialized_error
        self.__dict__["_set_lat"] = _raise_uninitialized_error
        self.__dict__["_get_lon"] = _raise_uninitialized_error
        self.__dict__["_set_lon"] = _raise_uninitialized_error
        self.__dict__["_get_altitude"] = _raise_uninitialized_error
        self.__dict__["_set_altitude"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IPlanetocentric._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IPlanetocentric from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPosition._private_init(self, pUnk)
        IID_IPlanetocentric = agcom.GUID(IPlanetocentric._uuid)
        vtable_offset_local = IPlanetocentric._vtable_offset - 1
        self.__dict__["_get_lat"] = IAGFUNCTYPE(pUnk, IID_IPlanetocentric, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_lat"] = IAGFUNCTYPE(pUnk, IID_IPlanetocentric, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_lon"] = IAGFUNCTYPE(pUnk, IID_IPlanetocentric, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_lon"] = IAGFUNCTYPE(pUnk, IID_IPlanetocentric, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_altitude"] = IAGFUNCTYPE(pUnk, IID_IPlanetocentric, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_altitude"] = IAGFUNCTYPE(pUnk, IID_IPlanetocentric, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @lat.setter
    def lat(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_lat"](arg_pVal.COM_val))

    @property
    def lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_lon"](arg_pVal.COM_val))

    @property
    def altitude(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_altitude"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @altitude.setter
    def altitude(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_altitude"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{605061D3-5594-4B88-AC0A-D4EA90EFFAA1}", IPlanetocentric)
agcls.AgTypeNameMap["IPlanetocentric"] = IPlanetocentric

class IGeocentric(IPosition):
    """Geocentric Position Type."""
    _uuid = "{7D22F2C8-81B1-452E-AA06-0AEEB1FDF0F9}"
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_lat"] = _raise_uninitialized_error
        self.__dict__["_set_lat"] = _raise_uninitialized_error
        self.__dict__["_get_lon"] = _raise_uninitialized_error
        self.__dict__["_set_lon"] = _raise_uninitialized_error
        self.__dict__["_get_altitude"] = _raise_uninitialized_error
        self.__dict__["_set_altitude"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IGeocentric._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IGeocentric from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPosition._private_init(self, pUnk)
        IID_IGeocentric = agcom.GUID(IGeocentric._uuid)
        vtable_offset_local = IGeocentric._vtable_offset - 1
        self.__dict__["_get_lat"] = IAGFUNCTYPE(pUnk, IID_IGeocentric, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_lat"] = IAGFUNCTYPE(pUnk, IID_IGeocentric, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_lon"] = IAGFUNCTYPE(pUnk, IID_IGeocentric, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_lon"] = IAGFUNCTYPE(pUnk, IID_IGeocentric, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_altitude"] = IAGFUNCTYPE(pUnk, IID_IGeocentric, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_altitude"] = IAGFUNCTYPE(pUnk, IID_IGeocentric, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @lat.setter
    def lat(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_lat"](arg_pVal.COM_val))

    @property
    def lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_lon"](arg_pVal.COM_val))

    @property
    def altitude(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_altitude"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @altitude.setter
    def altitude(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_altitude"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{7D22F2C8-81B1-452E-AA06-0AEEB1FDF0F9}", IGeocentric)
agcls.AgTypeNameMap["IGeocentric"] = IGeocentric

class ISpherical(IPosition):
    """Spherical Position Type."""
    _uuid = "{62B93DF1-C615-4363-B4D9-DAA1ACE56204}"
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_lat"] = _raise_uninitialized_error
        self.__dict__["_set_lat"] = _raise_uninitialized_error
        self.__dict__["_get_lon"] = _raise_uninitialized_error
        self.__dict__["_set_lon"] = _raise_uninitialized_error
        self.__dict__["_get_radius"] = _raise_uninitialized_error
        self.__dict__["_set_radius"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ISpherical._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ISpherical from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPosition._private_init(self, pUnk)
        IID_ISpherical = agcom.GUID(ISpherical._uuid)
        vtable_offset_local = ISpherical._vtable_offset - 1
        self.__dict__["_get_lat"] = IAGFUNCTYPE(pUnk, IID_ISpherical, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_lat"] = IAGFUNCTYPE(pUnk, IID_ISpherical, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_lon"] = IAGFUNCTYPE(pUnk, IID_ISpherical, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_lon"] = IAGFUNCTYPE(pUnk, IID_ISpherical, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_radius"] = IAGFUNCTYPE(pUnk, IID_ISpherical, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_radius"] = IAGFUNCTYPE(pUnk, IID_ISpherical, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def lat(self) -> typing.Any:
        """Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @lat.setter
    def lat(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_lat"](arg_pVal.COM_val))

    @property
    def lon(self) -> typing.Any:
        """Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_lon"](arg_pVal.COM_val))

    @property
    def radius(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_radius"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @radius.setter
    def radius(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_radius"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{62B93DF1-C615-4363-B4D9-DAA1ACE56204}", ISpherical)
agcls.AgTypeNameMap["ISpherical"] = ISpherical

class ICylindrical(IPosition):
    """Cylindrical Position Type."""
    _uuid = "{36F08499-F7C4-41DE-AB49-794EC65C5165}"
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_radius"] = _raise_uninitialized_error
        self.__dict__["_set_radius"] = _raise_uninitialized_error
        self.__dict__["_get_z"] = _raise_uninitialized_error
        self.__dict__["_set_z"] = _raise_uninitialized_error
        self.__dict__["_get_lon"] = _raise_uninitialized_error
        self.__dict__["_set_lon"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ICylindrical._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ICylindrical from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPosition._private_init(self, pUnk)
        IID_ICylindrical = agcom.GUID(ICylindrical._uuid)
        vtable_offset_local = ICylindrical._vtable_offset - 1
        self.__dict__["_get_radius"] = IAGFUNCTYPE(pUnk, IID_ICylindrical, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_set_radius"] = IAGFUNCTYPE(pUnk, IID_ICylindrical, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_get_z"] = IAGFUNCTYPE(pUnk, IID_ICylindrical, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_set_z"] = IAGFUNCTYPE(pUnk, IID_ICylindrical, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_get_lon"] = IAGFUNCTYPE(pUnk, IID_ICylindrical, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_set_lon"] = IAGFUNCTYPE(pUnk, IID_ICylindrical, vtable_offset_local+6, agcom.VARIANT)
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
    
    @property
    def radius(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_radius"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @radius.setter
    def radius(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_radius"](arg_pVal.COM_val))

    @property
    def z(self) -> float:
        """Uses Angle Dimension."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_z"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @z.setter
    def z(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_z"](arg_pVal.COM_val))

    @property
    def lon(self) -> typing.Any:
        """Dimension depends on context."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @lon.setter
    def lon(self, pVal:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_lon"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{36F08499-F7C4-41DE-AB49-794EC65C5165}", ICylindrical)
agcls.AgTypeNameMap["ICylindrical"] = ICylindrical

class ICartesian(IPosition):
    """ICartesian Interface used to access a position using Cartesian Coordinates"""
    _uuid = "{F6D3AD94-04C0-464E-8B95-8A859AA1BCA7}"
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_x"] = _raise_uninitialized_error
        self.__dict__["_set_x"] = _raise_uninitialized_error
        self.__dict__["_get_y"] = _raise_uninitialized_error
        self.__dict__["_set_y"] = _raise_uninitialized_error
        self.__dict__["_get_z"] = _raise_uninitialized_error
        self.__dict__["_set_z"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ICartesian._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ICartesian from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPosition._private_init(self, pUnk)
        IID_ICartesian = agcom.GUID(ICartesian._uuid)
        vtable_offset_local = ICartesian._vtable_offset - 1
        self.__dict__["_get_x"] = IAGFUNCTYPE(pUnk, IID_ICartesian, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_set_x"] = IAGFUNCTYPE(pUnk, IID_ICartesian, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_get_y"] = IAGFUNCTYPE(pUnk, IID_ICartesian, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_set_y"] = IAGFUNCTYPE(pUnk, IID_ICartesian, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_get_z"] = IAGFUNCTYPE(pUnk, IID_ICartesian, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_z"] = IAGFUNCTYPE(pUnk, IID_ICartesian, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def x(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_x"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @x.setter
    def x(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_x"](arg_pVal.COM_val))

    @property
    def y(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_y"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @y.setter
    def y(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_y"](arg_pVal.COM_val))

    @property
    def z(self) -> float:
        """Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_z"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @z.setter
    def z(self, pVal:float) -> None:
        with agmarshall.DOUBLE_arg(pVal) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_z"](arg_pVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{F6D3AD94-04C0-464E-8B95-8A859AA1BCA7}", ICartesian)
agcls.AgTypeNameMap["ICartesian"] = ICartesian

class IGeodetic(IPosition):
    """IGeodetic sets the position using Geodetic properties."""
    _uuid = "{93D3322B-C842-48D2-AFCF-BC42B59DB28E}"
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_lat"] = _raise_uninitialized_error
        self.__dict__["_set_lat"] = _raise_uninitialized_error
        self.__dict__["_get_lon"] = _raise_uninitialized_error
        self.__dict__["_set_lon"] = _raise_uninitialized_error
        self.__dict__["_get_altitude"] = _raise_uninitialized_error
        self.__dict__["_set_altitude"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IGeodetic._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IGeodetic from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPosition._private_init(self, pUnk)
        IID_IGeodetic = agcom.GUID(IGeodetic._uuid)
        vtable_offset_local = IGeodetic._vtable_offset - 1
        self.__dict__["_get_lat"] = IAGFUNCTYPE(pUnk, IID_IGeodetic, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_lat"] = IAGFUNCTYPE(pUnk, IID_IGeodetic, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_lon"] = IAGFUNCTYPE(pUnk, IID_IGeodetic, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_lon"] = IAGFUNCTYPE(pUnk, IID_IGeodetic, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_altitude"] = IAGFUNCTYPE(pUnk, IID_IGeodetic, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_altitude"] = IAGFUNCTYPE(pUnk, IID_IGeodetic, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def lat(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_get_lat"](byref(arg_pLat.COM_val)))
            return arg_pLat.python_val

    @lat.setter
    def lat(self, pLat:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLat) as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_set_lat"](arg_pLat.COM_val))

    @property
    def lon(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_get_lon"](byref(arg_pLon.COM_val)))
            return arg_pLon.python_val

    @lon.setter
    def lon(self, pLon:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLon) as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_set_lon"](arg_pLon.COM_val))

    @property
    def altitude(self) -> float:
        """Altitude. Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_get_altitude"](byref(arg_pAlt.COM_val)))
            return arg_pAlt.python_val

    @altitude.setter
    def altitude(self, pAlt:float) -> None:
        with agmarshall.DOUBLE_arg(pAlt) as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_set_altitude"](arg_pAlt.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{93D3322B-C842-48D2-AFCF-BC42B59DB28E}", IGeodetic)
agcls.AgTypeNameMap["IGeodetic"] = IGeodetic

class IPlanetodetic(IPosition):
    """IPlanetodetic sets the position using Planetodetic properties."""
    _uuid = "{E0F982B1-7B17-40F7-B64B-AFD0D112A74C}"
    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_lat"] = _raise_uninitialized_error
        self.__dict__["_set_lat"] = _raise_uninitialized_error
        self.__dict__["_get_lon"] = _raise_uninitialized_error
        self.__dict__["_set_lon"] = _raise_uninitialized_error
        self.__dict__["_get_altitude"] = _raise_uninitialized_error
        self.__dict__["_set_altitude"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IPlanetodetic._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IPlanetodetic from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPosition._private_init(self, pUnk)
        IID_IPlanetodetic = agcom.GUID(IPlanetodetic._uuid)
        vtable_offset_local = IPlanetodetic._vtable_offset - 1
        self.__dict__["_get_lat"] = IAGFUNCTYPE(pUnk, IID_IPlanetodetic, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_lat"] = IAGFUNCTYPE(pUnk, IID_IPlanetodetic, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_lon"] = IAGFUNCTYPE(pUnk, IID_IPlanetodetic, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_lon"] = IAGFUNCTYPE(pUnk, IID_IPlanetodetic, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_altitude"] = IAGFUNCTYPE(pUnk, IID_IPlanetodetic, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_altitude"] = IAGFUNCTYPE(pUnk, IID_IPlanetodetic, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def lat(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_get_lat"](byref(arg_pLat.COM_val)))
            return arg_pLat.python_val

    @lat.setter
    def lat(self, pLat:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLat) as arg_pLat:
            agcls.evaluate_hresult(self.__dict__["_set_lat"](arg_pLat.COM_val))

    @property
    def lon(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_get_lon"](byref(arg_pLon.COM_val)))
            return arg_pLon.python_val

    @lon.setter
    def lon(self, pLon:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pLon) as arg_pLon:
            agcls.evaluate_hresult(self.__dict__["_set_lon"](arg_pLon.COM_val))

    @property
    def altitude(self) -> float:
        """Altitude. Dimension depends on context."""
        with agmarshall.DOUBLE_arg() as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_get_altitude"](byref(arg_pAlt.COM_val)))
            return arg_pAlt.python_val

    @altitude.setter
    def altitude(self, pAlt:float) -> None:
        with agmarshall.DOUBLE_arg(pAlt) as arg_pAlt:
            agcls.evaluate_hresult(self.__dict__["_set_altitude"](arg_pAlt.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{E0F982B1-7B17-40F7-B64B-AFD0D112A74C}", IPlanetodetic)
agcls.AgTypeNameMap["IPlanetodetic"] = IPlanetodetic

class IDirection(object):
    """Interface to set and retrieve direction options for aligned and constrained vectors."""
    _uuid = "{8304507A-4915-453D-8944-2080659C0257}"
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_convert_to"] = _raise_uninitialized_error
        self.__dict__["_get_direction_type"] = _raise_uninitialized_error
        self.__dict__["_assign"] = _raise_uninitialized_error
        self.__dict__["_assign_euler"] = _raise_uninitialized_error
        self.__dict__["_assign_pr"] = _raise_uninitialized_error
        self.__dict__["_assign_ra_dec"] = _raise_uninitialized_error
        self.__dict__["_assign_xyz"] = _raise_uninitialized_error
        self.__dict__["_query_euler"] = _raise_uninitialized_error
        self.__dict__["_query_pr"] = _raise_uninitialized_error
        self.__dict__["_query_ra_dec"] = _raise_uninitialized_error
        self.__dict__["_query_xyz"] = _raise_uninitialized_error
        self.__dict__["_query_euler_array"] = _raise_uninitialized_error
        self.__dict__["_query_pr_array"] = _raise_uninitialized_error
        self.__dict__["_query_ra_dec_array"] = _raise_uninitialized_error
        self.__dict__["_query_xyz_array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDirection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDirection from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IDirection = agcom.GUID(IDirection._uuid)
        vtable_offset_local = IDirection._vtable_offset - 1
        self.__dict__["_convert_to"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get_direction_type"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_assign"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_assign_euler"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+4, agcom.VARIANT, agcom.VARIANT, agcom.LONG)
        self.__dict__["_assign_pr"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+5, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_assign_ra_dec"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+6, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_assign_xyz"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+7, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_query_euler"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+8, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_query_pr"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+9, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_query_ra_dec"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+10, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_query_xyz"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+11, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_query_euler_array"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+12, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_pr_array"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_ra_dec_array"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+14, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_xyz_array"] = IAGFUNCTYPE(pUnk, IID_IDirection, vtable_offset_local+15, POINTER(agcom.SAFEARRAY))
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
    
    def convert_to(self, type:"DIRECTION_TYPE") -> "IDirection":
        """Method to changes the direction to the type specified."""
        with agmarshall.AgEnum_arg(DIRECTION_TYPE, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgDirection:
            agcls.evaluate_hresult(self.__dict__["_convert_to"](arg_type.COM_val, byref(arg_ppIAgDirection.COM_val)))
            return arg_ppIAgDirection.python_val

    @property
    def direction_type(self) -> "DIRECTION_TYPE":
        """Returns the type of direction currently being used."""
        with agmarshall.AgEnum_arg(DIRECTION_TYPE) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_get_direction_type"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def assign(self, pDirection:"IDirection") -> None:
        """Assign a new direction."""
        with agmarshall.AgInterface_in_arg(pDirection, IDirection) as arg_pDirection:
            agcls.evaluate_hresult(self.__dict__["_assign"](arg_pDirection.COM_val))

    def assign_euler(self, b:typing.Any, c:typing.Any, sequence:"EULER_DIRECTION_SEQUENCE") -> None:
        """Helper method to set direction using the Euler representation. Params B and C use Angle Dimension."""
        with agmarshall.VARIANT_arg(b) as arg_b, \
             agmarshall.VARIANT_arg(c) as arg_c, \
             agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_assign_euler"](arg_b.COM_val, arg_c.COM_val, arg_sequence.COM_val))

    def assign_pr(self, pitch:typing.Any, roll:typing.Any) -> None:
        """Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        with agmarshall.VARIANT_arg(pitch) as arg_pitch, \
             agmarshall.VARIANT_arg(roll) as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_assign_pr"](arg_pitch.COM_val, arg_roll.COM_val))

    def assign_ra_dec(self, ra:typing.Any, dec:typing.Any) -> None:
        """Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        with agmarshall.VARIANT_arg(ra) as arg_ra, \
             agmarshall.VARIANT_arg(dec) as arg_dec:
            agcls.evaluate_hresult(self.__dict__["_assign_ra_dec"](arg_ra.COM_val, arg_dec.COM_val))

    def assign_xyz(self, x:float, y:float, z:float) -> None:
        """Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_assign_xyz"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def query_euler(self, sequence:"EULER_DIRECTION_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Euler representation. Params B and C use Angle Dimension."""
        with agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_b, \
             agmarshall.VARIANT_arg() as arg_c:
            agcls.evaluate_hresult(self.__dict__["_query_euler"](arg_sequence.COM_val, byref(arg_b.COM_val), byref(arg_c.COM_val)))
            return arg_b.python_val, arg_c.python_val

    def query_pr(self, sequence:"PR_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        with agmarshall.AgEnum_arg(PR_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_pitch, \
             agmarshall.VARIANT_arg() as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_query_pr"](arg_sequence.COM_val, byref(arg_pitch.COM_val), byref(arg_roll.COM_val)))
            return arg_pitch.python_val, arg_roll.python_val

    def query_ra_dec(self) -> typing.Tuple[typing.Any, typing.Any]:
        """Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        with agmarshall.VARIANT_arg() as arg_ra, \
             agmarshall.VARIANT_arg() as arg_dec:
            agcls.evaluate_hresult(self.__dict__["_query_ra_dec"](byref(arg_ra.COM_val), byref(arg_dec.COM_val)))
            return arg_ra.python_val, arg_dec.python_val

    def query_xyz(self) -> typing.Tuple[float, float, float]:
        """Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_query_xyz"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    def query_euler_array(self, sequence:"EULER_DIRECTION_SEQUENCE") -> list:
        """Returns the Euler elements in an array."""
        with agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_euler_array"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_pr_array(self, sequence:"PR_SEQUENCE") -> list:
        """Returns the PR elements in an array."""
        with agmarshall.AgEnum_arg(PR_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_pr_array"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_ra_dec_array(self) -> list:
        """Returns the RADec elements in an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_ra_dec_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_xyz_array(self) -> list:
        """Returns the XYZ elements in an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_xyz_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{8304507A-4915-453D-8944-2080659C0257}", IDirection)
agcls.AgTypeNameMap["IDirection"] = IDirection

class IDirectionEuler(IDirection):
    """Interface for Euler direction sequence."""
    _uuid = "{9CBDC138-72D1-4734-8F95-2140266D37B5}"
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_b"] = _raise_uninitialized_error
        self.__dict__["_set_b"] = _raise_uninitialized_error
        self.__dict__["_get_c"] = _raise_uninitialized_error
        self.__dict__["_set_c"] = _raise_uninitialized_error
        self.__dict__["_get_sequence"] = _raise_uninitialized_error
        self.__dict__["_set_sequence"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDirectionEuler._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDirectionEuler from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirection._private_init(self, pUnk)
        IID_IDirectionEuler = agcom.GUID(IDirectionEuler._uuid)
        vtable_offset_local = IDirectionEuler._vtable_offset - 1
        self.__dict__["_get_b"] = IAGFUNCTYPE(pUnk, IID_IDirectionEuler, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_b"] = IAGFUNCTYPE(pUnk, IID_IDirectionEuler, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_c"] = IAGFUNCTYPE(pUnk, IID_IDirectionEuler, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_c"] = IAGFUNCTYPE(pUnk, IID_IDirectionEuler, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_sequence"] = IAGFUNCTYPE(pUnk, IID_IDirectionEuler, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_set_sequence"] = IAGFUNCTYPE(pUnk, IID_IDirectionEuler, vtable_offset_local+6, agcom.LONG)
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
    
    @property
    def b(self) -> typing.Any:
        """Euler B angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_b"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @b.setter
    def b(self, va:typing.Any) -> None:
        with agmarshall.VARIANT_arg(va) as arg_va:
            agcls.evaluate_hresult(self.__dict__["_set_b"](arg_va.COM_val))

    @property
    def c(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_c"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @c.setter
    def c(self, vb:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vb) as arg_vb:
            agcls.evaluate_hresult(self.__dict__["_set_c"](arg_vb.COM_val))

    @property
    def sequence(self) -> "EULER_DIRECTION_SEQUENCE":
        """Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_sequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @sequence.setter
    def sequence(self, sequence:"EULER_DIRECTION_SEQUENCE") -> None:
        with agmarshall.AgEnum_arg(EULER_DIRECTION_SEQUENCE, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_set_sequence"](arg_sequence.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{9CBDC138-72D1-4734-8F95-2140266D37B5}", IDirectionEuler)
agcls.AgTypeNameMap["IDirectionEuler"] = IDirectionEuler

class IDirectionPR(IDirection):
    """Interface for Pitch-Roll (PR) direction sequence."""
    _uuid = "{5AC01BF1-2B95-4C13-8B69-09FDC485330E}"
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_pitch"] = _raise_uninitialized_error
        self.__dict__["_set_pitch"] = _raise_uninitialized_error
        self.__dict__["_get_roll"] = _raise_uninitialized_error
        self.__dict__["_set_roll"] = _raise_uninitialized_error
        self.__dict__["_get_sequence"] = _raise_uninitialized_error
        self.__dict__["_set_sequence"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDirectionPR._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDirectionPR from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirection._private_init(self, pUnk)
        IID_IDirectionPR = agcom.GUID(IDirectionPR._uuid)
        vtable_offset_local = IDirectionPR._vtable_offset - 1
        self.__dict__["_get_pitch"] = IAGFUNCTYPE(pUnk, IID_IDirectionPR, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_pitch"] = IAGFUNCTYPE(pUnk, IID_IDirectionPR, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_roll"] = IAGFUNCTYPE(pUnk, IID_IDirectionPR, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_roll"] = IAGFUNCTYPE(pUnk, IID_IDirectionPR, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_sequence"] = IAGFUNCTYPE(pUnk, IID_IDirectionPR, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_set_sequence"] = IAGFUNCTYPE(pUnk, IID_IDirectionPR, vtable_offset_local+6, agcom.LONG)
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
    
    @property
    def pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_pitch"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @pitch.setter
    def pitch(self, vPitch:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vPitch) as arg_vPitch:
            agcls.evaluate_hresult(self.__dict__["_set_pitch"](arg_vPitch.COM_val))

    @property
    def roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_roll"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @roll.setter
    def roll(self, vRoll:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vRoll) as arg_vRoll:
            agcls.evaluate_hresult(self.__dict__["_set_roll"](arg_vRoll.COM_val))

    @property
    def sequence(self) -> "PR_SEQUENCE":
        """PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(PR_SEQUENCE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_sequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @sequence.setter
    def sequence(self, sequence:"PR_SEQUENCE") -> None:
        with agmarshall.AgEnum_arg(PR_SEQUENCE, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_set_sequence"](arg_sequence.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{5AC01BF1-2B95-4C13-8B69-09FDC485330E}", IDirectionPR)
agcls.AgTypeNameMap["IDirectionPR"] = IDirectionPR

class IDirectionRADec(IDirection):
    """Interface for Spherical direction (Right Ascension and Declination)."""
    _uuid = "{A921E587-EC8A-4F1E-99BB-6E13B8E0D5E7}"
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_dec"] = _raise_uninitialized_error
        self.__dict__["_set_dec"] = _raise_uninitialized_error
        self.__dict__["_get_ra"] = _raise_uninitialized_error
        self.__dict__["_set_ra"] = _raise_uninitialized_error
        self.__dict__["_get_magnitude"] = _raise_uninitialized_error
        self.__dict__["_set_magnitude"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDirectionRADec._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDirectionRADec from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirection._private_init(self, pUnk)
        IID_IDirectionRADec = agcom.GUID(IDirectionRADec._uuid)
        vtable_offset_local = IDirectionRADec._vtable_offset - 1
        self.__dict__["_get_dec"] = IAGFUNCTYPE(pUnk, IID_IDirectionRADec, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_dec"] = IAGFUNCTYPE(pUnk, IID_IDirectionRADec, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_ra"] = IAGFUNCTYPE(pUnk, IID_IDirectionRADec, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_ra"] = IAGFUNCTYPE(pUnk, IID_IDirectionRADec, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_magnitude"] = IAGFUNCTYPE(pUnk, IID_IDirectionRADec, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_magnitude"] = IAGFUNCTYPE(pUnk, IID_IDirectionRADec, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def dec(self) -> typing.Any:
        """Declination: angle above the x-y plane. Uses Latitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_dec"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @dec.setter
    def dec(self, vLat:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vLat) as arg_vLat:
            agcls.evaluate_hresult(self.__dict__["_set_dec"](arg_vLat.COM_val))

    @property
    def ra(self) -> typing.Any:
        """Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_ra"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @ra.setter
    def ra(self, vLon:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vLon) as arg_vLon:
            agcls.evaluate_hresult(self.__dict__["_set_ra"](arg_vLon.COM_val))

    @property
    def magnitude(self) -> float:
        """A unitless value that represents magnitude."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_magnitude"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @magnitude.setter
    def magnitude(self, magnitude:float) -> None:
        with agmarshall.DOUBLE_arg(magnitude) as arg_magnitude:
            agcls.evaluate_hresult(self.__dict__["_set_magnitude"](arg_magnitude.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{A921E587-EC8A-4F1E-99BB-6E13B8E0D5E7}", IDirectionRADec)
agcls.AgTypeNameMap["IDirectionRADec"] = IDirectionRADec

class IDirectionXYZ(IDirection):
    """Interface for Cartesian direction."""
    _uuid = "{2B499A22-6662-4F20-8B82-AA7701CD87A4}"
    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_x"] = _raise_uninitialized_error
        self.__dict__["_set_x"] = _raise_uninitialized_error
        self.__dict__["_get_y"] = _raise_uninitialized_error
        self.__dict__["_set_y"] = _raise_uninitialized_error
        self.__dict__["_get_z"] = _raise_uninitialized_error
        self.__dict__["_set_z"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDirectionXYZ._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDirectionXYZ from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirection._private_init(self, pUnk)
        IID_IDirectionXYZ = agcom.GUID(IDirectionXYZ._uuid)
        vtable_offset_local = IDirectionXYZ._vtable_offset - 1
        self.__dict__["_get_x"] = IAGFUNCTYPE(pUnk, IID_IDirectionXYZ, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_set_x"] = IAGFUNCTYPE(pUnk, IID_IDirectionXYZ, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_get_y"] = IAGFUNCTYPE(pUnk, IID_IDirectionXYZ, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_set_y"] = IAGFUNCTYPE(pUnk, IID_IDirectionXYZ, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_get_z"] = IAGFUNCTYPE(pUnk, IID_IDirectionXYZ, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_z"] = IAGFUNCTYPE(pUnk, IID_IDirectionXYZ, vtable_offset_local+6, agcom.DOUBLE)
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
    
    @property
    def x(self) -> float:
        """X component. Dimensionless"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_x"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @x.setter
    def x(self, vx:float) -> None:
        with agmarshall.DOUBLE_arg(vx) as arg_vx:
            agcls.evaluate_hresult(self.__dict__["_set_x"](arg_vx.COM_val))

    @property
    def y(self) -> float:
        """Y component. Dimensionless"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_y"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @y.setter
    def y(self, vy:float) -> None:
        with agmarshall.DOUBLE_arg(vy) as arg_vy:
            agcls.evaluate_hresult(self.__dict__["_set_y"](arg_vy.COM_val))

    @property
    def z(self) -> float:
        """Z component. Dimensionless"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_z"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @z.setter
    def z(self, vz:float) -> None:
        with agmarshall.DOUBLE_arg(vz) as arg_vz:
            agcls.evaluate_hresult(self.__dict__["_set_z"](arg_vz.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{2B499A22-6662-4F20-8B82-AA7701CD87A4}", IDirectionXYZ)
agcls.AgTypeNameMap["IDirectionXYZ"] = IDirectionXYZ

class ICartesian3Vector(object):
    """Represents a cartesian 3-D vector."""
    _uuid = "{7B741836-71F9-4115-97F8-EAB30362E5C7}"
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_x"] = _raise_uninitialized_error
        self.__dict__["_set_x"] = _raise_uninitialized_error
        self.__dict__["_get_y"] = _raise_uninitialized_error
        self.__dict__["_set_y"] = _raise_uninitialized_error
        self.__dict__["_get_z"] = _raise_uninitialized_error
        self.__dict__["_set_z"] = _raise_uninitialized_error
        self.__dict__["_get"] = _raise_uninitialized_error
        self.__dict__["_set"] = _raise_uninitialized_error
        self.__dict__["_to_array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ICartesian3Vector._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ICartesian3Vector from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_ICartesian3Vector = agcom.GUID(ICartesian3Vector._uuid)
        vtable_offset_local = ICartesian3Vector._vtable_offset - 1
        self.__dict__["_get_x"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_set_x"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_get_y"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_set_y"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_get_z"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_z"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__["_get"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+7, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_set"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+8, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_to_array"] = IAGFUNCTYPE(pUnk, IID_ICartesian3Vector, vtable_offset_local+9, POINTER(agcom.SAFEARRAY))
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
    
    @property
    def x(self) -> float:
        """X coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_x"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @x.setter
    def x(self, x:float) -> None:
        with agmarshall.DOUBLE_arg(x) as arg_x:
            agcls.evaluate_hresult(self.__dict__["_set_x"](arg_x.COM_val))

    @property
    def y(self) -> float:
        """Y coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_y"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @y.setter
    def y(self, y:float) -> None:
        with agmarshall.DOUBLE_arg(y) as arg_y:
            agcls.evaluate_hresult(self.__dict__["_set_y"](arg_y.COM_val))

    @property
    def z(self) -> float:
        """Z coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_z"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @z.setter
    def z(self, z:float) -> None:
        with agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_set_z"](arg_z.COM_val))

    def get(self) -> typing.Tuple[float, float, float]:
        """Returns cartesian vector"""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y, \
             agmarshall.DOUBLE_arg() as arg_z:
            agcls.evaluate_hresult(self.__dict__["_get"](byref(arg_x.COM_val), byref(arg_y.COM_val), byref(arg_z.COM_val)))
            return arg_x.python_val, arg_y.python_val, arg_z.python_val

    def set(self, x:float, y:float, z:float) -> None:
        """Sets cartesian vector"""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z:
            agcls.evaluate_hresult(self.__dict__["_set"](arg_x.COM_val, arg_y.COM_val, arg_z.COM_val))

    def to_array(self) -> list:
        """Returns coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_to_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{7B741836-71F9-4115-97F8-EAB30362E5C7}", ICartesian3Vector)
agcls.AgTypeNameMap["ICartesian3Vector"] = ICartesian3Vector

class IOrientation(object):
    """Interface to set and retrieve the orientation method."""
    _uuid = "{8467175F-1BD8-4498-90FD-08C67072D120}"
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_convert_to"] = _raise_uninitialized_error
        self.__dict__["_get_orientation_type"] = _raise_uninitialized_error
        self.__dict__["_assign"] = _raise_uninitialized_error
        self.__dict__["_assign_az_el"] = _raise_uninitialized_error
        self.__dict__["_assign_euler_angles"] = _raise_uninitialized_error
        self.__dict__["_assign_quaternion"] = _raise_uninitialized_error
        self.__dict__["_assign_ypr_angles"] = _raise_uninitialized_error
        self.__dict__["_query_az_el"] = _raise_uninitialized_error
        self.__dict__["_query_euler_angles"] = _raise_uninitialized_error
        self.__dict__["_query_quaternion"] = _raise_uninitialized_error
        self.__dict__["_query_ypr_angles"] = _raise_uninitialized_error
        self.__dict__["_query_az_el_array"] = _raise_uninitialized_error
        self.__dict__["_query_euler_angles_array"] = _raise_uninitialized_error
        self.__dict__["_query_quaternion_array"] = _raise_uninitialized_error
        self.__dict__["_query_ypr_angles_array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IOrientation._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IOrientation from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IOrientation = agcom.GUID(IOrientation._uuid)
        vtable_offset_local = IOrientation._vtable_offset - 1
        self.__dict__["_convert_to"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get_orientation_type"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_assign"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_assign_az_el"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+4, agcom.VARIANT, agcom.VARIANT, agcom.LONG)
        self.__dict__["_assign_euler_angles"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+5, agcom.LONG, agcom.VARIANT, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_assign_quaternion"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+6, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_ypr_angles"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+7, agcom.LONG, agcom.VARIANT, agcom.VARIANT, agcom.VARIANT)
        self.__dict__["_query_az_el"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+8, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.LONG))
        self.__dict__["_query_euler_angles"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+9, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_query_quaternion"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+10, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_query_ypr_angles"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+11, agcom.LONG, POINTER(agcom.VARIANT), POINTER(agcom.VARIANT), POINTER(agcom.VARIANT))
        self.__dict__["_query_az_el_array"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+12, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_euler_angles_array"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+13, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_quaternion_array"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+14, POINTER(agcom.SAFEARRAY))
        self.__dict__["_query_ypr_angles_array"] = IAGFUNCTYPE(pUnk, IID_IOrientation, vtable_offset_local+15, agcom.LONG, POINTER(agcom.SAFEARRAY))
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
    
    def convert_to(self, type:"ORIENTATION_TYPE") -> "IOrientation":
        """Method to change the orientation method to the type specified."""
        with agmarshall.AgEnum_arg(ORIENTATION_TYPE, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgOrientation:
            agcls.evaluate_hresult(self.__dict__["_convert_to"](arg_type.COM_val, byref(arg_ppIAgOrientation.COM_val)))
            return arg_ppIAgOrientation.python_val

    @property
    def orientation_type(self) -> "ORIENTATION_TYPE":
        """Returns the orientation method currently being used."""
        with agmarshall.AgEnum_arg(ORIENTATION_TYPE) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_get_orientation_type"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def assign(self, pOrientation:"IOrientation") -> None:
        """Assign a new orientation method."""
        with agmarshall.AgInterface_in_arg(pOrientation, IOrientation) as arg_pOrientation:
            agcls.evaluate_hresult(self.__dict__["_assign"](arg_pOrientation.COM_val))

    def assign_az_el(self, azimuth:typing.Any, elevation:typing.Any, aboutBoresight:"AZ_EL_ABOUT_BORESIGHT") -> None:
        """Helper method to set orientation using the AzEl representation."""
        with agmarshall.VARIANT_arg(azimuth) as arg_azimuth, \
             agmarshall.VARIANT_arg(elevation) as arg_elevation, \
             agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT, aboutBoresight) as arg_aboutBoresight:
            agcls.evaluate_hresult(self.__dict__["_assign_az_el"](arg_azimuth.COM_val, arg_elevation.COM_val, arg_aboutBoresight.COM_val))

    def assign_euler_angles(self, sequence:"EULER_ORIENTATION_SEQUENCE", a:typing.Any, b:typing.Any, c:typing.Any) -> None:
        """Helper method to set orientation using the Euler angles representation."""
        with agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg(a) as arg_a, \
             agmarshall.VARIANT_arg(b) as arg_b, \
             agmarshall.VARIANT_arg(c) as arg_c:
            agcls.evaluate_hresult(self.__dict__["_assign_euler_angles"](arg_sequence.COM_val, arg_a.COM_val, arg_b.COM_val, arg_c.COM_val))

    def assign_quaternion(self, qx:float, qy:float, qz:float, qs:float) -> None:
        """Helper method to set orientation using the Quaternion representation."""
        with agmarshall.DOUBLE_arg(qx) as arg_qx, \
             agmarshall.DOUBLE_arg(qy) as arg_qy, \
             agmarshall.DOUBLE_arg(qz) as arg_qz, \
             agmarshall.DOUBLE_arg(qs) as arg_qs:
            agcls.evaluate_hresult(self.__dict__["_assign_quaternion"](arg_qx.COM_val, arg_qy.COM_val, arg_qz.COM_val, arg_qs.COM_val))

    def assign_ypr_angles(self, sequence:"YPR_ANGLES_SEQUENCE", yaw:typing.Any, pitch:typing.Any, roll:typing.Any) -> None:
        """Helper method to set orientation using the YPR angles representation."""
        with agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg(yaw) as arg_yaw, \
             agmarshall.VARIANT_arg(pitch) as arg_pitch, \
             agmarshall.VARIANT_arg(roll) as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_assign_ypr_angles"](arg_sequence.COM_val, arg_yaw.COM_val, arg_pitch.COM_val, arg_roll.COM_val))

    def query_az_el(self) -> typing.Tuple[typing.Any, typing.Any, AZ_EL_ABOUT_BORESIGHT]:
        """Helper method to get orientation using the AzEl representation."""
        with agmarshall.VARIANT_arg() as arg_azimuth, \
             agmarshall.VARIANT_arg() as arg_elevation, \
             agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT) as arg_aboutBoresight:
            agcls.evaluate_hresult(self.__dict__["_query_az_el"](byref(arg_azimuth.COM_val), byref(arg_elevation.COM_val), byref(arg_aboutBoresight.COM_val)))
            return arg_azimuth.python_val, arg_elevation.python_val, arg_aboutBoresight.python_val

    def query_euler_angles(self, sequence:"EULER_ORIENTATION_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Helper method to get orientation using the Euler angles representation."""
        with agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_a, \
             agmarshall.VARIANT_arg() as arg_b, \
             agmarshall.VARIANT_arg() as arg_c:
            agcls.evaluate_hresult(self.__dict__["_query_euler_angles"](arg_sequence.COM_val, byref(arg_a.COM_val), byref(arg_b.COM_val), byref(arg_c.COM_val)))
            return arg_a.python_val, arg_b.python_val, arg_c.python_val

    def query_quaternion(self) -> typing.Tuple[float, float, float, float]:
        """Helper method to get orientation using the Quaternion representation."""
        with agmarshall.DOUBLE_arg() as arg_qx, \
             agmarshall.DOUBLE_arg() as arg_qy, \
             agmarshall.DOUBLE_arg() as arg_qz, \
             agmarshall.DOUBLE_arg() as arg_qs:
            agcls.evaluate_hresult(self.__dict__["_query_quaternion"](byref(arg_qx.COM_val), byref(arg_qy.COM_val), byref(arg_qz.COM_val), byref(arg_qs.COM_val)))
            return arg_qx.python_val, arg_qy.python_val, arg_qz.python_val, arg_qs.python_val

    def query_ypr_angles(self, sequence:"YPR_ANGLES_SEQUENCE") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Helper method to get orientation using the YPR angles representation."""
        with agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.VARIANT_arg() as arg_yaw, \
             agmarshall.VARIANT_arg() as arg_pitch, \
             agmarshall.VARIANT_arg() as arg_roll:
            agcls.evaluate_hresult(self.__dict__["_query_ypr_angles"](arg_sequence.COM_val, byref(arg_yaw.COM_val), byref(arg_pitch.COM_val), byref(arg_roll.COM_val)))
            return arg_yaw.python_val, arg_pitch.python_val, arg_roll.python_val

    def query_az_el_array(self) -> list:
        """Returns the AzEl elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_az_el_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_euler_angles_array(self, sequence:"EULER_ORIENTATION_SEQUENCE") -> list:
        """Returns the Euler elements as an array."""
        with agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_euler_angles_array"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_quaternion_array(self) -> list:
        """Returns the Quaternion elements as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_quaternion_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_ypr_angles_array(self, sequence:"YPR_ANGLES_SEQUENCE") -> list:
        """Returns the YPR Angles elements as an array."""
        with agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE, sequence) as arg_sequence, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_ypr_angles_array"](arg_sequence.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{8467175F-1BD8-4498-90FD-08C67072D120}", IOrientation)
agcls.AgTypeNameMap["IOrientation"] = IOrientation

class IOrientationAzEl(IOrientation):
    """Interface for AzEl orientation method."""
    _uuid = "{6A6B1D7D-6A7F-48B3-98CA-019CA46499FE}"
    _num_methods = 6
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_azimuth"] = _raise_uninitialized_error
        self.__dict__["_set_azimuth"] = _raise_uninitialized_error
        self.__dict__["_get_elevation"] = _raise_uninitialized_error
        self.__dict__["_set_elevation"] = _raise_uninitialized_error
        self.__dict__["_get_about_boresight"] = _raise_uninitialized_error
        self.__dict__["_set_about_boresight"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IOrientationAzEl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IOrientationAzEl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientation._private_init(self, pUnk)
        IID_IOrientationAzEl = agcom.GUID(IOrientationAzEl._uuid)
        vtable_offset_local = IOrientationAzEl._vtable_offset - 1
        self.__dict__["_get_azimuth"] = IAGFUNCTYPE(pUnk, IID_IOrientationAzEl, vtable_offset_local+1, POINTER(agcom.VARIANT))
        self.__dict__["_set_azimuth"] = IAGFUNCTYPE(pUnk, IID_IOrientationAzEl, vtable_offset_local+2, agcom.VARIANT)
        self.__dict__["_get_elevation"] = IAGFUNCTYPE(pUnk, IID_IOrientationAzEl, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_elevation"] = IAGFUNCTYPE(pUnk, IID_IOrientationAzEl, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_about_boresight"] = IAGFUNCTYPE(pUnk, IID_IOrientationAzEl, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_set_about_boresight"] = IAGFUNCTYPE(pUnk, IID_IOrientationAzEl, vtable_offset_local+6, agcom.LONG)
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
    
    @property
    def azimuth(self) -> typing.Any:
        """Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_azimuth"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @azimuth.setter
    def azimuth(self, vAzimuth:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vAzimuth) as arg_vAzimuth:
            agcls.evaluate_hresult(self.__dict__["_set_azimuth"](arg_vAzimuth.COM_val))

    @property
    def elevation(self) -> typing.Any:
        """Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_elevation"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @elevation.setter
    def elevation(self, vElevation:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vElevation) as arg_vElevation:
            agcls.evaluate_hresult(self.__dict__["_set_elevation"](arg_vElevation.COM_val))

    @property
    def about_boresight(self) -> "AZ_EL_ABOUT_BORESIGHT":
        """Determines orientation of the X and Y axes with respect to the parent's reference frame."""
        with agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_about_boresight"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @about_boresight.setter
    def about_boresight(self, aboutBoresight:"AZ_EL_ABOUT_BORESIGHT") -> None:
        with agmarshall.AgEnum_arg(AZ_EL_ABOUT_BORESIGHT, aboutBoresight) as arg_aboutBoresight:
            agcls.evaluate_hresult(self.__dict__["_set_about_boresight"](arg_aboutBoresight.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{6A6B1D7D-6A7F-48B3-98CA-019CA46499FE}", IOrientationAzEl)
agcls.AgTypeNameMap["IOrientationAzEl"] = IOrientationAzEl

class IOrientationEulerAngles(IOrientation):
    """Interface for Euler Angles orientation method."""
    _uuid = "{4204C7E1-EC21-40AD-A905-BB35A3FDF7BD}"
    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_sequence"] = _raise_uninitialized_error
        self.__dict__["_set_sequence"] = _raise_uninitialized_error
        self.__dict__["_get_a"] = _raise_uninitialized_error
        self.__dict__["_set_a"] = _raise_uninitialized_error
        self.__dict__["_get_b"] = _raise_uninitialized_error
        self.__dict__["_set_b"] = _raise_uninitialized_error
        self.__dict__["_get_c"] = _raise_uninitialized_error
        self.__dict__["_set_c"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IOrientationEulerAngles._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IOrientationEulerAngles from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientation._private_init(self, pUnk)
        IID_IOrientationEulerAngles = agcom.GUID(IOrientationEulerAngles._uuid)
        vtable_offset_local = IOrientationEulerAngles._vtable_offset - 1
        self.__dict__["_get_sequence"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_set_sequence"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+2, agcom.LONG)
        self.__dict__["_get_a"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_a"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_b"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_set_b"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+6, agcom.VARIANT)
        self.__dict__["_get_c"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+7, POINTER(agcom.VARIANT))
        self.__dict__["_set_c"] = IAGFUNCTYPE(pUnk, IID_IOrientationEulerAngles, vtable_offset_local+8, agcom.VARIANT)
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
    
    @property
    def sequence(self) -> "EULER_ORIENTATION_SEQUENCE":
        """Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_sequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @sequence.setter
    def sequence(self, ppVal:"EULER_ORIENTATION_SEQUENCE") -> None:
        with agmarshall.AgEnum_arg(EULER_ORIENTATION_SEQUENCE, ppVal) as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_set_sequence"](arg_ppVal.COM_val))

    @property
    def a(self) -> typing.Any:
        """Euler A angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_a"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @a.setter
    def a(self, va:typing.Any) -> None:
        with agmarshall.VARIANT_arg(va) as arg_va:
            agcls.evaluate_hresult(self.__dict__["_set_a"](arg_va.COM_val))

    @property
    def b(self) -> typing.Any:
        """Euler b angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_b"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @b.setter
    def b(self, vb:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vb) as arg_vb:
            agcls.evaluate_hresult(self.__dict__["_set_b"](arg_vb.COM_val))

    @property
    def c(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_c"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @c.setter
    def c(self, vc:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vc) as arg_vc:
            agcls.evaluate_hresult(self.__dict__["_set_c"](arg_vc.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{4204C7E1-EC21-40AD-A905-BB35A3FDF7BD}", IOrientationEulerAngles)
agcls.AgTypeNameMap["IOrientationEulerAngles"] = IOrientationEulerAngles

class IOrientationQuaternion(IOrientation):
    """Interface for Quaternion orientation method."""
    _uuid = "{101FAC5C-8DDB-4D4F-9C73-58146CA8EB01}"
    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_qx"] = _raise_uninitialized_error
        self.__dict__["_set_qx"] = _raise_uninitialized_error
        self.__dict__["_get_qy"] = _raise_uninitialized_error
        self.__dict__["_set_qy"] = _raise_uninitialized_error
        self.__dict__["_get_qz"] = _raise_uninitialized_error
        self.__dict__["_set_qz"] = _raise_uninitialized_error
        self.__dict__["_get_qs"] = _raise_uninitialized_error
        self.__dict__["_set_qs"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IOrientationQuaternion._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IOrientationQuaternion from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientation._private_init(self, pUnk)
        IID_IOrientationQuaternion = agcom.GUID(IOrientationQuaternion._uuid)
        vtable_offset_local = IOrientationQuaternion._vtable_offset - 1
        self.__dict__["_get_qx"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_set_qx"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_get_qy"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_set_qy"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_get_qz"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_set_qz"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__["_get_qs"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_set_qs"] = IAGFUNCTYPE(pUnk, IID_IOrientationQuaternion, vtable_offset_local+8, agcom.DOUBLE)
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
    
    @property
    def qx(self) -> float:
        """The first element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QX = nx si..."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_qx"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @qx.setter
    def qx(self, vQX:float) -> None:
        with agmarshall.DOUBLE_arg(vQX) as arg_vQX:
            agcls.evaluate_hresult(self.__dict__["_set_qx"](arg_vQX.COM_val))

    @property
    def qy(self) -> float:
        """The second element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QY = ny s..."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_qy"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @qy.setter
    def qy(self, vQY:float) -> None:
        with agmarshall.DOUBLE_arg(vQY) as arg_vQY:
            agcls.evaluate_hresult(self.__dict__["_set_qy"](arg_vQY.COM_val))

    @property
    def qz(self) -> float:
        """The third element of the vector component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QZ = nz si..."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_qz"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @qz.setter
    def qz(self, vQZ:float) -> None:
        with agmarshall.DOUBLE_arg(vQZ) as arg_vQZ:
            agcls.evaluate_hresult(self.__dict__["_set_qz"](arg_vQZ.COM_val))

    @property
    def qs(self) -> float:
        """The scalar component of the quaternion representing orientation between two sets of axes. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QS = cos(A/2). Dimensionless."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_qs"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @qs.setter
    def qs(self, vQS:float) -> None:
        with agmarshall.DOUBLE_arg(vQS) as arg_vQS:
            agcls.evaluate_hresult(self.__dict__["_set_qs"](arg_vQS.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{101FAC5C-8DDB-4D4F-9C73-58146CA8EB01}", IOrientationQuaternion)
agcls.AgTypeNameMap["IOrientationQuaternion"] = IOrientationQuaternion

class IOrientationYPRAngles(IOrientation):
    """Interface for Yaw-Pitch Roll (YPR) Angles orientation system."""
    _uuid = "{97A9D45D-E718-41FC-ACD2-CEBBEFD2011B}"
    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_sequence"] = _raise_uninitialized_error
        self.__dict__["_set_sequence"] = _raise_uninitialized_error
        self.__dict__["_get_yaw"] = _raise_uninitialized_error
        self.__dict__["_set_yaw"] = _raise_uninitialized_error
        self.__dict__["_get_pitch"] = _raise_uninitialized_error
        self.__dict__["_set_pitch"] = _raise_uninitialized_error
        self.__dict__["_get_roll"] = _raise_uninitialized_error
        self.__dict__["_set_roll"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IOrientationYPRAngles._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IOrientationYPRAngles from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientation._private_init(self, pUnk)
        IID_IOrientationYPRAngles = agcom.GUID(IOrientationYPRAngles._uuid)
        vtable_offset_local = IOrientationYPRAngles._vtable_offset - 1
        self.__dict__["_get_sequence"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_set_sequence"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+2, agcom.LONG)
        self.__dict__["_get_yaw"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_yaw"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_pitch"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_set_pitch"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+6, agcom.VARIANT)
        self.__dict__["_get_roll"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+7, POINTER(agcom.VARIANT))
        self.__dict__["_set_roll"] = IAGFUNCTYPE(pUnk, IID_IOrientationYPRAngles, vtable_offset_local+8, agcom.VARIANT)
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
    
    @property
    def sequence(self) -> "YPR_ANGLES_SEQUENCE":
        """YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified."""
        with agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_sequence"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @sequence.setter
    def sequence(self, sequence:"YPR_ANGLES_SEQUENCE") -> None:
        with agmarshall.AgEnum_arg(YPR_ANGLES_SEQUENCE, sequence) as arg_sequence:
            agcls.evaluate_hresult(self.__dict__["_set_sequence"](arg_sequence.COM_val))

    @property
    def yaw(self) -> typing.Any:
        """Yaw angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_yaw"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @yaw.setter
    def yaw(self, vYaw:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vYaw) as arg_vYaw:
            agcls.evaluate_hresult(self.__dict__["_set_yaw"](arg_vYaw.COM_val))

    @property
    def pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_pitch"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @pitch.setter
    def pitch(self, vPitch:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vPitch) as arg_vPitch:
            agcls.evaluate_hresult(self.__dict__["_set_pitch"](arg_vPitch.COM_val))

    @property
    def roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_roll"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @roll.setter
    def roll(self, vRoll:typing.Any) -> None:
        with agmarshall.VARIANT_arg(vRoll) as arg_vRoll:
            agcls.evaluate_hresult(self.__dict__["_set_roll"](arg_vRoll.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{97A9D45D-E718-41FC-ACD2-CEBBEFD2011B}", IOrientationYPRAngles)
agcls.AgTypeNameMap["IOrientationYPRAngles"] = IOrientationYPRAngles

class IOrientationPositionOffset(object):
    """Interface for defining the orientation origin position offset relative to the parent object."""
    _uuid = "{0DDA686C-559C-4BEA-969B-BF40708242B6}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_position_offset"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IOrientationPositionOffset._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IOrientationPositionOffset from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IOrientationPositionOffset = agcom.GUID(IOrientationPositionOffset._uuid)
        vtable_offset_local = IOrientationPositionOffset._vtable_offset - 1
        self.__dict__["_get_position_offset"] = IAGFUNCTYPE(pUnk, IID_IOrientationPositionOffset, vtable_offset_local+1, POINTER(agcom.PVOID))
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
    
    @property
    def position_offset(self) -> "ICartesian3Vector":
        """Gets or sets the position offset cartesian vector."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_position_offset"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{0DDA686C-559C-4BEA-969B-BF40708242B6}", IOrientationPositionOffset)
agcls.AgTypeNameMap["IOrientationPositionOffset"] = IOrientationPositionOffset

class IOrbitState(object):
    """Interface to set and retrieve the coordinate type used to specify the orbit state."""
    _uuid = "{42342AD2-F6C5-426B-AB2A-3688F05353C8}"
    _num_methods = 13
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_convert_to"] = _raise_uninitialized_error
        self.__dict__["_get_orbit_state_type"] = _raise_uninitialized_error
        self.__dict__["_assign"] = _raise_uninitialized_error
        self.__dict__["_assign_classical"] = _raise_uninitialized_error
        self.__dict__["_assign_cartesian"] = _raise_uninitialized_error
        self.__dict__["_assign_geodetic"] = _raise_uninitialized_error
        self.__dict__["_assign_equinoctial_posigrade"] = _raise_uninitialized_error
        self.__dict__["_assign_equinoctial_retrograde"] = _raise_uninitialized_error
        self.__dict__["_assign_mixed_spherical"] = _raise_uninitialized_error
        self.__dict__["_assign_spherical"] = _raise_uninitialized_error
        self.__dict__["_get_central_body_name"] = _raise_uninitialized_error
        self.__dict__["_get_epoch"] = _raise_uninitialized_error
        self.__dict__["_set_epoch"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IOrbitState._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IOrbitState from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IOrbitState = agcom.GUID(IOrbitState._uuid)
        vtable_offset_local = IOrbitState._vtable_offset - 1
        self.__dict__["_convert_to"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get_orbit_state_type"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_assign"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+3, agcom.PVOID)
        self.__dict__["_assign_classical"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+4, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_cartesian"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+5, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_geodetic"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+6, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_equinoctial_posigrade"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+7, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_equinoctial_retrograde"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+8, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_mixed_spherical"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+9, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_assign_spherical"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+10, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_get_central_body_name"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+11, POINTER(agcom.BSTR))
        self.__dict__["_get_epoch"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+12, POINTER(agcom.VARIANT))
        self.__dict__["_set_epoch"] = IAGFUNCTYPE(pUnk, IID_IOrbitState, vtable_offset_local+13, agcom.VARIANT)
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
    
    def convert_to(self, type:"ORBIT_STATE_TYPE") -> "IOrbitState":
        """Method to changes the coordinate type to the type specified."""
        with agmarshall.AgEnum_arg(ORBIT_STATE_TYPE, type) as arg_type, \
             agmarshall.AgInterface_out_arg() as arg_ppIAgOrbitState:
            agcls.evaluate_hresult(self.__dict__["_convert_to"](arg_type.COM_val, byref(arg_ppIAgOrbitState.COM_val)))
            return arg_ppIAgOrbitState.python_val

    @property
    def orbit_state_type(self) -> "ORBIT_STATE_TYPE":
        """Returns the coordinate type currently being used."""
        with agmarshall.AgEnum_arg(ORBIT_STATE_TYPE) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_get_orbit_state_type"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    def assign(self, pOrbitState:"IOrbitState") -> None:
        """Assign a new coordinate type."""
        with agmarshall.AgInterface_in_arg(pOrbitState, IOrbitState) as arg_pOrbitState:
            agcls.evaluate_hresult(self.__dict__["_assign"](arg_pOrbitState.COM_val))

    def assign_classical(self, eCoordinateSystem:"COORDINATE_SYSTEM", semiMajorAxis:float, eccentricity:float, inclination:float, argOfPerigee:float, rAAN:float, meanAnomaly:float) -> None:
        """Helper method to assign a new orbit state using Classical representation"""
        with agmarshall.AgEnum_arg(COORDINATE_SYSTEM, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(semiMajorAxis) as arg_semiMajorAxis, \
             agmarshall.DOUBLE_arg(eccentricity) as arg_eccentricity, \
             agmarshall.DOUBLE_arg(inclination) as arg_inclination, \
             agmarshall.DOUBLE_arg(argOfPerigee) as arg_argOfPerigee, \
             agmarshall.DOUBLE_arg(rAAN) as arg_rAAN, \
             agmarshall.DOUBLE_arg(meanAnomaly) as arg_meanAnomaly:
            agcls.evaluate_hresult(self.__dict__["_assign_classical"](arg_eCoordinateSystem.COM_val, arg_semiMajorAxis.COM_val, arg_eccentricity.COM_val, arg_inclination.COM_val, arg_argOfPerigee.COM_val, arg_rAAN.COM_val, arg_meanAnomaly.COM_val))

    def assign_cartesian(self, eCoordinateSystem:"COORDINATE_SYSTEM", xPosition:float, yPosition:float, zPosition:float, xVelocity:float, yVelocity:float, zVelocity:float) -> None:
        """Helper method to assign a new orbit state using Cartesian representation"""
        with agmarshall.AgEnum_arg(COORDINATE_SYSTEM, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(xPosition) as arg_xPosition, \
             agmarshall.DOUBLE_arg(yPosition) as arg_yPosition, \
             agmarshall.DOUBLE_arg(zPosition) as arg_zPosition, \
             agmarshall.DOUBLE_arg(xVelocity) as arg_xVelocity, \
             agmarshall.DOUBLE_arg(yVelocity) as arg_yVelocity, \
             agmarshall.DOUBLE_arg(zVelocity) as arg_zVelocity:
            agcls.evaluate_hresult(self.__dict__["_assign_cartesian"](arg_eCoordinateSystem.COM_val, arg_xPosition.COM_val, arg_yPosition.COM_val, arg_zPosition.COM_val, arg_xVelocity.COM_val, arg_yVelocity.COM_val, arg_zVelocity.COM_val))

    def assign_geodetic(self, eCoordinateSystem:"COORDINATE_SYSTEM", latitude:float, longitude:float, altitude:float, latitudeRate:float, longitudeRate:float, altitudeRate:float) -> None:
        """Helper method to assign a new orbit state using Geodetic representation"""
        with agmarshall.AgEnum_arg(COORDINATE_SYSTEM, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg(altitude) as arg_altitude, \
             agmarshall.DOUBLE_arg(latitudeRate) as arg_latitudeRate, \
             agmarshall.DOUBLE_arg(longitudeRate) as arg_longitudeRate, \
             agmarshall.DOUBLE_arg(altitudeRate) as arg_altitudeRate:
            agcls.evaluate_hresult(self.__dict__["_assign_geodetic"](arg_eCoordinateSystem.COM_val, arg_latitude.COM_val, arg_longitude.COM_val, arg_altitude.COM_val, arg_latitudeRate.COM_val, arg_longitudeRate.COM_val, arg_altitudeRate.COM_val))

    def assign_equinoctial_posigrade(self, eCoordinateSystem:"COORDINATE_SYSTEM", semiMajorAxis:float, h:float, k:float, p:float, q:float, meanLon:float) -> None:
        """Helper method to assign a new orbit state using Equinoctial representation"""
        with agmarshall.AgEnum_arg(COORDINATE_SYSTEM, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(semiMajorAxis) as arg_semiMajorAxis, \
             agmarshall.DOUBLE_arg(h) as arg_h, \
             agmarshall.DOUBLE_arg(k) as arg_k, \
             agmarshall.DOUBLE_arg(p) as arg_p, \
             agmarshall.DOUBLE_arg(q) as arg_q, \
             agmarshall.DOUBLE_arg(meanLon) as arg_meanLon:
            agcls.evaluate_hresult(self.__dict__["_assign_equinoctial_posigrade"](arg_eCoordinateSystem.COM_val, arg_semiMajorAxis.COM_val, arg_h.COM_val, arg_k.COM_val, arg_p.COM_val, arg_q.COM_val, arg_meanLon.COM_val))

    def assign_equinoctial_retrograde(self, eCoordinateSystem:"COORDINATE_SYSTEM", semiMajorAxis:float, h:float, k:float, p:float, q:float, meanLon:float) -> None:
        """Helper method to assign a new orbit state using Equinoctial representation"""
        with agmarshall.AgEnum_arg(COORDINATE_SYSTEM, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(semiMajorAxis) as arg_semiMajorAxis, \
             agmarshall.DOUBLE_arg(h) as arg_h, \
             agmarshall.DOUBLE_arg(k) as arg_k, \
             agmarshall.DOUBLE_arg(p) as arg_p, \
             agmarshall.DOUBLE_arg(q) as arg_q, \
             agmarshall.DOUBLE_arg(meanLon) as arg_meanLon:
            agcls.evaluate_hresult(self.__dict__["_assign_equinoctial_retrograde"](arg_eCoordinateSystem.COM_val, arg_semiMajorAxis.COM_val, arg_h.COM_val, arg_k.COM_val, arg_p.COM_val, arg_q.COM_val, arg_meanLon.COM_val))

    def assign_mixed_spherical(self, eCoordinateSystem:"COORDINATE_SYSTEM", latitude:float, longitude:float, altitude:float, horFlightPathAngle:float, flightPathAzimuth:float, velocity:float) -> None:
        """Helper method to assign a new orbit state using Mixed Spherical representation"""
        with agmarshall.AgEnum_arg(COORDINATE_SYSTEM, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(latitude) as arg_latitude, \
             agmarshall.DOUBLE_arg(longitude) as arg_longitude, \
             agmarshall.DOUBLE_arg(altitude) as arg_altitude, \
             agmarshall.DOUBLE_arg(horFlightPathAngle) as arg_horFlightPathAngle, \
             agmarshall.DOUBLE_arg(flightPathAzimuth) as arg_flightPathAzimuth, \
             agmarshall.DOUBLE_arg(velocity) as arg_velocity:
            agcls.evaluate_hresult(self.__dict__["_assign_mixed_spherical"](arg_eCoordinateSystem.COM_val, arg_latitude.COM_val, arg_longitude.COM_val, arg_altitude.COM_val, arg_horFlightPathAngle.COM_val, arg_flightPathAzimuth.COM_val, arg_velocity.COM_val))

    def assign_spherical(self, eCoordinateSystem:"COORDINATE_SYSTEM", rightAscension:float, declination:float, radius:float, horFlightPathAngle:float, flightPathAzimuth:float, velocity:float) -> None:
        """Helper method to assign a new orbit state using Spherical representation"""
        with agmarshall.AgEnum_arg(COORDINATE_SYSTEM, eCoordinateSystem) as arg_eCoordinateSystem, \
             agmarshall.DOUBLE_arg(rightAscension) as arg_rightAscension, \
             agmarshall.DOUBLE_arg(declination) as arg_declination, \
             agmarshall.DOUBLE_arg(radius) as arg_radius, \
             agmarshall.DOUBLE_arg(horFlightPathAngle) as arg_horFlightPathAngle, \
             agmarshall.DOUBLE_arg(flightPathAzimuth) as arg_flightPathAzimuth, \
             agmarshall.DOUBLE_arg(velocity) as arg_velocity:
            agcls.evaluate_hresult(self.__dict__["_assign_spherical"](arg_eCoordinateSystem.COM_val, arg_rightAscension.COM_val, arg_declination.COM_val, arg_radius.COM_val, arg_horFlightPathAngle.COM_val, arg_flightPathAzimuth.COM_val, arg_velocity.COM_val))

    @property
    def central_body_name(self) -> str:
        """Gets the central body."""
        with agmarshall.BSTR_arg() as arg_pCBName:
            agcls.evaluate_hresult(self.__dict__["_get_central_body_name"](byref(arg_pCBName.COM_val)))
            return arg_pCBName.python_val

    @property
    def epoch(self) -> typing.Any:
        """The state epoch"""
        with agmarshall.VARIANT_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_epoch"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @epoch.setter
    def epoch(self, epoch:typing.Any) -> None:
        with agmarshall.VARIANT_arg(epoch) as arg_epoch:
            agcls.evaluate_hresult(self.__dict__["_set_epoch"](arg_epoch.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{42342AD2-F6C5-426B-AB2A-3688F05353C8}", IOrbitState)
agcls.AgTypeNameMap["IOrbitState"] = IOrbitState

class ICartesian2Vector(object):
    """Represents a cartesian 2-D vector."""
    _uuid = "{DA459BD7-5810-4B30-8397-21EDA9E52D2B}"
    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_x"] = _raise_uninitialized_error
        self.__dict__["_set_x"] = _raise_uninitialized_error
        self.__dict__["_get_y"] = _raise_uninitialized_error
        self.__dict__["_set_y"] = _raise_uninitialized_error
        self.__dict__["_get"] = _raise_uninitialized_error
        self.__dict__["_set"] = _raise_uninitialized_error
        self.__dict__["_to_array"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ICartesian2Vector._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ICartesian2Vector from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_ICartesian2Vector = agcom.GUID(ICartesian2Vector._uuid)
        vtable_offset_local = ICartesian2Vector._vtable_offset - 1
        self.__dict__["_get_x"] = IAGFUNCTYPE(pUnk, IID_ICartesian2Vector, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_set_x"] = IAGFUNCTYPE(pUnk, IID_ICartesian2Vector, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_get_y"] = IAGFUNCTYPE(pUnk, IID_ICartesian2Vector, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_set_y"] = IAGFUNCTYPE(pUnk, IID_ICartesian2Vector, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_get"] = IAGFUNCTYPE(pUnk, IID_ICartesian2Vector, vtable_offset_local+5, POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE))
        self.__dict__["_set"] = IAGFUNCTYPE(pUnk, IID_ICartesian2Vector, vtable_offset_local+6, agcom.DOUBLE, agcom.DOUBLE)
        self.__dict__["_to_array"] = IAGFUNCTYPE(pUnk, IID_ICartesian2Vector, vtable_offset_local+7, POINTER(agcom.SAFEARRAY))
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
    
    @property
    def x(self) -> float:
        """X coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_x"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @x.setter
    def x(self, x:float) -> None:
        with agmarshall.DOUBLE_arg(x) as arg_x:
            agcls.evaluate_hresult(self.__dict__["_set_x"](arg_x.COM_val))

    @property
    def y(self) -> float:
        """Y coordinate"""
        with agmarshall.DOUBLE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_y"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @y.setter
    def y(self, y:float) -> None:
        with agmarshall.DOUBLE_arg(y) as arg_y:
            agcls.evaluate_hresult(self.__dict__["_set_y"](arg_y.COM_val))

    def get(self) -> typing.Tuple[float, float]:
        """Returns cartesian vector"""
        with agmarshall.DOUBLE_arg() as arg_x, \
             agmarshall.DOUBLE_arg() as arg_y:
            agcls.evaluate_hresult(self.__dict__["_get"](byref(arg_x.COM_val), byref(arg_y.COM_val)))
            return arg_x.python_val, arg_y.python_val

    def set(self, x:float, y:float) -> None:
        """Sets cartesian vector"""
        with agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y:
            agcls.evaluate_hresult(self.__dict__["_set"](arg_x.COM_val, arg_y.COM_val))

    def to_array(self) -> list:
        """Returns coordinates as an array."""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_to_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{DA459BD7-5810-4B30-8397-21EDA9E52D2B}", ICartesian2Vector)
agcls.AgTypeNameMap["ICartesian2Vector"] = ICartesian2Vector

class IUnitPreferencesDimension(object):
    """Provides info on a Dimension from the global unit table."""
    _uuid = "{AA966FFD-1A99-45D8-9193-C519BBBA99FA}"
    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_id"] = _raise_uninitialized_error
        self.__dict__["_get_name"] = _raise_uninitialized_error
        self.__dict__["_get_available_units"] = _raise_uninitialized_error
        self.__dict__["_get_current_unit"] = _raise_uninitialized_error
        self.__dict__["_set_current_unit"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUnitPreferencesDimension._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesDimension from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUnitPreferencesDimension = agcom.GUID(IUnitPreferencesDimension._uuid)
        vtable_offset_local = IUnitPreferencesDimension._vtable_offset - 1
        self.__dict__["_get_id"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimension, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_get_name"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimension, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_get_available_units"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimension, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_get_current_unit"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimension, vtable_offset_local+4, POINTER(agcom.PVOID))
        self.__dict__["_set_current_unit"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimension, vtable_offset_local+5, agcom.BSTR)
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
    
    @property
    def id(self) -> int:
        """Returns the ID of the dimension."""
        with agmarshall.LONG_arg() as arg_pId:
            agcls.evaluate_hresult(self.__dict__["_get_id"](byref(arg_pId.COM_val)))
            return arg_pId.python_val

    @property
    def name(self) -> str:
        """Returns the current Dimension's full name."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_get_name"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def available_units(self) -> "IUnitPreferencesUnitCollection":
        """Returns collection of Units."""
        with agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnitCollection:
            agcls.evaluate_hresult(self.__dict__["_get_available_units"](byref(arg_ppUnitPrefsUnitCollection.COM_val)))
            return arg_ppUnitPrefsUnitCollection.python_val

    @property
    def current_unit(self) -> "IUnitPreferencesUnit":
        """Returns the current unit for this dimension."""
        with agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_get_current_unit"](byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    def set_current_unit(self, unitAbbrv:str) -> None:
        """Sets the Unit for this simple dimension."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_set_current_unit"](arg_unitAbbrv.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{AA966FFD-1A99-45D8-9193-C519BBBA99FA}", IUnitPreferencesDimension)
agcls.AgTypeNameMap["IUnitPreferencesDimension"] = IUnitPreferencesDimension

class IPropertyInfo(object):
    """Property information."""
    _uuid = "{26A48B4B-BF6A-4F9D-9658-44A7A2DBBE2A}"
    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_name"] = _raise_uninitialized_error
        self.__dict__["_get_property_type"] = _raise_uninitialized_error
        self.__dict__["_get_value"] = _raise_uninitialized_error
        self.__dict__["_set_value"] = _raise_uninitialized_error
        self.__dict__["_get_has_min"] = _raise_uninitialized_error
        self.__dict__["_get_has_max"] = _raise_uninitialized_error
        self.__dict__["_get_min"] = _raise_uninitialized_error
        self.__dict__["_get_max"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IPropertyInfo._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IPropertyInfo from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IPropertyInfo = agcom.GUID(IPropertyInfo._uuid)
        vtable_offset_local = IPropertyInfo._vtable_offset - 1
        self.__dict__["_get_name"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_get_property_type"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_get_value"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+3, POINTER(agcom.VARIANT))
        self.__dict__["_set_value"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+4, agcom.VARIANT)
        self.__dict__["_get_has_min"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_has_max"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_min"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+7, POINTER(agcom.VARIANT))
        self.__dict__["_get_max"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfo, vtable_offset_local+8, POINTER(agcom.VARIANT))
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
    
    @property
    def name(self) -> str:
        """The name of the property."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_name"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def property_type(self) -> "PROPERTY_INFO_VALUE_TYPE":
        """The type of property."""
        with agmarshall.AgEnum_arg(PROPERTY_INFO_VALUE_TYPE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_property_type"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def get_value(self) -> typing.Any:
        """The value of the property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_value"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def set_value(self, propertyInfo:typing.Any) -> None:
        """The value of the property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg(propertyInfo) as arg_propertyInfo:
            agcls.evaluate_hresult(self.__dict__["_set_value"](arg_propertyInfo.COM_val))

    @property
    def has_min(self) -> bool:
        """Used to determine if the property has a minimum value."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_has_min"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def has_max(self) -> bool:
        """Used to determine if the property has a maximum value."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_has_max"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def min(self) -> typing.Any:
        """The minimum value of this property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_min"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def max(self) -> typing.Any:
        """The maximum value of this property. Use PropertyType to determine the type to cast to."""
        with agmarshall.VARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_max"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{26A48B4B-BF6A-4F9D-9658-44A7A2DBBE2A}", IPropertyInfo)
agcls.AgTypeNameMap["IPropertyInfo"] = IPropertyInfo

class IPropertyInfoCollection(object):
    """The collection of properties."""
    _uuid = "{198E6280-1D5A-4AED-9DE3-ACE354B95287}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_index"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_name"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IPropertyInfoCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IPropertyInfoCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IPropertyInfoCollection = agcom.GUID(IPropertyInfoCollection._uuid)
        vtable_offset_local = IPropertyInfoCollection._vtable_offset - 1
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfoCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfoCollection, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfoCollection, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__["_get_item_by_index"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfoCollection, vtable_offset_local+4, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_name"] = IAGFUNCTYPE(pUnk, IID_IPropertyInfoCollection, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.PVOID))
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IPropertyInfo":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    def item(self, indexOrName:typing.Any) -> "IPropertyInfo":
        """Allows the user to iterate through the properties."""
        with agmarshall.VARIANT_arg(indexOrName) as arg_indexOrName, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_indexOrName.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates through the properties."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    @property
    def count(self) -> int:
        """The number of properties available."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def get_item_by_index(self, index:int) -> "IPropertyInfo":
        """Retrieves a property from the collection by index."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_index"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def get_item_by_name(self, name:str) -> "IPropertyInfo":
        """Retrieves a property from the collection by name."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_name"](arg_name.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{198E6280-1D5A-4AED-9DE3-ACE354B95287}", IPropertyInfoCollection)
agcls.AgTypeNameMap["IPropertyInfoCollection"] = IPropertyInfoCollection

class IRuntimeTypeInfo(object):
    """Interface used to retrieve the properties at runtime."""
    _uuid = "{01F8872C-9586-4131-A724-F97C6ADD083F}"
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_properties"] = _raise_uninitialized_error
        self.__dict__["_get_is_collection"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_get_item"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IRuntimeTypeInfo._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IRuntimeTypeInfo from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IRuntimeTypeInfo = agcom.GUID(IRuntimeTypeInfo._uuid)
        vtable_offset_local = IRuntimeTypeInfo._vtable_offset - 1
        self.__dict__["_get_properties"] = IAGFUNCTYPE(pUnk, IID_IRuntimeTypeInfo, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_get_is_collection"] = IAGFUNCTYPE(pUnk, IID_IRuntimeTypeInfo, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IRuntimeTypeInfo, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__["_get_item"] = IAGFUNCTYPE(pUnk, IID_IRuntimeTypeInfo, vtable_offset_local+4, agcom.LONG, POINTER(agcom.PVOID))
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
    
    @property
    def properties(self) -> "IPropertyInfoCollection":
        """The collection of properties."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_properties"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    @property
    def is_collection(self) -> bool:
        """Determines if the interface is a collection."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_is_collection"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def count(self) -> int:
        """If the interface is a collection, returns the collection count."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def get_item(self, index:int) -> "IPropertyInfo":
        """Returns the property of the collection at the given index."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_item"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{01F8872C-9586-4131-A724-F97C6ADD083F}", IRuntimeTypeInfo)
agcls.AgTypeNameMap["IRuntimeTypeInfo"] = IRuntimeTypeInfo

class IRuntimeTypeInfoProvider(object):
    """Access point for IRuntimeTypeInfo."""
    _uuid = "{E9AD01B5-7892-4367-8EC7-60EA26CE0E11}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_provide_runtime_type_info"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IRuntimeTypeInfoProvider._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IRuntimeTypeInfoProvider from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IRuntimeTypeInfoProvider = agcom.GUID(IRuntimeTypeInfoProvider._uuid)
        vtable_offset_local = IRuntimeTypeInfoProvider._vtable_offset - 1
        self.__dict__["_get_provide_runtime_type_info"] = IAGFUNCTYPE(pUnk, IID_IRuntimeTypeInfoProvider, vtable_offset_local+1, POINTER(agcom.PVOID))
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
    
    @property
    def provide_runtime_type_info(self) -> "IRuntimeTypeInfo":
        """Returns the IRuntimeTypeInfo interface to access properties at runtime."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_provide_runtime_type_info"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{E9AD01B5-7892-4367-8EC7-60EA26CE0E11}", IRuntimeTypeInfoProvider)
agcls.AgTypeNameMap["IRuntimeTypeInfoProvider"] = IRuntimeTypeInfoProvider

class IExecCmdResult(object):
    """Collection of strings returned by the ExecuteCommand."""
    _uuid = "{CC5C63BC-FF0A-4CC8-AD58-5A8D11DD9C60}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_range"] = _raise_uninitialized_error
        self.__dict__["_get_is_succeeded"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IExecCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IExecCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IExecCmdResult = agcom.GUID(IExecCmdResult._uuid)
        vtable_offset_local = IExecCmdResult._vtable_offset - 1
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_range"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+4, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_get_is_succeeded"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> str:
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def item(self, index:int) -> str:
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pItem:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pItem.COM_val)))
            return arg_pItem.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the strings in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    def range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        with agmarshall.LONG_arg(startIndex) as arg_startIndex, \
             agmarshall.LONG_arg(stopIndex) as arg_stopIndex, \
             agmarshall.SAFEARRAY_arg() as arg_ppVar:
            agcls.evaluate_hresult(self.__dict__["_range"](arg_startIndex.COM_val, arg_stopIndex.COM_val, byref(arg_ppVar.COM_val)))
            return arg_ppVar.python_val

    @property
    def is_succeeded(self) -> bool:
        """Indicates whether the object contains valid results."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_is_succeeded"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{CC5C63BC-FF0A-4CC8-AD58-5A8D11DD9C60}", IExecCmdResult)
agcls.AgTypeNameMap["IExecCmdResult"] = IExecCmdResult

class IExecMultiCmdResult(object):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    _uuid = "{ECEFEE1C-F623-4926-A738-3D95FC5E3DEE}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IExecMultiCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IExecMultiCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IExecMultiCmdResult = agcom.GUID(IExecMultiCmdResult._uuid)
        vtable_offset_local = IExecMultiCmdResult._vtable_offset - 1
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IExecMultiCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IExecMultiCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IExecMultiCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IExecCmdResult":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def item(self, index:int) -> "IExecCmdResult":
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the objects in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{ECEFEE1C-F623-4926-A738-3D95FC5E3DEE}", IExecMultiCmdResult)
agcls.AgTypeNameMap["IExecMultiCmdResult"] = IExecMultiCmdResult

class IUnitPreferencesUnit(object):
    """Provides info about a unit."""
    _uuid = "{4B4E2F51-280F-4E35-AEA5-71CDAC7342C4}"
    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_full_name"] = _raise_uninitialized_error
        self.__dict__["_get_abbrv"] = _raise_uninitialized_error
        self.__dict__["_get_id"] = _raise_uninitialized_error
        self.__dict__["_get_dimension"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUnitPreferencesUnit._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesUnit from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUnitPreferencesUnit = agcom.GUID(IUnitPreferencesUnit._uuid)
        vtable_offset_local = IUnitPreferencesUnit._vtable_offset - 1
        self.__dict__["_get_full_name"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnit, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_get_abbrv"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnit, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_get_id"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnit, vtable_offset_local+3, POINTER(agcom.LONG))
        self.__dict__["_get_dimension"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnit, vtable_offset_local+4, POINTER(agcom.PVOID))
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
    
    @property
    def full_name(self) -> str:
        """Returns the fullname of the unit."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_get_full_name"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def abbrv(self) -> str:
        """Returns the abbreviation of the unit."""
        with agmarshall.BSTR_arg() as arg_pAbbrv:
            agcls.evaluate_hresult(self.__dict__["_get_abbrv"](byref(arg_pAbbrv.COM_val)))
            return arg_pAbbrv.python_val

    @property
    def id(self) -> int:
        """Returns the ID of the unit."""
        with agmarshall.LONG_arg() as arg_pId:
            agcls.evaluate_hresult(self.__dict__["_get_id"](byref(arg_pId.COM_val)))
            return arg_pId.python_val

    @property
    def dimension(self) -> "IUnitPreferencesDimension":
        """Returns the Dimension for this unit."""
        with agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_get_dimension"](byref(arg_ppUnitPrefsDim.COM_val)))
            return arg_ppUnitPrefsDim.python_val


agcls.AgClassCatalog.add_catalog_entry("{4B4E2F51-280F-4E35-AEA5-71CDAC7342C4}", IUnitPreferencesUnit)
agcls.AgTypeNameMap["IUnitPreferencesUnit"] = IUnitPreferencesUnit

class IUnitPreferencesUnitCollection(object):
    """Provides access to the Unit collection."""
    _uuid = "{C9A263F5-A021-4BEC-85F3-526FA41F1CB4}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_index"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_name"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUnitPreferencesUnitCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesUnitCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUnitPreferencesUnitCollection = agcom.GUID(IUnitPreferencesUnitCollection._uuid)
        vtable_offset_local = IUnitPreferencesUnitCollection._vtable_offset - 1
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnitCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnitCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnitCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_index"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnitCollection, vtable_offset_local+4, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_name"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesUnitCollection, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.PVOID))
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IUnitPreferencesUnit":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    def item(self, indexOrName:typing.Any) -> "IUnitPreferencesUnit":
        """Returns the specific item in the collection given a unit identifier or an index."""
        with agmarshall.VARIANT_arg(indexOrName) as arg_indexOrName, \
             agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_indexOrName.COM_val, byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    @property
    def count(self) -> int:
        """Returns the number of items in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an enumeration of UnitPreferencesUnit."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def get_item_by_index(self, index:int) -> "IUnitPreferencesUnit":
        """Retrieves a unit from the collection by index."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_index"](arg_index.COM_val, byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    def get_item_by_name(self, name:str) -> "IUnitPreferencesUnit":
        """Retrieves a unit from the collection by name."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppUnitPrefsUnit:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_name"](arg_name.COM_val, byref(arg_ppUnitPrefsUnit.COM_val)))
            return arg_ppUnitPrefsUnit.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{C9A263F5-A021-4BEC-85F3-526FA41F1CB4}", IUnitPreferencesUnitCollection)
agcls.AgTypeNameMap["IUnitPreferencesUnitCollection"] = IUnitPreferencesUnitCollection

class IUnitPreferencesDimensionCollection(object):
    """Provides accesses to the global unit table."""
    _uuid = "{40AE1C29-E5F5-426A-AEB7-D02CC7D2873C}"
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_set_current_unit"] = _raise_uninitialized_error
        self.__dict__["_get_current_unit_abbrv"] = _raise_uninitialized_error
        self.__dict__["_get_mission_elapsed_time"] = _raise_uninitialized_error
        self.__dict__["_set_mission_elapsed_time"] = _raise_uninitialized_error
        self.__dict__["_get_julian_date_offset"] = _raise_uninitialized_error
        self.__dict__["_set_julian_date_offset"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_reset_units"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_index"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_name"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUnitPreferencesDimensionCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUnitPreferencesDimensionCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUnitPreferencesDimensionCollection = agcom.GUID(IUnitPreferencesDimensionCollection._uuid)
        vtable_offset_local = IUnitPreferencesDimensionCollection._vtable_offset - 1
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_set_current_unit"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+3, agcom.BSTR, agcom.BSTR)
        self.__dict__["_get_current_unit_abbrv"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+4, agcom.VARIANT, POINTER(agcom.BSTR))
        self.__dict__["_get_mission_elapsed_time"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+5, POINTER(agcom.VARIANT))
        self.__dict__["_set_mission_elapsed_time"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+6, agcom.VARIANT)
        self.__dict__["_get_julian_date_offset"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_set_julian_date_offset"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+9, POINTER(agcom.PVOID))
        self.__dict__["_reset_units"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+10, )
        self.__dict__["_get_item_by_index"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+11, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_name"] = IAGFUNCTYPE(pUnk, IID_IUnitPreferencesDimensionCollection, vtable_offset_local+12, agcom.BSTR, POINTER(agcom.PVOID))
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IUnitPreferencesDimension":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    def item(self, indexOrName:typing.Any) -> "IUnitPreferencesDimension":
        """Returns an IUnitPreferencesDimension given a Dimension name or an index."""
        with agmarshall.VARIANT_arg(indexOrName) as arg_indexOrName, \
             agmarshall.AgInterface_out_arg() as arg_ppAgUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_indexOrName.COM_val, byref(arg_ppAgUnitPrefsDim.COM_val)))
            return arg_ppAgUnitPrefsDim.python_val

    @property
    def count(self) -> int:
        """Returns the number of items in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def set_current_unit(self, dimension:str, unitAbbrv:str) -> None:
        """Returns the Current unit for a Dimension."""
        with agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_set_current_unit"](arg_dimension.COM_val, arg_unitAbbrv.COM_val))

    def get_current_unit_abbrv(self, indexOrDimName:typing.Any) -> str:
        """Returns the Current Unit for a Dimension."""
        with agmarshall.VARIANT_arg(indexOrDimName) as arg_indexOrDimName, \
             agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_get_current_unit_abbrv"](arg_indexOrDimName.COM_val, byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    @property
    def mission_elapsed_time(self) -> typing.Any:
        """The MissionElapsedTime."""
        with agmarshall.VARIANT_arg() as arg_pMisElapTime:
            agcls.evaluate_hresult(self.__dict__["_get_mission_elapsed_time"](byref(arg_pMisElapTime.COM_val)))
            return arg_pMisElapTime.python_val

    @mission_elapsed_time.setter
    def mission_elapsed_time(self, pMisElapTime:typing.Any) -> None:
        with agmarshall.VARIANT_arg(pMisElapTime) as arg_pMisElapTime:
            agcls.evaluate_hresult(self.__dict__["_set_mission_elapsed_time"](arg_pMisElapTime.COM_val))

    @property
    def julian_date_offset(self) -> float:
        """The JulianDateOffset."""
        with agmarshall.DOUBLE_arg() as arg_pJDateOffset:
            agcls.evaluate_hresult(self.__dict__["_get_julian_date_offset"](byref(arg_pJDateOffset.COM_val)))
            return arg_pJDateOffset.python_val

    @julian_date_offset.setter
    def julian_date_offset(self, pJDateOffset:float) -> None:
        with agmarshall.DOUBLE_arg(pJDateOffset) as arg_pJDateOffset:
            agcls.evaluate_hresult(self.__dict__["_set_julian_date_offset"](arg_pJDateOffset.COM_val))

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns a collection of IUnitPreferencesDimension."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def reset_units(self) -> None:
        """Resets the unitpreferences to the Default units"""
        agcls.evaluate_hresult(self.__dict__["_reset_units"]())

    def get_item_by_index(self, index:int) -> "IUnitPreferencesDimension":
        """Retrieves a dimension from the collection by index."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppAgUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_index"](arg_index.COM_val, byref(arg_ppAgUnitPrefsDim.COM_val)))
            return arg_ppAgUnitPrefsDim.python_val

    def get_item_by_name(self, name:str) -> "IUnitPreferencesDimension":
        """Retrieves a dimension from the collection by name."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppAgUnitPrefsDim:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_name"](arg_name.COM_val, byref(arg_ppAgUnitPrefsDim.COM_val)))
            return arg_ppAgUnitPrefsDim.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{40AE1C29-E5F5-426A-AEB7-D02CC7D2873C}", IUnitPreferencesDimensionCollection)
agcls.AgTypeNameMap["IUnitPreferencesDimensionCollection"] = IUnitPreferencesDimensionCollection

class IQuantity(object):
    """Provides helper methods for a quantity."""
    _uuid = "{C0BBB39C-54E2-4344-B24E-58AA6AA4446B}"
    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_dimension"] = _raise_uninitialized_error
        self.__dict__["_get_unit"] = _raise_uninitialized_error
        self.__dict__["_convert_to_unit"] = _raise_uninitialized_error
        self.__dict__["_get_value"] = _raise_uninitialized_error
        self.__dict__["_set_value"] = _raise_uninitialized_error
        self.__dict__["_add"] = _raise_uninitialized_error
        self.__dict__["_subtract"] = _raise_uninitialized_error
        self.__dict__["_multiply_qty"] = _raise_uninitialized_error
        self.__dict__["_divide_qty"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IQuantity._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IQuantity from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IQuantity = agcom.GUID(IQuantity._uuid)
        vtable_offset_local = IQuantity._vtable_offset - 1
        self.__dict__["_get_dimension"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_get_unit"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_convert_to_unit"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+3, agcom.BSTR)
        self.__dict__["_get_value"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_set_value"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+5, agcom.DOUBLE)
        self.__dict__["_add"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+6, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_subtract"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+7, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_multiply_qty"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+8, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_divide_qty"] = IAGFUNCTYPE(pUnk, IID_IQuantity, vtable_offset_local+9, agcom.PVOID, POINTER(agcom.PVOID))
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
    
    @property
    def dimension(self) -> str:
        """Gets the name of the dimension"""
        with agmarshall.BSTR_arg() as arg_pDimName:
            agcls.evaluate_hresult(self.__dict__["_get_dimension"](byref(arg_pDimName.COM_val)))
            return arg_pDimName.python_val

    @property
    def unit(self) -> str:
        """The current Unit abbreviation."""
        with agmarshall.BSTR_arg() as arg_pUnitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_get_unit"](byref(arg_pUnitAbbrv.COM_val)))
            return arg_pUnitAbbrv.python_val

    def convert_to_unit(self, unitAbbrv:str) -> None:
        """Changes the value in this quantity to the specified unit."""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv:
            agcls.evaluate_hresult(self.__dict__["_convert_to_unit"](arg_unitAbbrv.COM_val))

    @property
    def value(self) -> float:
        """The current value."""
        with agmarshall.DOUBLE_arg() as arg_pValue:
            agcls.evaluate_hresult(self.__dict__["_get_value"](byref(arg_pValue.COM_val)))
            return arg_pValue.python_val

    @value.setter
    def value(self, value:float) -> None:
        with agmarshall.DOUBLE_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_set_value"](arg_value.COM_val))

    def add(self, quantity:"IQuantity") -> "IQuantity":
        """Adds the value from the IQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_add"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def subtract(self, quantity:"IQuantity") -> "IQuantity":
        """Subtracts the value from the IQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_subtract"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def multiply_qty(self, quantity:"IQuantity") -> "IQuantity":
        """Multiplies the value from the IQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_multiply_qty"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def divide_qty(self, quantity:"IQuantity") -> "IQuantity":
        """Divides the value from the IQuantity interface to this interface. The dimensions must be similar."""
        with agmarshall.AgInterface_in_arg(quantity, IQuantity) as arg_quantity, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_divide_qty"](arg_quantity.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val


agcls.AgClassCatalog.add_catalog_entry("{C0BBB39C-54E2-4344-B24E-58AA6AA4446B}", IQuantity)
agcls.AgTypeNameMap["IQuantity"] = IQuantity

class IDate(object):
    """Provides helper methods for a date."""
    _uuid = "{BFC8EA09-19BD-432A-923D-C553E8E37993}"
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_format"] = _raise_uninitialized_error
        self.__dict__["_set_date"] = _raise_uninitialized_error
        self.__dict__["_get_ole_date"] = _raise_uninitialized_error
        self.__dict__["_set_ole_date"] = _raise_uninitialized_error
        self.__dict__["_get_whole_days"] = _raise_uninitialized_error
        self.__dict__["_set_whole_days"] = _raise_uninitialized_error
        self.__dict__["_get_sec_into_day"] = _raise_uninitialized_error
        self.__dict__["_set_sec_into_day"] = _raise_uninitialized_error
        self.__dict__["_get_whole_days_utc"] = _raise_uninitialized_error
        self.__dict__["_set_whole_days_utc"] = _raise_uninitialized_error
        self.__dict__["_get_sec_into_day_utc"] = _raise_uninitialized_error
        self.__dict__["_set_sec_into_day_utc"] = _raise_uninitialized_error
        self.__dict__["_add"] = _raise_uninitialized_error
        self.__dict__["_subtract"] = _raise_uninitialized_error
        self.__dict__["_span"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDate._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDate from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IDate = agcom.GUID(IDate._uuid)
        vtable_offset_local = IDate._vtable_offset - 1
        self.__dict__["_format"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+1, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_set_date"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+2, agcom.BSTR, agcom.BSTR)
        self.__dict__["_get_ole_date"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+3, POINTER(agcom.DATE))
        self.__dict__["_set_ole_date"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+4, agcom.DATE)
        self.__dict__["_get_whole_days"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_set_whole_days"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+6, agcom.LONG)
        self.__dict__["_get_sec_into_day"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+7, POINTER(agcom.DOUBLE))
        self.__dict__["_set_sec_into_day"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+8, agcom.DOUBLE)
        self.__dict__["_get_whole_days_utc"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+9, POINTER(agcom.LONG))
        self.__dict__["_set_whole_days_utc"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+10, agcom.LONG)
        self.__dict__["_get_sec_into_day_utc"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+11, POINTER(agcom.DOUBLE))
        self.__dict__["_set_sec_into_day_utc"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+12, agcom.DOUBLE)
        self.__dict__["_add"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+13, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID))
        self.__dict__["_subtract"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+14, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID))
        self.__dict__["_span"] = IAGFUNCTYPE(pUnk, IID_IDate, vtable_offset_local+15, agcom.PVOID, POINTER(agcom.PVOID))
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
    
    def format(self, unit:str) -> str:
        """Returns the value of the date given the unit."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.BSTR_arg() as arg_pValue:
            agcls.evaluate_hresult(self.__dict__["_format"](arg_unit.COM_val, byref(arg_pValue.COM_val)))
            return arg_pValue.python_val

    def set_date(self, unit:str, value:str) -> None:
        """Sets this date with the given date value and unit type."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.BSTR_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_set_date"](arg_unit.COM_val, arg_value.COM_val))

    @property
    def ole_date(self) -> datetime:
        """The current time in OLE DATE Format."""
        with agmarshall.DATE_arg() as arg_pDate:
            agcls.evaluate_hresult(self.__dict__["_get_ole_date"](byref(arg_pDate.COM_val)))
            return arg_pDate.python_val

    @ole_date.setter
    def ole_date(self, inVal:datetime) -> None:
        with agmarshall.DATE_arg(inVal) as arg_inVal:
            agcls.evaluate_hresult(self.__dict__["_set_ole_date"](arg_inVal.COM_val))

    @property
    def whole_days(self) -> int:
        """The Julian Day Number of the date of interest."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_whole_days"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @whole_days.setter
    def whole_days(self, wholeDays:int) -> None:
        with agmarshall.LONG_arg(wholeDays) as arg_wholeDays:
            agcls.evaluate_hresult(self.__dict__["_set_whole_days"](arg_wholeDays.COM_val))

    @property
    def sec_into_day(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_sec_into_day"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @sec_into_day.setter
    def sec_into_day(self, secIntoDay:float) -> None:
        with agmarshall.DOUBLE_arg(secIntoDay) as arg_secIntoDay:
            agcls.evaluate_hresult(self.__dict__["_set_sec_into_day"](arg_secIntoDay.COM_val))

    @property
    def whole_days_utc(self) -> int:
        """The UTC Day Number of the date of interest."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_whole_days_utc"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @whole_days_utc.setter
    def whole_days_utc(self, wholeDays:int) -> None:
        with agmarshall.LONG_arg(wholeDays) as arg_wholeDays:
            agcls.evaluate_hresult(self.__dict__["_set_whole_days_utc"](arg_wholeDays.COM_val))

    @property
    def sec_into_day_utc(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0"""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_sec_into_day_utc"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @sec_into_day_utc.setter
    def sec_into_day_utc(self, secIntoDay:float) -> None:
        with agmarshall.DOUBLE_arg(secIntoDay) as arg_secIntoDay:
            agcls.evaluate_hresult(self.__dict__["_set_sec_into_day_utc"](arg_secIntoDay.COM_val))

    def add(self, unit:str, value:float) -> "IDate":
        """Adds the value in the given unit and returns a new date interface."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppDate:
            agcls.evaluate_hresult(self.__dict__["_add"](arg_unit.COM_val, arg_value.COM_val, byref(arg_ppDate.COM_val)))
            return arg_ppDate.python_val

    def subtract(self, unit:str, value:float) -> "IDate":
        """Subtracts the value in the given unit and returns a new date interface."""
        with agmarshall.BSTR_arg(unit) as arg_unit, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppDate:
            agcls.evaluate_hresult(self.__dict__["_subtract"](arg_unit.COM_val, arg_value.COM_val, byref(arg_ppDate.COM_val)))
            return arg_ppDate.python_val

    def span(self, date:"IDate") -> "IQuantity":
        """Subtracts the value from the IDate interface and returns an IAgQuantity."""
        with agmarshall.AgInterface_in_arg(date, IDate) as arg_date, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_span"](arg_date.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val


agcls.AgClassCatalog.add_catalog_entry("{BFC8EA09-19BD-432A-923D-C553E8E37993}", IDate)
agcls.AgTypeNameMap["IDate"] = IDate

class IConversionUtility(object):
    """Provides conversion utilities."""
    _uuid = "{2B04A4E2-C647-4920-88FF-DE0413252D1C}"
    _num_methods = 18
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_convert_quantity"] = _raise_uninitialized_error
        self.__dict__["_convert_date"] = _raise_uninitialized_error
        self.__dict__["_convert_quantity_array"] = _raise_uninitialized_error
        self.__dict__["_convert_date_array"] = _raise_uninitialized_error
        self.__dict__["_new_quantity"] = _raise_uninitialized_error
        self.__dict__["_new_date"] = _raise_uninitialized_error
        self.__dict__["_new_position_on_earth"] = _raise_uninitialized_error
        self.__dict__["_convert_position_array"] = _raise_uninitialized_error
        self.__dict__["_new_direction"] = _raise_uninitialized_error
        self.__dict__["_new_orientation"] = _raise_uninitialized_error
        self.__dict__["_new_orbit_state_on_earth"] = _raise_uninitialized_error
        self.__dict__["_new_position_on_cb"] = _raise_uninitialized_error
        self.__dict__["_new_orbit_state_on_cb"] = _raise_uninitialized_error
        self.__dict__["_query_direction_cosine_matrix"] = _raise_uninitialized_error
        self.__dict__["_query_direction_cosine_matrix_array"] = _raise_uninitialized_error
        self.__dict__["_new_cartesian3_vector"] = _raise_uninitialized_error
        self.__dict__["_new_cartesian3_vector_from_direction"] = _raise_uninitialized_error
        self.__dict__["_new_cartesian3_vector_from_position"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IConversionUtility._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IConversionUtility from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IConversionUtility = agcom.GUID(IConversionUtility._uuid)
        vtable_offset_local = IConversionUtility._vtable_offset - 1
        self.__dict__["_convert_quantity"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+1, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.DOUBLE))
        self.__dict__["_convert_date"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+2, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_convert_quantity_array"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+3, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.SAFEARRAY), POINTER(agcom.SAFEARRAY))
        self.__dict__["_convert_date_array"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+4, agcom.BSTR, agcom.BSTR, POINTER(agcom.SAFEARRAY), POINTER(agcom.SAFEARRAY))
        self.__dict__["_new_quantity"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+5, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID))
        self.__dict__["_new_date"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+6, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_new_position_on_earth"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+7, POINTER(agcom.PVOID))
        self.__dict__["_convert_position_array"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+8, agcom.LONG, POINTER(agcom.SAFEARRAY), agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_new_direction"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+9, POINTER(agcom.PVOID))
        self.__dict__["_new_orientation"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+10, POINTER(agcom.PVOID))
        self.__dict__["_new_orbit_state_on_earth"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+11, POINTER(agcom.PVOID))
        self.__dict__["_new_position_on_cb"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+12, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_new_orbit_state_on_cb"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+13, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_query_direction_cosine_matrix"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+14, agcom.PVOID, POINTER(agcom.PVOID), POINTER(agcom.PVOID), POINTER(agcom.PVOID))
        self.__dict__["_query_direction_cosine_matrix_array"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+15, agcom.PVOID, POINTER(agcom.SAFEARRAY))
        self.__dict__["_new_cartesian3_vector"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+16, POINTER(agcom.PVOID))
        self.__dict__["_new_cartesian3_vector_from_direction"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+17, agcom.PVOID, POINTER(agcom.PVOID))
        self.__dict__["_new_cartesian3_vector_from_position"] = IAGFUNCTYPE(pUnk, IID_IConversionUtility, vtable_offset_local+18, agcom.PVOID, POINTER(agcom.PVOID))
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
    
    def convert_quantity(self, dimensionName:str, fromUnit:str, toUnit:str, fromValue:float) -> float:
        """Converts the specified quantity value from a given unit to another unit."""
        with agmarshall.BSTR_arg(dimensionName) as arg_dimensionName, \
             agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.DOUBLE_arg(fromValue) as arg_fromValue, \
             agmarshall.DOUBLE_arg() as arg_pToValue:
            agcls.evaluate_hresult(self.__dict__["_convert_quantity"](arg_dimensionName.COM_val, arg_fromUnit.COM_val, arg_toUnit.COM_val, arg_fromValue.COM_val, byref(arg_pToValue.COM_val)))
            return arg_pToValue.python_val

    def convert_date(self, fromUnit:str, toUnit:str, fromValue:str) -> str:
        """Converts the specified date from a given unit to another unit."""
        with agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.BSTR_arg(fromValue) as arg_fromValue, \
             agmarshall.BSTR_arg() as arg_pToValue:
            agcls.evaluate_hresult(self.__dict__["_convert_date"](arg_fromUnit.COM_val, arg_toUnit.COM_val, arg_fromValue.COM_val, byref(arg_pToValue.COM_val)))
            return arg_pToValue.python_val

    def convert_quantity_array(self, dimensionName:str, fromUnit:str, toUnit:str, quantityValues:list) -> list:
        """Converts the specified quantity values from a given unit to another unit."""
        with agmarshall.BSTR_arg(dimensionName) as arg_dimensionName, \
             agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.SAFEARRAY_arg(quantityValues) as arg_quantityValues, \
             agmarshall.SAFEARRAY_arg() as arg_ppConvertedQuantityValues:
            agcls.evaluate_hresult(self.__dict__["_convert_quantity_array"](arg_dimensionName.COM_val, arg_fromUnit.COM_val, arg_toUnit.COM_val, byref(arg_quantityValues.COM_val), byref(arg_ppConvertedQuantityValues.COM_val)))
            return arg_ppConvertedQuantityValues.python_val

    def convert_date_array(self, fromUnit:str, toUnit:str, fromValues:list) -> list:
        """Converts the specified dates from a given unit to another unit."""
        with agmarshall.BSTR_arg(fromUnit) as arg_fromUnit, \
             agmarshall.BSTR_arg(toUnit) as arg_toUnit, \
             agmarshall.SAFEARRAY_arg(fromValues) as arg_fromValues, \
             agmarshall.SAFEARRAY_arg() as arg_ppConvertedDateValues:
            agcls.evaluate_hresult(self.__dict__["_convert_date_array"](arg_fromUnit.COM_val, arg_toUnit.COM_val, byref(arg_fromValues.COM_val), byref(arg_ppConvertedDateValues.COM_val)))
            return arg_ppConvertedDateValues.python_val

    def new_quantity(self, dimension:str, unitAbbrv:str, value:float) -> "IQuantity":
        """Creates an IQuantity interface with the given dimension, unit and value"""
        with agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppQuantity:
            agcls.evaluate_hresult(self.__dict__["_new_quantity"](arg_dimension.COM_val, arg_unitAbbrv.COM_val, arg_value.COM_val, byref(arg_ppQuantity.COM_val)))
            return arg_ppQuantity.python_val

    def new_date(self, unitAbbrv:str, value:str) -> "IDate":
        """Creates an IDate interface with the given unit and value"""
        with agmarshall.BSTR_arg(unitAbbrv) as arg_unitAbbrv, \
             agmarshall.BSTR_arg(value) as arg_value, \
             agmarshall.AgInterface_out_arg() as arg_ppDate:
            agcls.evaluate_hresult(self.__dict__["_new_date"](arg_unitAbbrv.COM_val, arg_value.COM_val, byref(arg_ppDate.COM_val)))
            return arg_ppDate.python_val

    def new_position_on_earth(self) -> "IPosition":
        """Creates an IPosition interface with earth as its central body."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_position_on_earth"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def convert_position_array(self, positionType:"POSITION_TYPE", positionArray:list, convertTo:"POSITION_TYPE") -> list:
        """Converts the specified position values from a given position type to another position type."""
        with agmarshall.AgEnum_arg(POSITION_TYPE, positionType) as arg_positionType, \
             agmarshall.SAFEARRAY_arg(positionArray) as arg_positionArray, \
             agmarshall.AgEnum_arg(POSITION_TYPE, convertTo) as arg_convertTo, \
             agmarshall.SAFEARRAY_arg() as arg_ppOutVal:
            agcls.evaluate_hresult(self.__dict__["_convert_position_array"](arg_positionType.COM_val, byref(arg_positionArray.COM_val), arg_convertTo.COM_val, byref(arg_ppOutVal.COM_val)))
            return arg_ppOutVal.python_val

    def new_direction(self) -> "IDirection":
        """Creates an IDirection interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_direction"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def new_orientation(self) -> "IOrientation":
        """Creates an IOrientation interface."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_orientation"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def new_orbit_state_on_earth(self) -> "IOrbitState":
        """Creates an IOrbitState interface with earth as its central body."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_orbit_state_on_earth"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def new_position_on_cb(self, centralBodyName:str) -> "IPosition":
        """Creates an IPosition interface using the supplied central body."""
        with agmarshall.BSTR_arg(centralBodyName) as arg_centralBodyName, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_position_on_cb"](arg_centralBodyName.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def new_orbit_state_on_cb(self, centralBodyName:str) -> "IOrbitState":
        """Creates an IOrbitState interface using the supplied central body."""
        with agmarshall.BSTR_arg(centralBodyName) as arg_centralBodyName, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_orbit_state_on_cb"](arg_centralBodyName.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def query_direction_cosine_matrix(self, inputOrientation:"IOrientation") -> typing.Tuple[ICartesian3Vector, ICartesian3Vector, ICartesian3Vector]:
        """Returns a Direction Cosine Matrix (DCM)."""
        with agmarshall.AgInterface_in_arg(inputOrientation, IOrientation) as arg_inputOrientation, \
             agmarshall.AgInterface_out_arg() as arg_px, \
             agmarshall.AgInterface_out_arg() as arg_py, \
             agmarshall.AgInterface_out_arg() as arg_pz:
            agcls.evaluate_hresult(self.__dict__["_query_direction_cosine_matrix"](arg_inputOrientation.COM_val, byref(arg_px.COM_val), byref(arg_py.COM_val), byref(arg_pz.COM_val)))
            return arg_px.python_val, arg_py.python_val, arg_pz.python_val

    def query_direction_cosine_matrix_array(self, inputOrientation:"IOrientation") -> list:
        """Returns a Direction Cosine Matrix (DCM) as an array."""
        with agmarshall.AgInterface_in_arg(inputOrientation, IOrientation) as arg_inputOrientation, \
             agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_query_direction_cosine_matrix_array"](arg_inputOrientation.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def new_cartesian3_vector(self) -> "ICartesian3Vector":
        """Creates a cartesian vector."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_cartesian3_vector"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def new_cartesian3_vector_from_direction(self, inputDirection:"IDirection") -> "ICartesian3Vector":
        """Converts the direction to cartesian vector."""
        with agmarshall.AgInterface_in_arg(inputDirection, IDirection) as arg_inputDirection, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_cartesian3_vector_from_direction"](arg_inputDirection.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def new_cartesian3_vector_from_position(self, inputPosition:"IPosition") -> "ICartesian3Vector":
        """Converts the position to cartesian vector."""
        with agmarshall.AgInterface_in_arg(inputPosition, IPosition) as arg_inputPosition, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_new_cartesian3_vector_from_position"](arg_inputPosition.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{2B04A4E2-C647-4920-88FF-DE0413252D1C}", IConversionUtility)
agcls.AgTypeNameMap["IConversionUtility"] = IConversionUtility

class IDoublesCollection(object):
    """Represents a collection of doubles."""
    _uuid = "{DEE2EB74-C19C-44C9-8825-09010A8F60BE}"
    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_add"] = _raise_uninitialized_error
        self.__dict__["_remove_at"] = _raise_uninitialized_error
        self.__dict__["_remove_all"] = _raise_uninitialized_error
        self.__dict__["_to_array"] = _raise_uninitialized_error
        self.__dict__["_set_at"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDoublesCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDoublesCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IDoublesCollection = agcom.GUID(IDoublesCollection._uuid)
        vtable_offset_local = IDoublesCollection._vtable_offset - 1
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+1, agcom.LONG, POINTER(agcom.DOUBLE))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_add"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_remove_at"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+5, agcom.LONG)
        self.__dict__["_remove_all"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+6, )
        self.__dict__["_to_array"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+7, POINTER(agcom.SAFEARRAY))
        self.__dict__["_set_at"] = IAGFUNCTYPE(pUnk, IID_IDoublesCollection, vtable_offset_local+8, agcom.LONG, agcom.DOUBLE)
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> float:
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    def item(self, index:int) -> float:
        """Returns a double at a specified position."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def count(self) -> int:
        """Returns the number of items in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns a collection enumerator."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def add(self, value:float) -> None:
        """Add a value to the collection of doubles."""
        with agmarshall.DOUBLE_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_add"](arg_value.COM_val))

    def remove_at(self, index:int) -> None:
        """Remove an element from the collection at a specified position."""
        with agmarshall.LONG_arg(index) as arg_index:
            agcls.evaluate_hresult(self.__dict__["_remove_at"](arg_index.COM_val))

    def remove_all(self) -> None:
        """Clears the collection."""
        agcls.evaluate_hresult(self.__dict__["_remove_all"]())

    def to_array(self) -> list:
        """Returns an array of the elements in the collection"""
        with agmarshall.SAFEARRAY_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_to_array"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def set_at(self, index:int, value:float) -> None:
        """Updates an element in the collection at a specified position."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.DOUBLE_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_set_at"](arg_index.COM_val, arg_value.COM_val))

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{DEE2EB74-C19C-44C9-8825-09010A8F60BE}", IDoublesCollection)
agcls.AgTypeNameMap["IDoublesCollection"] = IDoublesCollection



class ExecCmdResult(IExecCmdResult):
    """Collection of strings returned by the ExecuteCommand."""
    def __init__(self, sourceObject=None):
        IExecCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IExecCmdResult._private_init(self, pUnk)
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


class ExecMultiCmdResult(IExecMultiCmdResult):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    def __init__(self, sourceObject=None):
        IExecMultiCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IExecMultiCmdResult._private_init(self, pUnk)
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


class UnitPreferencesUnit(IUnitPreferencesUnit):
    """Object that contains info on the unit."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesUnit.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUnitPreferencesUnit._private_init(self, pUnk)
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


class UnitPreferencesUnitCollection(IUnitPreferencesUnitCollection):
    """Object that contains a collection of IUnitPreferencesUnit."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesUnitCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUnitPreferencesUnitCollection._private_init(self, pUnk)
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


class UnitPreferencesDimension(IUnitPreferencesDimension):
    """Object that contains info on the Dimension."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesDimension.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUnitPreferencesDimension._private_init(self, pUnk)
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


class UnitPreferencesDimensionCollection(IUnitPreferencesDimensionCollection):
    """Object that contains a collection of dimensions."""
    def __init__(self, sourceObject=None):
        IUnitPreferencesDimensionCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUnitPreferencesDimensionCollection._private_init(self, pUnk)
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


class ConversionUtility(IConversionUtility):
    """Object that contains a unit conversion utility."""
    def __init__(self, sourceObject=None):
        IConversionUtility.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IConversionUtility._private_init(self, pUnk)
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


class Quantity(IQuantity):
    """Object that contains a quantity."""
    def __init__(self, sourceObject=None):
        IQuantity.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IQuantity._private_init(self, pUnk)
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


class Date(IDate):
    """Object that contains a date."""
    def __init__(self, sourceObject=None):
        IDate.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDate._private_init(self, pUnk)
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


class Position(ILocationData, IPosition):
    """The Position class."""
    def __init__(self, sourceObject=None):
        ILocationData.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ILocationData._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Cartesian(ICartesian, IPosition):
    """Class used to access a position using Cartesian Coordinates."""
    def __init__(self, sourceObject=None):
        ICartesian.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ICartesian._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Geodetic(IGeodetic, IPosition):
    """Class defining Geodetic position."""
    def __init__(self, sourceObject=None):
        IGeodetic.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IGeodetic._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Geocentric(IGeocentric, IPosition):
    """Class defining Geocentric position."""
    def __init__(self, sourceObject=None):
        IGeocentric.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IGeocentric._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Planetodetic(IPlanetodetic, IPosition):
    """Class defining Planetodetic position."""
    def __init__(self, sourceObject=None):
        IPlanetodetic.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPlanetodetic._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Planetocentric(IPlanetocentric, IPosition):
    """Class defining Planetocentric position."""
    def __init__(self, sourceObject=None):
        IPlanetocentric.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPlanetocentric._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Spherical(ISpherical, IPosition):
    """Class defining spherical position."""
    def __init__(self, sourceObject=None):
        ISpherical.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ISpherical._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Cylindrical(ICylindrical, IPosition):
    """Class defining cylindrical position."""
    def __init__(self, sourceObject=None):
        ICylindrical.__init__(self, sourceObject)
        IPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ICylindrical._private_init(self, pUnk)
        IPosition._private_init(self, pUnk)
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


class Direction(IDirection):
    """Class defining direction options for aligned and constrained vectors."""
    def __init__(self, sourceObject=None):
        IDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirection._private_init(self, pUnk)
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


class DirectionEuler(IDirectionEuler, IDirection):
    """Euler direction sequence."""
    def __init__(self, sourceObject=None):
        IDirectionEuler.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirectionEuler._private_init(self, pUnk)
        IDirection._private_init(self, pUnk)
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


class DirectionPR(IDirectionPR, IDirection):
    """Pitch-Roll (PR) direction sequence."""
    def __init__(self, sourceObject=None):
        IDirectionPR.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirectionPR._private_init(self, pUnk)
        IDirection._private_init(self, pUnk)
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


class DirectionRADec(IDirectionRADec, IDirection):
    """Spherical direction (Right Ascension and Declination)."""
    def __init__(self, sourceObject=None):
        IDirectionRADec.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirectionRADec._private_init(self, pUnk)
        IDirection._private_init(self, pUnk)
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


class DirectionXYZ(IDirectionXYZ, IDirection):
    """Cartesian direction."""
    def __init__(self, sourceObject=None):
        IDirectionXYZ.__init__(self, sourceObject)
        IDirection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDirectionXYZ._private_init(self, pUnk)
        IDirection._private_init(self, pUnk)
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


class Orientation(IOrientation):
    """Class defining the orientation of an orbit."""
    def __init__(self, sourceObject=None):
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientation._private_init(self, pUnk)
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


class OrientationAzEl(IOrientationAzEl, IOrientation):
    """AzEl orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationAzEl.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationAzEl._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
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


class OrientationEulerAngles(IOrientationEulerAngles, IOrientation):
    """Euler Angles orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationEulerAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationEulerAngles._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
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


class OrientationQuaternion(IOrientationQuaternion, IOrientation):
    """Quaternion orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationQuaternion.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationQuaternion._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
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


class OrientationYPRAngles(IOrientationYPRAngles, IOrientation):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, sourceObject=None):
        IOrientationYPRAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationYPRAngles._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
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


class DoublesCollection(IDoublesCollection):
    """A collection of doubles."""
    def __init__(self, sourceObject=None):
        IDoublesCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDoublesCollection._private_init(self, pUnk)
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


class Cartesian3Vector(ICartesian3Vector):
    """A 3-D cartesian vector."""
    def __init__(self, sourceObject=None):
        ICartesian3Vector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ICartesian3Vector._private_init(self, pUnk)
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


class Cartesian2Vector(ICartesian2Vector):
    """A 2-D cartesian vector."""
    def __init__(self, sourceObject=None):
        ICartesian2Vector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ICartesian2Vector._private_init(self, pUnk)
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


class PropertyInfo(IPropertyInfo):
    """Property Information coclass."""
    def __init__(self, sourceObject=None):
        IPropertyInfo.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPropertyInfo._private_init(self, pUnk)
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


class PropertyInfoCollection(IPropertyInfoCollection):
    """Property Information Collection coclass."""
    def __init__(self, sourceObject=None):
        IPropertyInfoCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPropertyInfoCollection._private_init(self, pUnk)
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


class RuntimeTypeInfo(IRuntimeTypeInfo):
    """Runtime Type info coclass."""
    def __init__(self, sourceObject=None):
        IRuntimeTypeInfo.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IRuntimeTypeInfo._private_init(self, pUnk)
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


class CROrientationAzEl(IOrientationAzEl, IOrientation, IOrientationPositionOffset):
    """AzEl orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationAzEl.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationAzEl._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
        IOrientationPositionOffset._private_init(self, pUnk)
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


class CROrientationEulerAngles(IOrientationEulerAngles, IOrientation, IOrientationPositionOffset):
    """Euler Angles orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationEulerAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationEulerAngles._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
        IOrientationPositionOffset._private_init(self, pUnk)
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


class CROrientationQuaternion(IOrientationQuaternion, IOrientation, IOrientationPositionOffset):
    """Quaternion orientation method."""
    def __init__(self, sourceObject=None):
        IOrientationQuaternion.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationQuaternion._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
        IOrientationPositionOffset._private_init(self, pUnk)
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


class CROrientationYPRAngles(IOrientationYPRAngles, IOrientation, IOrientationPositionOffset):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, sourceObject=None):
        IOrientationYPRAngles.__init__(self, sourceObject)
        IOrientation.__init__(self, sourceObject)
        IOrientationPositionOffset.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IOrientationYPRAngles._private_init(self, pUnk)
        IOrientation._private_init(self, pUnk)
        IOrientationPositionOffset._private_init(self, pUnk)
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


class CROrientationOffsetCart(ICartesian3Vector):
    """Orientation offset cartesian."""
    def __init__(self, sourceObject=None):
        ICartesian3Vector.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ICartesian3Vector._private_init(self, pUnk)
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



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
