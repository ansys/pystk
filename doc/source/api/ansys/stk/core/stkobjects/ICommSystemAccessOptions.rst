ICommSystemAccessOptions
========================

.. py:class:: ansys.stk.core.stkobjects.ICommSystemAccessOptions

   object
   
   Provide access to the CommSystem object access options.

.. py:currentmodule:: ICommSystemAccessOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessOptions.enable_light_time_delay`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessOptions.time_light_delay_convergence`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessOptions.aberration_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessOptions.event_detection_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessOptions.event_detection`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessOptions.sampling_method_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystemAccessOptions.sampling_method`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICommSystemAccessOptions


Property detail
---------------

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessOptions.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the computation.

.. py:property:: time_light_delay_convergence
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessOptions.time_light_delay_convergence
    :type: float

    Gets or sets the tolerance used when iterating to determine the light time delay. Uses Time Dimension.

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessOptions.aberration_type
    :type: ABERRATION_TYPE

    Gets or sets the model of aberration to be used in access computations.

.. py:property:: event_detection_type
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessOptions.event_detection_type
    :type: COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE

    Gets or sets the event detection type.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessOptions.event_detection
    :type: ICommSystemAccessEventDetection

    Gets the event detection algorithm.

.. py:property:: sampling_method_type
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessOptions.sampling_method_type
    :type: COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE

    Gets or sets the sampling method type.

.. py:property:: sampling_method
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessOptions.sampling_method
    :type: ICommSystemAccessSamplingMethod

    Gets the sampling method.


