IGreatArcVehicle
================

.. py:class:: ansys.stk.core.stkobjects.IGreatArcVehicle

   A base interface for all Great Arc Vehicles.

.. py:currentmodule:: IGreatArcVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.set_route_type`
              - Set the propagator type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.is_route_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.set_attitude_type`
              - Set the type of attitude profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.route_type`
              - Get the propagator type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.route_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.route`
              - Get the route properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.attitude_type`
              - Get the type of attitude profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.attitude_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.attitude`
              - Get the  attitude profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.ground_ellipses`
              - Get the  ground ellipses properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.access_constraints`
              - Get the constraints imposed on the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.eclipse_bodies`
              - Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.use_terrain_in_lighting_computations`
              - Opt whether to compute lighting using terrain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcVehicle.lighting_maximum_step`
              - Do not use this property, as it is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGreatArcVehicle


Property detail
---------------

.. py:property:: route_type
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.route_type
    :type: PropagatorType

    Get the propagator type.

.. py:property:: route_supported_types
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.route_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: route
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.route
    :type: IPropagator

    Get the route properties.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.attitude_type
    :type: VehicleAttitude

    Get the type of attitude profile.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.attitude_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.attitude
    :type: IVehicleAttitude

    Get the  attitude profile.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.ground_ellipses
    :type: VehicleGroundEllipsesCollection

    Get the  ground ellipses properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the vehicle.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.eclipse_bodies
    :type: VehicleEclipseBodies

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_maximum_step
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.lighting_maximum_step
    :type: float

    Do not use this property, as it is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.


Method detail
-------------


.. py:method:: set_route_type(self, route: PropagatorType) -> None
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.set_route_type

    Set the propagator type.

    :Parameters:

        **route** : :obj:`~PropagatorType`


    :Returns:

        :obj:`~None`

.. py:method:: is_route_type_supported(self, route: PropagatorType) -> bool
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.is_route_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **route** : :obj:`~PropagatorType`


    :Returns:

        :obj:`~bool`




.. py:method:: set_attitude_type(self, attitude: VehicleAttitude) -> None
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.set_attitude_type

    Set the type of attitude profile.

    :Parameters:

        **attitude** : :obj:`~VehicleAttitude`


    :Returns:

        :obj:`~None`

.. py:method:: is_attitude_type_supported(self, attitude: VehicleAttitude) -> bool
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.is_attitude_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attitude** : :obj:`~VehicleAttitude`


    :Returns:

        :obj:`~bool`










