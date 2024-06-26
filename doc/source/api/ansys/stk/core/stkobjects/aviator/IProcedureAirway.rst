IProcedureAirway
================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureAirway

   object
   
   Interface used to access the options for an Airway procedure.

.. py:currentmodule:: IProcedureAirway

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_airway_names`
              - Get the a list of names of the available airways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_sequences`
              - Get a list of sequence options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_waypoints`
              - Get a list of available waypoints for the airway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.copy_procedures`
              - Copy the airway route as a set of procedures to the clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.router`
              - Gets or sets the router used to provide available airways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.airway_id`
              - Gets or sets the airway ID.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.sequence`
              - Gets or sets the direction the aircraft will fly the route.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.entry_id`
              - Gets or sets the ID of the entry waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureAirway.exit_id`
              - Gets or sets the ID of the exit waypoint.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureAirway


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.altitude_options
    :type: IAltitudeMSLOptions

    Get the altitude options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.enroute_options
    :type: IEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: router
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.router
    :type: str

    Gets or sets the router used to provide available airways.

.. py:property:: airway_id
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.airway_id
    :type: str

    Gets or sets the airway ID.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.sequence
    :type: str

    Gets or sets the direction the aircraft will fly the route.

.. py:property:: entry_id
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.entry_id
    :type: str

    Gets or sets the ID of the entry waypoint.

.. py:property:: exit_id
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.exit_id
    :type: str

    Gets or sets the ID of the exit waypoint.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`








.. py:method:: get_airway_names(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_airway_names

    Get the a list of names of the available airways.

    :Returns:

        :obj:`~list`



.. py:method:: get_sequences(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_sequences

    Get a list of sequence options.

    :Returns:

        :obj:`~list`





.. py:method:: get_waypoints(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.get_waypoints

    Get a list of available waypoints for the airway.

    :Returns:

        :obj:`~list`

.. py:method:: copy_procedures(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureAirway.copy_procedures

    Copy the airway route as a set of procedures to the clipboard.

    :Returns:

        :obj:`~None`

