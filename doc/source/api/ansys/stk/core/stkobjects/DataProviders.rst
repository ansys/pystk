DataProviders
=============

.. py:class:: ansys.stk.core.stkobjects.DataProviders

   Class defining data providers.

.. py:currentmodule:: DataProviders

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviders.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviders.contains`
              - Determine whether the collection contains a specific data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviders.get_item_by_index`
              - Retrieve a data provider from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviders.get_item_by_name`
              - Retrieve a data provider from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviders.count`
              - Return an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviders._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviders


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviders.count
    :type: int

    Return an element in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviders._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index_or_name: typing.Any) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviders.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IDataProviderInfo`


.. py:method:: contains(self, data_provider_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.DataProviders.contains

    Determine whether the collection contains a specific data provider.

    :Parameters:

        **data_provider_name** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: get_item_by_index(self, index: int) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviders.get_item_by_index

    Retrieve a data provider from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_item_by_name(self, name: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviders.get_item_by_name

    Retrieve a data provider from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IDataProviderInfo`

