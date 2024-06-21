ICalculationOptions
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.ICalculationOptions

   object
   
   Interface used to access the calculation options for a procedure or phase.

.. py:currentmodule:: ICalculationOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICalculationOptions.max_rel_motion_factor`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICalculationOptions.state_cache_time_interval`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICalculationOptions.time_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICalculationOptions.max_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICalculationOptions.max_bad_steps`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICalculationOptions.integrator_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICalculationOptions.integrator_type_string`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ICalculationOptions


Property detail
---------------

.. py:property:: max_rel_motion_factor
    :canonical: ansys.stk.core.stkobjects.aviator.ICalculationOptions.max_rel_motion_factor
    :type: float

    Gets or sets the maximum motion allowed between sampling points.

.. py:property:: state_cache_time_interval
    :canonical: ansys.stk.core.stkobjects.aviator.ICalculationOptions.state_cache_time_interval
    :type: float

    Gets or sets the time interval used to store the state information.

.. py:property:: time_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.ICalculationOptions.time_resolution
    :type: float

    Gets or sets the tolerance for resolving time calculations.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.aviator.ICalculationOptions.max_iterations
    :type: int

    Gets or sets the maximum number of iterations per time step Aviator will attempt.

.. py:property:: max_bad_steps
    :canonical: ansys.stk.core.stkobjects.aviator.ICalculationOptions.max_bad_steps
    :type: int

    Gets or sets the maximum number of bad steps Aviator will allow before ceasing calculation.

.. py:property:: integrator_type
    :canonical: ansys.stk.core.stkobjects.aviator.ICalculationOptions.integrator_type
    :type: NUMERICAL_INTEGRATOR

    Gets or sets the integrator type.

.. py:property:: integrator_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.ICalculationOptions.integrator_type_string
    :type: str

    Gets or sets the integrator type as a string value. Use this for custom integrators.


