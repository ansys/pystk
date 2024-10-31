Aircraft
========

.. py:class:: ansys.stk.core.stkobjects.Aircraft

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IGreatArcVehicle`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Aircraft object.

.. py:currentmodule:: Aircraft

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.graphics`
              - Get the aircraft's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.graphics_3d`
              - Get the aircraft's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.export_tools`
              - Returns the IAgAcExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.atmosphere`
              - This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.radar_clutter_map`
              - Returns the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.radar_cross_section`
              - Returns the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.laser_environment`
              - Gets the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.rf_environment`
              - Gets the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_terrain`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_central_body_shape`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.get_eoir_settings`
              - Get the EOIR properties of the aircraft.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Aircraft


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Aircraft.graphics
    :type: AircraftGraphics

    Get the aircraft's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Aircraft.graphics_3d
    :type: AircraftGraphics3D

    Get the aircraft's 3D Graphics properties.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.Aircraft.export_tools
    :type: AircraftExportTools

    Returns the IAgAcExportTools interface.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.Aircraft.atmosphere
    :type: Atmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.Aircraft.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.Aircraft.radar_cross_section
    :type: RadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Aircraft.laser_environment
    :type: PlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Aircraft.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_maximum_step_terrain
    :canonical: ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_maximum_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir_settings
    :canonical: ansys.stk.core.stkobjects.Aircraft.get_eoir_settings
    :type: IEOIR

    Get the EOIR properties of the aircraft.


