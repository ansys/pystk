VehicleTargetPointingIntervalCollection
=======================================

.. py:class:: ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection

   Represents a collection of scheduled targeting intervals.

.. py:currentmodule:: VehicleTargetPointingIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.add`
              - Add a new element to the collection. Start/Stop Times use DateFormat Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleTargetPointingIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> AttitudeScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AttitudeScheduleTimesElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, start_time: typing.Any, stop_time: typing.Any) -> AttitudeScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection.add

    Add a new element to the collection. Start/Stop Times use DateFormat Dimension.

    :Parameters:

    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~AttitudeScheduleTimesElement`

