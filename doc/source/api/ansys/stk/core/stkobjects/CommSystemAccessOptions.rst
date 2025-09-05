CommSystemAccessOptions
=======================

.. py:class:: ansys.stk.core.stkobjects.CommSystemAccessOptions

   Class defining a CommSystem access options.

.. py:currentmodule:: CommSystemAccessOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.aberration_type`
              - Get or set the model of aberration to be used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.enable_light_time_delay`
              - Specify whether to take light time delay into account in the computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection`
              - Get the event detection algorithm.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection_type`
              - Get or set the event detection type.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method`
              - Get the sampling method.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method_type`
              - Get or set the sampling method type.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.time_light_delay_convergence`
              - Get or set the tolerance used when iterating to determine the light time delay. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CommSystemAccessOptions


Property detail
---------------

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.aberration_type
    :type: AberrationType

    Get or set the model of aberration to be used in access computations.

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the computation.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection
    :type: ICommSystemAccessEventDetection

    Get the event detection algorithm.

.. py:property:: event_detection_type
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection_type
    :type: CommSystemAccessEventDetectionType

    Get or set the event detection type.

.. py:property:: sampling_method
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method
    :type: ICommSystemAccessSamplingMethod

    Get the sampling method.

.. py:property:: sampling_method_type
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method_type
    :type: CommSystemAccessSamplingMethodType

    Get or set the sampling method type.

.. py:property:: time_light_delay_convergence
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.time_light_delay_convergence
    :type: float

    Get or set the tolerance used when iterating to determine the light time delay. Uses Time Dimension.


