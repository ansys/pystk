GroundVehicle
=============

.. py:class:: ansys.stk.core.stkobjects.GroundVehicle

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IGreatArcVehicle`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Ground vehicle object.

.. py:currentmodule:: GroundVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.graphics`
              - Get the ground vehicle's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.graphics_3d`
              - Get the ground vehicle's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.export_tools`
              - Returns the IAgGvExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.atmosphere`
              - This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.radar_clutter_map`
              - Returns the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.radar_cross_section`
              - Returns the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.laser_environment`
              - Gets the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.rf_environment`
              - Gets the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_terrain`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_central_body_shape`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.get_eoir_settings`
              - Get the EOIR properties of the gound vehicle.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import GroundVehicle


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.graphics
    :type: GroundVehicleGraphics

    Get the ground vehicle's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.graphics_3d
    :type: GroundVehicleGraphics3D

    Get the ground vehicle's 3D Graphics properties.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.export_tools
    :type: GroundVehicleExportTools

    Returns the IAgGvExportTools interface.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.atmosphere
    :type: Atmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.radar_cross_section
    :type: RadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.laser_environment
    :type: PlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_maximum_step_terrain
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_maximum_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir_settings
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.get_eoir_settings
    :type: IEOIR

    Get the EOIR properties of the gound vehicle.


