CalculationToolScalarFunction
=============================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by performing the specified function on the input scalar or time instant.

.. py:currentmodule:: CalculationToolScalarFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.available_functions`
              - Get the available function names.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_a`
              - The constant coefficient A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_b`
              - The constant coefficient B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_c`
              - The constant coefficient C.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_d`
              - The constant coefficient D.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficients`
              - The array of constant coefficients, whose dimension and units are determined by those of input and output.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.convergence`
              - The Convergence definition, which uses time tolerance to determine when time of extremum is found.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.inherit_dimension_from_input`
              - Specify whether to inherit the output dimension from the input scalar or time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.input_scalar`
              - The input scalar calculation (used if UseScalar is true). The UseScalar property should be set to true before this property can be set.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.input_time`
              - The input time instant (used if UseScalar is false).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.input_time_units`
              - The input time unit to interpret input time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.output_dimension`
              - The output dimension. Use any of STK supported dimensions. This value will be used if InheritDimensionFromInput is false. The InheritDimensionFromInput property should be set to false before this property can be fixed.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.output_units`
              - Specify a unit for the selected output dimension. This is not used for internal computations or reporting/graphing but is needed to unambiguously interpret units of associated coefficients.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.sampling`
              - The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.selected_function`
              - The function which will use the input scalar or time instant in some combination with the constant coefficients A, B, C, D.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.use_calculation_scalar`
              - Specify whether to use the input scalar calculation or the time elapsed from the input time instant. Set to true to use the scalar.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarFunction


Property detail
---------------

.. py:property:: available_functions
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.available_functions
    :type: list

    Get the available function names.

.. py:property:: coefficient_a
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_a
    :type: float

    The constant coefficient A.

.. py:property:: coefficient_b
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_b
    :type: float

    The constant coefficient B.

.. py:property:: coefficient_c
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_c
    :type: float

    The constant coefficient C.

.. py:property:: coefficient_d
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficient_d
    :type: float

    The constant coefficient D.

.. py:property:: coefficients
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.coefficients
    :type: list

    The array of constant coefficients, whose dimension and units are determined by those of input and output.

.. py:property:: convergence
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.convergence
    :type: IAnalysisWorkbenchConvergence

    The Convergence definition, which uses time tolerance to determine when time of extremum is found.

.. py:property:: inherit_dimension_from_input
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.inherit_dimension_from_input
    :type: bool

    Specify whether to inherit the output dimension from the input scalar or time instant.

.. py:property:: input_scalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.input_scalar
    :type: ICalculationToolScalar

    The input scalar calculation (used if UseScalar is true). The UseScalar property should be set to true before this property can be set.

.. py:property:: input_time
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.input_time
    :type: ITimeToolInstant

    The input time instant (used if UseScalar is false).

.. py:property:: input_time_units
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.input_time_units
    :type: str

    The input time unit to interpret input time.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.output_dimension
    :type: str

    The output dimension. Use any of STK supported dimensions. This value will be used if InheritDimensionFromInput is false. The InheritDimensionFromInput property should be set to false before this property can be fixed.

.. py:property:: output_units
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.output_units
    :type: str

    Specify a unit for the selected output dimension. This is not used for internal computations or reporting/graphing but is needed to unambiguously interpret units of associated coefficients.

.. py:property:: sampling
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: selected_function
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.selected_function
    :type: str

    The function which will use the input scalar or time instant in some combination with the constant coefficients A, B, C, D.

.. py:property:: use_calculation_scalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFunction.use_calculation_scalar
    :type: bool

    Specify whether to use the input scalar calculation or the time elapsed from the input time instant. Set to true to use the scalar.


