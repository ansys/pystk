VehicleAttitudePointing
=======================

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitudePointing

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePointing`

   Target pointing attitude parameters.

.. py:currentmodule:: VehicleAttitudePointing

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudePointing.advanced`
              - Returns advanced targeting access computation properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudePointing.target_slew`
              - Define the time required for the vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAttitudePointing


Property detail
---------------

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudePointing.advanced
    :type: IVehicleAccessAdvanced

    Returns advanced targeting access computation properties.

.. py:property:: target_slew
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudePointing.target_slew
    :type: IVehicleAttitudeTargetSlew

    Define the time required for the vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.


