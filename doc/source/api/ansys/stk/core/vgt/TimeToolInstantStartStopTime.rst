TimeToolInstantStartStopTime
============================

.. py:class:: ansys.stk.core.vgt.TimeToolInstantStartStopTime

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolInstant`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Event is either start or stop time selected from a reference interval.

.. py:currentmodule:: TimeToolInstantStartStopTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantStartStopTime.use_start`
              - Indicates whether to use start (true) or stop (false).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantStartStopTime.reference_interval`
              - The reference interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolInstantStartStopTime


Property detail
---------------

.. py:property:: use_start
    :canonical: ansys.stk.core.vgt.TimeToolInstantStartStopTime.use_start
    :type: bool

    Indicates whether to use start (true) or stop (false).

.. py:property:: reference_interval
    :canonical: ansys.stk.core.vgt.TimeToolInstantStartStopTime.reference_interval
    :type: ITimeToolTimeInterval

    The reference interval.


