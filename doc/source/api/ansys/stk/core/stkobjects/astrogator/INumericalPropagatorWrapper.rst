INumericalPropagatorWrapper
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper

   object
   
   General properties for propagators.

.. py:currentmodule:: INumericalPropagatorWrapper

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.set_numerical_integrator`
              - Change the single step integrator.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.central_body_name`
              - Gets or sets the central body for Propagation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.use_variation_of_parameters`
              - Whether or not to use a variation of parameters(VOP) in universal variables formulation of the equations of motion; related to numerical integrator.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.use_regularized_time`
              - Whether or not to use regularized time; related to numerical integrator.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.regularized_time_exponent`
              - Gets or sets the exponent to use in regularized time; related to numerical integrator. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.regularized_time_steps_per_orbit`
              - Gets or sets the steps per orbit used in regularized time; related to numerical integrator. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.propagator_functions`
              - Get the list of propagator functions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.numerical_integrator`
              - Get the numerical integrator.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.numerical_integrator_type`
              - Get the single step integrator type.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import INumericalPropagatorWrapper


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.central_body_name
    :type: str

    Gets or sets the central body for Propagation.

.. py:property:: use_variation_of_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.use_variation_of_parameters
    :type: bool

    Whether or not to use a variation of parameters(VOP) in universal variables formulation of the equations of motion; related to numerical integrator.

.. py:property:: use_regularized_time
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.use_regularized_time
    :type: bool

    Whether or not to use regularized time; related to numerical integrator.

.. py:property:: regularized_time_exponent
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.regularized_time_exponent
    :type: float

    Gets or sets the exponent to use in regularized time; related to numerical integrator. Dimensionless.

.. py:property:: regularized_time_steps_per_orbit
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.regularized_time_steps_per_orbit
    :type: int

    Gets or sets the steps per orbit used in regularized time; related to numerical integrator. Dimensionless.

.. py:property:: propagator_functions
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.propagator_functions
    :type: IPropagatorFunctionCollection

    Get the list of propagator functions.

.. py:property:: numerical_integrator
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.numerical_integrator
    :type: INumericalIntegrator

    Get the numerical integrator.

.. py:property:: numerical_integrator_type
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.numerical_integrator_type
    :type: NUMERICAL_INTEGRATOR

    Get the single step integrator type.


Method detail
-------------














.. py:method:: set_numerical_integrator(self, integrator: NUMERICAL_INTEGRATOR) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper.set_numerical_integrator

    Change the single step integrator.

    :Parameters:

    **integrator** : :obj:`~NUMERICAL_INTEGRATOR`

    :Returns:

        :obj:`~None`

