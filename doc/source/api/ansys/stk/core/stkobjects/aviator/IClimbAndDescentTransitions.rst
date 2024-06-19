IClimbAndDescentTransitions
===========================

.. py:class:: IClimbAndDescentTransitions

   object
   
   Interface used to access the Climb and Descent Transitions options found in the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_pull_up_g`
            * - :py:meth:`~max_push_over_g`
            * - :py:meth:`~maneuver_mode`
            * - :py:meth:`~ignore_fpa`
            * - :py:meth:`~maneuver_mode_helper`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IClimbAndDescentTransitions


Property detail
---------------

.. py:property:: max_pull_up_g
    :canonical: ansys.stk.core.stkobjects.aviator.IClimbAndDescentTransitions.max_pull_up_g
    :type: float

    Gets or sets the force normal to the velocity vector used to transition into a climb or to a transition out of a dive into the next flight segment.

.. py:property:: max_push_over_g
    :canonical: ansys.stk.core.stkobjects.aviator.IClimbAndDescentTransitions.max_push_over_g
    :type: float

    Gets or sets the force normal to the velocity vector used to transition into a descent or to a transition from a climb into the next flight segment.

.. py:property:: maneuver_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IClimbAndDescentTransitions.maneuver_mode
    :type: ACCEL_MANEUVER_MODE

    Gets or sets the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.

.. py:property:: ignore_fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IClimbAndDescentTransitions.ignore_fpa
    :type: bool

    Opt whether to ignore the flight path angle.

.. py:property:: maneuver_mode_helper
    :canonical: ansys.stk.core.stkobjects.aviator.IClimbAndDescentTransitions.maneuver_mode_helper
    :type: IAgAvtrAeroPropManeuverModeHelper

    Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.


