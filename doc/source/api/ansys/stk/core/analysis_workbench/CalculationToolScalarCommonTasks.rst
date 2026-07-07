CalculationToolScalarCommonTasks
================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks

   Common tasks for Calc Scalars.

.. py:currentmodule:: CalculationToolScalarCommonTasks

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_array_for_calculation_scalar_array`
              - Each calc scalar in calcArrayVec is evaluated over the array of input times returning the results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_event_array_for_calculation_scalar_array`
              - Each calc scalar in calcArrayVec is evaluated over the array of times provided by refArray returning results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_for_calculation_scalar_array`
              - Each calc scalar in calcArrayVec is evaluated at epoch returning results as an array of elements, where each element is itself an array with two elements: 1. success (boolean) 2. value (double-precision).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_with_rate_array_for_calculation_scalar_array`
              - Each calc scalar in calcArrayVec is evaluated over the array of input times returning the results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_with_rate_event_array_for_calculation_scalar_array`
              - Each calc scalar in calcArrayVec is evaluated over the array of times provided by refArray returning results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_with_rate_for_calculation_scalar_array`
              - Each calc scalar in calcArrayVec is evaluated at epoch returning results as an array of elements, where each element is itself an array with three elements: 1. success (boolean) 2. value (double-precision) 3. value rate (double-precision).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarCommonTasks



Method detail
-------------

.. py:method:: quick_evaluate_array_for_calculation_scalar_array(self, times: list, calc_array_vec: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_array_for_calculation_scalar_array

    Each calc scalar in calcArrayVec is evaluated over the array of input times returning the results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...

    :Parameters:

        **times** : :obj:`~list`

        **calc_array_vec** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_event_array_for_calculation_scalar_array(self, ref_array: ITimeToolTimeArray, calc_array_vec: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_event_array_for_calculation_scalar_array

    Each calc scalar in calcArrayVec is evaluated over the array of times provided by refArray returning results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...

    :Parameters:

        **ref_array** : :obj:`~ITimeToolTimeArray`

        **calc_array_vec** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_for_calculation_scalar_array(self, epoch: typing.Any, calc_array_vec: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_for_calculation_scalar_array

    Each calc scalar in calcArrayVec is evaluated at epoch returning results as an array of elements, where each element is itself an array with two elements: 1. success (boolean) 2. value (double-precision).

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **calc_array_vec** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_with_rate_array_for_calculation_scalar_array(self, times: list, calc_array_vec: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_with_rate_array_for_calculation_scalar_array

    Each calc scalar in calcArrayVec is evaluated over the array of input times returning the results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...

    :Parameters:

        **times** : :obj:`~list`

        **calc_array_vec** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_with_rate_event_array_for_calculation_scalar_array(self, ref_array: ITimeToolTimeArray, calc_array_vec: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_with_rate_event_array_for_calculation_scalar_array

    Each calc scalar in calcArrayVec is evaluated over the array of times provided by refArray returning results as an array of elements for each time, each element being an array of results for each calc scalar, results being an array...

    :Parameters:

        **ref_array** : :obj:`~ITimeToolTimeArray`

        **calc_array_vec** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_with_rate_for_calculation_scalar_array(self, epoch: typing.Any, calc_array_vec: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCommonTasks.quick_evaluate_with_rate_for_calculation_scalar_array

    Each calc scalar in calcArrayVec is evaluated at epoch returning results as an array of elements, where each element is itself an array with three elements: 1. success (boolean) 2. value (double-precision) 3. value rate (double-precision).

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **calc_array_vec** : :obj:`~list`


    :Returns:

        :obj:`~list`

