AreaTarget
==========

.. py:class:: ansys.stk.core.stkobjects.AreaTarget

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining the AreaTarget object.

.. py:currentmodule:: AreaTarget

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.use_local_time_offset`
              - Opt whether to use a local time offset from GMT.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.local_time_offset`
              - The amount of the time offset from GMT, if this option is used. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.automatic_computation_of_centroid`
              - Opt whether to have the centroid automatically computed.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.position`
              - Get the position of the area target centroid.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.access_constraints`
              - Get the constraints imposed on the area target. Basic constraints for area targets apply to all points within or along the area target. If the constraint is satisfied for at least one point, access to the area target is considered valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.graphics`
              - Get the area target's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.graphics_3d`
              - Get the area target's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.area_type`
              - The method for defining the area target boundary. A member of the AgEAreaType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.area_type_data`
              - Get the data defining the boundary with the selected method.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.use_terrain_data`
              - Opt whether to use terrain data for altitude updates.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.allow_object_access`
              - Opt whether access to the object is constrained with respect to the entire object, as opposed to any part of it.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTarget.common_tasks`
              - Common tasks associated with AreaTargets.



Examples
--------

List all points in an area target

.. code-block:: python

    # AreaTarget areaTarget: AreaTarget object
    if areaTarget.area_type == AreaType.PATTERN:
        # Get IAgAreaTypePatternCollection interface from AreaTypeData
        patternPoints = areaTarget.area_type_data

        # ToArray returns a two dimensional array of latitude and longitude points
        areaTargetPoints = patternPoints.to_array()

        print("All points in Area Target")
        for i in range(0, len(areaTargetPoints)):
            print("Latitude: %s Longitude: %s" % (str(areaTargetPoints[i][0]), str(areaTargetPoints[i][1])))


Define area target boundary and position from list of lat/lon/alt (using common tasks)

.. code-block:: python

    # AreaTarget areaTarget: AreaTarget object
    # Remove all points in the area target
    areaTarget.area_type_data.remove_all()

    # By using the CommonTasks interface,
    # make an array of lattitude and longitude boundary points
    boundary = [[29, -12], [29, 34], [6, 34], [6, -12]]

    # SetAreaTypePattern expects a two dimensional array of latitude and longitude values
    areaTarget.common_tasks.set_area_type_pattern(boundary)


Define area target boundary and position from list of lat/lon/alt

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AreaTarget areaTarget: AreaTarget object

    # By using the fine grained interfaces,
    # BeginUpdate/EndUpdate prevent intermediate redraws
    root.begin_update()
    areaTarget.area_type = AreaType.PATTERN
    patterns = areaTarget.area_type_data
    patterns.add(48.897, 18.637)
    patterns.add(46.534, 13.919)
    patterns.add(44.173, 21.476)
    root.end_update()
    areaTarget.automatic_computation_of_centroid = True


Set an elliptical area target (using common tasks)

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AreaTarget areaTarget: AreaTarget object

    # By using the CommonTasks interface
    areaTarget.common_tasks.set_area_type_ellipse(85.25, 80.75, 44)


Set an elliptical area target

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AreaTarget areaTarget: AreaTarget object

    # By using the fine grained interfaces,
    # BeginUpdate/EndUpdate prevent intermediate redraws
    root.begin_update()
    areaTarget.area_type = AreaType.ELLIPSE
    ellipse = areaTarget.area_type_data
    ellipse.semi_major_axis = 85.25  # in km (distance dimension)
    ellipse.semi_minor_axis = 80.75  # in km (distance dimension)
    ellipse.bearing = 44  # in deg (angle dimension)
    root.end_update()


Create an area target (on the current scenario central body)

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root

    # Create the AreaTarget on the current scenario central body (use
    # NewOnCentralBody to specify explicitly the central body)
    areaTarget = root.current_scenario.children.new(STKObjectType.AREA_TARGET, "MyAreaTarget")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AreaTarget


Property detail
---------------

.. py:property:: use_local_time_offset
    :canonical: ansys.stk.core.stkobjects.AreaTarget.use_local_time_offset
    :type: bool

    Opt whether to use a local time offset from GMT.

.. py:property:: local_time_offset
    :canonical: ansys.stk.core.stkobjects.AreaTarget.local_time_offset
    :type: float

    The amount of the time offset from GMT, if this option is used. Uses Time Dimension.

.. py:property:: automatic_computation_of_centroid
    :canonical: ansys.stk.core.stkobjects.AreaTarget.automatic_computation_of_centroid
    :type: bool

    Opt whether to have the centroid automatically computed.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.AreaTarget.position
    :type: IPosition

    Get the position of the area target centroid.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.AreaTarget.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the area target. Basic constraints for area targets apply to all points within or along the area target. If the constraint is satisfied for at least one point, access to the area target is considered valid.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.AreaTarget.graphics
    :type: AreaTargetGraphics

    Get the area target's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.AreaTarget.graphics_3d
    :type: AreaTargetGraphics3D

    Get the area target's 3D Graphics properties.

.. py:property:: area_type
    :canonical: ansys.stk.core.stkobjects.AreaTarget.area_type
    :type: AreaType

    The method for defining the area target boundary. A member of the AgEAreaType enumeration.

.. py:property:: area_type_data
    :canonical: ansys.stk.core.stkobjects.AreaTarget.area_type_data
    :type: IAreaTypeData

    Get the data defining the boundary with the selected method.

.. py:property:: use_terrain_data
    :canonical: ansys.stk.core.stkobjects.AreaTarget.use_terrain_data
    :type: bool

    Opt whether to use terrain data for altitude updates.

.. py:property:: allow_object_access
    :canonical: ansys.stk.core.stkobjects.AreaTarget.allow_object_access
    :type: bool

    Opt whether access to the object is constrained with respect to the entire object, as opposed to any part of it.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.AreaTarget.common_tasks
    :type: AreaTargetCommonTasks

    Common tasks associated with AreaTargets.


