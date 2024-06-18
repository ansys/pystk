
The ``stkutil`` module
======================


.. py:module:: ansys.stk.core.stkutil


Summary
-------

.. tab-set::
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ILocationData`
              - Base interface IAgLocationData. IAgPosition derives from this interface.

            * - :py:class:`~IPosition`
              - IAgPosition provides access to the position of the object.

            * - :py:class:`~IPlanetocentric`
              - Planetocentric Position Type.

            * - :py:class:`~IGeocentric`
              - Geocentric Position Type.

            * - :py:class:`~ISpherical`
              - Spherical Position Type.

            * - :py:class:`~ICylindrical`
              - Cylindrical Position Type.

            * - :py:class:`~ICartesian`
              - IAgCartesian Interface used to access a position using Cartesian Coordinates.

            * - :py:class:`~IGeodetic`
              - IAgGeodetic sets the position using Geodetic properties.

            * - :py:class:`~IPlanetodetic`
              - IAgPlanetodetic sets the position using Planetodetic properties.

            * - :py:class:`~IDirection`
              - Interface to set and retrieve direction options for aligned and constrained vectors.

            * - :py:class:`~IDirectionEuler`
              - Interface for Euler direction sequence.

            * - :py:class:`~IDirectionPR`
              - Interface for Pitch-Roll (PR) direction sequence.

            * - :py:class:`~IDirectionRADec`
              - Interface for Spherical direction (Right Ascension and Declination).

            * - :py:class:`~IDirectionXYZ`
              - Interface for Cartesian direction.

            * - :py:class:`~ICartesian3Vector`
              - Represents a cartesian 3-D vector.

            * - :py:class:`~IOrientation`
              - Interface to set and retrieve the orientation method.

            * - :py:class:`~IOrientationAzEl`
              - Interface for AzEl orientation method.

            * - :py:class:`~IOrientationEulerAngles`
              - Interface for Euler Angles orientation method.

            * - :py:class:`~IOrientationQuaternion`
              - Quaternion representing orientation between two sets of axes.

            * - :py:class:`~IOrientationYPRAngles`
              - Interface for Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~IOrientationPositionOffset`
              - Interface for defining the orientation origin position offset relative to the parent object.

            * - :py:class:`~IOrbitState`
              - Interface to set and retrieve the coordinate type used to specify the orbit state.

            * - :py:class:`~ICartesian2Vector`
              - Represents a cartesian 2-D vector.

            * - :py:class:`~IUnitPreferencesDimension`
              - Provide info on a Dimension from the global unit table.

            * - :py:class:`~IPropertyInfo`
              - Property information.

            * - :py:class:`~IPropertyInfoCollection`
              - The collection of properties.

            * - :py:class:`~IRuntimeTypeInfo`
              - Interface used to retrieve the properties at runtime.

            * - :py:class:`~IRuntimeTypeInfoProvider`
              - Access point for IAgRuntimeTypeInfo.

            * - :py:class:`~IExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~IExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~IUnitPreferencesUnit`
              - Provide info about a unit.

            * - :py:class:`~IUnitPreferencesUnitCollection`
              - Provide access to the Unit collection.

            * - :py:class:`~IUnitPreferencesDimensionCollection`
              - Provide accesses to the global unit table.

            * - :py:class:`~IQuantity`
              - Provide helper methods for a quantity.

            * - :py:class:`~IDate`
              - Provide helper methods for a date.

            * - :py:class:`~IConversionUtility`
              - Provide conversion utilities.

            * - :py:class:`~IDoublesCollection`
              - Represents a collection of doubles.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~ExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~UnitPreferencesUnit`
              - Object that contains info on the unit.

            * - :py:class:`~UnitPreferencesUnitCollection`
              - Object that contains a collection of IAgUnitPrefsUnit.

            * - :py:class:`~UnitPreferencesDimension`
              - Object that contains info on the Dimension.

            * - :py:class:`~UnitPreferencesDimensionCollection`
              - Object that contains a collection of dimensions.

            * - :py:class:`~ConversionUtility`
              - Object that contains a unit conversion utility.

            * - :py:class:`~Quantity`
              - Object that contains a quantity.

            * - :py:class:`~Date`
              - Object that contains a date.

            * - :py:class:`~Position`
              - The Position class.

            * - :py:class:`~Cartesian`
              - Class used to access a position using Cartesian Coordinates.

            * - :py:class:`~Geodetic`
              - Class defining Geodetic position.

            * - :py:class:`~Geocentric`
              - Class defining Geocentric position.

            * - :py:class:`~Planetodetic`
              - Class defining Planetodetic position.

            * - :py:class:`~Planetocentric`
              - Class defining Planetocentric position.

            * - :py:class:`~Spherical`
              - Class defining spherical position.

            * - :py:class:`~Cylindrical`
              - Class defining cylindrical position.

            * - :py:class:`~Direction`
              - Class defining direction options for aligned and constrained vectors.

            * - :py:class:`~DirectionEuler`
              - Euler direction sequence.

            * - :py:class:`~DirectionPR`
              - Pitch-Roll (PR) direction sequence.

            * - :py:class:`~DirectionRADec`
              - Spherical direction (Right Ascension and Declination).

            * - :py:class:`~DirectionXYZ`
              - Cartesian direction.

            * - :py:class:`~Orientation`
              - Class defining the orientation of an orbit.

            * - :py:class:`~OrientationAzEl`
              - AzEl orientation method.

            * - :py:class:`~OrientationEulerAngles`
              - Euler Angles orientation method.

            * - :py:class:`~OrientationQuaternion`
              - Quaternion orientation method.

            * - :py:class:`~OrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~DoublesCollection`
              - A collection of doubles.

            * - :py:class:`~Cartesian3Vector`
              - A 3-D cartesian vector.

            * - :py:class:`~Cartesian2Vector`
              - A 2-D cartesian vector.

            * - :py:class:`~PropertyInfo`
              - Property Information coclass.

            * - :py:class:`~PropertyInfoCollection`
              - Property Information Collection coclass.

            * - :py:class:`~RuntimeTypeInfo`
              - Runtime Type info coclass.

            * - :py:class:`~CROrientationAzEl`
              - AzEl orientation method.

            * - :py:class:`~CROrientationEulerAngles`
              - Euler Angles orientation method.

            * - :py:class:`~CROrientationQuaternion`
              - Quaternion orientation method.

            * - :py:class:`~CROrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~CROrientationOffsetCart`
              - Orientation offset cartesian.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~POSITION_TYPE`
              - Facility/place/target position types.

            * - :py:class:`~EULER_DIRECTION_SEQUENCE`
              - Euler direction sequences.

            * - :py:class:`~DIRECTION_TYPE`
              - Direction options for aligned and constrained vectors.

            * - :py:class:`~PR_SEQUENCE`
              - Pitch-Roll (PR) direction sequences.

            * - :py:class:`~ORIENTATION_TYPE`
              - Orientation methods.

            * - :py:class:`~AZ_EL_ABOUT_BORESIGHT`
              - About Boresight options for AzEl orientation method.

            * - :py:class:`~EULER_ORIENTATION_SEQUENCE`
              - Euler rotation sequence options:.

            * - :py:class:`~YPR_ANGLES_SEQUENCE`
              - Yaw-Pitch-Roll (YPR) sequences.

            * - :py:class:`~ORBIT_STATE_TYPE`
              - Coordinate types used in specifying orbit state.

            * - :py:class:`~COORDINATE_SYSTEM`
              - Earth-centered coordinate systems for defining certain propagators.

            * - :py:class:`~LOG_MSG_TYPE`
              - Log message types.

            * - :py:class:`~LOG_MSG_DISP_ID`
              - Log message destination options.

            * - :py:class:`~LINE_STYLE`
              - Line Style.

            * - :py:class:`~EXEC_MULTI_CMD_RESULT_ACTION`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :py:class:`~FILL_STYLE`
              - Fill Style.

            * - :py:class:`~PROPERTY_INFO_VALUE_TYPE`
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

     ILocationData<stkutil\ILocationData>
     IPosition<stkutil\IPosition>
     IPlanetocentric<stkutil\IPlanetocentric>
     IGeocentric<stkutil\IGeocentric>
     ISpherical<stkutil\ISpherical>
     ICylindrical<stkutil\ICylindrical>
     ICartesian<stkutil\ICartesian>
     IGeodetic<stkutil\IGeodetic>
     IPlanetodetic<stkutil\IPlanetodetic>
     IDirection<stkutil\IDirection>
     IDirectionEuler<stkutil\IDirectionEuler>
     IDirectionPR<stkutil\IDirectionPR>
     IDirectionRADec<stkutil\IDirectionRADec>
     IDirectionXYZ<stkutil\IDirectionXYZ>
     ICartesian3Vector<stkutil\ICartesian3Vector>
     IOrientation<stkutil\IOrientation>
     IOrientationAzEl<stkutil\IOrientationAzEl>
     IOrientationEulerAngles<stkutil\IOrientationEulerAngles>
     IOrientationQuaternion<stkutil\IOrientationQuaternion>
     IOrientationYPRAngles<stkutil\IOrientationYPRAngles>
     IOrientationPositionOffset<stkutil\IOrientationPositionOffset>
     IOrbitState<stkutil\IOrbitState>
     ICartesian2Vector<stkutil\ICartesian2Vector>
     IUnitPreferencesDimension<stkutil\IUnitPreferencesDimension>
     IPropertyInfo<stkutil\IPropertyInfo>
     IPropertyInfoCollection<stkutil\IPropertyInfoCollection>
     IRuntimeTypeInfo<stkutil\IRuntimeTypeInfo>
     IRuntimeTypeInfoProvider<stkutil\IRuntimeTypeInfoProvider>
     IExecCmdResult<stkutil\IExecCmdResult>
     IExecMultiCmdResult<stkutil\IExecMultiCmdResult>
     IUnitPreferencesUnit<stkutil\IUnitPreferencesUnit>
     IUnitPreferencesUnitCollection<stkutil\IUnitPreferencesUnitCollection>
     IUnitPreferencesDimensionCollection<stkutil\IUnitPreferencesDimensionCollection>
     IQuantity<stkutil\IQuantity>
     IDate<stkutil\IDate>
     IConversionUtility<stkutil\IConversionUtility>
     IDoublesCollection<stkutil\IDoublesCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ExecCmdResult<stkutil\ExecCmdResult>
     ExecMultiCmdResult<stkutil\ExecMultiCmdResult>
     UnitPreferencesUnit<stkutil\UnitPreferencesUnit>
     UnitPreferencesUnitCollection<stkutil\UnitPreferencesUnitCollection>
     UnitPreferencesDimension<stkutil\UnitPreferencesDimension>
     UnitPreferencesDimensionCollection<stkutil\UnitPreferencesDimensionCollection>
     ConversionUtility<stkutil\ConversionUtility>
     Quantity<stkutil\Quantity>
     Date<stkutil\Date>
     Position<stkutil\Position>
     Cartesian<stkutil\Cartesian>
     Geodetic<stkutil\Geodetic>
     Geocentric<stkutil\Geocentric>
     Planetodetic<stkutil\Planetodetic>
     Planetocentric<stkutil\Planetocentric>
     Spherical<stkutil\Spherical>
     Cylindrical<stkutil\Cylindrical>
     Direction<stkutil\Direction>
     DirectionEuler<stkutil\DirectionEuler>
     DirectionPR<stkutil\DirectionPR>
     DirectionRADec<stkutil\DirectionRADec>
     DirectionXYZ<stkutil\DirectionXYZ>
     Orientation<stkutil\Orientation>
     OrientationAzEl<stkutil\OrientationAzEl>
     OrientationEulerAngles<stkutil\OrientationEulerAngles>
     OrientationQuaternion<stkutil\OrientationQuaternion>
     OrientationYPRAngles<stkutil\OrientationYPRAngles>
     DoublesCollection<stkutil\DoublesCollection>
     Cartesian3Vector<stkutil\Cartesian3Vector>
     Cartesian2Vector<stkutil\Cartesian2Vector>
     PropertyInfo<stkutil\PropertyInfo>
     PropertyInfoCollection<stkutil\PropertyInfoCollection>
     RuntimeTypeInfo<stkutil\RuntimeTypeInfo>
     CROrientationAzEl<stkutil\CROrientationAzEl>
     CROrientationEulerAngles<stkutil\CROrientationEulerAngles>
     CROrientationQuaternion<stkutil\CROrientationQuaternion>
     CROrientationYPRAngles<stkutil\CROrientationYPRAngles>
     CROrientationOffsetCart<stkutil\CROrientationOffsetCart>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ POSITION_TYPE<stkutil\POSITION_TYPE>
    ≔ EULER_DIRECTION_SEQUENCE<stkutil\EULER_DIRECTION_SEQUENCE>
    ≔ DIRECTION_TYPE<stkutil\DIRECTION_TYPE>
    ≔ PR_SEQUENCE<stkutil\PR_SEQUENCE>
    ≔ ORIENTATION_TYPE<stkutil\ORIENTATION_TYPE>
    ≔ AZ_EL_ABOUT_BORESIGHT<stkutil\AZ_EL_ABOUT_BORESIGHT>
    ≔ EULER_ORIENTATION_SEQUENCE<stkutil\EULER_ORIENTATION_SEQUENCE>
    ≔ YPR_ANGLES_SEQUENCE<stkutil\YPR_ANGLES_SEQUENCE>
    ≔ ORBIT_STATE_TYPE<stkutil\ORBIT_STATE_TYPE>
    ≔ COORDINATE_SYSTEM<stkutil\COORDINATE_SYSTEM>
    ≔ LOG_MSG_TYPE<stkutil\LOG_MSG_TYPE>
    ≔ LOG_MSG_DISP_ID<stkutil\LOG_MSG_DISP_ID>
    ≔ LINE_STYLE<stkutil\LINE_STYLE>
    ≔ EXEC_MULTI_CMD_RESULT_ACTION<stkutil\EXEC_MULTI_CMD_RESULT_ACTION>
    ≔ FILL_STYLE<stkutil\FILL_STYLE>
    ≔ PROPERTY_INFO_VALUE_TYPE<stkutil\PROPERTY_INFO_VALUE_TYPE>

