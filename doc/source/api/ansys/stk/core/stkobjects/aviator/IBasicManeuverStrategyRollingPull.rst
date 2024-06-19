IBasicManeuverStrategyRollingPull
=================================

.. py:class:: IBasicManeuverStrategyRollingPull

   object
   
   Interface used to access options for a Rolling Pull Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~active_mode`
            * - :py:meth:`~turn_direction`
            * - :py:meth:`~angle`
            * - :py:meth:`~roll_orientation`
            * - :py:meth:`~roll_rate_mode`
            * - :py:meth:`~override_roll_rate`
            * - :py:meth:`~pull_g_mode`
            * - :py:meth:`~override_pull_g`
            * - :py:meth:`~airspeed_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyRollingPull


Property detail
---------------

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.active_mode
    :type: ROLLING_PULL_MODE

    Gets or sets the active mode for the rolling pull basic maneuver strategy.

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.turn_direction
    :type: ROLL_LEFT_RIGHT

    Gets or sets the turn direction for the active mode.

.. py:property:: angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.angle
    :type: typing.Any

    Gets or sets the angle value for the active mode.

.. py:property:: roll_orientation
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.roll_orientation
    :type: ROLL_UPRIGHT_INVERTED

    Gets or sets the orientation to roll to for the roll to orientation mode.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.roll_rate_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the roll rate mode for the rolling pull.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.override_roll_rate
    :type: typing.Any

    Gets or sets the roll rate override value. The roll rate mode must be set to override to access this property.

.. py:property:: pull_g_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.pull_g_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the pull G mode for a rolling pull.

.. py:property:: override_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.override_pull_g
    :type: float

    Gets or sets the pull G override value. The pull G mode must be set to override to access this property.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRollingPull.airspeed_options
    :type: IAgAvtrBasicManeuverAirspeedOptions

    Get the airspeed options.


