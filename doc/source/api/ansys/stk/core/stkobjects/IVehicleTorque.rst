IVehicleTorque
==============

.. py:class:: IVehicleTorque

   object
   
   Torque file to use in defining integrated attitude.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_torque_file`
            * - :py:meth:`~torque_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTorque


Property detail
---------------

.. py:property:: use_torque_file
    :canonical: ansys.stk.core.stkobjects.IVehicleTorque.use_torque_file
    :type: bool

    Opt whether to use an external torque file.

.. py:property:: torque_file
    :canonical: ansys.stk.core.stkobjects.IVehicleTorque.torque_file
    :type: str

    Name of external torque (.tq) file. Torque files define a time-ordered list of body-fixed torques to be applied to the satellite.


