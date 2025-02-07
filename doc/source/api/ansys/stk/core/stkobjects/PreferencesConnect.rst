PreferencesConnect
==================

.. py:class:: ansys.stk.core.stkobjects.PreferencesConnect

   Allow configuring connect preferences.

.. py:currentmodule:: PreferencesConnect

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.allow_connect`
              - Get or set the connection allowed property.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.allow_asynchronous_communications`
              - Asynchronous allowed.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.maximum_connections`
              - Max number of simultaneous connections.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.polling_period`
              - Period between port polls in msec.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.socket`
              - TCP/IP Socket Port.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.acknowledge_message_receipt`
              - Get or set the initial connect Acknowledge mode state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.error_notify_mode`
              - Get or set the initial connect Error Notify mode state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.wildcard_ignore_nack`
              - Ignore Backs when Wildcards used.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.verbose`
              - Get or set the initial connect Verbose mode state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.allow_logging`
              - Allow for command logging.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.log_filename`
              - File for logging commands.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesConnect.allow_external_connect`
              - Allow connections from other machines.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PreferencesConnect


Property detail
---------------

.. py:property:: allow_connect
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.allow_connect
    :type: bool

    Get or set the connection allowed property.

.. py:property:: allow_asynchronous_communications
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.allow_asynchronous_communications
    :type: bool

    Asynchronous allowed.

.. py:property:: maximum_connections
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.maximum_connections
    :type: int

    Max number of simultaneous connections.

.. py:property:: polling_period
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.polling_period
    :type: int

    Period between port polls in msec.

.. py:property:: socket
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.socket
    :type: int

    TCP/IP Socket Port.

.. py:property:: acknowledge_message_receipt
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.acknowledge_message_receipt
    :type: bool

    Get or set the initial connect Acknowledge mode state.

.. py:property:: error_notify_mode
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.error_notify_mode
    :type: bool

    Get or set the initial connect Error Notify mode state.

.. py:property:: wildcard_ignore_nack
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.wildcard_ignore_nack
    :type: bool

    Ignore Backs when Wildcards used.

.. py:property:: verbose
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.verbose
    :type: bool

    Get or set the initial connect Verbose mode state.

.. py:property:: allow_logging
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.allow_logging
    :type: bool

    Allow for command logging.

.. py:property:: log_filename
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.log_filename
    :type: str

    File for logging commands.

.. py:property:: allow_external_connect
    :canonical: ansys.stk.core.stkobjects.PreferencesConnect.allow_external_connect
    :type: bool

    Allow connections from other machines.


