DataProviderCollection
======================

.. py:class:: ansys.stk.core.stkobjects.DataProviderCollection

   Collection of data providers attached to the current STK object.

.. py:currentmodule:: DataProviderCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_schema`
              - Return a string containing the XML representation of the available data providers.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.item`
              - Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_information_from_path`
              - Return the data provider information specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_time_varying_from_path`
              - Return the time variable data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_interval_from_path`
              - Return the interval data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_fixed_from_path`
              - Return the fixed data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_index`
              - Retrieve a data provider from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_name`
              - Retrieve a data provider from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.count`
              - Returns number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection._new_enum`
              - Returns the enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.count
    :type: int

    Returns number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection._new_enum
    :type: EnumeratorProxy

    Returns the enumerator for the collection.


Method detail
-------------

.. py:method:: get_schema(self) -> str
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_schema

    Return a string containing the XML representation of the available data providers.

    :Returns:

        :obj:`~str`

.. py:method:: item(self, index_or_name: typing.Any) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.item

    Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IDataProviderInfo`



.. py:method:: get_data_provider_information_from_path(self, data_provider_path: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_information_from_path

    Return the data provider information specified by the data provider path.

    :Parameters:

    **data_provider_path** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_data_provider_time_varying_from_path(self, data_provider_path: str) -> DataProviderTimeVarying
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_time_varying_from_path

    Return the time variable data provider specified by the data provider path.

    :Parameters:

    **data_provider_path** : :obj:`~str`

    :Returns:

        :obj:`~DataProviderTimeVarying`

.. py:method:: get_data_provider_interval_from_path(self, data_provider_path: str) -> DataProviderInterval
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_interval_from_path

    Return the interval data provider specified by the data provider path.

    :Parameters:

    **data_provider_path** : :obj:`~str`

    :Returns:

        :obj:`~DataProviderInterval`

.. py:method:: get_data_provider_fixed_from_path(self, data_provider_path: str) -> DataProviderFixed
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_fixed_from_path

    Return the fixed data provider specified by the data provider path.

    :Parameters:

    **data_provider_path** : :obj:`~str`

    :Returns:

        :obj:`~DataProviderFixed`

.. py:method:: get_item_by_index(self, index: int) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_index

    Retrieve a data provider from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_item_by_name(self, name: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_name

    Retrieve a data provider from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderInfo`

