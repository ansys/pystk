IUiToolbarCollection
====================

.. py:class:: ansys.stk.core.uicore.IUiToolbarCollection

   object
   
   Provide methods and properties to obtain a window's toolbars.

.. py:currentmodule:: IUiToolbarCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.IUiToolbarCollection.item`
              - Retrieve a toolbar object.
            * - :py:attr:`~ansys.stk.core.uicore.IUiToolbarCollection.get_toolbar_by_id`
              - Return a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object.
            * - :py:attr:`~ansys.stk.core.uicore.IUiToolbarCollection.get_item_by_index`
              - Retrieve a toolbar object based on the index in the collection.
            * - :py:attr:`~ansys.stk.core.uicore.IUiToolbarCollection.get_item_by_name`
              - Retrieve a toolbar object based on the name of the Toolbar in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.IUiToolbarCollection.count`
              - Returns a total number of toolbars in the collection.
            * - :py:attr:`~ansys.stk.core.uicore.IUiToolbarCollection._NewEnum`
              - Enumerates the toolbars in the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uicore import IUiToolbarCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uicore.IUiToolbarCollection.count
    :type: int

    Returns a total number of toolbars in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.uicore.IUiToolbarCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the toolbars in the collection.


Method detail
-------------

.. py:method:: item(self, indexOrCaption: typing.Any) -> IUiToolbar
    :canonical: ansys.stk.core.uicore.IUiToolbarCollection.item

    Retrieve a toolbar object.

    :Parameters:

    **indexOrCaption** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IUiToolbar`



.. py:method:: get_toolbar_by_id(self, id: int) -> IUiToolbar
    :canonical: ansys.stk.core.uicore.IUiToolbarCollection.get_toolbar_by_id

    Return a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object.

    :Parameters:

    **id** : :obj:`~int`

    :Returns:

        :obj:`~IUiToolbar`

.. py:method:: get_item_by_index(self, index: int) -> IUiToolbar
    :canonical: ansys.stk.core.uicore.IUiToolbarCollection.get_item_by_index

    Retrieve a toolbar object based on the index in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IUiToolbar`

.. py:method:: get_item_by_name(self, name: str) -> IUiToolbar
    :canonical: ansys.stk.core.uicore.IUiToolbarCollection.get_item_by_name

    Retrieve a toolbar object based on the name of the Toolbar in the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUiToolbar`

