IPathPointCollection
====================

.. py:class:: IPathPointCollection

   object
   
   A collection of path points.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return a path point at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPathPointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IPathPointCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IPathPointCollection._NewEnum
    :type: EnumeratorProxy




Method detail
-------------


.. py:method:: item(self, index: int) -> IPathPoint
    :canonical: ansys.stk.core.graphics.IPathPointCollection.item

    Return a path point at the specified position in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IPathPoint`


