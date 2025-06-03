ThrusterSetCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection

   Thruster Set Collection.

.. py:currentmodule:: ThrusterSetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.item`
              - Iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.add`
              - Add a new thruster.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.remove`
              - Remove a specified thruster.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.remove_all`
              - Remove all thrusters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.cut`
              - Copy a thruster to the clipboard and removes the thruster from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.paste`
              - Pastes a thruster from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.insert_copy`
              - Copy a thruster and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.get_item_by_index`
              - Retrieve a thruster from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.get_item_by_name`
              - Retrieve a thruster from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection._new_enum`
              - A property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.count`
              - Get the number of thrusters in the set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ThrusterSetCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection._new_enum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.count
    :type: int

    Get the number of thrusters in the set.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> Thruster
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.item

    Iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~Thruster`



.. py:method:: add(self, thruster_name: str) -> Thruster
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.add

    Add a new thruster.

    :Parameters:

        **thruster_name** : :obj:`~str`


    :Returns:

        :obj:`~Thruster`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.remove

    Remove a specified thruster.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.remove_all

    Remove all thrusters.

    :Returns:

        :obj:`~None`

.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.cut

    Copy a thruster to the clipboard and removes the thruster from the list.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> Thruster
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.paste

    Pastes a thruster from the clipboard into the list.

    :Returns:

        :obj:`~Thruster`

.. py:method:: insert_copy(self, thruster: Thruster) -> Thruster
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.insert_copy

    Copy a thruster and inserts the copy into the list.

    :Parameters:

        **thruster** : :obj:`~Thruster`


    :Returns:

        :obj:`~Thruster`

.. py:method:: get_item_by_index(self, index: int) -> Thruster
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.get_item_by_index

    Retrieve a thruster from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Thruster`

.. py:method:: get_item_by_name(self, name: str) -> Thruster
    :canonical: ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection.get_item_by_name

    Retrieve a thruster from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~Thruster`

