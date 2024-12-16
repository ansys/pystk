STKEngineTimerType
==================

.. py:class:: ansys.stk.core.stkengine.STKEngineTimerType

   IntEnum

   Specify the timer implementation to use.

   Timers are needed for events on Linux applications.
   May be overridden by specifying environment variable STK_PYTHONAPI_TIMERTYPE.

.. py:currentmodule:: STKEngineTimerType


Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~DISABLE_TIMERS`
              - Disable timers. This option is always selected on Windows applications.

            * - :py:attr:`~TKINTER_MAIN_LOOP`
              - Tkinter TCL timer dependent on the tkinter main loop. Default for tkinter applications.

            * - :py:attr:`~INTERACTIVE_PYTHON`
              - Tkinter TCL timer dependent on the interactive Python environment. Default for interactive Python applications.

            * - :py:attr:`~SIG_ALARM`
              - Use the standard signal SIGALRM for timer notifications. Default when not using tkinter or interactice Python.

            * - :py:attr:`~SIG_RT`
              - Use a real-time signal for timer notifications. Default signal is SIGRTMIN. May be overridden by specifying environment variable STK_PYHONAPI_TIMERTYPE5_SIGRTMIN_OFFSET.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkengine import STKEngineTimerType


