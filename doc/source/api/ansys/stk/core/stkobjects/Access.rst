Access
======

.. py:class:: ansys.stk.core.stkobjects.Access

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Class defining Access.

.. py:currentmodule:: Access

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Access.remove_access`
              - Remove the access that was computed between two objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.compute_access`
              - Recomputes the access between two objects.  Calls to ComputeAccess should not be made between calls to BeginUpdate and EndUpdate.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.specify_access_time_period`
              - If eUserSpec is selected for AccessTimePeriod, specify the start and stop times for the user-defined period.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.specify_access_intervals`
              - Allow a list of intervals to be used for the access calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.specify_access_event_intervals`
              - Access is computed using the intervals in the specified event interval list.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.clear_access`
              - Clear the access intervals, but not the definitional settings of the access object itself (like step size, light time delay settings, time interval, etc.).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Access.data_providers`
              - Return the object representing a list of available data providers for the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.access_time_period`
              - Specify the time period option. A member of the AccessTimeType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.graphics`
              - Get the Graphics properties for the Access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.advanced`
              - Get the Advanced properties for the Access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.data_displays`
              - Get the VO Data Display Collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.computed_access_interval_times`
              - Return a list of the computed access interval times.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.access_time_period_data`
              - Return an TimeIntervalCollection if AccessTimePeriod is eAccessTimeIntervals; returns an AccessTimePeriod if AccessTimePeriod is eUserSpecAccessTime; returns an AccessAllowedTimeIntervals if AccessTimePeriod is eAccessTimeEventIntervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.analysis_workbench_components`
              - Get a VGT provider to access the analytical vector geometry, timeline, calculation and other types of components.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.save_computed_data`
              - Flag indicating whether to save computed data with the Access instance.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.base`
              - Base object used in the access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.target`
              - Target object used in the access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.name`
              - Name of the access.



Examples
--------

Configure the access analysis time period to specified time instants

.. code-block:: python

    # StkObjectRoot root: STK Object Model root

    satellite = root.get_object_from_path("Satellite/MySatellite")
    facility = root.get_object_from_path("Facility/MyFacility")

    # For this code snippet, let's use the time interval when the satellite reached min and max altitude values.
    # Note, this assumes time at min happens before time at max.
    timeOfAltMin = satellite.analysis_workbench_components.time_instants.item(
        "GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"
    )
    timeOfAltMax = satellite.analysis_workbench_components.time_instants.item(
        "GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"
    )

    # Set the access time period with the times we figured out above.
    access = satellite.get_access_to_object(facility)
    access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
    accessTimePeriod = access.access_time_period_data

    accessTimePeriod.access_interval.state = SmartIntervalState.START_STOP

    accessStartEpoch = accessTimePeriod.access_interval.get_start_epoch()
    accessStartEpoch.set_implicit_time(timeOfAltMin)
    accessTimePeriod.access_interval.set_start_epoch(accessStartEpoch)

    accessStopEpoch = accessTimePeriod.access_interval.get_stop_epoch()
    accessStopEpoch.set_implicit_time(timeOfAltMax)
    accessTimePeriod.access_interval.set_stop_epoch(accessStopEpoch)


Compute and extract access interval times

.. code-block:: python

    # Access access: Access calculation
    # Get and display the Computed Access Intervals
    intervalCollection = access.computed_access_interval_times

    # Set the intervals to use to the Computed Access Intervals
    computedIntervals = intervalCollection.to_array(0, -1)
    access.specify_access_intervals(computedIntervals)


Compute Access with Advanced Settings

.. code-block:: python

    # Access access: Access object

    access.advanced.enable_light_time_delay = True
    access.advanced.time_light_delay_convergence = 0.00005
    access.advanced.aberration_type = AberrationType.ANNUAL
    access.advanced.use_default_clock_host_and_signal_sense = False
    access.advanced.clock_host = IvClockHost.BASE
    access.advanced.signal_sense_of_clock_host = IvTimeSense.TRANSMIT
    access.compute_access()


Compute an access between two STK Objects (using object path)

.. code-block:: python

    # Satellite satellite: Satellite object

    # Get access by object path
    access = satellite.get_access("Facility/MyFacility")

    # Compute access
    access.compute_access()


Compute an access between two STK Objects (using IStkObject interface)

.. code-block:: python

    # Satellite satellite: Satellite object
    # Facility facility: Facility object

    # Get access by STK Object
    access = satellite.get_access_to_object(facility)

    # Compute access
    access.compute_access()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Access


Property detail
---------------

.. py:property:: data_providers
    :canonical: ansys.stk.core.stkobjects.Access.data_providers
    :type: DataProviderCollection

    Return the object representing a list of available data providers for the object.

.. py:property:: access_time_period
    :canonical: ansys.stk.core.stkobjects.Access.access_time_period
    :type: AccessTimeType

    Specify the time period option. A member of the AccessTimeType enumeration.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Access.graphics
    :type: AccessGraphics

    Get the Graphics properties for the Access computations.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.Access.advanced
    :type: AccessAdvancedSettings

    Get the Advanced properties for the Access computations.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.Access.data_displays
    :type: Graphics3DDataDisplayCollection

    Get the VO Data Display Collection.

.. py:property:: computed_access_interval_times
    :canonical: ansys.stk.core.stkobjects.Access.computed_access_interval_times
    :type: TimeIntervalCollection

    Return a list of the computed access interval times.

.. py:property:: access_time_period_data
    :canonical: ansys.stk.core.stkobjects.Access.access_time_period_data
    :type: IAccessInterval

    Return an TimeIntervalCollection if AccessTimePeriod is eAccessTimeIntervals; returns an AccessTimePeriod if AccessTimePeriod is eUserSpecAccessTime; returns an AccessAllowedTimeIntervals if AccessTimePeriod is eAccessTimeEventIntervals.

.. py:property:: analysis_workbench_components
    :canonical: ansys.stk.core.stkobjects.Access.analysis_workbench_components
    :type: IAnalysisWorkbenchComponentProvider

    Get a VGT provider to access the analytical vector geometry, timeline, calculation and other types of components.

.. py:property:: save_computed_data
    :canonical: ansys.stk.core.stkobjects.Access.save_computed_data
    :type: bool

    Flag indicating whether to save computed data with the Access instance.

.. py:property:: base
    :canonical: ansys.stk.core.stkobjects.Access.base
    :type: IStkObject

    Base object used in the access.

.. py:property:: target
    :canonical: ansys.stk.core.stkobjects.Access.target
    :type: IStkObject

    Target object used in the access.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.Access.name
    :type: str

    Name of the access.


Method detail
-------------


.. py:method:: remove_access(self) -> None
    :canonical: ansys.stk.core.stkobjects.Access.remove_access

    Remove the access that was computed between two objects.

    :Returns:

        :obj:`~None`

.. py:method:: compute_access(self) -> None
    :canonical: ansys.stk.core.stkobjects.Access.compute_access

    Recomputes the access between two objects.  Calls to ComputeAccess should not be made between calls to BeginUpdate and EndUpdate.

    :Returns:

        :obj:`~None`



.. py:method:: specify_access_time_period(self, start_time: typing.Any, stop_time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.Access.specify_access_time_period

    If eUserSpec is selected for AccessTimePeriod, specify the start and stop times for the user-defined period.

    :Parameters:

    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`




.. py:method:: specify_access_intervals(self, access_intervals: list) -> None
    :canonical: ansys.stk.core.stkobjects.Access.specify_access_intervals

    Allow a list of intervals to be used for the access calculation.

    :Parameters:

    **access_intervals** : :obj:`~list`

    :Returns:

        :obj:`~None`



.. py:method:: specify_access_event_intervals(self, event_interval_list: ITimeToolTimeIntervalList) -> None
    :canonical: ansys.stk.core.stkobjects.Access.specify_access_event_intervals

    Access is computed using the intervals in the specified event interval list.

    :Parameters:

    **event_interval_list** : :obj:`~ITimeToolTimeIntervalList`

    :Returns:

        :obj:`~None`

.. py:method:: clear_access(self) -> None
    :canonical: ansys.stk.core.stkobjects.Access.clear_access

    Clear the access intervals, but not the definitional settings of the access object itself (like step size, light time delay settings, time interval, etc.).

    :Returns:

        :obj:`~None`







