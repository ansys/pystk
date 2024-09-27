CelestialBodyCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.CelestialBodyCollection

   Represents a collection of stars.

.. py:currentmodule:: CelestialBodyCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyCollection.recycle`
              - Controls whether to reuse the same celestial info object when accessing the elements of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CelestialBodyCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CelestialBodyCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.CelestialBodyCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: recycle
    :canonical: ansys.stk.core.stkobjects.CelestialBodyCollection.recycle
    :type: bool

    Controls whether to reuse the same celestial info object when accessing the elements of the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> CelestialBodyInfo
    :canonical: ansys.stk.core.stkobjects.CelestialBodyCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~CelestialBodyInfo`




