IBasicManeuverStrategySmoothTurn
================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn

   object
   
   Interface used to access options for a Smooth Turn Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: IBasicManeuverStrategySmoothTurn

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.heading_change`
              - Gets or sets the heading change for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.turn_mode`
              - Gets or sets the turn mode for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.load_factor_mode`
              - Gets or sets the load factor mode for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.max_load_factor_rate`
              - Gets or sets the max load factor rate for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.override_load_factor`
              - Gets or sets the max load factor override value for the smooth turn. The load factor mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.roll_rate_mode`
              - Gets or sets the roll rate mode for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.roll_angle`
              - Gets or sets the roll angle for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.override_roll_rate`
              - Gets or sets the max roll rate override value for the smooth turn. The roll rate mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.fpa_mode`
              - Gets or sets the flight path angle mode.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategySmoothTurn


Property detail
---------------

.. py:property:: heading_change
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.heading_change
    :type: typing.Any

    Gets or sets the heading change for the smooth turn.

.. py:property:: turn_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.turn_mode
    :type: SMOOTH_TURN_MODE

    Gets or sets the turn mode for the smooth turn.

.. py:property:: load_factor_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.load_factor_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the load factor mode for the smooth turn.

.. py:property:: max_load_factor_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.max_load_factor_rate
    :type: float

    Gets or sets the max load factor rate for the smooth turn.

.. py:property:: override_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.override_load_factor
    :type: float

    Gets or sets the max load factor override value for the smooth turn. The load factor mode must be set to override to access this property.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.roll_rate_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the roll rate mode for the smooth turn.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.roll_angle
    :type: typing.Any

    Gets or sets the roll angle for the smooth turn.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.override_roll_rate
    :type: typing.Any

    Gets or sets the max roll rate override value for the smooth turn. The roll rate mode must be set to override to access this property.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.airspeed_options
    :type: IBasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: fpa_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothTurn.fpa_mode
    :type: SMOOTH_TURN_FPA_MODE

    Gets or sets the flight path angle mode.


