IDataProviderResultIntervalCollection
=====================================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResultIntervalCollection

   object
   
   Represents a collection of intervals.

.. py:currentmodule:: IDataProviderResultIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultIntervalCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultIntervalCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultIntervalCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultIntervalCollection.count
    :type: int

    Returns a number of elements in collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultIntervalCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IDataProviderResultInterval
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultIntervalCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDataProviderResultInterval`


