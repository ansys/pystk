TimeToolTimeArrayFactory
========================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeArrayFactory

   The factory creates event arrays.

.. py:currentmodule:: TimeToolTimeArrayFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create`
              - Create and register an event array using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_extrema`
              - Create an event array by determining times of local minimum and/or maximum of specified scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_start_stop_times`
              - Create an event array by taking start and/or stop times of every interval in the specified reference interval list and adding them to array.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_merged`
              - Create an event array by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_filtered`
              - Create an event array by filtering times from an original time array according to specified filtering method.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_fixed_step`
              - Create an event array using fixed time steps from the specified time reference and adding sampled times to array if they fall within specified bounding interval list.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_condition_crossings`
              - Create an event array containing times at which the specified condition will change its satisfaction status.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_signaled`
              - Create an event array recorded at target clock location by performing signal transmission of original time array between base and target clock locations.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_fixed_times`
              - Create an event array using specified times.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeArrayFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: EVENT_ARRAY_TYPE) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create

    Create and register an event array using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~EVENT_ARRAY_TYPE`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: create_extrema(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_extrema

    Create an event array by determining times of local minimum and/or maximum of specified scalar calculation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: create_start_stop_times(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_start_stop_times

    Create an event array by taking start and/or stop times of every interval in the specified reference interval list and adding them to array.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: create_merged(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_merged

    Create an event array by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: create_filtered(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_filtered

    Create an event array by filtering times from an original time array according to specified filtering method.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: create_fixed_step(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_fixed_step

    Create an event array using fixed time steps from the specified time reference and adding sampled times to array if they fall within specified bounding interval list.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: create_condition_crossings(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_condition_crossings

    Create an event array containing times at which the specified condition will change its satisfaction status.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: create_signaled(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_signaled

    Create an event array recorded at target clock location by performing signal transmission of original time array between base and target clock locations.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

.. py:method:: is_type_supported(self, eType: EVENT_ARRAY_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~EVENT_ARRAY_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_fixed_times(self, name: str, description: str) -> ITimeToolTimeArray
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFactory.create_fixed_times

    Create an event array using specified times.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeArray`

