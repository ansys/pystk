IDataProviderResultSubSectionCollection
=======================================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResultSubSectionCollection

   object
   
   Represents a collection of sub-section data elements.

.. py:currentmodule:: IDataProviderResultSubSectionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultSubSectionCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultSubSectionCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultSubSectionCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultSubSectionCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultSubSectionCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultSubSectionCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IDataProviderResultSubSection
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultSubSectionCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDataProviderResultSubSection`


