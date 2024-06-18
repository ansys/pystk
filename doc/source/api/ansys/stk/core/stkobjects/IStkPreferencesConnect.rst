IStkPreferencesConnect
======================

.. py:class:: IStkPreferencesConnect

   object
   
   Connect settings.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~allow_connect`
            * - :py:meth:`~allow_async`
            * - :py:meth:`~max_connections`
            * - :py:meth:`~poll_period`
            * - :py:meth:`~socket`
            * - :py:meth:`~acknowledge_message_receipt`
            * - :py:meth:`~error_notify_mode`
            * - :py:meth:`~wildcard_ignore_nack`
            * - :py:meth:`~verbose`
            * - :py:meth:`~allow_logging`
            * - :py:meth:`~log_file`
            * - :py:meth:`~allow_ext_connect`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkPreferencesConnect


Property detail
---------------

.. py:property:: allow_connect
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.allow_connect
    :type: bool

    Gets or sets the connection allowed property.

.. py:property:: allow_async
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.allow_async
    :type: bool

    Asynchronous allowed.

.. py:property:: max_connections
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.max_connections
    :type: int

    Max number of simultaneous connections.

.. py:property:: poll_period
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.poll_period
    :type: int

    Period between port polls in msec.

.. py:property:: socket
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.socket
    :type: int

    TCP/IP Socket Port.

.. py:property:: acknowledge_message_receipt
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.acknowledge_message_receipt
    :type: bool

    Gets or sets the initial connect Acknowledge mode state.

.. py:property:: error_notify_mode
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.error_notify_mode
    :type: bool

    Gets or sets the initial connect Error Notify mode state.

.. py:property:: wildcard_ignore_nack
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.wildcard_ignore_nack
    :type: bool

    Ignore Backs when Wildcards used.

.. py:property:: verbose
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.verbose
    :type: bool

    Gets or sets the initial connect Verbose mode state.

.. py:property:: allow_logging
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.allow_logging
    :type: bool

    Allow for command logging.

.. py:property:: log_file
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.log_file
    :type: str

    File for logging commands.

.. py:property:: allow_ext_connect
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesConnect.allow_ext_connect
    :type: bool

    Allow connections from other machines.


