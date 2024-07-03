IProcedureArcEnroute
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute

   object
   
   Interface used to access the options for an arc enroute procedure.

.. py:currentmodule:: IProcedureArcEnroute

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.arc_options`
              - Get the arc options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.arc_cruise_airspeed_options`
              - Get the arc cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_turn_direction_options`
              - Get the enroute turn direction options.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureArcEnroute


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.altitude_options
    :type: IArcAltitudeAndDelayOptions

    Get the altitude options.

.. py:property:: arc_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.arc_options
    :type: IArcOptions

    Get the arc options.

.. py:property:: arc_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.arc_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the arc cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_turn_direction_options
    :type: IEnrouteTurnDirectionOptions

    Get the enroute turn direction options.


Method detail
-------------







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

