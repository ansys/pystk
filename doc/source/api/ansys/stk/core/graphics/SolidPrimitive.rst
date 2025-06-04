SolidPrimitive
==============

.. py:class:: ansys.stk.core.graphics.SolidPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

.. py:currentmodule:: SolidPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.set_with_result`
              - Define the solid using the specified solidTriangulatorResult. The solid is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.set`
              - Define the solid using the specified parameters. The solid is rendered in the primitive's reference frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.affected_by_lighting`
              - Get or set whether the primitive is affected by lighting.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.display_fill`
              - Get or set whether the solid's fill is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.display_silhouette`
              - Get or set whether the solid's silhouette is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.silhouette_color`
              - Get or set the silhouette's color.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.silhouette_translucency`
              - Get or set the silhouette's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.silhouette_width`
              - Get or set the silhouette' width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.minimum_silhouette_width_supported`
              - Get the minimum silhouette width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.maximum_silhouette_width_supported`
              - Get the maximum silhouette width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.display_outline`
              - Get or set whether the solid's outline is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_color`
              - Get or set the outline's color.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_translucency`
              - Get or set the outline's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_width`
              - Get or set the outline's width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_appearance`
              - Get or set the outline's appearance.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.back_line_color`
              - Get or set the back line's color.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.back_line_translucency`
              - Get or set the back line's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.position`
              - Get or set the solid's position. The position is defined in the solid's reference frame. The array contains the components of the position in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.rotation`
              - Get or set the rotation applied to the solid before rendering.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.scale`
              - Get or set a non-uniform scale that is applied to the solid to increase or decrease its rendered size. The array contains the scale for each component of the size in the order x scale, y scale, z scale.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.back_line_width`
              - Get or set the back line's width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.set_hint`
              - Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.



Examples
--------

Draw a Solid Cylinder Primitive and set properties

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    originCylinder = root.conversion_utility.new_position_on_earth()
    originCylinder.assign_geodetic(0, 7, 100)

    orientCylinder = root.conversion_utility.new_orientation()
    orientCylinder.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

    cylinder = manager.initializers.cylinder_triangulator.create_simple(200, 100)
    solidCylinder = manager.initializers.solid_primitive.initialize()
    solidCylinder.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item("Fixed")
    solidCylinder.position = originCylinder.query_cartesian_array()
    solidCylinder.set_with_result(cylinder)
    solidCylinder.color = Colors.Lime
    solidCylinder.outline_color = Colors.Blue
    solidCylinder.outline_width = 3
    solidCylinder.translucency = 0.75
    solidCylinder.rotation = orientCylinder
    manager.primitives.add(solidCylinder)
    manager.render()


Draw a Solid Ellipsoid Primitive and set properties

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    originEllipsoid = root.conversion_utility.new_position_on_earth()
    originEllipsoid.assign_geodetic(0, 5, 100)

    orientEllipsoid = root.conversion_utility.new_orientation()
    orientEllipsoid.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

    radii = [[200], [100], [100]]
    ellipsoid = manager.initializers.ellipsoid_triangulator.compute_simple(radii)
    solidEllipsoid = manager.initializers.solid_primitive.initialize()
    solidEllipsoid.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item(
        "Fixed"
    )  # vgtSat.Systems.item('Body')
    solidEllipsoid.position = originEllipsoid.query_cartesian_array()
    solidEllipsoid.set_with_result(ellipsoid)
    solidEllipsoid.color = Colors.White
    solidEllipsoid.outline_color = Colors.DeepPink
    solidEllipsoid.translucency = 0.75
    solidEllipsoid.rotation = orientEllipsoid
    manager.primitives.add(solidEllipsoid)
    manager.render()


Draw a Solid Box Primitive and set properties

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    originBox = root.conversion_utility.new_position_on_earth()
    originBox.assign_geodetic(0, 3, 100)

    orientBox = root.conversion_utility.new_orientation()
    orientBox.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

    size = [[100], [100], [200]]
    result = manager.initializers.box_triangulator.compute(size)
    solidBox = manager.initializers.solid_primitive.initialize()
    solidBox.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item("Fixed")
    solidBox.position = originBox.query_cartesian_array()
    solidBox.set_with_result(result)
    solidBox.color = Colors.Red
    solidBox.outline_color = Colors.Cyan
    solidBox.translucency = 0.75
    solidBox.rotation = orientBox
    manager.primitives.add(solidBox)
    manager.render()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SolidPrimitive


Property detail
---------------

.. py:property:: affected_by_lighting
    :canonical: ansys.stk.core.graphics.SolidPrimitive.affected_by_lighting
    :type: bool

    Get or set whether the primitive is affected by lighting.

.. py:property:: display_fill
    :canonical: ansys.stk.core.graphics.SolidPrimitive.display_fill
    :type: bool

    Get or set whether the solid's fill is displayed.

.. py:property:: display_silhouette
    :canonical: ansys.stk.core.graphics.SolidPrimitive.display_silhouette
    :type: bool

    Get or set whether the solid's silhouette is displayed.

.. py:property:: silhouette_color
    :canonical: ansys.stk.core.graphics.SolidPrimitive.silhouette_color
    :type: agcolor.Color

    Get or set the silhouette's color.

.. py:property:: silhouette_translucency
    :canonical: ansys.stk.core.graphics.SolidPrimitive.silhouette_translucency
    :type: float

    Get or set the silhouette's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: silhouette_width
    :canonical: ansys.stk.core.graphics.SolidPrimitive.silhouette_width
    :type: float

    Get or set the silhouette' width, in pixels.

.. py:property:: minimum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.SolidPrimitive.minimum_silhouette_width_supported
    :type: float

    Get the minimum silhouette width, in pixels, supported by the video card.

.. py:property:: maximum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.SolidPrimitive.maximum_silhouette_width_supported
    :type: float

    Get the maximum silhouette width, in pixels, supported by the video card.

.. py:property:: display_outline
    :canonical: ansys.stk.core.graphics.SolidPrimitive.display_outline
    :type: bool

    Get or set whether the solid's outline is displayed.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_color
    :type: agcolor.Color

    Get or set the outline's color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_translucency
    :type: float

    Get or set the outline's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: outline_width
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_width
    :type: float

    Get or set the outline's width, in pixels.

.. py:property:: outline_appearance
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_appearance
    :type: OutlineAppearance

    Get or set the outline's appearance.

.. py:property:: back_line_color
    :canonical: ansys.stk.core.graphics.SolidPrimitive.back_line_color
    :type: agcolor.Color

    Get or set the back line's color.

.. py:property:: back_line_translucency
    :canonical: ansys.stk.core.graphics.SolidPrimitive.back_line_translucency
    :type: float

    Get or set the back line's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.SolidPrimitive.position
    :type: list

    Get or set the solid's position. The position is defined in the solid's reference frame. The array contains the components of the position in the order x, y, z.

.. py:property:: rotation
    :canonical: ansys.stk.core.graphics.SolidPrimitive.rotation
    :type: IOrientation

    Get or set the rotation applied to the solid before rendering.

.. py:property:: scale
    :canonical: ansys.stk.core.graphics.SolidPrimitive.scale
    :type: list

    Get or set a non-uniform scale that is applied to the solid to increase or decrease its rendered size. The array contains the scale for each component of the size in the order x scale, y scale, z scale.

.. py:property:: back_line_width
    :canonical: ansys.stk.core.graphics.SolidPrimitive.back_line_width
    :type: float

    Get or set the back line's width, in pixels.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.SolidPrimitive.set_hint
    :type: SetHint

    Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.


Method detail
-------------






































.. py:method:: set_with_result(self, solid_triangulator_result: SolidTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.SolidPrimitive.set_with_result

    Define the solid using the specified solidTriangulatorResult. The solid is rendered in the primitive's reference frame.

    :Parameters:

        **solid_triangulator_result** : :obj:`~SolidTriangulatorResult`


    :Returns:

        :obj:`~None`

.. py:method:: set(self, positions: list, normals: list, indices: list, outline_indices: list, winding_order: WindingOrder, bounding_sphere: BoundingSphere, closed: bool) -> None
    :canonical: ansys.stk.core.graphics.SolidPrimitive.set

    Define the solid using the specified parameters. The solid is rendered in the primitive's reference frame.

    :Parameters:

        **positions** : :obj:`~list`

        **normals** : :obj:`~list`

        **indices** : :obj:`~list`

        **outline_indices** : :obj:`~list`

        **winding_order** : :obj:`~WindingOrder`

        **bounding_sphere** : :obj:`~BoundingSphere`

        **closed** : :obj:`~bool`


    :Returns:

        :obj:`~None`

