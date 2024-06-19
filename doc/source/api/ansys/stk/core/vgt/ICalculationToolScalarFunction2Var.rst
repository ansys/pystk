ICalculationToolScalarFunction2Var
==================================

.. py:class:: ICalculationToolScalarFunction2Var

   object
   
   Defined by performing a function(x,y) on two scalar arguments.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~x`
            * - :py:meth:`~unit_x`
            * - :py:meth:`~a`
            * - :py:meth:`~y`
            * - :py:meth:`~unit_y`
            * - :py:meth:`~b`
            * - :py:meth:`~c`
            * - :py:meth:`~output_dimension_inheritance`
            * - :py:meth:`~output_dimension`
            * - :py:meth:`~available_functions`
            * - :py:meth:`~selected_function`
            * - :py:meth:`~output_unit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarFunction2Var


Property detail
---------------

.. py:property:: x
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.x
    :type: IAgCrdnCalcScalar

    The scalar argument X.

.. py:property:: unit_x
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.unit_x
    :type: str

    The unit used to interpret numerical values of scalar argument X.

.. py:property:: a
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.a
    :type: float

    The constant coefficient A.

.. py:property:: y
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.y
    :type: IAgCrdnCalcScalar

    The scalar argument Y.

.. py:property:: unit_y
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.unit_y
    :type: str

    The unit used to interpret numerical values of scalar argument Y.

.. py:property:: b
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.b
    :type: float

    The constant coefficient B.

.. py:property:: c
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.c
    :type: float

    The constant coefficient C.

.. py:property:: output_dimension_inheritance
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.output_dimension_inheritance
    :type: CRDN_DIMENSION_INHERITANCE

    Specifies whether the output dimension is inherited or explicitly specified using OutputDimension.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.output_dimension
    :type: str

    The output dimension. Use any of STK supported dimensions. This value will be used if OutputDimensionInheritance is false.

.. py:property:: available_functions
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.available_functions
    :type: list

    The available functions. A function(x,y) uses some combination of two scalar arguments x and y as well as one to three constant coefficients a, b, c.

.. py:property:: selected_function
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.selected_function
    :type: str

    The selected function.

.. py:property:: output_unit
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFunction2Var.output_unit
    :type: str

    The unit for the selected dimension. The unit is not used for internal computations or reporting/graphing but is needed to unambiguously interpret units of associated coefficients.


