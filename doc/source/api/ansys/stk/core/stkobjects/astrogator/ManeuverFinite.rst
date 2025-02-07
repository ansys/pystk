ManeuverFinite
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ManeuverFinite

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuver`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Finite Maneuver.

.. py:currentmodule:: ManeuverFinite

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinite.pressure_mode`
              - Get or set the pressure mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinite.thrust_efficiency`
              - Get or set the thrust efficiency value. Any number above zero is valid, with typical values around 0.98 to 1.02. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinite.thrust_efficiency_mode`
              - Thrust - the calculations that are effected by the thrust efficiency value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinite.propagator`
              - Get the propagator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ManeuverFinite


Property detail
---------------

.. py:property:: pressure_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinite.pressure_mode
    :type: PressureMode

    Get or set the pressure mode.

.. py:property:: thrust_efficiency
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinite.thrust_efficiency
    :type: float

    Get or set the thrust efficiency value. Any number above zero is valid, with typical values around 0.98 to 1.02. Dimensionless.

.. py:property:: thrust_efficiency_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinite.thrust_efficiency_mode
    :type: ThrustType

    Thrust - the calculations that are effected by the thrust efficiency value.

.. py:property:: propagator
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinite.propagator
    :type: ManeuverFinitePropagator

    Get the propagator.


