ITarget
=======

.. py:class:: ITarget

   object
   
   Provide access to the properties and methods used in defining a target object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_az_el_mask`
              - Set an az-el mask. A member of the AgEAzElMaskType enumeration.
            * - :py:meth:`~reset_az_el_mask`
              - Reset the az-el mask.
            * - :py:meth:`~get_az_el_mask`
              - Get the az-el mask. A member of the AgEAzElMaskType enumeration.
            * - :py:meth:`~get_az_el_mask_data`
              - Get az-el mask data.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_local_time_offset`
            * - :py:meth:`~local_time_offset`
            * - :py:meth:`~use_terrain`
            * - :py:meth:`~graphics`
            * - :py:meth:`~position`
            * - :py:meth:`~terrain_norm`
            * - :py:meth:`~terrain_norm_data`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~height_above_ground`
            * - :py:meth:`~altitude_reference`
            * - :py:meth:`~atmosphere`
            * - :py:meth:`~radar_clutter_map`
            * - :py:meth:`~radar_cross_section`
            * - :py:meth:`~save_terrain_mask_data_in_binary`
            * - :py:meth:`~lighting_obstruction_model`
            * - :py:meth:`~lighting_max_step`
            * - :py:meth:`~laser_environment`
            * - :py:meth:`~rf_environment`
            * - :py:meth:`~max_range_when_computing_az_el_mask`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITarget


Property detail
---------------

.. py:property:: use_local_time_offset
    :canonical: ansys.stk.core.stkobjects.ITarget.use_local_time_offset
    :type: bool

    Opt whether to use a local time offset from GMT.

.. py:property:: local_time_offset
    :canonical: ansys.stk.core.stkobjects.ITarget.local_time_offset
    :type: float

    The amount of the time offset from GMT, if this option is used. Uses Time Dimension.

.. py:property:: use_terrain
    :canonical: ansys.stk.core.stkobjects.ITarget.use_terrain
    :type: bool

    Opt whether to set altitude automatically by using terrain data.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ITarget.graphics
    :type: "IAgTargetGraphics"

    Get the 2D Graphics properties of the target.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.ITarget.position
    :type: "IAgPosition"

    Get the position of the target.

.. py:property:: terrain_norm
    :canonical: ansys.stk.core.stkobjects.ITarget.terrain_norm
    :type: None

    Set the normal to the local terrain.

.. py:property:: terrain_norm_data
    :canonical: ansys.stk.core.stkobjects.ITarget.terrain_norm_data
    :type: "IAgTerrainNormData"

    Data used in specifying terrain slope.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ITarget.graphics_3d
    :type: "IAgTargetVO"

    Get the 3D Graphics properties of the target.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.ITarget.access_constraints
    :type: "IAgAccessConstraintCollection"

    Get the constraints imposed on the target.

.. py:property:: height_above_ground
    :canonical: ansys.stk.core.stkobjects.ITarget.height_above_ground
    :type: None

    Height of target above its model of the ground. Height is measured along the normal to surface defined by reference ellipsoid of the central body. Target models the ground as an ellipsoid passing through the ground position. Uses Distance Dimension.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.ITarget.altitude_reference
    :type: None

    Gets or sets the altitude reference of the object.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.ITarget.atmosphere
    :type: "IAgAtmosphere"

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.ITarget.radar_clutter_map
    :type: "IAgRadarClutterMapInheritable"

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ITarget.radar_cross_section
    :type: "IAgRadarCrossSectionInheritable"

    Returns the radar cross sectoin.

.. py:property:: save_terrain_mask_data_in_binary
    :canonical: ansys.stk.core.stkobjects.ITarget.save_terrain_mask_data_in_binary
    :type: bool

    Save terrain az-el mask data in binary.

.. py:property:: lighting_obstruction_model
    :canonical: ansys.stk.core.stkobjects.ITarget.lighting_obstruction_model
    :type: "LIGHTING_OBSTRUCTION_MODEL_TYPE"

    Gets or sets the obstruction model used in lighting computations.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.ITarget.lighting_max_step
    :type: float

    Gets or sets the maximum step size to use when computing lighting. Only applies (and only can be set) when LightingObstructionModel is eLightingObstructionAzElMask or eLightingObstructionTerrain. Uses Time Dimension.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.ITarget.laser_environment
    :type: "IAgPlatformLaserEnvironment"

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.ITarget.rf_environment
    :type: "IAgPlatformRFEnvironment"

    Gets the RF environment.

.. py:property:: max_range_when_computing_az_el_mask
    :canonical: ansys.stk.core.stkobjects.ITarget.max_range_when_computing_az_el_mask
    :type: float

    Gets or sets the maximum range to use when computing the az el mask using terrain data. Zero indicates to use algorithm default. Only applies when GetAzElMask returns eTerrainData (cannot be set if eMaskFile). Uses Distance Dimension.


Method detail
-------------







.. py:method:: set_az_el_mask(self, type:"AZ_EL_MASK_TYPE", data:typing.Any) -> None

    Set an az-el mask. A member of the AgEAzElMaskType enumeration.

    :Parameters:

    **type** : :obj:`~"AZ_EL_MASK_TYPE"`
    **data** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`








.. py:method:: reset_az_el_mask(self) -> None

    Reset the az-el mask.

    :Returns:

        :obj:`~None`

.. py:method:: get_az_el_mask(self) -> "AZ_EL_MASK_TYPE"

    Get the az-el mask. A member of the AgEAzElMaskType enumeration.

    :Returns:

        :obj:`~"AZ_EL_MASK_TYPE"`

.. py:method:: get_az_el_mask_data(self) -> typing.Any

    Get az-el mask data.

    :Returns:

        :obj:`~typing.Any`


















