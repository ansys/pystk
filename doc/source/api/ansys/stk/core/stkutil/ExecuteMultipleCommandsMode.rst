ExecuteMultipleCommandsMode
===========================

.. py:class:: ansys.stk.core.stkutil.ExecuteMultipleCommandsMode

   IntFlag


.. py:currentmodule:: ExecuteMultipleCommandsMode

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CONTINUE_ON_ERROR`
              - Continue executing the remaining commands in the command batch.

            * - :py:attr:`~STOP_ON_ERROR`
              - Terminate the execution of the command batch but do not throw an exception.

            * - :py:attr:`~EXCEPTION_ON_ERROR`
              - Terminate the execution of the command batch and throw an exception.

            * - :py:attr:`~DISCARD_RESULTS`
              - Ignore results returned by individual commands. The option must be used in combination with other flags.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import ExecuteMultipleCommandsMode


