ILandingEnterDownwindPattern
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern

   object
   
   The interface used to access the options for a Downwind Pattern approach mode for a landing procedure. The approach mode must be set to Downwind Pattern to access this interface.

.. py:currentmodule:: ILandingEnterDownwindPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.approach_fix_range`
              - Gets or sets the range from the reference point of the runway at which the aircraft begins its landing approach.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.approach_fix_range_mode`
              - Gets or sets the reference point on the runway for the Approach Fix Range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.abeam_distance`
              - Gets or sets the distance from the runway that the aircraft will fly the parallel leg of the landing pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.abeam_altitude`
              - Gets or sets the altitude at which the aircraft will fly the parallel leg of the landing pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.final_turn`
              - Gets or sets the direction of the turn that the aircraft will make when it lines up over the runway to land.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.glideslope`
              - Gets or sets the angle from the horizontal on which the aircraft descends to touchdown.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.runway_altitude_offset`
              - Gets or sets the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.touch_and_go`
              - Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ILandingEnterDownwindPattern


Property detail
---------------

.. py:property:: approach_fix_range
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.approach_fix_range
    :type: float

    Gets or sets the range from the reference point of the runway at which the aircraft begins its landing approach.

.. py:property:: approach_fix_range_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.approach_fix_range_mode
    :type: LANDING_APPROACH_FIX_RANGE_MODE

    Gets or sets the reference point on the runway for the Approach Fix Range.

.. py:property:: abeam_distance
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.abeam_distance
    :type: float

    Gets or sets the distance from the runway that the aircraft will fly the parallel leg of the landing pattern.

.. py:property:: abeam_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.abeam_altitude
    :type: float

    Gets or sets the altitude at which the aircraft will fly the parallel leg of the landing pattern.

.. py:property:: final_turn
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.final_turn
    :type: NAVIGATOR_TURN_DIRECTION

    Gets or sets the direction of the turn that the aircraft will make when it lines up over the runway to land.

.. py:property:: glideslope
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.glideslope
    :type: typing.Any

    Gets or sets the angle from the horizontal on which the aircraft descends to touchdown.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: touch_and_go
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingEnterDownwindPattern.touch_and_go
    :type: bool

    Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.


