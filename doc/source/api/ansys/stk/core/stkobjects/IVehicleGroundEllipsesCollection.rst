IVehicleGroundEllipsesCollection
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection

   object
   
   Ground Ellipses.

.. py:currentmodule:: IVehicleGroundEllipsesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.remove_ellipse_set`
              - Remove an element from the collection using the Ellipse Set name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.get_ellipse_set`
              - Get an element from the collection using the Ellipse Set name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGroundEllipsesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGroundEllipseElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGroundEllipseElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, name: str) -> IVehicleGroundEllipseElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.add

    Add a new element to the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleGroundEllipseElement`

.. py:method:: remove_ellipse_set(self, ellipseSetName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.remove_ellipse_set

    Remove an element from the collection using the Ellipse Set name.

    :Parameters:

    **ellipseSetName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_ellipse_set(self, ellipseSetName: str) -> IVehicleGroundEllipseElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGroundEllipsesCollection.get_ellipse_set

    Get an element from the collection using the Ellipse Set name.

    :Parameters:

    **ellipseSetName** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleGroundEllipseElement`

