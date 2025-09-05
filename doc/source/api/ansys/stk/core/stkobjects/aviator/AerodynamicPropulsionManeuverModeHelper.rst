AerodynamicPropulsionManeuverModeHelper
=======================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper

   Class defining the The calculation mode for the Aero/Prop maneuver mode helper. Helper for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AerodynamicPropulsionManeuverModeHelper

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.set_reference_airspeed`
              - Set the reference airspeed and reference airspeed type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.control_authority`
              - Get or set the control authority of how much to factor a turn over push/pull.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.estimated_ps`
              - Get the estimated specific excess power.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.flight_mode`
              - Get or set the performance flight mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.mode`
              - Get or set the calculation mode for the Aero/Prop maneuver mode helper.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed`
              - Get the reference airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed_type`
              - Get the reference airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_altitude`
              - Get or set the reference altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_load_factor`
              - Get or set the reference load factor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_weight`
              - Get or set the reference weight.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.status_message`
              - Get the status message in the message window.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.use_afterburner`
              - Opt whether to use the afterburner if it is possible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AerodynamicPropulsionManeuverModeHelper


Property detail
---------------

.. py:property:: control_authority
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.control_authority
    :type: float

    Get or set the control authority of how much to factor a turn over push/pull.

.. py:property:: estimated_ps
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.estimated_ps
    :type: float

    Get the estimated specific excess power.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.flight_mode
    :type: AerodynamicPropulsionFlightMode

    Get or set the performance flight mode.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.mode
    :type: AccelerationManeuverAerodynamicPropulsionMode

    Get or set the calculation mode for the Aero/Prop maneuver mode helper.

.. py:property:: reference_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed
    :type: float

    Get the reference airspeed.

.. py:property:: reference_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed_type
    :type: AirspeedType

    Get the reference airspeed type.

.. py:property:: reference_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_altitude
    :type: float

    Get or set the reference altitude.

.. py:property:: reference_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_load_factor
    :type: float

    Get or set the reference load factor.

.. py:property:: reference_weight
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_weight
    :type: float

    Get or set the reference weight.

.. py:property:: status_message
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.status_message
    :type: str

    Get the status message in the message window.

.. py:property:: use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.use_afterburner
    :type: bool

    Opt whether to use the afterburner if it is possible.


Method detail
-------------
















.. py:method:: set_reference_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.set_reference_airspeed

    Set the reference airspeed and reference airspeed type.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`




