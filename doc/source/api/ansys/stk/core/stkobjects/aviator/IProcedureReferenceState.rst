IProcedureReferenceState
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState

   object
   
   Interface used to access the options for a reference state procedure.

.. py:currentmodule:: IProcedureReferenceState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.start_time`
              - Gets or sets the start time of the reference state.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.latitude`
              - Gets or sets the waypoint latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.longitude`
              - Gets or sets the waypoint longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.use_default_cruise_altitude`
              - Opt whether to use the default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.msl_altitude`
              - Get the MSL altitude. Can only be used when the option to use the default cruise altitude is off.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.performance_mode`
              - Gets or sets the type of motion the aircraft is engaged in.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.reference_frame`
              - Gets or sets the reference frame the aircraft will use.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.fuel_flow`
              - Gets or sets the rate of fuel consumption.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_forward_flight`
              - Get the forward flight options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_takeoff_landing`
              - Get the takeoff and landing options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_hover`
              - Get the hover options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_weight_on_wheels`
              - Get the weight on wheels options.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureReferenceState


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.start_time
    :type: typing.Any

    Gets or sets the start time of the reference state.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.latitude
    :type: typing.Any

    Gets or sets the waypoint latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.longitude
    :type: typing.Any

    Gets or sets the waypoint longitude.

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: msl_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.msl_altitude
    :type: float

    Get the MSL altitude. Can only be used when the option to use the default cruise altitude is off.

.. py:property:: performance_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.performance_mode
    :type: REFERENCE_STATE_PERF_MODE

    Gets or sets the type of motion the aircraft is engaged in.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.reference_frame
    :type: BASIC_MANEUVER_REFERENCE_FRAME

    Gets or sets the reference frame the aircraft will use.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.fuel_flow
    :type: float

    Gets or sets the rate of fuel consumption.

.. py:property:: mode_as_forward_flight
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_forward_flight
    :type: IReferenceStateForwardFlightOptions

    Get the forward flight options.

.. py:property:: mode_as_takeoff_landing
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_takeoff_landing
    :type: IReferenceStateTakeoffLandingOptions

    Get the takeoff and landing options.

.. py:property:: mode_as_hover
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_hover
    :type: IReferenceStateHoverOptions

    Get the hover options.

.. py:property:: mode_as_weight_on_wheels
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.mode_as_weight_on_wheels
    :type: IReferenceStateWeightOnWheelsOptions

    Get the weight on wheels options.


Method detail
-------------



.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureReferenceState.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`



















