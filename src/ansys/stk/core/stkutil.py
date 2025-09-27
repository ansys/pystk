# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Objects and enumerations shared by the STK X and STK Objects libraries.

The
types provided by STK Util are used indirectly through methods and properties
in the STK X and STK Objects libraries.
"""

__all__ = ["AzElAboutBoresight", "Cartesian", "Cartesian2Vector", "Cartesian3Vector", "CommRadOrientationAzEl",
"CommRadOrientationEulerAngles", "CommRadOrientationOffsetCart", "CommRadOrientationQuaternion",
"CommRadOrientationYPRAngles", "ConversionUtility", "CoordinateSystem", "Cylindrical", "Date", "Direction",
"DirectionEuler", "DirectionPR", "DirectionRADec", "DirectionType", "DirectionXYZ", "DoublesCollection",
"EulerDirectionSequence", "EulerOrientationSequenceType", "ExecuteCommandResult", "ExecuteMultipleCommandsMode",
"ExecuteMultipleCommandsResult", "FillStyle", "Geocentric", "Geodetic", "ICartesian3Vector", "IDirection",
"ILocationData", "IOrbitState", "IOrientation", "IOrientationAzEl", "IOrientationEulerAngles",
"IOrientationPositionOffset", "IOrientationQuaternion", "IOrientationYPRAngles", "IPosition",
"IRuntimeTypeInfoProvider", "LineStyle", "LogMessageDisplayID", "LogMessageType", "OrbitStateType", "Orientation",
"OrientationAzEl", "OrientationEulerAngles", "OrientationQuaternion", "OrientationType", "OrientationYPRAngles",
"PRSequence", "Planetocentric", "Planetodetic", "Position", "PositionType", "PropertyInfo", "PropertyInfoCollection",
"PropertyInfoValueType", "Quantity", "RuntimeTypeInfo", "Spherical", "UnitPreferencesDimension",
"UnitPreferencesDimensionCollection", "UnitPreferencesUnit", "UnitPreferencesUnitCollection", "YPRAnglesSequence"]

from ctypes import POINTER
from datetime import datetime
from enum import IntEnum, IntFlag
import typing

from .internal import coclassutil as agcls, comutil as agcom, marshall as agmarshall
from .internal.apiutil import (
    EnumeratorProxy,
    InterfaceProxy,
    OutArg,
    SupportsDeleteCallback,
    get_interface_property,
    initialize_from_source_object,
    set_class_attribute,
    set_interface_attribute,
)
from .internal.comutil import IDispatch, IUnknown


class PositionType(IntEnum):
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

PositionType.CARTESIAN.__doc__ = "Cartesian: position specified in terms of the X, Y and Z components of the object's position vector, where the Z-axis points to the North pole, and the X-axis crosses 0 degrees latitude/0 degrees longitude."
PositionType.CYLINDRICAL.__doc__ = "Cylindrical: position specified in terms of radius (polar), longitude (measured in degrees from -360.0 degrees to +360.0 degrees), and the Z component of the object's position vector."
PositionType.GEOCENTRIC.__doc__ = "Geocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude."
PositionType.GEODETIC.__doc__ = "Geodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude."
PositionType.SPHERICAL.__doc__ = "Spherical: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and radius (distance of the object from the center of the Earth)."
PositionType.PLANETOCENTRIC.__doc__ = "Planetocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude."
PositionType.PLANETODETIC.__doc__ = "Planetodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude."

agcls.AgTypeNameMap["PositionType"] = PositionType

class EulerDirectionSequence(IntEnum):
    """Euler direction sequences."""

    SEQUENCE_12 = 0
    """12 sequence."""
    SEQUENCE_21 = 1
    """21 sequence."""
    SEQUENCE_31 = 2
    """31 sequence."""
    SEQUENCE_32 = 3
    """32 sequence."""

EulerDirectionSequence.SEQUENCE_12.__doc__ = "12 sequence."
EulerDirectionSequence.SEQUENCE_21.__doc__ = "21 sequence."
EulerDirectionSequence.SEQUENCE_31.__doc__ = "31 sequence."
EulerDirectionSequence.SEQUENCE_32.__doc__ = "32 sequence."

agcls.AgTypeNameMap["EulerDirectionSequence"] = EulerDirectionSequence

class DirectionType(IntEnum):
    """Direction options for aligned and constrained vectors."""

    EULER = 0
    """Euler B and C angles."""
    PR = 1
    """Pitch and Roll angles."""
    RA_DEC = 2
    """Spherical elements: Right Ascension and Declination."""
    XYZ = 3
    """Cartesian elements."""

DirectionType.EULER.__doc__ = "Euler B and C angles."
DirectionType.PR.__doc__ = "Pitch and Roll angles."
DirectionType.RA_DEC.__doc__ = "Spherical elements: Right Ascension and Declination."
DirectionType.XYZ.__doc__ = "Cartesian elements."

agcls.AgTypeNameMap["DirectionType"] = DirectionType

class PRSequence(IntEnum):
    """Pitch-Roll (PR) direction sequences."""

    PR = 0
    """PR sequence."""

PRSequence.PR.__doc__ = "PR sequence."

agcls.AgTypeNameMap["PRSequence"] = PRSequence

class OrientationType(IntEnum):
    """Orientation methods."""

    AZ_EL = 0
    """AzEl (azimuth-elevation) method."""
    EULER_ANGLES = 1
    """Euler angles method."""
    QUATERNION = 2
    """Quaternion method."""
    YPR_ANGLES = 3
    """YPR (yaw-pitch-roll) method."""

OrientationType.AZ_EL.__doc__ = "AzEl (azimuth-elevation) method."
OrientationType.EULER_ANGLES.__doc__ = "Euler angles method."
OrientationType.QUATERNION.__doc__ = "Quaternion method."
OrientationType.YPR_ANGLES.__doc__ = "YPR (yaw-pitch-roll) method."

agcls.AgTypeNameMap["OrientationType"] = OrientationType

class AzElAboutBoresight(IntEnum):
    """About Boresight options for AzEl orientation method."""

    HOLD = 0
    """Hold: rotation about the Y axis followed by rotation about the new X-axis."""
    ROTATE = 1
    """Rotate: rotation about the sensor's or antenna's Z axis by the azimuth angle, followed by rotation about the new Y axis by 90 degrees minus the elevation angle."""

AzElAboutBoresight.HOLD.__doc__ = "Hold: rotation about the Y axis followed by rotation about the new X-axis."
AzElAboutBoresight.ROTATE.__doc__ = "Rotate: rotation about the sensor's or antenna's Z axis by the azimuth angle, followed by rotation about the new Y axis by 90 degrees minus the elevation angle."

agcls.AgTypeNameMap["AzElAboutBoresight"] = AzElAboutBoresight

class EulerOrientationSequenceType(IntEnum):
    """Euler rotation sequence options:."""

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

EulerOrientationSequenceType.SEQUENCE_121.__doc__ = "121 rotation."
EulerOrientationSequenceType.SEQUENCE_123.__doc__ = "123 rotation."
EulerOrientationSequenceType.SEQUENCE_131.__doc__ = "131 rotation."
EulerOrientationSequenceType.SEQUENCE_132.__doc__ = "132 rotation."
EulerOrientationSequenceType.SEQUENCE_212.__doc__ = "212 rotation."
EulerOrientationSequenceType.SEQUENCE_213.__doc__ = "213 rotation."
EulerOrientationSequenceType.SEQUENCE_231.__doc__ = "231 rotation."
EulerOrientationSequenceType.SEQUENCE_232.__doc__ = "232 rotation."
EulerOrientationSequenceType.SEQUENCE_312.__doc__ = "312 rotation."
EulerOrientationSequenceType.SEQUENCE_313.__doc__ = "313 rotation."
EulerOrientationSequenceType.SEQUENCE_321.__doc__ = "321 rotation."
EulerOrientationSequenceType.SEQUENCE_323.__doc__ = "323 rotation."

agcls.AgTypeNameMap["EulerOrientationSequenceType"] = EulerOrientationSequenceType

class YPRAnglesSequence(IntEnum):
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

YPRAnglesSequence.PRY.__doc__ = "PRY sequence."
YPRAnglesSequence.PYR.__doc__ = "PYR sequence."
YPRAnglesSequence.RPY.__doc__ = "RPY sequence."
YPRAnglesSequence.RYP.__doc__ = "RYP sequence."
YPRAnglesSequence.YPR.__doc__ = "YPR sequence."
YPRAnglesSequence.YRP.__doc__ = "YRP sequence."

agcls.AgTypeNameMap["YPRAnglesSequence"] = YPRAnglesSequence

class OrbitStateType(IntEnum):
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

OrbitStateType.CARTESIAN.__doc__ = "Cartesian coordinate type."
OrbitStateType.CLASSICAL.__doc__ = "Classical (Keplerian) coordinate type."
OrbitStateType.EQUINOCTIAL.__doc__ = "Equinoctial coordinate type."
OrbitStateType.DELAUNAY.__doc__ = "Delaunay variables coordinate type."
OrbitStateType.SPHERICAL.__doc__ = "Spherical coordinate type."
OrbitStateType.MIXED_SPHERICAL.__doc__ = "Mixed spherical coordinate type."
OrbitStateType.GEODETIC.__doc__ = "Geodetic coordinate type."

agcls.AgTypeNameMap["OrbitStateType"] = OrbitStateType

class CoordinateSystem(IntEnum):
    """Earth-centered coordinate systems for defining certain propagators."""

    UNKNOWN = -1
    """Represents coordinate system not supported by the Object Model."""
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
    """Mean Earth."""
    FIXED_NO_LIBRATION = 14
    """uses an analytic formula not modeling lunar libration."""
    FIXED_IAU2003 = 15
    """Fixed_IAU2003."""
    PRINCIPAL_AXES421 = 16
    """PrincipalAxes_421."""
    PRINCIPAL_AXES403 = 17
    """PrincipalAxes_403."""
    INERTIAL = 18
    """Inertial."""
    J2000_ECLIPTIC = 19
    """The mean ecliptic system evaluated at the J2000 epoch. The mean ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the mean obliquity defined using FK5 IAU76 theory."""
    TRUE_ECLIPTIC_OF_DATE = 21
    """The true ecliptic system, evaluated at each given time. The true ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the true obliquity defined using FK5 IAU76 theory."""
    PRINCIPAL_AXES430 = 22
    """PrincipalAxes_430."""
    TRUE_OF_DATE_ROTATING = 23
    """TrueOfDateRotating: Like the Fixed system, but ignores pole wander. The XY plane is the same as the XY plane of the TrueOfDate system, and the system rotates about the TrueOfDate Z-axis."""
    ECLIPTIC_J2000ICRF = 24
    """EclipticJ2000ICRF: An ecliptic system that is a fixed offset of the ICRF system, found by rotating the ICRF system about its X-axis by the mean obliquity at the J2000 epoch (i.e., 84381.448 arcSecs). The ecliptic plane is the XY-plane of this system."""

CoordinateSystem.UNKNOWN.__doc__ = "Represents coordinate system not supported by the Object Model."
CoordinateSystem.ALIGNMENT_AT_EPOCH.__doc__ = "Alignment at Epoch: an inertial system coincident with ECF at the Coord Epoch. Often used to specify launch trajectories."
CoordinateSystem.B1950.__doc__ = "B1950: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the beginning of the Besselian year 1950 and corresponds to 31 December 1949 22:09:07.2 or JD 2433282.423."
CoordinateSystem.FIXED.__doc__ = "Fixed: X is fixed at 0 deg longitude, Y is fixed at 90 deg longitude, and Z is directed toward the north pole."
CoordinateSystem.J2000.__doc__ = "J2000: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth on 1 Jan 2000 at 12:00:00.00 TDB, which corresponds to JD 2451545.0 TDB."
CoordinateSystem.MEAN_OF_DATE.__doc__ = "Mean of Date: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Orbit Epoch."
CoordinateSystem.MEAN_OF_EPOCH.__doc__ = "Mean of Epoch: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Coord Epoch."
CoordinateSystem.TEME_OF_DATE.__doc__ = "TEME of Date: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch."
CoordinateSystem.TEME_OF_EPOCH.__doc__ = "TEME of Epoch: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch."
CoordinateSystem.TRUE_OF_DATE.__doc__ = "True of Date: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch."
CoordinateSystem.TRUE_OF_EPOCH.__doc__ = "True of Epoch: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch."
CoordinateSystem.TRUE_OF_REFERENCE_DATE.__doc__ = "True of Ref Date: A special case of True of Epoch. Instead of the Coord Epoch, this system uses a Reference Date defined in the Integration Control page of the scenario's PODS properties."
CoordinateSystem.ICRF.__doc__ = "ICRF: International Celestial Reference Frame."
CoordinateSystem.MEAN_EARTH.__doc__ = "Mean Earth."
CoordinateSystem.FIXED_NO_LIBRATION.__doc__ = "uses an analytic formula not modeling lunar libration."
CoordinateSystem.FIXED_IAU2003.__doc__ = "Fixed_IAU2003."
CoordinateSystem.PRINCIPAL_AXES421.__doc__ = "PrincipalAxes_421."
CoordinateSystem.PRINCIPAL_AXES403.__doc__ = "PrincipalAxes_403."
CoordinateSystem.INERTIAL.__doc__ = "Inertial."
CoordinateSystem.J2000_ECLIPTIC.__doc__ = "The mean ecliptic system evaluated at the J2000 epoch. The mean ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the mean obliquity defined using FK5 IAU76 theory."
CoordinateSystem.TRUE_ECLIPTIC_OF_DATE.__doc__ = "The true ecliptic system, evaluated at each given time. The true ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the true obliquity defined using FK5 IAU76 theory."
CoordinateSystem.PRINCIPAL_AXES430.__doc__ = "PrincipalAxes_430."
CoordinateSystem.TRUE_OF_DATE_ROTATING.__doc__ = "TrueOfDateRotating: Like the Fixed system, but ignores pole wander. The XY plane is the same as the XY plane of the TrueOfDate system, and the system rotates about the TrueOfDate Z-axis."
CoordinateSystem.ECLIPTIC_J2000ICRF.__doc__ = "EclipticJ2000ICRF: An ecliptic system that is a fixed offset of the ICRF system, found by rotating the ICRF system about its X-axis by the mean obliquity at the J2000 epoch (i.e., 84381.448 arcSecs). The ecliptic plane is the XY-plane of this system."

agcls.AgTypeNameMap["CoordinateSystem"] = CoordinateSystem

class LogMessageType(IntEnum):
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

LogMessageType.DEBUG.__doc__ = "Debugging message."
LogMessageType.INFO.__doc__ = "Informational message."
LogMessageType.FORCE_INFO.__doc__ = "Informational message."
LogMessageType.WARNING.__doc__ = "Warning message."
LogMessageType.ALARM.__doc__ = "Alarm message."

agcls.AgTypeNameMap["LogMessageType"] = LogMessageType

class LogMessageDisplayID(IntEnum):
    """Log message destination options."""

    ALL = -1
    """STK displays the message in all the log destination."""
    DEFAULT = 0
    """STK displays the message in the default log destination."""
    MESSAGE_WINDOW = 1
    """STK displays the message in the message window."""
    STATUS_BAR = 2
    """STK displays the message in the status bar."""

LogMessageDisplayID.ALL.__doc__ = "STK displays the message in all the log destination."
LogMessageDisplayID.DEFAULT.__doc__ = "STK displays the message in the default log destination."
LogMessageDisplayID.MESSAGE_WINDOW.__doc__ = "STK displays the message in the message window."
LogMessageDisplayID.STATUS_BAR.__doc__ = "STK displays the message in the status bar."

agcls.AgTypeNameMap["LogMessageDisplayID"] = LogMessageDisplayID

class LineStyle(IntEnum):
    """Line Style."""

    SOLID = 0
    """Specify a solid line."""
    DASHED = 1
    """Specify a dashed line."""
    DOTTED = 2
    """Specify a dotted line."""
    DOT_DASHED = 3
    """Dot-dashed line."""
    LONG_DASHED = 4
    """Specify a long dashed line."""
    DASH_DOT_DOTTED = 5
    """Specify an alternating dash-dot-dot line."""
    M_DASH = 6
    """Specify a user configurable medium dashed line."""
    L_DASH = 7
    """Specify a user configurable long dashed line."""
    S_DASH_DOT = 8
    """Specify a user configurable small dash-dotted line."""
    M_DASH_DOT = 9
    """Specify a user configurable medium dash-dotted line."""
    DASH_DOT = 10
    """Specify a user configurable long dash-dotted line."""
    MS_DASH = 11
    """Specify a user configurable medium followed by small dashed line."""
    LS_DASH = 12
    """Specify a user configurable long followed by small dashed line."""
    LM_DASH = 13
    """Specify a user configurable long followed by medium dashed line."""
    LMS_DASH = 14
    """Specify a user configurable medium followed by small dashed line."""
    DOT = 15
    """Specify a dotted line."""
    LONG_DASH = 16
    """Specify a long dashed line."""
    S_DASH = 17
    """Specify an alternating dash-dot line."""

LineStyle.SOLID.__doc__ = "Specify a solid line."
LineStyle.DASHED.__doc__ = "Specify a dashed line."
LineStyle.DOTTED.__doc__ = "Specify a dotted line."
LineStyle.DOT_DASHED.__doc__ = "Dot-dashed line."
LineStyle.LONG_DASHED.__doc__ = "Specify a long dashed line."
LineStyle.DASH_DOT_DOTTED.__doc__ = "Specify an alternating dash-dot-dot line."
LineStyle.M_DASH.__doc__ = "Specify a user configurable medium dashed line."
LineStyle.L_DASH.__doc__ = "Specify a user configurable long dashed line."
LineStyle.S_DASH_DOT.__doc__ = "Specify a user configurable small dash-dotted line."
LineStyle.M_DASH_DOT.__doc__ = "Specify a user configurable medium dash-dotted line."
LineStyle.DASH_DOT.__doc__ = "Specify a user configurable long dash-dotted line."
LineStyle.MS_DASH.__doc__ = "Specify a user configurable medium followed by small dashed line."
LineStyle.LS_DASH.__doc__ = "Specify a user configurable long followed by small dashed line."
LineStyle.LM_DASH.__doc__ = "Specify a user configurable long followed by medium dashed line."
LineStyle.LMS_DASH.__doc__ = "Specify a user configurable medium followed by small dashed line."
LineStyle.DOT.__doc__ = "Specify a dotted line."
LineStyle.LONG_DASH.__doc__ = "Specify a long dashed line."
LineStyle.S_DASH.__doc__ = "Specify an alternating dash-dot line."

agcls.AgTypeNameMap["LineStyle"] = LineStyle

class ExecuteMultipleCommandsMode(IntFlag):
    """Enumeration defines a set of actions when an error occurs while executing a command batch."""

    CONTINUE_ON_ERROR = 0
    """Continue executing the remaining commands in the command batch."""
    STOP_ON_ERROR = 1
    """Terminate the execution of the command batch but do not throw an exception."""
    EXCEPTION_ON_ERROR = 2
    """Terminate the execution of the command batch and throw an exception."""
    DISCARD_RESULTS = 0x8000
    """Ignore results returned by individual commands. The option must be used in combination with other flags."""

ExecuteMultipleCommandsMode.CONTINUE_ON_ERROR.__doc__ = "Continue executing the remaining commands in the command batch."
ExecuteMultipleCommandsMode.STOP_ON_ERROR.__doc__ = "Terminate the execution of the command batch but do not throw an exception."
ExecuteMultipleCommandsMode.EXCEPTION_ON_ERROR.__doc__ = "Terminate the execution of the command batch and throw an exception."
ExecuteMultipleCommandsMode.DISCARD_RESULTS.__doc__ = "Ignore results returned by individual commands. The option must be used in combination with other flags."

agcls.AgTypeNameMap["ExecuteMultipleCommandsMode"] = ExecuteMultipleCommandsMode

class FillStyle(IntEnum):
    """Fill Style."""

    SOLID = 0
    """Specify a solid fill style."""
    HORIZONTAL_STRIPE = 1
    """Specify a horizontally striped fill style."""
    DIAGONAL_STRIPE1 = 2
    """Specify a diagonally striped fill style."""
    DIAGONAL_STRIPE2 = 3
    """Specify a diagonally striped fill style."""
    HATCH = 4
    """Specify a hatched fill style."""
    DIAGONAL_HATCH = 5
    """Specify a diagonally hatched fill style."""
    SCREEN = 6
    """Specify a special fill style where every other pixel is drawn."""
    VERTICAL_STRIPE = 7
    """Specify a vertically striped fill style."""

FillStyle.SOLID.__doc__ = "Specify a solid fill style."
FillStyle.HORIZONTAL_STRIPE.__doc__ = "Specify a horizontally striped fill style."
FillStyle.DIAGONAL_STRIPE1.__doc__ = "Specify a diagonally striped fill style."
FillStyle.DIAGONAL_STRIPE2.__doc__ = "Specify a diagonally striped fill style."
FillStyle.HATCH.__doc__ = "Specify a hatched fill style."
FillStyle.DIAGONAL_HATCH.__doc__ = "Specify a diagonally hatched fill style."
FillStyle.SCREEN.__doc__ = "Specify a special fill style where every other pixel is drawn."
FillStyle.VERTICAL_STRIPE.__doc__ = "Specify a vertically striped fill style."

agcls.AgTypeNameMap["FillStyle"] = FillStyle

class PropertyInfoValueType(IntEnum):
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

PropertyInfoValueType.INT.__doc__ = "Property is of type int."
PropertyInfoValueType.REAL.__doc__ = "Property is of type real."
PropertyInfoValueType.QUANTITY.__doc__ = "Property is of type Quantity."
PropertyInfoValueType.DATE.__doc__ = "Property is of type Date."
PropertyInfoValueType.STRING.__doc__ = "Property is of type string."
PropertyInfoValueType.BOOL.__doc__ = "Property is of type bool."
PropertyInfoValueType.INTERFACE.__doc__ = "Property is an interface."

agcls.AgTypeNameMap["PropertyInfoValueType"] = PropertyInfoValueType


class ILocationData(object):
    """Base interface ILocationData. IPosition derives from this interface."""

    _num_methods = 0
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "iid_data" : (5072494462713693543, 17287417281374770098),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type ILocationData."""
        initialize_from_source_object(self, source_object, ILocationData)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, ILocationData)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, ILocationData, None)



agcls.AgClassCatalog.add_catalog_entry((5072494462713693543, 17287417281374770098), ILocationData)
agcls.AgTypeNameMap["ILocationData"] = ILocationData

class IPosition(object):
    """IPosition provides access to the position of the object."""

    _num_methods = 21
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _convert_to_method_offset = 1
    _get_position_type_method_offset = 2
    _assign_method_offset = 3
    _assign_geocentric_method_offset = 4
    _assign_geodetic_method_offset = 5
    _assign_spherical_method_offset = 6
    _assign_cylindrical_method_offset = 7
    _assign_cartesian_method_offset = 8
    _assign_planetocentric_method_offset = 9
    _assign_planetodetic_method_offset = 10
    _query_planetocentric_method_offset = 11
    _query_planetodetic_method_offset = 12
    _query_spherical_method_offset = 13
    _query_cylindrical_method_offset = 14
    _query_cartesian_method_offset = 15
    _get_central_body_name_method_offset = 16
    _query_planetocentric_array_method_offset = 17
    _query_planetodetic_array_method_offset = 18
    _query_spherical_array_method_offset = 19
    _query_cylindrical_array_method_offset = 20
    _query_cartesian_array_method_offset = 21
    _metadata = {
        "iid_data" : (4915275008665419291, 11705930105741336507),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IPosition."""
        initialize_from_source_object(self, source_object, IPosition)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IPosition)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IPosition, None)

    _convert_to_metadata = { "offset" : _convert_to_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(PositionType), agmarshall.InterfaceOutArg,) }
    def convert_to(self, type:"PositionType") -> "IPosition":
        """Change the position coordinates to type specified."""
        return self._intf.invoke(IPosition._metadata, IPosition._convert_to_metadata, type, OutArg())

    _get_position_type_metadata = { "offset" : _get_position_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(PositionType),) }
    @property
    def position_type(self) -> "PositionType":
        """Get the type of position currently being used."""
        return self._intf.get_property(IPosition._metadata, IPosition._get_position_type_metadata)

    _assign_metadata = { "offset" : _assign_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IPosition"),) }
    def assign(self, position:"IPosition") -> None:
        """Assign the coordinates into the system."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_metadata, position)

    _assign_geocentric_metadata = { "offset" : _assign_geocentric_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def assign_geocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Assign the position using the Geocentric representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_geocentric_metadata, lat, lon, alt)

    _assign_geodetic_metadata = { "offset" : _assign_geodetic_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def assign_geodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Assign the position using the Geodetic representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_geodetic_metadata, lat, lon, alt)

    _assign_spherical_metadata = { "offset" : _assign_spherical_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def assign_spherical(self, lat:typing.Any, lon:typing.Any, radius:float) -> None:
        """Assign the position using the Spherical representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_spherical_metadata, lat, lon, radius)

    _assign_cylindrical_metadata = { "offset" : _assign_cylindrical_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.Variant,),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.VariantArg,) }
    def assign_cylindrical(self, radius:float, z:float, lon:typing.Any) -> None:
        """Assign the position using the Cylindrical representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_cylindrical_metadata, radius, z, lon)

    _assign_cartesian_metadata = { "offset" : _assign_cartesian_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_cartesian(self, x:float, y:float, z:float) -> None:
        """Assign the position using the Cartesian representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_cartesian_metadata, x, y, z)

    _assign_planetocentric_metadata = { "offset" : _assign_planetocentric_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def assign_planetocentric(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Assign the position using the Planetocentric representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_planetocentric_metadata, lat, lon, alt)

    _assign_planetodetic_metadata = { "offset" : _assign_planetodetic_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant, agcom.DOUBLE,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def assign_planetodetic(self, lat:typing.Any, lon:typing.Any, alt:float) -> None:
        """Assign the position using the Planetodetic representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._assign_planetodetic_metadata, lat, lon, alt)

    _query_planetocentric_metadata = { "offset" : _query_planetocentric_method_offset,
            "arg_types" : (POINTER(agcom.Variant), POINTER(agcom.Variant), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def query_planetocentric(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Get the position using the Planetocentric representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetocentric_metadata, OutArg(), OutArg(), OutArg())

    _query_planetodetic_metadata = { "offset" : _query_planetodetic_method_offset,
            "arg_types" : (POINTER(agcom.Variant), POINTER(agcom.Variant), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def query_planetodetic(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Get the position using the Planetodetic representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetodetic_metadata, OutArg(), OutArg(), OutArg())

    _query_spherical_metadata = { "offset" : _query_spherical_method_offset,
            "arg_types" : (POINTER(agcom.Variant), POINTER(agcom.Variant), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def query_spherical(self) -> typing.Tuple[typing.Any, typing.Any, float]:
        """Get the position using the Spherical representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_spherical_metadata, OutArg(), OutArg(), OutArg())

    _query_cylindrical_metadata = { "offset" : _query_cylindrical_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.Variant), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.VariantArg, agmarshall.DoubleArg,) }
    def query_cylindrical(self) -> typing.Tuple[float, typing.Any, float]:
        """Get the position using the Cylindrical representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cylindrical_metadata, OutArg(), OutArg(), OutArg())

    _query_cartesian_metadata = { "offset" : _query_cartesian_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def query_cartesian(self) -> typing.Tuple[float, float, float]:
        """Get the position using the Cartesian representation."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cartesian_metadata, OutArg(), OutArg(), OutArg())

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the central body."""
        return self._intf.get_property(IPosition._metadata, IPosition._get_central_body_name_metadata)

    _query_planetocentric_array_metadata = { "offset" : _query_planetocentric_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_planetocentric_array(self) -> list:
        """Return the Planetocentric elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetocentric_array_metadata, OutArg())

    _query_planetodetic_array_metadata = { "offset" : _query_planetodetic_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_planetodetic_array(self) -> list:
        """Return the Planetodetic elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_planetodetic_array_metadata, OutArg())

    _query_spherical_array_metadata = { "offset" : _query_spherical_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_spherical_array(self) -> list:
        """Return the Spherical elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_spherical_array_metadata, OutArg())

    _query_cylindrical_array_metadata = { "offset" : _query_cylindrical_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_cylindrical_array(self) -> list:
        """Return the Cylindrical elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cylindrical_array_metadata, OutArg())

    _query_cartesian_array_metadata = { "offset" : _query_cartesian_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_cartesian_array(self) -> list:
        """Return the Cartesian elements as an array."""
        return self._intf.invoke(IPosition._metadata, IPosition._query_cartesian_array_metadata, OutArg())

    _property_names[position_type] = "position_type"
    _property_names[central_body_name] = "central_body_name"


agcls.AgClassCatalog.add_catalog_entry((4915275008665419291, 11705930105741336507), IPosition)
agcls.AgTypeNameMap["IPosition"] = IPosition

class IDirection(object):
    """Interface to set and retrieve direction options for aligned and constrained vectors."""

    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _convert_to_method_offset = 1
    _get_direction_type_method_offset = 2
    _assign_method_offset = 3
    _assign_euler_method_offset = 4
    _assign_pr_method_offset = 5
    _assign_ra_dec_method_offset = 6
    _assign_xyz_method_offset = 7
    _query_euler_method_offset = 8
    _query_pr_method_offset = 9
    _query_ra_dec_method_offset = 10
    _query_xyz_method_offset = 11
    _query_euler_array_method_offset = 12
    _query_pr_array_method_offset = 13
    _query_ra_dec_array_method_offset = 14
    _query_xyz_array_method_offset = 15
    _metadata = {
        "iid_data" : (4665164470270701823, 18073961302852259771),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IDirection."""
        initialize_from_source_object(self, source_object, IDirection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IDirection)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IDirection, None)

    _convert_to_metadata = { "offset" : _convert_to_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(DirectionType), agmarshall.InterfaceOutArg,) }
    def convert_to(self, type:"DirectionType") -> "IDirection":
        """Change the direction to the type specified."""
        return self._intf.invoke(IDirection._metadata, IDirection._convert_to_metadata, type, OutArg())

    _get_direction_type_metadata = { "offset" : _get_direction_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(DirectionType),) }
    @property
    def direction_type(self) -> "DirectionType":
        """Return the type of direction currently being used."""
        return self._intf.get_property(IDirection._metadata, IDirection._get_direction_type_metadata)

    _assign_metadata = { "offset" : _assign_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IDirection"),) }
    def assign(self, direction:"IDirection") -> None:
        """Assign a new direction."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_metadata, direction)

    _assign_euler_metadata = { "offset" : _assign_euler_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant, agcom.LONG,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.EnumArg(EulerDirectionSequence),) }
    def assign_euler(self, b:typing.Any, c:typing.Any, sequence:"EulerDirectionSequence") -> None:
        """Set direction using the Euler representation. Params B and C use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_euler_metadata, b, c, sequence)

    _assign_pr_metadata = { "offset" : _assign_pr_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg,) }
    def assign_pr(self, pitch:typing.Any, roll:typing.Any) -> None:
        """Set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_pr_metadata, pitch, roll)

    _assign_ra_dec_metadata = { "offset" : _assign_ra_dec_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg,) }
    def assign_ra_dec(self, ra:typing.Any, dec:typing.Any) -> None:
        """Set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_ra_dec_metadata, ra, dec)

    _assign_xyz_metadata = { "offset" : _assign_xyz_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_xyz(self, x:float, y:float, z:float) -> None:
        """Set direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        return self._intf.invoke(IDirection._metadata, IDirection._assign_xyz_metadata, x, y, z)

    _query_euler_metadata = { "offset" : _query_euler_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.Variant), POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.EnumArg(EulerDirectionSequence), agmarshall.VariantArg, agmarshall.VariantArg,) }
    def query_euler(self, sequence:"EulerDirectionSequence") -> typing.Tuple[typing.Any, typing.Any]:
        """Get direction using the Euler representation. Params B and C use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_euler_metadata, sequence, OutArg(), OutArg())

    _query_pr_metadata = { "offset" : _query_pr_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.Variant), POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.EnumArg(PRSequence), agmarshall.VariantArg, agmarshall.VariantArg,) }
    def query_pr(self, sequence:"PRSequence") -> typing.Tuple[typing.Any, typing.Any]:
        """Get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_pr_metadata, sequence, OutArg(), OutArg())

    _query_ra_dec_metadata = { "offset" : _query_ra_dec_method_offset,
            "arg_types" : (POINTER(agcom.Variant), POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg,) }
    def query_ra_dec(self) -> typing.Tuple[typing.Any, typing.Any]:
        """Get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_ra_dec_metadata, OutArg(), OutArg())

    _query_xyz_metadata = { "offset" : _query_xyz_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def query_xyz(self) -> typing.Tuple[float, float, float]:
        """Get direction using the Cartesian representation. Params X, Y and Z are dimensionless."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_xyz_metadata, OutArg(), OutArg(), OutArg())

    _query_euler_array_metadata = { "offset" : _query_euler_array_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.EnumArg(EulerDirectionSequence), agmarshall.LPSafearrayArg,) }
    def query_euler_array(self, sequence:"EulerDirectionSequence") -> list:
        """Return the Euler elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_euler_array_metadata, sequence, OutArg())

    _query_pr_array_metadata = { "offset" : _query_pr_array_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.EnumArg(PRSequence), agmarshall.LPSafearrayArg,) }
    def query_pr_array(self, sequence:"PRSequence") -> list:
        """Return the PR elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_pr_array_metadata, sequence, OutArg())

    _query_ra_dec_array_metadata = { "offset" : _query_ra_dec_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_ra_dec_array(self) -> list:
        """Return the RADec elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_ra_dec_array_metadata, OutArg())

    _query_xyz_array_metadata = { "offset" : _query_xyz_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_xyz_array(self) -> list:
        """Return the XYZ elements in an array."""
        return self._intf.invoke(IDirection._metadata, IDirection._query_xyz_array_metadata, OutArg())

    _property_names[direction_type] = "direction_type"


agcls.AgClassCatalog.add_catalog_entry((4665164470270701823, 18073961302852259771), IDirection)
agcls.AgTypeNameMap["IDirection"] = IDirection

class ICartesian3Vector(object):
    """Represents a cartesian 3-D vector."""

    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_x_method_offset = 1
    _set_x_method_offset = 2
    _get_y_method_offset = 3
    _set_y_method_offset = 4
    _get_z_method_offset = 5
    _set_z_method_offset = 6
    _get_method_offset = 7
    _set_method_offset = 8
    _to_array_method_offset = 9
    _metadata = {
        "iid_data" : (5655437622738394688, 13912570415437090448),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type ICartesian3Vector."""
        initialize_from_source_object(self, source_object, ICartesian3Vector)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, ICartesian3Vector)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, ICartesian3Vector, None)

    _get_x_metadata = { "offset" : _get_x_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def x(self) -> float:
        """X coordinate."""
        return self._intf.get_property(ICartesian3Vector._metadata, ICartesian3Vector._get_x_metadata)

    _set_x_metadata = { "offset" : _set_x_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @x.setter
    def x(self, x:float) -> None:
        return self._intf.set_property(ICartesian3Vector._metadata, ICartesian3Vector._set_x_metadata, x)

    _get_y_metadata = { "offset" : _get_y_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def y(self) -> float:
        """Y coordinate."""
        return self._intf.get_property(ICartesian3Vector._metadata, ICartesian3Vector._get_y_metadata)

    _set_y_metadata = { "offset" : _set_y_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @y.setter
    def y(self, y:float) -> None:
        return self._intf.set_property(ICartesian3Vector._metadata, ICartesian3Vector._set_y_metadata, y)

    _get_z_metadata = { "offset" : _get_z_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def z(self) -> float:
        """Z coordinate."""
        return self._intf.get_property(ICartesian3Vector._metadata, ICartesian3Vector._get_z_metadata)

    _set_z_metadata = { "offset" : _set_z_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @z.setter
    def z(self, z:float) -> None:
        return self._intf.set_property(ICartesian3Vector._metadata, ICartesian3Vector._set_z_metadata, z)

    _get_metadata = { "offset" : _get_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def get(self) -> typing.Tuple[float, float, float]:
        """Return cartesian vector."""
        return self._intf.invoke(ICartesian3Vector._metadata, ICartesian3Vector._get_metadata, OutArg(), OutArg(), OutArg())

    _set_metadata = { "offset" : _set_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def set(self, x:float, y:float, z:float) -> None:
        """Set cartesian vector."""
        return self._intf.invoke(ICartesian3Vector._metadata, ICartesian3Vector._set_metadata, x, y, z)

    _to_array_metadata = { "offset" : _to_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def to_array(self) -> list:
        """Return coordinates as an array."""
        return self._intf.invoke(ICartesian3Vector._metadata, ICartesian3Vector._to_array_metadata, OutArg())

    _property_names[x] = "x"
    _property_names[y] = "y"
    _property_names[z] = "z"


agcls.AgClassCatalog.add_catalog_entry((5655437622738394688, 13912570415437090448), ICartesian3Vector)
agcls.AgTypeNameMap["ICartesian3Vector"] = ICartesian3Vector

class IOrientation(object):
    """Interface to set and retrieve the orientation method."""

    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _convert_to_method_offset = 1
    _get_orientation_type_method_offset = 2
    _assign_method_offset = 3
    _assign_az_el_method_offset = 4
    _assign_euler_angles_method_offset = 5
    _assign_quaternion_method_offset = 6
    _assign_ypr_angles_method_offset = 7
    _query_az_el_method_offset = 8
    _query_euler_angles_method_offset = 9
    _query_quaternion_method_offset = 10
    _query_ypr_angles_method_offset = 11
    _query_az_el_array_method_offset = 12
    _query_euler_angles_array_method_offset = 13
    _query_quaternion_array_method_offset = 14
    _query_ypr_angles_array_method_offset = 15
    _metadata = {
        "iid_data" : (5527531896719355797, 5509404503921157029),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IOrientation."""
        initialize_from_source_object(self, source_object, IOrientation)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IOrientation)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IOrientation, None)

    _convert_to_metadata = { "offset" : _convert_to_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(OrientationType), agmarshall.InterfaceOutArg,) }
    def convert_to(self, type:"OrientationType") -> "IOrientation":
        """Change the orientation method to the type specified."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._convert_to_metadata, type, OutArg())

    _get_orientation_type_metadata = { "offset" : _get_orientation_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(OrientationType),) }
    @property
    def orientation_type(self) -> "OrientationType":
        """Return the orientation method currently being used."""
        return self._intf.get_property(IOrientation._metadata, IOrientation._get_orientation_type_metadata)

    _assign_metadata = { "offset" : _assign_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IOrientation"),) }
    def assign(self, orientation:"IOrientation") -> None:
        """Assign a new orientation method."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_metadata, orientation)

    _assign_az_el_metadata = { "offset" : _assign_az_el_method_offset,
            "arg_types" : (agcom.Variant, agcom.Variant, agcom.LONG,),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.EnumArg(AzElAboutBoresight),) }
    def assign_az_el(self, azimuth:typing.Any, elevation:typing.Any, about_boresight:"AzElAboutBoresight") -> None:
        """Set orientation using the AzEl representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_az_el_metadata, azimuth, elevation, about_boresight)

    _assign_euler_angles_metadata = { "offset" : _assign_euler_angles_method_offset,
            "arg_types" : (agcom.LONG, agcom.Variant, agcom.Variant, agcom.Variant,),
            "marshallers" : (agmarshall.EnumArg(EulerOrientationSequenceType), agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.VariantArg,) }
    def assign_euler_angles(self, sequence:"EulerOrientationSequenceType", a:typing.Any, b:typing.Any, c:typing.Any) -> None:
        """Set orientation using the Euler angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_euler_angles_metadata, sequence, a, b, c)

    _assign_quaternion_metadata = { "offset" : _assign_quaternion_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_quaternion(self, qx:float, qy:float, qz:float, qs:float) -> None:
        """Set orientation using the Quaternion representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_quaternion_metadata, qx, qy, qz, qs)

    _assign_ypr_angles_metadata = { "offset" : _assign_ypr_angles_method_offset,
            "arg_types" : (agcom.LONG, agcom.Variant, agcom.Variant, agcom.Variant,),
            "marshallers" : (agmarshall.EnumArg(YPRAnglesSequence), agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.VariantArg,) }
    def assign_ypr_angles(self, sequence:"YPRAnglesSequence", yaw:typing.Any, pitch:typing.Any, roll:typing.Any) -> None:
        """Set orientation using the YPR angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._assign_ypr_angles_metadata, sequence, yaw, pitch, roll)

    _query_az_el_metadata = { "offset" : _query_az_el_method_offset,
            "arg_types" : (POINTER(agcom.Variant), POINTER(agcom.Variant), POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.EnumArg(AzElAboutBoresight),) }
    def query_az_el(self) -> typing.Tuple[typing.Any, typing.Any, AzElAboutBoresight]:
        """Get orientation using the AzEl representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_az_el_metadata, OutArg(), OutArg(), OutArg())

    _query_euler_angles_metadata = { "offset" : _query_euler_angles_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.Variant), POINTER(agcom.Variant), POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.EnumArg(EulerOrientationSequenceType), agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.VariantArg,) }
    def query_euler_angles(self, sequence:"EulerOrientationSequenceType") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Get orientation using the Euler angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_euler_angles_metadata, sequence, OutArg(), OutArg(), OutArg())

    _query_quaternion_metadata = { "offset" : _query_quaternion_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def query_quaternion(self) -> typing.Tuple[float, float, float, float]:
        """Get orientation using the Quaternion representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_quaternion_metadata, OutArg(), OutArg(), OutArg(), OutArg())

    _query_ypr_angles_metadata = { "offset" : _query_ypr_angles_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.Variant), POINTER(agcom.Variant), POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.EnumArg(YPRAnglesSequence), agmarshall.VariantArg, agmarshall.VariantArg, agmarshall.VariantArg,) }
    def query_ypr_angles(self, sequence:"YPRAnglesSequence") -> typing.Tuple[typing.Any, typing.Any, typing.Any]:
        """Get orientation using the YPR angles representation."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_ypr_angles_metadata, sequence, OutArg(), OutArg(), OutArg())

    _query_az_el_array_metadata = { "offset" : _query_az_el_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_az_el_array(self) -> list:
        """Return the AzEl elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_az_el_array_metadata, OutArg())

    _query_euler_angles_array_metadata = { "offset" : _query_euler_angles_array_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.EnumArg(EulerOrientationSequenceType), agmarshall.LPSafearrayArg,) }
    def query_euler_angles_array(self, sequence:"EulerOrientationSequenceType") -> list:
        """Return the Euler elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_euler_angles_array_metadata, sequence, OutArg())

    _query_quaternion_array_metadata = { "offset" : _query_quaternion_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def query_quaternion_array(self) -> list:
        """Return the Quaternion elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_quaternion_array_metadata, OutArg())

    _query_ypr_angles_array_metadata = { "offset" : _query_ypr_angles_array_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.EnumArg(YPRAnglesSequence), agmarshall.LPSafearrayArg,) }
    def query_ypr_angles_array(self, sequence:"YPRAnglesSequence") -> list:
        """Return the YPR Angles elements as an array."""
        return self._intf.invoke(IOrientation._metadata, IOrientation._query_ypr_angles_array_metadata, sequence, OutArg())

    _property_names[orientation_type] = "orientation_type"


agcls.AgClassCatalog.add_catalog_entry((5527531896719355797, 5509404503921157029), IOrientation)
agcls.AgTypeNameMap["IOrientation"] = IOrientation

class IOrientationAzEl(IOrientation):
    """Interface for AzEl orientation method."""

    _num_methods = 6
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _get_azimuth_method_offset = 1
    _set_azimuth_method_offset = 2
    _get_elevation_method_offset = 3
    _set_elevation_method_offset = 4
    _get_about_boresight_method_offset = 5
    _set_about_boresight_method_offset = 6
    _metadata = {
        "iid_data" : (5380876048439019019, 3075237744116676795),
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IOrientationAzEl."""
        initialize_from_source_object(self, source_object, IOrientationAzEl)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IOrientationAzEl)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IOrientationAzEl, IOrientation)

    _get_azimuth_metadata = { "offset" : _get_azimuth_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def azimuth(self) -> typing.Any:
        """Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationAzEl._metadata, IOrientationAzEl._get_azimuth_metadata)

    _set_azimuth_metadata = { "offset" : _set_azimuth_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @azimuth.setter
    def azimuth(self, azimuth:typing.Any) -> None:
        return self._intf.set_property(IOrientationAzEl._metadata, IOrientationAzEl._set_azimuth_metadata, azimuth)

    _get_elevation_metadata = { "offset" : _get_elevation_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def elevation(self) -> typing.Any:
        """Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationAzEl._metadata, IOrientationAzEl._get_elevation_metadata)

    _set_elevation_metadata = { "offset" : _set_elevation_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @elevation.setter
    def elevation(self, elevation:typing.Any) -> None:
        return self._intf.set_property(IOrientationAzEl._metadata, IOrientationAzEl._set_elevation_metadata, elevation)

    _get_about_boresight_metadata = { "offset" : _get_about_boresight_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(AzElAboutBoresight),) }
    @property
    def about_boresight(self) -> "AzElAboutBoresight":
        """Determine orientation of the X and Y axes with respect to the parent's reference frame."""
        return self._intf.get_property(IOrientationAzEl._metadata, IOrientationAzEl._get_about_boresight_metadata)

    _set_about_boresight_metadata = { "offset" : _set_about_boresight_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(AzElAboutBoresight),) }
    @about_boresight.setter
    def about_boresight(self, about_boresight:"AzElAboutBoresight") -> None:
        return self._intf.set_property(IOrientationAzEl._metadata, IOrientationAzEl._set_about_boresight_metadata, about_boresight)

    _property_names[azimuth] = "azimuth"
    _property_names[elevation] = "elevation"
    _property_names[about_boresight] = "about_boresight"


agcls.AgClassCatalog.add_catalog_entry((5380876048439019019, 3075237744116676795), IOrientationAzEl)
agcls.AgTypeNameMap["IOrientationAzEl"] = IOrientationAzEl

class IOrientationEulerAngles(IOrientation):
    """Interface for Euler Angles orientation method."""

    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _get_sequence_method_offset = 1
    _set_sequence_method_offset = 2
    _get_a_method_offset = 3
    _set_a_method_offset = 4
    _get_b_method_offset = 5
    _set_b_method_offset = 6
    _get_c_method_offset = 7
    _set_c_method_offset = 8
    _metadata = {
        "iid_data" : (5157329419772963673, 3459874081805935802),
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IOrientationEulerAngles."""
        initialize_from_source_object(self, source_object, IOrientationEulerAngles)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IOrientationEulerAngles)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IOrientationEulerAngles, IOrientation)

    _get_sequence_metadata = { "offset" : _get_sequence_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(EulerOrientationSequenceType),) }
    @property
    def sequence(self) -> "EulerOrientationSequenceType":
        """Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_sequence_metadata)

    _set_sequence_metadata = { "offset" : _set_sequence_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(EulerOrientationSequenceType),) }
    @sequence.setter
    def sequence(self, value:"EulerOrientationSequenceType") -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_sequence_metadata, value)

    _get_a_metadata = { "offset" : _get_a_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def a(self) -> typing.Any:
        """Euler A angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_a_metadata)

    _set_a_metadata = { "offset" : _set_a_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @a.setter
    def a(self, va:typing.Any) -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_a_metadata, va)

    _get_b_metadata = { "offset" : _get_b_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def b(self) -> typing.Any:
        """Euler b angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_b_metadata)

    _set_b_metadata = { "offset" : _set_b_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @b.setter
    def b(self, vb:typing.Any) -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_b_metadata, vb)

    _get_c_metadata = { "offset" : _get_c_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def c(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._get_c_metadata)

    _set_c_metadata = { "offset" : _set_c_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @c.setter
    def c(self, vc:typing.Any) -> None:
        return self._intf.set_property(IOrientationEulerAngles._metadata, IOrientationEulerAngles._set_c_metadata, vc)

    _property_names[sequence] = "sequence"
    _property_names[a] = "a"
    _property_names[b] = "b"
    _property_names[c] = "c"


agcls.AgClassCatalog.add_catalog_entry((5157329419772963673, 3459874081805935802), IOrientationEulerAngles)
agcls.AgTypeNameMap["IOrientationEulerAngles"] = IOrientationEulerAngles

class IOrientationQuaternion(IOrientation):
    """Quaternion representing orientation between two sets of axes."""

    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _get_qx_method_offset = 1
    _set_qx_method_offset = 2
    _get_qy_method_offset = 3
    _set_qy_method_offset = 4
    _get_qz_method_offset = 5
    _set_qz_method_offset = 6
    _get_qs_method_offset = 7
    _set_qs_method_offset = 8
    _metadata = {
        "iid_data" : (5021744214173578956, 16583656354618992062),
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IOrientationQuaternion."""
        initialize_from_source_object(self, source_object, IOrientationQuaternion)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IOrientationQuaternion)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IOrientationQuaternion, IOrientation)

    _get_qx_metadata = { "offset" : _get_qx_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def qx(self) -> float:
        """Get or set the first element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QX = nx sin(A/2). Dimensionless."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qx_metadata)

    _set_qx_metadata = { "offset" : _set_qx_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @qx.setter
    def qx(self, qx:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qx_metadata, qx)

    _get_qy_metadata = { "offset" : _get_qy_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def qy(self) -> float:
        """Get or set the second element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QY = ny sin(A/2). Dimensionless."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qy_metadata)

    _set_qy_metadata = { "offset" : _set_qy_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @qy.setter
    def qy(self, qy:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qy_metadata, qy)

    _get_qz_metadata = { "offset" : _get_qz_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def qz(self) -> float:
        """Get or set the third element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QZ = nz sin(A/2). Dimensionless."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qz_metadata)

    _set_qz_metadata = { "offset" : _set_qz_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @qz.setter
    def qz(self, qz:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qz_metadata, qz)

    _get_qs_metadata = { "offset" : _get_qs_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def qs(self) -> float:
        """Get or set the scalar component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QS = cos(A/2). Dimensionless."""
        return self._intf.get_property(IOrientationQuaternion._metadata, IOrientationQuaternion._get_qs_metadata)

    _set_qs_metadata = { "offset" : _set_qs_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @qs.setter
    def qs(self, qs:float) -> None:
        return self._intf.set_property(IOrientationQuaternion._metadata, IOrientationQuaternion._set_qs_metadata, qs)

    _property_names[qx] = "qx"
    _property_names[qy] = "qy"
    _property_names[qz] = "qz"
    _property_names[qs] = "qs"


agcls.AgClassCatalog.add_catalog_entry((5021744214173578956, 16583656354618992062), IOrientationQuaternion)
agcls.AgTypeNameMap["IOrientationQuaternion"] = IOrientationQuaternion

class IOrientationYPRAngles(IOrientation):
    """Interface for Yaw-Pitch Roll (YPR) Angles orientation system."""

    _num_methods = 8
    _vtable_offset = IOrientation._vtable_offset + IOrientation._num_methods
    _get_sequence_method_offset = 1
    _set_sequence_method_offset = 2
    _get_yaw_method_offset = 3
    _set_yaw_method_offset = 4
    _get_pitch_method_offset = 5
    _set_pitch_method_offset = 6
    _get_roll_method_offset = 7
    _set_roll_method_offset = 8
    _metadata = {
        "iid_data" : (5036279671908239678, 3907031560372993438),
        "vtable_reference" : IOrientation._vtable_offset + IOrientation._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IOrientationYPRAngles."""
        initialize_from_source_object(self, source_object, IOrientationYPRAngles)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IOrientationYPRAngles)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IOrientationYPRAngles, IOrientation)

    _get_sequence_metadata = { "offset" : _get_sequence_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(YPRAnglesSequence),) }
    @property
    def sequence(self) -> "YPRAnglesSequence":
        """YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_sequence_metadata)

    _set_sequence_metadata = { "offset" : _set_sequence_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(YPRAnglesSequence),) }
    @sequence.setter
    def sequence(self, sequence:"YPRAnglesSequence") -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_sequence_metadata, sequence)

    _get_yaw_metadata = { "offset" : _get_yaw_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def yaw(self) -> typing.Any:
        """Yaw angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_yaw_metadata)

    _set_yaw_metadata = { "offset" : _set_yaw_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @yaw.setter
    def yaw(self, yaw:typing.Any) -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_yaw_metadata, yaw)

    _get_pitch_metadata = { "offset" : _get_pitch_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_pitch_metadata)

    _set_pitch_metadata = { "offset" : _set_pitch_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @pitch.setter
    def pitch(self, pitch:typing.Any) -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_pitch_metadata, pitch)

    _get_roll_metadata = { "offset" : _get_roll_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        return self._intf.get_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._get_roll_metadata)

    _set_roll_metadata = { "offset" : _set_roll_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @roll.setter
    def roll(self, roll:typing.Any) -> None:
        return self._intf.set_property(IOrientationYPRAngles._metadata, IOrientationYPRAngles._set_roll_metadata, roll)

    _property_names[sequence] = "sequence"
    _property_names[yaw] = "yaw"
    _property_names[pitch] = "pitch"
    _property_names[roll] = "roll"


agcls.AgClassCatalog.add_catalog_entry((5036279671908239678, 3907031560372993438), IOrientationYPRAngles)
agcls.AgTypeNameMap["IOrientationYPRAngles"] = IOrientationYPRAngles

class IOrientationPositionOffset(object):
    """Interface for defining the orientation origin position offset relative to the parent object."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_position_offset_method_offset = 1
    _metadata = {
        "iid_data" : (5742937774821171935, 3792791559970519990),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IOrientationPositionOffset."""
        initialize_from_source_object(self, source_object, IOrientationPositionOffset)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IOrientationPositionOffset)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IOrientationPositionOffset, None)

    _get_position_offset_metadata = { "offset" : _get_position_offset_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def position_offset(self) -> "ICartesian3Vector":
        """Get or set the position offset cartesian vector."""
        return self._intf.get_property(IOrientationPositionOffset._metadata, IOrientationPositionOffset._get_position_offset_metadata)

    _property_names[position_offset] = "position_offset"


agcls.AgClassCatalog.add_catalog_entry((5742937774821171935, 3792791559970519990), IOrientationPositionOffset)
agcls.AgTypeNameMap["IOrientationPositionOffset"] = IOrientationPositionOffset

class IOrbitState(object):
    """Interface to set and retrieve the coordinate type used to specify the orbit state."""

    _num_methods = 13
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _convert_to_method_offset = 1
    _get_orbit_state_type_method_offset = 2
    _assign_method_offset = 3
    _assign_classical_method_offset = 4
    _assign_cartesian_method_offset = 5
    _assign_geodetic_method_offset = 6
    _assign_equinoctial_posigrade_method_offset = 7
    _assign_equinoctial_retrograde_method_offset = 8
    _assign_mixed_spherical_method_offset = 9
    _assign_spherical_method_offset = 10
    _get_central_body_name_method_offset = 11
    _get_epoch_method_offset = 12
    _set_epoch_method_offset = 13
    _metadata = {
        "iid_data" : (4661309965933595946, 13542321643039239316),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IOrbitState."""
        initialize_from_source_object(self, source_object, IOrbitState)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IOrbitState)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IOrbitState, None)

    _convert_to_metadata = { "offset" : _convert_to_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(OrbitStateType), agmarshall.InterfaceOutArg,) }
    def convert_to(self, type:"OrbitStateType") -> "IOrbitState":
        """Change the coordinate type to the type specified."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._convert_to_metadata, type, OutArg())

    _get_orbit_state_type_metadata = { "offset" : _get_orbit_state_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(OrbitStateType),) }
    @property
    def orbit_state_type(self) -> "OrbitStateType":
        """Return the coordinate type currently being used."""
        return self._intf.get_property(IOrbitState._metadata, IOrbitState._get_orbit_state_type_metadata)

    _assign_metadata = { "offset" : _assign_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IOrbitState"),) }
    def assign(self, orbit_state:"IOrbitState") -> None:
        """Assign a new coordinate type."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_metadata, orbit_state)

    _assign_classical_metadata = { "offset" : _assign_classical_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.EnumArg(CoordinateSystem), agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_classical(self, coordinate_system:"CoordinateSystem", semi_major_axis:float, eccentricity:float, inclination:float, arg_of_perigee:float, raan:float, mean_anomaly:float) -> None:
        """Assign a new orbit state using Classical representation."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_classical_metadata, coordinate_system, semi_major_axis, eccentricity, inclination, arg_of_perigee, raan, mean_anomaly)

    _assign_cartesian_metadata = { "offset" : _assign_cartesian_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.EnumArg(CoordinateSystem), agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_cartesian(self, coordinate_system:"CoordinateSystem", x_position:float, y_position:float, z_position:float, x_velocity:float, y_velocity:float, z_velocity:float) -> None:
        """Assign a new orbit state using Cartesian representation."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_cartesian_metadata, coordinate_system, x_position, y_position, z_position, x_velocity, y_velocity, z_velocity)

    _assign_geodetic_metadata = { "offset" : _assign_geodetic_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.EnumArg(CoordinateSystem), agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_geodetic(self, coordinate_system:"CoordinateSystem", latitude:float, longitude:float, altitude:float, latitude_rate:float, longitude_rate:float, altitude_rate:float) -> None:
        """Assign a new orbit state using Geodetic representation."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_geodetic_metadata, coordinate_system, latitude, longitude, altitude, latitude_rate, longitude_rate, altitude_rate)

    _assign_equinoctial_posigrade_metadata = { "offset" : _assign_equinoctial_posigrade_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.EnumArg(CoordinateSystem), agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_equinoctial_posigrade(self, coordinate_system:"CoordinateSystem", semi_major_axis:float, h:float, k:float, p:float, q:float, mean_lon:float) -> None:
        """Assign a new orbit state using Equinoctial representation."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_equinoctial_posigrade_metadata, coordinate_system, semi_major_axis, h, k, p, q, mean_lon)

    _assign_equinoctial_retrograde_metadata = { "offset" : _assign_equinoctial_retrograde_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.EnumArg(CoordinateSystem), agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_equinoctial_retrograde(self, coordinate_system:"CoordinateSystem", semi_major_axis:float, h:float, k:float, p:float, q:float, mean_lon:float) -> None:
        """Assign a new orbit state using Equinoctial representation."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_equinoctial_retrograde_metadata, coordinate_system, semi_major_axis, h, k, p, q, mean_lon)

    _assign_mixed_spherical_metadata = { "offset" : _assign_mixed_spherical_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.EnumArg(CoordinateSystem), agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_mixed_spherical(self, coordinate_system:"CoordinateSystem", latitude:float, longitude:float, altitude:float, horizontal_flight_path_angle:float, flight_path_azimuth:float, velocity:float) -> None:
        """Assign a new orbit state using Mixed Spherical representation."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_mixed_spherical_metadata, coordinate_system, latitude, longitude, altitude, horizontal_flight_path_angle, flight_path_azimuth, velocity)

    _assign_spherical_metadata = { "offset" : _assign_spherical_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.EnumArg(CoordinateSystem), agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def assign_spherical(self, coordinate_system:"CoordinateSystem", right_ascension:float, declination:float, radius:float, horizontal_flight_path_angle:float, flight_path_azimuth:float, velocity:float) -> None:
        """Assign a new orbit state using Spherical representation."""
        return self._intf.invoke(IOrbitState._metadata, IOrbitState._assign_spherical_metadata, coordinate_system, right_ascension, declination, radius, horizontal_flight_path_angle, flight_path_azimuth, velocity)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the central body."""
        return self._intf.get_property(IOrbitState._metadata, IOrbitState._get_central_body_name_metadata)

    _get_epoch_metadata = { "offset" : _get_epoch_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def epoch(self) -> typing.Any:
        """Get or set the state epoch."""
        return self._intf.get_property(IOrbitState._metadata, IOrbitState._get_epoch_metadata)

    _set_epoch_metadata = { "offset" : _set_epoch_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @epoch.setter
    def epoch(self, epoch:typing.Any) -> None:
        return self._intf.set_property(IOrbitState._metadata, IOrbitState._set_epoch_metadata, epoch)

    _property_names[orbit_state_type] = "orbit_state_type"
    _property_names[central_body_name] = "central_body_name"
    _property_names[epoch] = "epoch"


agcls.AgClassCatalog.add_catalog_entry((4661309965933595946, 13542321643039239316), IOrbitState)
agcls.AgTypeNameMap["IOrbitState"] = IOrbitState

class IRuntimeTypeInfoProvider(object):
    """Access point for RuntimeTypeInfo."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_provide_runtime_type_info_method_offset = 1
    _metadata = {
        "iid_data" : (5674705672689382170, 17933926892286240679),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IRuntimeTypeInfoProvider."""
        initialize_from_source_object(self, source_object, IRuntimeTypeInfoProvider)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IRuntimeTypeInfoProvider)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IRuntimeTypeInfoProvider, None)

    _get_provide_runtime_type_info_metadata = { "offset" : _get_provide_runtime_type_info_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def provide_runtime_type_info(self) -> "RuntimeTypeInfo":
        """Return the RuntimeTypeInfo interface to access properties at runtime."""
        return self._intf.get_property(IRuntimeTypeInfoProvider._metadata, IRuntimeTypeInfoProvider._get_provide_runtime_type_info_metadata)

    _property_names[provide_runtime_type_info] = "provide_runtime_type_info"


agcls.AgClassCatalog.add_catalog_entry((5674705672689382170, 17933926892286240679), IRuntimeTypeInfoProvider)
agcls.AgTypeNameMap["IRuntimeTypeInfoProvider"] = IRuntimeTypeInfoProvider



class ExecuteCommandResult(SupportsDeleteCallback):
    """Collection of strings returned by the ExecuteCommand."""

    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _range_method_offset = 4
    _get_is_succeeded_method_offset = 5
    _metadata = {
        "iid_data" : (5116368304795373993, 3944362883220586125),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ExecuteCommandResult)
    def __iter__(self):
        """Create an iterator for the ExecuteCommandResult object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(ExecuteCommandResult._metadata, ExecuteCommandResult._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LongArg, agmarshall.BStrArg,) }
    def item(self, index:int) -> str:
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(ExecuteCommandResult._metadata, ExecuteCommandResult._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an object that can be used to iterate through all the strings in the collection."""
        return self._intf.get_property(ExecuteCommandResult._metadata, ExecuteCommandResult._get__new_enum_metadata)

    _range_metadata = { "offset" : _range_method_offset,
            "arg_types" : (agcom.LONG, agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LongArg, agmarshall.LongArg, agmarshall.LPSafearrayArg,) }
    def range(self, start_index:int, stop_index:int) -> list:
        """Return the elements within the specified range."""
        return self._intf.invoke(ExecuteCommandResult._metadata, ExecuteCommandResult._range_metadata, start_index, stop_index, OutArg())

    _get_is_succeeded_metadata = { "offset" : _get_is_succeeded_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_succeeded(self) -> bool:
        """Indicate whether the object contains valid results."""
        return self._intf.get_property(ExecuteCommandResult._metadata, ExecuteCommandResult._get_is_succeeded_metadata)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"
    _property_names[is_succeeded] = "is_succeeded"

    def __init__(self, source_object=None):
        """Construct an object of type ExecuteCommandResult."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ExecuteCommandResult)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ExecuteCommandResult, [ExecuteCommandResult, ])

agcls.AgClassCatalog.add_catalog_entry((5325039016176067736, 10330533696176440711), ExecuteCommandResult)
agcls.AgClassCatalog.add_catalog_entry(agcom.GUID.from_registry_format('{760B3E9D-004F-451B-ABEE-C9B725E168CA}').as_data_pair(), ExecuteCommandResult)
# mapping for ExecuteCommandResult
agcls.AgBackwardsCompatabilityMapping.add_mapping(agcom.GUID.from_registry_format('{936551A9-FDDD-4700-8D3E-99E72431BD36}').as_data_pair(), agcom.GUID.from_registry_format('{DE68E2F7-30CF-40FE-A6CD-E883AE3D43B6}').as_data_pair())
agcls.AgTypeNameMap["ExecuteCommandResult"] = ExecuteCommandResult

class ExecuteMultipleCommandsResult(SupportsDeleteCallback):
    """Collection of objects returned by the ExecuteMultipleCommands."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _metadata = {
        "iid_data" : (4800451087513012265, 17131709637358464434),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ExecuteMultipleCommandsResult)
    def __iter__(self):
        """Create an iterator for the ExecuteMultipleCommandsResult object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "ExecuteCommandResult":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(ExecuteMultipleCommandsResult._metadata, ExecuteMultipleCommandsResult._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LongArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "ExecuteCommandResult":
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(ExecuteMultipleCommandsResult._metadata, ExecuteMultipleCommandsResult._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an object that can be used to iterate through all the objects in the collection."""
        return self._intf.get_property(ExecuteMultipleCommandsResult._metadata, ExecuteMultipleCommandsResult._get__new_enum_metadata)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type ExecuteMultipleCommandsResult."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ExecuteMultipleCommandsResult)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ExecuteMultipleCommandsResult, [ExecuteMultipleCommandsResult, ])

agcls.AgClassCatalog.add_catalog_entry((5725886502310958038, 3372349005439043232), ExecuteMultipleCommandsResult)
agcls.AgClassCatalog.add_catalog_entry(agcom.GUID.from_registry_format('{CF0ED205-6ABE-4665-BB1B-E4793082893E}').as_data_pair(), ExecuteMultipleCommandsResult)
# mapping for ExecuteMultipleCommandsResult
agcls.AgBackwardsCompatabilityMapping.add_mapping(agcom.GUID.from_registry_format('{88D9C829-A0D4-429E-B22D-E3C1250FC0ED}').as_data_pair(), agcom.GUID.from_registry_format('{6F7CA447-CD92-4860-BF55-B034D88D317E}').as_data_pair())
agcls.AgTypeNameMap["ExecuteMultipleCommandsResult"] = ExecuteMultipleCommandsResult

class UnitPreferencesUnit(SupportsDeleteCallback):
    """Provide info about a unit."""

    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_full_name_method_offset = 1
    _get_abbrv_method_offset = 2
    _get_identifier_method_offset = 3
    _get_dimension_method_offset = 4
    _metadata = {
        "iid_data" : (4844437149658170964, 6264569844926471836),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UnitPreferencesUnit)

    _get_full_name_metadata = { "offset" : _get_full_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def full_name(self) -> str:
        """Return the fullname of the unit."""
        return self._intf.get_property(UnitPreferencesUnit._metadata, UnitPreferencesUnit._get_full_name_metadata)

    _get_abbrv_metadata = { "offset" : _get_abbrv_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def abbrv(self) -> str:
        """Return the abbreviation of the unit."""
        return self._intf.get_property(UnitPreferencesUnit._metadata, UnitPreferencesUnit._get_abbrv_metadata)

    _get_identifier_metadata = { "offset" : _get_identifier_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def identifier(self) -> int:
        """Return the ID of the unit."""
        return self._intf.get_property(UnitPreferencesUnit._metadata, UnitPreferencesUnit._get_identifier_metadata)

    _get_dimension_metadata = { "offset" : _get_dimension_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def dimension(self) -> "UnitPreferencesDimension":
        """Return the Dimension for this unit."""
        return self._intf.get_property(UnitPreferencesUnit._metadata, UnitPreferencesUnit._get_dimension_metadata)

    _property_names[full_name] = "full_name"
    _property_names[abbrv] = "abbrv"
    _property_names[identifier] = "identifier"
    _property_names[dimension] = "dimension"

    def __init__(self, source_object=None):
        """Construct an object of type UnitPreferencesUnit."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, UnitPreferencesUnit)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UnitPreferencesUnit, [UnitPreferencesUnit, ])

agcls.AgClassCatalog.add_catalog_entry((5605834986361923886, 2839872590025622964), UnitPreferencesUnit)
agcls.AgTypeNameMap["UnitPreferencesUnit"] = UnitPreferencesUnit

class UnitPreferencesUnitCollection(SupportsDeleteCallback):
    """Provide access to the Unit collection."""

    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _get__new_enum_method_offset = 3
    _get_item_by_index_method_offset = 4
    _get_item_by_name_method_offset = 5
    _metadata = {
        "iid_data" : (5320669267766174731, 17033319525141121451),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UnitPreferencesUnitCollection)
    def __iter__(self):
        """Create an iterator for the UnitPreferencesUnitCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "UnitPreferencesUnit":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def item(self, index_or_name:typing.Any) -> "UnitPreferencesUnit":
        """Return the specific item in the collection given a unit identifier or an index."""
        return self._intf.invoke(UnitPreferencesUnitCollection._metadata, UnitPreferencesUnitCollection._item_metadata, index_or_name, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of items in the collection."""
        return self._intf.get_property(UnitPreferencesUnitCollection._metadata, UnitPreferencesUnitCollection._get_count_metadata)

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumeration of UnitPreferencesUnit."""
        return self._intf.get_property(UnitPreferencesUnitCollection._metadata, UnitPreferencesUnitCollection._get__new_enum_metadata)

    _get_item_by_index_metadata = { "offset" : _get_item_by_index_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "UnitPreferencesUnit":
        """Retrieve a unit from the collection by index."""
        return self._intf.invoke(UnitPreferencesUnitCollection._metadata, UnitPreferencesUnitCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "offset" : _get_item_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "UnitPreferencesUnit":
        """Retrieve a unit from the collection by name."""
        return self._intf.invoke(UnitPreferencesUnitCollection._metadata, UnitPreferencesUnitCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type UnitPreferencesUnitCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, UnitPreferencesUnitCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UnitPreferencesUnitCollection, [UnitPreferencesUnitCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5749538487087641148, 11168942521363040385), UnitPreferencesUnitCollection)
agcls.AgTypeNameMap["UnitPreferencesUnitCollection"] = UnitPreferencesUnitCollection

class UnitPreferencesDimension(SupportsDeleteCallback):
    """Provide info on a Dimension from the global unit table."""

    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_identifier_method_offset = 1
    _get_name_method_offset = 2
    _get_available_units_method_offset = 3
    _get_current_unit_method_offset = 4
    _set_current_unit_method_offset = 5
    _metadata = {
        "iid_data" : (4776818722171872996, 4798204912498317700),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UnitPreferencesDimension)

    _get_identifier_metadata = { "offset" : _get_identifier_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def identifier(self) -> int:
        """Return the ID of the dimension."""
        return self._intf.get_property(UnitPreferencesDimension._metadata, UnitPreferencesDimension._get_identifier_metadata)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Return the current Dimension's full name."""
        return self._intf.get_property(UnitPreferencesDimension._metadata, UnitPreferencesDimension._get_name_metadata)

    _get_available_units_metadata = { "offset" : _get_available_units_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def available_units(self) -> "UnitPreferencesUnitCollection":
        """Return collection of Units."""
        return self._intf.get_property(UnitPreferencesDimension._metadata, UnitPreferencesDimension._get_available_units_metadata)

    _get_current_unit_metadata = { "offset" : _get_current_unit_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def current_unit(self) -> "UnitPreferencesUnit":
        """Return the current unit for this dimension."""
        return self._intf.get_property(UnitPreferencesDimension._metadata, UnitPreferencesDimension._get_current_unit_metadata)

    _set_current_unit_metadata = { "offset" : _set_current_unit_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def set_current_unit(self, unit_abbrv:str) -> None:
        """Set the Unit for this simple dimension."""
        return self._intf.invoke(UnitPreferencesDimension._metadata, UnitPreferencesDimension._set_current_unit_metadata, unit_abbrv)

    _property_names[identifier] = "identifier"
    _property_names[name] = "name"
    _property_names[available_units] = "available_units"
    _property_names[current_unit] = "current_unit"

    def __init__(self, source_object=None):
        """Construct an object of type UnitPreferencesDimension."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, UnitPreferencesDimension)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UnitPreferencesDimension, [UnitPreferencesDimension, ])

agcls.AgClassCatalog.add_catalog_entry((4679286811697929572, 9862317536618453903), UnitPreferencesDimension)
agcls.AgTypeNameMap["UnitPreferencesDimension"] = UnitPreferencesDimension

class UnitPreferencesDimensionCollection(SupportsDeleteCallback):
    """Provide accesses to the global unit table."""

    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _set_current_unit_method_offset = 3
    _get_current_unit_abbrv_method_offset = 4
    _get_mission_elapsed_time_method_offset = 5
    _set_mission_elapsed_time_method_offset = 6
    _get_julian_date_offset_method_offset = 7
    _set_julian_date_offset_method_offset = 8
    _get__new_enum_method_offset = 9
    _reset_units_method_offset = 10
    _get_item_by_index_method_offset = 11
    _get_item_by_name_method_offset = 12
    _metadata = {
        "iid_data" : (4991061726184554424, 12406965035632193459),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UnitPreferencesDimensionCollection)
    def __iter__(self):
        """Create an iterator for the UnitPreferencesDimensionCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "UnitPreferencesDimension":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def item(self, index_or_name:typing.Any) -> "UnitPreferencesDimension":
        """Return an UnitPreferencesDimension given a Dimension name or an index."""
        return self._intf.invoke(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._item_metadata, index_or_name, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of items in the collection."""
        return self._intf.get_property(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._get_count_metadata)

    _set_current_unit_metadata = { "offset" : _set_current_unit_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg,) }
    def set_current_unit(self, dimension:str, unit_abbrv:str) -> None:
        """Return the Current unit for a Dimension."""
        return self._intf.invoke(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._set_current_unit_metadata, dimension, unit_abbrv)

    _get_current_unit_abbrv_metadata = { "offset" : _get_current_unit_abbrv_method_offset,
            "arg_types" : (agcom.Variant, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.BStrArg,) }
    def get_current_unit_abbrv(self, index_or_dim_name:typing.Any) -> str:
        """Return the Current Unit for a Dimension."""
        return self._intf.invoke(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._get_current_unit_abbrv_metadata, index_or_dim_name, OutArg())

    _get_mission_elapsed_time_metadata = { "offset" : _get_mission_elapsed_time_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def mission_elapsed_time(self) -> typing.Any:
        """The MissionElapsedTime."""
        return self._intf.get_property(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._get_mission_elapsed_time_metadata)

    _set_mission_elapsed_time_metadata = { "offset" : _set_mission_elapsed_time_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @mission_elapsed_time.setter
    def mission_elapsed_time(self, mis_elap_time:typing.Any) -> None:
        return self._intf.set_property(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._set_mission_elapsed_time_metadata, mis_elap_time)

    _get_julian_date_offset_metadata = { "offset" : _get_julian_date_offset_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def julian_date_offset(self) -> float:
        """The JulianDateOffset."""
        return self._intf.get_property(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._get_julian_date_offset_metadata)

    _set_julian_date_offset_metadata = { "offset" : _set_julian_date_offset_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @julian_date_offset.setter
    def julian_date_offset(self, julian_date_offset:float) -> None:
        return self._intf.set_property(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._set_julian_date_offset_metadata, julian_date_offset)

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return a collection of UnitPreferencesDimension."""
        return self._intf.get_property(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._get__new_enum_metadata)

    _reset_units_metadata = { "offset" : _reset_units_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def reset_units(self) -> None:
        """Reset the unitpreferences to the Default units."""
        return self._intf.invoke(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._reset_units_metadata, )

    _get_item_by_index_metadata = { "offset" : _get_item_by_index_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "UnitPreferencesDimension":
        """Retrieve a dimension from the collection by index."""
        return self._intf.invoke(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "offset" : _get_item_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "UnitPreferencesDimension":
        """Retrieve a dimension from the collection by name."""
        return self._intf.invoke(UnitPreferencesDimensionCollection._metadata, UnitPreferencesDimensionCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[mission_elapsed_time] = "mission_elapsed_time"
    _property_names[julian_date_offset] = "julian_date_offset"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type UnitPreferencesDimensionCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, UnitPreferencesDimensionCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UnitPreferencesDimensionCollection, [UnitPreferencesDimensionCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5550056258024923394, 1513114167815356310), UnitPreferencesDimensionCollection)
agcls.AgTypeNameMap["UnitPreferencesDimensionCollection"] = UnitPreferencesDimensionCollection

class ConversionUtility(SupportsDeleteCallback):
    """Provide conversion utilities."""

    _num_methods = 18
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _convert_quantity_method_offset = 1
    _convert_date_method_offset = 2
    _convert_quantity_array_method_offset = 3
    _convert_date_array_method_offset = 4
    _new_quantity_method_offset = 5
    _new_date_method_offset = 6
    _new_position_on_earth_method_offset = 7
    _convert_position_array_method_offset = 8
    _new_direction_method_offset = 9
    _new_orientation_method_offset = 10
    _new_orbit_state_on_earth_method_offset = 11
    _new_position_on_cb_method_offset = 12
    _new_orbit_state_on_cb_method_offset = 13
    _query_direction_cosine_matrix_method_offset = 14
    _query_direction_cosine_matrix_array_method_offset = 15
    _new_cartesian3_vector_method_offset = 16
    _new_cartesian3_vector_from_direction_method_offset = 17
    _new_cartesian3_vector_from_position_method_offset = 18
    _metadata = {
        "iid_data" : (5542071105973083214, 3736498381011271868),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ConversionUtility)

    _convert_quantity_metadata = { "offset" : _convert_quantity_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def convert_quantity(self, dimension_name:str, from_unit:str, to_unit:str, from_value:float) -> float:
        """Convert the specified quantity value from a given unit to another unit."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._convert_quantity_metadata, dimension_name, from_unit, to_unit, from_value, OutArg())

    _convert_date_metadata = { "offset" : _convert_date_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg,) }
    def convert_date(self, from_unit:str, to_unit:str, from_value:str) -> str:
        """Convert the specified date from a given unit to another unit."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._convert_date_metadata, from_unit, to_unit, from_value, OutArg())

    _convert_quantity_array_metadata = { "offset" : _convert_quantity_array_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.LPSAFEARRAY), POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.LPSafearrayArg, agmarshall.LPSafearrayArg,) }
    def convert_quantity_array(self, dimension_name:str, from_unit:str, to_unit:str, quantity_values:list) -> list:
        """Convert the specified quantity values from a given unit to another unit."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._convert_quantity_array_metadata, dimension_name, from_unit, to_unit, quantity_values, OutArg())

    _convert_date_array_metadata = { "offset" : _convert_date_array_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.LPSAFEARRAY), POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.LPSafearrayArg, agmarshall.LPSafearrayArg,) }
    def convert_date_array(self, from_unit:str, to_unit:str, from_values:list) -> list:
        """Convert the specified dates from a given unit to another unit."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._convert_date_array_metadata, from_unit, to_unit, from_values, OutArg())

    _new_quantity_metadata = { "offset" : _new_quantity_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.DoubleArg, agmarshall.InterfaceOutArg,) }
    def new_quantity(self, dimension:str, unit_abbrv:str, value:float) -> "Quantity":
        """Create an Quantity interface with the given dimension, unit and value."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_quantity_metadata, dimension, unit_abbrv, value, OutArg())

    _new_date_metadata = { "offset" : _new_date_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def new_date(self, unit_abbrv:str, value:str) -> "Date":
        """Create an Date interface with the given unit and value."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_date_metadata, unit_abbrv, value, OutArg())

    _new_position_on_earth_metadata = { "offset" : _new_position_on_earth_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def new_position_on_earth(self) -> "IPosition":
        """Create an IPosition interface with earth as its central body."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_position_on_earth_metadata, OutArg())

    _convert_position_array_metadata = { "offset" : _convert_position_array_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.LPSAFEARRAY), agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.EnumArg(PositionType), agmarshall.LPSafearrayArg, agmarshall.EnumArg(PositionType), agmarshall.LPSafearrayArg,) }
    def convert_position_array(self, position_type:"PositionType", position_array:list, convert_to:"PositionType") -> list:
        """Convert the specified position values from a given position type to another position type."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._convert_position_array_metadata, position_type, position_array, convert_to, OutArg())

    _new_direction_metadata = { "offset" : _new_direction_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def new_direction(self) -> "IDirection":
        """Create an IDirection interface."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_direction_metadata, OutArg())

    _new_orientation_metadata = { "offset" : _new_orientation_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def new_orientation(self) -> "IOrientation":
        """Create an IOrientation interface."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_orientation_metadata, OutArg())

    _new_orbit_state_on_earth_metadata = { "offset" : _new_orbit_state_on_earth_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def new_orbit_state_on_earth(self) -> "IOrbitState":
        """Create an IOrbitState interface with earth as its central body."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_orbit_state_on_earth_metadata, OutArg())

    _new_position_on_cb_metadata = { "offset" : _new_position_on_cb_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def new_position_on_cb(self, central_body_name:str) -> "IPosition":
        """Create an IPosition interface using the supplied central body."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_position_on_cb_metadata, central_body_name, OutArg())

    _new_orbit_state_on_cb_metadata = { "offset" : _new_orbit_state_on_cb_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def new_orbit_state_on_cb(self, central_body_name:str) -> "IOrbitState":
        """Create an IOrbitState interface using the supplied central body."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_orbit_state_on_cb_metadata, central_body_name, OutArg())

    _query_direction_cosine_matrix_metadata = { "offset" : _query_direction_cosine_matrix_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID), POINTER(agcom.PVOID), POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("IOrientation"), agmarshall.InterfaceOutArg, agmarshall.InterfaceOutArg, agmarshall.InterfaceOutArg,) }
    def query_direction_cosine_matrix(self, input_orientation:"IOrientation") -> typing.Tuple[ICartesian3Vector, ICartesian3Vector, ICartesian3Vector]:
        """Return a Direction Cosine Matrix (DCM)."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._query_direction_cosine_matrix_metadata, input_orientation, OutArg(), OutArg(), OutArg())

    _query_direction_cosine_matrix_array_metadata = { "offset" : _query_direction_cosine_matrix_array_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.InterfaceInArg("IOrientation"), agmarshall.LPSafearrayArg,) }
    def query_direction_cosine_matrix_array(self, input_orientation:"IOrientation") -> list:
        """Return a Direction Cosine Matrix (DCM) as an array."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._query_direction_cosine_matrix_array_metadata, input_orientation, OutArg())

    _new_cartesian3_vector_metadata = { "offset" : _new_cartesian3_vector_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def new_cartesian3_vector(self) -> "ICartesian3Vector":
        """Create a cartesian vector."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_cartesian3_vector_metadata, OutArg())

    _new_cartesian3_vector_from_direction_metadata = { "offset" : _new_cartesian3_vector_from_direction_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("IDirection"), agmarshall.InterfaceOutArg,) }
    def new_cartesian3_vector_from_direction(self, input_direction:"IDirection") -> "ICartesian3Vector":
        """Convert the direction to cartesian vector."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_cartesian3_vector_from_direction_metadata, input_direction, OutArg())

    _new_cartesian3_vector_from_position_metadata = { "offset" : _new_cartesian3_vector_from_position_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("IPosition"), agmarshall.InterfaceOutArg,) }
    def new_cartesian3_vector_from_position(self, input_position:"IPosition") -> "ICartesian3Vector":
        """Convert the position to cartesian vector."""
        return self._intf.invoke(ConversionUtility._metadata, ConversionUtility._new_cartesian3_vector_from_position_metadata, input_position, OutArg())


    def __init__(self, source_object=None):
        """Construct an object of type ConversionUtility."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ConversionUtility)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ConversionUtility, [ConversionUtility, ])

agcls.AgClassCatalog.add_catalog_entry((5539894848391888927, 9267881117088044206), ConversionUtility)
agcls.AgTypeNameMap["ConversionUtility"] = ConversionUtility

class Quantity(SupportsDeleteCallback):
    """Provide helper methods for a quantity."""

    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_dimension_method_offset = 1
    _get_unit_method_offset = 2
    _convert_to_unit_method_offset = 3
    _get_value_method_offset = 4
    _set_value_method_offset = 5
    _add_method_offset = 6
    _subtract_method_offset = 7
    _multiply_qty_method_offset = 8
    _divide_qty_method_offset = 9
    _metadata = {
        "iid_data" : (4839776343014410790, 5745116756208999326),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Quantity)

    _get_dimension_metadata = { "offset" : _get_dimension_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def dimension(self) -> str:
        """Get the name of the dimension."""
        return self._intf.get_property(Quantity._metadata, Quantity._get_dimension_metadata)

    _get_unit_metadata = { "offset" : _get_unit_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def unit(self) -> str:
        """Get the current Unit abbreviation."""
        return self._intf.get_property(Quantity._metadata, Quantity._get_unit_metadata)

    _convert_to_unit_metadata = { "offset" : _convert_to_unit_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def convert_to_unit(self, unit_abbrv:str) -> None:
        """Change the value in this quantity to the specified unit."""
        return self._intf.invoke(Quantity._metadata, Quantity._convert_to_unit_metadata, unit_abbrv)

    _get_value_metadata = { "offset" : _get_value_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def value(self) -> float:
        """Get or set the current value."""
        return self._intf.get_property(Quantity._metadata, Quantity._get_value_metadata)

    _set_value_metadata = { "offset" : _set_value_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @value.setter
    def value(self, value:float) -> None:
        return self._intf.set_property(Quantity._metadata, Quantity._set_value_metadata, value)

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("Quantity"), agmarshall.InterfaceOutArg,) }
    def add(self, quantity:"Quantity") -> "Quantity":
        """Add the value from the Quantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        return self._intf.invoke(Quantity._metadata, Quantity._add_metadata, quantity, OutArg())

    _subtract_metadata = { "offset" : _subtract_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("Quantity"), agmarshall.InterfaceOutArg,) }
    def subtract(self, quantity:"Quantity") -> "Quantity":
        """Subtracts the value from the Quantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        return self._intf.invoke(Quantity._metadata, Quantity._subtract_metadata, quantity, OutArg())

    _multiply_qty_metadata = { "offset" : _multiply_qty_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("Quantity"), agmarshall.InterfaceOutArg,) }
    def multiply_qty(self, quantity:"Quantity") -> "Quantity":
        """Multiplies the value from the Quantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar."""
        return self._intf.invoke(Quantity._metadata, Quantity._multiply_qty_metadata, quantity, OutArg())

    _divide_qty_metadata = { "offset" : _divide_qty_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("Quantity"), agmarshall.InterfaceOutArg,) }
    def divide_qty(self, quantity:"Quantity") -> "Quantity":
        """Divides the value from the Quantity interface to this interface. The dimensions must be similar."""
        return self._intf.invoke(Quantity._metadata, Quantity._divide_qty_metadata, quantity, OutArg())

    _property_names[dimension] = "dimension"
    _property_names[unit] = "unit"
    _property_names[value] = "value"

    def __init__(self, source_object=None):
        """Construct an object of type Quantity."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Quantity)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Quantity, [Quantity, ])

agcls.AgClassCatalog.add_catalog_entry((4969259561547526744, 4189472907173738428), Quantity)
agcls.AgTypeNameMap["Quantity"] = Quantity

class Date(SupportsDeleteCallback):
    """Provide helper methods for a date."""

    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _format_method_offset = 1
    _set_date_method_offset = 2
    _get_ole_date_method_offset = 3
    _set_ole_date_method_offset = 4
    _get_whole_days_method_offset = 5
    _set_whole_days_method_offset = 6
    _get_sec_into_day_method_offset = 7
    _set_sec_into_day_method_offset = 8
    _get_whole_days_utc_method_offset = 9
    _set_whole_days_utc_method_offset = 10
    _get_sec_into_day_utc_method_offset = 11
    _set_sec_into_day_utc_method_offset = 12
    _add_method_offset = 13
    _subtract_method_offset = 14
    _span_method_offset = 15
    _metadata = {
        "iid_data" : (5143062082172252718, 16663391782392029362),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Date)

    _format_metadata = { "offset" : _format_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg,) }
    def format(self, unit:str) -> str:
        """Return the value of the date given the unit."""
        return self._intf.invoke(Date._metadata, Date._format_metadata, unit, OutArg())

    _set_date_metadata = { "offset" : _set_date_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg,) }
    def set_date(self, unit:str, value:str) -> None:
        """Set this date with the given date value and unit type."""
        return self._intf.invoke(Date._metadata, Date._set_date_metadata, unit, value)

    _get_ole_date_metadata = { "offset" : _get_ole_date_method_offset,
            "arg_types" : (POINTER(agcom.DATE),),
            "marshallers" : (agmarshall.DateArg,) }
    @property
    def ole_date(self) -> datetime:
        """Get or set the current time in OLE DATE Format."""
        return self._intf.get_property(Date._metadata, Date._get_ole_date_metadata)

    _set_ole_date_metadata = { "offset" : _set_ole_date_method_offset,
            "arg_types" : (agcom.DATE,),
            "marshallers" : (agmarshall.DateArg,) }
    @ole_date.setter
    def ole_date(self, value:datetime) -> None:
        return self._intf.set_property(Date._metadata, Date._set_ole_date_metadata, value)

    _get_whole_days_metadata = { "offset" : _get_whole_days_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def whole_days(self) -> int:
        """Get or set the Julian Day Number of the date of interest."""
        return self._intf.get_property(Date._metadata, Date._get_whole_days_metadata)

    _set_whole_days_metadata = { "offset" : _set_whole_days_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @whole_days.setter
    def whole_days(self, whole_days:int) -> None:
        return self._intf.set_property(Date._metadata, Date._set_whole_days_metadata, whole_days)

    _get_sec_into_day_metadata = { "offset" : _get_sec_into_day_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def sec_into_day(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0."""
        return self._intf.get_property(Date._metadata, Date._get_sec_into_day_metadata)

    _set_sec_into_day_metadata = { "offset" : _set_sec_into_day_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @sec_into_day.setter
    def sec_into_day(self, sec_into_day:float) -> None:
        return self._intf.set_property(Date._metadata, Date._set_sec_into_day_metadata, sec_into_day)

    _get_whole_days_utc_metadata = { "offset" : _get_whole_days_utc_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def whole_days_utc(self) -> int:
        """Get or set the UTC Day Number of the date of interest."""
        return self._intf.get_property(Date._metadata, Date._get_whole_days_utc_metadata)

    _set_whole_days_utc_metadata = { "offset" : _set_whole_days_utc_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @whole_days_utc.setter
    def whole_days_utc(self, whole_days:int) -> None:
        return self._intf.set_property(Date._metadata, Date._set_whole_days_utc_metadata, whole_days)

    _get_sec_into_day_utc_metadata = { "offset" : _get_sec_into_day_utc_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def sec_into_day_utc(self) -> float:
        """Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0."""
        return self._intf.get_property(Date._metadata, Date._get_sec_into_day_utc_metadata)

    _set_sec_into_day_utc_metadata = { "offset" : _set_sec_into_day_utc_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @sec_into_day_utc.setter
    def sec_into_day_utc(self, sec_into_day:float) -> None:
        return self._intf.set_property(Date._metadata, Date._set_sec_into_day_utc_metadata, sec_into_day)

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.DoubleArg, agmarshall.InterfaceOutArg,) }
    def add(self, unit:str, value:float) -> "Date":
        """Add the value in the given unit and returns a new date interface."""
        return self._intf.invoke(Date._metadata, Date._add_metadata, unit, value, OutArg())

    _subtract_metadata = { "offset" : _subtract_method_offset,
            "arg_types" : (agcom.BSTR, agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.DoubleArg, agmarshall.InterfaceOutArg,) }
    def subtract(self, unit:str, value:float) -> "Date":
        """Subtracts the value in the given unit and returns a new date interface."""
        return self._intf.invoke(Date._metadata, Date._subtract_metadata, unit, value, OutArg())

    _span_metadata = { "offset" : _span_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("Date"), agmarshall.InterfaceOutArg,) }
    def span(self, date:"Date") -> "Quantity":
        """Subtracts the value from the Date interface and returns an Quantity."""
        return self._intf.invoke(Date._metadata, Date._span_metadata, date, OutArg())

    _property_names[ole_date] = "ole_date"
    _property_names[whole_days] = "whole_days"
    _property_names[sec_into_day] = "sec_into_day"
    _property_names[whole_days_utc] = "whole_days_utc"
    _property_names[sec_into_day_utc] = "sec_into_day_utc"

    def __init__(self, source_object=None):
        """Construct an object of type Date."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Date)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Date, [Date, ])

agcls.AgClassCatalog.add_catalog_entry((5679847419525019692, 5770745202026769536), Date)
agcls.AgTypeNameMap["Date"] = Date

class Position(ILocationData, IPosition, SupportsDeleteCallback):
    """The Position class."""
    def __init__(self, source_object=None):
        """Construct an object of type Position."""
        SupportsDeleteCallback.__init__(self)
        ILocationData.__init__(self, source_object)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        ILocationData._private_init(self, intf)
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Position, [ILocationData, IPosition])

agcls.AgClassCatalog.add_catalog_entry((4903267763032508190, 8061043874875400886), Position)
agcls.AgTypeNameMap["Position"] = Position

class Cartesian(IPosition, SupportsDeleteCallback):
    """Cartesian Interface used to access a position using Cartesian Coordinates."""

    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _get_x_method_offset = 1
    _set_x_method_offset = 2
    _get_y_method_offset = 3
    _set_y_method_offset = 4
    _get_z_method_offset = 5
    _set_z_method_offset = 6
    _metadata = {
        "iid_data" : (4664677019618527909, 4016879878245765533),
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Cartesian)

    _get_x_metadata = { "offset" : _get_x_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def x(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(Cartesian._metadata, Cartesian._get_x_metadata)

    _set_x_metadata = { "offset" : _set_x_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @x.setter
    def x(self, value:float) -> None:
        return self._intf.set_property(Cartesian._metadata, Cartesian._set_x_metadata, value)

    _get_y_metadata = { "offset" : _get_y_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def y(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(Cartesian._metadata, Cartesian._get_y_metadata)

    _set_y_metadata = { "offset" : _set_y_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @y.setter
    def y(self, value:float) -> None:
        return self._intf.set_property(Cartesian._metadata, Cartesian._set_y_metadata, value)

    _get_z_metadata = { "offset" : _get_z_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def z(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(Cartesian._metadata, Cartesian._get_z_metadata)

    _set_z_metadata = { "offset" : _set_z_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @z.setter
    def z(self, value:float) -> None:
        return self._intf.set_property(Cartesian._metadata, Cartesian._set_z_metadata, value)

    _property_names[x] = "x"
    _property_names[y] = "y"
    _property_names[z] = "z"

    def __init__(self, source_object=None):
        """Construct an object of type Cartesian."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Cartesian)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Cartesian, [Cartesian, IPosition])

agcls.AgClassCatalog.add_catalog_entry((5476007582665385228, 1380540108325311903), Cartesian)
agcls.AgTypeNameMap["Cartesian"] = Cartesian

class Geodetic(IPosition, SupportsDeleteCallback):
    """Geodetic sets the position using Geodetic properties."""

    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _get_latitude_method_offset = 1
    _set_latitude_method_offset = 2
    _get_longitude_method_offset = 3
    _set_longitude_method_offset = 4
    _get_altitude_method_offset = 5
    _set_altitude_method_offset = 6
    _metadata = {
        "iid_data" : (5755180572778472763, 8873003113985691520),
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Geodetic)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def latitude(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        return self._intf.get_property(Geodetic._metadata, Geodetic._get_latitude_metadata)

    _set_latitude_metadata = { "offset" : _set_latitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @latitude.setter
    def latitude(self, lat:typing.Any) -> None:
        return self._intf.set_property(Geodetic._metadata, Geodetic._set_latitude_metadata, lat)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def longitude(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        return self._intf.get_property(Geodetic._metadata, Geodetic._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @longitude.setter
    def longitude(self, lon:typing.Any) -> None:
        return self._intf.set_property(Geodetic._metadata, Geodetic._set_longitude_metadata, lon)

    _get_altitude_metadata = { "offset" : _get_altitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def altitude(self) -> float:
        """Altitude. Dimension depends on context."""
        return self._intf.get_property(Geodetic._metadata, Geodetic._get_altitude_metadata)

    _set_altitude_metadata = { "offset" : _set_altitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @altitude.setter
    def altitude(self, alt:float) -> None:
        return self._intf.set_property(Geodetic._metadata, Geodetic._set_altitude_metadata, alt)

    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"
    _property_names[altitude] = "altitude"

    def __init__(self, source_object=None):
        """Construct an object of type Geodetic."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Geodetic)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Geodetic, [Geodetic, IPosition])

agcls.AgClassCatalog.add_catalog_entry((5077970453785586462, 13280626410757950117), Geodetic)
agcls.AgTypeNameMap["Geodetic"] = Geodetic

class Geocentric(IPosition, SupportsDeleteCallback):
    """Geocentric Position Type."""

    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _get_latitude_method_offset = 1
    _set_latitude_method_offset = 2
    _get_longitude_method_offset = 3
    _set_longitude_method_offset = 4
    _get_altitude_method_offset = 5
    _set_altitude_method_offset = 6
    _metadata = {
        "iid_data" : (5321660841076291992, 12202118420183971209),
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Geocentric)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def latitude(self) -> typing.Any:
        """Uses Latitude Dimension."""
        return self._intf.get_property(Geocentric._metadata, Geocentric._get_latitude_metadata)

    _set_latitude_metadata = { "offset" : _set_latitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @latitude.setter
    def latitude(self, value:typing.Any) -> None:
        return self._intf.set_property(Geocentric._metadata, Geocentric._set_latitude_metadata, value)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def longitude(self) -> typing.Any:
        """Uses Longitude Dimension."""
        return self._intf.get_property(Geocentric._metadata, Geocentric._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @longitude.setter
    def longitude(self, value:typing.Any) -> None:
        return self._intf.set_property(Geocentric._metadata, Geocentric._set_longitude_metadata, value)

    _get_altitude_metadata = { "offset" : _get_altitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def altitude(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(Geocentric._metadata, Geocentric._get_altitude_metadata)

    _set_altitude_metadata = { "offset" : _set_altitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @altitude.setter
    def altitude(self, value:float) -> None:
        return self._intf.set_property(Geocentric._metadata, Geocentric._set_altitude_metadata, value)

    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"
    _property_names[altitude] = "altitude"

    def __init__(self, source_object=None):
        """Construct an object of type Geocentric."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Geocentric)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Geocentric, [Geocentric, IPosition])

agcls.AgClassCatalog.add_catalog_entry((4926694488194314560, 14984931694156885123), Geocentric)
agcls.AgTypeNameMap["Geocentric"] = Geocentric

class Planetodetic(IPosition, SupportsDeleteCallback):
    """Planetodetic sets the position using Planetodetic properties."""

    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _get_latitude_method_offset = 1
    _set_latitude_method_offset = 2
    _get_longitude_method_offset = 3
    _set_longitude_method_offset = 4
    _get_altitude_method_offset = 5
    _set_altitude_method_offset = 6
    _metadata = {
        "iid_data" : (4995327019235292843, 11578217686482779582),
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Planetodetic)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def latitude(self) -> typing.Any:
        """Latitude. Uses Latitude Dimension."""
        return self._intf.get_property(Planetodetic._metadata, Planetodetic._get_latitude_metadata)

    _set_latitude_metadata = { "offset" : _set_latitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @latitude.setter
    def latitude(self, lat:typing.Any) -> None:
        return self._intf.set_property(Planetodetic._metadata, Planetodetic._set_latitude_metadata, lat)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def longitude(self) -> typing.Any:
        """Longitude. Uses Longitude Dimension."""
        return self._intf.get_property(Planetodetic._metadata, Planetodetic._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @longitude.setter
    def longitude(self, lon:typing.Any) -> None:
        return self._intf.set_property(Planetodetic._metadata, Planetodetic._set_longitude_metadata, lon)

    _get_altitude_metadata = { "offset" : _get_altitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def altitude(self) -> float:
        """Altitude. Dimension depends on context."""
        return self._intf.get_property(Planetodetic._metadata, Planetodetic._get_altitude_metadata)

    _set_altitude_metadata = { "offset" : _set_altitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @altitude.setter
    def altitude(self, alt:float) -> None:
        return self._intf.set_property(Planetodetic._metadata, Planetodetic._set_altitude_metadata, alt)

    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"
    _property_names[altitude] = "altitude"

    def __init__(self, source_object=None):
        """Construct an object of type Planetodetic."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Planetodetic)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Planetodetic, [Planetodetic, IPosition])

agcls.AgClassCatalog.add_catalog_entry((4789625949537807248, 4321240179333893275), Planetodetic)
agcls.AgTypeNameMap["Planetodetic"] = Planetodetic

class Planetocentric(IPosition, SupportsDeleteCallback):
    """Planetocentric Position Type."""

    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _get_latitude_method_offset = 1
    _set_latitude_method_offset = 2
    _get_longitude_method_offset = 3
    _set_longitude_method_offset = 4
    _get_altitude_method_offset = 5
    _set_altitude_method_offset = 6
    _metadata = {
        "iid_data" : (5231220175109486764, 11935839591636368564),
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Planetocentric)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def latitude(self) -> typing.Any:
        """Uses Latitude Dimension."""
        return self._intf.get_property(Planetocentric._metadata, Planetocentric._get_latitude_metadata)

    _set_latitude_metadata = { "offset" : _set_latitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @latitude.setter
    def latitude(self, value:typing.Any) -> None:
        return self._intf.set_property(Planetocentric._metadata, Planetocentric._set_latitude_metadata, value)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def longitude(self) -> typing.Any:
        """Uses Longitude Dimension."""
        return self._intf.get_property(Planetocentric._metadata, Planetocentric._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @longitude.setter
    def longitude(self, value:typing.Any) -> None:
        return self._intf.set_property(Planetocentric._metadata, Planetocentric._set_longitude_metadata, value)

    _get_altitude_metadata = { "offset" : _get_altitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def altitude(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(Planetocentric._metadata, Planetocentric._get_altitude_metadata)

    _set_altitude_metadata = { "offset" : _set_altitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @altitude.setter
    def altitude(self, value:float) -> None:
        return self._intf.set_property(Planetocentric._metadata, Planetocentric._set_altitude_metadata, value)

    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"
    _property_names[altitude] = "altitude"

    def __init__(self, source_object=None):
        """Construct an object of type Planetocentric."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Planetocentric)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Planetocentric, [Planetocentric, IPosition])

agcls.AgClassCatalog.add_catalog_entry((5020504029532171928, 12730859081806240444), Planetocentric)
agcls.AgTypeNameMap["Planetocentric"] = Planetocentric

class Spherical(IPosition, SupportsDeleteCallback):
    """Spherical Position Type."""

    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _get_latitude_method_offset = 1
    _set_latitude_method_offset = 2
    _get_longitude_method_offset = 3
    _set_longitude_method_offset = 4
    _get_radius_method_offset = 5
    _set_radius_method_offset = 6
    _metadata = {
        "iid_data" : (4843995526478015953, 2468654405511808670),
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Spherical)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def latitude(self) -> typing.Any:
        """Uses Latitude Dimension."""
        return self._intf.get_property(Spherical._metadata, Spherical._get_latitude_metadata)

    _set_latitude_metadata = { "offset" : _set_latitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @latitude.setter
    def latitude(self, value:typing.Any) -> None:
        return self._intf.set_property(Spherical._metadata, Spherical._set_latitude_metadata, value)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def longitude(self) -> typing.Any:
        """Uses Longitude Dimension."""
        return self._intf.get_property(Spherical._metadata, Spherical._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @longitude.setter
    def longitude(self, value:typing.Any) -> None:
        return self._intf.set_property(Spherical._metadata, Spherical._set_longitude_metadata, value)

    _get_radius_metadata = { "offset" : _get_radius_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def radius(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(Spherical._metadata, Spherical._get_radius_metadata)

    _set_radius_metadata = { "offset" : _set_radius_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @radius.setter
    def radius(self, value:float) -> None:
        return self._intf.set_property(Spherical._metadata, Spherical._set_radius_metadata, value)

    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"
    _property_names[radius] = "radius"

    def __init__(self, source_object=None):
        """Construct an object of type Spherical."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Spherical)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Spherical, [Spherical, IPosition])

agcls.AgClassCatalog.add_catalog_entry((5145632099031410238, 4654345009365226685), Spherical)
agcls.AgTypeNameMap["Spherical"] = Spherical

class Cylindrical(IPosition, SupportsDeleteCallback):
    """Cylindrical Position Type."""

    _num_methods = 6
    _vtable_offset = IPosition._vtable_offset + IPosition._num_methods
    _get_radius_method_offset = 1
    _set_radius_method_offset = 2
    _get_z_method_offset = 3
    _set_z_method_offset = 4
    _get_longitude_method_offset = 5
    _set_longitude_method_offset = 6
    _metadata = {
        "iid_data" : (4890168943673034718, 7924545433188815245),
        "vtable_reference" : IPosition._vtable_offset + IPosition._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Cylindrical)

    _get_radius_metadata = { "offset" : _get_radius_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def radius(self) -> float:
        """Dimension depends on context."""
        return self._intf.get_property(Cylindrical._metadata, Cylindrical._get_radius_metadata)

    _set_radius_metadata = { "offset" : _set_radius_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @radius.setter
    def radius(self, value:float) -> None:
        return self._intf.set_property(Cylindrical._metadata, Cylindrical._set_radius_metadata, value)

    _get_z_metadata = { "offset" : _get_z_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def z(self) -> float:
        """Uses Angle Dimension."""
        return self._intf.get_property(Cylindrical._metadata, Cylindrical._get_z_metadata)

    _set_z_metadata = { "offset" : _set_z_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @z.setter
    def z(self, value:float) -> None:
        return self._intf.set_property(Cylindrical._metadata, Cylindrical._set_z_metadata, value)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def longitude(self) -> typing.Any:
        """Dimension depends on context."""
        return self._intf.get_property(Cylindrical._metadata, Cylindrical._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @longitude.setter
    def longitude(self, value:typing.Any) -> None:
        return self._intf.set_property(Cylindrical._metadata, Cylindrical._set_longitude_metadata, value)

    _property_names[radius] = "radius"
    _property_names[z] = "z"
    _property_names[longitude] = "longitude"

    def __init__(self, source_object=None):
        """Construct an object of type Cylindrical."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Cylindrical)
        IPosition.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IPosition._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Cylindrical, [Cylindrical, IPosition])

agcls.AgClassCatalog.add_catalog_entry((4618344560482090476, 3818300535688770476), Cylindrical)
agcls.AgTypeNameMap["Cylindrical"] = Cylindrical

class Direction(IDirection, SupportsDeleteCallback):
    """Class defining direction options for aligned and constrained vectors."""
    def __init__(self, source_object=None):
        """Construct an object of type Direction."""
        SupportsDeleteCallback.__init__(self)
        IDirection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Direction, [IDirection])

agcls.AgClassCatalog.add_catalog_entry((5543184440989437028, 15687242444519207338), Direction)
agcls.AgTypeNameMap["Direction"] = Direction

class DirectionEuler(IDirection, SupportsDeleteCallback):
    """Interface for Euler direction sequence."""

    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _get_b_method_offset = 1
    _set_b_method_offset = 2
    _get_c_method_offset = 3
    _set_c_method_offset = 4
    _get_sequence_method_offset = 5
    _set_sequence_method_offset = 6
    _metadata = {
        "iid_data" : (5120067861098403612, 16675157910874070404),
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DirectionEuler)

    _get_b_metadata = { "offset" : _get_b_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def b(self) -> typing.Any:
        """Euler B angle. Uses Angle Dimension."""
        return self._intf.get_property(DirectionEuler._metadata, DirectionEuler._get_b_metadata)

    _set_b_metadata = { "offset" : _set_b_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @b.setter
    def b(self, va:typing.Any) -> None:
        return self._intf.set_property(DirectionEuler._metadata, DirectionEuler._set_b_metadata, va)

    _get_c_metadata = { "offset" : _get_c_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def c(self) -> typing.Any:
        """Euler C angle. Uses Angle Dimension."""
        return self._intf.get_property(DirectionEuler._metadata, DirectionEuler._get_c_metadata)

    _set_c_metadata = { "offset" : _set_c_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @c.setter
    def c(self, vb:typing.Any) -> None:
        return self._intf.set_property(DirectionEuler._metadata, DirectionEuler._set_c_metadata, vb)

    _get_sequence_metadata = { "offset" : _get_sequence_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(EulerDirectionSequence),) }
    @property
    def sequence(self) -> "EulerDirectionSequence":
        """Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified."""
        return self._intf.get_property(DirectionEuler._metadata, DirectionEuler._get_sequence_metadata)

    _set_sequence_metadata = { "offset" : _set_sequence_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(EulerDirectionSequence),) }
    @sequence.setter
    def sequence(self, sequence:"EulerDirectionSequence") -> None:
        return self._intf.set_property(DirectionEuler._metadata, DirectionEuler._set_sequence_metadata, sequence)

    _property_names[b] = "b"
    _property_names[c] = "c"
    _property_names[sequence] = "sequence"

    def __init__(self, source_object=None):
        """Construct an object of type DirectionEuler."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DirectionEuler)
        IDirection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DirectionEuler, [DirectionEuler, IDirection])

agcls.AgClassCatalog.add_catalog_entry((4656326325412983050, 17465710618493224627), DirectionEuler)
agcls.AgTypeNameMap["DirectionEuler"] = DirectionEuler

class DirectionPR(IDirection, SupportsDeleteCallback):
    """Interface for Pitch-Roll (PR) direction sequence."""

    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _get_pitch_method_offset = 1
    _set_pitch_method_offset = 2
    _get_roll_method_offset = 3
    _set_roll_method_offset = 4
    _get_sequence_method_offset = 5
    _set_sequence_method_offset = 6
    _metadata = {
        "iid_data" : (4656718276851111407, 5112873649160444078),
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DirectionPR)

    _get_pitch_metadata = { "offset" : _get_pitch_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def pitch(self) -> typing.Any:
        """Pitch angle. Uses Angle Dimension."""
        return self._intf.get_property(DirectionPR._metadata, DirectionPR._get_pitch_metadata)

    _set_pitch_metadata = { "offset" : _set_pitch_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @pitch.setter
    def pitch(self, pitch:typing.Any) -> None:
        return self._intf.set_property(DirectionPR._metadata, DirectionPR._set_pitch_metadata, pitch)

    _get_roll_metadata = { "offset" : _get_roll_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def roll(self) -> typing.Any:
        """Roll angle. Uses Angle Dimension."""
        return self._intf.get_property(DirectionPR._metadata, DirectionPR._get_roll_metadata)

    _set_roll_metadata = { "offset" : _set_roll_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @roll.setter
    def roll(self, roll:typing.Any) -> None:
        return self._intf.set_property(DirectionPR._metadata, DirectionPR._set_roll_metadata, roll)

    _get_sequence_metadata = { "offset" : _get_sequence_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(PRSequence),) }
    @property
    def sequence(self) -> "PRSequence":
        """PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified."""
        return self._intf.get_property(DirectionPR._metadata, DirectionPR._get_sequence_metadata)

    _set_sequence_metadata = { "offset" : _set_sequence_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(PRSequence),) }
    @sequence.setter
    def sequence(self, sequence:"PRSequence") -> None:
        return self._intf.set_property(DirectionPR._metadata, DirectionPR._set_sequence_metadata, sequence)

    _property_names[pitch] = "pitch"
    _property_names[roll] = "roll"
    _property_names[sequence] = "sequence"

    def __init__(self, source_object=None):
        """Construct an object of type DirectionPR."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DirectionPR)
        IDirection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DirectionPR, [DirectionPR, IDirection])

agcls.AgClassCatalog.add_catalog_entry((4765442014194737078, 3575547082610573999), DirectionPR)
agcls.AgTypeNameMap["DirectionPR"] = DirectionPR

class DirectionRADec(IDirection, SupportsDeleteCallback):
    """Interface for Spherical direction (Right Ascension and Declination)."""

    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _get_dec_method_offset = 1
    _set_dec_method_offset = 2
    _get_ra_method_offset = 3
    _set_ra_method_offset = 4
    _get_magnitude_method_offset = 5
    _set_magnitude_method_offset = 6
    _metadata = {
        "iid_data" : (5255513060882853966, 7426472758042126763),
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DirectionRADec)

    _get_dec_metadata = { "offset" : _get_dec_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def dec(self) -> typing.Any:
        """Declination: angle above the x-y plane. Uses Latitude Dimension."""
        return self._intf.get_property(DirectionRADec._metadata, DirectionRADec._get_dec_metadata)

    _set_dec_metadata = { "offset" : _set_dec_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @dec.setter
    def dec(self, lat:typing.Any) -> None:
        return self._intf.set_property(DirectionRADec._metadata, DirectionRADec._set_dec_metadata, lat)

    _get_ra_metadata = { "offset" : _get_ra_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def ra(self) -> typing.Any:
        """Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension."""
        return self._intf.get_property(DirectionRADec._metadata, DirectionRADec._get_ra_metadata)

    _set_ra_metadata = { "offset" : _set_ra_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    @ra.setter
    def ra(self, lon:typing.Any) -> None:
        return self._intf.set_property(DirectionRADec._metadata, DirectionRADec._set_ra_metadata, lon)

    _get_magnitude_metadata = { "offset" : _get_magnitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def magnitude(self) -> float:
        """A unitless value that represents magnitude."""
        return self._intf.get_property(DirectionRADec._metadata, DirectionRADec._get_magnitude_metadata)

    _set_magnitude_metadata = { "offset" : _set_magnitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @magnitude.setter
    def magnitude(self, magnitude:float) -> None:
        return self._intf.set_property(DirectionRADec._metadata, DirectionRADec._set_magnitude_metadata, magnitude)

    _property_names[dec] = "dec"
    _property_names[ra] = "ra"
    _property_names[magnitude] = "magnitude"

    def __init__(self, source_object=None):
        """Construct an object of type DirectionRADec."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DirectionRADec)
        IDirection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DirectionRADec, [DirectionRADec, IDirection])

agcls.AgClassCatalog.add_catalog_entry((5029533422370176750, 13677593222416528541), DirectionRADec)
agcls.AgTypeNameMap["DirectionRADec"] = DirectionRADec

class DirectionXYZ(IDirection, SupportsDeleteCallback):
    """Interface for Cartesian direction."""

    _num_methods = 6
    _vtable_offset = IDirection._vtable_offset + IDirection._num_methods
    _get_x_method_offset = 1
    _set_x_method_offset = 2
    _get_y_method_offset = 3
    _set_y_method_offset = 4
    _get_z_method_offset = 5
    _set_z_method_offset = 6
    _metadata = {
        "iid_data" : (5271633318387734883, 7251070032551109279),
        "vtable_reference" : IDirection._vtable_offset + IDirection._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DirectionXYZ)

    _get_x_metadata = { "offset" : _get_x_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def x(self) -> float:
        """X component. Dimensionless."""
        return self._intf.get_property(DirectionXYZ._metadata, DirectionXYZ._get_x_metadata)

    _set_x_metadata = { "offset" : _set_x_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @x.setter
    def x(self, vx:float) -> None:
        return self._intf.set_property(DirectionXYZ._metadata, DirectionXYZ._set_x_metadata, vx)

    _get_y_metadata = { "offset" : _get_y_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def y(self) -> float:
        """Y component. Dimensionless."""
        return self._intf.get_property(DirectionXYZ._metadata, DirectionXYZ._get_y_metadata)

    _set_y_metadata = { "offset" : _set_y_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @y.setter
    def y(self, vy:float) -> None:
        return self._intf.set_property(DirectionXYZ._metadata, DirectionXYZ._set_y_metadata, vy)

    _get_z_metadata = { "offset" : _get_z_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def z(self) -> float:
        """Z component. Dimensionless."""
        return self._intf.get_property(DirectionXYZ._metadata, DirectionXYZ._get_z_metadata)

    _set_z_metadata = { "offset" : _set_z_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @z.setter
    def z(self, vz:float) -> None:
        return self._intf.set_property(DirectionXYZ._metadata, DirectionXYZ._set_z_metadata, vz)

    _property_names[x] = "x"
    _property_names[y] = "y"
    _property_names[z] = "z"

    def __init__(self, source_object=None):
        """Construct an object of type DirectionXYZ."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DirectionXYZ)
        IDirection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDirection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DirectionXYZ, [DirectionXYZ, IDirection])

agcls.AgClassCatalog.add_catalog_entry((5522619834884476326, 212967685867618494), DirectionXYZ)
agcls.AgTypeNameMap["DirectionXYZ"] = DirectionXYZ

class Orientation(IOrientation, SupportsDeleteCallback):
    """Class defining the orientation of an orbit."""
    def __init__(self, source_object=None):
        """Construct an object of type Orientation."""
        SupportsDeleteCallback.__init__(self)
        IOrientation.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Orientation, [IOrientation])

agcls.AgClassCatalog.add_catalog_entry((4657791083284412214, 446798242243343514), Orientation)
agcls.AgTypeNameMap["Orientation"] = Orientation

class OrientationAzEl(IOrientationAzEl, IOrientation, SupportsDeleteCallback):
    """AzEl orientation method."""
    def __init__(self, source_object=None):
        """Construct an object of type OrientationAzEl."""
        SupportsDeleteCallback.__init__(self)
        IOrientationAzEl.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationAzEl._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, OrientationAzEl, [IOrientationAzEl, IOrientation])

agcls.AgClassCatalog.add_catalog_entry((4943993280998572960, 9219980346145398932), OrientationAzEl)
agcls.AgTypeNameMap["OrientationAzEl"] = OrientationAzEl

class OrientationEulerAngles(IOrientationEulerAngles, IOrientation, SupportsDeleteCallback):
    """Euler Angles orientation method."""
    def __init__(self, source_object=None):
        """Construct an object of type OrientationEulerAngles."""
        SupportsDeleteCallback.__init__(self)
        IOrientationEulerAngles.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationEulerAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, OrientationEulerAngles, [IOrientationEulerAngles, IOrientation])

agcls.AgClassCatalog.add_catalog_entry((5323505186834167241, 15446891256313371564), OrientationEulerAngles)
agcls.AgTypeNameMap["OrientationEulerAngles"] = OrientationEulerAngles

class OrientationQuaternion(IOrientationQuaternion, IOrientation, SupportsDeleteCallback):
    """Quaternion orientation method."""
    def __init__(self, source_object=None):
        """Construct an object of type OrientationQuaternion."""
        SupportsDeleteCallback.__init__(self)
        IOrientationQuaternion.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationQuaternion._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, OrientationQuaternion, [IOrientationQuaternion, IOrientation])

agcls.AgClassCatalog.add_catalog_entry((5129641859492381649, 14851164480077184942), OrientationQuaternion)
agcls.AgTypeNameMap["OrientationQuaternion"] = OrientationQuaternion

class OrientationYPRAngles(IOrientationYPRAngles, IOrientation, SupportsDeleteCallback):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, source_object=None):
        """Construct an object of type OrientationYPRAngles."""
        SupportsDeleteCallback.__init__(self)
        IOrientationYPRAngles.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationYPRAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, OrientationYPRAngles, [IOrientationYPRAngles, IOrientation])

agcls.AgClassCatalog.add_catalog_entry((5144566701309896761, 2495531606460782228), OrientationYPRAngles)
agcls.AgTypeNameMap["OrientationYPRAngles"] = OrientationYPRAngles

class DoublesCollection(SupportsDeleteCallback):
    """Represents a collection of doubles."""

    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _get__new_enum_method_offset = 3
    _add_method_offset = 4
    _remove_at_method_offset = 5
    _remove_all_method_offset = 6
    _to_array_method_offset = 7
    _set_at_method_offset = 8
    _metadata = {
        "iid_data" : (5159166046074231158, 4676395751707776654),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DoublesCollection)
    def __iter__(self):
        """Create an iterator for the DoublesCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> float:
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.LongArg, agmarshall.DoubleArg,) }
    def item(self, index:int) -> float:
        """Return a double at a specified position."""
        return self._intf.invoke(DoublesCollection._metadata, DoublesCollection._item_metadata, index, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of items in the collection."""
        return self._intf.get_property(DoublesCollection._metadata, DoublesCollection._get_count_metadata)

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return a collection enumerator."""
        return self._intf.get_property(DoublesCollection._metadata, DoublesCollection._get__new_enum_metadata)

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    def add(self, value:float) -> None:
        """Add a value to the collection of doubles."""
        return self._intf.invoke(DoublesCollection._metadata, DoublesCollection._add_metadata, value)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    def remove_at(self, index:int) -> None:
        """Remove an element from the collection at a specified position."""
        return self._intf.invoke(DoublesCollection._metadata, DoublesCollection._remove_at_metadata, index)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear the collection."""
        return self._intf.invoke(DoublesCollection._metadata, DoublesCollection._remove_all_metadata, )

    _to_array_metadata = { "offset" : _to_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def to_array(self) -> list:
        """Return an array of the elements in the collection."""
        return self._intf.invoke(DoublesCollection._metadata, DoublesCollection._to_array_metadata, OutArg())

    _set_at_metadata = { "offset" : _set_at_method_offset,
            "arg_types" : (agcom.LONG, agcom.DOUBLE,),
            "marshallers" : (agmarshall.LongArg, agmarshall.DoubleArg,) }
    def set_at(self, index:int, value:float) -> None:
        """Update an element in the collection at a specified position."""
        return self._intf.invoke(DoublesCollection._metadata, DoublesCollection._set_at_metadata, index, value)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type DoublesCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DoublesCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DoublesCollection, [DoublesCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5518211324354631135, 2324476080933736880), DoublesCollection)
agcls.AgTypeNameMap["DoublesCollection"] = DoublesCollection

class Cartesian3Vector(ICartesian3Vector, SupportsDeleteCallback):
    """A 3-D cartesian vector."""
    def __init__(self, source_object=None):
        """Construct an object of type Cartesian3Vector."""
        SupportsDeleteCallback.__init__(self)
        ICartesian3Vector.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        ICartesian3Vector._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Cartesian3Vector, [ICartesian3Vector])

agcls.AgClassCatalog.add_catalog_entry((4999830393484217834, 4471742921241496718), Cartesian3Vector)
agcls.AgTypeNameMap["Cartesian3Vector"] = Cartesian3Vector

class Cartesian2Vector(SupportsDeleteCallback):
    """Represents a cartesian 2-D vector."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_x_method_offset = 1
    _set_x_method_offset = 2
    _get_y_method_offset = 3
    _set_y_method_offset = 4
    _get_method_offset = 5
    _set_method_offset = 6
    _to_array_method_offset = 7
    _metadata = {
        "iid_data" : (5272910570004807503, 10054311596169292473),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Cartesian2Vector)

    _get_x_metadata = { "offset" : _get_x_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def x(self) -> float:
        """X coordinate."""
        return self._intf.get_property(Cartesian2Vector._metadata, Cartesian2Vector._get_x_metadata)

    _set_x_metadata = { "offset" : _set_x_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @x.setter
    def x(self, x:float) -> None:
        return self._intf.set_property(Cartesian2Vector._metadata, Cartesian2Vector._set_x_metadata, x)

    _get_y_metadata = { "offset" : _get_y_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def y(self) -> float:
        """Y coordinate."""
        return self._intf.get_property(Cartesian2Vector._metadata, Cartesian2Vector._get_y_metadata)

    _set_y_metadata = { "offset" : _set_y_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @y.setter
    def y(self, y:float) -> None:
        return self._intf.set_property(Cartesian2Vector._metadata, Cartesian2Vector._set_y_metadata, y)

    _get_metadata = { "offset" : _get_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE), POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def get(self) -> typing.Tuple[float, float]:
        """Return cartesian vector."""
        return self._intf.invoke(Cartesian2Vector._metadata, Cartesian2Vector._get_metadata, OutArg(), OutArg())

    _set_metadata = { "offset" : _set_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def set(self, x:float, y:float) -> None:
        """Set cartesian vector."""
        return self._intf.invoke(Cartesian2Vector._metadata, Cartesian2Vector._set_metadata, x, y)

    _to_array_metadata = { "offset" : _to_array_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def to_array(self) -> list:
        """Return coordinates as an array."""
        return self._intf.invoke(Cartesian2Vector._metadata, Cartesian2Vector._to_array_metadata, OutArg())

    _property_names[x] = "x"
    _property_names[y] = "y"

    def __init__(self, source_object=None):
        """Construct an object of type Cartesian2Vector."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Cartesian2Vector)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Cartesian2Vector, [Cartesian2Vector, ])

agcls.AgClassCatalog.add_catalog_entry((5020079430311867935, 9173204252285117336), Cartesian2Vector)
agcls.AgTypeNameMap["Cartesian2Vector"] = Cartesian2Vector

class PropertyInfo(SupportsDeleteCallback):
    """Property information."""

    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _get_property_type_method_offset = 2
    _get_value_method_offset = 3
    _set_value_method_offset = 4
    _get_has_min_method_offset = 5
    _get_has_max_method_offset = 6
    _get_min_method_offset = 7
    _get_max_method_offset = 8
    _metadata = {
        "iid_data" : (5709449963146046365, 5862416140085874335),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, PropertyInfo)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the name of the property."""
        return self._intf.get_property(PropertyInfo._metadata, PropertyInfo._get_name_metadata)

    _get_property_type_metadata = { "offset" : _get_property_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(PropertyInfoValueType),) }
    @property
    def property_type(self) -> "PropertyInfoValueType":
        """Get the type of property."""
        return self._intf.get_property(PropertyInfo._metadata, PropertyInfo._get_property_type_metadata)

    _get_value_metadata = { "offset" : _get_value_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    def get_value(self) -> typing.Any:
        """Get the value of the property. Use PropertyType to determine the type to cast to."""
        return self._intf.invoke(PropertyInfo._metadata, PropertyInfo._get_value_metadata, OutArg())

    _set_value_metadata = { "offset" : _set_value_method_offset,
            "arg_types" : (agcom.Variant,),
            "marshallers" : (agmarshall.VariantArg,) }
    def set_value(self, property_info:typing.Any) -> None:
        """Set the value of the property. Use PropertyType to determine the type to cast to."""
        return self._intf.invoke(PropertyInfo._metadata, PropertyInfo._set_value_metadata, property_info)

    _get_has_min_metadata = { "offset" : _get_has_min_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def has_min(self) -> bool:
        """Determine if the property has a minimum value."""
        return self._intf.get_property(PropertyInfo._metadata, PropertyInfo._get_has_min_metadata)

    _get_has_max_metadata = { "offset" : _get_has_max_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def has_max(self) -> bool:
        """Determine if the property has a maximum value."""
        return self._intf.get_property(PropertyInfo._metadata, PropertyInfo._get_has_max_metadata)

    _get_min_metadata = { "offset" : _get_min_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def min(self) -> typing.Any:
        """Get the minimum value of this property. Use PropertyType to determine the type to cast to."""
        return self._intf.get_property(PropertyInfo._metadata, PropertyInfo._get_min_metadata)

    _get_max_metadata = { "offset" : _get_max_method_offset,
            "arg_types" : (POINTER(agcom.Variant),),
            "marshallers" : (agmarshall.VariantArg,) }
    @property
    def max(self) -> typing.Any:
        """Get the maximum value of this property. Use PropertyType to determine the type to cast to."""
        return self._intf.get_property(PropertyInfo._metadata, PropertyInfo._get_max_metadata)

    _property_names[name] = "name"
    _property_names[property_type] = "property_type"
    _property_names[has_min] = "has_min"
    _property_names[has_max] = "has_max"
    _property_names[min] = "min"
    _property_names[max] = "max"

    def __init__(self, source_object=None):
        """Construct an object of type PropertyInfo."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, PropertyInfo)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, PropertyInfo, [PropertyInfo, ])

agcls.AgClassCatalog.add_catalog_entry((5624653087871619118, 4148759758090164110), PropertyInfo)
agcls.AgTypeNameMap["PropertyInfo"] = PropertyInfo

class PropertyInfoCollection(SupportsDeleteCallback):
    """The collection of properties."""

    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get__new_enum_method_offset = 2
    _get_count_method_offset = 3
    _get_item_by_index_method_offset = 4
    _get_item_by_name_method_offset = 5
    _metadata = {
        "iid_data" : (5183620403292925645, 11703217979470873482),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, PropertyInfoCollection)
    def __iter__(self):
        """Create an iterator for the PropertyInfoCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "PropertyInfo":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def item(self, index_or_name:typing.Any) -> "PropertyInfo":
        """Allow the user to iterate through the properties."""
        return self._intf.invoke(PropertyInfoCollection._metadata, PropertyInfoCollection._item_metadata, index_or_name, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Enumerates through the properties."""
        return self._intf.get_property(PropertyInfoCollection._metadata, PropertyInfoCollection._get__new_enum_metadata)

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Get the number of properties available."""
        return self._intf.get_property(PropertyInfoCollection._metadata, PropertyInfoCollection._get_count_metadata)

    _get_item_by_index_metadata = { "offset" : _get_item_by_index_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "PropertyInfo":
        """Retrieve a property from the collection by index."""
        return self._intf.invoke(PropertyInfoCollection._metadata, PropertyInfoCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "offset" : _get_item_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "PropertyInfo":
        """Retrieve a property from the collection by name."""
        return self._intf.invoke(PropertyInfoCollection._metadata, PropertyInfoCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item


    _property_names[_new_enum] = "_new_enum"
    _property_names[count] = "count"

    def __init__(self, source_object=None):
        """Construct an object of type PropertyInfoCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, PropertyInfoCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, PropertyInfoCollection, [PropertyInfoCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5239823179109569743, 18033180869792707228), PropertyInfoCollection)
agcls.AgTypeNameMap["PropertyInfoCollection"] = PropertyInfoCollection

class RuntimeTypeInfo(SupportsDeleteCallback):
    """Interface used to retrieve the properties at runtime."""

    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_properties_method_offset = 1
    _get_is_collection_method_offset = 2
    _get_count_method_offset = 3
    _get_item_method_offset = 4
    _metadata = {
        "iid_data" : (5445061941216308710, 10476542387161536171),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RuntimeTypeInfo)

    _get_properties_metadata = { "offset" : _get_properties_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def properties(self) -> "PropertyInfoCollection":
        """Get the collection of properties."""
        return self._intf.get_property(RuntimeTypeInfo._metadata, RuntimeTypeInfo._get_properties_metadata)

    _get_is_collection_metadata = { "offset" : _get_is_collection_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_collection(self) -> bool:
        """Determine if the interface is a collection."""
        return self._intf.get_property(RuntimeTypeInfo._metadata, RuntimeTypeInfo._get_is_collection_metadata)

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """If the interface is a collection, returns the collection count."""
        return self._intf.get_property(RuntimeTypeInfo._metadata, RuntimeTypeInfo._get_count_metadata)

    _get_item_metadata = { "offset" : _get_item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LongArg, agmarshall.InterfaceOutArg,) }
    def get_item(self, index:int) -> "PropertyInfo":
        """Return the property of the collection at the given index."""
        return self._intf.invoke(RuntimeTypeInfo._metadata, RuntimeTypeInfo._get_item_metadata, index, OutArg())

    _property_names[properties] = "properties"
    _property_names[is_collection] = "is_collection"
    _property_names[count] = "count"

    def __init__(self, source_object=None):
        """Construct an object of type RuntimeTypeInfo."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RuntimeTypeInfo)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RuntimeTypeInfo, [RuntimeTypeInfo, ])

agcls.AgClassCatalog.add_catalog_entry((5085516699645273237, 15111374025420939179), RuntimeTypeInfo)
agcls.AgTypeNameMap["RuntimeTypeInfo"] = RuntimeTypeInfo

class CommRadOrientationAzEl(IOrientationAzEl, IOrientation, IOrientationPositionOffset, SupportsDeleteCallback):
    """AzEl orientation method."""
    def __init__(self, source_object=None):
        """Construct an object of type CommRadOrientationAzEl."""
        SupportsDeleteCallback.__init__(self)
        IOrientationAzEl.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
        IOrientationPositionOffset.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationAzEl._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommRadOrientationAzEl, [IOrientationAzEl, IOrientation, IOrientationPositionOffset])

agcls.AgClassCatalog.add_catalog_entry((5496216944672659152, 12932999778863326882), CommRadOrientationAzEl)
agcls.AgTypeNameMap["CommRadOrientationAzEl"] = CommRadOrientationAzEl

class CommRadOrientationEulerAngles(IOrientationEulerAngles, IOrientation, IOrientationPositionOffset, SupportsDeleteCallback):
    """Euler Angles orientation method."""
    def __init__(self, source_object=None):
        """Construct an object of type CommRadOrientationEulerAngles."""
        SupportsDeleteCallback.__init__(self)
        IOrientationEulerAngles.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
        IOrientationPositionOffset.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationEulerAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommRadOrientationEulerAngles, [IOrientationEulerAngles, IOrientation, IOrientationPositionOffset])

agcls.AgClassCatalog.add_catalog_entry((5587391684415620486, 8349151267853573270), CommRadOrientationEulerAngles)
agcls.AgTypeNameMap["CommRadOrientationEulerAngles"] = CommRadOrientationEulerAngles

class CommRadOrientationQuaternion(IOrientationQuaternion, IOrientation, IOrientationPositionOffset, SupportsDeleteCallback):
    """Quaternion orientation method."""
    def __init__(self, source_object=None):
        """Construct an object of type CommRadOrientationQuaternion."""
        SupportsDeleteCallback.__init__(self)
        IOrientationQuaternion.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
        IOrientationPositionOffset.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationQuaternion._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommRadOrientationQuaternion, [IOrientationQuaternion, IOrientation, IOrientationPositionOffset])

agcls.AgClassCatalog.add_catalog_entry((5498453980279883775, 11762246145700755869), CommRadOrientationQuaternion)
agcls.AgTypeNameMap["CommRadOrientationQuaternion"] = CommRadOrientationQuaternion

class CommRadOrientationYPRAngles(IOrientationYPRAngles, IOrientation, IOrientationPositionOffset, SupportsDeleteCallback):
    """Yaw-Pitch Roll (YPR) Angles orientation system."""
    def __init__(self, source_object=None):
        """Construct an object of type CommRadOrientationYPRAngles."""
        SupportsDeleteCallback.__init__(self)
        IOrientationYPRAngles.__init__(self, source_object)
        IOrientation.__init__(self, source_object)
        IOrientationPositionOffset.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IOrientationYPRAngles._private_init(self, intf)
        IOrientation._private_init(self, intf)
        IOrientationPositionOffset._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommRadOrientationYPRAngles, [IOrientationYPRAngles, IOrientation, IOrientationPositionOffset])

agcls.AgClassCatalog.add_catalog_entry((4971420367151630190, 4339807439705369485), CommRadOrientationYPRAngles)
agcls.AgTypeNameMap["CommRadOrientationYPRAngles"] = CommRadOrientationYPRAngles

class CommRadOrientationOffsetCart(ICartesian3Vector, SupportsDeleteCallback):
    """Orientation offset cartesian."""
    def __init__(self, source_object=None):
        """Construct an object of type CommRadOrientationOffsetCart."""
        SupportsDeleteCallback.__init__(self)
        ICartesian3Vector.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        ICartesian3Vector._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommRadOrientationOffsetCart, [ICartesian3Vector])

agcls.AgClassCatalog.add_catalog_entry((5035051098943192979, 5602065750200574353), CommRadOrientationOffsetCart)
agcls.AgTypeNameMap["CommRadOrientationOffsetCart"] = CommRadOrientationOffsetCart