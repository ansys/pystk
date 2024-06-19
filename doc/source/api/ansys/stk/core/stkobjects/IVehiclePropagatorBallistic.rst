IVehiclePropagatorBallistic
===========================

.. py:class:: IVehiclePropagatorBallistic

   IVehiclePropagator
   
   Ballistic propagator interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagate`
              - Propagates the missile's path using the specified time interval.
            * - :py:meth:`~set_launch_type`
              - Set flight parameters type.
            * - :py:meth:`~is_launch_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:meth:`~set_impact_location_type`
              - Set the impact location type.
            * - :py:meth:`~is_impact_location_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~step`
            * - :py:meth:`~launch_type`
            * - :py:meth:`~launch_supported_types`
            * - :py:meth:`~launch`
            * - :py:meth:`~impact_location_type`
            * - :py:meth:`~impact_location_supported_types`
            * - :py:meth:`~impact_location`
            * - :py:meth:`~ephemeris_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorBallistic


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: launch_type
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.launch_type
    :type: VEHICLE_LAUNCH

    Get flight parameters type.

.. py:property:: launch_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.launch_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: launch
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.launch
    :type: IAgVeLaunch

    Get launch parameters.

.. py:property:: impact_location_type
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.impact_location_type
    :type: VEHICLE_IMPACT_LOCATION

    Get impact location type.

.. py:property:: impact_location_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.impact_location_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: impact_location
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.impact_location
    :type: IAgVeImpactLocation

    Get the impact location.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.ephemeris_interval
    :type: IAgCrdnEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.propagate

    Propagates the missile's path using the specified time interval.

    :Returns:

        :obj:`~None`




.. py:method:: set_launch_type(self, launch: VEHICLE_LAUNCH) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.set_launch_type

    Set flight parameters type.

    :Parameters:

    **launch** : :obj:`~VEHICLE_LAUNCH`

    :Returns:

        :obj:`~None`

.. py:method:: is_launch_type_supported(self, launch: VEHICLE_LAUNCH) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.is_launch_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **launch** : :obj:`~VEHICLE_LAUNCH`

    :Returns:

        :obj:`~bool`




.. py:method:: set_impact_location_type(self, impactLocation: VEHICLE_IMPACT_LOCATION) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.set_impact_location_type

    Set the impact location type.

    :Parameters:

    **impactLocation** : :obj:`~VEHICLE_IMPACT_LOCATION`

    :Returns:

        :obj:`~None`

.. py:method:: is_impact_location_type_supported(self, impactLocation: VEHICLE_IMPACT_LOCATION) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorBallistic.is_impact_location_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **impactLocation** : :obj:`~VEHICLE_IMPACT_LOCATION`

    :Returns:

        :obj:`~bool`




