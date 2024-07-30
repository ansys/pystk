
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

            * - :py:class:`~ansys.stk.core.stkutil.IDirection`
              - Interface to set and retrieve direction options for aligned and constrained vectors.

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

            * - :py:class:`~ansys.stk.core.stkutil.IRuntimeTypeInfoProvider`
              - Access point for IAgRuntimeTypeInfo.

    
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

            * - :py:class:`~ansys.stk.core.stkutil.LOG_MESSAGE_TYPE`
              - Log message types.

            * - :py:class:`~ansys.stk.core.stkutil.LOG_MESSAGE_DISP_ID`
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


.. py:currentmodule:: ansys.stk.core.stkutil


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ILocationData<stkutil/ILocationData>
     IPosition<stkutil/IPosition>
     IDirection<stkutil/IDirection>
     ICartesian3Vector<stkutil/ICartesian3Vector>
     IOrientation<stkutil/IOrientation>
     IOrientationAzEl<stkutil/IOrientationAzEl>
     IOrientationEulerAngles<stkutil/IOrientationEulerAngles>
     IOrientationQuaternion<stkutil/IOrientationQuaternion>
     IOrientationYPRAngles<stkutil/IOrientationYPRAngles>
     IOrientationPositionOffset<stkutil/IOrientationPositionOffset>
     IOrbitState<stkutil/IOrbitState>
     IRuntimeTypeInfoProvider<stkutil/IRuntimeTypeInfoProvider>

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

    ≔ POSITION_TYPE<stkutil/POSITION_TYPE_enum>
    ≔ EULER_DIRECTION_SEQUENCE<stkutil/EULER_DIRECTION_SEQUENCE_enum>
    ≔ DIRECTION_TYPE<stkutil/DIRECTION_TYPE_enum>
    ≔ PR_SEQUENCE<stkutil/PR_SEQUENCE_enum>
    ≔ ORIENTATION_TYPE<stkutil/ORIENTATION_TYPE_enum>
    ≔ AZ_EL_ABOUT_BORESIGHT<stkutil/AZ_EL_ABOUT_BORESIGHT_enum>
    ≔ EULER_ORIENTATION_SEQUENCE<stkutil/EULER_ORIENTATION_SEQUENCE_enum>
    ≔ YPR_ANGLES_SEQUENCE<stkutil/YPR_ANGLES_SEQUENCE_enum>
    ≔ ORBIT_STATE_TYPE<stkutil/ORBIT_STATE_TYPE_enum>
    ≔ COORDINATE_SYSTEM<stkutil/COORDINATE_SYSTEM_enum>
    ≔ LOG_MESSAGE_TYPE<stkutil/LOG_MESSAGE_TYPE_enum>
    ≔ LOG_MESSAGE_DISP_ID<stkutil/LOG_MESSAGE_DISP_ID_enum>
    ≔ LINE_STYLE<stkutil/LINE_STYLE_enum>
    ≔ EXEC_MULTI_CMD_RESULT_ACTION<stkutil/EXEC_MULTI_CMD_RESULT_ACTION_enum>
    ≔ FILL_STYLE<stkutil/FILL_STYLE_enum>
    ≔ PROPERTY_INFO_VALUE_TYPE<stkutil/PROPERTY_INFO_VALUE_TYPE_enum>

