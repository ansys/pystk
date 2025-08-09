ChainTimePeriodType
===================

.. py:class:: ansys.stk.core.stkobjects.ChainTimePeriodType

   IntEnum


.. py:currentmodule:: ChainTimePeriodType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported time period type.

            * - :py:attr:`~OBJECT_TIME_PERIODS`
              - The Time Period that you set for objects in the chain is used to compute access. For facilities, places and targets, the scenario Time Period is used.

            * - :py:attr:`~SCENARIO_TIME_PERIOD`
              - The Time Period that you set for the scenario is used to compute access.

            * - :py:attr:`~SPECIFIED_TIME_PERIOD`
              - Specify the Start and Stop time for access computation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainTimePeriodType


