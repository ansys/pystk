ITimeToolEventIntervalFactory
=============================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalFactory

   object
   
   The factory creates event intervals.

.. py:currentmodule:: ITimeToolEventIntervalFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create`
              - Create and register an interval using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_fixed`
              - Create an interval defined between two explicitly specified start and stop times.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_fixed_duration`
              - Create an interval of fixed duration specified using start and stop offsets relative to specified reference time instant.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_between_time_instants`
              - Create an interval using specified start and stop time instants.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_from_interval_list`
              - Create an interval from a specified interval list by using one of several selection methods.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_scaled`
              - Create an interval by scaling an original interval using either absolute or relative scale.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_signaled`
              - Create an interval that is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_time_offset`
              - Create an interval defined by shifting the specified reference interval by a fixed time offset.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFactory.is_type_supported`
              - Return whether the specified type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CRDN_EVENT_INTERVAL_TYPE) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create

    Create and register an interval using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_EVENT_INTERVAL_TYPE`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: create_event_interval_fixed(self, name: str, description: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_fixed

    Create an interval defined between two explicitly specified start and stop times.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: create_event_interval_fixed_duration(self, name: str, description: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_fixed_duration

    Create an interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: create_event_interval_between_time_instants(self, name: str, description: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_between_time_instants

    Create an interval using specified start and stop time instants.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: create_event_interval_from_interval_list(self, name: str, description: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_from_interval_list

    Create an interval from a specified interval list by using one of several selection methods.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: create_event_interval_scaled(self, name: str, description: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_scaled

    Create an interval by scaling an original interval using either absolute or relative scale.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: create_event_interval_signaled(self, name: str, description: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_signaled

    Create an interval that is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: create_event_interval_time_offset(self, name: str, description: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.create_event_interval_time_offset

    Create an interval defined by shifting the specified reference interval by a fixed time offset.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: is_type_supported(self, eType: CRDN_EVENT_INTERVAL_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_EVENT_INTERVAL_TYPE`

    :Returns:

        :obj:`~bool`

