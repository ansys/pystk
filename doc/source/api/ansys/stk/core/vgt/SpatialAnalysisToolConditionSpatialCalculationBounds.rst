SpatialAnalysisToolConditionSpatialCalculationBounds
====================================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   An volume from calc volume interface.

.. py:currentmodule:: SpatialAnalysisToolConditionSpatialCalculationBounds

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.get_minimum`
              - Get the minimum bound value from the bounds. Call SetMinimum to apply changes.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.set_minimum`
              - Set the minimum bound value for the bounds.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.get_maximum`
              - Get the maximum bound value from the bounds. Call SetMaximum to apply changes.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.set_maximum`
              - Set the maximum bound value for the condition.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.set`
              - Set the min/max bounds. Throws an exception if the minimum is greater than maximum.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.operation`
              - Get the operation from the condition that determines how the bounds are considered. The operation can be set to define satisfaction when the scalar is above minimum, below maximum, between minimum and maximum or outside minimum and maximum.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.spatial_calculation`
              - Get the volume calc from the bounds.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolConditionSpatialCalculationBounds


Property detail
---------------

.. py:property:: operation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.operation
    :type: ConditionThresholdType

    Get the operation from the condition that determines how the bounds are considered. The operation can be set to define satisfaction when the scalar is above minimum, below maximum, between minimum and maximum or outside minimum and maximum.

.. py:property:: spatial_calculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.spatial_calculation
    :type: ISpatialAnalysisToolSpatialCalculation

    Get the volume calc from the bounds.


Method detail
-------------





.. py:method:: get_minimum(self) -> Quantity
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.get_minimum

    Get the minimum bound value from the bounds. Call SetMinimum to apply changes.

    :Returns:

        :obj:`~Quantity`

.. py:method:: set_minimum(self, value: Quantity) -> None
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.set_minimum

    Set the minimum bound value for the bounds.

    :Parameters:

    **value** : :obj:`~Quantity`

    :Returns:

        :obj:`~None`

.. py:method:: get_maximum(self) -> Quantity
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.get_maximum

    Get the maximum bound value from the bounds. Call SetMaximum to apply changes.

    :Returns:

        :obj:`~Quantity`

.. py:method:: set_maximum(self, value: Quantity) -> None
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.set_maximum

    Set the maximum bound value for the condition.

    :Parameters:

    **value** : :obj:`~Quantity`

    :Returns:

        :obj:`~None`

.. py:method:: set(self, min: Quantity, max: Quantity) -> None
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds.set

    Set the min/max bounds. Throws an exception if the minimum is greater than maximum.

    :Parameters:

    **min** : :obj:`~Quantity`
    **max** : :obj:`~Quantity`

    :Returns:

        :obj:`~None`

