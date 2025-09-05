ProcedureAirway
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureAirway

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining an Airway procedure.

.. py:currentmodule:: ProcedureAirway

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.copy_procedures`
              - Copy the airway route as a set of procedures to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_airway_names`
              - Get the a list of names of the available airways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_sequences`
              - Get a list of sequence options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_waypoints`
              - Get a list of available waypoints for the airway.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.airway_id`
              - Get or set the airway ID.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.entry_id`
              - Get or set the ID of the entry waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.exit_id`
              - Get or set the ID of the exit waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.router`
              - Get or set the router used to provide available airways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway.sequence`
              - Get or set the direction the aircraft will fly the route.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureAirway


Property detail
---------------

.. py:property:: airway_id
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.airway_id
    :type: str

    Get or set the airway ID.

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.altitude_options
    :type: AltitudeMSLOptions

    Get the altitude options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.enroute_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.enroute_options
    :type: EnrouteOptions

    Get the enroute options.

.. py:property:: entry_id
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.entry_id
    :type: str

    Get or set the ID of the entry waypoint.

.. py:property:: exit_id
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.exit_id
    :type: str

    Get or set the ID of the exit waypoint.

.. py:property:: router
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.router
    :type: str

    Get or set the router used to provide available airways.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.sequence
    :type: str

    Get or set the direction the aircraft will fly the route.


Method detail
-------------




.. py:method:: copy_procedures(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.copy_procedures

    Copy the airway route as a set of procedures to the clipboard.

    :Returns:

        :obj:`~None`







.. py:method:: get_airway_names(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_airway_names

    Get the a list of names of the available airways.

    :Returns:

        :obj:`~list`

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

.. py:method:: get_sequences(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_sequences

    Get a list of sequence options.

    :Returns:

        :obj:`~list`

.. py:method:: get_waypoints(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureAirway.get_waypoints

    Get a list of available waypoints for the airway.

    :Returns:

        :obj:`~list`





