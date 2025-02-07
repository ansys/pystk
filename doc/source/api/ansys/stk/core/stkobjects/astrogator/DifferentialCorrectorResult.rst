DifferentialCorrectorResult
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Differential Corrector equality constraints.

.. py:currentmodule:: DifferentialCorrectorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.desired_value`
              - Get or set the desired value. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.current_value`
              - Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.parent_name`
              - Object - the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.difference`
              - Get the difference between the current and desired value for this dependent variable. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.tolerance`
              - How close the targeter should come to the desired value before stopping. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.scaling_method`
              - Allow better numerical behavior if the constraints have very different magnitudes. The same scaling method is applied to all constraints.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.scaling_value`
              - Apply to the Specified Value scaling method. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.weight`
              - Get or set the factor by which the constraint error is to be multiplied. This is used to emphasize/de-emphasize the importance of one constraint relative to the others. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.dimension`
              - Get the dimension of the values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.values`
              - List of values of this dependent variable at each iteration, including nominal run. Dimension depends on context.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DifferentialCorrectorResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.desired_value
    :type: typing.Any

    Get or set the desired value. Dimension depends on context.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.current_value
    :type: typing.Any

    Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.parent_name
    :type: str

    Object - the name of the segment to which the parameter belongs.

.. py:property:: difference
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.difference
    :type: typing.Any

    Get the difference between the current and desired value for this dependent variable. Dimension depends on context.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.tolerance
    :type: typing.Any

    How close the targeter should come to the desired value before stopping. Dimension depends on context.

.. py:property:: scaling_method
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.scaling_method
    :type: DifferentialCorrectorScalingMethod

    Allow better numerical behavior if the constraints have very different magnitudes. The same scaling method is applied to all constraints.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.scaling_value
    :type: typing.Any

    Apply to the Specified Value scaling method. Dimension depends on context.

.. py:property:: weight
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.weight
    :type: float

    Get or set the factor by which the constraint error is to be multiplied. This is used to emphasize/de-emphasize the importance of one constraint relative to the others. Dimensionless.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.dimension
    :type: str

    Get the dimension of the values.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.

.. py:property:: values
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult.values
    :type: list

    List of values of this dependent variable at each iteration, including nominal run. Dimension depends on context.


