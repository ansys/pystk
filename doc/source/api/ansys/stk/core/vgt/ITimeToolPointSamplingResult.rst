ITimeToolPointSamplingResult
============================

.. py:class:: ansys.stk.core.vgt.ITimeToolPointSamplingResult

   object
   
   Contains tabulated positions and velocities of a point created by Sample method.

.. py:currentmodule:: ITimeToolPointSamplingResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolPointSamplingResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolPointSamplingResult.intervals`
              - A collection of sampling intervals.


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
    :type: ITimeToolPointSamplingIntervalCollection

    A collection of sampling intervals.


