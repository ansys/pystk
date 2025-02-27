ProcedureTakeoff
================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a takeoff procedure.

.. py:currentmodule:: ProcedureTakeoff

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.runway_heading_options`
              - Get the runway heading options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_normal`
              - Get the interface for a normal takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_departure_point`
              - Get the interface for a departure point takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_low_transition`
              - Get the interface for a low transition takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.takeoff_mode`
              - Get or set the type of takeoff the aircraft will perform.



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

    from ansys.stk.core.stkobjects.aviator import ProcedureTakeoff


Property detail
---------------

.. py:property:: runway_heading_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.runway_heading_options
    :type: RunwayHeadingOptions

    Get the runway heading options.

.. py:property:: mode_as_normal
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_normal
    :type: TakeoffNormal

    Get the interface for a normal takeoff.

.. py:property:: mode_as_departure_point
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_departure_point
    :type: TakeoffDeparturePoint

    Get the interface for a departure point takeoff.

.. py:property:: mode_as_low_transition
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_low_transition
    :type: TakeoffLowTransition

    Get the interface for a low transition takeoff.

.. py:property:: takeoff_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.takeoff_mode
    :type: TakeoffMode

    Get or set the type of takeoff the aircraft will perform.


Method detail
-------------







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

