Ship
====

.. py:class:: ansys.stk.core.stkobjects.Ship

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IGreatArcVehicle`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Ship object.

.. py:currentmodule:: Ship

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.chain_analysis_options`
              - Get the ship's chain analysis options.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.export_tools`
              - Return the ShipExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.get_eoir_settings`
              - Get the EOIR properties of the ship.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.graphics`
              - Get the ship's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.graphics_3d`
              - Get the ship's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.laser_environment`
              - Get the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.lighting_maximum_step_central_body_shape`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.lighting_maximum_step_terrain`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.radar_cross_section`
              - Return the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.Ship.rf_environment`
              - Get the RF environment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Ship


Property detail
---------------

.. py:property:: chain_analysis_options
    :canonical: ansys.stk.core.stkobjects.Ship.chain_analysis_options
    :type: ChainAnalysisOptions

    Get the ship's chain analysis options.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.Ship.export_tools
    :type: ShipExportTools

    Return the ShipExportTools interface.

.. py:property:: get_eoir_settings
    :canonical: ansys.stk.core.stkobjects.Ship.get_eoir_settings
    :type: IEOIR

    Get the EOIR properties of the ship.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Ship.graphics
    :type: ShipGraphics

    Get the ship's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Ship.graphics_3d
    :type: ShipGraphics3D

    Get the ship's 3D Graphics properties.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Ship.laser_environment
    :type: PlatformLaserEnvironment

    Get the laser environment.

.. py:property:: lighting_maximum_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.Ship.lighting_maximum_step_central_body_shape
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: lighting_maximum_step_terrain
    :canonical: ansys.stk.core.stkobjects.Ship.lighting_maximum_step_terrain
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.Ship.radar_cross_section
    :type: RadarCrossSectionInheritable

    Return the radar cross sectoin.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Ship.rf_environment
    :type: PlatformRFEnvironment

    Get the RF environment.


