UiApplication
=============

.. py:class:: ansys.stk.core.uiapplication.UiApplication

   Bases: :py:class:`~ansys.stk.core.uiapplication.IUiApplicationPartnerAccess`

   A root object of the Application Model.

.. py:currentmodule:: UiApplication

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.load_personality`
              - Load a personality by its name.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.activate`
              - Activates the application's main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.file_open_dialog`
              - Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.create_object`
              - Only works from local HTML pages and scripts.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.file_save_as_dialog`
              - Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.quit`
              - Shuts down the application.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.file_open_dialog_ext`
              - Brings up a standard File Open Dialog and returns an object representing the selected file.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.directory_picker_dialog`
              - Brings up the Directory Picker Dialog and returns a selected directory name.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.open_log_file`
              - Specify the current log file to be written to.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.log_message`
              - Log the Message specified.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.create_application`
              - Create a new instance of the application model root object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.personality`
              - Returns a reference to the currently loaded personality.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.visible`
              - Gets/sets whether the main window is visible.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.user_control`
              - Gets/sets whether the application is user controlled.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.windows`
              - Returns a collection of windows.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.height`
              - Gets/sets a height of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.width`
              - Gets/sets a width of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.left`
              - Gets/sets a vertical coordinate of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.top`
              - Gets/sets a horizontal coordinate of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.window_state`
              - Gets/sets the state of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.mru_list`
              - Returns a collection most recently used files.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.path`
              - Returns the complete path to the application, excluding the final separator and name of the application. Read-only String.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.hwnd`
              - Returns an HWND handle associated with the application main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.message_pending_delay`
              - Gets/Sets message-pending delay for server busy dialog (in milliseconds).
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.personality2`
              - Returns an new instance of the root object of the STK Object Model.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.log_file`
              - Gets the current log files full path.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.display_alerts`
              - Set to true to display certain alerts and messages. Otherwise false. The default value is True.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.process_id`
              - Gets process id for the current instance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import UiApplication


Property detail
---------------

.. py:property:: personality
    :canonical: ansys.stk.core.uiapplication.UiApplication.personality
    :type: typing.Any

    Returns a reference to the currently loaded personality.

.. py:property:: visible
    :canonical: ansys.stk.core.uiapplication.UiApplication.visible
    :type: bool

    Gets/sets whether the main window is visible.

.. py:property:: user_control
    :canonical: ansys.stk.core.uiapplication.UiApplication.user_control
    :type: bool

    Gets/sets whether the application is user controlled.

.. py:property:: windows
    :canonical: ansys.stk.core.uiapplication.UiApplication.windows
    :type: IUiWindowsCollection

    Returns a collection of windows.

.. py:property:: height
    :canonical: ansys.stk.core.uiapplication.UiApplication.height
    :type: int

    Gets/sets a height of the main window.

.. py:property:: width
    :canonical: ansys.stk.core.uiapplication.UiApplication.width
    :type: int

    Gets/sets a width of the main window.

.. py:property:: left
    :canonical: ansys.stk.core.uiapplication.UiApplication.left
    :type: int

    Gets/sets a vertical coordinate of the main window.

.. py:property:: top
    :canonical: ansys.stk.core.uiapplication.UiApplication.top
    :type: int

    Gets/sets a horizontal coordinate of the main window.

.. py:property:: window_state
    :canonical: ansys.stk.core.uiapplication.UiApplication.window_state
    :type: WINDOW_STATE

    Gets/sets the state of the main window.

.. py:property:: mru_list
    :canonical: ansys.stk.core.uiapplication.UiApplication.mru_list
    :type: MRUCollection

    Returns a collection most recently used files.

.. py:property:: path
    :canonical: ansys.stk.core.uiapplication.UiApplication.path
    :type: str

    Returns the complete path to the application, excluding the final separator and name of the application. Read-only String.

.. py:property:: hwnd
    :canonical: ansys.stk.core.uiapplication.UiApplication.hwnd
    :type: int

    Returns an HWND handle associated with the application main window.

.. py:property:: message_pending_delay
    :canonical: ansys.stk.core.uiapplication.UiApplication.message_pending_delay
    :type: int

    Gets/Sets message-pending delay for server busy dialog (in milliseconds).

.. py:property:: personality2
    :canonical: ansys.stk.core.uiapplication.UiApplication.personality2
    :type: typing.Any

    Returns an new instance of the root object of the STK Object Model.

.. py:property:: log_file
    :canonical: ansys.stk.core.uiapplication.UiApplication.log_file
    :type: str

    Gets the current log files full path.

.. py:property:: display_alerts
    :canonical: ansys.stk.core.uiapplication.UiApplication.display_alerts
    :type: bool

    Set to true to display certain alerts and messages. Otherwise false. The default value is True.

.. py:property:: process_id
    :canonical: ansys.stk.core.uiapplication.UiApplication.process_id
    :type: int

    Gets process id for the current instance.


Method detail
-------------

.. py:method:: load_personality(self, persName: str) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.load_personality

    Load a personality by its name.

    :Parameters:

    **persName** : :obj:`~str`

    :Returns:

        :obj:`~None`

















.. py:method:: activate(self) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.activate

    Activates the application's main window.

    :Returns:

        :obj:`~None`


.. py:method:: file_open_dialog(self, defaultExt: str, filter: str, initialDir: str) -> str
    :canonical: ansys.stk.core.uiapplication.UiApplication.file_open_dialog

    Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.

    :Parameters:

    **defaultExt** : :obj:`~str`
    **filter** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~str`


.. py:method:: create_object(self, progID: str, remoteServer: str) -> typing.Any
    :canonical: ansys.stk.core.uiapplication.UiApplication.create_object

    Only works from local HTML pages and scripts.

    :Parameters:

    **progID** : :obj:`~str`
    **remoteServer** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: file_save_as_dialog(self, defaultExt: str, filter: str, initialDir: str) -> str
    :canonical: ansys.stk.core.uiapplication.UiApplication.file_save_as_dialog

    Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.

    :Parameters:

    **defaultExt** : :obj:`~str`
    **filter** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: quit(self) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.quit

    Shuts down the application.

    :Returns:

        :obj:`~None`

.. py:method:: file_open_dialog_ext(self, allowMultiSelect: bool, defaultExt: str, filter: str, initialDir: str) -> UiFileOpenExt
    :canonical: ansys.stk.core.uiapplication.UiApplication.file_open_dialog_ext

    Brings up a standard File Open Dialog and returns an object representing the selected file.

    :Parameters:

    **allowMultiSelect** : :obj:`~bool`
    **defaultExt** : :obj:`~str`
    **filter** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~UiFileOpenExt`


.. py:method:: directory_picker_dialog(self, title: str, initialDir: str) -> str
    :canonical: ansys.stk.core.uiapplication.UiApplication.directory_picker_dialog

    Brings up the Directory Picker Dialog and returns a selected directory name.

    :Parameters:

    **title** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~str`




.. py:method:: open_log_file(self, logFileName: str, logFileMode: OPEN_LOG_FILE_MODE) -> bool
    :canonical: ansys.stk.core.uiapplication.UiApplication.open_log_file

    Specify the current log file to be written to.

    :Parameters:

    **logFileName** : :obj:`~str`
    **logFileMode** : :obj:`~OPEN_LOG_FILE_MODE`

    :Returns:

        :obj:`~bool`

.. py:method:: log_message(self, msgType: UI_LOG_MESSAGE_TYPE, msg: str) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.log_message

    Log the Message specified.

    :Parameters:

    **msgType** : :obj:`~UI_LOG_MESSAGE_TYPE`
    **msg** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: create_application(self) -> UiApplication
    :canonical: ansys.stk.core.uiapplication.UiApplication.create_application

    Create a new instance of the application model root object.

    :Returns:

        :obj:`~UiApplication`


