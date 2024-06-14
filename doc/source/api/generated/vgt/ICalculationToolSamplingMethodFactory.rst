ICalculationToolSamplingMethodFactory
=====================================

.. py:class:: ICalculationToolSamplingMethodFactory

   object
   
   The factory creates sampling method components.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create_fixed_step`
              - Create a fixed time step sampling definition.
            * - :py:meth:`~create_curvature_tolerance`
              - Create a curvature tolerance sampling definition. Curvature tolerance uses changes in slope between samples.
            * - :py:meth:`~create_relative_tolerance`
              - Create a relative tolerance sampling definition. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolSamplingMethodFactory



Method detail
-------------

.. py:method:: create_fixed_step(self, fixedStep:float) -> "ICalculationToolSamplingMethod"

    Create a fixed time step sampling definition.

    :Parameters:

    **fixedStep** : :obj:`~float`

    :Returns:

        :obj:`~"ICalculationToolSamplingMethod"`

.. py:method:: create_curvature_tolerance(self, curvatureTolerance:float) -> "ICalculationToolSamplingMethod"

    Create a curvature tolerance sampling definition. Curvature tolerance uses changes in slope between samples.

    :Parameters:

    **curvatureTolerance** : :obj:`~float`

    :Returns:

        :obj:`~"ICalculationToolSamplingMethod"`

.. py:method:: create_relative_tolerance(self, relativeTolerance:float) -> "ICalculationToolSamplingMethod"

    Create a relative tolerance sampling definition. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples.

    :Parameters:

    **relativeTolerance** : :obj:`~float`

    :Returns:

        :obj:`~"ICalculationToolSamplingMethod"`

