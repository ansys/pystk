CentralBodyCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection

   Bases: 

   Central Body Collection.

.. py:currentmodule:: CentralBodyCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.add`
              - Add a central body to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.remove`
              - Remove a central body from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.remove_all`
              - Remove all central bodies from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.get_item_by_index`
              - Retrieve a central body from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.get_item_by_name`
              - Retrieve a central body from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection._NewEnum`
              - Iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CentralBodyCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection._NewEnum
    :type: EnumeratorProxy

    Iterates through the collection.


Method detail
-------------

.. py:method:: item(self, indexOrCbName: typing.Any) -> AstrogatorCentralBody
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrCbName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~AstrogatorCentralBody`



.. py:method:: add(self, cbName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.add

    Add a central body to the collection.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.remove

    Remove a central body from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.remove_all

    Remove all central bodies from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_index(self, index: int) -> AstrogatorCentralBody
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.get_item_by_index

    Retrieve a central body from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AstrogatorCentralBody`

.. py:method:: get_item_by_name(self, cbName: str) -> AstrogatorCentralBody
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyCollection.get_item_by_name

    Retrieve a central body from the collection by name.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~AstrogatorCentralBody`

