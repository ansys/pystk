ScatteringPointCollection
=========================

.. py:class:: ansys.stk.core.stkobjects.ScatteringPointCollection

   Class defining a collection of scattering points.

.. py:currentmodule:: ScatteringPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointCollection._NewEnum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScatteringPointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ScatteringPointCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ScatteringPointCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ScatteringPointCollectionElement
    :canonical: ansys.stk.core.stkobjects.ScatteringPointCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScatteringPointCollectionElement`


