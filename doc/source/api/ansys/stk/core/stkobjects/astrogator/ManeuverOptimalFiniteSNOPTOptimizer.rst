ManeuverOptimalFiniteSNOPTOptimizer
===================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer

   Properties of SNOPT Optimizer options for optimal finite maneuver.

.. py:currentmodule:: ManeuverOptimalFiniteSNOPTOptimizer

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.objective`
              - Objective.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.max_major_iterations`
              - Gets or sets the maximum number of major iterations allowed.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.tolerance_on_major_feasibility`
              - Specifies how accurately the nonlinear constraints should be satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.tolerance_on_major_optimality`
              - Specifies the final accuracy of the dual variables.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.max_minor_iterations`
              - Gets or sets the maximum number of iterations for the QP subproblem allowed during a single major iteration.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.tolerance_on_minor_feasibility`
              - Gets or sets the tolerance which the QP subproblem must meet before being considered feasible.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.options_filename`
              - If used, the associated SNOPT specifications file may define any of the various SNOPT options. Options in the file that conflict with options specified elsewhere will take precedence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.use_console_monitor`
              - Whether to use the out-of-process console monitor for the optimizer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.allow_internal_primal_infeasibility_measure_normalization`
              - Whether to allow internal normalization of the primal infeasibility measure.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.snopt_scaling`
              - SNOPT scaling option.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ManeuverOptimalFiniteSNOPTOptimizer


Property detail
---------------

.. py:property:: objective
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.objective
    :type: OPTIMAL_FINITE_SNOPT_OBJECTIVE

    Objective.

.. py:property:: max_major_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.max_major_iterations
    :type: int

    Gets or sets the maximum number of major iterations allowed.

.. py:property:: tolerance_on_major_feasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.tolerance_on_major_feasibility
    :type: float

    Specifies how accurately the nonlinear constraints should be satisfied.

.. py:property:: tolerance_on_major_optimality
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.tolerance_on_major_optimality
    :type: float

    Specifies the final accuracy of the dual variables.

.. py:property:: max_minor_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.max_minor_iterations
    :type: int

    Gets or sets the maximum number of iterations for the QP subproblem allowed during a single major iteration.

.. py:property:: tolerance_on_minor_feasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.tolerance_on_minor_feasibility
    :type: float

    Gets or sets the tolerance which the QP subproblem must meet before being considered feasible.

.. py:property:: options_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.options_filename
    :type: str

    If used, the associated SNOPT specifications file may define any of the various SNOPT options. Options in the file that conflict with options specified elsewhere will take precedence.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.

.. py:property:: use_console_monitor
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.use_console_monitor
    :type: bool

    Whether to use the out-of-process console monitor for the optimizer.

.. py:property:: allow_internal_primal_infeasibility_measure_normalization
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.allow_internal_primal_infeasibility_measure_normalization
    :type: bool

    Whether to allow internal normalization of the primal infeasibility measure.

.. py:property:: snopt_scaling
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer.snopt_scaling
    :type: OPTIMAL_FINITE_SNOPT_SCALING

    SNOPT scaling option.


