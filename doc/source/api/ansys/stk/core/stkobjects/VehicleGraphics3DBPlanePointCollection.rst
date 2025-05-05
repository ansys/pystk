VehicleGraphics3DBPlanePointCollection
======================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection

   VehicleGraphics3DBPlanePointCollection Class.

.. py:currentmodule:: VehicleGraphics3DBPlanePointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.add`
              - Add a new element to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.point_color`
              - Whether to display the first point in the same color as the other points.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.first_point_color`
              - Get or set the specified color of the first point, if different from the others.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DBPlanePointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: point_color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.point_color
    :type: agcolor.Color

    Whether to display the first point in the same color as the other points.

.. py:property:: first_point_color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.first_point_color
    :type: agcolor.Color

    Get or set the specified color of the first point, if different from the others.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGraphics3DBPlanePoint
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleGraphics3DBPlanePoint`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self) -> VehicleGraphics3DBPlanePoint
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~VehicleGraphics3DBPlanePoint`





