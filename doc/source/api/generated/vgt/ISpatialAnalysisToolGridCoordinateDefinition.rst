ISpatialAnalysisToolGridCoordinateDefinition
============================================

.. py:class:: ISpatialAnalysisToolGridCoordinateDefinition

   object
   
   Define a set of coordinate values.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_grid_values_fixed_step`
              - Set grid values type to fixed step.
            * - :py:meth:`~set_grid_values_fixed_number_of_steps`
              - Do not use this method, as it is deprecated. Use SetGridValuesFixedNumberOfStepsEx.
            * - :py:meth:`~set_grid_values_custom`
              - Set grid values type to custom values.
            * - :py:meth:`~set_grid_values_fixed_number_of_steps_ex`
              - Set grid values type to fixed number of steps with min and max as IAgQuantity.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~method_type`
            * - :py:meth:`~grid_values_method`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolGridCoordinateDefinition


Property detail
---------------

.. py:property:: method_type
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridCoordinateDefinition.method_type
    :type: "CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE"

    Grid values method type.

.. py:property:: grid_values_method
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridCoordinateDefinition.grid_values_method
    :type: "IAgCrdnGridValuesMethod"

    Sets/Returns the grid values interface.


Method detail
-------------



.. py:method:: set_grid_values_fixed_step(self, min:float, max:float, includeMinMax:bool, refValue:float, fixedStep:float) -> "ISpatialAnalysisToolGridValuesFixedStep"

    Set grid values type to fixed step.

    :Parameters:

    **min** : :obj:`~float`
    **max** : :obj:`~float`
    **includeMinMax** : :obj:`~bool`
    **refValue** : :obj:`~float`
    **fixedStep** : :obj:`~float`

    :Returns:

        :obj:`~"ISpatialAnalysisToolGridValuesFixedStep"`

.. py:method:: set_grid_values_fixed_number_of_steps(self, min:float, max:float, numSteps:int) -> "ISpatialAnalysisToolGridValuesFixedNumberOfSteps"

    Do not use this method, as it is deprecated. Use SetGridValuesFixedNumberOfStepsEx.

    :Parameters:

    **min** : :obj:`~float`
    **max** : :obj:`~float`
    **numSteps** : :obj:`~int`

    :Returns:

        :obj:`~"ISpatialAnalysisToolGridValuesFixedNumberOfSteps"`

.. py:method:: set_grid_values_custom(self, values:list) -> "ISpatialAnalysisToolGridValuesCustom"

    Set grid values type to custom values.

    :Parameters:

    **values** : :obj:`~list`

    :Returns:

        :obj:`~"ISpatialAnalysisToolGridValuesCustom"`

.. py:method:: set_grid_values_fixed_number_of_steps_ex(self, min:"IQuantity", max:"IQuantity", numSteps:int) -> "ISpatialAnalysisToolGridValuesFixedNumberOfSteps"

    Set grid values type to fixed number of steps with min and max as IAgQuantity.

    :Parameters:

    **min** : :obj:`~"IQuantity"`
    **max** : :obj:`~"IQuantity"`
    **numSteps** : :obj:`~int`

    :Returns:

        :obj:`~"ISpatialAnalysisToolGridValuesFixedNumberOfSteps"`

