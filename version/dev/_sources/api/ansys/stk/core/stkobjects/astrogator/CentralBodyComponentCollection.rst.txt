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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.add`
              - Add a central body to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_index`
              - Retrieve a central body from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_name`
              - Retrieve a central body from the collection by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove`
              - Remove a central body from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove_all`
              - Remove all central bodies from the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection._new_enum`
              - Iterates through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CentralBodyComponentCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection._new_enum
    :type: EnumeratorProxy

    Iterates through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: add(self, cb_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.add

    Add a central body to the collection.

    :Parameters:

        **cb_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: get_item_by_index(self, index: int) -> CentralBodyComponent
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_index

    Retrieve a central body from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~CentralBodyComponent`

.. py:method:: get_item_by_name(self, cb_name: str) -> CentralBodyComponent
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.get_item_by_name

    Retrieve a central body from the collection by name.

    :Parameters:

        **cb_name** : :obj:`~str`


    :Returns:

        :obj:`~CentralBodyComponent`

.. py:method:: item(self, index_or_cb_name: typing.Any) -> CentralBodyComponent
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index_or_cb_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~CentralBodyComponent`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove

    Remove a central body from the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection.remove_all

    Remove all central bodies from the collection.

    :Returns:

        :obj:`~None`


