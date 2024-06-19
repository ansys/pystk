IVehicleGraphics2DGroundEllipsesCollection
==========================================

.. py:class:: IVehicleGraphics2DGroundEllipsesCollection

   object
   
   Collection of ground ellipse 2D graphics properties.

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

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DGroundEllipsesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DGroundEllipsesCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DGroundEllipsesCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics2DGroundEllipsesElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DGroundEllipsesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics2DGroundEllipsesElement`


