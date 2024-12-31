CalculationToolScalarFunctionOf2Variables
=========================================

.. py:class:: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Defined by performing a function(x,y) on two scalar arguments.

.. py:currentmodule:: CalculationToolScalarFunctionOf2Variables

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.x`
              - The scalar argument X.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.units_x`
              - The unit used to interpret numerical values of scalar argument X.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.coefficient_a`
              - The constant coefficient A.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.y`
              - The scalar argument Y.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.units_y`
              - The unit used to interpret numerical values of scalar argument Y.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.coefficient_b`
              - The constant coefficient B.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.coefficient_c`
              - The constant coefficient C.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.output_dimension_inheritance`
              - Specifies whether the output dimension is inherited or explicitly specified using OutputDimension.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.output_dimension`
              - The output dimension. Use any of STK supported dimensions. This value will be used if OutputDimensionInheritance is false.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.available_functions`
              - The available functions. A function(x,y) uses some combination of two scalar arguments x and y as well as one to three constant coefficients a, b, c.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.selected_function`
              - The selected function.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.output_units`
              - The unit for the selected dimension. The unit is not used for internal computations or reporting/graphing but is needed to unambiguously interpret units of associated coefficients.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolScalarFunctionOf2Variables


Property detail
---------------

.. py:property:: x
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.x
    :type: ICalculationToolScalar

    The scalar argument X.

.. py:property:: units_x
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.units_x
    :type: str

    The unit used to interpret numerical values of scalar argument X.

.. py:property:: coefficient_a
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.coefficient_a
    :type: float

    The constant coefficient A.

.. py:property:: y
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.y
    :type: ICalculationToolScalar

    The scalar argument Y.

.. py:property:: units_y
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.units_y
    :type: str

    The unit used to interpret numerical values of scalar argument Y.

.. py:property:: coefficient_b
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.coefficient_b
    :type: float

    The constant coefficient B.

.. py:property:: coefficient_c
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.coefficient_c
    :type: float

    The constant coefficient C.

.. py:property:: output_dimension_inheritance
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.output_dimension_inheritance
    :type: InheritDimensionType

    Specifies whether the output dimension is inherited or explicitly specified using OutputDimension.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.output_dimension
    :type: str

    The output dimension. Use any of STK supported dimensions. This value will be used if OutputDimensionInheritance is false.

.. py:property:: available_functions
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.available_functions
    :type: list

    The available functions. A function(x,y) uses some combination of two scalar arguments x and y as well as one to three constant coefficients a, b, c.

.. py:property:: selected_function
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.selected_function
    :type: str

    The selected function.

.. py:property:: output_units
    :canonical: ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables.output_units
    :type: str

    The unit for the selected dimension. The unit is not used for internal computations or reporting/graphing but is needed to unambiguously interpret units of associated coefficients.


