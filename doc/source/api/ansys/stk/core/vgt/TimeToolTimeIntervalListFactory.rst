TimeToolTimeIntervalListFactory
===============================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory

   The factory creates event interval lists.

.. py:currentmodule:: TimeToolTimeIntervalListFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create`
              - Create and register an interval list using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_merged`
              - Create an interval list by merging two constituent interval lists using specified logical operation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_filtered`
              - Create an interval list by filtering intervals from original interval list using specified filtering method.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_from_condition`
              - Create an interval list containing intervals during which specified condition is satisfied.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_scaled`
              - Create an interval list defined by scaling every interval in original interval list using either absolute or relative scale.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_signaled`
              - Create an interval list recorded at the target clock location by performing signal transmission of original interval list between base and target clock locations.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_time_offset`
              - Create an interval list defined by shifting the specified reference interval list by a fixed time offset.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_from_file`
              - Create an interval list based on specified interval file.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_fixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalListFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: EVENT_INTERVAL_LIST_TYPE) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create

    Create and register an interval list using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~EVENT_INTERVAL_LIST_TYPE`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: create_merged(self, name: str, description: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_merged

    Create an interval list by merging two constituent interval lists using specified logical operation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: create_filtered(self, name: str, description: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_filtered

    Create an interval list by filtering intervals from original interval list using specified filtering method.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: create_from_condition(self, name: str, description: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_from_condition

    Create an interval list containing intervals during which specified condition is satisfied.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: create_scaled(self, name: str, description: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_scaled

    Create an interval list defined by scaling every interval in original interval list using either absolute or relative scale.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: create_signaled(self, name: str, description: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_signaled

    Create an interval list recorded at the target clock location by performing signal transmission of original interval list between base and target clock locations.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: create_time_offset(self, name: str, description: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_time_offset

    Create an interval list defined by shifting the specified reference interval list by a fixed time offset.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: is_type_supported(self, type: EVENT_INTERVAL_LIST_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **type** : :obj:`~EVENT_INTERVAL_LIST_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_from_file(self, name: str, description: str, file_path: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_from_file

    Create an interval list based on specified interval file.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **file_path** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: create_fixed(self, name: str, description: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFactory.create_fixed

    Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

