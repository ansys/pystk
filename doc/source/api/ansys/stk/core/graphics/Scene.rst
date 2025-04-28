Scene
=====

.. py:class:: ansys.stk.core.graphics.Scene

   A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

.. py:currentmodule:: Scene

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Scene.render`
              - Render the scene. To render all the scenes within an application, use the Render method.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.pick`
              - Execute a pick at the given x, y and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.pick_rectangular`
              - Execute a pick in the given rectangular region and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.pick_screen_overlays`
              - Execute a pick on screen overlays at the given x, y and returns a front to back sorted collection of picked overlays. The coordinate origin is top, left. To pick other objects in the scene, use the Pick method.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.subscribe`
              - """Return an ISceneEventHandler that is subscribed to handle events associated with this instance of Scene."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Scene.camera`
              - Get the camera associated with the scene, which affects the view that is rendered by the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.lighting`
              - Get the lighting associated with the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.show_sunshine`
              - Get or set whether sunshine is rendered by the Sun central body. Sunshine renders a halo effect around the sun when it is viewed in the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.central_bodies`
              - Get the central body graphics for a specified central body.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.background_color`
              - Get or set the background color of the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.shade_sky_based_on_altitude`
              - Get or set whether the sky will be shaded based on camera altitude. When shade sky based on altitude is set to true, the sky will become more blue as the Camera gets closer to the surface of the central body.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.show_stars`
              - Get or set whether stars are shown or hidden in the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.globe_overlay_settings`
              - Get the scene globe overlay settings for the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.scene_id`
              - Return the scene identifier.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.show_water_surface`
              - Get or set whether water surface on earth is shown or hidden in the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.anti_aliasing`
              - Get or set the multisample anti-aliasing (MSAA) option for this scene. As the level of anti-aliasing increases, performance will generally decrease, but the quality of the anti-aliasing will improve.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.visual_effects`
              - Get the visual  effects associated with the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.clouds`
              - Get the clouds for the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Scene.show_star_labels`
              - Get or set whether stars labels are shown or hidden in the scene.



Examples
--------

Control the Display of Stars and Water Texture

.. code-block:: python

    # Scenario scenario: Scenario object
    # Turn off the stars and water texture
    manager = scenario.scene_manager
    manager.scenes.item(0).show_stars = False
    manager.scenes.item(0).show_water_surface = False


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import Scene


Property detail
---------------

.. py:property:: camera
    :canonical: ansys.stk.core.graphics.Scene.camera
    :type: Camera

    Get the camera associated with the scene, which affects the view that is rendered by the scene.

.. py:property:: lighting
    :canonical: ansys.stk.core.graphics.Scene.lighting
    :type: Lighting

    Get the lighting associated with the scene.

.. py:property:: show_sunshine
    :canonical: ansys.stk.core.graphics.Scene.show_sunshine
    :type: bool

    Get or set whether sunshine is rendered by the Sun central body. Sunshine renders a halo effect around the sun when it is viewed in the scene.

.. py:property:: central_bodies
    :canonical: ansys.stk.core.graphics.Scene.central_bodies
    :type: CentralBodyGraphicsIndexer

    Get the central body graphics for a specified central body.

.. py:property:: background_color
    :canonical: ansys.stk.core.graphics.Scene.background_color
    :type: agcolor.Color

    Get or set the background color of the scene.

.. py:property:: shade_sky_based_on_altitude
    :canonical: ansys.stk.core.graphics.Scene.shade_sky_based_on_altitude
    :type: bool

    Get or set whether the sky will be shaded based on camera altitude. When shade sky based on altitude is set to true, the sky will become more blue as the Camera gets closer to the surface of the central body.

.. py:property:: show_stars
    :canonical: ansys.stk.core.graphics.Scene.show_stars
    :type: bool

    Get or set whether stars are shown or hidden in the scene.

.. py:property:: globe_overlay_settings
    :canonical: ansys.stk.core.graphics.Scene.globe_overlay_settings
    :type: SceneGlobeOverlaySettings

    Get the scene globe overlay settings for the scene.

.. py:property:: scene_id
    :canonical: ansys.stk.core.graphics.Scene.scene_id
    :type: int

    Return the scene identifier.

.. py:property:: show_water_surface
    :canonical: ansys.stk.core.graphics.Scene.show_water_surface
    :type: bool

    Get or set whether water surface on earth is shown or hidden in the scene.

.. py:property:: anti_aliasing
    :canonical: ansys.stk.core.graphics.Scene.anti_aliasing
    :type: AntiAliasingMethod

    Get or set the multisample anti-aliasing (MSAA) option for this scene. As the level of anti-aliasing increases, performance will generally decrease, but the quality of the anti-aliasing will improve.

.. py:property:: visual_effects
    :canonical: ansys.stk.core.graphics.Scene.visual_effects
    :type: VisualEffects

    Get the visual  effects associated with the scene.

.. py:property:: clouds
    :canonical: ansys.stk.core.graphics.Scene.clouds
    :type: Clouds

    Get the clouds for the scene.

.. py:property:: show_star_labels
    :canonical: ansys.stk.core.graphics.Scene.show_star_labels
    :type: bool

    Get or set whether stars labels are shown or hidden in the scene.


Method detail
-------------













.. py:method:: render(self) -> None
    :canonical: ansys.stk.core.graphics.Scene.render

    Render the scene. To render all the scenes within an application, use the Render method.

    :Returns:

        :obj:`~None`

.. py:method:: pick(self, x: int, y: int) -> PickResultCollection
    :canonical: ansys.stk.core.graphics.Scene.pick

    Execute a pick at the given x, y and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.

    :Parameters:

    **x** : :obj:`~int`
    **y** : :obj:`~int`

    :Returns:

        :obj:`~PickResultCollection`

.. py:method:: pick_rectangular(self, left: int, bottom: int, right: int, top: int) -> PickResultCollection
    :canonical: ansys.stk.core.graphics.Scene.pick_rectangular

    Execute a pick in the given rectangular region and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.

    :Parameters:

    **left** : :obj:`~int`
    **bottom** : :obj:`~int`
    **right** : :obj:`~int`
    **top** : :obj:`~int`

    :Returns:

        :obj:`~PickResultCollection`

.. py:method:: pick_screen_overlays(self, x: int, y: int) -> ScreenOverlayPickResultCollection
    :canonical: ansys.stk.core.graphics.Scene.pick_screen_overlays

    Execute a pick on screen overlays at the given x, y and returns a front to back sorted collection of picked overlays. The coordinate origin is top, left. To pick other objects in the scene, use the Pick method.

    :Parameters:

    **x** : :obj:`~int`
    **y** : :obj:`~int`

    :Returns:

        :obj:`~ScreenOverlayPickResultCollection`










