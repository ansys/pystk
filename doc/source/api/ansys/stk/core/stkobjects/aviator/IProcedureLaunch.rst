IProcedureLaunch
================

.. py:class:: IProcedureLaunch

   object
   
   Interface used to access the options for a launch procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_airspeed`
              - Set the launch airspeed.
            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~launch_time`
            * - :py:meth:`~position_point_name`
            * - :py:meth:`~direction_vec_name`
            * - :py:meth:`~attitude_mode`
            * - :py:meth:`~specify_launch_airspeed`
            * - :py:meth:`~accel_g`
            * - :py:meth:`~airspeed_type`
            * - :py:meth:`~airspeed`
            * - :py:meth:`~fuel_flow_type`
            * - :py:meth:`~override_fuel_flow`
            * - :py:meth:`~true_course_hint`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureLaunch


Property detail
---------------

.. py:property:: launch_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.launch_time
    :type: typing.Any

    Gets or sets the launch time of the aircraft.

.. py:property:: position_point_name
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.position_point_name
    :type: str

    Gets or sets the name of the point used for the launch position.

.. py:property:: direction_vec_name
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.direction_vec_name
    :type: str

    Gets or sets the name of the vector used for the launch direction.

.. py:property:: attitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.attitude_mode
    :type: "LAUNCH_ATTITUDE_MODE"

    Gets or sets the attitude mode during the launch.

.. py:property:: specify_launch_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.specify_launch_airspeed
    :type: bool

    Opt to specify a minimum launch speed the aircraft will accelerate to.

.. py:property:: accel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.accel_g
    :type: float

    Gets or sets the acceleration of the aircraft during the launch.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.fuel_flow_type
    :type: "FUEL_FLOW_TYPE"

    Gets or sets the fuel flow type of the aircraft during the launch.

.. py:property:: override_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.override_fuel_flow
    :type: float

    Gets or sets the fuel flow value for a fuel flow type set to Override.

.. py:property:: true_course_hint
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunch.true_course_hint
    :type: typing.Any

    Gets or sets the true course used when the vehicle's direction vector is set to Zenith.


Method detail
-------------















.. py:method:: set_airspeed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the launch airspeed.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`





.. py:method:: get_as_procedure(self) -> "IProcedure"

    Get the procedure interface.

    :Returns:

        :obj:`~"IProcedure"`



