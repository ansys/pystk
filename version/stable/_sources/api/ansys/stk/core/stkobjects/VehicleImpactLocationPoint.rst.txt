VehicleImpactLocationPoint
==========================

.. py:class:: ansys.stk.core.stkobjects.VehicleImpactLocationPoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleImpactLocation`

   Class defining a Missile's impact location.

.. py:currentmodule:: VehicleImpactLocationPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.set_impact_type`
              - Set the impact type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.is_impact_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.set_launch_control_type`
              - Set the flight parameter type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.is_launch_control_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.impact_type`
              - Get the impact type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.impact_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.impact`
              - Get the impact point.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.launch_control_type`
              - Get the flight parameter type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.launch_control_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint.launch_control`
              - Get the flight parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleImpactLocationPoint


Property detail
---------------

.. py:property:: impact_type
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.impact_type
    :type: VehicleImpact

    Get the impact type.

.. py:property:: impact_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.impact_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: impact
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.impact
    :type: IVehicleImpact

    Get the impact point.

.. py:property:: launch_control_type
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.launch_control_type
    :type: VehicleLaunchControl

    Get the flight parameter type.

.. py:property:: launch_control_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.launch_control_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: launch_control
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.launch_control
    :type: IVehicleLaunchControl

    Get the flight parameters.


Method detail
-------------


.. py:method:: set_impact_type(self, impact: VehicleImpact) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.set_impact_type

    Set the impact type.

    :Parameters:

        **impact** : :obj:`~VehicleImpact`


    :Returns:

        :obj:`~None`

.. py:method:: is_impact_type_supported(self, impact: VehicleImpact) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.is_impact_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **impact** : :obj:`~VehicleImpact`


    :Returns:

        :obj:`~bool`




.. py:method:: set_launch_control_type(self, launch_control: VehicleLaunchControl) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.set_launch_control_type

    Set the flight parameter type.

    :Parameters:

        **launch_control** : :obj:`~VehicleLaunchControl`


    :Returns:

        :obj:`~None`

.. py:method:: is_launch_control_type_supported(self, launch_control: VehicleLaunchControl) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationPoint.is_launch_control_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **launch_control** : :obj:`~VehicleLaunchControl`


    :Returns:

        :obj:`~bool`



