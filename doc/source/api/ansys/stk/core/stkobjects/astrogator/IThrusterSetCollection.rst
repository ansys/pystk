IThrusterSetCollection
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection

   object
   
   The list of thrusters in a thruster set.

.. py:currentmodule:: IThrusterSetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.item`
              - Iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.add`
              - Add a new thruster.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.remove`
              - Remove a specified thruster.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.remove_all`
              - Remove all thrusters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.cut`
              - Copy a thruster to the clipboard and removes the thruster from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.paste`
              - Pastes a thruster from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.insert_copy`
              - Copy a thruster and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.get_item_by_index`
              - Retrieve a thruster from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.get_item_by_name`
              - Retrieve a thruster from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection._NewEnum`
              - A property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.count`
              - Get the number of thrusters in the set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IThrusterSetCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection._NewEnum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.count
    :type: int

    Get the number of thrusters in the set.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IThruster
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.item

    Iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IThruster`



.. py:method:: add(self, thrusterName: str) -> IThruster
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.add

    Add a new thruster.

    :Parameters:

    **thrusterName** : :obj:`~str`

    :Returns:

        :obj:`~IThruster`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.remove

    Remove a specified thruster.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.remove_all

    Remove all thrusters.

    :Returns:

        :obj:`~None`

.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.cut

    Copy a thruster to the clipboard and removes the thruster from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IThruster
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.paste

    Pastes a thruster from the clipboard into the list.

    :Returns:

        :obj:`~IThruster`

.. py:method:: insert_copy(self, thruster: IThruster) -> IThruster
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.insert_copy

    Copy a thruster and inserts the copy into the list.

    :Parameters:

    **thruster** : :obj:`~IThruster`

    :Returns:

        :obj:`~IThruster`

.. py:method:: get_item_by_index(self, index: int) -> IThruster
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.get_item_by_index

    Retrieve a thruster from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IThruster`

.. py:method:: get_item_by_name(self, name: str) -> IThruster
    :canonical: ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection.get_item_by_name

    Retrieve a thruster from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IThruster`

