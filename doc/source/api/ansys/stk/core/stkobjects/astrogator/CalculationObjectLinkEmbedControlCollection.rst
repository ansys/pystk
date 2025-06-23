CalculationObjectLinkEmbedControlCollection
===========================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection

   The Calculation Object link/embed component folder.

.. py:currentmodule:: CalculationObjectLinkEmbedControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.add`
              - Add a link/embed calc object to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.item`
              - Return a link/embed calc object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.remove`
              - Remove a link/embed calc object from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.cut`
              - Copy a link/embed calc object to the clipboard and removes the calc object from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.paste`
              - Pastes a link/embed calc object from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.insert_copy`
              - Copy a link/embed calc object and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.get_item_by_index`
              - Retrieve a link/embed calc object found by the index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.get_item_by_name`
              - Retrieve a link/embed calc object found by the name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CalculationObjectLinkEmbedControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: add(self, name: str, ref_type: ComponentLinkEmbedControlReferenceType) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.add

    Add a link/embed calc object to the collection.

    :Parameters:

        **name** : :obj:`~str`

        **ref_type** : :obj:`~ComponentLinkEmbedControlReferenceType`


    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: item(self, index_or_name: typing.Any) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.item

    Return a link/embed calc object.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.remove

    Remove a link/embed calc object from the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`



.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.cut

    Copy a link/embed calc object to the clipboard and removes the calc object from the list.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.paste

    Pastes a link/embed calc object from the clipboard into the list.

    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: insert_copy(self, calc_obj: IComponentLinkEmbedControl) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.insert_copy

    Copy a link/embed calc object and inserts the copy into the list.

    :Parameters:

        **calc_obj** : :obj:`~IComponentLinkEmbedControl`


    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: get_item_by_index(self, index: int) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.get_item_by_index

    Retrieve a link/embed calc object found by the index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IComponentLinkEmbedControl`

.. py:method:: get_item_by_name(self, name: str) -> IComponentLinkEmbedControl
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection.get_item_by_name

    Retrieve a link/embed calc object found by the name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IComponentLinkEmbedControl`

