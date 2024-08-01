ProcedureAreaTargetSearch
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining an Area Target Search procedure.

.. py:currentmodule:: ProcedureAreaTargetSearch

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.copy_procedures`
              - Copy the search pattern maneuvers as a set of procedures to the clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.procedure_type`
              - Gets or sets the procedure methodology used to calculate the flight line.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.max_separation`
              - Gets or sets the maximum distance between the parallel flight lines of the search pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.course_mode`
              - Gets or sets the mode to determine the course of the search pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.first_leg_retrograde`
              - Gets or sets the option to fly the first leg of the search pattern on the reverse heading.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.centroid_true_course`
              - Gets or sets the specific course of the search pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.fly_cruise_airspeed_profile`
              - Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.must_level_off`
              - Opt whether the procedure must level off.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.level_off_mode`
              - Gets or sets the level off mode. This is only used when the must level off option is on.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureAreaTargetSearch


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.altitude_options
    :type: IAltitudeOptions

    Get the altitude options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.enroute_options
    :type: IEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: procedure_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.procedure_type
    :type: FLIGHT_LINE_PROCEDURE_TYPE

    Gets or sets the procedure methodology used to calculate the flight line.

.. py:property:: max_separation
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.max_separation
    :type: float

    Gets or sets the maximum distance between the parallel flight lines of the search pattern.

.. py:property:: course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.course_mode
    :type: SEARCH_PATTERN_COURSE_MODE

    Gets or sets the mode to determine the course of the search pattern.

.. py:property:: first_leg_retrograde
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.first_leg_retrograde
    :type: bool

    Gets or sets the option to fly the first leg of the search pattern on the reverse heading.

.. py:property:: centroid_true_course
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.centroid_true_course
    :type: typing.Any

    Gets or sets the specific course of the search pattern.

.. py:property:: fly_cruise_airspeed_profile
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.fly_cruise_airspeed_profile
    :type: bool

    Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.

.. py:property:: must_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.must_level_off
    :type: bool

    Opt whether the procedure must level off.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.level_off_mode
    :type: ALTITUDE_CONSTRAINT_MANEUVER_MODE

    Gets or sets the level off mode. This is only used when the must level off option is on.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`




















.. py:method:: copy_procedures(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch.copy_procedures

    Copy the search pattern maneuvers as a set of procedures to the clipboard.

    :Returns:

        :obj:`~None`

