IProcedureAirwayRouter
======================

.. py:class:: IProcedureAirwayRouter

   object
   
   Interface used to access the options for an Airway Router procedure.

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
            * - :py:meth:`~update_route`
              - Recalculate the route.
            * - :py:meth:`~get_waypoints`
              - Get a list of the current route's waypoints.
            * - :py:meth:`~get_segments`
              - Get a list of the current route's individual procedures.
            * - :py:meth:`~copy_procedures`
              - Copy the route as a set of procedures to the clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_options`
            * - :py:meth:`~enroute_options`
            * - :py:meth:`~enroute_cruise_airspeed_options`
            * - :py:meth:`~router`
            * - :py:meth:`~optimize_for_wind`
            * - :py:meth:`~bounding_box_pad`
            * - :py:meth:`~max_waypoint_range`
            * - :py:meth:`~entry_exit_and_or`
            * - :py:meth:`~max_waypoint_count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureAirwayRouter


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.altitude_options
    :type: "IAgAvtrAltitudeMSLOptions"

    Get the altitude options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.enroute_options
    :type: "IAgAvtrEnrouteOptions"

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.enroute_cruise_airspeed_options
    :type: "IAgAvtrCruiseAirspeedOptions"

    Get the enroute cruise airspeed options.

.. py:property:: router
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.router
    :type: str

    Gets or sets the router used to provide available airways.

.. py:property:: optimize_for_wind
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.optimize_for_wind
    :type: bool

    Opt to account for the wind when calculating the most efficient route.

.. py:property:: bounding_box_pad
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.bounding_box_pad
    :type: float

    Gets or sets the maximum distance beyond the bounding box that a waypoint will be considered for the final route.

.. py:property:: max_waypoint_range
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.max_waypoint_range
    :type: float

    Gets or sets the maximum distance from the end of the previous procedure that an airway waypoint will be considered.

.. py:property:: entry_exit_and_or
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.entry_exit_and_or
    :type: "AND_OR"

    Define how the two Entry/Exit Waypoint constraints will be considered.

.. py:property:: max_waypoint_count
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirwayRouter.max_waypoint_count
    :type: int

    Gets or sets the maximum number of airway waypoints that the procedure will consider for each segment.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> "IProcedure"

    Get the procedure interface.

    :Returns:

        :obj:`~"IProcedure"`















.. py:method:: update_route(self) -> None

    Recalculate the route.

    :Returns:

        :obj:`~None`

.. py:method:: get_waypoints(self) -> list

    Get a list of the current route's waypoints.

    :Returns:

        :obj:`~list`

.. py:method:: get_segments(self) -> list

    Get a list of the current route's individual procedures.

    :Returns:

        :obj:`~list`

.. py:method:: copy_procedures(self) -> None

    Copy the route as a set of procedures to the clipboard.

    :Returns:

        :obj:`~None`

