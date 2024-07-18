VehicleScheduleTimesCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection

   Bases: 

   List of scheduled accesses.

.. py:currentmodule:: VehicleScheduleTimesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.add`
              - Add a new element to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.available_targets`
              - Returns a list of available targets.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleScheduleTimesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_targets
    :canonical: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.available_targets
    :type: list

    Returns a list of available targets.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleScheduleTimesElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, targetPath: str) -> VehicleScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.VehicleScheduleTimesCollection.add

    Add a new element to the collection.

    :Parameters:

    **targetPath** : :obj:`~str`

    :Returns:

        :obj:`~VehicleScheduleTimesElement`


