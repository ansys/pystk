IProcedureAreaTargetSearch
==========================

.. py:class:: IProcedureAreaTargetSearch

   object
   
   Interface used to access the options for an Area Target Search procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.
            * - :py:meth:`~copy_procedures`
              - Copy the search pattern maneuvers as a set of procedures to the clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_options`
            * - :py:meth:`~enroute_options`
            * - :py:meth:`~enroute_cruise_airspeed_options`
            * - :py:meth:`~procedure_type`
            * - :py:meth:`~max_separation`
            * - :py:meth:`~course_mode`
            * - :py:meth:`~first_leg_retrograde`
            * - :py:meth:`~centroid_true_course`
            * - :py:meth:`~fly_cruise_airspeed_profile`
            * - :py:meth:`~must_level_off`
            * - :py:meth:`~level_off_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureAreaTargetSearch


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.altitude_options
    :type: "IAgAvtrAltitudeOptions"

    Get the altitude options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.enroute_options
    :type: "IAgAvtrEnrouteOptions"

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.enroute_cruise_airspeed_options
    :type: "IAgAvtrCruiseAirspeedOptions"

    Get the enroute cruise airspeed options.

.. py:property:: procedure_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.procedure_type
    :type: "FLIGHT_LINE_PROC_TYPE"

    Gets or sets the procedure methodology used to calculate the flight line.

.. py:property:: max_separation
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.max_separation
    :type: float

    Gets or sets the maximum distance between the parallel flight lines of the search pattern.

.. py:property:: course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.course_mode
    :type: "SEARCH_PATTERN_COURSE_MODE"

    Gets or sets the mode to determine the course of the search pattern.

.. py:property:: first_leg_retrograde
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.first_leg_retrograde
    :type: bool

    Gets or sets the option to fly the first leg of the search pattern on the reverse heading.

.. py:property:: centroid_true_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.centroid_true_course
    :type: typing.Any

    Gets or sets the specific course of the search pattern.

.. py:property:: fly_cruise_airspeed_profile
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.fly_cruise_airspeed_profile
    :type: bool

    Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.

.. py:property:: must_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.must_level_off
    :type: bool

    Opt whether the procedure must level off.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAreaTargetSearch.level_off_mode
    :type: "ALTITUDE_CONSTRAINT_MANEUVER_MODE"

    Gets or sets the level off mode. This is only used when the must level off option is on.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> "IProcedure"

    Get the procedure interface.

    :Returns:

        :obj:`~"IProcedure"`




















.. py:method:: copy_procedures(self) -> None

    Copy the search pattern maneuvers as a set of procedures to the clipboard.

    :Returns:

        :obj:`~None`

