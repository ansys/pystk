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

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.set_airspeed`
              - Set the launch airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.launch_time`
              - Gets or sets the launch time of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.position_point_name`
              - Gets or sets the name of the point used for the launch position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.direction_vec_name`
              - Gets or sets the name of the vector used for the launch direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.attitude_mode`
              - Gets or sets the attitude mode during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.specify_launch_airspeed`
              - Opt to specify a minimum launch speed the aircraft will accelerate to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.acceleration_g`
              - Gets or sets the acceleration of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed`
              - Get the goal airspeed for the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.fuel_flow_type`
              - Gets or sets the fuel flow type of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.override_fuel_flow`
              - Gets or sets the fuel flow value for a fuel flow type set to Override.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch.true_course_hint`
              - Gets or sets the true course used when the vehicle's direction vector is set to Zenith.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureLaunch


Property detail
---------------

.. py:property:: launch_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.launch_time
    :type: typing.Any

    Gets or sets the launch time of the aircraft.

.. py:property:: position_point_name
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.position_point_name
    :type: str

    Gets or sets the name of the point used for the launch position.

.. py:property:: direction_vec_name
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.direction_vec_name
    :type: str

    Gets or sets the name of the vector used for the launch direction.

.. py:property:: attitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.attitude_mode
    :type: LAUNCH_ATTITUDE_MODE

    Gets or sets the attitude mode during the launch.

.. py:property:: specify_launch_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.specify_launch_airspeed
    :type: bool

    Opt to specify a minimum launch speed the aircraft will accelerate to.

.. py:property:: acceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.acceleration_g
    :type: float

    Gets or sets the acceleration of the aircraft during the launch.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.fuel_flow_type
    :type: FUEL_FLOW_TYPE

    Gets or sets the fuel flow type of the aircraft during the launch.

.. py:property:: override_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.override_fuel_flow
    :type: float

    Gets or sets the fuel flow value for a fuel flow type set to Override.

.. py:property:: true_course_hint
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.true_course_hint
    :type: typing.Any

    Gets or sets the true course used when the vehicle's direction vector is set to Zenith.


Method detail
-------------















.. py:method:: set_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.set_airspeed

    Set the launch airspeed.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`





.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunch.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`



