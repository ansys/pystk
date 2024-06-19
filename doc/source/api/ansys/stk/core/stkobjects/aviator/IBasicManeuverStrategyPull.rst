IBasicManeuverStrategyPull
==========================

.. py:class:: IBasicManeuverStrategyPull

   object
   
   Interface used to access options for a Pull Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~active_mode`
            * - :py:meth:`~active_angle`
            * - :py:meth:`~pull_g_mode`
            * - :py:meth:`~override_pull_g`
            * - :py:meth:`~airspeed_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyPull


Property detail
---------------

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPull.active_mode
    :type: PULL_MODE

    Gets or sets the pull mode for the pull basic maneuver strategy.

.. py:property:: active_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPull.active_angle
    :type: typing.Any

    Gets or sets the pull angle for the active mode.

.. py:property:: pull_g_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPull.pull_g_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the pull G mode for a pull basic maneuver strategy.

.. py:property:: override_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPull.override_pull_g
    :type: float

    Gets or sets the pull G override value. The pull G mode must be set to override to access this property.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPull.airspeed_options
    :type: IAgAvtrBasicManeuverAirspeedOptions

    Get the airspeed options.


