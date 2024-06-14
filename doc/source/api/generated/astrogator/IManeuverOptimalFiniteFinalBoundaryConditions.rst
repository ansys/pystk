IManeuverOptimalFiniteFinalBoundaryConditions
=============================================

.. py:class:: IManeuverOptimalFiniteFinalBoundaryConditions

   object
   
   Properties of final boundary conditions for optimal finite maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_from_final_guess`
            * - :py:meth:`~a`
            * - :py:meth:`~h`
            * - :py:meth:`~k`
            * - :py:meth:`~p`
            * - :py:meth:`~q`
            * - :py:meth:`~l`
            * - :py:meth:`~lower_delta_final_time`
            * - :py:meth:`~upper_delta_final_time`
            * - :py:meth:`~provide_runtime_type_info`


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
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element a.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.h
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element h.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.k
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element k.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.p
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element p.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.q
    :type: "IAgVAManeuverOptimalFiniteBounds"

    Bound limits for element q.

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions.l
    :type: "IAgVAManeuverOptimalFiniteBounds"

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
    :type: "IAgRuntimeTypeInfo"

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


