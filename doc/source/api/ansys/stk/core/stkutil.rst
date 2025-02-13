
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
        

            * - :py:class:`~ansys.stk.core.stkutil.ExecuteCommandResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~ansys.stk.core.stkutil.ExecuteMultipleCommandsResult`
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

            * - :py:class:`~ansys.stk.core.stkutil.AgCROrientationAzEl`
              - AzEl orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.AgCROrientationEulerAngles`
              - Euler Angles orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.AgCROrientationQuaternion`
              - Quaternion orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.AgCROrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~ansys.stk.core.stkutil.AgCROrientationOffsetCart`
              - Orientation offset cartesian.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkutil.PositionType`
              - Facility/place/target position types.

            * - :py:class:`~ansys.stk.core.stkutil.EulerDirectionSequence`
              - Euler direction sequences.

            * - :py:class:`~ansys.stk.core.stkutil.DirectionType`
              - Direction options for aligned and constrained vectors.

            * - :py:class:`~ansys.stk.core.stkutil.PRSequence`
              - Pitch-Roll (PR) direction sequences.

            * - :py:class:`~ansys.stk.core.stkutil.OrientationType`
              - Orientation methods.

            * - :py:class:`~ansys.stk.core.stkutil.AzElAboutBoresight`
              - About Boresight options for AzEl orientation method.

            * - :py:class:`~ansys.stk.core.stkutil.EulerOrientationSequenceType`
              - Euler rotation sequence options:.

            * - :py:class:`~ansys.stk.core.stkutil.YPRAnglesSequence`
              - Yaw-Pitch-Roll (YPR) sequences.

            * - :py:class:`~ansys.stk.core.stkutil.OrbitStateType`
              - Coordinate types used in specifying orbit state.

            * - :py:class:`~ansys.stk.core.stkutil.CoordinateSystem`
              - Earth-centered coordinate systems for defining certain propagators.

            * - :py:class:`~ansys.stk.core.stkutil.LogMessageType`
              - Log message types.

            * - :py:class:`~ansys.stk.core.stkutil.LogMessageDisplayID`
              - Log message destination options.

            * - :py:class:`~ansys.stk.core.stkutil.LineStyle`
              - Line Style.

            * - :py:class:`~ansys.stk.core.stkutil.ExecuteMultipleCommandsMode`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :py:class:`~ansys.stk.core.stkutil.FillStyle`
              - Fill Style.

            * - :py:class:`~ansys.stk.core.stkutil.PropertyInfoValueType`
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

     ExecuteCommandResult<stkutil/ExecuteCommandResult>
     ExecuteMultipleCommandsResult<stkutil/ExecuteMultipleCommandsResult>
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
     AgCROrientationAzEl<stkutil/AgCROrientationAzEl>
     AgCROrientationEulerAngles<stkutil/AgCROrientationEulerAngles>
     AgCROrientationQuaternion<stkutil/AgCROrientationQuaternion>
     AgCROrientationYPRAngles<stkutil/AgCROrientationYPRAngles>
     AgCROrientationOffsetCart<stkutil/AgCROrientationOffsetCart>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ PositionType<stkutil/PositionType>
    ≔ EulerDirectionSequence<stkutil/EulerDirectionSequence>
    ≔ DirectionType<stkutil/DirectionType>
    ≔ PRSequence<stkutil/PRSequence>
    ≔ OrientationType<stkutil/OrientationType>
    ≔ AzElAboutBoresight<stkutil/AzElAboutBoresight>
    ≔ EulerOrientationSequenceType<stkutil/EulerOrientationSequenceType>
    ≔ YPRAnglesSequence<stkutil/YPRAnglesSequence>
    ≔ OrbitStateType<stkutil/OrbitStateType>
    ≔ CoordinateSystem<stkutil/CoordinateSystem>
    ≔ LogMessageType<stkutil/LogMessageType>
    ≔ LogMessageDisplayID<stkutil/LogMessageDisplayID>
    ≔ LineStyle<stkutil/LineStyle>
    ≔ ExecuteMultipleCommandsMode<stkutil/ExecuteMultipleCommandsMode>
    ≔ FillStyle<stkutil/FillStyle>
    ≔ PropertyInfoValueType<stkutil/PropertyInfoValueType>

