ITimeToolIntervalListResult
===========================

.. py:class:: ansys.stk.core.vgt.ITimeToolIntervalListResult

   object
   
   Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

.. py:currentmodule:: ITimeToolIntervalListResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolIntervalListResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolIntervalListResult.intervals`
              - A list of intervals.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolIntervalListResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalListResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalListResult.intervals
    :type: ITimeToolIntervalCollection

    A list of intervals.


