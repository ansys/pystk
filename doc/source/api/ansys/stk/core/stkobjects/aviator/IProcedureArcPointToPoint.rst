IProcedureArcPointToPoint
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint

   object
   
   Interface used to access the options for an arc point to point procedure.

.. py:currentmodule:: IProcedureArcPointToPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.arc_options`
              - Get the arc options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.arc_cruise_airspeed_options`
              - Get the arc cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_turn_direction_options`
              - Get the enroute turn direction options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.fly_cruise_airspeed_profile`
              - Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.vertical_plane_options`
              - Get the vertical plane options.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureArcPointToPoint


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.altitude_options
    :type: IArcAltitudeOptions

    Get the altitude options.

.. py:property:: arc_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.arc_options
    :type: IArcOptions

    Get the arc options.

.. py:property:: arc_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.arc_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the arc cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_options
    :type: IEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.enroute_turn_direction_options
    :type: IEnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: fly_cruise_airspeed_profile
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.fly_cruise_airspeed_profile
    :type: bool

    Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.vertical_plane_options
    :type: IArcVerticalPlaneOptions

    Get the vertical plane options.


Method detail
-------------










.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcPointToPoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

