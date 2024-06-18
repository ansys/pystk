IDataProviderResultDataSetCollection
====================================

.. py:class:: IDataProviderResultDataSetCollection

   object
   
   Represents a collection of dataset elements.

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
            * - :py:meth:`~get_data_set_by_name`
              - Return the element, given the name.
            * - :py:meth:`~get_row`
              - Return the specified row.
            * - :py:meth:`~to_array`
              - Return the entire dataset collection in row format.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~row_count`
            * - :py:meth:`~element_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultDataSetCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSetCollection.count
    :type: int

    Returns a number of elements in collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSetCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.

.. py:property:: row_count
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSetCollection.row_count
    :type: int

    Returns the number of rows in the dataset collection.

.. py:property:: element_names
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSetCollection.element_names
    :type: list

    Returns the element names.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IDataProviderResultDataSet"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IDataProviderResultDataSet"`


.. py:method:: get_data_set_by_name(self, dataSetName:str) -> "IDataProviderResultDataSet"

    Return the element, given the name.

    :Parameters:

    **dataSetName** : :obj:`~str`

    :Returns:

        :obj:`~"IDataProviderResultDataSet"`


.. py:method:: get_row(self, index:int) -> list

    Return the specified row.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: to_array(self) -> list

    Return the entire dataset collection in row format.

    :Returns:

        :obj:`~list`


