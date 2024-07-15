Sensor
======

.. py:class:: ansys.stk.core.stkobjects.Sensor

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Class defining the Sensor class.

.. py:currentmodule:: Sensor

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.set_pattern_type`
              - Set the pattern type.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.set_pointing_type`
              - Set the sensor's pointing type, using the AgESnPointing enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.set_pointing_external_file`
              - Set the external pointing type.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.reset_az_el_mask`
              - Reset the az-el mask.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.set_az_el_mask`
              - Set the az-el mask type, using the AgEAzElMaskType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.set_az_el_mask_file`
              - Path and file name of az-el mask file.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.set_location_type`
              - Set the sensor's location type, a member of the AgESnLocation enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.get_stars_in_fov`
              - Return celestial bodies within the sensor's field of view.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.pattern_type`
              - Criterion for defining the sensor pattern. A member of the AgESnPattern enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.pattern`
              - Get data defining the sensor pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.pointing_type`
              - The sensor's pointing type. A member of the AgESnPointing enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.pointing`
              - Get pointing data for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.az_el_mask`
              - Get the az-el mask.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.az_el_mask_data`
              - Get az-el mask data for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.focal_length`
              - Focal length used in defining sensor resolution. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.detector_pitch`
              - Detector pitch used in defining senor resolution. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.refraction`
              - Refraction method, a member of the AgESnRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.graphics`
              - Get the 2D Graphics properties for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.graphics_3d`
              - Get the 3D Graphics properties for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.location_type`
              - The location type being used by the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.location_data`
              - Get location data for the sensor. The sensor's center point is invalid; all other points are valid choices for the location data.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.access_constraints`
              - Get constraints imposed on the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.swath`
              - Get the sensor's swath.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.refraction_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.refraction_model`
              - Gets a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Sensor.common_tasks`
              - Returns an interface that exposes common tasks.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Sensor


Property detail
---------------

.. py:property:: pattern_type
    :canonical: ansys.stk.core.stkobjects.Sensor.pattern_type
    :type: SENSOR_PATTERN

    Criterion for defining the sensor pattern. A member of the AgESnPattern enumeration.

.. py:property:: pattern
    :canonical: ansys.stk.core.stkobjects.Sensor.pattern
    :type: ISensorPattern

    Get data defining the sensor pattern.

.. py:property:: pointing_type
    :canonical: ansys.stk.core.stkobjects.Sensor.pointing_type
    :type: SENSOR_POINTING

    The sensor's pointing type. A member of the AgESnPointing enumeration.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.Sensor.pointing
    :type: ISensorPointing

    Get pointing data for the sensor.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.Sensor.az_el_mask
    :type: AZ_EL_MASK_TYPE

    Get the az-el mask.

.. py:property:: az_el_mask_data
    :canonical: ansys.stk.core.stkobjects.Sensor.az_el_mask_data
    :type: IAzElMaskData

    Get az-el mask data for the sensor.

.. py:property:: focal_length
    :canonical: ansys.stk.core.stkobjects.Sensor.focal_length
    :type: float

    Focal length used in defining sensor resolution. Uses SmallDistanceUnit Dimension.

.. py:property:: detector_pitch
    :canonical: ansys.stk.core.stkobjects.Sensor.detector_pitch
    :type: float

    Detector pitch used in defining senor resolution. Uses SmallDistanceUnit Dimension.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Sensor.refraction
    :type: SENSOR_REFRACTION_TYPE

    Refraction method, a member of the AgESnRefractionType enumeration.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Sensor.graphics
    :type: ISensorGraphics

    Get the 2D Graphics properties for the sensor.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Sensor.graphics_3d
    :type: ISensorGraphics3D

    Get the 3D Graphics properties for the sensor.

.. py:property:: location_type
    :canonical: ansys.stk.core.stkobjects.Sensor.location_type
    :type: SENSOR_LOCATION

    The location type being used by the sensor.

.. py:property:: location_data
    :canonical: ansys.stk.core.stkobjects.Sensor.location_data
    :type: ILocationData

    Get location data for the sensor. The sensor's center point is invalid; all other points are valid choices for the location data.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.Sensor.access_constraints
    :type: IAccessConstraintCollection

    Get constraints imposed on the sensor.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.Sensor.swath
    :type: ISwath

    Get the sensor's swath.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Sensor.refraction_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Sensor.refraction_model
    :type: IRefractionModelBase

    Gets a refraction model.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.Sensor.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.Sensor.common_tasks
    :type: ISensorCommonTasks

    Returns an interface that exposes common tasks.


Method detail
-------------


.. py:method:: set_pattern_type(self, patternType: SENSOR_PATTERN) -> None
    :canonical: ansys.stk.core.stkobjects.Sensor.set_pattern_type

    Set the pattern type.

    :Parameters:

    **patternType** : :obj:`~SENSOR_PATTERN`

    :Returns:

        :obj:`~None`



.. py:method:: set_pointing_type(self, pointingType: SENSOR_POINTING) -> None
    :canonical: ansys.stk.core.stkobjects.Sensor.set_pointing_type

    Set the sensor's pointing type, using the AgESnPointing enumeration.

    :Parameters:

    **pointingType** : :obj:`~SENSOR_POINTING`

    :Returns:

        :obj:`~None`

.. py:method:: set_pointing_external_file(self, sensorPointingFile: str) -> None
    :canonical: ansys.stk.core.stkobjects.Sensor.set_pointing_external_file

    Set the external pointing type.

    :Parameters:

    **sensorPointingFile** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: reset_az_el_mask(self) -> None
    :canonical: ansys.stk.core.stkobjects.Sensor.reset_az_el_mask

    Reset the az-el mask.

    :Returns:

        :obj:`~None`


.. py:method:: set_az_el_mask(self, azElMaskType: AZ_EL_MASK_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.Sensor.set_az_el_mask

    Set the az-el mask type, using the AgEAzElMaskType enumeration.

    :Parameters:

    **azElMaskType** : :obj:`~AZ_EL_MASK_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: set_az_el_mask_file(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.Sensor.set_az_el_mask_file

    Path and file name of az-el mask file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`











.. py:method:: set_location_type(self, locationType: SENSOR_LOCATION) -> None
    :canonical: ansys.stk.core.stkobjects.Sensor.set_location_type

    Set the sensor's location type, a member of the AgESnLocation enumeration.

    :Parameters:

    **locationType** : :obj:`~SENSOR_LOCATION`

    :Returns:

        :obj:`~None`




.. py:method:: is_refraction_type_supported(self, model: SENSOR_REFRACTION_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.Sensor.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **model** : :obj:`~SENSOR_REFRACTION_TYPE`

    :Returns:

        :obj:`~bool`






.. py:method:: get_stars_in_fov(self, epoch: typing.Any) -> CelestialBodyCollection
    :canonical: ansys.stk.core.stkobjects.Sensor.get_stars_in_fov

    Return celestial bodies within the sensor's field of view.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~CelestialBodyCollection`

