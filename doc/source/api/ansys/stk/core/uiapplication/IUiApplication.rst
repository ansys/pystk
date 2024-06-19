IUiApplication
==============

.. py:class:: IUiApplication

   object
   
   IAgUiApplication represents a root of the Application Model.

.. py:currentmodule:: ansys.stk.core.uiapplication

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~load_personality`
              - Load a personality by its name.
            * - :py:meth:`~activate`
              - Activates the application's main window.
            * - :py:meth:`~file_open_dialog`
              - Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.
            * - :py:meth:`~create_object`
              - Only works from local HTML pages and scripts.
            * - :py:meth:`~file_save_as_dialog`
              - Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.
            * - :py:meth:`~quit`
              - Shuts down the application.
            * - :py:meth:`~file_open_dialog_ext`
              - Brings up a standard File Open Dialog and returns an object representing the selected file.
            * - :py:meth:`~directory_picker_dialog`
              - Brings up the Directory Picker Dialog and returns a selected directory name.
            * - :py:meth:`~open_log_file`
              - Specify the current log file to be written to.
            * - :py:meth:`~log_msg`
              - Log the Message specified.
            * - :py:meth:`~create_application`
              - Create a new instance of the application model root object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~personality`
            * - :py:meth:`~visible`
            * - :py:meth:`~user_control`
            * - :py:meth:`~windows`
            * - :py:meth:`~height`
            * - :py:meth:`~width`
            * - :py:meth:`~left`
            * - :py:meth:`~top`
            * - :py:meth:`~window_state`
            * - :py:meth:`~mru_list`
            * - :py:meth:`~path`
            * - :py:meth:`~hwnd`
            * - :py:meth:`~message_pending_delay`
            * - :py:meth:`~personality2`
            * - :py:meth:`~log_file`
            * - :py:meth:`~display_alerts`
            * - :py:meth:`~process_id`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import IUiApplication


Property detail
---------------

.. py:property:: personality
    :canonical: ansys.stk.core.uiapplication.IUiApplication.personality
    :type: typing.Any

    Returns a reference to the currently loaded personality.

.. py:property:: visible
    :canonical: ansys.stk.core.uiapplication.IUiApplication.visible
    :type: bool

    Gets/sets whether the main window is visible.

.. py:property:: user_control
    :canonical: ansys.stk.core.uiapplication.IUiApplication.user_control
    :type: bool

    Gets/sets whether the application is user controlled.

.. py:property:: windows
    :canonical: ansys.stk.core.uiapplication.IUiApplication.windows
    :type: IAgUiWindowsCollection

    Returns a collection of windows.

.. py:property:: height
    :canonical: ansys.stk.core.uiapplication.IUiApplication.height
    :type: int

    Gets/sets a height of the main window.

.. py:property:: width
    :canonical: ansys.stk.core.uiapplication.IUiApplication.width
    :type: int

    Gets/sets a width of the main window.

.. py:property:: left
    :canonical: ansys.stk.core.uiapplication.IUiApplication.left
    :type: int

    Gets/sets a vertical coordinate of the main window.

.. py:property:: top
    :canonical: ansys.stk.core.uiapplication.IUiApplication.top
    :type: int

    Gets/sets a horizontal coordinate of the main window.

.. py:property:: window_state
    :canonical: ansys.stk.core.uiapplication.IUiApplication.window_state
    :type: WINDOW_STATE

    Gets/sets the state of the main window.

.. py:property:: mru_list
    :canonical: ansys.stk.core.uiapplication.IUiApplication.mru_list
    :type: IAgMRUCollection

    Returns a collection most recently used files.

.. py:property:: path
    :canonical: ansys.stk.core.uiapplication.IUiApplication.path
    :type: str

    Returns the complete path to the application, excluding the final separator and name of the application. Read-only String.

.. py:property:: hwnd
    :canonical: ansys.stk.core.uiapplication.IUiApplication.hwnd
    :type: int

    Returns an HWND handle associated with the application main window.

.. py:property:: message_pending_delay
    :canonical: ansys.stk.core.uiapplication.IUiApplication.message_pending_delay
    :type: int

    Gets/Sets message-pending delay for server busy dialog (in milliseconds).

.. py:property:: personality2
    :canonical: ansys.stk.core.uiapplication.IUiApplication.personality2
    :type: typing.Any

    Returns an new instance of the root object of the STK Object Model.

.. py:property:: log_file
    :canonical: ansys.stk.core.uiapplication.IUiApplication.log_file
    :type: str

    Gets the current log files full path.

.. py:property:: display_alerts
    :canonical: ansys.stk.core.uiapplication.IUiApplication.display_alerts
    :type: bool

    Set to true to display certain alerts and messages. Otherwise false. The default value is True.

.. py:property:: process_id
    :canonical: ansys.stk.core.uiapplication.IUiApplication.process_id
    :type: int

    Gets process id for the current instance.


Method detail
-------------

.. py:method:: load_personality(self, persName: str) -> None
    :canonical: ansys.stk.core.uiapplication.IUiApplication.load_personality

    Load a personality by its name.

    :Parameters:

    **persName** : :obj:`~str`

    :Returns:

        :obj:`~None`

















.. py:method:: activate(self) -> None
    :canonical: ansys.stk.core.uiapplication.IUiApplication.activate

    Activates the application's main window.

    :Returns:

        :obj:`~None`


.. py:method:: file_open_dialog(self, defaultExt: str, filter: str, initialDir: str) -> str
    :canonical: ansys.stk.core.uiapplication.IUiApplication.file_open_dialog

    Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.

    :Parameters:

    **defaultExt** : :obj:`~str`
    **filter** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~str`


.. py:method:: create_object(self, progID: str, remoteServer: str) -> typing.Any
    :canonical: ansys.stk.core.uiapplication.IUiApplication.create_object

    Only works from local HTML pages and scripts.

    :Parameters:

    **progID** : :obj:`~str`
    **remoteServer** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: file_save_as_dialog(self, defaultExt: str, filter: str, initialDir: str) -> str
    :canonical: ansys.stk.core.uiapplication.IUiApplication.file_save_as_dialog

    Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.

    :Parameters:

    **defaultExt** : :obj:`~str`
    **filter** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: quit(self) -> None
    :canonical: ansys.stk.core.uiapplication.IUiApplication.quit

    Shuts down the application.

    :Returns:

        :obj:`~None`

.. py:method:: file_open_dialog_ext(self, allowMultiSelect: bool, defaultExt: str, filter: str, initialDir: str) -> IUiFileOpenExt
    :canonical: ansys.stk.core.uiapplication.IUiApplication.file_open_dialog_ext

    Brings up a standard File Open Dialog and returns an object representing the selected file.

    :Parameters:

    **allowMultiSelect** : :obj:`~bool`
    **defaultExt** : :obj:`~str`
    **filter** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~IUiFileOpenExt`


.. py:method:: directory_picker_dialog(self, title: str, initialDir: str) -> str
    :canonical: ansys.stk.core.uiapplication.IUiApplication.directory_picker_dialog

    Brings up the Directory Picker Dialog and returns a selected directory name.

    :Parameters:

    **title** : :obj:`~str`
    **initialDir** : :obj:`~str`

    :Returns:

        :obj:`~str`




.. py:method:: open_log_file(self, logFileName: str, logFileMode: OPEN_LOG_FILE_MODE) -> bool
    :canonical: ansys.stk.core.uiapplication.IUiApplication.open_log_file

    Specify the current log file to be written to.

    :Parameters:

    **logFileName** : :obj:`~str`
    **logFileMode** : :obj:`~OPEN_LOG_FILE_MODE`

    :Returns:

        :obj:`~bool`

.. py:method:: log_msg(self, msgType: UI_LOG_MSG_TYPE, msg: str) -> None
    :canonical: ansys.stk.core.uiapplication.IUiApplication.log_msg

    Log the Message specified.

    :Parameters:

    **msgType** : :obj:`~UI_LOG_MSG_TYPE`
    **msg** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: create_application(self) -> IUiApplication
    :canonical: ansys.stk.core.uiapplication.IUiApplication.create_application

    Create a new instance of the application model root object.

    :Returns:

        :obj:`~IUiApplication`


