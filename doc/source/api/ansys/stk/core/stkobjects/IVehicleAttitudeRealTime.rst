IVehicleAttitudeRealTime
========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime

   IVehicleAttitude
   
   Real time attitude interface.

.. py:currentmodule:: IVehicleAttitudeRealTime

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_cbf_quaternion`
              - Add attitude data based on a time-ordered set of quaternions interpreted relative to CBF.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_quaternion`
              - Add attitude data based on a time-ordered set of quaternions.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_ypr`
              - Add attitude data based on a time-ordered set of yaw, pitch and roll angles.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_eciypr`
              - Add attitude data based on a time-ordered set of yaw, pitch, roll angles in the J2000 ECI coordinate system.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_euler`
              - Add attitude data based on a time-ordered set of Euler angles.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.clear_all`
              - Clear attitude data created using AddXXX commands.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.look_ahead_method`
              - Look ahead method can be extrapolate or hold.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.duration`
              - Get look ahead/look behind duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.data_reference`
              - Returns a reference attitude profile for incoming attitude data.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.block_factor`
              - A block factor used to help size allocated memory used to hold the history.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeRealTime


Property detail
---------------

.. py:property:: look_ahead_method
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.look_ahead_method
    :type: VEHICLE_LOOK_AHEAD_METHOD

    Look ahead method can be extrapolate or hold.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.duration
    :type: IVehicleDuration

    Get look ahead/look behind duration.

.. py:property:: data_reference
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.data_reference
    :type: IVehicleAttitudeRealTimeDataReference

    Returns a reference attitude profile for incoming attitude data.

.. py:property:: block_factor
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.block_factor
    :type: int

    A block factor used to help size allocated memory used to hold the history.


Method detail
-------------




.. py:method:: add_cbf_quaternion(self, time: typing.Any, q1: float, q2: float, q3: float, q4: float) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_cbf_quaternion

    Add attitude data based on a time-ordered set of quaternions interpreted relative to CBF.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **q1** : :obj:`~float`
    **q2** : :obj:`~float`
    **q3** : :obj:`~float`
    **q4** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add_quaternion(self, time: typing.Any, q1: float, q2: float, q3: float, q4: float) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_quaternion

    Add attitude data based on a time-ordered set of quaternions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **q1** : :obj:`~float`
    **q2** : :obj:`~float`
    **q3** : :obj:`~float`
    **q4** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add_ypr(self, time: typing.Any, sequence: str, yaw: float, pitch: float, roll: float) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_ypr

    Add attitude data based on a time-ordered set of yaw, pitch and roll angles.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **sequence** : :obj:`~str`
    **yaw** : :obj:`~float`
    **pitch** : :obj:`~float`
    **roll** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add_eciypr(self, time: typing.Any, sequence: str, yaw: float, pitch: float, roll: float) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_eciypr

    Add attitude data based on a time-ordered set of yaw, pitch, roll angles in the J2000 ECI coordinate system.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **sequence** : :obj:`~str`
    **yaw** : :obj:`~float`
    **pitch** : :obj:`~float`
    **roll** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add_euler(self, time: typing.Any, sequence: str, angle1: float, angle2: float, angle3: float) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.add_euler

    Add attitude data based on a time-ordered set of Euler angles.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **sequence** : :obj:`~str`
    **angle1** : :obj:`~float`
    **angle2** : :obj:`~float`
    **angle3** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: clear_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTime.clear_all

    Clear attitude data created using AddXXX commands.

    :Returns:

        :obj:`~None`




