ITimeToolEventArrayFactory
==========================

.. py:class:: ITimeToolEventArrayFactory

   object
   
   The factory creates event arrays.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create and register an event array using specified name, description, and type.
            * - :py:meth:`~create_event_array_extrema`
              - Create an event array by determining times of local minimum and/or maximum of specified scalar calculation.
            * - :py:meth:`~create_event_array_start_stop_times`
              - Create an event array by taking start and/or stop times of every interval in the specified reference interval list and adding them to array.
            * - :py:meth:`~create_event_array_merged`
              - Create an event array by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays.
            * - :py:meth:`~create_event_array_filtered`
              - Create an event array by filtering times from an original time array according to specified filtering method.
            * - :py:meth:`~create_event_array_fixed_step`
              - Create an event array using fixed time steps from the specified time reference and adding sampled times to array if they fall within specified bounding interval list.
            * - :py:meth:`~create_event_array_condition_crossings`
              - Create an event array containing times at which the specified condition will change its satisfaction status.
            * - :py:meth:`~create_event_array_signaled`
              - Create an event array recorded at target clock location by performing signal transmission of original time array between base and target clock locations.
            * - :py:meth:`~is_type_supported`
              - Return whether the specified type is supported.
            * - :py:meth:`~create_event_array_fixed_times`
              - Create an event array using specified times.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CRDN_EVENT_ARRAY_TYPE) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create

    Create and register an event array using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_EVENT_ARRAY_TYPE`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: create_event_array_extrema(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_extrema

    Create an event array by determining times of local minimum and/or maximum of specified scalar calculation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: create_event_array_start_stop_times(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_start_stop_times

    Create an event array by taking start and/or stop times of every interval in the specified reference interval list and adding them to array.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: create_event_array_merged(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_merged

    Create an event array by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: create_event_array_filtered(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_filtered

    Create an event array by filtering times from an original time array according to specified filtering method.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: create_event_array_fixed_step(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_fixed_step

    Create an event array using fixed time steps from the specified time reference and adding sampled times to array if they fall within specified bounding interval list.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: create_event_array_condition_crossings(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_condition_crossings

    Create an event array containing times at which the specified condition will change its satisfaction status.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: create_event_array_signaled(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_signaled

    Create an event array recorded at target clock location by performing signal transmission of original time array between base and target clock locations.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

.. py:method:: is_type_supported(self, eType: CRDN_EVENT_ARRAY_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_EVENT_ARRAY_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_event_array_fixed_times(self, name: str, description: str) -> ITimeToolEventArray
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFactory.create_event_array_fixed_times

    Create an event array using specified times.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventArray`

