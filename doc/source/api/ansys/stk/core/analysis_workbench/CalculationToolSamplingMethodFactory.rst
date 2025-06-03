CalculationToolSamplingMethodFactory
====================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory

   The factory creates sampling method components.

.. py:currentmodule:: CalculationToolSamplingMethodFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory.create_fixed_step`
              - Create a fixed time step sampling definition.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory.create_curvature_tolerance`
              - Create a curvature tolerance sampling definition. Curvature tolerance uses changes in slope between samples.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory.create_relative_tolerance`
              - Create a relative tolerance sampling definition. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolSamplingMethodFactory



Method detail
-------------

.. py:method:: create_fixed_step(self, fixed_step: float) -> ICalculationToolSamplingMethod
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory.create_fixed_step

    Create a fixed time step sampling definition.

    :Parameters:

        **fixed_step** : :obj:`~float`


    :Returns:

        :obj:`~ICalculationToolSamplingMethod`

.. py:method:: create_curvature_tolerance(self, curvature_tolerance: float) -> ICalculationToolSamplingMethod
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory.create_curvature_tolerance

    Create a curvature tolerance sampling definition. Curvature tolerance uses changes in slope between samples.

    :Parameters:

        **curvature_tolerance** : :obj:`~float`


    :Returns:

        :obj:`~ICalculationToolSamplingMethod`

.. py:method:: create_relative_tolerance(self, relative_tolerance: float) -> ICalculationToolSamplingMethod
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory.create_relative_tolerance

    Create a relative tolerance sampling definition. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples.

    :Parameters:

        **relative_tolerance** : :obj:`~float`


    :Returns:

        :obj:`~ICalculationToolSamplingMethod`

