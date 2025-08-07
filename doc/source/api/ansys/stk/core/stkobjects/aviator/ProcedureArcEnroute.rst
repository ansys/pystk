ProcedureArcEnroute
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a arc enroute procedure.

.. py:currentmodule:: ProcedureArcEnroute

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.arc_cruise_airspeed_options`
              - Get the arc cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.arc_options`
              - Get the arc options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.enroute_turn_direction_options`
              - Get the enroute turn direction options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureArcEnroute


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.altitude_options
    :type: ArcAltitudeAndDelayOptions

    Get the altitude options.

.. py:property:: arc_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.arc_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the arc cruise airspeed options.

.. py:property:: arc_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.arc_options
    :type: ArcOptions

    Get the arc options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.enroute_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.enroute_turn_direction_options
    :type: EnrouteTurnDirectionOptions

    Get the enroute turn direction options.


Method detail
-------------







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

