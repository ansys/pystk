NumericalPropagatorWrapperCR3BP
===============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Numerical CR3BP Propagator.

.. py:currentmodule:: NumericalPropagatorWrapperCR3BP

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.set_numerical_integrator`
              - Change the numerical integrator.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.central_body_name`
              - Get or set the central body for Propagation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.propagator_functions`
              - Get the list of propagator functions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.numerical_integrator`
              - Get the numerical integrator.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.numerical_integrator_type`
              - Get the numerical integrator type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import NumericalPropagatorWrapperCR3BP


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.central_body_name
    :type: str

    Get or set the central body for Propagation.

.. py:property:: propagator_functions
    :canonical: ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.propagator_functions
    :type: PropagatorFunctionCollection

    Get the list of propagator functions.

.. py:property:: numerical_integrator
    :canonical: ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.numerical_integrator
    :type: INumericalIntegrator

    Get the numerical integrator.

.. py:property:: numerical_integrator_type
    :canonical: ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.numerical_integrator_type
    :type: NumericalIntegrator

    Get the numerical integrator type.


Method detail
-------------






.. py:method:: set_numerical_integrator(self, integrator: NumericalIntegrator) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP.set_numerical_integrator

    Change the numerical integrator.

    :Parameters:

        **integrator** : :obj:`~NumericalIntegrator`


    :Returns:

        :obj:`~None`

