GaussJacksonIntegrator
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalIntegrator`

   Gauss-Jackson Numerical Integrator.

.. py:currentmodule:: GaussJacksonIntegrator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.set_single_step_integrator`
              - Change the stopping integrator.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.initial_step`
              - Get or set the initial step. Uses time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.max_corrector_relative_err`
              - Get or set the maximum relative error between corrector iterations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.corrector_mode`
              - Get or set the Predictor Corrector scheme.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.max_corrector_iterations`
              - Get or set the maximum corrector iterations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.single_step_integrator`
              - Get the stopping integrator; a single-step integrator.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.single_step_integrator_type`
              - Get the stopping integrator type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GaussJacksonIntegrator


Property detail
---------------

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.initial_step
    :type: float

    Get or set the initial step. Uses time dimension.

.. py:property:: max_corrector_relative_err
    :canonical: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.max_corrector_relative_err
    :type: float

    Get or set the maximum relative error between corrector iterations. Dimensionless.

.. py:property:: corrector_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.corrector_mode
    :type: PredictorCorrector

    Get or set the Predictor Corrector scheme.

.. py:property:: max_corrector_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.max_corrector_iterations
    :type: int

    Get or set the maximum corrector iterations. Dimensionless.

.. py:property:: single_step_integrator
    :canonical: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.single_step_integrator
    :type: INumericalIntegrator

    Get the stopping integrator; a single-step integrator.

.. py:property:: single_step_integrator_type
    :canonical: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.single_step_integrator_type
    :type: NumericalIntegrator

    Get the stopping integrator type.


Method detail
-------------











.. py:method:: set_single_step_integrator(self, integrator: NumericalIntegrator) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator.set_single_step_integrator

    Change the stopping integrator.

    :Parameters:

        **integrator** : :obj:`~NumericalIntegrator`


    :Returns:

        :obj:`~None`

