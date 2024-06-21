ICalcObjectLinkEmbedControlCollection
=====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection

   object
   
   Collection of link/embed calculation objects.

.. py:currentmodule:: ICalcObjectLinkEmbedControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.add`
              - Add a link/embed calc object to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.item`
              - Return a link/embed calc object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.remove`
              - Remove a link/embed calc object from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.cut`
              - Copy a link/embed calc object to the clipboard and removes the calc object from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.paste`
              - Pastes a link/embed calc object from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.insert_copy`
              - Copy a link/embed calc object and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.get_item_by_index`
              - Retrieve a link/embed calc object found by the index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.get_item_by_name`
              - Retrieve a link/embed calc object found by the name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ICalcObjectLinkEmbedControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: add(self, name: str, refType: COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.add

    Add a link/embed calc object to the collection.

    :Parameters:

    **name** : :obj:`~str`
    **refType** : :obj:`~COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: item(self, indexOrName: typing.Any) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.item

    Return a link/embed calc object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.remove

    Remove a link/embed calc object from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.cut

    Copy a link/embed calc object to the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.paste

    Pastes a link/embed calc object from the clipboard into the list.

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: insert_copy(self, calcObj: IComponentLinkEmbedControl) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.insert_copy

    Copy a link/embed calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~IComponentLinkEmbedControl`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: get_item_by_index(self, index: int) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.get_item_by_index

    Retrieve a link/embed calc object found by the index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: get_item_by_name(self, name: str) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection.get_item_by_name

    Retrieve a link/embed calc object found by the name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

