Window
======

.. py:class:: ansys.stk.core.uicore.Window

   Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window.

.. py:currentmodule:: Window

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.Window.activate`
              - Activates the window.
            * - :py:attr:`~ansys.stk.core.uicore.Window.close`
              - Close the window.
            * - :py:attr:`~ansys.stk.core.uicore.Window.get_service_by_name`
              - Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.
            * - :py:attr:`~ansys.stk.core.uicore.Window.get_service_by_type`
              - Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uicore.Window.can_pin`
              - Return whether the window supports pinning.
            * - :py:attr:`~ansys.stk.core.uicore.Window.caption`
              - Get or set the window caption. Can only be set within UI plugins for the non unique windows they own.
            * - :py:attr:`~ansys.stk.core.uicore.Window.dock_style`
              - The window docking style.
            * - :py:attr:`~ansys.stk.core.uicore.Window.height`
              - The window height.
            * - :py:attr:`~ansys.stk.core.uicore.Window.left`
              - The window horizontal position.
            * - :py:attr:`~ansys.stk.core.uicore.Window.no_workbook_close`
              - Whether to close the window when the application workbook is loaded/closed.
            * - :py:attr:`~ansys.stk.core.uicore.Window.toolbars`
              - Return the window's toolbar collection.
            * - :py:attr:`~ansys.stk.core.uicore.Window.top`
              - The window vertical position.
            * - :py:attr:`~ansys.stk.core.uicore.Window.unpinned`
              - The window's pinned state.
            * - :py:attr:`~ansys.stk.core.uicore.Window.width`
              - The window width.
            * - :py:attr:`~ansys.stk.core.uicore.Window.window_state`
              - The window state.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uicore import Window


Property detail
---------------

.. py:property:: can_pin
    :canonical: ansys.stk.core.uicore.Window.can_pin
    :type: bool

    Return whether the window supports pinning.

.. py:property:: caption
    :canonical: ansys.stk.core.uicore.Window.caption
    :type: str

    Get or set the window caption. Can only be set within UI plugins for the non unique windows they own.

.. py:property:: dock_style
    :canonical: ansys.stk.core.uicore.Window.dock_style
    :type: WindowDockStyle

    The window docking style.

.. py:property:: height
    :canonical: ansys.stk.core.uicore.Window.height
    :type: int

    The window height.

.. py:property:: left
    :canonical: ansys.stk.core.uicore.Window.left
    :type: int

    The window horizontal position.

.. py:property:: no_workbook_close
    :canonical: ansys.stk.core.uicore.Window.no_workbook_close
    :type: bool

    Whether to close the window when the application workbook is loaded/closed.

.. py:property:: toolbars
    :canonical: ansys.stk.core.uicore.Window.toolbars
    :type: ToolbarCollection

    Return the window's toolbar collection.

.. py:property:: top
    :canonical: ansys.stk.core.uicore.Window.top
    :type: int

    The window vertical position.

.. py:property:: unpinned
    :canonical: ansys.stk.core.uicore.Window.unpinned
    :type: bool

    The window's pinned state.

.. py:property:: width
    :canonical: ansys.stk.core.uicore.Window.width
    :type: int

    The window width.

.. py:property:: window_state
    :canonical: ansys.stk.core.uicore.Window.window_state
    :type: ApplicationWindowState

    The window state.


Method detail
-------------

.. py:method:: activate(self) -> None
    :canonical: ansys.stk.core.uicore.Window.activate

    Activates the window.

    :Returns:

        :obj:`~None`



.. py:method:: close(self) -> None
    :canonical: ansys.stk.core.uicore.Window.close

    Close the window.

    :Returns:

        :obj:`~None`



.. py:method:: get_service_by_name(self, name: str) -> typing.Any
    :canonical: ansys.stk.core.uicore.Window.get_service_by_name

    Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

.. py:method:: get_service_by_type(self, service_type: WindowServiceType) -> typing.Any
    :canonical: ansys.stk.core.uicore.Window.get_service_by_type

    Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.

    :Parameters:

        **service_type** : :obj:`~WindowServiceType`


    :Returns:

        :obj:`~typing.Any`

















