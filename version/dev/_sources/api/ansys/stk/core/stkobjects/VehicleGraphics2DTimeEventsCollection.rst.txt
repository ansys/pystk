VehicleGraphics2DTimeEventsCollection
=====================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection

   A satellite's time events collection.

.. py:currentmodule:: VehicleGraphics2DTimeEventsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DTimeEventsCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self) -> VehicleGraphics2DTimeEventsElement
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~VehicleGraphics2DTimeEventsElement`


.. py:method:: item(self, index: int) -> VehicleGraphics2DTimeEventsElement
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehicleGraphics2DTimeEventsElement`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


