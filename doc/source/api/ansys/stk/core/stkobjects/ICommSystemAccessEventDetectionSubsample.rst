ICommSystemAccessEventDetectionSubsample
========================================

.. py:class:: ansys.stk.core.stkobjects.ICommSystemAccessEventDetectionSubsample

   object
   
   Provide access to the properties an access sub-sample event detection algorithm.

.. py:currentmodule:: ICommSystemAccessEventDetectionSubsample

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessEventDetectionSubsample.time_convergence`
              - Gets or sets the time convergence value for Access. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessEventDetectionSubsample.absolute_tolerance`
              - Gets or sets the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessEventDetectionSubsample.relative_tolerance`
              - An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICommSystemAccessEventDetectionSubsample


Property detail
---------------

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessEventDetectionSubsample.time_convergence
    :type: float

    Gets or sets the time convergence value for Access. Uses Time Dimension.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessEventDetectionSubsample.absolute_tolerance
    :type: float

    Gets or sets the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessEventDetectionSubsample.relative_tolerance
    :type: float

    An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.


