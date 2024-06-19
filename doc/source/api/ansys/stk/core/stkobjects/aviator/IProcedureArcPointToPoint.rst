IProcedureArcPointToPoint
=========================

.. py:class:: IProcedureArcPointToPoint

   object
   
   Interface used to access the options for an arc point to point procedure.

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

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_options`
            * - :py:meth:`~arc_options`
            * - :py:meth:`~arc_cruise_airspeed_options`
            * - :py:meth:`~enroute_options`
            * - :py:meth:`~enroute_cruise_airspeed_options`
            * - :py:meth:`~enroute_turn_direction_options`
            * - :py:meth:`~fly_cruise_airspeed_profile`
            * - :py:meth:`~vertical_plane_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureArcPointToPoint


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.altitude_options
    :type: IAgAvtrArcAltitudeOptions

    Get the altitude options.

.. py:property:: arc_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.arc_options
    :type: IAgAvtrArcOptions

    Get the arc options.

.. py:property:: arc_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.arc_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the arc cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_options
    :type: IAgAvtrEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_turn_direction_options
    :type: IAgAvtrEnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: fly_cruise_airspeed_profile
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.fly_cruise_airspeed_profile
    :type: bool

    Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.vertical_plane_options
    :type: IAgAvtrArcVerticalPlaneOptions

    Get the vertical plane options.


Method detail
-------------










.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

