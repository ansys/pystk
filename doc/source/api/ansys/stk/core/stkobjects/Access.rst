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
              - Returns the object representing a list of available data providers for the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.access_time_period`
              - Specifies the time period option. A member of the AgEAccessTimeType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.graphics`
              - Gets the Graphics properties for the Access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.advanced`
              - Gets the Advanced properties for the Access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.data_displays`
              - Gets the VO Data Display Collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.computed_access_interval_times`
              - Returns a list of the computed access interval times.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.access_time_period_data`
              - Returns an IAgIntervalCollection if AccessTimePeriod is eAccessTimeIntervals; returns an IAgAccessTimePeriod if AccessTimePeriod is eUserSpecAccessTime; returns an IAgAccessTimeEventIntervals if AccessTimePeriod is eAccessTimeEventIntervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.analysis_workbench_components`
              - Gets a VGT provider to access the analytical vector geometry, timeline, calculation and other types of components.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.save_computed_data`
              - Flag indicating whether to save computed data with the Access instance.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.base`
              - Base object used in the access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.target`
              - Target object used in the access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Access.name`
              - Name of the access.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Access


Property detail
---------------

.. py:property:: data_providers
    :canonical: ansys.stk.core.stkobjects.Access.data_providers
    :type: DataProviderCollection

    Returns the object representing a list of available data providers for the object.

.. py:property:: access_time_period
    :canonical: ansys.stk.core.stkobjects.Access.access_time_period
    :type: ACCESS_TIME_TYPE

    Specifies the time period option. A member of the AgEAccessTimeType enumeration.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Access.graphics
    :type: AccessGraphics

    Gets the Graphics properties for the Access computations.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.Access.advanced
    :type: AccessAdvancedSettings

    Gets the Advanced properties for the Access computations.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.Access.data_displays
    :type: Graphics3DDataDisplayCollection

    Gets the VO Data Display Collection.

.. py:property:: computed_access_interval_times
    :canonical: ansys.stk.core.stkobjects.Access.computed_access_interval_times
    :type: TimeIntervalCollection

    Returns a list of the computed access interval times.

.. py:property:: access_time_period_data
    :canonical: ansys.stk.core.stkobjects.Access.access_time_period_data
    :type: IAccessInterval

    Returns an IAgIntervalCollection if AccessTimePeriod is eAccessTimeIntervals; returns an IAgAccessTimePeriod if AccessTimePeriod is eUserSpecAccessTime; returns an IAgAccessTimeEventIntervals if AccessTimePeriod is eAccessTimeEventIntervals.

.. py:property:: analysis_workbench_components
    :canonical: ansys.stk.core.stkobjects.Access.analysis_workbench_components
    :type: IAnalysisWorkbenchComponentProvider

    Gets a VGT provider to access the analytical vector geometry, timeline, calculation and other types of components.

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







