AsTriggerCondition
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Constraint.

.. py:currentmodule:: AsTriggerCondition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.copy_calculation_object_to_clipboard`
              - Copy calculation object to clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.paste_calculation_object_from_clipboard`
              - Replace calculation object with instance in clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.criteria`
              - Gets or sets the criteria to be applied to the desired value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.calculation_object`
              - Gets or sets the calculation object to perform calculation to evaluate condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.calculation_object_name`
              - Gets or sets the name of the calculation object to perform calculation to evaluate condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.value`
              - Gets or sets the value to satisfy the condition. Dimension depends on CalcObject.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.tolerance`
              - How closely the test parameter must approximate the desired value for the constraint. Dimension depends on CalcObject.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.use_absolute_value`
              - Whether or not to take the absolute value of the calculation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AsTriggerCondition


Property detail
---------------

.. py:property:: criteria
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.criteria
    :type: Criteria

    Gets or sets the criteria to be applied to the desired value.

.. py:property:: calculation_object
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.calculation_object
    :type: IComponentInfo

    Gets or sets the calculation object to perform calculation to evaluate condition.

.. py:property:: calculation_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.calculation_object_name
    :type: str

    Gets or sets the name of the calculation object to perform calculation to evaluate condition.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.value
    :type: typing.Any

    Gets or sets the value to satisfy the condition. Dimension depends on CalcObject.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.tolerance
    :type: typing.Any

    How closely the test parameter must approximate the desired value for the constraint. Dimension depends on CalcObject.

.. py:property:: use_absolute_value
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.use_absolute_value
    :type: bool

    Whether or not to take the absolute value of the calculation.


Method detail
-------------













.. py:method:: copy_calculation_object_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.copy_calculation_object_to_clipboard

    Copy calculation object to clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_calculation_object_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.AsTriggerCondition.paste_calculation_object_from_clipboard

    Replace calculation object with instance in clipboard.

    :Returns:

        :obj:`~None`

