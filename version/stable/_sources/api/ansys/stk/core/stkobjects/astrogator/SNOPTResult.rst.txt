SNOPTResult
===========

.. py:class:: ansys.stk.core.stkobjects.astrogator.SNOPTResult

   Properties for objecvtive and constraints of a SNOPT profile.

.. py:currentmodule:: SNOPTResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.current_value`
              - Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.parent_name`
              - Object - the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.lower_bound`
              - Get or set the lower limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.upper_bound`
              - Get or set the upper limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.scaling_value`
              - Apply to the Specified Value scaling method. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.weight`
              - Get or set the factor by which the constraint error is to be multiplied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.goal`
              - Get or set the purpose of the element in the problem.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SNOPTResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.current_value
    :type: typing.Any

    Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.parent_name
    :type: str

    Object - the name of the segment to which the parameter belongs.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.lower_bound
    :type: typing.Any

    Get or set the lower limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.upper_bound
    :type: typing.Any

    Get or set the upper limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.scaling_value
    :type: typing.Any

    Apply to the Specified Value scaling method. Dimension depends on context.

.. py:property:: weight
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.weight
    :type: float

    Get or set the factor by which the constraint error is to be multiplied.

.. py:property:: goal
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.goal
    :type: SNOPTGoal

    Get or set the purpose of the element in the problem.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResult.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.


