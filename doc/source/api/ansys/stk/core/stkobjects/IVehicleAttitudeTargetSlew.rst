IVehicleAttitudeTargetSlew
==========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew

   object
   
   Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

.. py:currentmodule:: IVehicleAttitudeTargetSlew

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.set_slew_mode_type`
              - Select an attitude slew mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.is_slew_mode_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.slew_mode_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.slew_mode_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.slew_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeTargetSlew


Property detail
---------------

.. py:property:: slew_mode_type
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.slew_mode_type
    :type: VEHICLE_SLEW_MODE

    Select an attitude slew mode.

.. py:property:: slew_mode_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.slew_mode_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: slew_mode
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.slew_mode
    :type: IVehicleAttitudeSlewBase

    Returns a currently selected attitude slew configuration.


Method detail
-------------


.. py:method:: set_slew_mode_type(self, slewMode: VEHICLE_SLEW_MODE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.set_slew_mode_type

    Select an attitude slew mode.

    :Parameters:

    **slewMode** : :obj:`~VEHICLE_SLEW_MODE`

    :Returns:

        :obj:`~None`

.. py:method:: is_slew_mode_type_supported(self, slewMode: VEHICLE_SLEW_MODE) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTargetSlew.is_slew_mode_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **slewMode** : :obj:`~VEHICLE_SLEW_MODE`

    :Returns:

        :obj:`~bool`



