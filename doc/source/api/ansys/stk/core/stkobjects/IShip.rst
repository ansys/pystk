IShip
=====

.. py:class:: IShip

   IGreatArcVehicle
   
   Interface for a ship object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~graphics`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~export_tools`
            * - :py:meth:`~atmosphere`
            * - :py:meth:`~radar_clutter_map`
            * - :py:meth:`~radar_cross_section`
            * - :py:meth:`~laser_environment`
            * - :py:meth:`~rf_environment`
            * - :py:meth:`~lighting_max_step_terrain`
            * - :py:meth:`~lighting_max_step_central_body_shape`
            * - :py:meth:`~get_eoir`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IShip


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IShip.graphics
    :type: IAgShGraphics

    Get the ship's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IShip.graphics_3d
    :type: IAgShVO

    Get the ship's 3D Graphics properties.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.IShip.export_tools
    :type: IAgShExportTools

    Returns the IAgShExportTools interface.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.IShip.atmosphere
    :type: IAgAtmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.IShip.radar_clutter_map
    :type: IAgRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IShip.radar_cross_section
    :type: IAgRadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IShip.laser_environment
    :type: IAgPlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IShip.rf_environment
    :type: IAgPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.IShip.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.IShip.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir
    :canonical: ansys.stk.core.stkobjects.IShip.get_eoir
    :type: IAgEOIR

    Get the EOIR properties of the ship.


