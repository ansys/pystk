VehicleAttitudeTargetSlew
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew

   Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

.. py:currentmodule:: VehicleAttitudeTargetSlew

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.set_slew_mode_type`
              - Select an attitude slew mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.is_slew_mode_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_type`
              - Select an attitude slew mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode`
              - Returns a currently selected attitude slew configuration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAttitudeTargetSlew


Property detail
---------------

.. py:property:: slew_mode_type
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_type
    :type: VEHICLE_SLEW_MODE

    Select an attitude slew mode.

.. py:property:: slew_mode_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: slew_mode
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode
    :type: IVehicleAttitudeSlewBase

    Returns a currently selected attitude slew configuration.


Method detail
-------------


.. py:method:: set_slew_mode_type(self, slew_mode: VEHICLE_SLEW_MODE) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.set_slew_mode_type

    Select an attitude slew mode.

    :Parameters:

    **slew_mode** : :obj:`~VEHICLE_SLEW_MODE`

    :Returns:

        :obj:`~None`

.. py:method:: is_slew_mode_type_supported(self, slew_mode: VEHICLE_SLEW_MODE) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew.is_slew_mode_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **slew_mode** : :obj:`~VEHICLE_SLEW_MODE`

    :Returns:

        :obj:`~bool`



