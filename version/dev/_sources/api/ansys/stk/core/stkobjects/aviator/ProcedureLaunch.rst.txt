ProcedureLaunch
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureLaunch

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a launch procedure.

.. py:currentmodule:: ProcedureLaunch

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.set_airspeed`
              - Set the launch airspeed.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.acceleration_g`
              - Get or set the acceleration of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed`
              - Get the goal airspeed for the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.attitude_mode`
              - Get or set the attitude mode during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.direction_vec_name`
              - Get or set the name of the vector used for the launch direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.fuel_flow_type`
              - Get or set the fuel flow type of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.launch_time`
              - Get or set the launch time of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.override_fuel_flow`
              - Get or set the fuel flow value for a fuel flow type set to Override.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.position_point_name`
              - Get or set the name of the point used for the launch position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.specify_launch_airspeed`
              - Opt to specify a minimum launch speed the aircraft will accelerate to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.true_course_hint`
              - Get or set the true course used when the vehicle's direction vector is set to Zenith.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureLaunch


Property detail
---------------

.. py:property:: acceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.acceleration_g
    :type: float

    Get or set the acceleration of the aircraft during the launch.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: attitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.attitude_mode
    :type: LaunchAttitudeMode

    Get or set the attitude mode during the launch.

.. py:property:: direction_vec_name
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.direction_vec_name
    :type: str

    Get or set the name of the vector used for the launch direction.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.fuel_flow_type
    :type: FuelFlowType

    Get or set the fuel flow type of the aircraft during the launch.

.. py:property:: launch_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.launch_time
    :type: typing.Any

    Get or set the launch time of the aircraft.

.. py:property:: override_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.override_fuel_flow
    :type: float

    Get or set the fuel flow value for a fuel flow type set to Override.

.. py:property:: position_point_name
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.position_point_name
    :type: str

    Get or set the name of the point used for the launch position.

.. py:property:: specify_launch_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.specify_launch_airspeed
    :type: bool

    Opt to specify a minimum launch speed the aircraft will accelerate to.

.. py:property:: true_course_hint
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.true_course_hint
    :type: typing.Any

    Get or set the true course used when the vehicle's direction vector is set to Zenith.


Method detail
-------------











.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`







.. py:method:: set_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.set_airspeed

    Set the launch airspeed.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`





