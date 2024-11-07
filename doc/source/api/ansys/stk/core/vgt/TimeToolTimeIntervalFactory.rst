TimeToolTimeIntervalFactory
===========================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalFactory

   The factory creates event intervals.

.. py:currentmodule:: TimeToolTimeIntervalFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create`
              - Create and register an interval using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_fixed`
              - Create an interval defined between two explicitly specified start and stop times.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_fixed_duration`
              - Create an interval of fixed duration specified using start and stop offsets relative to specified reference time instant.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_between_time_instants`
              - Create an interval using specified start and stop time instants.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_from_interval_list`
              - Create an interval from a specified interval list by using one of several selection methods.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_scaled`
              - Create an interval by scaling an original interval using either absolute or relative scale.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_signaled`
              - Create an interval that is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_time_offset`
              - Create an interval defined by shifting the specified reference interval by a fixed time offset.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory.is_type_supported`
              - Return whether the specified type is supported.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: EVENT_INTERVAL_TYPE) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create

    Create and register an interval using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~EVENT_INTERVAL_TYPE`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: create_fixed(self, name: str, description: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_fixed

    Create an interval defined between two explicitly specified start and stop times.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: create_fixed_duration(self, name: str, description: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_fixed_duration

    Create an interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: create_between_time_instants(self, name: str, description: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_between_time_instants

    Create an interval using specified start and stop time instants.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: create_from_interval_list(self, name: str, description: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_from_interval_list

    Create an interval from a specified interval list by using one of several selection methods.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: create_scaled(self, name: str, description: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_scaled

    Create an interval by scaling an original interval using either absolute or relative scale.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: create_signaled(self, name: str, description: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_signaled

    Create an interval that is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: create_time_offset(self, name: str, description: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.create_time_offset

    Create an interval defined by shifting the specified reference interval by a fixed time offset.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: is_type_supported(self, type: EVENT_INTERVAL_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **type** : :obj:`~EVENT_INTERVAL_TYPE`

    :Returns:

        :obj:`~bool`

