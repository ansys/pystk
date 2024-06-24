ITimeToolAxesSamplingResult
===========================

.. py:class:: ansys.stk.core.vgt.ITimeToolAxesSamplingResult

   object
   
   Contains tabulated orientations and angular velocities of axes created by Sample method.

.. py:currentmodule:: ITimeToolAxesSamplingResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolAxesSamplingResult.is_valid`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolAxesSamplingResult.intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolAxesSamplingResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingResult.intervals
    :type: ITimeToolAxesSamplingIntervalCollection

    A collection of sampling intervals.


