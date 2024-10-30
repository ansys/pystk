PropagatorBallistic
===================

.. py:class:: ansys.stk.core.stkobjects.PropagatorBallistic

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the ballistic propagator for a Missile.

.. py:currentmodule:: PropagatorBallistic

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.propagate`
              - Propagates the missile's path using the specified time interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.set_launch_type`
              - Set flight parameters type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.is_launch_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.set_impact_location_type`
              - Set the impact location type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.is_impact_location_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.launch_type`
              - Get flight parameters type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.launch_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.launch`
              - Get launch parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_type`
              - Get impact location type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.impact_location`
              - Get the impact location.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorBallistic


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: launch_type
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.launch_type
    :type: VEHICLE_LAUNCH

    Get flight parameters type.

.. py:property:: launch_supported_types
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.launch_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: launch
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.launch
    :type: IVehicleLaunch

    Get launch parameters.

.. py:property:: impact_location_type
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_type
    :type: VEHICLE_IMPACT_LOCATION

    Get impact location type.

.. py:property:: impact_location_supported_types
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: impact_location
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.impact_location
    :type: IVehicleImpactLocation

    Get the impact location.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.propagate

    Propagates the missile's path using the specified time interval.

    :Returns:

        :obj:`~None`




.. py:method:: set_launch_type(self, launch: VEHICLE_LAUNCH) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.set_launch_type

    Set flight parameters type.

    :Parameters:

    **launch** : :obj:`~VEHICLE_LAUNCH`

    :Returns:

        :obj:`~None`

.. py:method:: is_launch_type_supported(self, launch: VEHICLE_LAUNCH) -> bool
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.is_launch_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **launch** : :obj:`~VEHICLE_LAUNCH`

    :Returns:

        :obj:`~bool`




.. py:method:: set_impact_location_type(self, impactLocation: VEHICLE_IMPACT_LOCATION) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.set_impact_location_type

    Set the impact location type.

    :Parameters:

    **impactLocation** : :obj:`~VEHICLE_IMPACT_LOCATION`

    :Returns:

        :obj:`~None`

.. py:method:: is_impact_location_type_supported(self, impactLocation: VEHICLE_IMPACT_LOCATION) -> bool
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.is_impact_location_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **impactLocation** : :obj:`~VEHICLE_IMPACT_LOCATION`

    :Returns:

        :obj:`~bool`




