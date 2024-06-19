ICelestialBodyCollection
========================

.. py:class:: ICelestialBodyCollection

   object
   
   Represents a collection of celestial bodies.

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
            * - :py:meth:`~recycle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICelestialBodyCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: recycle
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyCollection.recycle
    :type: bool

    Controls whether to reuse the same celestial info object when accessing the elements of the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ICelestialBodyInfo
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICelestialBodyInfo`




