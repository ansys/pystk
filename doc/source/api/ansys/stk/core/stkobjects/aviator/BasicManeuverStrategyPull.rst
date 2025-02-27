BasicManeuverStrategyPull
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the pull strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyPull

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.active_mode`
              - Get or set the pull mode for the pull basic maneuver strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.active_angle`
              - Get or set the pull angle for the active mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.pull_g_mode`
              - Get or set the pull G mode for a pull basic maneuver strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.override_pull_g`
              - Get or set the pull G override value. The pull G mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.airspeed_options`
              - Get the airspeed options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyPull


Property detail
---------------

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.active_mode
    :type: PullMode

    Get or set the pull mode for the pull basic maneuver strategy.

.. py:property:: active_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.active_angle
    :type: typing.Any

    Get or set the pull angle for the active mode.

.. py:property:: pull_g_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.pull_g_mode
    :type: PerformanceModelOverride

    Get or set the pull G mode for a pull basic maneuver strategy.

.. py:property:: override_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.override_pull_g
    :type: float

    Get or set the pull G override value. The pull G mode must be set to override to access this property.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.


