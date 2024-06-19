ITimeToolIntervalListResult
===========================

.. py:class:: ITimeToolIntervalListResult

   object
   
   Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

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
    :type: IAgCrdnIntervalCollection

    A list of intervals.


