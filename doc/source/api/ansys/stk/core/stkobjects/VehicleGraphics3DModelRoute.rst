VehicleGraphics3DModelRoute
===========================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DModel`

   3D marker for great arc vehicles.

.. py:currentmodule:: VehicleGraphics3DModelRoute

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.route_marker`
              - Represents the vehicle while traveling along its route.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.show_point`
              - Whether the point that is shown at certain viewing distances to represent an object, is visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.point_size`
              - A size of the point (in pixels). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.gltf_reflection_map_type`
              - Get or set the glTF reflection map type property. A member of the AgEModelGltfReflectionMapType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.gltf_image_based`
              - Get the glTF Image Based properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DModelRoute


Property detail
---------------

.. py:property:: route_marker
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.route_marker
    :type: Graphics3DMarker

    Represents the vehicle while traveling along its route.

.. py:property:: show_point
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.show_point
    :type: bool

    Whether the point that is shown at certain viewing distances to represent an object, is visible.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.point_size
    :type: typing.Any

    A size of the point (in pixels). Dimensionless.

.. py:property:: gltf_reflection_map_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.gltf_reflection_map_type
    :type: ModelGltfReflectionMapType

    Get or set the glTF reflection map type property. A member of the AgEModelGltfReflectionMapType enumeration.

.. py:property:: gltf_image_based
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute.gltf_image_based
    :type: Graphics3DModelglTFImageBased

    Get the glTF Image Based properties.


