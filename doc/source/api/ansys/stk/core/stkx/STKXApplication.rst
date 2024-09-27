STKXApplication
===============

.. py:class:: ansys.stk.core.stkx.STKXApplication

   STK X Application object.

.. py:currentmodule:: STKXApplication

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.execute_command`
              - Send a connect command to STK X.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.get_licensing_report`
              - Do not use this method, as it is deprecated. Returns a formatted string that contains the license names and their states. The string is formatted as an XML document.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.set_online_options`
              - Set http proxy online options.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.get_online_options`
              - Get http proxy online options.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.set_connect_handler`
              - Set callback to handle a certain connect command.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.execute_multiple_commands`
              - Execute multiple CONNECT actions. The method throws an exception if any of the specified commands have failed.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.is_feature_available`
              - Return true if the specified feature is available.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.terminate`
              - Terminates the use of STK Engine. This must be the last call to STK Engine.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.use_software_renderer`
              - Configure engine graphics to use a software renderer in order to meet minimum graphics requirements. Enabling this option will result in significant performance impacts.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.Subscribe`
              - """Return an ISTKXApplicationEventHandler that is subscribed to handle events associated with this instance of STKXApplication."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.enable_connect`
              - Enable or disable TCP/IP connect command processing (default: disabled).
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.connect_port`
              - Specify TCP/IP port to be used by Connect (default: 5001).
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.host_id`
              - Returns the Host ID.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.registration_id`
              - Returns the Registration ID.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.version`
              - Returns the version number.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.vendor_id`
              - This property is deprecated. The identifier of the vendor.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.log_file_full_name`
              - Returns full path and log file name.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.logging_mode`
              - Controls the log file generation, and if the log file is deleted or not on application exit.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.connect_max_connections`
              - Specify the maximum number of Connect connections to allow.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.no_graphics`
              - Start engine with or without graphics (default: engine starts with graphics.).
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.show_sla_if_not_accepted`
              - Shows the Software License Agreement dialog if not already accepted.
            * - :py:attr:`~ansys.stk.core.stkx.STKXApplication.use_hook`
              - Start engine with or without message hook setup (default: engine starts with message hook setup.).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import STKXApplication


Property detail
---------------

.. py:property:: enable_connect
    :canonical: ansys.stk.core.stkx.STKXApplication.enable_connect
    :type: bool

    Enable or disable TCP/IP connect command processing (default: disabled).

.. py:property:: connect_port
    :canonical: ansys.stk.core.stkx.STKXApplication.connect_port
    :type: int

    Specify TCP/IP port to be used by Connect (default: 5001).

.. py:property:: host_id
    :canonical: ansys.stk.core.stkx.STKXApplication.host_id
    :type: str

    Returns the Host ID.

.. py:property:: registration_id
    :canonical: ansys.stk.core.stkx.STKXApplication.registration_id
    :type: str

    Returns the Registration ID.

.. py:property:: version
    :canonical: ansys.stk.core.stkx.STKXApplication.version
    :type: str

    Returns the version number.

.. py:property:: vendor_id
    :canonical: ansys.stk.core.stkx.STKXApplication.vendor_id
    :type: str

    This property is deprecated. The identifier of the vendor.

.. py:property:: log_file_full_name
    :canonical: ansys.stk.core.stkx.STKXApplication.log_file_full_name
    :type: str

    Returns full path and log file name.

.. py:property:: logging_mode
    :canonical: ansys.stk.core.stkx.STKXApplication.logging_mode
    :type: LOGGING_MODE

    Controls the log file generation, and if the log file is deleted or not on application exit.

.. py:property:: connect_max_connections
    :canonical: ansys.stk.core.stkx.STKXApplication.connect_max_connections
    :type: int

    Specify the maximum number of Connect connections to allow.

.. py:property:: no_graphics
    :canonical: ansys.stk.core.stkx.STKXApplication.no_graphics
    :type: bool

    Start engine with or without graphics (default: engine starts with graphics.).

.. py:property:: show_sla_if_not_accepted
    :canonical: ansys.stk.core.stkx.STKXApplication.show_sla_if_not_accepted
    :type: bool

    Shows the Software License Agreement dialog if not already accepted.

.. py:property:: use_hook
    :canonical: ansys.stk.core.stkx.STKXApplication.use_hook
    :type: None

    Start engine with or without message hook setup (default: engine starts with message hook setup.).


Method detail
-------------

.. py:method:: execute_command(self, command: str) -> ExecuteCommandResult
    :canonical: ansys.stk.core.stkx.STKXApplication.execute_command

    Send a connect command to STK X.

    :Parameters:

    **command** : :obj:`~str`

    :Returns:

        :obj:`~ExecuteCommandResult`








.. py:method:: get_licensing_report(self) -> str
    :canonical: ansys.stk.core.stkx.STKXApplication.get_licensing_report

    Do not use this method, as it is deprecated. Returns a formatted string that contains the license names and their states. The string is formatted as an XML document.

    :Returns:

        :obj:`~str`



.. py:method:: set_online_options(self, useProxy: bool, serverName: str, portNum: int, userName: str, password: str, savePassword: bool) -> bool
    :canonical: ansys.stk.core.stkx.STKXApplication.set_online_options

    Set http proxy online options.

    :Parameters:

    **useProxy** : :obj:`~bool`
    **serverName** : :obj:`~str`
    **portNum** : :obj:`~int`
    **userName** : :obj:`~str`
    **password** : :obj:`~str`
    **savePassword** : :obj:`~bool`

    :Returns:

        :obj:`~bool`

.. py:method:: get_online_options(self) -> typing.Tuple[bool, str, int, str, bool]
    :canonical: ansys.stk.core.stkx.STKXApplication.get_online_options

    Get http proxy online options.

    :Returns:

        :obj:`~typing.Tuple[bool, str, int, str, bool]`

.. py:method:: set_connect_handler(self, commandID: str, progID: str) -> None
    :canonical: ansys.stk.core.stkx.STKXApplication.set_connect_handler

    Set callback to handle a certain connect command.

    :Parameters:

    **commandID** : :obj:`~str`
    **progID** : :obj:`~str`

    :Returns:

        :obj:`~None`






.. py:method:: execute_multiple_commands(self, connectCommands: list, eAction: EXECUTE_MULTIPLE_COMMANDS_MODE) -> ExecuteMultipleCommandResult
    :canonical: ansys.stk.core.stkx.STKXApplication.execute_multiple_commands

    Execute multiple CONNECT actions. The method throws an exception if any of the specified commands have failed.

    :Parameters:

    **connectCommands** : :obj:`~list`
    **eAction** : :obj:`~EXECUTE_MULTIPLE_COMMANDS_MODE`

    :Returns:

        :obj:`~ExecuteMultipleCommandResult`

.. py:method:: is_feature_available(self, featureCode: FEATURE_CODES) -> bool
    :canonical: ansys.stk.core.stkx.STKXApplication.is_feature_available

    Return true if the specified feature is available.

    :Parameters:

    **featureCode** : :obj:`~FEATURE_CODES`

    :Returns:

        :obj:`~bool`



.. py:method:: terminate(self) -> None
    :canonical: ansys.stk.core.stkx.STKXApplication.terminate

    Terminates the use of STK Engine. This must be the last call to STK Engine.

    :Returns:

        :obj:`~None`





.. py:method:: use_software_renderer(self) -> None
    :canonical: ansys.stk.core.stkx.STKXApplication.use_software_renderer

    Configure engine graphics to use a software renderer in order to meet minimum graphics requirements. Enabling this option will result in significant performance impacts.

    :Returns:

        :obj:`~None`

