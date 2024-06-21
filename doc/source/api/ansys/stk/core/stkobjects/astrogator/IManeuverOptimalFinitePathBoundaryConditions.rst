IManeuverOptimalFinitePathBoundaryConditions
============================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions

   object
   
   Properties of path boundary conditions for optimal finite maneuver.

.. py:currentmodule:: IManeuverOptimalFinitePathBoundaryConditions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.compute_from_initial_guess`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.a`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.h`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.k`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.p`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.q`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.l`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.lower_bound_azimuth`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.upper_bound_azimuth`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.lower_bound_elevation`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.upper_bound_elevation`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuverOptimalFinitePathBoundaryConditions


Property detail
---------------

.. py:property:: compute_from_initial_guess
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.compute_from_initial_guess
    :type: bool

    Compute path boundary conditions from initial guess.

.. py:property:: a
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.a
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element a.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.h
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element h.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.k
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element k.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.p
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element p.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.q
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element q.

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.l
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element L.

.. py:property:: lower_bound_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.lower_bound_azimuth
    :type: float

    Thrust direction azimuth lower bound along the path.

.. py:property:: upper_bound_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.upper_bound_azimuth
    :type: float

    Thrust direction azimuth upper bound along the path.

.. py:property:: lower_bound_elevation
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.lower_bound_elevation
    :type: float

    Thrust direction elevation lower bound along the path.

.. py:property:: upper_bound_elevation
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.upper_bound_elevation
    :type: float

    Thrust direction elevation upper bound along the path.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


