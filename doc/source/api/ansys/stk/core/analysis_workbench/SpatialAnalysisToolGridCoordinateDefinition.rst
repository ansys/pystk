SpatialAnalysisToolGridCoordinateDefinition
===========================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition

   Define a set of coordinate values.

.. py:currentmodule:: SpatialAnalysisToolGridCoordinateDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_fixed_step`
              - Set grid values type to fixed step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_number_of_steps`
              - Do not use this method, as it is deprecated. Use SetGridValuesFixedNumberOfStepsEx.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_custom`
              - Set grid values type to custom values.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_fixed_number_of_steps`
              - Set grid values type to fixed number of steps with min and max as Quantity.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.method_type`
              - Grid values method type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.grid_values_method`
              - Get or set the grid values interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        SpatialAnalysisToolGridCoordinateDefinition,
    )


Property detail
---------------

.. py:property:: method_type
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.method_type
    :type: GridValuesMethodType

    Grid values method type.

.. py:property:: grid_values_method
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.grid_values_method
    :type: ISpatialAnalysisToolGridValuesMethod

    Get or set the grid values interface.


Method detail
-------------



.. py:method:: set_fixed_step(self, min: float, max: float, include_min_max: bool, ref_value: float, fixed_step: float) -> SpatialAnalysisToolGridValuesFixedStep
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_fixed_step

    Set grid values type to fixed step.

    :Parameters:

        **min** : :obj:`~float`

        **max** : :obj:`~float`

        **include_min_max** : :obj:`~bool`

        **ref_value** : :obj:`~float`

        **fixed_step** : :obj:`~float`


    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesFixedStep`

.. py:method:: set_grid_values_fixed_number_of_steps(self, min: float, max: float, num_steps: int) -> SpatialAnalysisToolGridValuesFixedNumberOfSteps
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_grid_values_fixed_number_of_steps

    Do not use this method, as it is deprecated. Use SetGridValuesFixedNumberOfStepsEx.

    :Parameters:

        **min** : :obj:`~float`

        **max** : :obj:`~float`

        **num_steps** : :obj:`~int`


    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesFixedNumberOfSteps`

.. py:method:: set_custom(self, values: list) -> SpatialAnalysisToolGridValuesCustom
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_custom

    Set grid values type to custom values.

    :Parameters:

        **values** : :obj:`~list`


    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesCustom`

.. py:method:: set_fixed_number_of_steps(self, min: Quantity, max: Quantity, num_steps: int) -> SpatialAnalysisToolGridValuesFixedNumberOfSteps
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition.set_fixed_number_of_steps

    Set grid values type to fixed number of steps with min and max as Quantity.

    :Parameters:

        **min** : :obj:`~Quantity`

        **max** : :obj:`~Quantity`

        **num_steps** : :obj:`~int`


    :Returns:

        :obj:`~SpatialAnalysisToolGridValuesFixedNumberOfSteps`

