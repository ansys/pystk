IScatteringPointCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.IScatteringPointCollection

   object
   
   Represents a collection of scattering points.

.. py:currentmodule:: IScatteringPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointCollection._NewEnum`
              - Returns an enumerator for the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScatteringPointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IScatteringPointCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IScatteringPointCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IScatteringPointCollectionElement
    :canonical: ansys.stk.core.stkobjects.IScatteringPointCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScatteringPointCollectionElement`


