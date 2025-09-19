BasicManeuverStrategyPitch3D
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining Pitch 3D strategy for a Basic Maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyPitch3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.command_flight_path_angle`
              - Get or set the commanded flight path angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.control_flight_path_angle_dot`
              - Get or set the flight path angle rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.control_mode`
              - Get or set the control mode for the pitch 3D strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.stop_when_flight_path_angle_achieved`
              - Stop when the commanded flight path angle is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.wind_force_effective_area`
              - Get or set the vehicle's wind force effective area.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyPitch3D


Property detail
---------------

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: command_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.command_flight_path_angle
    :type: typing.Any

    Get or set the commanded flight path angle.

.. py:property:: control_flight_path_angle_dot
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.control_flight_path_angle_dot
    :type: typing.Any

    Get or set the flight path angle rate.

.. py:property:: control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.control_mode
    :type: Pitch3DControlMode

    Get or set the control mode for the pitch 3D strategy.

.. py:property:: stop_when_flight_path_angle_achieved
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.stop_when_flight_path_angle_achieved
    :type: bool

    Stop when the commanded flight path angle is achieved.

.. py:property:: wind_force_effective_area
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D.wind_force_effective_area
    :type: float

    Get or set the vehicle's wind force effective area.


