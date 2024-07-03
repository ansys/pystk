IVehicleRouteGraphics3DModel
============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel

   IGraphics3DModel
   
   3D marker interface for great arc vehicles.

.. py:currentmodule:: IVehicleRouteGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.route_marker`
              - Represents the vehicle while traveling along its route.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.is_point_visible`
              - Whether the point that is shown at certain viewing distances to represent an object, is visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.point_size`
              - A size of the point (in pixels). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.gltf_reflection_map_type`
              - Gets or sets the glTF reflection map type property. A member of the AgEModelGltfReflectionMapType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.gltf_image_based`
              - Gets the glTF Image Based properties.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleRouteGraphics3DModel


Property detail
---------------

.. py:property:: route_marker
    :canonical: ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.route_marker
    :type: IGraphics3DMarker

    Represents the vehicle while traveling along its route.

.. py:property:: is_point_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.is_point_visible
    :type: bool

    Whether the point that is shown at certain viewing distances to represent an object, is visible.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.point_size
    :type: typing.Any

    A size of the point (in pixels). Dimensionless.

.. py:property:: gltf_reflection_map_type
    :canonical: ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.gltf_reflection_map_type
    :type: MODEL_GLTF_REFLECTION_MAP_TYPE

    Gets or sets the glTF reflection map type property. A member of the AgEModelGltfReflectionMapType enumeration.

.. py:property:: gltf_image_based
    :canonical: ansys.stk.core.stkobjects.IVehicleRouteGraphics3DModel.gltf_image_based
    :type: IGraphics3DModelGltfImageBased

    Gets the glTF Image Based properties.


