
The ``STKUtil`` module
======================


.. py::module:: ansys.stk.core.stkutil


Summary
-------

.. tab-set::
    .. tab-items:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~ILocationData`
              - Base interface IAgLocationData. IAgPosition derives from this interface.

            * - :pyclass:`~IPosition`
              - IAgPosition provides access to the position of the object.

            * - :pyclass:`~IPlanetocentric`
              - Planetocentric Position Type.

            * - :pyclass:`~IGeocentric`
              - Geocentric Position Type.

            * - :pyclass:`~ISpherical`
              - Spherical Position Type.

            * - :pyclass:`~ICylindrical`
              - Cylindrical Position Type.

            * - :pyclass:`~ICartesian`
              - IAgCartesian Interface used to access a position using Cartesian Coordinates.

            * - :pyclass:`~IGeodetic`
              - IAgGeodetic sets the position using Geodetic properties.

            * - :pyclass:`~IPlanetodetic`
              - IAgPlanetodetic sets the position using Planetodetic properties.

            * - :pyclass:`~IDirection`
              - Interface to set and retrieve direction options for aligned and constrained vectors.

            * - :pyclass:`~IDirectionEuler`
              - Interface for Euler direction sequence.

            * - :pyclass:`~IDirectionPR`
              - Interface for Pitch-Roll (PR) direction sequence.

            * - :pyclass:`~IDirectionRADec`
              - Interface for Spherical direction (Right Ascension and Declination).

            * - :pyclass:`~IDirectionXYZ`
              - Interface for Cartesian direction.

            * - :pyclass:`~ICartesian3Vector`
              - Represents a cartesian 3-D vector.

            * - :pyclass:`~IOrientation`
              - Interface to set and retrieve the orientation method.

            * - :pyclass:`~IOrientationAzEl`
              - Interface for AzEl orientation method.

            * - :pyclass:`~IOrientationEulerAngles`
              - Interface for Euler Angles orientation method.

            * - :pyclass:`~IOrientationQuaternion`
              - Quaternion representing orientation between two sets of axes.

            * - :pyclass:`~IOrientationYPRAngles`
              - Interface for Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :pyclass:`~IOrientationPositionOffset`
              - Interface for defining the orientation origin position offset relative to the parent object.

            * - :pyclass:`~IOrbitState`
              - Interface to set and retrieve the coordinate type used to specify the orbit state.

            * - :pyclass:`~ICartesian2Vector`
              - Represents a cartesian 2-D vector.

            * - :pyclass:`~IUnitPreferencesDimension`
              - Provide info on a Dimension from the global unit table.

            * - :pyclass:`~IPropertyInfo`
              - Property information.

            * - :pyclass:`~IPropertyInfoCollection`
              - The collection of properties.

            * - :pyclass:`~IRuntimeTypeInfo`
              - Interface used to retrieve the properties at runtime.

            * - :pyclass:`~IRuntimeTypeInfoProvider`
              - Access point for IAgRuntimeTypeInfo.

            * - :pyclass:`~IExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :pyclass:`~IExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :pyclass:`~IUnitPreferencesUnit`
              - Provide info about a unit.

            * - :pyclass:`~IUnitPreferencesUnitCollection`
              - Provide access to the Unit collection.

            * - :pyclass:`~IUnitPreferencesDimensionCollection`
              - Provide accesses to the global unit table.

            * - :pyclass:`~IQuantity`
              - Provide helper methods for a quantity.

            * - :pyclass:`~IDate`
              - Provide helper methods for a date.

            * - :pyclass:`~IConversionUtility`
              - Provide conversion utilities.

            * - :pyclass:`~IDoublesCollection`
              - Represents a collection of doubles.

    
    .. tab-items:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~ExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :pyclass:`~ExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :pyclass:`~UnitPreferencesUnit`
              - Object that contains info on the unit.

            * - :pyclass:`~UnitPreferencesUnitCollection`
              - Object that contains a collection of IAgUnitPrefsUnit.

            * - :pyclass:`~UnitPreferencesDimension`
              - Object that contains info on the Dimension.

            * - :pyclass:`~UnitPreferencesDimensionCollection`
              - Object that contains a collection of dimensions.

            * - :pyclass:`~ConversionUtility`
              - Object that contains a unit conversion utility.

            * - :pyclass:`~Quantity`
              - Object that contains a quantity.

            * - :pyclass:`~Date`
              - Object that contains a date.

            * - :pyclass:`~Position`
              - The Position class.

            * - :pyclass:`~Cartesian`
              - Class used to access a position using Cartesian Coordinates.

            * - :pyclass:`~Geodetic`
              - Class defining Geodetic position.

            * - :pyclass:`~Geocentric`
              - Class defining Geocentric position.

            * - :pyclass:`~Planetodetic`
              - Class defining Planetodetic position.

            * - :pyclass:`~Planetocentric`
              - Class defining Planetocentric position.

            * - :pyclass:`~Spherical`
              - Class defining spherical position.

            * - :pyclass:`~Cylindrical`
              - Class defining cylindrical position.

            * - :pyclass:`~Direction`
              - Class defining direction options for aligned and constrained vectors.

            * - :pyclass:`~DirectionEuler`
              - Euler direction sequence.

            * - :pyclass:`~DirectionPR`
              - Pitch-Roll (PR) direction sequence.

            * - :pyclass:`~DirectionRADec`
              - Spherical direction (Right Ascension and Declination).

            * - :pyclass:`~DirectionXYZ`
              - Cartesian direction.

            * - :pyclass:`~Orientation`
              - Class defining the orientation of an orbit.

            * - :pyclass:`~OrientationAzEl`
              - AzEl orientation method.

            * - :pyclass:`~OrientationEulerAngles`
              - Euler Angles orientation method.

            * - :pyclass:`~OrientationQuaternion`
              - Quaternion orientation method.

            * - :pyclass:`~OrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :pyclass:`~DoublesCollection`
              - A collection of doubles.

            * - :pyclass:`~Cartesian3Vector`
              - A 3-D cartesian vector.

            * - :pyclass:`~Cartesian2Vector`
              - A 2-D cartesian vector.

            * - :pyclass:`~PropertyInfo`
              - Property Information coclass.

            * - :pyclass:`~PropertyInfoCollection`
              - Property Information Collection coclass.

            * - :pyclass:`~RuntimeTypeInfo`
              - Runtime Type info coclass.

            * - :pyclass:`~CROrientationAzEl`
              - AzEl orientation method.

            * - :pyclass:`~CROrientationEulerAngles`
              - Euler Angles orientation method.

            * - :pyclass:`~CROrientationQuaternion`
              - Quaternion orientation method.

            * - :pyclass:`~CROrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :pyclass:`~CROrientationOffsetCart`
              - Orientation offset cartesian.


    .. tab-items:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~POSITION_TYPE`
              - Facility/place/target position types.

            * - :pyclass:`~EULER_DIRECTION_SEQUENCE`
              - Euler direction sequences.

            * - :pyclass:`~DIRECTION_TYPE`
              - Direction options for aligned and constrained vectors.

            * - :pyclass:`~PR_SEQUENCE`
              - Pitch-Roll (PR) direction sequences.

            * - :pyclass:`~ORIENTATION_TYPE`
              - Orientation methods.

            * - :pyclass:`~AZ_EL_ABOUT_BORESIGHT`
              - About Boresight options for AzEl orientation method.

            * - :pyclass:`~EULER_ORIENTATION_SEQUENCE`
              - Euler rotation sequence options:.

            * - :pyclass:`~YPR_ANGLES_SEQUENCE`
              - Yaw-Pitch-Roll (YPR) sequences.

            * - :pyclass:`~ORBIT_STATE_TYPE`
              - Coordinate types used in specifying orbit state.

            * - :pyclass:`~COORDINATE_SYSTEM`
              - Earth-centered coordinate systems for defining certain propagators.

            * - :pyclass:`~LOG_MSG_TYPE`
              - Log message types.

            * - :pyclass:`~LOG_MSG_DISP_ID`
              - Log message destination options.

            * - :pyclass:`~LINE_STYLE`
              - Line Style.

            * - :pyclass:`~EXEC_MULTI_CMD_RESULT_ACTION`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :pyclass:`~FILL_STYLE`
              - Fill Style.

            * - :pyclass:`~PROPERTY_INFO_VALUE_TYPE`
              - The enumeration used to determine what type of property is being used.



Description
-----------

Objects and enumerations shared by the STK X and STK Objects libraries.

The
types provided by STK Util are used indirectly through methods and properties
in the STK X and STK Objects libraries.

Detail
------

.. py:currentmodule:: ansys.stk.core.stkutil


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> ILocationData<ILocationData>
    --> IPosition<IPosition>
    --> IPlanetocentric<IPlanetocentric>
    --> IGeocentric<IGeocentric>
    --> ISpherical<ISpherical>
    --> ICylindrical<ICylindrical>
    --> ICartesian<ICartesian>
    --> IGeodetic<IGeodetic>
    --> IPlanetodetic<IPlanetodetic>
    --> IDirection<IDirection>
    --> IDirectionEuler<IDirectionEuler>
    --> IDirectionPR<IDirectionPR>
    --> IDirectionRADec<IDirectionRADec>
    --> IDirectionXYZ<IDirectionXYZ>
    --> ICartesian3Vector<ICartesian3Vector>
    --> IOrientation<IOrientation>
    --> IOrientationAzEl<IOrientationAzEl>
    --> IOrientationEulerAngles<IOrientationEulerAngles>
    --> IOrientationQuaternion<IOrientationQuaternion>
    --> IOrientationYPRAngles<IOrientationYPRAngles>
    --> IOrientationPositionOffset<IOrientationPositionOffset>
    --> IOrbitState<IOrbitState>
    --> ICartesian2Vector<ICartesian2Vector>
    --> IUnitPreferencesDimension<IUnitPreferencesDimension>
    --> IPropertyInfo<IPropertyInfo>
    --> IPropertyInfoCollection<IPropertyInfoCollection>
    --> IRuntimeTypeInfo<IRuntimeTypeInfo>
    --> IRuntimeTypeInfoProvider<IRuntimeTypeInfoProvider>
    --> IExecCmdResult<IExecCmdResult>
    --> IExecMultiCmdResult<IExecMultiCmdResult>
    --> IUnitPreferencesUnit<IUnitPreferencesUnit>
    --> IUnitPreferencesUnitCollection<IUnitPreferencesUnitCollection>
    --> IUnitPreferencesDimensionCollection<IUnitPreferencesDimensionCollection>
    --> IQuantity<IQuantity>
    --> IDate<IDate>
    --> IConversionUtility<IConversionUtility>
    --> IDoublesCollection<IDoublesCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> ExecCmdResult<>
    --> ExecMultiCmdResult<>
    --> UnitPreferencesUnit<>
    --> UnitPreferencesUnitCollection<>
    --> UnitPreferencesDimension<>
    --> UnitPreferencesDimensionCollection<>
    --> ConversionUtility<>
    --> Quantity<>
    --> Date<>
    --> Position<>
    --> Cartesian<>
    --> Geodetic<>
    --> Geocentric<>
    --> Planetodetic<>
    --> Planetocentric<>
    --> Spherical<>
    --> Cylindrical<>
    --> Direction<>
    --> DirectionEuler<>
    --> DirectionPR<>
    --> DirectionRADec<>
    --> DirectionXYZ<>
    --> Orientation<>
    --> OrientationAzEl<>
    --> OrientationEulerAngles<>
    --> OrientationQuaternion<>
    --> OrientationYPRAngles<>
    --> DoublesCollection<>
    --> Cartesian3Vector<>
    --> Cartesian2Vector<>
    --> PropertyInfo<>
    --> PropertyInfoCollection<>
    --> RuntimeTypeInfo<>
    --> CROrientationAzEl<>
    --> CROrientationEulerAngles<>
    --> CROrientationQuaternion<>
    --> CROrientationYPRAngles<>
    --> CROrientationOffsetCart<>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ POSITION_TYPE<POSITION_TYPE>
    ≔ EULER_DIRECTION_SEQUENCE<EULER_DIRECTION_SEQUENCE>
    ≔ DIRECTION_TYPE<DIRECTION_TYPE>
    ≔ PR_SEQUENCE<PR_SEQUENCE>
    ≔ ORIENTATION_TYPE<ORIENTATION_TYPE>
    ≔ AZ_EL_ABOUT_BORESIGHT<AZ_EL_ABOUT_BORESIGHT>
    ≔ EULER_ORIENTATION_SEQUENCE<EULER_ORIENTATION_SEQUENCE>
    ≔ YPR_ANGLES_SEQUENCE<YPR_ANGLES_SEQUENCE>
    ≔ ORBIT_STATE_TYPE<ORBIT_STATE_TYPE>
    ≔ COORDINATE_SYSTEM<COORDINATE_SYSTEM>
    ≔ LOG_MSG_TYPE<LOG_MSG_TYPE>
    ≔ LOG_MSG_DISP_ID<LOG_MSG_DISP_ID>
    ≔ LINE_STYLE<LINE_STYLE>
    ≔ EXEC_MULTI_CMD_RESULT_ACTION<EXEC_MULTI_CMD_RESULT_ACTION>
    ≔ FILL_STYLE<FILL_STYLE>
    ≔ PROPERTY_INFO_VALUE_TYPE<PROPERTY_INFO_VALUE_TYPE>

