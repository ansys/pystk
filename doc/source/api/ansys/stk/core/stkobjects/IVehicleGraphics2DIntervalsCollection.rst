IVehicleGraphics2DIntervalsCollection
=====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection

   object
   
   Custom Intervals Graphics List.

.. py:currentmodule:: IVehicleGraphics2DIntervalsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.add`
              - Add a new element to the collection. Start/Stop params use DateFormat Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DIntervalsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics2DInterval
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics2DInterval`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, start: typing.Any, stop: typing.Any) -> IVehicleGraphics2DInterval
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DIntervalsCollection.add

    Add a new element to the collection. Start/Stop params use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVehicleGraphics2DInterval`

