IProcedureDelay
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureDelay

   object
   
   Interface used to access the options for a delay procedure.

.. py:currentmodule:: IProcedureDelay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureDelay.altitude_mode`
              - Gets or sets the mode for handling the altitude of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureDelay.altitude`
              - Gets or sets the requested altitude of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureDelay.cruise_airspeed_options`
              - Get the interface for the cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureDelay.turn_direction`
              - Gets or sets the turn direction of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureDelay.turn_radius_factor`
              - Gets or sets the turn radius factor.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureDelay


Property detail
---------------

.. py:property:: altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureDelay.altitude_mode
    :type: DELAY_ALTITUDE_MODE

    Gets or sets the mode for handling the altitude of the aircraft.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureDelay.altitude
    :type: float

    Gets or sets the requested altitude of the procedure.

.. py:property:: cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureDelay.cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the interface for the cruise airspeed options.

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureDelay.turn_direction
    :type: NAVIGATOR_TURN_DIRECTION

    Gets or sets the turn direction of the procedure.

.. py:property:: turn_radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureDelay.turn_radius_factor
    :type: float

    Gets or sets the turn radius factor.


