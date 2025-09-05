LandingInterceptGlideslope
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope

   Class defining the intercept glideslope options for a landing procedure.

.. py:currentmodule:: LandingInterceptGlideslope

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.approach_fix_range`
              - Get or set the range from the reference point of the runway at which the aircraft begins its landing approach.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.approach_fix_range_mode`
              - Get or set the reference point on the runway for the Approach Fix Range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.glideslope`
              - Get or set the angle from the horizontal on which the aircraft descends to touchdown.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.runway_altitude_offset`
              - Get or set the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.touch_and_go`
              - Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import LandingInterceptGlideslope


Property detail
---------------

.. py:property:: approach_fix_range
    :canonical: ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.approach_fix_range
    :type: float

    Get or set the range from the reference point of the runway at which the aircraft begins its landing approach.

.. py:property:: approach_fix_range_mode
    :canonical: ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.approach_fix_range_mode
    :type: LandingApproachFixRangeMode

    Get or set the reference point on the runway for the Approach Fix Range.

.. py:property:: glideslope
    :canonical: ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.glideslope
    :type: typing.Any

    Get or set the angle from the horizontal on which the aircraft descends to touchdown.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.runway_altitude_offset
    :type: float

    Get or set the altitude offset above the ground level.

.. py:property:: touch_and_go
    :canonical: ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.touch_and_go
    :type: bool

    Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.


