IRotorcraftModel
================

.. py:class:: IRotorcraftModel

   object
   
   Interface used to access the rotorcraft options in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_max_safe_airspeed`
              - Set the maximum safe airspeed and airspeed type.
            * - :py:meth:`~set_max_safe_translation_speed`
              - Set the maximum safe translation airspeed and airspeed type.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_altitude`
            * - :py:meth:`~default_cruise_altitude`
            * - :py:meth:`~descent_rate_factor`
            * - :py:meth:`~max_climb_angle`
            * - :py:meth:`~climb_at_cruise_airspeed`
            * - :py:meth:`~max_descent_angle`
            * - :py:meth:`~min_descent_rate`
            * - :py:meth:`~max_load_factor`
            * - :py:meth:`~roll_rate`
            * - :py:meth:`~pitch_rate`
            * - :py:meth:`~yaw_rate`
            * - :py:meth:`~yaw_rate_dot`
            * - :py:meth:`~max_transition_pitch_angle`
            * - :py:meth:`~tf_max_flight_path_angle`
            * - :py:meth:`~tf_terrain_window`
            * - :py:meth:`~compute_delta_altitude`
            * - :py:meth:`~max_safe_airspeed`
            * - :py:meth:`~max_safe_airspeed_type`
            * - :py:meth:`~max_safe_translation_speed`
            * - :py:meth:`~max_safe_translation_speed_type`
            * - :py:meth:`~ignore_fpa_for_climb_descent_transitions`
            * - :py:meth:`~default_configuration`
            * - :py:meth:`~aerodynamics`
            * - :py:meth:`~propulsion`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IRotorcraftModel


Property detail
---------------

.. py:property:: max_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_altitude
    :type: float

    Gets or sets the maximum altitude at which the rotorcraft is capable of operating.

.. py:property:: default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.default_cruise_altitude
    :type: float

    Gets or sets the rotorcraft's default cruising altitude.

.. py:property:: descent_rate_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.descent_rate_factor
    :type: float

    Gets or sets the descent rate of the rotorcraft as a factor multiplied by the altitude change rate calculated at zero throttle.

.. py:property:: max_climb_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_climb_angle
    :type: typing.Any

    Gets or sets the maximum pitch angle of the rotorcraft's flight path while climbing.

.. py:property:: climb_at_cruise_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.climb_at_cruise_airspeed
    :type: bool

    Select to define the climbing airspeed of the rotorcraft using the cruise airspeed of the current procedure.

.. py:property:: max_descent_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_descent_angle
    :type: typing.Any

    Gets or sets the maximum pitch angle of the rotorcraft's flight path while descending.

.. py:property:: min_descent_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.min_descent_rate
    :type: float

    Gets or sets the minimum rate at which the aircraft will descend once established in a steady descent.

.. py:property:: max_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_load_factor
    :type: float

    Gets or sets the maximum load factor that the aircraft can bear while maneuvering in formation.

.. py:property:: roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.roll_rate
    :type: typing.Any

    Gets or sets the standard roll rate of the rotorcraft in a turn.

.. py:property:: pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.pitch_rate
    :type: typing.Any

    Gets or sets the pitch rate when transitioning between attitude modes or procedures.

.. py:property:: yaw_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.yaw_rate
    :type: typing.Any

    Gets or sets the yaw rate when transitioning between attitude modes.

.. py:property:: yaw_rate_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.yaw_rate_dot
    :type: typing.Any

    Gets or sets the rate of change of the yaw rate.

.. py:property:: max_transition_pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_transition_pitch_angle
    :type: typing.Any

    Gets or sets the maximum pitch angle of the flight path when transitioning between forward flight and hovering.

.. py:property:: tf_max_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.tf_max_flight_path_angle
    :type: typing.Any

    Gets or sets the maximum pitch angle of the flight path when the rotorcraft is engaged in terrain following flight.

.. py:property:: tf_terrain_window
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.tf_terrain_window
    :type: float

    Gets or sets the time interval over which terrain points are sampled when the rotorcraft is engaged in terrain following flight.

.. py:property:: compute_delta_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.compute_delta_altitude
    :type: float

    Gets or sets the maximum change in altitude in a computed segment before the data is sampled again.

.. py:property:: max_safe_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_safe_airspeed
    :type: float

    Get the maximum cruising airspeed of the rotorcraft.

.. py:property:: max_safe_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_safe_airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the maximum safe airspeed type.

.. py:property:: max_safe_translation_speed
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_safe_translation_speed
    :type: float

    Get the maximum translation speed of the rotorcraft.

.. py:property:: max_safe_translation_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.max_safe_translation_speed_type
    :type: "AIRSPEED_TYPE"

    Get the maximum safe translation speed type.

.. py:property:: ignore_fpa_for_climb_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.ignore_fpa_for_climb_descent_transitions
    :type: bool

    Opt to ignore load factor limits when pushing over or pulling up.

.. py:property:: default_configuration
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.default_configuration
    :type: "IAgAvtrConfiguration"

    Get the aircraft's default configuration as saved in the catalog.

.. py:property:: aerodynamics
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.aerodynamics
    :type: "IAgAvtrRotorcraftAero"

    Get the aerodynamics interface.

.. py:property:: propulsion
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftModel.propulsion
    :type: "IAgAvtrRotorcraftProp"

    Get the propulsion interface.


Method detail
-------------



































.. py:method:: set_max_safe_airspeed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the maximum safe airspeed and airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_safe_translation_speed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the maximum safe translation airspeed and airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`






.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

