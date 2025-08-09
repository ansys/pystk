IPOPTResult
===========

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPOPTResult

   Properties for objecvtive and constraints of a IPOPT profile.

.. py:currentmodule:: IPOPTResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.current_value`
              - Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.parent_name`
              - Object - the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.lower_bound`
              - Get or set the lower limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.upper_bound`
              - Get or set the upper limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.scaling_value`
              - Apply to the Specified Value scaling method. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.weight`
              - Get or set the factor by which the constraint error is to be multiplied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.goal`
              - Get or set the purpose of the element in the problem.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPOPTResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.current_value
    :type: typing.Any

    Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.parent_name
    :type: str

    Object - the name of the segment to which the parameter belongs.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.lower_bound
    :type: typing.Any

    Get or set the lower limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.upper_bound
    :type: typing.Any

    Get or set the upper limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.scaling_value
    :type: typing.Any

    Apply to the Specified Value scaling method. Dimension depends on context.

.. py:property:: weight
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.weight
    :type: float

    Get or set the factor by which the constraint error is to be multiplied.

.. py:property:: goal
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.goal
    :type: IPOPTGoal

    Get or set the purpose of the element in the problem.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResult.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.


