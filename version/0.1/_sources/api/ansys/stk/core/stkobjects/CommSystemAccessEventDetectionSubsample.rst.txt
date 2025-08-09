CommSystemAccessEventDetectionSubsample
=======================================

.. py:class:: ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICommSystemAccessEventDetection`

   Class defining a CommSystem access options.

.. py:currentmodule:: CommSystemAccessEventDetectionSubsample

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample.time_convergence`
              - Get or set the time convergence value for Access. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample.absolute_tolerance`
              - Get or set the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample.relative_tolerance`
              - An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CommSystemAccessEventDetectionSubsample


Property detail
---------------

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample.time_convergence
    :type: float

    Get or set the time convergence value for Access. Uses Time Dimension.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample.absolute_tolerance
    :type: float

    Get or set the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample.relative_tolerance
    :type: float

    An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.


