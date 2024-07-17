SpatialAnalysisToolGridCoordinateDefinition
===========================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition

   Bases: 

   Define a set of coordinate values.

.. py:currentmodule:: SpatialAnalysisToolGridCoordinateDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_step`
              - Set grid values type to fixed step.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_number_of_steps`
              - Do not use this method, as it is deprecated. Use SetGridValuesFixedNumberOfStepsEx.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_custom`
              - Set grid values type to custom values.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_number_of_steps_ex`
              - Set grid values type to fixed number of steps with min and max as IAgQuantity.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.method_type`
              - Grid values method type.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.grid_values_method`
              - Sets/Returns the grid values interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolGridCoordinateDefinition


Property detail
---------------

.. py:property:: method_type
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.method_type
    :type: CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE

    Grid values method type.

.. py:property:: grid_values_method
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.grid_values_method
    :type: ISpatialAnalysisToolGridValuesMethod

    Sets/Returns the grid values interface.


Method detail
-------------



.. py:method:: set_grid_values_fixed_step(self, min: float, max: float, includeMinMax: bool, refValue: float, fixedStep: float) -> SpatialAnalysisToolGridValuesFixedStep
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_step

    Set grid values type to fixed step.

    :Parameters:

    **min** : :obj:`~float`
    **max** : :obj:`~float`
    **includeMinMax** : :obj:`~bool`
    **refValue** : :obj:`~float`
    **fixedStep** : :obj:`~float`

    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesFixedStep`

.. py:method:: set_grid_values_fixed_number_of_steps(self, min: float, max: float, numSteps: int) -> SpatialAnalysisToolGridValuesFixedNumberOfSteps
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_number_of_steps

    Do not use this method, as it is deprecated. Use SetGridValuesFixedNumberOfStepsEx.

    :Parameters:

    **min** : :obj:`~float`
    **max** : :obj:`~float`
    **numSteps** : :obj:`~int`

    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesFixedNumberOfSteps`

.. py:method:: set_grid_values_custom(self, values: list) -> SpatialAnalysisToolGridValuesCustom
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_custom

    Set grid values type to custom values.

    :Parameters:

    **values** : :obj:`~list`

    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesCustom`

.. py:method:: set_grid_values_fixed_number_of_steps_ex(self, min: Quantity, max: Quantity, numSteps: int) -> SpatialAnalysisToolGridValuesFixedNumberOfSteps
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_number_of_steps_ex

    Set grid values type to fixed number of steps with min and max as IAgQuantity.

    :Parameters:

    **min** : :obj:`~Quantity`
    **max** : :obj:`~Quantity`
    **numSteps** : :obj:`~int`

    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesFixedNumberOfSteps`

