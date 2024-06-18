ITimeToolPointSamplingResult
============================

.. py:class:: ITimeToolPointSamplingResult

   object
   
   Contains tabulated positions and velocities of a point created by Sample method.

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

    from ansys.stk.core.vgt import ITimeToolPointSamplingResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolPointSamplingResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.vgt.ITimeToolPointSamplingResult.intervals
    :type: "IAgCrdnPointSamplingIntervalCollection"

    A collection of sampling intervals.


