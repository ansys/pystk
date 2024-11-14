VehicleGraphics2DIntervalsCollection
====================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection

   Custom Intervals Graphics List.

.. py:currentmodule:: VehicleGraphics2DIntervalsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.add`
              - Add a new element to the collection. Start/Stop params use DateFormat Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DIntervalsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGraphics2DInterval
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleGraphics2DInterval`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, start: typing.Any, stop: typing.Any) -> VehicleGraphics2DInterval
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection.add

    Add a new element to the collection. Start/Stop params use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~VehicleGraphics2DInterval`

