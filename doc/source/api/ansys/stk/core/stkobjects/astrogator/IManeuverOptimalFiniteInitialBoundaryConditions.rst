IManeuverOptimalFiniteInitialBoundaryConditions
===============================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions

   object
   
   Properties of initial boundary conditions for optimal finite maneuver.

.. py:currentmodule:: IManeuverOptimalFiniteInitialBoundaryConditions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.set_from_initial_guess`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.a`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.h`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.k`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.p`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.q`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.l`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuverOptimalFiniteInitialBoundaryConditions


Property detail
---------------

.. py:property:: set_from_initial_guess
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.set_from_initial_guess
    :type: bool

    Set initial boundary conditions from initial guess.

.. py:property:: a
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.a
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element a.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.h
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element h.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.k
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element k.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.p
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element p.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.q
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element q.

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.l
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element L.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


