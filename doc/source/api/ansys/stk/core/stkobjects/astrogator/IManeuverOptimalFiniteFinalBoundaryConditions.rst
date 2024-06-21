IManeuverOptimalFiniteFinalBoundaryConditions
=============================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions

   object
   
   Properties of final boundary conditions for optimal finite maneuver.

.. py:currentmodule:: IManeuverOptimalFiniteFinalBoundaryConditions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.set_from_final_guess`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.a`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.h`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.k`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.p`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.q`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.l`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.lower_delta_final_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.upper_delta_final_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuverOptimalFiniteFinalBoundaryConditions


Property detail
---------------

.. py:property:: set_from_final_guess
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.set_from_final_guess
    :type: bool

    Set initial boundary conditions from initial guess.

.. py:property:: a
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.a
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element a.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.h
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element h.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.k
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element k.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.p
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element p.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.q
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element q.

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.l
    :type: IManeuverOptimalFiniteBounds

    Bound limits for element L.

.. py:property:: lower_delta_final_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.lower_delta_final_time
    :type: float

    Lower delta for final time.

.. py:property:: upper_delta_final_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.upper_delta_final_time
    :type: float

    Upper delta for final time.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


