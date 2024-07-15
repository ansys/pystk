TimeToolFindTimesResult
=======================

.. py:class:: ansys.stk.core.vgt.TimeToolFindTimesResult

   Bases: 

   Return a collection of intervals and an array of times.

.. py:currentmodule:: TimeToolFindTimesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolFindTimesResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolFindTimesResult.intervals`
              - A collection of found intervals.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolFindTimesResult.start`
              - The start time of the entire interval span.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolFindTimesResult.stop`
              - The stop time of the entire interval span.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolFindTimesResult.times`
              - An array of found times.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolFindTimesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.TimeToolFindTimesResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.vgt.TimeToolFindTimesResult.intervals
    :type: ITimeToolIntervalCollection

    A collection of found intervals.

.. py:property:: start
    :canonical: ansys.stk.core.vgt.TimeToolFindTimesResult.start
    :type: typing.Any

    The start time of the entire interval span.

.. py:property:: stop
    :canonical: ansys.stk.core.vgt.TimeToolFindTimesResult.stop
    :type: typing.Any

    The stop time of the entire interval span.

.. py:property:: times
    :canonical: ansys.stk.core.vgt.TimeToolFindTimesResult.times
    :type: list

    An array of found times.


