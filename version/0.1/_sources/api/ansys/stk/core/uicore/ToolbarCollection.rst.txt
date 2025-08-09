ToolbarCollection
=================

.. py:class:: ansys.stk.core.uicore.ToolbarCollection

   Provide methods and properties to manage the toolbars.

.. py:currentmodule:: ToolbarCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.ToolbarCollection.item`
              - Retrieve a toolbar object.
            * - :py:attr:`~ansys.stk.core.uicore.ToolbarCollection.get_toolbar_by_id`
              - Return a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object.
            * - :py:attr:`~ansys.stk.core.uicore.ToolbarCollection.get_item_by_index`
              - Retrieve a toolbar object based on the index in the collection.
            * - :py:attr:`~ansys.stk.core.uicore.ToolbarCollection.get_item_by_name`
              - Retrieve a toolbar object based on the name of the Toolbar in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.ToolbarCollection.count`
              - Return a total number of toolbars in the collection.
            * - :py:attr:`~ansys.stk.core.uicore.ToolbarCollection._new_enum`
              - Enumerates the toolbars in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uicore import ToolbarCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uicore.ToolbarCollection.count
    :type: int

    Return a total number of toolbars in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.uicore.ToolbarCollection._new_enum
    :type: EnumeratorProxy

    Enumerates the toolbars in the collection.


Method detail
-------------

.. py:method:: item(self, index_or_caption: typing.Any) -> Toolbar
    :canonical: ansys.stk.core.uicore.ToolbarCollection.item

    Retrieve a toolbar object.

    :Parameters:

        **index_or_caption** : :obj:`~typing.Any`


    :Returns:

        :obj:`~Toolbar`



.. py:method:: get_toolbar_by_id(self, id: int) -> Toolbar
    :canonical: ansys.stk.core.uicore.ToolbarCollection.get_toolbar_by_id

    Return a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object.

    :Parameters:

        **id** : :obj:`~int`


    :Returns:

        :obj:`~Toolbar`

.. py:method:: get_item_by_index(self, index: int) -> Toolbar
    :canonical: ansys.stk.core.uicore.ToolbarCollection.get_item_by_index

    Retrieve a toolbar object based on the index in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Toolbar`

.. py:method:: get_item_by_name(self, name: str) -> Toolbar
    :canonical: ansys.stk.core.uicore.ToolbarCollection.get_item_by_name

    Retrieve a toolbar object based on the name of the Toolbar in the collection.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~Toolbar`

