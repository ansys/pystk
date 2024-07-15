PathPointCollection
===================

.. py:class:: ansys.stk.core.graphics.PathPointCollection

   Bases: 

   A collection of path points.

.. py:currentmodule:: PathPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPointCollection.item`
              - Return a path point at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPointCollection.count`
              - A total number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.PathPointCollection._NewEnum`
              - Return an enumerator that iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PathPointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.PathPointCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.PathPointCollection._NewEnum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPointCollection.item

    Return a path point at the specified position in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~PathPoint`


