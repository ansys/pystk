VehicleIntegratedAttitude
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleIntegratedAttitude

   Integrated Attitude generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

.. py:currentmodule:: VehicleIntegratedAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.initialize_from_attitude`
              - Initialize the parameters using a satellite's attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.save_to_file`
              - Generate an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite and save results to the specified file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.start_time`
              - Start time for the attitude file. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.stop_time`
              - Stop time for the attitude file. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.epoch`
              - Epoch of the attitude file. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.orientation`
              - Get the initial orientation of the satellite in the Earth Inertial (ECI) frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.wx`
              - Body fixed wx rate: initial angular velocity rate about the satellite's X axis. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.wy`
              - Body fixed wy rate:  initial angular velocity rate about the satellite's Y axis. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.wz`
              - Body fixed wz rate:  initial angular velocity rate about the satellite's Z axis. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude.torque`
              - Get the external torque data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleIntegratedAttitude


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.start_time
    :type: typing.Any

    Start time for the attitude file. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.stop_time
    :type: typing.Any

    Stop time for the attitude file. Uses DateFormat Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.epoch
    :type: typing.Any

    Epoch of the attitude file. Uses DateFormat Dimension.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.orientation
    :type: IOrientation

    Get the initial orientation of the satellite in the Earth Inertial (ECI) frame.

.. py:property:: wx
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.wx
    :type: float

    Body fixed wx rate: initial angular velocity rate about the satellite's X axis. Uses AngleRate Dimension.

.. py:property:: wy
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.wy
    :type: float

    Body fixed wy rate:  initial angular velocity rate about the satellite's Y axis. Uses AngleRate Dimension.

.. py:property:: wz
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.wz
    :type: float

    Body fixed wz rate:  initial angular velocity rate about the satellite's Z axis. Uses AngleRate Dimension.

.. py:property:: torque
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.torque
    :type: AttitudeTorque

    Get the external torque data.


Method detail
-------------















.. py:method:: initialize_from_attitude(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.initialize_from_attitude

    Initialize the parameters using a satellite's attitude.

    :Returns:

        :obj:`~None`

.. py:method:: save_to_file(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleIntegratedAttitude.save_to_file

    Generate an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite and save results to the specified file.

    :Parameters:

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~None`

