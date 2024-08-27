VehicleTorque
=============

.. py:class:: ansys.stk.core.stkobjects.VehicleTorque

   Torque file to use in defining integrated attitude.

.. py:currentmodule:: VehicleTorque

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTorque.use_torque_file`
              - Opt whether to use an external torque file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTorque.torque_file`
              - Name of external torque (.tq) file. Torque files define a time-ordered list of body-fixed torques to be applied to the satellite.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleTorque


Property detail
---------------

.. py:property:: use_torque_file
    :canonical: ansys.stk.core.stkobjects.VehicleTorque.use_torque_file
    :type: bool

    Opt whether to use an external torque file.

.. py:property:: torque_file
    :canonical: ansys.stk.core.stkobjects.VehicleTorque.torque_file
    :type: str

    Name of external torque (.tq) file. Torque files define a time-ordered list of body-fixed torques to be applied to the satellite.


