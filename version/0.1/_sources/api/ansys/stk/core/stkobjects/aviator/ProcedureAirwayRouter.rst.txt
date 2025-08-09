ProcedureAirwayRouter
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining an Airway Router procedure.

.. py:currentmodule:: ProcedureAirwayRouter

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.update_route`
              - Recalculate the route.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.get_waypoints`
              - Get a list of the current route's waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.get_segments`
              - Get a list of the current route's individual procedures.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.copy_procedures`
              - Copy the route as a set of procedures to the clipboard.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.router`
              - Get or set the router used to provide available airways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.optimize_for_wind`
              - Opt to account for the wind when calculating the most efficient route.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.bounding_box_pad`
              - Get or set the maximum distance beyond the bounding box that a waypoint will be considered for the final route.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.max_waypoint_range`
              - Get or set the maximum distance from the end of the previous procedure that an airway waypoint will be considered.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.entry_exit_and_or`
              - Define how the two Entry/Exit Waypoint constraints will be considered.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.max_waypoint_count`
              - Get or set the maximum number of airway waypoints that the procedure will consider for each segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureAirwayRouter


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.altitude_options
    :type: AltitudeMSLOptions

    Get the altitude options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.enroute_options
    :type: EnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.enroute_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: router
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.router
    :type: str

    Get or set the router used to provide available airways.

.. py:property:: optimize_for_wind
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.optimize_for_wind
    :type: bool

    Opt to account for the wind when calculating the most efficient route.

.. py:property:: bounding_box_pad
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.bounding_box_pad
    :type: float

    Get or set the maximum distance beyond the bounding box that a waypoint will be considered for the final route.

.. py:property:: max_waypoint_range
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.max_waypoint_range
    :type: float

    Get or set the maximum distance from the end of the previous procedure that an airway waypoint will be considered.

.. py:property:: entry_exit_and_or
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.entry_exit_and_or
    :type: AndOr

    Define how the two Entry/Exit Waypoint constraints will be considered.

.. py:property:: max_waypoint_count
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.max_waypoint_count
    :type: int

    Get or set the maximum number of airway waypoints that the procedure will consider for each segment.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`















.. py:method:: update_route(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.update_route

    Recalculate the route.

    :Returns:

        :obj:`~None`

.. py:method:: get_waypoints(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.get_waypoints

    Get a list of the current route's waypoints.

    :Returns:

        :obj:`~list`

.. py:method:: get_segments(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.get_segments

    Get a list of the current route's individual procedures.

    :Returns:

        :obj:`~list`

.. py:method:: copy_procedures(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter.copy_procedures

    Copy the route as a set of procedures to the clipboard.

    :Returns:

        :obj:`~None`

