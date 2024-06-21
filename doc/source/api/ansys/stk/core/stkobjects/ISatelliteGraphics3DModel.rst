ISatelliteGraphics3DModel
=========================

.. py:class:: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel

   IGraphics3DModel
   
   Interface IAgSaVOModel exposes all Satellite's VO Model properties.

.. py:currentmodule:: ISatelliteGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.orbit_marker`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.ground_marker`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.solar_panels_point_at_sun`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.is_point_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.point_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.gltf_reflection_map_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.gltf_image_based`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISatelliteGraphics3DModel


Property detail
---------------

.. py:property:: orbit_marker
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.orbit_marker
    :type: IGraphics3DMarker

    Define the display of the marker to represent the selected vehicle while traveling along its actual orbit, separate from that of its ground track. The orbit is the actual path that a vehicle follows.

.. py:property:: ground_marker
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.ground_marker
    :type: IGraphics3DMarker

    Define the display of the marker to represent the vehicle's position along its ground track, separate from that of its orbit. The ground track of a vehicle is the portion of the central body's surface that it covers while traveling along its track.

.. py:property:: solar_panels_point_at_sun
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.solar_panels_point_at_sun
    :type: bool

    The model's solar panels are defaulted to point toward the sun.

.. py:property:: is_point_visible
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.is_point_visible
    :type: bool

    Whether the point that is shown at certain viewing distances to represent an object, is visible.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.point_size
    :type: typing.Any

    A size of the point (in pixels). Dimensionless.

.. py:property:: gltf_reflection_map_type
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.gltf_reflection_map_type
    :type: MODEL_GLTF_REFLECTION_MAP_TYPE

    Gets or sets the glTF reflection map type property. A member of the AgEModelGltfReflectionMapType enumeration.

.. py:property:: gltf_image_based
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3DModel.gltf_image_based
    :type: IGraphics3DModelGltfImageBased

    Gets glTF Image Based properties.


