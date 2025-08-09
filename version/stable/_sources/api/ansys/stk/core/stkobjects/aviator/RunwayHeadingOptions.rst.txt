RunwayHeadingOptions
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.RunwayHeadingOptions

   Class defining the runway heading options in a takeoff or landing procedure.

.. py:currentmodule:: RunwayHeadingOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RunwayHeadingOptions.runway_mode`
              - Get or set the runway heading that the aircraft will use.



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

    from ansys.stk.core.stkobjects.aviator import RunwayHeadingOptions


Property detail
---------------

.. py:property:: runway_mode
    :canonical: ansys.stk.core.stkobjects.aviator.RunwayHeadingOptions.runway_mode
    :type: RunwayHighLowEnd

    Get or set the runway heading that the aircraft will use.


