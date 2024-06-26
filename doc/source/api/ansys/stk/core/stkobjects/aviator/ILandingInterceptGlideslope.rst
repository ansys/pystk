ILandingInterceptGlideslope
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope

   object
   
   The interface used to access the options for an Intercept Glideslope approach mode for a landing procedure. The approach mode must be set to Intercept Glideslope to access this interface.

.. py:currentmodule:: ILandingInterceptGlideslope

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.approach_fix_range`
              - Gets or sets the range from the reference point of the runway at which the aircraft begins its landing approach.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.approach_fix_range_mode`
              - Gets or sets the reference point on the runway for the Approach Fix Range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.glideslope`
              - Gets or sets the angle from the horizontal on which the aircraft descends to touchdown.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.runway_altitude_offset`
              - Gets or sets the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.touch_and_go`
              - Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ILandingInterceptGlideslope


Property detail
---------------

.. py:property:: approach_fix_range
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.approach_fix_range
    :type: float

    Gets or sets the range from the reference point of the runway at which the aircraft begins its landing approach.

.. py:property:: approach_fix_range_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.approach_fix_range_mode
    :type: LANDING_APPROACH_FIX_RANGE_MODE

    Gets or sets the reference point on the runway for the Approach Fix Range.

.. py:property:: glideslope
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.glideslope
    :type: typing.Any

    Gets or sets the angle from the horizontal on which the aircraft descends to touchdown.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: touch_and_go
    :canonical: ansys.stk.core.stkobjects.aviator.ILandingInterceptGlideslope.touch_and_go
    :type: bool

    Opt whether to perform a Touch and Go landing. The procedure will stop at wheels down and can be immediately followed by a takeoff procedure.


