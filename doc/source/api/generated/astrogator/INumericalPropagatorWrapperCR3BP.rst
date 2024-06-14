INumericalPropagatorWrapperCR3BP
================================

.. py:class:: INumericalPropagatorWrapperCR3BP

   object
   
   General properties for three-body problem propagators.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_numerical_integrator`
              - Change the numerical integrator.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~propagator_functions`
            * - :py:meth:`~numerical_integrator`
            * - :py:meth:`~numerical_integrator_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import INumericalPropagatorWrapperCR3BP


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapperCR3BP.central_body_name
    :type: str

    Gets or sets the central body for Propagation.

.. py:property:: propagator_functions
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapperCR3BP.propagator_functions
    :type: "IAgVAPropagatorFunctionCollection"

    Get the list of propagator functions.

.. py:property:: numerical_integrator
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapperCR3BP.numerical_integrator
    :type: "IAgVANumericalIntegrator"

    Get the numerical integrator.

.. py:property:: numerical_integrator_type
    :canonical: ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapperCR3BP.numerical_integrator_type
    :type: "NUMERICAL_INTEGRATOR"

    Get the numerical integrator type.


Method detail
-------------






.. py:method:: set_numerical_integrator(self, integrator:"NUMERICAL_INTEGRATOR") -> None

    Change the numerical integrator.

    :Parameters:

    **integrator** : :obj:`~"NUMERICAL_INTEGRATOR"`

    :Returns:

        :obj:`~None`

