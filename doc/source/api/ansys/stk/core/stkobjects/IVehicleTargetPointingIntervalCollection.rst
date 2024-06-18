IVehicleTargetPointingIntervalCollection
========================================

.. py:class:: IVehicleTargetPointingIntervalCollection

   object
   
   Represents a collection of scheduled targeting intervals.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection. Start/Stop Times use DateFormat Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTargetPointingIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingIntervalCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingIntervalCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IVehicleScheduleTimesElement"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVehicleScheduleTimesElement"`


.. py:method:: remove_at(self, index:int) -> None

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, startTime:typing.Any, stopTime:typing.Any) -> "IVehicleScheduleTimesElement"

    Add a new element to the collection. Start/Stop Times use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IVehicleScheduleTimesElement"`

