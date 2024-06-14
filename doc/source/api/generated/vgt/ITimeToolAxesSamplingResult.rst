ITimeToolAxesSamplingResult
===========================

.. py:class:: ITimeToolAxesSamplingResult

   object
   
   Contains tabulated orientations and angular velocities of axes created by Sample method.

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

    from ansys.stk.core.vgt import ITimeToolAxesSamplingResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: intervals
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingResult.intervals
    :type: "IAgCrdnAxesSamplingIntervalCollection"

    A collection of sampling intervals.


