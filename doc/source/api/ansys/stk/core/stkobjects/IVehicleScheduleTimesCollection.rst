IVehicleScheduleTimesCollection
===============================

.. py:class:: IVehicleScheduleTimesCollection

   object
   
   List of scheduled accesses.

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
              - Add a new element to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~available_targets`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleScheduleTimesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_targets
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesCollection.available_targets
    :type: list

    Returns a list of available targets.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleScheduleTimesElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, targetPath: str) -> IVehicleScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesCollection.add

    Add a new element to the collection.

    :Parameters:

    **targetPath** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleScheduleTimesElement`


