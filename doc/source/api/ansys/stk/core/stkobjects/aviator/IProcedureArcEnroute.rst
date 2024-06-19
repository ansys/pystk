IProcedureArcEnroute
====================

.. py:class:: IProcedureArcEnroute

   object
   
   Interface used to access the options for an arc enroute procedure.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureArcEnroute


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.altitude_options
    :type: IAgAvtrArcAltitudeAndDelayOptions

    Get the altitude options.

.. py:property:: arc_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.arc_options
    :type: IAgAvtrArcOptions

    Get the arc options.

.. py:property:: arc_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.arc_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the arc cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_options
    :type: IAgAvtrEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.enroute_turn_direction_options
    :type: IAgAvtrEnrouteTurnDirectionOptions

    Get the enroute turn direction options.


Method detail
-------------







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureArcEnroute.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

