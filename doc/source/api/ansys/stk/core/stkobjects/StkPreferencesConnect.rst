StkPreferencesConnect
=====================

.. py:class:: ansys.stk.core.stkobjects.StkPreferencesConnect

   Allow configuring connect preferences.

.. py:currentmodule:: StkPreferencesConnect

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.allow_connect`
              - Gets or sets the connection allowed property.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.allow_async`
              - Asynchronous allowed.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.max_connections`
              - Max number of simultaneous connections.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.poll_period`
              - Period between port polls in msec.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.socket`
              - TCP/IP Socket Port.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.acknowledge_message_receipt`
              - Gets or sets the initial connect Acknowledge mode state.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.error_notify_mode`
              - Gets or sets the initial connect Error Notify mode state.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.wildcard_ignore_nack`
              - Ignore Backs when Wildcards used.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.verbose`
              - Gets or sets the initial connect Verbose mode state.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.allow_logging`
              - Allow for command logging.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.log_file`
              - File for logging commands.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesConnect.allow_ext_connect`
              - Allow connections from other machines.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkPreferencesConnect


Property detail
---------------

.. py:property:: allow_connect
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.allow_connect
    :type: bool

    Gets or sets the connection allowed property.

.. py:property:: allow_async
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.allow_async
    :type: bool

    Asynchronous allowed.

.. py:property:: max_connections
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.max_connections
    :type: int

    Max number of simultaneous connections.

.. py:property:: poll_period
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.poll_period
    :type: int

    Period between port polls in msec.

.. py:property:: socket
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.socket
    :type: int

    TCP/IP Socket Port.

.. py:property:: acknowledge_message_receipt
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.acknowledge_message_receipt
    :type: bool

    Gets or sets the initial connect Acknowledge mode state.

.. py:property:: error_notify_mode
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.error_notify_mode
    :type: bool

    Gets or sets the initial connect Error Notify mode state.

.. py:property:: wildcard_ignore_nack
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.wildcard_ignore_nack
    :type: bool

    Ignore Backs when Wildcards used.

.. py:property:: verbose
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.verbose
    :type: bool

    Gets or sets the initial connect Verbose mode state.

.. py:property:: allow_logging
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.allow_logging
    :type: bool

    Allow for command logging.

.. py:property:: log_file
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.log_file
    :type: str

    File for logging commands.

.. py:property:: allow_ext_connect
    :canonical: ansys.stk.core.stkobjects.StkPreferencesConnect.allow_ext_connect
    :type: bool

    Allow connections from other machines.


