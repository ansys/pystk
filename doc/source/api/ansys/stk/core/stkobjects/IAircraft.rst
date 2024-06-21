IAircraft
=========

.. py:class:: ansys.stk.core.stkobjects.IAircraft

   IGreatArcVehicle
   
   Interface for aircraft object.

.. py:currentmodule:: IAircraft

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.graphics`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.graphics_3d`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.export_tools`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.atmosphere`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.radar_clutter_map`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.radar_cross_section`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.laser_environment`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.rf_environment`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.lighting_max_step_terrain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.lighting_max_step_central_body_shape`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraft.get_eoir`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAircraft


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IAircraft.graphics
    :type: IAircraftGraphics

    Get the aircraft's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IAircraft.graphics_3d
    :type: IAircraftGraphics3D

    Get the aircraft's 3D Graphics properties.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.IAircraft.export_tools
    :type: IAircraftExportTools

    Returns the IAgAcExportTools interface.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.IAircraft.atmosphere
    :type: IAtmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.IAircraft.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IAircraft.radar_cross_section
    :type: IRadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IAircraft.laser_environment
    :type: IPlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IAircraft.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.IAircraft.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.IAircraft.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir
    :canonical: ansys.stk.core.stkobjects.IAircraft.get_eoir
    :type: IEOIR

    Get the EOIR properties of the aircraft.


