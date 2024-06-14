IManeuverOptimalFiniteInitialBoundaryConditions
===============================================

.. py:class:: IManeuverOptimalFiniteInitialBoundaryConditions

   object
   
   Properties of initial boundary conditions for optimal finite maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_from_initial_guess`
            * - :py:meth:`~a`
            * - :py:meth:`~h`
            * - :py:meth:`~k`
            * - :py:meth:`~p`
            * - :py:meth:`~q`
            * - :py:meth:`~l`
            * - :py:meth:`~provide_runtime_type_info`


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
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element a.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.h
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element h.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.k
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element k.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.p
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element p.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.q
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element q.

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.l
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element L.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions.provide_runtime_type_info
    :type: "IAgRuntimeTypeInfo"

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


