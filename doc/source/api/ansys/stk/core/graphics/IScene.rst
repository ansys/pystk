IScene
======

.. py:class:: ansys.stk.core.graphics.IScene

   object
   
   A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

.. py:currentmodule:: IScene

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScene.render`
              - Render the scene. To render all the scenes within an application, use the Render method.
            * - :py:attr:`~ansys.stk.core.graphics.IScene.pick`
              - Execute a pick at the given x, y and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.
            * - :py:attr:`~ansys.stk.core.graphics.IScene.pick_rectangular`
              - Execute a pick in the given rectangular region and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.
            * - :py:attr:`~ansys.stk.core.graphics.IScene.pick_screen_overlays`
              - Execute a pick on screen overlays at the given x, y and returns a front to back sorted collection of picked overlays. The coordinate origin is top, left. To pick other objects in the scene, use the Pick method.
            * - :py:attr:`~Subscribe`
              - """Return an ISceneEventHandler that is subscribed to handle events associated with this instance of IScene."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScene.camera`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.lighting`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.show_sunshine`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.central_bodies`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.background_color`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.shade_sky_based_on_altitude`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.show_stars`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.globe_overlay_settings`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.scene_id`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.show_water_surface`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.anti_aliasing`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.visual_effects`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.clouds`
            * - :py:attr:`~ansys.stk.core.graphics.IScene.show_star_labels`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IScene


Property detail
---------------

.. py:property:: camera
    :canonical: ansys.stk.core.graphics.IScene.camera
    :type: ICamera

    Gets the camera associated with the scene, which affects the view that is rendered by the scene.

.. py:property:: lighting
    :canonical: ansys.stk.core.graphics.IScene.lighting
    :type: ILighting

    Gets the lighting associated with the scene.

.. py:property:: show_sunshine
    :canonical: ansys.stk.core.graphics.IScene.show_sunshine
    :type: bool

    Gets or sets whether sunshine is rendered by the Sun central body. Sunshine renders a halo effect around the sun when it is viewed in the scene.

.. py:property:: central_bodies
    :canonical: ansys.stk.core.graphics.IScene.central_bodies
    :type: ICentralBodyGraphicsIndexer

    Gets the central body graphics for a specified central body.

.. py:property:: background_color
    :canonical: ansys.stk.core.graphics.IScene.background_color
    :type: agcolor.Color

    Gets or sets the background color of the scene.

.. py:property:: shade_sky_based_on_altitude
    :canonical: ansys.stk.core.graphics.IScene.shade_sky_based_on_altitude
    :type: bool

    Gets or sets whether the sky will be shaded based on camera altitude. When shade sky based on altitude is set to true, the sky will become more blue as the Camera gets closer to the surface of the central body.

.. py:property:: show_stars
    :canonical: ansys.stk.core.graphics.IScene.show_stars
    :type: bool

    Gets or sets whether stars are shown or hidden in the scene.

.. py:property:: globe_overlay_settings
    :canonical: ansys.stk.core.graphics.IScene.globe_overlay_settings
    :type: ISceneGlobeOverlaySettings

    Gets the scene globe overlay settings for the scene.

.. py:property:: scene_id
    :canonical: ansys.stk.core.graphics.IScene.scene_id
    :type: int

    Returns the scene identifier.

.. py:property:: show_water_surface
    :canonical: ansys.stk.core.graphics.IScene.show_water_surface
    :type: bool

    Gets or sets whether water surface on earth is shown or hidden in the scene.

.. py:property:: anti_aliasing
    :canonical: ansys.stk.core.graphics.IScene.anti_aliasing
    :type: ANTI_ALIASING

    Gets or sets the multisample anti-aliasing (MSAA) option for this scene. As the level of anti-aliasing increases, performance will generally decrease, but the quality of the anti-aliasing will improve.

.. py:property:: visual_effects
    :canonical: ansys.stk.core.graphics.IScene.visual_effects
    :type: IVisualEffects

    Gets the visual  effects associated with the scene.

.. py:property:: clouds
    :canonical: ansys.stk.core.graphics.IScene.clouds
    :type: IClouds

    Gets the clouds for the scene.

.. py:property:: show_star_labels
    :canonical: ansys.stk.core.graphics.IScene.show_star_labels
    :type: bool

    Gets or sets whether stars labels are shown or hidden in the scene.


Method detail
-------------













.. py:method:: render(self) -> None
    :canonical: ansys.stk.core.graphics.IScene.render

    Render the scene. To render all the scenes within an application, use the Render method.

    :Returns:

        :obj:`~None`

.. py:method:: pick(self, x: int, y: int) -> IPickResultCollection
    :canonical: ansys.stk.core.graphics.IScene.pick

    Execute a pick at the given x, y and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.

    :Parameters:

    **x** : :obj:`~int`
    **y** : :obj:`~int`

    :Returns:

        :obj:`~IPickResultCollection`

.. py:method:: pick_rectangular(self, left: int, bottom: int, right: int, top: int) -> IPickResultCollection
    :canonical: ansys.stk.core.graphics.IScene.pick_rectangular

    Execute a pick in the given rectangular region and returns a depth sorted collection of picked objects. The coordinate origin is top, left. To pick screen overlays, use the PickScreenOverlays method.

    :Parameters:

    **left** : :obj:`~int`
    **bottom** : :obj:`~int`
    **right** : :obj:`~int`
    **top** : :obj:`~int`

    :Returns:

        :obj:`~IPickResultCollection`

.. py:method:: pick_screen_overlays(self, x: int, y: int) -> IScreenOverlayPickResultCollection
    :canonical: ansys.stk.core.graphics.IScene.pick_screen_overlays

    Execute a pick on screen overlays at the given x, y and returns a front to back sorted collection of picked overlays. The coordinate origin is top, left. To pick other objects in the scene, use the Pick method.

    :Parameters:

    **x** : :obj:`~int`
    **y** : :obj:`~int`

    :Returns:

        :obj:`~IScreenOverlayPickResultCollection`










