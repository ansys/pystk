IVehicleTrajectoryGraphics3DModel
=================================

.. py:class:: IVehicleTrajectoryGraphics3DModel

   IGraphics3DModel
   
   Marker interface for launch vehicle or missile.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~trajectory_marker`
            * - :py:meth:`~ground_marker`
            * - :py:meth:`~is_point_visible`
            * - :py:meth:`~point_size`
            * - :py:meth:`~gltf_reflection_map_type`
            * - :py:meth:`~gltf_image_based`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTrajectoryGraphics3DModel


Property detail
---------------

.. py:property:: trajectory_marker
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryGraphics3DModel.trajectory_marker
    :type: IAgVOMarker

    Represents the vehicle while traveling along its actual trajectory.

.. py:property:: ground_marker
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryGraphics3DModel.ground_marker
    :type: IAgVOMarker

    Represents the vehicle's position along its ground track.

.. py:property:: is_point_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryGraphics3DModel.is_point_visible
    :type: bool

    Whether the point that is shown at certain viewing distances to represent an object, is visible.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryGraphics3DModel.point_size
    :type: typing.Any

    A size of the point (in pixels). Dimensionless.

.. py:property:: gltf_reflection_map_type
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryGraphics3DModel.gltf_reflection_map_type
    :type: MODEL_GLTF_REFLECTION_MAP_TYPE

    Gets or sets the glTF reflection map type property. A member of the AgEModelGltfReflectionMapType enumeration.

.. py:property:: gltf_image_based
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryGraphics3DModel.gltf_image_based
    :type: IAgVOModelGltfImageBased

    Gets the glTF Image Based properties.


