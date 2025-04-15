Scenario
========

.. py:class:: ansys.stk.core.stkobjects.Scenario

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Class defining the Scenario object.

.. py:currentmodule:: Scenario

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.set_time_period`
              - Set the Scenario time period. startTime/stopTime use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.set_dirty`
              - Set the flag indicating the scenario has been modified.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.get_existing_accesses`
              - Return an array of existing accesses in the current scenario. The result is a two-dimensional array of triplets where each triplet contains the paths of two objects participating in the access and a flag indicating whether the access is computed.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.get_access_between_objects_by_path`
              - Return an IAgStkAccess object associated with the two STK objects specified using their paths. The paths can be fully-qualified or truncated.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.start_time`
              - Scenario start time. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.stop_time`
              - Scenario stop time. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.epoch`
              - Scenario epoch. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.animation_settings`
              - Scenario animation settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.earth_data`
              - Scenario Earth Data settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.graphics`
              - Scenario 2D Graphics settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.database_settings`
              - Scenario database settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.display_warning_if_orbit_impacts_ground`
              - Specify whether to display a warning when a satellite orbit intersects the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.show_warning_if_missile_fails_to_impact`
              - Specify whether to display a warning when a missile trajectory does not impact the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.graphics_3d`
              - Scenario 3D Graphics settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.aircraft_wgs84_warning`
              - Specify when to display the aircraft mission modeler WGS84 warning.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.show_warning_whether_missile_achieves_orbit_or_not`
              - Generate a message that warns the user if the missile achieves orbit (and give the perigee) or impacts the surface (and give the interval after missile's stop time).
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.terrain`
              - Return a list of central bodies and their terrains.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.component_directory`
              - Get the component directory interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.scenario_files`
              - Return list of scenario files.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.is_dirty`
              - Specify whether scenario needs to be saved.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.use_analysis_start_time_for_epoch`
              - Whether the scenario Epoch is the same as the scenario's StartTime.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.space_environment`
              - Scenario SpaceEnvironment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.scene_manager`
              - A scene manager.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.analysis_interval`
              - Allow the user to configure the scenario's analysis time period.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.analysis_epoch`
              - Allow the user to configure the scenario's analysis epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.radar_clutter_map`
              - Return the global radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.radar_cross_section`
              - Return the global radar cross section.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.rf_environment`
              - Return the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.tilesets`
              - Return a list of 3D Tilesets used for Analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.Scenario.laser_environment`
              - Return the laser environment.



Examples
--------

Set the current scenario's time period

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    scenario = root.current_scenario
    scenario.set_time_period(
        start_time="1 Jan 2012 12:00:00.000",
        stop_time="2 Jan 2012 12:00:00.000"
    )


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Scenario


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.Scenario.start_time
    :type: typing.Any

    Scenario start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.Scenario.stop_time
    :type: typing.Any

    Scenario stop time. Uses DateFormat Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.Scenario.epoch
    :type: typing.Any

    Scenario epoch. Uses DateFormat Dimension.

.. py:property:: animation_settings
    :canonical: ansys.stk.core.stkobjects.Scenario.animation_settings
    :type: ScenarioAnimation

    Scenario animation settings.

.. py:property:: earth_data
    :canonical: ansys.stk.core.stkobjects.Scenario.earth_data
    :type: ScenarioEarthData

    Scenario Earth Data settings.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Scenario.graphics
    :type: ScenarioGraphics

    Scenario 2D Graphics settings.

.. py:property:: database_settings
    :canonical: ansys.stk.core.stkobjects.Scenario.database_settings
    :type: ScenarioDatabaseCollection

    Scenario database settings.

.. py:property:: display_warning_if_orbit_impacts_ground
    :canonical: ansys.stk.core.stkobjects.Scenario.display_warning_if_orbit_impacts_ground
    :type: bool

    Specify whether to display a warning when a satellite orbit intersects the central body.

.. py:property:: show_warning_if_missile_fails_to_impact
    :canonical: ansys.stk.core.stkobjects.Scenario.show_warning_if_missile_fails_to_impact
    :type: bool

    Specify whether to display a warning when a missile trajectory does not impact the central body.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Scenario.graphics_3d
    :type: ScenarioGraphics3D

    Scenario 3D Graphics settings.

.. py:property:: aircraft_wgs84_warning
    :canonical: ansys.stk.core.stkobjects.Scenario.aircraft_wgs84_warning
    :type: AircraftWGS84WarningType

    Specify when to display the aircraft mission modeler WGS84 warning.

.. py:property:: show_warning_whether_missile_achieves_orbit_or_not
    :canonical: ansys.stk.core.stkobjects.Scenario.show_warning_whether_missile_achieves_orbit_or_not
    :type: bool

    Generate a message that warns the user if the missile achieves orbit (and give the perigee) or impacts the surface (and give the interval after missile's stop time).

.. py:property:: terrain
    :canonical: ansys.stk.core.stkobjects.Scenario.terrain
    :type: CentralBodyTerrainCollection

    Return a list of central bodies and their terrains.

.. py:property:: component_directory
    :canonical: ansys.stk.core.stkobjects.Scenario.component_directory
    :type: ComponentDirectory

    Get the component directory interface.

.. py:property:: scenario_files
    :canonical: ansys.stk.core.stkobjects.Scenario.scenario_files
    :type: list

    Return list of scenario files.

.. py:property:: is_dirty
    :canonical: ansys.stk.core.stkobjects.Scenario.is_dirty
    :type: bool

    Specify whether scenario needs to be saved.

.. py:property:: use_analysis_start_time_for_epoch
    :canonical: ansys.stk.core.stkobjects.Scenario.use_analysis_start_time_for_epoch
    :type: bool

    Whether the scenario Epoch is the same as the scenario's StartTime.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.Scenario.space_environment
    :type: ScenarioSpaceEnvironment

    Scenario SpaceEnvironment settings.

.. py:property:: scene_manager
    :canonical: ansys.stk.core.stkobjects.Scenario.scene_manager
    :type: ISceneManager

    A scene manager.

.. py:property:: analysis_interval
    :canonical: ansys.stk.core.stkobjects.Scenario.analysis_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Allow the user to configure the scenario's analysis time period.

.. py:property:: analysis_epoch
    :canonical: ansys.stk.core.stkobjects.Scenario.analysis_epoch
    :type: ITimeToolInstantSmartEpoch

    Allow the user to configure the scenario's analysis epoch.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.Scenario.radar_clutter_map
    :type: IRadarClutterMap

    Return the global radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.Scenario.radar_cross_section
    :type: RadarCrossSection

    Return the global radar cross section.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Scenario.rf_environment
    :type: RFEnvironment

    Return the RF environment.

.. py:property:: tilesets
    :canonical: ansys.stk.core.stkobjects.Scenario.tilesets
    :type: Tileset3DCollection

    Return a list of 3D Tilesets used for Analysis.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Scenario.laser_environment
    :type: LaserEnvironment

    Return the laser environment.


Method detail
-------------





.. py:method:: set_time_period(self, start_time: typing.Any, stop_time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.Scenario.set_time_period

    Set the Scenario time period. startTime/stopTime use DateFormat Dimension.

    :Parameters:

    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`






















    Examples
    --------

    Set the current scenario's time period

    .. code-block:: python

        # StkObjectRoot root: STK Object Model Root
        scenario = root.current_scenario
        scenario.set_time_period(
            start_time="1 Jan 2012 12:00:00.000",
            stop_time="2 Jan 2012 12:00:00.000"
        )


.. py:method:: set_dirty(self) -> None
    :canonical: ansys.stk.core.stkobjects.Scenario.set_dirty

    Set the flag indicating the scenario has been modified.

    :Returns:

        :obj:`~None`





.. py:method:: get_existing_accesses(self) -> list
    :canonical: ansys.stk.core.stkobjects.Scenario.get_existing_accesses

    Return an array of existing accesses in the current scenario. The result is a two-dimensional array of triplets where each triplet contains the paths of two objects participating in the access and a flag indicating whether the access is computed.

    :Returns:

        :obj:`~list`

.. py:method:: get_access_between_objects_by_path(self, object_path1: str, object_path2: str) -> Access
    :canonical: ansys.stk.core.stkobjects.Scenario.get_access_between_objects_by_path

    Return an IAgStkAccess object associated with the two STK objects specified using their paths. The paths can be fully-qualified or truncated.

    :Parameters:

    **object_path1** : :obj:`~str`
    **object_path2** : :obj:`~str`

    :Returns:

        :obj:`~Access`






