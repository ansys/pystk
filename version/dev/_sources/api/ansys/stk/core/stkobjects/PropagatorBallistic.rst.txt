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

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.is_impact_location_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.is_launch_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.propagate`
              - Propagates the missile's path using the specified time interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.set_impact_location_type`
              - Set the impact location type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.set_launch_type`
              - Set flight parameters type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.impact_location`
              - Get the impact location.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_type`
              - Get impact location type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.launch`
              - Get launch parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.launch_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.launch_type`
              - Get flight parameters type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorBallistic.step`
              - Step size. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorBallistic


Property detail
---------------

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: impact_location
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.impact_location
    :type: IVehicleImpactLocation

    Get the impact location.

.. py:property:: impact_location_supported_types
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: impact_location_type
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.impact_location_type
    :type: VehicleImpactLocation

    Get impact location type.

.. py:property:: launch
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.launch
    :type: IVehicleLaunch

    Get launch parameters.

.. py:property:: launch_supported_types
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.launch_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: launch_type
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.launch_type
    :type: VehicleLaunch

    Get flight parameters type.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.step
    :type: float

    Step size. Uses Time Dimension.


Method detail
-------------





.. py:method:: is_impact_location_type_supported(self, impact_location: VehicleImpactLocation) -> bool
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.is_impact_location_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **impact_location** : :obj:`~VehicleImpactLocation`


    :Returns:

        :obj:`~bool`

.. py:method:: is_launch_type_supported(self, launch: VehicleLaunch) -> bool
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.is_launch_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **launch** : :obj:`~VehicleLaunch`


    :Returns:

        :obj:`~bool`




.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.propagate

    Propagates the missile's path using the specified time interval.

    :Returns:

        :obj:`~None`

.. py:method:: set_impact_location_type(self, impact_location: VehicleImpactLocation) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.set_impact_location_type

    Set the impact location type.

    :Parameters:

        **impact_location** : :obj:`~VehicleImpactLocation`


    :Returns:

        :obj:`~None`

.. py:method:: set_launch_type(self, launch: VehicleLaunch) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorBallistic.set_launch_type

    Set flight parameters type.

    :Parameters:

        **launch** : :obj:`~VehicleLaunch`


    :Returns:

        :obj:`~None`



