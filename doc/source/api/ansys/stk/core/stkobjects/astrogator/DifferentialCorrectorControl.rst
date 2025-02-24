DifferentialCorrectorControl
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Control Parameters for a Target Sequence.

.. py:currentmodule:: DifferentialCorrectorControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.final_value`
              - Get the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.last_update`
              - Get the amount by which the value of the independent variable changed during the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.initial_value`
              - Get the nominal value of the element selected as a parameter. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.perturbation`
              - Get the value to be used in calculating numerical derivatives. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.correction`
              - Get the amount by which the nominal value of the parameter should be corrected to achieve the selected goals. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.tolerance`
              - Get or set the smallest update to the parameter to be made before the targeter stops. Only used if the convergence criteria is set to 'Either equality constraints or last control parameter updates within tolerance'. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.max_step`
              - Get or set the maximum increment to make to the value of the parameter in any one step. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.scaling_method`
              - Allow better numerical behavior if the parameters have very different magnitudes. The same scaling method is applied to all parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.scaling_value`
              - Apply to the Specified Value scaling method. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.dimension`
              - Dimension of the constraint.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.values`
              - List of values of this independent variable at each iteration, including nominal run. Dimension depends on context.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DifferentialCorrectorControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: final_value
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.final_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: last_update
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.last_update
    :type: typing.Any

    Get the amount by which the value of the independent variable changed during the last targeter run.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: initial_value
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.initial_value
    :type: typing.Any

    Get the nominal value of the element selected as a parameter. Dimension depends on context.

.. py:property:: perturbation
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.perturbation
    :type: typing.Any

    Get the value to be used in calculating numerical derivatives. Dimension depends on context.

.. py:property:: correction
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.correction
    :type: typing.Any

    Get the amount by which the nominal value of the parameter should be corrected to achieve the selected goals. Dimension depends on context.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.tolerance
    :type: typing.Any

    Get or set the smallest update to the parameter to be made before the targeter stops. Only used if the convergence criteria is set to 'Either equality constraints or last control parameter updates within tolerance'. Dimension depends on context.

.. py:property:: max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.max_step
    :type: typing.Any

    Get or set the maximum increment to make to the value of the parameter in any one step. Dimension depends on context.

.. py:property:: scaling_method
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.scaling_method
    :type: DifferentialCorrectorScalingMethod

    Allow better numerical behavior if the parameters have very different magnitudes. The same scaling method is applied to all parameters.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.scaling_value
    :type: typing.Any

    Apply to the Specified Value scaling method. Dimension depends on context.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.dimension
    :type: str

    Dimension of the constraint.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.

.. py:property:: values
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl.values
    :type: list

    List of values of this independent variable at each iteration, including nominal run. Dimension depends on context.


