IPointTargetGraphics3DModel
===========================

.. py:class:: ansys.stk.core.stkobjects.IPointTargetGraphics3DModel

   IGraphics3DModel
   
   AgPtTargetVOModel used to access the 3D model attributes.

.. py:currentmodule:: IPointTargetGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.marker`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.is_point_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.point_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.gltf_reflection_map_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.gltf_image_based`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPointTargetGraphics3DModel


Property detail
---------------

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.marker
    :type: IGraphics3DMarker

    VO Marker attributes.

.. py:property:: is_point_visible
    :canonical: ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.is_point_visible
    :type: bool

    Whether the point that is shown at certain viewing distances to represent an object, is visible.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.point_size
    :type: typing.Any

    A size of the point (in pixels).

.. py:property:: gltf_reflection_map_type
    :canonical: ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.gltf_reflection_map_type
    :type: MODEL_GLTF_REFLECTION_MAP_TYPE

    Gets or sets the glTF reflection map type property. A member of the AgEModelGltfReflectionMapType enumeration.

.. py:property:: gltf_image_based
    :canonical: ansys.stk.core.stkobjects.IPointTargetGraphics3DModel.gltf_image_based
    :type: IGraphics3DModelGltfImageBased

    Gets the glTF Image Based properties.


