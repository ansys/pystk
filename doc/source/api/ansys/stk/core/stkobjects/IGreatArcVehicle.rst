IGreatArcVehicle
================

.. py:class:: IGreatArcVehicle

   object
   
   A base interface for all Great Arc Vehicles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_route_type`
              - Set the propagator type.
            * - :py:meth:`~is_route_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:meth:`~set_attitude_type`
              - Set the type of attitude profile.
            * - :py:meth:`~is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~route_type`
            * - :py:meth:`~route_supported_types`
            * - :py:meth:`~route`
            * - :py:meth:`~attitude_type`
            * - :py:meth:`~attitude_supported_types`
            * - :py:meth:`~attitude`
            * - :py:meth:`~ground_ellipses`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~eclipse_bodies`
            * - :py:meth:`~use_terrain_in_lighting_computations`
            * - :py:meth:`~lighting_max_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGreatArcVehicle


Property detail
---------------

.. py:property:: route_type
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.route_type
    :type: VEHICLE_PROPAGATOR_TYPE

    Get the propagator type.

.. py:property:: route_supported_types
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.route_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: route
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.route
    :type: IAgVePropagator

    Get the route properties.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.attitude_type
    :type: VEHICLE_ATTITUDE

    Get the type of attitude profile.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.attitude_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.attitude
    :type: IAgVeAttitude

    Get the  attitude profile.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.ground_ellipses
    :type: IAgVeGroundEllipsesCollection

    Get the  ground ellipses properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.access_constraints
    :type: IAgAccessConstraintCollection

    Get the constraints imposed on the vehicle.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.eclipse_bodies
    :type: IAgVeEclipseBodies

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.lighting_max_step
    :type: float

    This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.


Method detail
-------------


.. py:method:: set_route_type(self, route: VEHICLE_PROPAGATOR_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.set_route_type

    Set the propagator type.

    :Parameters:

    **route** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_route_type_supported(self, route: VEHICLE_PROPAGATOR_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.is_route_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **route** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~bool`




.. py:method:: set_attitude_type(self, attitude: VEHICLE_ATTITUDE) -> None
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.set_attitude_type

    Set the type of attitude profile.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~None`

.. py:method:: is_attitude_type_supported(self, attitude: VEHICLE_ATTITUDE) -> bool
    :canonical: ansys.stk.core.stkobjects.IGreatArcVehicle.is_attitude_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~bool`










