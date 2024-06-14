IGaussJacksonIntegrator
=======================

.. py:class:: IGaussJacksonIntegrator

   object
   
   Properties for the Gauss-Jackson numerical integrator.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_single_step_integrator`
              - Change the stopping integrator.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initial_step`
            * - :py:meth:`~max_corrector_rel_err`
            * - :py:meth:`~corrector_mode`
            * - :py:meth:`~max_corrector_iterations`
            * - :py:meth:`~single_step_integrator`
            * - :py:meth:`~single_step_integrator_type`


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
    :type: "PREDICTOR_CORRECTOR"

    Gets or sets the Predictor Corrector scheme.

.. py:property:: max_corrector_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.max_corrector_iterations
    :type: int

    Gets or sets the maximum corrector iterations. Dimensionless.

.. py:property:: single_step_integrator
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.single_step_integrator
    :type: "IAgVANumericalIntegrator"

    Get the stopping integrator; a single-step integrator.

.. py:property:: single_step_integrator_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator.single_step_integrator_type
    :type: "NUMERICAL_INTEGRATOR"

    Get the stopping integrator type.


Method detail
-------------











.. py:method:: set_single_step_integrator(self, integrator:"NUMERICAL_INTEGRATOR") -> None

    Change the stopping integrator.

    :Parameters:

    **integrator** : :obj:`~"NUMERICAL_INTEGRATOR"`

    :Returns:

        :obj:`~None`

