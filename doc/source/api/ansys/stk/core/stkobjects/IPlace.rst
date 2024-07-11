IPlace
======

.. py:class:: ansys.stk.core.stkobjects.IPlace

   object
   
   Provide access to the properties and methods used in defining a place object.

.. py:currentmodule:: IPlace

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.set_az_el_mask`
              - Set an az-el mask. A member of the AgEAzElMaskType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.reset_az_el_mask`
              - Reset the az-el mask.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.get_az_el_mask`
              - Get the az-el mask. A member of the AgEAzElMaskType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.get_az_el_mask_data`
              - Get az-el mask data.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.use_local_time_offset`
              - Opt whether to use a local time offset from GMT.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.local_time_offset`
              - The amount of the time offset from GMT, if this option is used. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.use_terrain`
              - Opt whether to set altitude automatically by using terrain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.graphics`
              - Get the 2D Graphics properties of the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.position`
              - Get the position of the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.terrain_norm`
              - Set the normal to the local terrain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.terrain_norm_data`
              - Data used in specifying terrain slope.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.graphics_3d`
              - Get the 3D Graphics properties of the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.access_constraints`
              - Get the constraints imposed on the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.height_above_ground`
              - Height of place above its model of the ground. Height is measured along the normal to surface defined by reference ellipsoid of the central body. Place models the ground as an ellipsoid passing through the ground position. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.altitude_reference`
              - Gets or sets the altitude reference of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.atmosphere`
              - This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.radar_clutter_map`
              - Returns the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.radar_cross_section`
              - Returns the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.save_terrain_mask_data_in_binary`
              - Save terrain az-el mask data in binary.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.lighting_obstruction_model`
              - Gets or sets the obstruction model used in lighting computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.lighting_max_step`
              - Gets or sets the maximum step size to use when computing lighting. Only applies (and only can be set) when LightingObstructionModel is eLightingObstructionAzElMask or eLightingObstructionTerrain. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.laser_environment`
              - Gets the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.rf_environment`
              - Gets the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlace.max_range_when_computing_az_el_mask`
              - Gets or sets the maximum range to use when computing the az el mask using terrain data. Zero indicates to use algorithm default. Only applies when GetAzElMask returns eTerrainData (cannot be set if eMaskFile). Uses Distance Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlace


Property detail
---------------

.. py:property:: use_local_time_offset
    :canonical: ansys.stk.core.stkobjects.IPlace.use_local_time_offset
    :type: bool

    Opt whether to use a local time offset from GMT.

.. py:property:: local_time_offset
    :canonical: ansys.stk.core.stkobjects.IPlace.local_time_offset
    :type: float

    The amount of the time offset from GMT, if this option is used. Uses Time Dimension.

.. py:property:: use_terrain
    :canonical: ansys.stk.core.stkobjects.IPlace.use_terrain
    :type: bool

    Opt whether to set altitude automatically by using terrain data.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IPlace.graphics
    :type: IPlaceGraphics

    Get the 2D Graphics properties of the place.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IPlace.position
    :type: IPosition

    Get the position of the place.

.. py:property:: terrain_norm
    :canonical: ansys.stk.core.stkobjects.IPlace.terrain_norm
    :type: None

    Set the normal to the local terrain.

.. py:property:: terrain_norm_data
    :canonical: ansys.stk.core.stkobjects.IPlace.terrain_norm_data
    :type: ITerrainNormData

    Data used in specifying terrain slope.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IPlace.graphics_3d
    :type: IPlaceGraphics3D

    Get the 3D Graphics properties of the place.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IPlace.access_constraints
    :type: IAccessConstraintCollection

    Get the constraints imposed on the place.

.. py:property:: height_above_ground
    :canonical: ansys.stk.core.stkobjects.IPlace.height_above_ground
    :type: None

    Height of place above its model of the ground. Height is measured along the normal to surface defined by reference ellipsoid of the central body. Place models the ground as an ellipsoid passing through the ground position. Uses Distance Dimension.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.IPlace.altitude_reference
    :type: None

    Gets or sets the altitude reference of the object.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.IPlace.atmosphere
    :type: IAtmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.IPlace.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IPlace.radar_cross_section
    :type: IRadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: save_terrain_mask_data_in_binary
    :canonical: ansys.stk.core.stkobjects.IPlace.save_terrain_mask_data_in_binary
    :type: bool

    Save terrain az-el mask data in binary.

.. py:property:: lighting_obstruction_model
    :canonical: ansys.stk.core.stkobjects.IPlace.lighting_obstruction_model
    :type: LIGHTING_OBSTRUCTION_MODEL_TYPE

    Gets or sets the obstruction model used in lighting computations.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.IPlace.lighting_max_step
    :type: float

    Gets or sets the maximum step size to use when computing lighting. Only applies (and only can be set) when LightingObstructionModel is eLightingObstructionAzElMask or eLightingObstructionTerrain. Uses Time Dimension.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IPlace.laser_environment
    :type: IPlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IPlace.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: max_range_when_computing_az_el_mask
    :canonical: ansys.stk.core.stkobjects.IPlace.max_range_when_computing_az_el_mask
    :type: float

    Gets or sets the maximum range to use when computing the az el mask using terrain data. Zero indicates to use algorithm default. Only applies when GetAzElMask returns eTerrainData (cannot be set if eMaskFile). Uses Distance Dimension.


Method detail
-------------







.. py:method:: set_az_el_mask(self, type: AZ_EL_MASK_TYPE, data: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IPlace.set_az_el_mask

    Set an az-el mask. A member of the AgEAzElMaskType enumeration.

    :Parameters:

    **type** : :obj:`~AZ_EL_MASK_TYPE`
    **data** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`








.. py:method:: reset_az_el_mask(self) -> None
    :canonical: ansys.stk.core.stkobjects.IPlace.reset_az_el_mask

    Reset the az-el mask.

    :Returns:

        :obj:`~None`

.. py:method:: get_az_el_mask(self) -> AZ_EL_MASK_TYPE
    :canonical: ansys.stk.core.stkobjects.IPlace.get_az_el_mask

    Get the az-el mask. A member of the AgEAzElMaskType enumeration.

    :Returns:

        :obj:`~AZ_EL_MASK_TYPE`

.. py:method:: get_az_el_mask_data(self) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.IPlace.get_az_el_mask_data

    Get az-el mask data.

    :Returns:

        :obj:`~typing.Any`


















