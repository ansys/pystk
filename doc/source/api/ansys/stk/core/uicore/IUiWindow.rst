IUiWindow
=========

.. py:class:: IUiWindow

   object
   
   Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window.

.. py:currentmodule:: ansys.stk.core.uicore

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~activate`
              - Activates the window.
            * - :py:meth:`~close`
              - Close the window.
            * - :py:meth:`~get_service_by_name`
              - Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.
            * - :py:meth:`~get_service_by_type`
              - Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~caption`
            * - :py:meth:`~window_state`
            * - :py:meth:`~height`
            * - :py:meth:`~width`
            * - :py:meth:`~left`
            * - :py:meth:`~top`
            * - :py:meth:`~dock_style`
            * - :py:meth:`~no_wb_close`
            * - :py:meth:`~un_pinned`
            * - :py:meth:`~supports_pinning`
            * - :py:meth:`~toolbars`


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
    :type: IAgUiToolbarCollection

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

