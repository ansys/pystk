VehicleGraphics2DTimeComponentsCollection
=========================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection

   A collection of time components used to configure the object appearance in 2D and 3D views.

.. py:currentmodule:: VehicleGraphics2DTimeComponentsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.add`
              - Add a new element to the collection using the specified fully qualified component's path (i.e. ``Scenario/Scenario1 AnalysisInterval EventInterval``). Only intervals, interval lists or interval collections are allowed.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DTimeComponentsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics2DTimeComponentsElement
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IVehicleGraphics2DTimeComponentsElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, qualified_path: str) -> IVehicleGraphics2DTimeComponentsElement
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection.add

    Add a new element to the collection using the specified fully qualified component's path (i.e. ``Scenario/Scenario1 AnalysisInterval EventInterval``). Only intervals, interval lists or interval collections are allowed.

    :Parameters:

        **qualified_path** : :obj:`~str`


    :Returns:

        :obj:`~IVehicleGraphics2DTimeComponentsElement`

