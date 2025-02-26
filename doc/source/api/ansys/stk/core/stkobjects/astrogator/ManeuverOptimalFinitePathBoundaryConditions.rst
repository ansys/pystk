ManeuverOptimalFinitePathBoundaryConditions
===========================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions

   Properties of path boundary conditions for optimal finite maneuver.

.. py:currentmodule:: ManeuverOptimalFinitePathBoundaryConditions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.compute_from_initial_guess`
              - Compute path boundary conditions from initial guess.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.a`
              - Bound limits for element a.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.h`
              - Bound limits for element h.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.k`
              - Bound limits for element k.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.p`
              - Bound limits for element p.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.q`
              - Bound limits for element q.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.l`
              - Bound limits for element L.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.lower_bound_azimuth`
              - Thrust direction azimuth lower bound along the path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.upper_bound_azimuth`
              - Thrust direction azimuth upper bound along the path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.lower_bound_elevation`
              - Thrust direction elevation lower bound along the path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.upper_bound_elevation`
              - Thrust direction elevation upper bound along the path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.provide_runtime_type_info`
              - Return the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ManeuverOptimalFinitePathBoundaryConditions


Property detail
---------------

.. py:property:: compute_from_initial_guess
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.compute_from_initial_guess
    :type: bool

    Compute path boundary conditions from initial guess.

.. py:property:: a
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.a
    :type: ManeuverOptimalFiniteBounds

    Bound limits for element a.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.h
    :type: ManeuverOptimalFiniteBounds

    Bound limits for element h.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.k
    :type: ManeuverOptimalFiniteBounds

    Bound limits for element k.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.p
    :type: ManeuverOptimalFiniteBounds

    Bound limits for element p.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.q
    :type: ManeuverOptimalFiniteBounds

    Bound limits for element q.

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.l
    :type: ManeuverOptimalFiniteBounds

    Bound limits for element L.

.. py:property:: lower_bound_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.lower_bound_azimuth
    :type: float

    Thrust direction azimuth lower bound along the path.

.. py:property:: upper_bound_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.upper_bound_azimuth
    :type: float

    Thrust direction azimuth upper bound along the path.

.. py:property:: lower_bound_elevation
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.lower_bound_elevation
    :type: float

    Thrust direction elevation lower bound along the path.

.. py:property:: upper_bound_elevation
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.upper_bound_elevation
    :type: float

    Thrust direction elevation upper bound along the path.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions.provide_runtime_type_info
    :type: RuntimeTypeInfo

    Return the IAgRuntimeTypeInfo interface to access properties at runtime.


