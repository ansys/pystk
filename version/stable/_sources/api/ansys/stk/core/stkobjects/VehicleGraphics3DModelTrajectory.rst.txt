VehicleGraphics3DModelTrajectory
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DModel`

   Marker for launch vehicle or missile.

.. py:currentmodule:: VehicleGraphics3DModelTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.trajectory_marker`
              - Represents the vehicle while traveling along its actual trajectory.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.ground_marker`
              - Represents the vehicle's position along its ground track.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.show_point`
              - Whether the point that is shown at certain viewing distances to represent an object, is visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.point_size`
              - A size of the point (in pixels). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.gltf_reflection_map_type`
              - Get or set the glTF reflection map type property. A member of the ModelGltfReflectionMapType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.gltf_image_based`
              - Get the glTF Image Based properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DModelTrajectory


Property detail
---------------

.. py:property:: trajectory_marker
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.trajectory_marker
    :type: Graphics3DMarker

    Represents the vehicle while traveling along its actual trajectory.

.. py:property:: ground_marker
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.ground_marker
    :type: Graphics3DMarker

    Represents the vehicle's position along its ground track.

.. py:property:: show_point
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.show_point
    :type: bool

    Whether the point that is shown at certain viewing distances to represent an object, is visible.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.point_size
    :type: typing.Any

    A size of the point (in pixels). Dimensionless.

.. py:property:: gltf_reflection_map_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.gltf_reflection_map_type
    :type: ModelGltfReflectionMapType

    Get or set the glTF reflection map type property. A member of the ModelGltfReflectionMapType enumeration.

.. py:property:: gltf_image_based
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory.gltf_image_based
    :type: Graphics3DModelglTFImageBased

    Get the glTF Image Based properties.


