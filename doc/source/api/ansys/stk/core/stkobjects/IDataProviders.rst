IDataProviders
==============

.. py:class:: IDataProviders

   object
   
   Represents a collection of data providers.

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
            * - :py:meth:`~contains`
              - Determine whether the collection contains a specific data provider.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a data provider from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a data provider from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviders


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviders.count
    :type: int

    Returns an element in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IDataProviders._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, indexOrName: typing.Any) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.IDataProviders.item

    Given an index, returns an element in the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IDataProviderInfo`


.. py:method:: contains(self, dataProviderName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IDataProviders.contains

    Determine whether the collection contains a specific data provider.

    :Parameters:

    **dataProviderName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: get_item_by_index(self, index: int) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.IDataProviders.get_item_by_index

    Retrieve a data provider from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_item_by_name(self, name: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.IDataProviders.get_item_by_name

    Retrieve a data provider from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderInfo`

