IDifferentialCorrectorResult
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult

   object
   
   Properties for equality constraints of a differential corrector profile.

.. py:currentmodule:: IDifferentialCorrectorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.desired_value`
              - Gets or sets the desired value. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.current_value`
              - Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.parent_name`
              - Object - the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.difference`
              - Get the difference between the current and desired value for this dependent variable. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.tolerance`
              - How close the targeter should come to the desired value before stopping. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.scaling_method`
              - Allows better numerical behavior if the constraints have very different magnitudes. The same scaling method is applied to all constraints.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.scaling_value`
              - Applies to the Specified Value scaling method. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.weight`
              - Gets or sets the factor by which the constraint error is to be multiplied. This is used to emphasize/de-emphasize the importance of one constraint relative to the others. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.dimension`
              - Get the dimension of the values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.custom_display_unit`
              - Gets or sets the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.values`
              - List of values of this dependent variable at each iteration, including nominal run. Dimension depends on context.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDifferentialCorrectorResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.desired_value
    :type: typing.Any

    Gets or sets the desired value. Dimension depends on context.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.current_value
    :type: typing.Any

    Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.parent_name
    :type: str

    Object - the name of the segment to which the parameter belongs.

.. py:property:: difference
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.difference
    :type: typing.Any

    Get the difference between the current and desired value for this dependent variable. Dimension depends on context.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.tolerance
    :type: typing.Any

    How close the targeter should come to the desired value before stopping. Dimension depends on context.

.. py:property:: scaling_method
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.scaling_method
    :type: DIFFERENTIAL_CORRECTOR_SCALING_METHOD

    Allows better numerical behavior if the constraints have very different magnitudes. The same scaling method is applied to all constraints.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.scaling_value
    :type: typing.Any

    Applies to the Specified Value scaling method. Dimension depends on context.

.. py:property:: weight
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.weight
    :type: float

    Gets or sets the factor by which the constraint error is to be multiplied. This is used to emphasize/de-emphasize the importance of one constraint relative to the others. Dimensionless.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.dimension
    :type: str

    Get the dimension of the values.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.

.. py:property:: values
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult.values
    :type: list

    List of values of this dependent variable at each iteration, including nominal run. Dimension depends on context.


