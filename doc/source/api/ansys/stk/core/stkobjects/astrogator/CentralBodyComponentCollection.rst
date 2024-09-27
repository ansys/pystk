CentralBodyComponentCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection

   Central Body Collection.

.. py:currentmodule:: CentralBodyComponentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.add`
              - Add a central body to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove`
              - Remove a central body from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove_all`
              - Remove all central bodies from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_index`
              - Retrieve a central body from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_name`
              - Retrieve a central body from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection._NewEnum`
              - Iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CentralBodyComponentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection._NewEnum
    :type: EnumeratorProxy

    Iterates through the collection.


Method detail
-------------

.. py:method:: item(self, indexOrCbName: typing.Any) -> CentralBodyComponent
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrCbName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~CentralBodyComponent`



.. py:method:: add(self, cbName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.add

    Add a central body to the collection.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove

    Remove a central body from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove_all

    Remove all central bodies from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_index(self, index: int) -> CentralBodyComponent
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_index

    Retrieve a central body from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~CentralBodyComponent`

.. py:method:: get_item_by_name(self, cbName: str) -> CentralBodyComponent
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_name

    Retrieve a central body from the collection by name.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~CentralBodyComponent`

