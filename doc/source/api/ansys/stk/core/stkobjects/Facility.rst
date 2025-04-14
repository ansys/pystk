Facility
========

.. py:class:: ansys.stk.core.stkobjects.Facility

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining the Facility object.

.. py:currentmodule:: Facility

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.set_az_el_mask`
              - Set an az-el mask. A member of the AgEAzElMaskType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.reset_az_el_mask`
              - Reset the az-el mask.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.get_az_el_mask`
              - Get the az-el mask. A member of the AgEAzElMaskType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.get_az_el_mask_data`
              - Get az-el mask data.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.use_local_time_offset`
              - Opt whether to use a local time offset from GMT.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.local_time_offset`
              - The amount of the time offset from GMT, if this option is used. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.use_terrain`
              - Opt whether to set altitude automatically by using terrain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.graphics`
              - Get the 2D Graphics properties of the facility.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.position`
              - Get the position of the facility.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.terrain_normal`
              - Set the normal to the local terrain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.terrain_normal_data`
              - Data used in specifying terrain slope.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.graphics_3d`
              - Get the 3D Graphics properties of the facility.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.access_constraints`
              - Get the constraints imposed on the facility.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.height_above_ground`
              - Height of facility above its model of the ground. Height is measured along the normal to surface defined by reference ellipsoid of the central body. Facility models the ground as an ellipsoid passing through the ground position. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.altitude_reference`
              - Get or set the altitude reference of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.atmosphere`
              - Do not use this property, as it is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.radar_clutter_map`
              - Return the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.radar_cross_section`
              - Return the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.save_terrain_mask_data_in_binary`
              - Save terrain az-el mask data in binary.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.lighting_obstruction_model`
              - Get or set the obstruction model used in lighting computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.lighting_maximum_step`
              - Get or set the maximum step size to use when computing lighting. Only applies (and only can be set) when LightingObstructionModel is eLightingObstructionAzElMask or eLightingObstructionTerrain. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.laser_environment`
              - Get the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.rf_environment`
              - Get the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Facility.maximum_range_when_computing_az_el_mask`
              - Get or set the maximum range to use when computing the az el mask using terrain data. Zero indicates to use algorithm default. Only applies when GetAzElMask returns eTerrainData (cannot be set if eMaskFile). Uses Distance Dimension.



Examples
--------

Add an AzEl Mask to a Facility

.. code-block:: python

    # Facility facility: Facility Object
    facility.set_az_el_mask(AzElMaskType.TERRAIN_DATA, 0)

Get the cartesian position of a facility

.. code-block:: python

    # Facility facility: Facility Object
    (x, y, z) = facility.position.query_cartesian()
    
Set the geodetic position of the facility

.. code-block:: python

    # Facility facility: Facility Object
    facility.position.assign_geodetic(41.9849, 21.4039, 0)  # Latitude, Longitude, Altitude

    # Set altitude to height of terrain
    facility.use_terrain = True

    # Set altitude to a distance above the ground
    facility.height_above_ground = 0.05  # km


Create a facility and set its height relative to ground level

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    from ansys.stk.core.stkobjects import Facility, STKObjectType

    facility = Facility(root.current_scenario.children.new(STKObjectType.FACILITY, "facility1"))
    facility.height_above_ground = 123.4


Create a facility (on the current scenario central body)

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    facility = root.current_scenario.children.new(STKObjectType.FACILITY, "MyFacility")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Facility


Property detail
---------------

.. py:property:: use_local_time_offset
    :canonical: ansys.stk.core.stkobjects.Facility.use_local_time_offset
    :type: bool

    Opt whether to use a local time offset from GMT.

.. py:property:: local_time_offset
    :canonical: ansys.stk.core.stkobjects.Facility.local_time_offset
    :type: float

    The amount of the time offset from GMT, if this option is used. Uses Time Dimension.

.. py:property:: use_terrain
    :canonical: ansys.stk.core.stkobjects.Facility.use_terrain
    :type: bool

    Opt whether to set altitude automatically by using terrain data.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Facility.graphics
    :type: FacilityGraphics

    Get the 2D Graphics properties of the facility.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.Facility.position
    :type: IPosition

    Get the position of the facility.

.. py:property:: terrain_normal
    :canonical: ansys.stk.core.stkobjects.Facility.terrain_normal
    :type: None

    Set the normal to the local terrain.

.. py:property:: terrain_normal_data
    :canonical: ansys.stk.core.stkobjects.Facility.terrain_normal_data
    :type: ITerrainNormData

    Data used in specifying terrain slope.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Facility.graphics_3d
    :type: FacilityGraphics3D

    Get the 3D Graphics properties of the facility.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.Facility.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the facility.

.. py:property:: height_above_ground
    :canonical: ansys.stk.core.stkobjects.Facility.height_above_ground
    :type: None

    Height of facility above its model of the ground. Height is measured along the normal to surface defined by reference ellipsoid of the central body. Facility models the ground as an ellipsoid passing through the ground position. Uses Distance Dimension.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.Facility.altitude_reference
    :type: None

    Get or set the altitude reference of the object.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.Facility.atmosphere
    :type: Atmosphere

    Do not use this property, as it is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.Facility.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Return the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.Facility.radar_cross_section
    :type: RadarCrossSectionInheritable

    Return the radar cross sectoin.

.. py:property:: save_terrain_mask_data_in_binary
    :canonical: ansys.stk.core.stkobjects.Facility.save_terrain_mask_data_in_binary
    :type: bool

    Save terrain az-el mask data in binary.

.. py:property:: lighting_obstruction_model
    :canonical: ansys.stk.core.stkobjects.Facility.lighting_obstruction_model
    :type: LightingObstructionModelType

    Get or set the obstruction model used in lighting computations.

.. py:property:: lighting_maximum_step
    :canonical: ansys.stk.core.stkobjects.Facility.lighting_maximum_step
    :type: float

    Get or set the maximum step size to use when computing lighting. Only applies (and only can be set) when LightingObstructionModel is eLightingObstructionAzElMask or eLightingObstructionTerrain. Uses Time Dimension.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Facility.laser_environment
    :type: PlatformLaserEnvironment

    Get the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Facility.rf_environment
    :type: IPlatformRFEnvironment

    Get the RF environment.

.. py:property:: maximum_range_when_computing_az_el_mask
    :canonical: ansys.stk.core.stkobjects.Facility.maximum_range_when_computing_az_el_mask
    :type: float

    Get or set the maximum range to use when computing the az el mask using terrain data. Zero indicates to use algorithm default. Only applies when GetAzElMask returns eTerrainData (cannot be set if eMaskFile). Uses Distance Dimension.


Method detail
-------------







.. py:method:: set_az_el_mask(self, type: AzElMaskType, data: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.Facility.set_az_el_mask

    Set an az-el mask. A member of the AgEAzElMaskType enumeration.

    :Parameters:

    **type** : :obj:`~AzElMaskType`
    **data** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`








.. py:method:: reset_az_el_mask(self) -> None
    :canonical: ansys.stk.core.stkobjects.Facility.reset_az_el_mask

    Reset the az-el mask.

    :Returns:

        :obj:`~None`

.. py:method:: get_az_el_mask(self) -> AzElMaskType
    :canonical: ansys.stk.core.stkobjects.Facility.get_az_el_mask

    Get the az-el mask. A member of the AgEAzElMaskType enumeration.

    :Returns:

        :obj:`~AzElMaskType`

.. py:method:: get_az_el_mask_data(self) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.Facility.get_az_el_mask_data

    Get az-el mask data.

    :Returns:

        :obj:`~typing.Any`


















