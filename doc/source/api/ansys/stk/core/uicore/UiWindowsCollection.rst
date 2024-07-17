UiWindowsCollection
===================

.. py:class:: ansys.stk.core.uicore.UiWindowsCollection

   Bases: 

   Provide methods and properties to manage the windows.

.. py:currentmodule:: UiWindowsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.UiWindowsCollection.item`
              - Retrieve a window object.
            * - :py:attr:`~ansys.stk.core.uicore.UiWindowsCollection.arrange`
              - Arranges the application windows using the specified style.
            * - :py:attr:`~ansys.stk.core.uicore.UiWindowsCollection.add`
              - Create a new window. The bstrPluginID is a COM ProgID associated with an STK plugin.
            * - :py:attr:`~ansys.stk.core.uicore.UiWindowsCollection.get_item_by_index`
              - Retrieve a window object by index in collection.
            * - :py:attr:`~ansys.stk.core.uicore.UiWindowsCollection.get_item_by_name`
              - Retrieve a window object by name of window object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.UiWindowsCollection.count`
              - Returns a total number of window objects in the collection.
            * - :py:attr:`~ansys.stk.core.uicore.UiWindowsCollection._NewEnum`
              - Enumerates the windows in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uicore import UiWindowsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uicore.UiWindowsCollection.count
    :type: int

    Returns a total number of window objects in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.uicore.UiWindowsCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the windows in the collection.


Method detail
-------------

.. py:method:: item(self, indexOrCaption: typing.Any) -> UiWindow
    :canonical: ansys.stk.core.uicore.UiWindowsCollection.item

    Retrieve a window object.

    :Parameters:

    **indexOrCaption** : :obj:`~typing.Any`

    :Returns:

        :obj:`~UiWindow`


.. py:method:: arrange(self, arrangeStyle: ARRANGE_STYLE) -> None
    :canonical: ansys.stk.core.uicore.UiWindowsCollection.arrange

    Arranges the application windows using the specified style.

    :Parameters:

    **arrangeStyle** : :obj:`~ARRANGE_STYLE`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, pluginID: str, initData: typing.Any) -> UiWindow
    :canonical: ansys.stk.core.uicore.UiWindowsCollection.add

    Create a new window. The bstrPluginID is a COM ProgID associated with an STK plugin.

    :Parameters:

    **pluginID** : :obj:`~str`
    **initData** : :obj:`~typing.Any`

    :Returns:

        :obj:`~UiWindow`


.. py:method:: get_item_by_index(self, index: int) -> UiWindow
    :canonical: ansys.stk.core.uicore.UiWindowsCollection.get_item_by_index

    Retrieve a window object by index in collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~UiWindow`

.. py:method:: get_item_by_name(self, name: str) -> UiWindow
    :canonical: ansys.stk.core.uicore.UiWindowsCollection.get_item_by_name

    Retrieve a window object by name of window object.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~UiWindow`

