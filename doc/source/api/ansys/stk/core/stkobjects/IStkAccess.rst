IStkAccess
==========

.. py:class:: IStkAccess

   object
   
   Provide access to the Data Providers and access computations.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove_access`
              - Remove the access that was computed between two objects.
            * - :py:meth:`~compute_access`
              - Recomputes the access between two objects.  Calls to ComputeAccess should not be made between calls to BeginUpdate and EndUpdate.
            * - :py:meth:`~specify_access_time_period`
              - If eUserSpec is selected for AccessTimePeriod, specify the start and stop times for the user-defined period.
            * - :py:meth:`~specify_access_intervals`
              - Allow a list of intervals to be used for the access calculation.
            * - :py:meth:`~specify_access_event_intervals`
              - Access is computed using the intervals in the specified event interval list.
            * - :py:meth:`~clear_access`
              - Clear the access intervals, but not the definitional settings of the access object itself (like step size, light time delay settings, time interval, etc.).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~data_providers`
            * - :py:meth:`~access_time_period`
            * - :py:meth:`~graphics`
            * - :py:meth:`~advanced`
            * - :py:meth:`~data_displays`
            * - :py:meth:`~computed_access_interval_times`
            * - :py:meth:`~access_time_period_data`
            * - :py:meth:`~vgt`
            * - :py:meth:`~save_computed_data`
            * - :py:meth:`~base`
            * - :py:meth:`~target`
            * - :py:meth:`~name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkAccess


Property detail
---------------

.. py:property:: data_providers
    :canonical: ansys.stk.core.stkobjects.IStkAccess.data_providers
    :type: "IAgDataProviderCollection"

    Returns the object representing a list of available data providers for the object.

.. py:property:: access_time_period
    :canonical: ansys.stk.core.stkobjects.IStkAccess.access_time_period
    :type: "ACCESS_TIME_TYPE"

    Specifies the time period option. A member of the AgEAccessTimeType enumeration.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IStkAccess.graphics
    :type: "IAgStkAccessGraphics"

    Gets the Graphics properties for the Access computations.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.IStkAccess.advanced
    :type: "IAgStkAccessAdvanced"

    Gets the Advanced properties for the Access computations.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.IStkAccess.data_displays
    :type: "IAgVODataDisplayCollection"

    Gets the VO Data Display Collection.

.. py:property:: computed_access_interval_times
    :canonical: ansys.stk.core.stkobjects.IStkAccess.computed_access_interval_times
    :type: "IAgIntervalCollection"

    Returns a list of the computed access interval times.

.. py:property:: access_time_period_data
    :canonical: ansys.stk.core.stkobjects.IStkAccess.access_time_period_data
    :type: "IAgAccessInterval"

    Returns an IAgIntervalCollection if AccessTimePeriod is eAccessTimeIntervals; returns an IAgAccessTimePeriod if AccessTimePeriod is eUserSpecAccessTime; returns an IAgAccessTimeEventIntervals if AccessTimePeriod is eAccessTimeEventIntervals.

.. py:property:: vgt
    :canonical: ansys.stk.core.stkobjects.IStkAccess.vgt
    :type: "IAgCrdnProvider"

    Gets a VGT provider to access the analytical vector geometry, timeline, calculation and other types of components.

.. py:property:: save_computed_data
    :canonical: ansys.stk.core.stkobjects.IStkAccess.save_computed_data
    :type: bool

    Flag indicating whether to save computed data with the Access instance.

.. py:property:: base
    :canonical: ansys.stk.core.stkobjects.IStkAccess.base
    :type: "IAgStkObject"

    Base object used in the access.

.. py:property:: target
    :canonical: ansys.stk.core.stkobjects.IStkAccess.target
    :type: "IAgStkObject"

    Target object used in the access.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IStkAccess.name
    :type: str

    Name of the access.


Method detail
-------------


.. py:method:: remove_access(self) -> None

    Remove the access that was computed between two objects.

    :Returns:

        :obj:`~None`

.. py:method:: compute_access(self) -> None

    Recomputes the access between two objects.  Calls to ComputeAccess should not be made between calls to BeginUpdate and EndUpdate.

    :Returns:

        :obj:`~None`



.. py:method:: specify_access_time_period(self, startTime:typing.Any, stopTime:typing.Any) -> None

    If eUserSpec is selected for AccessTimePeriod, specify the start and stop times for the user-defined period.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`




.. py:method:: specify_access_intervals(self, accessIntervals:list) -> None

    Allow a list of intervals to be used for the access calculation.

    :Parameters:

    **accessIntervals** : :obj:`~list`

    :Returns:

        :obj:`~None`



.. py:method:: specify_access_event_intervals(self, pEventIntervalList:"ITimeToolEventIntervalList") -> None

    Access is computed using the intervals in the specified event interval list.

    :Parameters:

    **pEventIntervalList** : :obj:`~"ITimeToolEventIntervalList"`

    :Returns:

        :obj:`~None`

.. py:method:: clear_access(self) -> None

    Clear the access intervals, but not the definitional settings of the access object itself (like step size, light time delay settings, time interval, etc.).

    :Returns:

        :obj:`~None`







