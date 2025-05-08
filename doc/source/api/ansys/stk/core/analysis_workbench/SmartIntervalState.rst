SmartIntervalState
==================

.. py:class:: ansys.stk.core.analysis_workbench.SmartIntervalState

   IntEnum


.. py:currentmodule:: SmartIntervalState

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EXPLICIT`
              - Smart interval is specified explicitly using start/stop times.

            * - :py:attr:`~IMPLICIT`
              - Smart interval is specified implicitly using start/stop times.

            * - :py:attr:`~START_STOP`
              - Smart interval is specified using smart epochs.

            * - :py:attr:`~START_DURATION`
              - Smart interval is specified using a start epoch and duration.

            * - :py:attr:`~EXPLICIT_DURATION`
              - Smart interval is specified using a start time and explicit duration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SmartIntervalState


