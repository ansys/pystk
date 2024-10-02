TimeToolSamplingResult
======================

.. py:class:: ansys.stk.core.vgt.TimeToolSamplingResult

   Contains tabulated orientations and angular velocities of axes created by Sample method.

.. py:currentmodule:: TimeToolSamplingResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSamplingResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSamplingResult.intervals`
              - A collection of sampling intervals.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolSamplingResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.TimeToolSamplingResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.vgt.TimeToolSamplingResult.intervals
    :type: TimeToolAxesSamplingIntervalCollection

    A collection of sampling intervals.


