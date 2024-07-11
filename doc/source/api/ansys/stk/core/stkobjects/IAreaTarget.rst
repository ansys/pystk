IAreaTarget
===========

.. py:class:: ansys.stk.core.stkobjects.IAreaTarget

   object
   
   Provide access to the properties and methods defining an AreaTarget object.

.. py:currentmodule:: IAreaTarget

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.use_local_time_offset`
              - Opt whether to use a local time offset from GMT.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.local_time_offset`
              - The amount of the time offset from GMT, if this option is used. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.auto_centroid`
              - Opt whether to have the centroid automatically computed.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.position`
              - Get the position of the area target centroid.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.access_constraints`
              - Get the constraints imposed on the area target. Basic constraints for area targets apply to all points within or along the area target. If the constraint is satisfied for at least one point, access to the area target is considered valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.graphics`
              - Get the area target's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.graphics_3d`
              - Get the area target's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.area_type`
              - The method for defining the area target boundary. A member of the AgEAreaType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.area_type_data`
              - Get the data defining the boundary with the selected method.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.use_terrain_data`
              - Opt whether to use terrain data for altitude updates.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.allow_object_access`
              - Opt whether access to the object is constrained with respect to the entire object, as opposed to any part of it.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTarget.common_tasks`
              - Common tasks associated with AreaTargets.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAreaTarget


Property detail
---------------

.. py:property:: use_local_time_offset
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.use_local_time_offset
    :type: bool

    Opt whether to use a local time offset from GMT.

.. py:property:: local_time_offset
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.local_time_offset
    :type: float

    The amount of the time offset from GMT, if this option is used. Uses Time Dimension.

.. py:property:: auto_centroid
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.auto_centroid
    :type: bool

    Opt whether to have the centroid automatically computed.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.position
    :type: IPosition

    Get the position of the area target centroid.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.access_constraints
    :type: IAccessConstraintCollection

    Get the constraints imposed on the area target. Basic constraints for area targets apply to all points within or along the area target. If the constraint is satisfied for at least one point, access to the area target is considered valid.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.graphics
    :type: IAreaTargetGraphics

    Get the area target's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.graphics_3d
    :type: IAreaTargetGraphics3D

    Get the area target's 3D Graphics properties.

.. py:property:: area_type
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.area_type
    :type: AREA_TYPE

    The method for defining the area target boundary. A member of the AgEAreaType enumeration.

.. py:property:: area_type_data
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.area_type_data
    :type: IAreaTypeData

    Get the data defining the boundary with the selected method.

.. py:property:: use_terrain_data
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.use_terrain_data
    :type: bool

    Opt whether to use terrain data for altitude updates.

.. py:property:: allow_object_access
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.allow_object_access
    :type: bool

    Opt whether access to the object is constrained with respect to the entire object, as opposed to any part of it.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.IAreaTarget.common_tasks
    :type: IAreaTargetCommonTasks

    Common tasks associated with AreaTargets.


