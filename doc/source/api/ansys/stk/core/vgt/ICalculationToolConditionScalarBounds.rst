ICalculationToolConditionScalarBounds
=====================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds

   object
   
   Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

.. py:currentmodule:: ICalculationToolConditionScalarBounds

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_minimum`
              - Get the minimum bound value from the condition. Call SetMinimum to apply changes.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_minimum`
              - Set the minimum bound value for the condition.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_maximum`
              - Get the maximum bound value from the condition. Call SetMaximum to apply changes.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_maximum`
              - Set the maximum bound value for the condition.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set`
              - Set the min/max bounds. Throws an exception if the minimum is greater than maximum.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_minimum_unitless`
              - Get the unitless minimum bound value from the condition. Call SetMinimum to apply changes.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_minimum_unitless`
              - Set the unitless minimum bound value for the condition.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_maximum_unitless`
              - Get the unitless maximum bound value from the condition. Call SetMaximum to apply changes.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_maximum_unitless`
              - Set the unitless maximum bound value for the condition.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_unitless`
              - Set the unitless min/max bounds. Throws an exception if the minimum is greater than maximum.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.scalar`
              - Get the scalar calculation from the condition.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.operation`
              - Get the operation from the condition that determines how the bounds are considered. The operation can be set to define satisfaction when the scalar is above minimum, below maximum, between minimum and maximum or outside minimum and maximum.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionScalarBounds


Property detail
---------------

.. py:property:: scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.scalar
    :type: ICalculationToolScalar

    Get the scalar calculation from the condition.

.. py:property:: operation
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.operation
    :type: CRDN_CONDITION_THRESHOLD_OPTION

    Get the operation from the condition that determines how the bounds are considered. The operation can be set to define satisfaction when the scalar is above minimum, below maximum, between minimum and maximum or outside minimum and maximum.


Method detail
-------------





.. py:method:: get_minimum(self) -> IQuantity
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_minimum

    Get the minimum bound value from the condition. Call SetMinimum to apply changes.

    :Returns:

        :obj:`~IQuantity`

.. py:method:: set_minimum(self, value: IQuantity) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_minimum

    Set the minimum bound value for the condition.

    :Parameters:

    **value** : :obj:`~IQuantity`

    :Returns:

        :obj:`~None`

.. py:method:: get_maximum(self) -> IQuantity
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_maximum

    Get the maximum bound value from the condition. Call SetMaximum to apply changes.

    :Returns:

        :obj:`~IQuantity`

.. py:method:: set_maximum(self, value: IQuantity) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_maximum

    Set the maximum bound value for the condition.

    :Parameters:

    **value** : :obj:`~IQuantity`

    :Returns:

        :obj:`~None`

.. py:method:: set(self, min: IQuantity, max: IQuantity) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set

    Set the min/max bounds. Throws an exception if the minimum is greater than maximum.

    :Parameters:

    **min** : :obj:`~IQuantity`
    **max** : :obj:`~IQuantity`

    :Returns:

        :obj:`~None`

.. py:method:: get_minimum_unitless(self) -> float
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_minimum_unitless

    Get the unitless minimum bound value from the condition. Call SetMinimum to apply changes.

    :Returns:

        :obj:`~float`

.. py:method:: set_minimum_unitless(self, value: float) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_minimum_unitless

    Set the unitless minimum bound value for the condition.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: get_maximum_unitless(self) -> float
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.get_maximum_unitless

    Get the unitless maximum bound value from the condition. Call SetMaximum to apply changes.

    :Returns:

        :obj:`~float`

.. py:method:: set_maximum_unitless(self, value: float) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_maximum_unitless

    Set the unitless maximum bound value for the condition.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: set_unitless(self, min: float, max: float) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionScalarBounds.set_unitless

    Set the unitless min/max bounds. Throws an exception if the minimum is greater than maximum.

    :Parameters:

    **min** : :obj:`~float`
    **max** : :obj:`~float`

    :Returns:

        :obj:`~None`

