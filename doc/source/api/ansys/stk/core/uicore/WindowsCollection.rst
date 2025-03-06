WindowsCollection
=================

.. py:class:: ansys.stk.core.uicore.WindowsCollection

   Provide methods and properties to manage the windows.

.. py:currentmodule:: WindowsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.WindowsCollection.item`
              - Retrieve a window object.
            * - :py:attr:`~ansys.stk.core.uicore.WindowsCollection.arrange`
              - Arranges the application windows using the specified style.
            * - :py:attr:`~ansys.stk.core.uicore.WindowsCollection.add`
              - Create a new window. The bstrPluginID is a COM ProgID associated with an STK plugin.
            * - :py:attr:`~ansys.stk.core.uicore.WindowsCollection.get_item_by_index`
              - Retrieve a window object by index in collection.
            * - :py:attr:`~ansys.stk.core.uicore.WindowsCollection.get_item_by_name`
              - Retrieve a window object by name of window object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.WindowsCollection.count`
              - Return a total number of window objects in the collection.
            * - :py:attr:`~ansys.stk.core.uicore.WindowsCollection._new_enum`
              - Enumerates the windows in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uicore import WindowsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uicore.WindowsCollection.count
    :type: int

    Return a total number of window objects in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.uicore.WindowsCollection._new_enum
    :type: EnumeratorProxy

    Enumerates the windows in the collection.


Method detail
-------------

.. py:method:: item(self, index_or_caption: typing.Any) -> Window
    :canonical: ansys.stk.core.uicore.WindowsCollection.item

    Retrieve a window object.

    :Parameters:

    **index_or_caption** : :obj:`~typing.Any`

    :Returns:

        :obj:`~Window`


.. py:method:: arrange(self, arrange_style: WindowArrangeStyle) -> None
    :canonical: ansys.stk.core.uicore.WindowsCollection.arrange

    Arranges the application windows using the specified style.

    :Parameters:

    **arrange_style** : :obj:`~WindowArrangeStyle`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, plugin_id: str, init_data: typing.Any) -> Window
    :canonical: ansys.stk.core.uicore.WindowsCollection.add

    Create a new window. The bstrPluginID is a COM ProgID associated with an STK plugin.

    :Parameters:

    **plugin_id** : :obj:`~str`
    **init_data** : :obj:`~typing.Any`

    :Returns:

        :obj:`~Window`


.. py:method:: get_item_by_index(self, index: int) -> Window
    :canonical: ansys.stk.core.uicore.WindowsCollection.get_item_by_index

    Retrieve a window object by index in collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Window`

.. py:method:: get_item_by_name(self, name: str) -> Window
    :canonical: ansys.stk.core.uicore.WindowsCollection.get_item_by_name

    Retrieve a window object by name of window object.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~Window`

