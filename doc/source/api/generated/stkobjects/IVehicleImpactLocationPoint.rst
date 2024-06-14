IVehicleImpactLocationPoint
===========================

.. py:class:: IVehicleImpactLocationPoint

   object
   
   Missile impact point interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_impact_type`
              - Set the impact type.
            * - :py:meth:`~is_impact_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:meth:`~set_launch_control_type`
              - Set the flight parameter type.
            * - :py:meth:`~is_launch_control_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~impact_type`
            * - :py:meth:`~impact_supported_types`
            * - :py:meth:`~impact`
            * - :py:meth:`~launch_control_type`
            * - :py:meth:`~launch_control_supported_types`
            * - :py:meth:`~launch_control`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleImpactLocationPoint


Property detail
---------------

.. py:property:: impact_type
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLocationPoint.impact_type
    :type: "VEHICLE_IMPACT"

    Get the impact type.

.. py:property:: impact_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLocationPoint.impact_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: impact
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLocationPoint.impact
    :type: "IAgVeImpact"

    Get the impact point.

.. py:property:: launch_control_type
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLocationPoint.launch_control_type
    :type: "VEHICLE_LAUNCH_CONTROL"

    Get the flight parameter type.

.. py:property:: launch_control_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLocationPoint.launch_control_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: launch_control
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLocationPoint.launch_control
    :type: "IAgVeLaunchControl"

    Get the flight parameters.


Method detail
-------------


.. py:method:: set_impact_type(self, impact:"VEHICLE_IMPACT") -> None

    Set the impact type.

    :Parameters:

    **impact** : :obj:`~"VEHICLE_IMPACT"`

    :Returns:

        :obj:`~None`

.. py:method:: is_impact_type_supported(self, impact:"VEHICLE_IMPACT") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **impact** : :obj:`~"VEHICLE_IMPACT"`

    :Returns:

        :obj:`~bool`




.. py:method:: set_launch_control_type(self, launchControl:"VEHICLE_LAUNCH_CONTROL") -> None

    Set the flight parameter type.

    :Parameters:

    **launchControl** : :obj:`~"VEHICLE_LAUNCH_CONTROL"`

    :Returns:

        :obj:`~None`

.. py:method:: is_launch_control_type_supported(self, launchControl:"VEHICLE_LAUNCH_CONTROL") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **launchControl** : :obj:`~"VEHICLE_LAUNCH_CONTROL"`

    :Returns:

        :obj:`~bool`



