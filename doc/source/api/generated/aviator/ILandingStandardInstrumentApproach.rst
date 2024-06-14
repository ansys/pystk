ILandingStandardInstrumentApproach
==================================

.. py:class:: ILandingStandardInstrumentApproach

   object
   
   The interface used to access the options for a Standard Instrument Approach mode for a landing procedure. The approach mode must be set to Standard Instrument Approach to access this interface.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~approach_altitude`
            * - :py:meth:`~level_off_mode`
            * - :py:meth:`~approach_fix_range`
            * - :py:meth:`~approach_fix_range_mode`
            * - :py:meth:`~glideslope`
            * - :py:meth:`~runway_altitude_offset`
            * - :py:meth:`~use_runway_terrain`
            * - :py:meth:`~touch_and_go`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ILandingStandardInstrumentApproach


Property detail
---------------

.. py:property:: approach_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.approach_altitude
    :type: float

    Gets or sets the aircraft's altitude at the Initial Approach Fix Range.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.level_off_mode
    :type: "ALTITUDE_CONSTRAINT_MANEUVER_MODE"

    Gets or sets the level off mode. This is only used when the must level off option is on.

.. py:property:: approach_fix_range
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.approach_fix_range
    :type: float

    Gets or sets the range from the reference point of the runway at which the aircraft begins its landing approach.

.. py:property:: approach_fix_range_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.approach_fix_range_mode
    :type: "LANDING_APPROACH_FIX_RANGE_MODE"

    Gets or sets the reference point on the runway for the Approach Fix Range.

.. py:property:: glideslope
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.glideslope
    :type: typing.Any

    Gets or sets the angle from the horizontal on which the aircraft descends to touchdown.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: touch_and_go
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingStandardInstrumentApproach.touch_and_go
    :type: bool

    Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.


