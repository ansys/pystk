IAsTriggerCondition
===================

.. py:class:: IAsTriggerCondition

   object
   
   Properties for a constraint - an additional condition to be met to satisfy a stopping condition.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~copy_calc_object_to_clipboard`
              - Copy calculation object to clipboard.
            * - :py:meth:`~paste_calc_object_from_clipboard`
              - Replace calculation object with instance in clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~criteria`
            * - :py:meth:`~calc_object`
            * - :py:meth:`~calc_object_name`
            * - :py:meth:`~value`
            * - :py:meth:`~tolerance`
            * - :py:meth:`~use_absolute_value`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAsTriggerCondition


Property detail
---------------

.. py:property:: criteria
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.criteria
    :type: CRITERIA

    Gets or sets the criteria to be applied to the desired value.

.. py:property:: calc_object
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.calc_object
    :type: IAgComponentInfo

    Gets or sets the calculation object to perform calculation to evaluate condition.

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.calc_object_name
    :type: str

    Gets or sets the name of the calculation object to perform calculation to evaluate condition.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.value
    :type: typing.Any

    Gets or sets the value to satisfy the condition. Dimension depends on CalcObject.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.tolerance
    :type: typing.Any

    How closely the test parameter must approximate the desired value for the constraint. Dimension depends on CalcObject.

.. py:property:: use_absolute_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.use_absolute_value
    :type: bool

    Whether or not to take the absolute value of the calculation.


Method detail
-------------













.. py:method:: copy_calc_object_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.copy_calc_object_to_clipboard

    Copy calculation object to clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_calc_object_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition.paste_calc_object_from_clipboard

    Replace calculation object with instance in clipboard.

    :Returns:

        :obj:`~None`

