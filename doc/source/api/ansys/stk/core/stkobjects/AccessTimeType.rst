AccessTimeType
==============

.. py:class:: ansys.stk.core.stkobjects.AccessTimeType

   IntEnum


.. py:currentmodule:: AccessTimeType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~OBJECT_ACCESS_TIME`
              - Use the start and stop time set for the objects involved in the access calculations as a time period for the access computation.

            * - :py:attr:`~SCENARIO_INTERVAL`
              - Use the start and stop time set at the scenario level as a time period for the access computation.

            * - :py:attr:`~SPECIFIED_TIME_PERIOD`
              - The option is used to select a user-specified start and stop time to define the time period for the access computation.

            * - :py:attr:`~TIME_INTERVALS`
              - The option is used to select a collection of intervals to define the time period for the access computation.

            * - :py:attr:`~TIME_INTERVAL_LIST`
              - The option is used to select an event interval list to define the time period for the access computation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessTimeType


