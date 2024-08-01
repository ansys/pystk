AerodynamicPropulsionManeuverModeHelper
=======================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper

   Bases: 

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

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.mode`
              - Gets or sets the calculation mode for the Aero/Prop maneuver mode helper.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.flight_mode`
              - Gets or sets the performance flight mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.use_afterburner`
              - Opt whether to use the afterburner if it is possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_weight`
              - Gets or sets the reference weight.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_altitude`
              - Gets or sets the reference altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed`
              - Get the reference airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed_type`
              - Get the reference airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_load_factor`
              - Gets or sets the reference load factor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.estimated_ps`
              - Get the estimated specific excess power.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.control_authority`
              - Gets or sets the control authority of how much to factor a turn over push/pull.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.status_message`
              - Get the status message in the message window.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AerodynamicPropulsionManeuverModeHelper


Property detail
---------------

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.mode
    :type: ACCELERATION_MANEUVER_AERODYNAMIC_PROPULSION_MODE

    Gets or sets the calculation mode for the Aero/Prop maneuver mode helper.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.flight_mode
    :type: AERODYNAMIC_PROPULSION_FLIGHT_MODE

    Gets or sets the performance flight mode.

.. py:property:: use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.use_afterburner
    :type: bool

    Opt whether to use the afterburner if it is possible.

.. py:property:: reference_weight
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_weight
    :type: float

    Gets or sets the reference weight.

.. py:property:: reference_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_altitude
    :type: float

    Gets or sets the reference altitude.

.. py:property:: reference_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed
    :type: float

    Get the reference airspeed.

.. py:property:: reference_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed_type
    :type: AIRSPEED_TYPE

    Get the reference airspeed type.

.. py:property:: reference_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_load_factor
    :type: float

    Gets or sets the reference load factor.

.. py:property:: estimated_ps
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.estimated_ps
    :type: float

    Get the estimated specific excess power.

.. py:property:: control_authority
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.control_authority
    :type: float

    Gets or sets the control authority of how much to factor a turn over push/pull.

.. py:property:: status_message
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.status_message
    :type: str

    Get the status message in the message window.


Method detail
-------------













.. py:method:: set_reference_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.set_reference_airspeed

    Set the reference airspeed and reference airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`







