IScenario
=========

.. py:class:: IScenario

   object
   
   IAgScenario Interface for Scenario-level properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_time_period`
              - Set the Scenario time period. startTime/stopTime use DateFormat Dimension.
            * - :py:meth:`~set_dirty`
              - Set the flag indicating the scenario has been modified.
            * - :py:meth:`~get_existing_accesses`
              - Return an array of existing accesses in the current scenario. The result is a two-dimensional array of triplets where each triplet contains the paths of two objects participating in the access and a flag indicating whether the access is computed.
            * - :py:meth:`~get_access_between_objects_by_path`
              - Return an IAgStkAccess object associated with the two STK objects specified using their paths. The paths can be fully-qualified or truncated.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~epoch`
            * - :py:meth:`~animation`
            * - :py:meth:`~earth_data`
            * - :py:meth:`~graphics`
            * - :py:meth:`~gen_dbs`
            * - :py:meth:`~sat_no_orbit_warning`
            * - :py:meth:`~msl_no_orbit_warning`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~aircraft_wgs84_warning`
            * - :py:meth:`~msl_stop_time_warning`
            * - :py:meth:`~terrain`
            * - :py:meth:`~component_directory`
            * - :py:meth:`~scenario_files`
            * - :py:meth:`~is_dirty`
            * - :py:meth:`~use_analysis_start_time_for_epoch`
            * - :py:meth:`~space_environment`
            * - :py:meth:`~scene_manager`
            * - :py:meth:`~analysis_interval`
            * - :py:meth:`~analysis_epoch`
            * - :py:meth:`~radar_clutter_map`
            * - :py:meth:`~radar_cross_section`
            * - :py:meth:`~rf_environment`
            * - :py:meth:`~tilesets`
            * - :py:meth:`~laser_environment`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenario


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IScenario.start_time
    :type: typing.Any

    Scenario start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IScenario.stop_time
    :type: typing.Any

    Scenario stop time. Uses DateFormat Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.IScenario.epoch
    :type: typing.Any

    Scenario epoch. Uses DateFormat Dimension.

.. py:property:: animation
    :canonical: ansys.stk.core.stkobjects.IScenario.animation
    :type: IAgScAnimation

    Scenario animation settings.

.. py:property:: earth_data
    :canonical: ansys.stk.core.stkobjects.IScenario.earth_data
    :type: IAgScEarthData

    Scenario Earth Data settings.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IScenario.graphics
    :type: IAgScGraphics

    Scenario 2D Graphics settings.

.. py:property:: gen_dbs
    :canonical: ansys.stk.core.stkobjects.IScenario.gen_dbs
    :type: IAgScGenDbCollection

    Scenario database settings.

.. py:property:: sat_no_orbit_warning
    :canonical: ansys.stk.core.stkobjects.IScenario.sat_no_orbit_warning
    :type: bool

    Specify whether to display a warning when a satellite orbit intersects the central body.

.. py:property:: msl_no_orbit_warning
    :canonical: ansys.stk.core.stkobjects.IScenario.msl_no_orbit_warning
    :type: bool

    Specify whether to display a warning when a missile trajectory does not impact the central body.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IScenario.graphics_3d
    :type: IAgScVO

    Scenario 3D Graphics settings.

.. py:property:: aircraft_wgs84_warning
    :canonical: ansys.stk.core.stkobjects.IScenario.aircraft_wgs84_warning
    :type: AIRCRAFT_WGS84_WARNING_TYPE

    Specify when to display the aircraft mission modeler WGS84 warning.

.. py:property:: msl_stop_time_warning
    :canonical: ansys.stk.core.stkobjects.IScenario.msl_stop_time_warning
    :type: bool

    Generate a message that warns the user if the missile achieves orbit (and give the perigee) or impacts the surface (and give the interval after missile's stop time).

.. py:property:: terrain
    :canonical: ansys.stk.core.stkobjects.IScenario.terrain
    :type: IAgCentralBodyTerrainCollection

    Returns a list of central bodies and their terrains.

.. py:property:: component_directory
    :canonical: ansys.stk.core.stkobjects.IScenario.component_directory
    :type: IAgComponentDirectory

    Get the component directory interface.

.. py:property:: scenario_files
    :canonical: ansys.stk.core.stkobjects.IScenario.scenario_files
    :type: list

    Returns list of scenario files.

.. py:property:: is_dirty
    :canonical: ansys.stk.core.stkobjects.IScenario.is_dirty
    :type: bool

    Specify whether scenario needs to be saved.

.. py:property:: use_analysis_start_time_for_epoch
    :canonical: ansys.stk.core.stkobjects.IScenario.use_analysis_start_time_for_epoch
    :type: bool

    Whether the scenario Epoch is the same as the scenario's StartTime.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.IScenario.space_environment
    :type: IAgSpEnvScenSpaceEnvironment

    Scenario SpaceEnvironment settings.

.. py:property:: scene_manager
    :canonical: ansys.stk.core.stkobjects.IScenario.scene_manager
    :type: IAgStkGraphicsSceneManager

    A scene manager.

.. py:property:: analysis_interval
    :canonical: ansys.stk.core.stkobjects.IScenario.analysis_interval
    :type: IAgCrdnEventIntervalSmartInterval

    Allows the user to configure the scenario's analysis time period.

.. py:property:: analysis_epoch
    :canonical: ansys.stk.core.stkobjects.IScenario.analysis_epoch
    :type: IAgCrdnEventSmartEpoch

    Allows the user to configure the scenario's analysis epoch.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.IScenario.radar_clutter_map
    :type: IAgRadarClutterMap

    Returns the global radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IScenario.radar_cross_section
    :type: IAgRadarCrossSection

    Returns the global radar cross section.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IScenario.rf_environment
    :type: IAgRFEnvironment

    Returns the RF environment.

.. py:property:: tilesets
    :canonical: ansys.stk.core.stkobjects.IScenario.tilesets
    :type: IAg3DTilesetCollection

    Returns a list of 3D Tilesets used for Analysis.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IScenario.laser_environment
    :type: IAgLaserEnvironment

    Returns the laser environment.


Method detail
-------------





.. py:method:: set_time_period(self, startTime: typing.Any, stopTime: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IScenario.set_time_period

    Set the Scenario time period. startTime/stopTime use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`






















.. py:method:: set_dirty(self) -> None
    :canonical: ansys.stk.core.stkobjects.IScenario.set_dirty

    Set the flag indicating the scenario has been modified.

    :Returns:

        :obj:`~None`





.. py:method:: get_existing_accesses(self) -> list
    :canonical: ansys.stk.core.stkobjects.IScenario.get_existing_accesses

    Return an array of existing accesses in the current scenario. The result is a two-dimensional array of triplets where each triplet contains the paths of two objects participating in the access and a flag indicating whether the access is computed.

    :Returns:

        :obj:`~list`

.. py:method:: get_access_between_objects_by_path(self, objectPath1: str, objectPath2: str) -> IStkAccess
    :canonical: ansys.stk.core.stkobjects.IScenario.get_access_between_objects_by_path

    Return an IAgStkAccess object associated with the two STK objects specified using their paths. The paths can be fully-qualified or truncated.

    :Parameters:

    **objectPath1** : :obj:`~str`
    **objectPath2** : :obj:`~str`

    :Returns:

        :obj:`~IStkAccess`






