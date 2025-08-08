LandingStandardInstrumentApproach
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach

   Class defining the standard instrument approach options for a landing procedure.

.. py:currentmodule:: LandingStandardInstrumentApproach

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.approach_altitude`
              - Get or set the aircraft's altitude at the Initial Approach Fix Range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.approach_fix_range`
              - Get or set the range from the reference point of the runway at which the aircraft begins its landing approach.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.approach_fix_range_mode`
              - Get or set the reference point on the runway for the Approach Fix Range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.glideslope`
              - Get or set the angle from the horizontal on which the aircraft descends to touchdown.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.level_off_mode`
              - Get or set the level off mode. This is only used when the must level off option is on.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.runway_altitude_offset`
              - Get or set the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.touch_and_go`
              - Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.



Examples
--------

Add and configure a landing procedure

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a landing procedure
    landing = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_LANDING)

    # Get the runway heading options
    headingOptions = landing.runway_heading_options
    # Land from the low end
    headingOptions.runway_mode = RunwayHighLowEnd.LOW_END

    # Use a standard instrument approach
    landing.approach_mode = ApproachMode.STANDARD_INSTRUMENT_APPROACH
    # Get the options for a standard instrument approach
    sia = landing.mode_as_standard_instrument_approach
    # Change the approach altitude
    sia.approach_altitude = 1000
    # Change the glideslope
    sia.glideslope = 4
    # Offset the runway altitude
    sia.runway_altitude_offset = 10
    # Use the terrain as an altitude reference for the runway
    sia.use_runway_terrain = True


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import LandingStandardInstrumentApproach


Property detail
---------------

.. py:property:: approach_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.approach_altitude
    :type: float

    Get or set the aircraft's altitude at the Initial Approach Fix Range.

.. py:property:: approach_fix_range
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.approach_fix_range
    :type: float

    Get or set the range from the reference point of the runway at which the aircraft begins its landing approach.

.. py:property:: approach_fix_range_mode
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.approach_fix_range_mode
    :type: LandingApproachFixRangeMode

    Get or set the reference point on the runway for the Approach Fix Range.

.. py:property:: glideslope
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.glideslope
    :type: typing.Any

    Get or set the angle from the horizontal on which the aircraft descends to touchdown.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.level_off_mode
    :type: AltitudeConstraintManeuverMode

    Get or set the level off mode. This is only used when the must level off option is on.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.runway_altitude_offset
    :type: float

    Get or set the altitude offset above the ground level.

.. py:property:: touch_and_go
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.touch_and_go
    :type: bool

    Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.


