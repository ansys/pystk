ITimeToolEventStartStopTime
===========================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventStartStopTime

   object
   
   Event is either start or stop time selected from a reference interval.

.. py:currentmodule:: ITimeToolEventStartStopTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventStartStopTime.use_start`
              - Indicates whether to use start (true) or stop (false).
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventStartStopTime.reference_event_interval`
              - The reference interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventStartStopTime


Property detail
---------------

.. py:property:: use_start
    :canonical: ansys.stk.core.vgt.ITimeToolEventStartStopTime.use_start
    :type: bool

    Indicates whether to use start (true) or stop (false).

.. py:property:: reference_event_interval
    :canonical: ansys.stk.core.vgt.ITimeToolEventStartStopTime.reference_event_interval
    :type: ITimeToolEventInterval

    The reference interval.


