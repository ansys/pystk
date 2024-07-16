ClimbAndDescentTransitions
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions

   Bases: 

   Class defining the climb and descent transition options for an Acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: ClimbAndDescentTransitions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_pull_up_g`
              - Gets or sets the force normal to the velocity vector used to transition into a climb or to a transition out of a dive into the next flight segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_push_over_g`
              - Gets or sets the force normal to the velocity vector used to transition into a descent or to a transition from a climb into the next flight segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode`
              - Gets or sets the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.ignore_fpa`
              - Opt whether to ignore the flight path angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode_helper`
              - Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ClimbAndDescentTransitions


Property detail
---------------

.. py:property:: max_pull_up_g
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_pull_up_g
    :type: float

    Gets or sets the force normal to the velocity vector used to transition into a climb or to a transition out of a dive into the next flight segment.

.. py:property:: max_push_over_g
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_push_over_g
    :type: float

    Gets or sets the force normal to the velocity vector used to transition into a descent or to a transition from a climb into the next flight segment.

.. py:property:: maneuver_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode
    :type: ACCEL_MANEUVER_MODE

    Gets or sets the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.

.. py:property:: ignore_fpa
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.ignore_fpa
    :type: bool

    Opt whether to ignore the flight path angle.

.. py:property:: maneuver_mode_helper
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode_helper
    :type: IAeroPropManeuverModeHelper

    Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.


