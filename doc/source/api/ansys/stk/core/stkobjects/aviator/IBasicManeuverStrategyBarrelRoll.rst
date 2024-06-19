IBasicManeuverStrategyBarrelRoll
================================

.. py:class:: IBasicManeuverStrategyBarrelRoll

   object
   
   Interface used to access options for a Barrel Roll Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_airspeeds`
              - Set the speeds at the top and bottom of the loop.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~helix_angle`
            * - :py:meth:`~helix_angle_mode`
            * - :py:meth:`~top_load_factor`
            * - :py:meth:`~bottom_load_factor`
            * - :py:meth:`~torsion_angle`
            * - :py:meth:`~hold_init_tas`
            * - :py:meth:`~airspeed_type`
            * - :py:meth:`~top_airspeed`
            * - :py:meth:`~bottom_airspeed`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyBarrelRoll


Property detail
---------------

.. py:property:: helix_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.helix_angle
    :type: typing.Any

    Gets or sets the helix angle for the barrel roll. The angle that the aircraft travels around the velocity vector.

.. py:property:: helix_angle_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.helix_angle_mode
    :type: ANGLE_MODE

    Gets or sets the helix angle mode for the barrel roll.

.. py:property:: top_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.top_load_factor
    :type: float

    Gets or sets the load factor at the top of the loop.

.. py:property:: bottom_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.bottom_load_factor
    :type: float

    Gets or sets the load factor at the bottom of the loop.

.. py:property:: torsion_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.torsion_angle
    :type: typing.Any

    Gets or sets the torsion angle for the barrel roll. The angle of the turn from the aircraft's velocity vector.

.. py:property:: hold_init_tas
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.hold_init_tas
    :type: bool

    Gets or sets the option to hold the initial true airspeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: top_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.top_airspeed
    :type: float

    Get the speed at the top of the loop.

.. py:property:: bottom_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.bottom_airspeed
    :type: float

    Get the speed at the bottom of the loop.


Method detail
-------------
















.. py:method:: set_airspeeds(self, airspeedType: AIRSPEED_TYPE, topAirspeed: float, bottomAirspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBarrelRoll.set_airspeeds

    Set the speeds at the top and bottom of the loop.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **topAirspeed** : :obj:`~float`
    **bottomAirspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`

