IVehicleGraphics3DBPlanePointCollection
=======================================

.. py:class:: IVehicleGraphics3DBPlanePointCollection

   object
   
   A list of available additional points.

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
            * - :py:meth:`~point_color`
            * - :py:meth:`~first_point_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBPlanePointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlanePointCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlanePointCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: point_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlanePointCollection.point_color
    :type: agcolor.Color

    Whether to display the first point in the same color as the other points.

.. py:property:: first_point_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlanePointCollection.first_point_color
    :type: agcolor.Color

    Gets or sets the specified color of the first point, if different from the others.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IVehicleGraphics3DBPlanePoint"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVehicleGraphics3DBPlanePoint"`


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

.. py:method:: add(self) -> "IVehicleGraphics3DBPlanePoint"

    Add a new element to the collection.

    :Returns:

        :obj:`~"IVehicleGraphics3DBPlanePoint"`





