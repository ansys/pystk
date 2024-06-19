ITimeToolFindTimesResult
========================

.. py:class:: ITimeToolFindTimesResult

   object
   
   Return a collection of intervals and an array of times.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~intervals`
            * - :py:meth:`~start`
            * - :py:meth:`~stop`
            * - :py:meth:`~times`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolFindTimesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolFindTimesResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.vgt.ITimeToolFindTimesResult.intervals
    :type: IAgCrdnIntervalCollection

    A collection of found intervals.

.. py:property:: start
    :canonical: ansys.stk.core.vgt.ITimeToolFindTimesResult.start
    :type: typing.Any

    The start time of the entire interval span.

.. py:property:: stop
    :canonical: ansys.stk.core.vgt.ITimeToolFindTimesResult.stop
    :type: typing.Any

    The stop time of the entire interval span.

.. py:property:: times
    :canonical: ansys.stk.core.vgt.ITimeToolFindTimesResult.times
    :type: list

    An array of found times.


