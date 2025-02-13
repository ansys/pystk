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
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.file_open_dialog_extension`
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
              - Return a reference to the currently loaded personality.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.visible`
              - Get or set whether the main window is visible.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.user_control`
              - Get or set whether the application is user controlled.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.windows`
              - Return a collection of windows.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.height`
              - Get or set a height of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.width`
              - Get or set a width of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.left`
              - Get or set a vertical coordinate of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.top`
              - Get or set a horizontal coordinate of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.window_state`
              - Get or set the state of the main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.most_recently_used_list`
              - Return a collection most recently used files.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.path`
              - Return the complete path to the application, excluding the final separator and name of the application. Read-only String.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.hwnd`
              - Return an HWND handle associated with the application main window.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.message_pending_delay`
              - Get or set message-pending delay for server busy dialog (in milliseconds).
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.personality2`
              - Return an new instance of the root object of the STK Object Model.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.log_file`
              - Get the current log files full path.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.display_alerts`
              - Set to true to display certain alerts and messages. Otherwise false. The default value is True.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiApplication.process_id`
              - Get process id for the current instance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import UiApplication


Property detail
---------------

.. py:property:: personality
    :canonical: ansys.stk.core.uiapplication.UiApplication.personality
    :type: typing.Any

    Return a reference to the currently loaded personality.

.. py:property:: visible
    :canonical: ansys.stk.core.uiapplication.UiApplication.visible
    :type: bool

    Get or set whether the main window is visible.

.. py:property:: user_control
    :canonical: ansys.stk.core.uiapplication.UiApplication.user_control
    :type: bool

    Get or set whether the application is user controlled.

.. py:property:: windows
    :canonical: ansys.stk.core.uiapplication.UiApplication.windows
    :type: IWindowsCollection

    Return a collection of windows.

.. py:property:: height
    :canonical: ansys.stk.core.uiapplication.UiApplication.height
    :type: int

    Get or set a height of the main window.

.. py:property:: width
    :canonical: ansys.stk.core.uiapplication.UiApplication.width
    :type: int

    Get or set a width of the main window.

.. py:property:: left
    :canonical: ansys.stk.core.uiapplication.UiApplication.left
    :type: int

    Get or set a vertical coordinate of the main window.

.. py:property:: top
    :canonical: ansys.stk.core.uiapplication.UiApplication.top
    :type: int

    Get or set a horizontal coordinate of the main window.

.. py:property:: window_state
    :canonical: ansys.stk.core.uiapplication.UiApplication.window_state
    :type: ApplicationWindowState

    Get or set the state of the main window.

.. py:property:: most_recently_used_list
    :canonical: ansys.stk.core.uiapplication.UiApplication.most_recently_used_list
    :type: MostRecentlyUsedCollection

    Return a collection most recently used files.

.. py:property:: path
    :canonical: ansys.stk.core.uiapplication.UiApplication.path
    :type: str

    Return the complete path to the application, excluding the final separator and name of the application. Read-only String.

.. py:property:: hwnd
    :canonical: ansys.stk.core.uiapplication.UiApplication.hwnd
    :type: int

    Return an HWND handle associated with the application main window.

.. py:property:: message_pending_delay
    :canonical: ansys.stk.core.uiapplication.UiApplication.message_pending_delay
    :type: int

    Get or set message-pending delay for server busy dialog (in milliseconds).

.. py:property:: personality2
    :canonical: ansys.stk.core.uiapplication.UiApplication.personality2
    :type: typing.Any

    Return an new instance of the root object of the STK Object Model.

.. py:property:: log_file
    :canonical: ansys.stk.core.uiapplication.UiApplication.log_file
    :type: str

    Get the current log files full path.

.. py:property:: display_alerts
    :canonical: ansys.stk.core.uiapplication.UiApplication.display_alerts
    :type: bool

    Set to true to display certain alerts and messages. Otherwise false. The default value is True.

.. py:property:: process_id
    :canonical: ansys.stk.core.uiapplication.UiApplication.process_id
    :type: int

    Get process id for the current instance.


Method detail
-------------

.. py:method:: load_personality(self, pers_name: str) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.load_personality

    Load a personality by its name.

    :Parameters:

    **pers_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

















.. py:method:: activate(self) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.activate

    Activates the application's main window.

    :Returns:

        :obj:`~None`


.. py:method:: file_open_dialog(self, default_ext: str, filter: str, initial_dir: str) -> str
    :canonical: ansys.stk.core.uiapplication.UiApplication.file_open_dialog

    Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.

    :Parameters:

    **default_ext** : :obj:`~str`
    **filter** : :obj:`~str`
    **initial_dir** : :obj:`~str`

    :Returns:

        :obj:`~str`


.. py:method:: create_object(self, prog_id: str, remote_server: str) -> typing.Any
    :canonical: ansys.stk.core.uiapplication.UiApplication.create_object

    Only works from local HTML pages and scripts.

    :Parameters:

    **prog_id** : :obj:`~str`
    **remote_server** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: file_save_as_dialog(self, default_ext: str, filter: str, initial_dir: str) -> str
    :canonical: ansys.stk.core.uiapplication.UiApplication.file_save_as_dialog

    Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.

    :Parameters:

    **default_ext** : :obj:`~str`
    **filter** : :obj:`~str`
    **initial_dir** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: quit(self) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.quit

    Shuts down the application.

    :Returns:

        :obj:`~None`

.. py:method:: file_open_dialog_extension(self, allow_multi_select: bool, default_ext: str, filter: str, initial_dir: str) -> UiFileOpenDialogExtension
    :canonical: ansys.stk.core.uiapplication.UiApplication.file_open_dialog_extension

    Brings up a standard File Open Dialog and returns an object representing the selected file.

    :Parameters:

    **allow_multi_select** : :obj:`~bool`
    **default_ext** : :obj:`~str`
    **filter** : :obj:`~str`
    **initial_dir** : :obj:`~str`

    :Returns:

        :obj:`~UiFileOpenDialogExtension`


.. py:method:: directory_picker_dialog(self, title: str, initial_dir: str) -> str
    :canonical: ansys.stk.core.uiapplication.UiApplication.directory_picker_dialog

    Brings up the Directory Picker Dialog and returns a selected directory name.

    :Parameters:

    **title** : :obj:`~str`
    **initial_dir** : :obj:`~str`

    :Returns:

        :obj:`~str`




.. py:method:: open_log_file(self, log_file_name: str, log_file_mode: ApplicationOpenLogFileMode) -> bool
    :canonical: ansys.stk.core.uiapplication.UiApplication.open_log_file

    Specify the current log file to be written to.

    :Parameters:

    **log_file_name** : :obj:`~str`
    **log_file_mode** : :obj:`~ApplicationOpenLogFileMode`

    :Returns:

        :obj:`~bool`

.. py:method:: log_message(self, msg_type: ApplicationLogMessageType, msg: str) -> None
    :canonical: ansys.stk.core.uiapplication.UiApplication.log_message

    Log the Message specified.

    :Parameters:

    **msg_type** : :obj:`~ApplicationLogMessageType`
    **msg** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: create_application(self) -> UiApplication
    :canonical: ansys.stk.core.uiapplication.UiApplication.create_application

    Create a new instance of the application model root object.

    :Returns:

        :obj:`~UiApplication`


