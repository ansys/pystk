CalculationOptions
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.CalculationOptions

   Class defining the calculation options for a procedure or phase.

.. py:currentmodule:: CalculationOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CalculationOptions.max_relative_motion_factor`
              - Gets or sets the maximum motion allowed between sampling points.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CalculationOptions.state_cache_time_interval`
              - Gets or sets the time interval used to store the state information.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CalculationOptions.time_resolution`
              - Gets or sets the tolerance for resolving time calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CalculationOptions.max_iterations`
              - Gets or sets the maximum number of iterations per time step Aviator will attempt.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CalculationOptions.max_bad_steps`
              - Gets or sets the maximum number of bad steps Aviator will allow before ceasing calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CalculationOptions.integrator_type`
              - Gets or sets the integrator type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CalculationOptions.integrator_type_string`
              - Gets or sets the integrator type as a string value. Use this for custom integrators.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import CalculationOptions


Property detail
---------------

.. py:property:: max_relative_motion_factor
    :canonical: ansys.stk.core.stkobjects.aviator.CalculationOptions.max_relative_motion_factor
    :type: float

    Gets or sets the maximum motion allowed between sampling points.

.. py:property:: state_cache_time_interval
    :canonical: ansys.stk.core.stkobjects.aviator.CalculationOptions.state_cache_time_interval
    :type: float

    Gets or sets the time interval used to store the state information.

.. py:property:: time_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.CalculationOptions.time_resolution
    :type: float

    Gets or sets the tolerance for resolving time calculations.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.aviator.CalculationOptions.max_iterations
    :type: int

    Gets or sets the maximum number of iterations per time step Aviator will attempt.

.. py:property:: max_bad_steps
    :canonical: ansys.stk.core.stkobjects.aviator.CalculationOptions.max_bad_steps
    :type: int

    Gets or sets the maximum number of bad steps Aviator will allow before ceasing calculation.

.. py:property:: integrator_type
    :canonical: ansys.stk.core.stkobjects.aviator.CalculationOptions.integrator_type
    :type: AviatorNumericalIntegrator

    Gets or sets the integrator type.

.. py:property:: integrator_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.CalculationOptions.integrator_type_string
    :type: str

    Gets or sets the integrator type as a string value. Use this for custom integrators.


