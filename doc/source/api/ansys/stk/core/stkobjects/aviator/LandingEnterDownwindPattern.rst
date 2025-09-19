LandingEnterDownwindPattern
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern

   Class defining the enter downwind pattern options for a landing procedure.

.. py:currentmodule:: LandingEnterDownwindPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.abeam_altitude`
              - Get or set the altitude at which the aircraft will fly the parallel leg of the landing pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.abeam_distance`
              - Get or set the distance from the runway that the aircraft will fly the parallel leg of the landing pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.approach_fix_range`
              - Get or set the range from the reference point of the runway at which the aircraft begins its landing approach.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.approach_fix_range_mode`
              - Get or set the reference point on the runway for the Approach Fix Range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.final_turn`
              - Get or set the direction of the turn that the aircraft will make when it lines up over the runway to land.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.glideslope`
              - Get or set the angle from the horizontal on which the aircraft descends to touchdown.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.runway_altitude_offset`
              - Get or set the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.touch_and_go`
              - Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import LandingEnterDownwindPattern


Property detail
---------------

.. py:property:: abeam_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.abeam_altitude
    :type: float

    Get or set the altitude at which the aircraft will fly the parallel leg of the landing pattern.

.. py:property:: abeam_distance
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.abeam_distance
    :type: float

    Get or set the distance from the runway that the aircraft will fly the parallel leg of the landing pattern.

.. py:property:: approach_fix_range
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.approach_fix_range
    :type: float

    Get or set the range from the reference point of the runway at which the aircraft begins its landing approach.

.. py:property:: approach_fix_range_mode
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.approach_fix_range_mode
    :type: LandingApproachFixRangeMode

    Get or set the reference point on the runway for the Approach Fix Range.

.. py:property:: final_turn
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.final_turn
    :type: NavigatorTurnDirection

    Get or set the direction of the turn that the aircraft will make when it lines up over the runway to land.

.. py:property:: glideslope
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.glideslope
    :type: typing.Any

    Get or set the angle from the horizontal on which the aircraft descends to touchdown.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.runway_altitude_offset
    :type: float

    Get or set the altitude offset above the ground level.

.. py:property:: touch_and_go
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.touch_and_go
    :type: bool

    Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.


