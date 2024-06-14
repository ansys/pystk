IVehicleIntegratedAttitude
==========================

.. py:class:: IVehicleIntegratedAttitude

   object
   
   Integrated Attitude interface generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~init_from_attitude`
              - Initialize the parameters using a satellite's attitude.
            * - :py:meth:`~save_to_file`
              - Generate an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite and save results to the specified file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~epoch`
            * - :py:meth:`~orientation`
            * - :py:meth:`~wx`
            * - :py:meth:`~wy`
            * - :py:meth:`~wz`
            * - :py:meth:`~torque`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleIntegratedAttitude


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.start_time
    :type: typing.Any

    Start time for the attitude file. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.stop_time
    :type: typing.Any

    Stop time for the attitude file. Uses DateFormat Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.epoch
    :type: typing.Any

    Epoch of the attitude file. Uses DateFormat Dimension.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.orientation
    :type: "IAgOrientation"

    Get the initial orientation of the satellite in the Earth Inertial (ECI) frame.

.. py:property:: wx
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.wx
    :type: float

    Body fixed wx rate: initial angular velocity rate about the satellite's X axis. Uses AngleRate Dimension.

.. py:property:: wy
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.wy
    :type: float

    Body fixed wy rate:  initial angular velocity rate about the satellite's Y axis. Uses AngleRate Dimension.

.. py:property:: wz
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.wz
    :type: float

    Body fixed wz rate:  initial angular velocity rate about the satellite's Z axis. Uses AngleRate Dimension.

.. py:property:: torque
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegratedAttitude.torque
    :type: "IAgVeTorque"

    Get the external torque data.


Method detail
-------------















.. py:method:: init_from_attitude(self) -> None

    Initialize the parameters using a satellite's attitude.

    :Returns:

        :obj:`~None`

.. py:method:: save_to_file(self, filename:str) -> None

    Generate an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite and save results to the specified file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

