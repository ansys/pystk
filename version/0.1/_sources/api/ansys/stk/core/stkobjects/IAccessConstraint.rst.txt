IAccessConstraint
=================

.. py:class:: ansys.stk.core.stkobjects.IAccessConstraint

   AccessConstraint used to access the AccessConstraint attributes.

.. py:currentmodule:: IAccessConstraint

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.constraint_name`
              - Property used to access the constraint name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.is_plugin`
              - Return true if the access constraint is a plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.exclusion_interval`
              - Exclude Time Intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.constraint_type`
              - Property used to access the constraint type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.maximum_time_step`
              - Maximum time step used in adaptive sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.maximum_relative_motion`
              - Maximum relative motion used in adaptive sampling.


Examples
--------

Get access between objects by path using the existing accesses

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    scenario = root.current_scenario
    accesses = scenario.get_existing_accesses()

    size = len(accesses)  # number of accesses

    object1 = accesses[0][0]  # e.g. "Satellite/MySatellite"
    object2 = accesses[0][1]  # e.g.  "Facility/MyFacility"
    computed = accesses[0][2]  # e.g. True  (if access has been computed)

    access = scenario.get_access_between_objects_by_path(object1, object2)


Configure the access interval to the availability time span of the object where access is being computed to

.. code-block:: python

    # STKObjectRoot root: STK Object Model root

    satellite = root.get_object_from_path("Satellite/MySatellite")
    facility = root.get_object_from_path("Facility/MyFacility")
    access = satellite.get_access_to_object(facility)

    access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
    accessTimePeriod = access.access_time_period_data

    if satellite.analysis_workbench_components.time_intervals.contains("AvailabilityTimeSpan"):
        availabilityTimeSpan = satellite.analysis_workbench_components.time_intervals.item("AvailabilityTimeSpan")
        accessTimePeriod.access_interval.set_implicit_interval(availabilityTimeSpan)


Remove all access constraints except for Line Of Sight

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    for i in range(accessConstraints.count - 1, 0, -1):
        constraint = accessConstraints.Item(i).ConstraintName

        if (constraint == "LineOfSight") is False:
            if constraint == "ThirdBodyObstruction":
                thirdBodyConstraint = accessConstraints.GetActiveNamedConstraint("ThirdBodyObstruction")
                assignedArray = thirdBodyConstraint.AssignedObstructions

                for j in range(0, len(assignedArray)):
                    thirdBodyConstraint.RemoveObstruction(assignedArray[j])

            elif constraint == "ExclusionZone":
                accessConstraints.GetActiveNamedConstraint("ExclusionZone").RemoveAll()

            else:
                accessConstraints.RemoveNamedConstraint(constraint)


Add an Exclusion Zone access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    excludeZone = accessConstraints.add_named_constraint("ExclusionZone")
    excludeZone.maximum_latitude = 45
    excludeZone.minimum_latitude = 15
    excludeZone.minimum_longitude = -75
    excludeZone.maximum_longitude = -35


Add multiple access constraints of the same type to an STK Object

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # Add constraints
    # Only the eCstrApparentTime (4), eCstrDuration (13), eCstrGMT (16), eCstrIntervals (22), eCstrLocalTime (27) constraint
    # types can be added multiple times to the constraint collection.
    time1 = accessConstraints.add_constraint(AccessConstraintType.LOCAL_TIME)
    time1.minimum = "00:00:00.000"
    time1.maximum = "23:00:00.000"


Add and configure an altitude access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
    # Attitude constraint
    altitude = accessConstraints.add_constraint(AccessConstraintType.ALTITUDE)
    altitude.enable_minimum = True
    altitude.minimum = 20.5  # km


Add and configure a central body obstruction access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    # Get IAgAccessCnstrCbObstruction interface
    cbObstrConstraint = accessConstraints.add_constraint(AccessConstraintType.CENTRAL_BODY_OBSTRUCTION)

    # AvailableObstructions returns a one dimensional array of obstruction paths
    availableArray = cbObstrConstraint.available_obstructions

    # In this example add all available obstructions
    print("Available obstructions")
    for i in range(0, len(availableArray)):
        print(availableArray[i])
        if availableArray[i] != "Sun":  # Sun is enabled by default
            cbObstrConstraint.add_obstruction(availableArray[i])

    # AssignedObstructions returns a one dimensional array of obstruction paths
    assignedArray = cbObstrConstraint.assigned_obstructions

    print("Assigned obstructions")
    for i in range(0, len(assignedArray)):
        print(assignedArray[i])


Add and configure a sun elevation angle access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
    minmax = accessConstraints.add_constraint(AccessConstraintType.SUN_ELEVATION_ANGLE)
    minmax.enable_minimum = True
    minmax.minimum = 22.2
    minmax.enable_maximum = True
    minmax.maximum = 77.7


Add and configure a lunar elevation angle access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
    minmax = accessConstraints.add_constraint(AccessConstraintType.LUNAR_ELEVATION_ANGLE)
    minmax.enable_minimum = True
    minmax.minimum = 11.1
    minmax.enable_maximum = True
    minmax.maximum = 88.8


Add and configure a Line Of Sight sun exclusion access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # Angle constraint
    cnstrAngle = accessConstraints.add_constraint(AccessConstraintType.LIGHT_OF_SIGHT_SOLAR_EXCLUSION_ANGLE)
    cnstrAngle.angle = 176.0


Add and configure a lighting condition access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # Condition constraint
    light = accessConstraints.add_constraint(AccessConstraintType.LIGHTING)
    light.condition = ConstraintLighting.DIRECT_SUN


Return a list of available constraints

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    constraintArray = accessConstraints.available_constraints()

    print("List of Available Constraints:")
    for i in range(0, len(constraintArray)):
        print(constraintArray[i])


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraint


Property detail
---------------

.. py:property:: constraint_name
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.constraint_name
    :type: str

    Property used to access the constraint name.

.. py:property:: is_plugin
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.is_plugin
    :type: bool

    Return true if the access constraint is a plugin.

.. py:property:: exclusion_interval
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.exclusion_interval
    :type: bool

    Exclude Time Intervals.

.. py:property:: constraint_type
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.constraint_type
    :type: AccessConstraintType

    Property used to access the constraint type.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.maximum_time_step
    :type: float

    Maximum time step used in adaptive sampling.

.. py:property:: maximum_relative_motion
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.maximum_relative_motion
    :type: float

    Maximum relative motion used in adaptive sampling.


