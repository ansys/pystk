IGroundVehicle
==============

.. py:class:: ansys.stk.core.stkobjects.IGroundVehicle

   IGreatArcVehicle
   
   Interface for a ground vehicle object.

.. py:currentmodule:: IGroundVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.graphics`
              - Get the ground vehicle's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.graphics_3d`
              - Get the ground vehicle's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.export_tools`
              - Returns the IAgGvExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.atmosphere`
              - This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.radar_clutter_map`
              - Returns the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.radar_cross_section`
              - Returns the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.laser_environment`
              - Gets the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.rf_environment`
              - Gets the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.lighting_max_step_terrain`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.lighting_max_step_central_body_shape`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicle.get_eoir`
              - Get the EOIR properties of the gound vehicle.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGroundVehicle


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.graphics
    :type: IGroundVehicleGraphics

    Get the ground vehicle's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.graphics_3d
    :type: IGroundVehicleGraphics3D

    Get the ground vehicle's 3D Graphics properties.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.export_tools
    :type: IGroundVehicleExportTools

    Returns the IAgGvExportTools interface.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.atmosphere
    :type: IAtmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.radar_cross_section
    :type: IRadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.laser_environment
    :type: IPlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir
    :canonical: ansys.stk.core.stkobjects.IGroundVehicle.get_eoir
    :type: IEOIR

    Get the EOIR properties of the gound vehicle.


