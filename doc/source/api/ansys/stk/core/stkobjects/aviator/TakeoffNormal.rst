TakeoffNormal
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.TakeoffNormal

   Class defining the normal options for a takeoff procedure.

.. py:currentmodule:: TakeoffNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffNormal.departure_altitude`
              - Get or set the aircraft's altitude when it departs the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffNormal.hold_on_deck`
              - Get or set the duration the aircraft will wait before beginning the takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffNormal.runway_altitude_offset`
              - Get or set the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffNormal.takeoff_climb_angle`
              - Get or set the angle at which the aircraft will climb from the procedure site to the departure point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffNormal.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.



Examples
--------

Add a takeoff procedure from a runway

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a takeoff procedure with a runway as a site
    takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)

    # Get the runway heading options
    headingOptions = takeoff.runway_heading_options
    # Opt to use the headwind runway
    headingOptions.runway_mode = RunwayHighLowEnd.HEADWIND

    # Set the takeoff mode and get that interface
    takeoff.takeoff_mode = TakeoffMode.TAKEOFF_NORMAL
    takeoffNormal = takeoff.mode_as_normal

    # Set the takeoff climb angle
    takeoffNormal.takeoff_climb_angle = 5
    # Set the departure altitude above the runway
    takeoffNormal.departure_altitude = 600
    # Set the altitude offset for the runway
    takeoffNormal.runway_altitude_offset = 10
    # Use terrain for the runway's altitude
    takeoffNormal.use_runway_terrain = True


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import TakeoffNormal


Property detail
---------------

.. py:property:: departure_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffNormal.departure_altitude
    :type: float

    Get or set the aircraft's altitude when it departs the runway.

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffNormal.hold_on_deck
    :type: typing.Any

    Get or set the duration the aircraft will wait before beginning the takeoff.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffNormal.runway_altitude_offset
    :type: float

    Get or set the altitude offset above the ground level.

.. py:property:: takeoff_climb_angle
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffNormal.takeoff_climb_angle
    :type: typing.Any

    Get or set the angle at which the aircraft will climb from the procedure site to the departure point.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffNormal.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.


