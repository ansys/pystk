VehicleGroundEllipsesCollection
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection

   List of Ground Ellipses.

.. py:currentmodule:: VehicleGroundEllipsesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.remove_ellipse_set`
              - Remove an element from the collection using the Ellipse Set name.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.get_ellipse_set`
              - Get an element from the collection using the Ellipse Set name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGroundEllipsesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGroundEllipseElement
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleGroundEllipseElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, name: str) -> VehicleGroundEllipseElement
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.add

    Add a new element to the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~VehicleGroundEllipseElement`

.. py:method:: remove_ellipse_set(self, ellipse_set_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.remove_ellipse_set

    Remove an element from the collection using the Ellipse Set name.

    :Parameters:

    **ellipse_set_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_ellipse_set(self, ellipse_set_name: str) -> VehicleGroundEllipseElement
    :canonical: ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection.get_ellipse_set

    Get an element from the collection using the Ellipse Set name.

    :Parameters:

    **ellipse_set_name** : :obj:`~str`

    :Returns:

        :obj:`~VehicleGroundEllipseElement`

