DataProviderResultDataSetCollection
===================================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection

   Represents a collection of datasets in the interval returned by the data providers.

.. py:currentmodule:: DataProviderResultDataSetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_data_set_by_name`
              - Return the element, given the name.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_row`
              - Return the specified row.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_array`
              - Return the entire dataset collection in row format.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_numpy_array`
              - Return a row formatted dataset collection as a numpy array. This function requires ``numpy``.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_pandas_dataframe`
              - Return a row formatted dataset collection as a pandas DataFrame. This function requires ``pandas``.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.count`
              - Return a number of elements in collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.row_count`
              - Return the number of rows in the dataset collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.element_names`
              - Return the element names.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultDataSetCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.count
    :type: int

    Return a number of elements in collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: row_count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.row_count
    :type: int

    Return the number of rows in the dataset collection.

.. py:property:: element_names
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.element_names
    :type: list

    Return the element names.


Method detail
-------------


.. py:method:: item(self, index: int) -> DataProviderResultDataSet
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~DataProviderResultDataSet`


.. py:method:: get_data_set_by_name(self, data_set_name: str) -> DataProviderResultDataSet
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_data_set_by_name

    Return the element, given the name.

    :Parameters:

    **data_set_name** : :obj:`~str`

    :Returns:

        :obj:`~DataProviderResultDataSet`


.. py:method:: get_row(self, index: int) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_row

    Return the specified row.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_array

    Return the entire dataset collection in row format.

    :Returns:

        :obj:`~list`

.. py:method:: to_numpy_array(self) -> ndarray
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_numpy_array

    Return a row formatted dataset collection as a numpy array. This function requires ``numpy``.

    :Returns:

        :obj:`~ndarray`

.. py:method:: to_pandas_dataframe(self, index_element_name: str, data_provider_elements: IAgDataPrvElements) -> DataFrame:
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_pandas_dataframe

    Return a row formatted dataset collection as a pandas DataFrame. This function requires ``pandas``.

    This function optionally maps data provider element types to pandas DataFrame column dtypes and optionally sets the
    column to be used as the DataFrame index.

    :Parameters:

    **index_element_name** : :obj:`~str`
    **data_provider_elements** : :obj:`~DataProviderElements`

    :Returns:

        :obj:`~DataFrame`

