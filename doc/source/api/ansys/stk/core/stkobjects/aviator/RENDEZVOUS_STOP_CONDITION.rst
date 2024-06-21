RENDEZVOUS_STOP_CONDITION
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.RENDEZVOUS_STOP_CONDITION

   IntEnum


.. py:currentmodule:: RENDEZVOUS_STOP_CONDITION

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~STOP_NORMAL`
              - The basic stopping conditions will be used.

            * - :py:attr:`~STOP_AFTER_TARGET_CURRENT_PROCEDURE`
              - Stop after the target completes the current procedure.

            * - :py:attr:`~STOP_AFTER_TARGET_CURRENT_PHASE`
              - Stop after the target completes the current phase.

            * - :py:attr:`~STOP_WHEN_TARGET_PERF_MODE_CHANGES`
              - Stop when the target enters a new mode of flight.

            * - :py:attr:`~STOP_WHEN_TARGET_PHASE_OF_FLIGHT_CHANGES`
              - Stop when the target enters a new performance phase.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import RENDEZVOUS_STOP_CONDITION


