IVehicleGraphics2DElevationsCollection
======================================

.. py:class:: IVehicleGraphics2DElevationsCollection

   object
   
   Collection for elevation contours. Used by vehicles.

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
            * - :py:meth:`~add_level`
              - Add a new element to the collection.
            * - :py:meth:`~add_level_range`
              - Add a range of new levels to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DElevationsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevationsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevationsCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IVehicleGraphics2DElevationsElement"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVehicleGraphics2DElevationsElement"`


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

.. py:method:: add_level(self, elevation:float) -> "IVehicleGraphics2DElevationsElement"

    Add a new element to the collection.

    :Parameters:

    **elevation** : :obj:`~float`

    :Returns:

        :obj:`~"IVehicleGraphics2DElevationsElement"`

.. py:method:: add_level_range(self, start:typing.Any, stop:typing.Any, step:typing.Any) -> None

    Add a range of new levels to the collection.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`
    **step** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

