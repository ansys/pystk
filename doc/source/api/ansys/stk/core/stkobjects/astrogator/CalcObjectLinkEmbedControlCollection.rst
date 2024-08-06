CalcObjectLinkEmbedControlCollection
====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection

   The Calculation Object link/embed component folder.

.. py:currentmodule:: CalcObjectLinkEmbedControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.add`
              - Add a link/embed calc object to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.item`
              - Return a link/embed calc object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.remove`
              - Remove a link/embed calc object from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.cut`
              - Copy a link/embed calc object to the clipboard and removes the calc object from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.paste`
              - Pastes a link/embed calc object from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.insert_copy`
              - Copy a link/embed calc object and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.get_item_by_index`
              - Retrieve a link/embed calc object found by the index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.get_item_by_name`
              - Retrieve a link/embed calc object found by the name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CalcObjectLinkEmbedControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: add(self, name: str, refType: COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.add

    Add a link/embed calc object to the collection.

    :Parameters:

    **name** : :obj:`~str`
    **refType** : :obj:`~COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: item(self, indexOrName: typing.Any) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.item

    Return a link/embed calc object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.remove

    Remove a link/embed calc object from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.cut

    Copy a link/embed calc object to the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.paste

    Pastes a link/embed calc object from the clipboard into the list.

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: insert_copy(self, calcObj: IComponentLinkEmbedControl) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.insert_copy

    Copy a link/embed calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~IComponentLinkEmbedControl`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: get_item_by_index(self, index: int) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.get_item_by_index

    Retrieve a link/embed calc object found by the index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: get_item_by_name(self, name: str) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection.get_item_by_name

    Retrieve a link/embed calc object found by the name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

