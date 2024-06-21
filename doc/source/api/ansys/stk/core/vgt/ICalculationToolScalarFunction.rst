ICalculationToolScalarFunction
==============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarFunction

   object
   
   Defined by performing the specified function on the input scalar or time instant.

.. py:currentmodule:: ICalculationToolScalarFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.use_scalar`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.input_scalar`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.input_time`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.input_unit`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.a`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.b`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.c`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.d`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.coefficients`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.selected_function`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.available_functions`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.inherit_dimension_from_input`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.output_dimension`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.output_unit`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.sampling`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFunction.convergence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarFunction


Property detail
---------------

.. py:property:: use_scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.use_scalar
    :type: bool

    Specify whether to use the input scalar calculation or the time elapsed from the input time instant. Set to true to use the scalar.

.. py:property:: input_scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.input_scalar
    :type: ICalculationToolScalar

    The input scalar calculation (used if UseScalar is true). The UseScalar property should be set to true before this property can be set.

.. py:property:: input_time
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.input_time
    :type: ITimeToolEvent

    The input time instant (used if UseScalar is false).

.. py:property:: input_unit
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.input_unit
    :type: str

    The input time unit to interpret input time.

.. py:property:: a
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.a
    :type: float

    The constant coefficient A.

.. py:property:: b
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.b
    :type: float

    The constant coefficient B.

.. py:property:: c
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.c
    :type: float

    The constant coefficient C.

.. py:property:: d
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.d
    :type: float

    The constant coefficient D.

.. py:property:: coefficients
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.coefficients
    :type: list

    The array of constant coefficients, whose dimension and units are determined by those of input and output.

.. py:property:: selected_function
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.selected_function
    :type: str

    The function which will use the input scalar or time instant in some combination with the constant coefficients A, B, C, D.

.. py:property:: available_functions
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.available_functions
    :type: list

    Get the available function names.

.. py:property:: inherit_dimension_from_input
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.inherit_dimension_from_input
    :type: bool

    Specify whether to inherit the output dimension from the input scalar or time instant.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.output_dimension
    :type: str

    The output dimension. Use any of STK supported dimensions. This value will be used if InheritDimensionFromInput is false. The InheritDimensionFromInput property should be set to false before this property can be fixed.

.. py:property:: output_unit
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.output_unit
    :type: str

    Specify a unit for the selected output dimension. This is not used for internal computations or reporting/graphing but is needed to unambiguously interpret units of associated coefficients.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction.convergence
    :type: IAnalysisWorkbenchConverge

    The Convergence definition, which uses time tolerance to determine when time of extremum is found.


