TimeToolTimeArrayFindTimesResult
================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult

   Return a collection of intervals and an array of times.

.. py:currentmodule:: TimeToolTimeArrayFindTimesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.is_valid`
              - Indicate whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.intervals`
              - A collection of found intervals.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.start`
              - The start time of the entire interval span.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.stop`
              - The stop time of the entire interval span.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.times`
              - An array of found times.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeArrayFindTimesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.is_valid
    :type: bool

    Indicate whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.intervals
    :type: TimeToolIntervalCollection

    A collection of found intervals.

.. py:property:: start
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.start
    :type: typing.Any

    The start time of the entire interval span.

.. py:property:: stop
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.stop
    :type: typing.Any

    The stop time of the entire interval span.

.. py:property:: times
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.times
    :type: list

    An array of found times.


