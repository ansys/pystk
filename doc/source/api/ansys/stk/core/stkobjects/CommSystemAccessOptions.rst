CommSystemAccessOptions
=======================

.. py:class:: ansys.stk.core.stkobjects.CommSystemAccessOptions

   Bases: 

   Class defining a CommSystem access options.

.. py:currentmodule:: CommSystemAccessOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.enable_light_time_delay`
              - Specify whether to take light time delay into account in the computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.time_light_delay_convergence`
              - Gets or sets the tolerance used when iterating to determine the light time delay. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.aberration_type`
              - Gets or sets the model of aberration to be used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection_type`
              - Gets or sets the event detection type.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection`
              - Gets the event detection algorithm.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method_type`
              - Gets or sets the sampling method type.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method`
              - Gets the sampling method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CommSystemAccessOptions


Property detail
---------------

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the computation.

.. py:property:: time_light_delay_convergence
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.time_light_delay_convergence
    :type: float

    Gets or sets the tolerance used when iterating to determine the light time delay. Uses Time Dimension.

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.aberration_type
    :type: ABERRATION_TYPE

    Gets or sets the model of aberration to be used in access computations.

.. py:property:: event_detection_type
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection_type
    :type: COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE

    Gets or sets the event detection type.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.event_detection
    :type: ICommSystemAccessEventDetection

    Gets the event detection algorithm.

.. py:property:: sampling_method_type
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method_type
    :type: COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE

    Gets or sets the sampling method type.

.. py:property:: sampling_method
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessOptions.sampling_method
    :type: ICommSystemAccessSamplingMethod

    Gets the sampling method.


