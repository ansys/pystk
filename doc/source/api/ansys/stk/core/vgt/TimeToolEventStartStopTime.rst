TimeToolEventStartStopTime
==========================

.. py:class:: ansys.stk.core.vgt.TimeToolEventStartStopTime

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEvent`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Event is either start or stop time selected from a reference interval.

.. py:currentmodule:: TimeToolEventStartStopTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventStartStopTime.use_start`
              - Indicates whether to use start (true) or stop (false).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventStartStopTime.reference_event_interval`
              - The reference interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventStartStopTime


Property detail
---------------

.. py:property:: use_start
    :canonical: ansys.stk.core.vgt.TimeToolEventStartStopTime.use_start
    :type: bool

    Indicates whether to use start (true) or stop (false).

.. py:property:: reference_event_interval
    :canonical: ansys.stk.core.vgt.TimeToolEventStartStopTime.reference_event_interval
    :type: ITimeToolEventInterval

    The reference interval.


