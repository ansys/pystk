IUiWindow
=========

.. py:class:: ansys.stk.core.uicore.IUiWindow

   object
   
   Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window.

.. py:currentmodule:: IUiWindow

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.activate`
              - Activates the window.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.close`
              - Close the window.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.get_service_by_name`
              - Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.get_service_by_type`
              - Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.caption`
              - Gets or sets the window caption. Can only be set within UI plugins for the non unique windows they own.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.window_state`
              - The window state.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.height`
              - The window height.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.width`
              - The window width.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.left`
              - The window horizontal position.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.top`
              - The window vertical position.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.dock_style`
              - The window docking style.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.no_wb_close`
              - Whether to close the window when the application workbook is loaded/closed.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.un_pinned`
              - The window's pinned state.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.supports_pinning`
              - Returns whether the window supports pinning.
            * - :py:attr:`~ansys.stk.core.uicore.IUiWindow.toolbars`
              - Returns the window's toolbar collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uicore import IUiWindow


Property detail
---------------

.. py:property:: caption
    :canonical: ansys.stk.core.uicore.IUiWindow.caption
    :type: str

    Gets or sets the window caption. Can only be set within UI plugins for the non unique windows they own.

.. py:property:: window_state
    :canonical: ansys.stk.core.uicore.IUiWindow.window_state
    :type: WINDOW_STATE

    The window state.

.. py:property:: height
    :canonical: ansys.stk.core.uicore.IUiWindow.height
    :type: int

    The window height.

.. py:property:: width
    :canonical: ansys.stk.core.uicore.IUiWindow.width
    :type: int

    The window width.

.. py:property:: left
    :canonical: ansys.stk.core.uicore.IUiWindow.left
    :type: int

    The window horizontal position.

.. py:property:: top
    :canonical: ansys.stk.core.uicore.IUiWindow.top
    :type: int

    The window vertical position.

.. py:property:: dock_style
    :canonical: ansys.stk.core.uicore.IUiWindow.dock_style
    :type: DOCK_STYLE

    The window docking style.

.. py:property:: no_wb_close
    :canonical: ansys.stk.core.uicore.IUiWindow.no_wb_close
    :type: bool

    Whether to close the window when the application workbook is loaded/closed.

.. py:property:: un_pinned
    :canonical: ansys.stk.core.uicore.IUiWindow.un_pinned
    :type: bool

    The window's pinned state.

.. py:property:: supports_pinning
    :canonical: ansys.stk.core.uicore.IUiWindow.supports_pinning
    :type: bool

    Returns whether the window supports pinning.

.. py:property:: toolbars
    :canonical: ansys.stk.core.uicore.IUiWindow.toolbars
    :type: IUiToolbarCollection

    Returns the window's toolbar collection.


Method detail
-------------



.. py:method:: activate(self) -> None
    :canonical: ansys.stk.core.uicore.IUiWindow.activate

    Activates the window.

    :Returns:

        :obj:`~None`



.. py:method:: close(self) -> None
    :canonical: ansys.stk.core.uicore.IUiWindow.close

    Close the window.

    :Returns:

        :obj:`~None`

















.. py:method:: get_service_by_name(self, name: str) -> typing.Any
    :canonical: ansys.stk.core.uicore.IUiWindow.get_service_by_name

    Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: get_service_by_type(self, serviceType: WINDOW_SERVICE) -> typing.Any
    :canonical: ansys.stk.core.uicore.IUiWindow.get_service_by_type

    Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.

    :Parameters:

    **serviceType** : :obj:`~WINDOW_SERVICE`

    :Returns:

        :obj:`~typing.Any`

