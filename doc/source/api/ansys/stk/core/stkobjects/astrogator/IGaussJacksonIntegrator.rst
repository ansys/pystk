IGaussJacksonIntegrator
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator

   object
   
   Properties for the Gauss-Jackson numerical integrator.

.. py:currentmodule:: IGaussJacksonIntegrator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.set_single_step_integrator`
              - Change the stopping integrator.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.initial_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.max_corrector_rel_err`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.corrector_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.max_corrector_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.single_step_integrator`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.single_step_integrator_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGaussJacksonIntegrator


Property detail
---------------

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.initial_step
    :type: float

    Gets or sets the initial step. Uses time dimension.

.. py:property:: max_corrector_rel_err
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.max_corrector_rel_err
    :type: float

    Gets or sets the maximum relative error between corrector iterations. Dimensionless.

.. py:property:: corrector_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.corrector_mode
    :type: PREDICTOR_CORRECTOR

    Gets or sets the Predictor Corrector scheme.

.. py:property:: max_corrector_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.max_corrector_iterations
    :type: int

    Gets or sets the maximum corrector iterations. Dimensionless.

.. py:property:: single_step_integrator
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.single_step_integrator
    :type: INumericalIntegrator

    Get the stopping integrator; a single-step integrator.

.. py:property:: single_step_integrator_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.single_step_integrator_type
    :type: NUMERICAL_INTEGRATOR

    Get the stopping integrator type.


Method detail
-------------











.. py:method:: set_single_step_integrator(self, integrator: NUMERICAL_INTEGRATOR) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.set_single_step_integrator

    Change the stopping integrator.

    :Parameters:

    **integrator** : :obj:`~NUMERICAL_INTEGRATOR`

    :Returns:

        :obj:`~None`

