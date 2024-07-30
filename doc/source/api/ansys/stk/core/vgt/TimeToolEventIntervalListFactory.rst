TimeToolEventIntervalListFactory
================================

.. py:class:: ansys.stk.core.vgt.TimeToolEventIntervalListFactory

   Bases: 

   The factory creates event interval lists.

.. py:currentmodule:: TimeToolEventIntervalListFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create`
              - Create and register an interval list using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_merged`
              - Create an interval list by merging two constituent interval lists using specified logical operation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_filtered`
              - Create an interval list by filtering intervals from original interval list using specified filtering method.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_condition`
              - Create an interval list containing intervals during which specified condition is satisfied.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_scaled`
              - Create an interval list defined by scaling every interval in original interval list using either absolute or relative scale.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_signaled`
              - Create an interval list recorded at the target clock location by performing signal transmission of original interval list between base and target clock locations.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_time_offset`
              - Create an interval list defined by shifting the specified reference interval list by a fixed time offset.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_file`
              - Create an interval list based on specified interval file.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_fixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventIntervalListFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CRDN_EVENT_INTERVAL_LIST_TYPE) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create

    Create and register an interval list using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_EVENT_INTERVAL_LIST_TYPE`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: create_event_interval_list_merged(self, name: str, description: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_merged

    Create an interval list by merging two constituent interval lists using specified logical operation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: create_event_interval_list_filtered(self, name: str, description: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_filtered

    Create an interval list by filtering intervals from original interval list using specified filtering method.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: create_event_interval_list_condition(self, name: str, description: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_condition

    Create an interval list containing intervals during which specified condition is satisfied.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: create_event_interval_list_scaled(self, name: str, description: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_scaled

    Create an interval list defined by scaling every interval in original interval list using either absolute or relative scale.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: create_event_interval_list_signaled(self, name: str, description: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_signaled

    Create an interval list recorded at the target clock location by performing signal transmission of original interval list between base and target clock locations.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: create_event_interval_list_time_offset(self, name: str, description: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_time_offset

    Create an interval list defined by shifting the specified reference interval list by a fixed time offset.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: is_type_supported(self, eType: CRDN_EVENT_INTERVAL_LIST_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_EVENT_INTERVAL_LIST_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_event_interval_list_file(self, name: str, description: str, filePath: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_file

    Create an interval list based on specified interval file.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **filePath** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: create_event_interval_list_fixed(self, name: str, description: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFactory.create_event_interval_list_fixed

    Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

