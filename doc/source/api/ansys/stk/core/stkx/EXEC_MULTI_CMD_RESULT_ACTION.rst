EXEC_MULTI_CMD_RESULT_ACTION
============================

.. py:class:: EXEC_MULTI_CMD_RESULT_ACTION

   IntFlag


.. py:currentmodule:: ansys.stk.core.stkx

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

            * - :py:attr:`~IGNORE_EXEC_CMD_RESULT`
              - Ignore results returned by individual commands. The option must be used in combination with other flags.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import EXEC_MULTI_CMD_RESULT_ACTION


