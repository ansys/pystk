BasicManeuverStrategyBallistic3D
================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining Ballistic 3D strategy for a Basic Maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyBallistic3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.control_mode`
              - Get or set the control mode for the ballistic 3D strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.parachute_area`
              - Get or set the parachute area used as part of the Parachute control mode for the ballistic 3D strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.parachute_cd`
              - Get or set the parachute coefficient of drag used as part of the Parachute control mode for the ballistic 3D strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.wind_force_effective_area`
              - Get or set the vehicle's wind force effective area.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyBallistic3D


Property detail
---------------

.. py:property:: control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.control_mode
    :type: Ballistic3DControlMode

    Get or set the control mode for the ballistic 3D strategy.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: parachute_area
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.parachute_area
    :type: float

    Get or set the parachute area used as part of the Parachute control mode for the ballistic 3D strategy.

.. py:property:: parachute_cd
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.parachute_cd
    :type: float

    Get or set the parachute coefficient of drag used as part of the Parachute control mode for the ballistic 3D strategy.

.. py:property:: wind_force_effective_area
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D.wind_force_effective_area
    :type: float

    Get or set the vehicle's wind force effective area.


