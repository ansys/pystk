IDataProviderCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderCollection

   object
   
   Represents a collection of data providers.

.. py:currentmodule:: IDataProviderCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.get_schema`
              - Return a string containing the XML representation of the available data providers.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.item`
              - Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_info_from_path`
              - Return the data provider information specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_time_varying_from_path`
              - Return the time variable data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_interval_from_path`
              - Return the interval data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_fixed_from_path`
              - Return the fixed data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.get_item_by_index`
              - Retrieve a data provider from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.get_item_by_name`
              - Retrieve a data provider from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.count
    :type: int

    Returns number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection._NewEnum
    :type: EnumeratorProxy

    Returns the enumerator for the collection.


Method detail
-------------

.. py:method:: get_schema(self) -> str
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.get_schema

    Return a string containing the XML representation of the available data providers.

    :Returns:

        :obj:`~str`

.. py:method:: item(self, indexOrName: typing.Any) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.item

    Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IDataProviderInfo`



.. py:method:: get_data_provider_info_from_path(self, dataProviderPath: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_info_from_path

    Return the data provider information specified by the data provider path.

    :Parameters:

    **dataProviderPath** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_data_provider_time_varying_from_path(self, dataProviderPath: str) -> IDataProviderTimeVarying
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_time_varying_from_path

    Return the time variable data provider specified by the data provider path.

    :Parameters:

    **dataProviderPath** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderTimeVarying`

.. py:method:: get_data_provider_interval_from_path(self, dataProviderPath: str) -> IDataProviderInterval
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_interval_from_path

    Return the interval data provider specified by the data provider path.

    :Parameters:

    **dataProviderPath** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderInterval`

.. py:method:: get_data_provider_fixed_from_path(self, dataProviderPath: str) -> IDataProviderFixed
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.get_data_provider_fixed_from_path

    Return the fixed data provider specified by the data provider path.

    :Parameters:

    **dataProviderPath** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderFixed`

.. py:method:: get_item_by_index(self, index: int) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.get_item_by_index

    Retrieve a data provider from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_item_by_name(self, name: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.IDataProviderCollection.get_item_by_name

    Retrieve a data provider from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderInfo`

