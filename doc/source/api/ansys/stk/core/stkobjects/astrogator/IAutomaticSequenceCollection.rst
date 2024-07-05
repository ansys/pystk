IAutomaticSequenceCollection
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection

   object
   
   Properties for the Automatic Sequence Browser.

.. py:currentmodule:: IAutomaticSequenceCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.item`
              - Return the given automatic sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.add`
              - Create a new sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.remove`
              - Remove a sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.get_item_by_index`
              - Retrieve the given automatic sequence found by the index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.get_item_by_name`
              - Retrieve the given automatic sequence found by the name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.count`
              - Get the size of the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAutomaticSequenceCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.count
    :type: int

    Get the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IAutomaticSequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.item

    Return the given automatic sequence.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IAutomaticSequence`

.. py:method:: add(self, name: str) -> IAutomaticSequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.add

    Create a new sequence.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAutomaticSequence`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.remove

    Remove a sequence.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: get_item_by_index(self, index: int) -> IAutomaticSequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.get_item_by_index

    Retrieve the given automatic sequence found by the index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAutomaticSequence`

.. py:method:: get_item_by_name(self, name: str) -> IAutomaticSequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection.get_item_by_name

    Retrieve the given automatic sequence found by the name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAutomaticSequence`

