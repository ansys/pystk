LOGGING_MODE
============

.. py:class:: LOGGING_MODE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~INACTIVE`
              - The log file is not created.

            * - :py:attr:`~ACTIVE`
              - The log file is created but deleted upon application termination.

            * - :py:attr:`~ACTIVE_KEEP_FILE`
              - The log file is created and kept even after application is terminated.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import LOGGING_MODE


