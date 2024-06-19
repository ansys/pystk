CHAIN_TIME_PERIOD_TYPE
======================

.. py:class:: CHAIN_TIME_PERIOD_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~TIME_PERIOD_UNKNOWN`
              - Unsupported time period type.

            * - :py:attr:`~USE_OBJECT_TIME_PERIODS`
              - The Time Period that you set for objects in the chain is used to compute access. For facilities, places and targets, the scenario Time Period is used.

            * - :py:attr:`~USE_SCENARIO_TIME_PERIOD`
              - The Time Period that you set for the scenario is used to compute access.

            * - :py:attr:`~USER_SPECIFIED_TIME_PERIOD`
              - Specify the Start and Stop time for access computation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CHAIN_TIME_PERIOD_TYPE


