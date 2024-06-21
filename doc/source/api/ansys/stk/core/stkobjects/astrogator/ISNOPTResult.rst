ISNOPTResult
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ISNOPTResult

   object
   
   Properties for objecvtive and constraints of a SNOPT profile.

.. py:currentmodule:: ISNOPTResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.enable`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.current_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.parent_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.lower_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.upper_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.scaling_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.weight`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.goal`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.use_custom_display_unit`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult.custom_display_unit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISNOPTResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.current_value
    :type: typing.Any

    Get the value achieved for this dependent variable in the last targeter run. Dimension depends on context.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.parent_name
    :type: str

    Object - the name of the segment to which the parameter belongs.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.lower_bound
    :type: typing.Any

    Gets or sets the lower limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.upper_bound
    :type: typing.Any

    Gets or sets the upper limit achievable by this quantity in the optimizer's iteration history. Dimension depends on context.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.scaling_value
    :type: typing.Any

    Applies to the Specified Value scaling method. Dimension depends on context.

.. py:property:: weight
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.weight
    :type: float

    Gets or sets the factor by which the constraint error is to be multiplied.

.. py:property:: goal
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.goal
    :type: SNOPT_GOAL

    Gets or sets the purpose of the element in the problem.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTResult.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.


