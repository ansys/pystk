
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
        

            * - :py:class:`~ansys.stk.core.stkutil.ILocationData`
              - Base interface IAgLocationData. IAgPosition derives from this interface.

            * - :py:class:`~ansys.stk.core.stkutil.IPosition`
              - IAgPosition provides access to the position of the object.

            * - :py:class:`~ansys.stk.core.stkutil.IPlanetocentric`
              - Planetocentric Position Type.

            * - :py:class:`~ansys.stk.core.stkutil.IGeocentric`
              - Geocentric Position Type.

            * - :py:class:`~ansys.stk.core.stkutil.ISpherical`
              - Spherical Position Type.

            * - :py:class:`~ansys.stk.core.stkutil.ICylindrical`
              - Cylindrical Position Type.

            * - :py:class:`~ansys.stk.core.stkutil.ICartesian`
              - IAgCartesian Interface used to access a position using Cartesian Coordinates.

            * - :py:class:`~ansys.stk.core.stkutil.IGeodetic`
              - IAgGeodetic sets the position using Geodetic properties.

            * - :py:class:`~ansys.stk.core.stkutil.IPlanetodetic`
              - IAgPlanetodetic sets the position using Planetodetic properties.

            * - :py:class:`~ansys.stk.core.stkutil.IDirection`
              - Interface to set and retrieve direction options for aligned and constrained vectors.

            * - :py:class:`~ansys.stk.core.stkutil.IDirectionEuler`
              - Interface for Euler direction sequence.

            * - :py:class:`~ansys.stk.core.stkutil.IDirectionPR`
              - Interface for Pitch-Roll (PR) direction sequence.

            * - :py:class:`~ansys.stk.core.stkutil.IDirectionRADec`
              - Interface for Spherical direction (Right Ascension and Declination).

            * - :py:class:`~ansys.stk.core.stkutil.IDirectionXYZ`
              - Interface for Cartesian direction.

            * - :py:class:`~ansys.stk.core.stkutil.ICartesian3Vector`
              - Represents a cartesian 3-D vector.

            * - :py:class:`~ansys.stk.core.stkutil.IOrientation`
              - Interface to set and retrieve the orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.IOrientationAzEl`
              - Interface for AzEl orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.IOrientationEulerAngles`
              - Interface for Euler Angles orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.IOrientationQuaternion`
              - Quaternion representing orientation between two sets of axes.

            * - :py:class:`~ansys.stk.core.stkutil.IOrientationYPRAngles`
              - Interface for Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~ansys.stk.core.stkutil.IOrientationPositionOffset`
              - Interface for defining the orientation origin position offset relative to the parent object.

            * - :py:class:`~ansys.stk.core.stkutil.IOrbitState`
              - Interface to set and retrieve the coordinate type used to specify the orbit state.

            * - :py:class:`~ansys.stk.core.stkutil.ICartesian2Vector`
              - Represents a cartesian 2-D vector.

            * - :py:class:`~ansys.stk.core.stkutil.IUnitPreferencesDimension`
              - Provide info on a Dimension from the global unit table.

            * - :py:class:`~ansys.stk.core.stkutil.IPropertyInfo`
              - Property information.

            * - :py:class:`~ansys.stk.core.stkutil.IPropertyInfoCollection`
              - The collection of properties.

            * - :py:class:`~ansys.stk.core.stkutil.IRuntimeTypeInfo`
              - Interface used to retrieve the properties at runtime.

            * - :py:class:`~ansys.stk.core.stkutil.IRuntimeTypeInfoProvider`
              - Access point for IAgRuntimeTypeInfo.

            * - :py:class:`~ansys.stk.core.stkutil.IExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~ansys.stk.core.stkutil.IExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~ansys.stk.core.stkutil.IUnitPreferencesUnit`
              - Provide info about a unit.

            * - :py:class:`~ansys.stk.core.stkutil.IUnitPreferencesUnitCollection`
              - Provide access to the Unit collection.

            * - :py:class:`~ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection`
              - Provide accesses to the global unit table.

            * - :py:class:`~ansys.stk.core.stkutil.IQuantity`
              - Provide helper methods for a quantity.

            * - :py:class:`~ansys.stk.core.stkutil.IDate`
              - Provide helper methods for a date.

            * - :py:class:`~ansys.stk.core.stkutil.IConversionUtility`
              - Provide conversion utilities.

            * - :py:class:`~ansys.stk.core.stkutil.IDoublesCollection`
              - Represents a collection of doubles.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkutil.ExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~ansys.stk.core.stkutil.ExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~ansys.stk.core.stkutil.UnitPreferencesUnit`
              - Object that contains info on the unit.

            * - :py:class:`~ansys.stk.core.stkutil.UnitPreferencesUnitCollection`
              - Object that contains a collection of IAgUnitPrefsUnit.

            * - :py:class:`~ansys.stk.core.stkutil.UnitPreferencesDimension`
              - Object that contains info on the Dimension.

            * - :py:class:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection`
              - Object that contains a collection of dimensions.

            * - :py:class:`~ansys.stk.core.stkutil.ConversionUtility`
              - Object that contains a unit conversion utility.

            * - :py:class:`~ansys.stk.core.stkutil.Quantity`
              - Object that contains a quantity.

            * - :py:class:`~ansys.stk.core.stkutil.Date`
              - Object that contains a date.

            * - :py:class:`~ansys.stk.core.stkutil.Position`
              - The Position class.

            * - :py:class:`~ansys.stk.core.stkutil.Cartesian`
              - Class used to access a position using Cartesian Coordinates.

            * - :py:class:`~ansys.stk.core.stkutil.Geodetic`
              - Class defining Geodetic position.

            * - :py:class:`~ansys.stk.core.stkutil.Geocentric`
              - Class defining Geocentric position.

            * - :py:class:`~ansys.stk.core.stkutil.Planetodetic`
              - Class defining Planetodetic position.

            * - :py:class:`~ansys.stk.core.stkutil.Planetocentric`
              - Class defining Planetocentric position.

            * - :py:class:`~ansys.stk.core.stkutil.Spherical`
              - Class defining spherical position.

            * - :py:class:`~ansys.stk.core.stkutil.Cylindrical`
              - Class defining cylindrical position.

            * - :py:class:`~ansys.stk.core.stkutil.Direction`
              - Class defining direction options for aligned and constrained vectors.

            * - :py:class:`~ansys.stk.core.stkutil.DirectionEuler`
              - Euler direction sequence.

            * - :py:class:`~ansys.stk.core.stkutil.DirectionPR`
              - Pitch-Roll (PR) direction sequence.

            * - :py:class:`~ansys.stk.core.stkutil.DirectionRADec`
              - Spherical direction (Right Ascension and Declination).

            * - :py:class:`~ansys.stk.core.stkutil.DirectionXYZ`
              - Cartesian direction.

            * - :py:class:`~ansys.stk.core.stkutil.Orientation`
              - Class defining the orientation of an orbit.

            * - :py:class:`~ansys.stk.core.stkutil.OrientationAzEl`
              - AzEl orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.OrientationEulerAngles`
              - Euler Angles orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.OrientationQuaternion`
              - Quaternion orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.OrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~ansys.stk.core.stkutil.DoublesCollection`
              - A collection of doubles.

            * - :py:class:`~ansys.stk.core.stkutil.Cartesian3Vector`
              - A 3-D cartesian vector.

            * - :py:class:`~ansys.stk.core.stkutil.Cartesian2Vector`
              - A 2-D cartesian vector.

            * - :py:class:`~ansys.stk.core.stkutil.PropertyInfo`
              - Property Information coclass.

            * - :py:class:`~ansys.stk.core.stkutil.PropertyInfoCollection`
              - Property Information Collection coclass.

            * - :py:class:`~ansys.stk.core.stkutil.RuntimeTypeInfo`
              - Runtime Type info coclass.

            * - :py:class:`~ansys.stk.core.stkutil.CROrientationAzEl`
              - AzEl orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.CROrientationEulerAngles`
              - Euler Angles orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.CROrientationQuaternion`
              - Quaternion orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.CROrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~ansys.stk.core.stkutil.CROrientationOffsetCart`
              - Orientation offset cartesian.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkutil.POSITION_TYPE`
              - Facility/place/target position types.

            * - :py:class:`~ansys.stk.core.stkutil.EULER_DIRECTION_SEQUENCE`
              - Euler direction sequences.

            * - :py:class:`~ansys.stk.core.stkutil.DIRECTION_TYPE`
              - Direction options for aligned and constrained vectors.

            * - :py:class:`~ansys.stk.core.stkutil.PR_SEQUENCE`
              - Pitch-Roll (PR) direction sequences.

            * - :py:class:`~ansys.stk.core.stkutil.ORIENTATION_TYPE`
              - Orientation methods.

            * - :py:class:`~ansys.stk.core.stkutil.AZ_EL_ABOUT_BORESIGHT`
              - About Boresight options for AzEl orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.EULER_ORIENTATION_SEQUENCE`
              - Euler rotation sequence options:.

            * - :py:class:`~ansys.stk.core.stkutil.YPR_ANGLES_SEQUENCE`
              - Yaw-Pitch-Roll (YPR) sequences.

            * - :py:class:`~ansys.stk.core.stkutil.ORBIT_STATE_TYPE`
              - Coordinate types used in specifying orbit state.

            * - :py:class:`~ansys.stk.core.stkutil.COORDINATE_SYSTEM`
              - Earth-centered coordinate systems for defining certain propagators.

            * - :py:class:`~ansys.stk.core.stkutil.LOG_MSG_TYPE`
              - Log message types.

            * - :py:class:`~ansys.stk.core.stkutil.LOG_MSG_DISP_ID`
              - Log message destination options.

            * - :py:class:`~ansys.stk.core.stkutil.LINE_STYLE`
              - Line Style.

            * - :py:class:`~ansys.stk.core.stkutil.EXEC_MULTI_CMD_RESULT_ACTION`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :py:class:`~ansys.stk.core.stkutil.FILL_STYLE`
              - Fill Style.

            * - :py:class:`~ansys.stk.core.stkutil.PROPERTY_INFO_VALUE_TYPE`
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

     ILocationData<stkutil/ILocationData>
     IPosition<stkutil/IPosition>
     IPlanetocentric<stkutil/IPlanetocentric>
     IGeocentric<stkutil/IGeocentric>
     ISpherical<stkutil/ISpherical>
     ICylindrical<stkutil/ICylindrical>
     ICartesian<stkutil/ICartesian>
     IGeodetic<stkutil/IGeodetic>
     IPlanetodetic<stkutil/IPlanetodetic>
     IDirection<stkutil/IDirection>
     IDirectionEuler<stkutil/IDirectionEuler>
     IDirectionPR<stkutil/IDirectionPR>
     IDirectionRADec<stkutil/IDirectionRADec>
     IDirectionXYZ<stkutil/IDirectionXYZ>
     ICartesian3Vector<stkutil/ICartesian3Vector>
     IOrientation<stkutil/IOrientation>
     IOrientationAzEl<stkutil/IOrientationAzEl>
     IOrientationEulerAngles<stkutil/IOrientationEulerAngles>
     IOrientationQuaternion<stkutil/IOrientationQuaternion>
     IOrientationYPRAngles<stkutil/IOrientationYPRAngles>
     IOrientationPositionOffset<stkutil/IOrientationPositionOffset>
     IOrbitState<stkutil/IOrbitState>
     ICartesian2Vector<stkutil/ICartesian2Vector>
     IUnitPreferencesDimension<stkutil/IUnitPreferencesDimension>
     IPropertyInfo<stkutil/IPropertyInfo>
     IPropertyInfoCollection<stkutil/IPropertyInfoCollection>
     IRuntimeTypeInfo<stkutil/IRuntimeTypeInfo>
     IRuntimeTypeInfoProvider<stkutil/IRuntimeTypeInfoProvider>
     IExecCmdResult<stkutil/IExecCmdResult>
     IExecMultiCmdResult<stkutil/IExecMultiCmdResult>
     IUnitPreferencesUnit<stkutil/IUnitPreferencesUnit>
     IUnitPreferencesUnitCollection<stkutil/IUnitPreferencesUnitCollection>
     IUnitPreferencesDimensionCollection<stkutil/IUnitPreferencesDimensionCollection>
     IQuantity<stkutil/IQuantity>
     IDate<stkutil/IDate>
     IConversionUtility<stkutil/IConversionUtility>
     IDoublesCollection<stkutil/IDoublesCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ExecCmdResult<stkutil/ExecCmdResult>
     ExecMultiCmdResult<stkutil/ExecMultiCmdResult>
     UnitPreferencesUnit<stkutil/UnitPreferencesUnit>
     UnitPreferencesUnitCollection<stkutil/UnitPreferencesUnitCollection>
     UnitPreferencesDimension<stkutil/UnitPreferencesDimension>
     UnitPreferencesDimensionCollection<stkutil/UnitPreferencesDimensionCollection>
     ConversionUtility<stkutil/ConversionUtility>
     Quantity<stkutil/Quantity>
     Date<stkutil/Date>
     Position<stkutil/Position>
     Cartesian<stkutil/Cartesian>
     Geodetic<stkutil/Geodetic>
     Geocentric<stkutil/Geocentric>
     Planetodetic<stkutil/Planetodetic>
     Planetocentric<stkutil/Planetocentric>
     Spherical<stkutil/Spherical>
     Cylindrical<stkutil/Cylindrical>
     Direction<stkutil/Direction>
     DirectionEuler<stkutil/DirectionEuler>
     DirectionPR<stkutil/DirectionPR>
     DirectionRADec<stkutil/DirectionRADec>
     DirectionXYZ<stkutil/DirectionXYZ>
     Orientation<stkutil/Orientation>
     OrientationAzEl<stkutil/OrientationAzEl>
     OrientationEulerAngles<stkutil/OrientationEulerAngles>
     OrientationQuaternion<stkutil/OrientationQuaternion>
     OrientationYPRAngles<stkutil/OrientationYPRAngles>
     DoublesCollection<stkutil/DoublesCollection>
     Cartesian3Vector<stkutil/Cartesian3Vector>
     Cartesian2Vector<stkutil/Cartesian2Vector>
     PropertyInfo<stkutil/PropertyInfo>
     PropertyInfoCollection<stkutil/PropertyInfoCollection>
     RuntimeTypeInfo<stkutil/RuntimeTypeInfo>
     CROrientationAzEl<stkutil/CROrientationAzEl>
     CROrientationEulerAngles<stkutil/CROrientationEulerAngles>
     CROrientationQuaternion<stkutil/CROrientationQuaternion>
     CROrientationYPRAngles<stkutil/CROrientationYPRAngles>
     CROrientationOffsetCart<stkutil/CROrientationOffsetCart>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ POSITION_TYPE<stkutil/POSITION_TYPE>
    ≔ EULER_DIRECTION_SEQUENCE<stkutil/EULER_DIRECTION_SEQUENCE>
    ≔ DIRECTION_TYPE<stkutil/DIRECTION_TYPE>
    ≔ PR_SEQUENCE<stkutil/PR_SEQUENCE>
    ≔ ORIENTATION_TYPE<stkutil/ORIENTATION_TYPE>
    ≔ AZ_EL_ABOUT_BORESIGHT<stkutil/AZ_EL_ABOUT_BORESIGHT>
    ≔ EULER_ORIENTATION_SEQUENCE<stkutil/EULER_ORIENTATION_SEQUENCE>
    ≔ YPR_ANGLES_SEQUENCE<stkutil/YPR_ANGLES_SEQUENCE>
    ≔ ORBIT_STATE_TYPE<stkutil/ORBIT_STATE_TYPE>
    ≔ COORDINATE_SYSTEM<stkutil/COORDINATE_SYSTEM>
    ≔ LOG_MSG_TYPE<stkutil/LOG_MSG_TYPE>
    ≔ LOG_MSG_DISP_ID<stkutil/LOG_MSG_DISP_ID>
    ≔ LINE_STYLE<stkutil/LINE_STYLE>
    ≔ EXEC_MULTI_CMD_RESULT_ACTION<stkutil/EXEC_MULTI_CMD_RESULT_ACTION>
    ≔ FILL_STYLE<stkutil/FILL_STYLE>
    ≔ PROPERTY_INFO_VALUE_TYPE<stkutil/PROPERTY_INFO_VALUE_TYPE>

