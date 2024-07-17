SceneManager
============

.. py:class:: ansys.stk.core.graphics.SceneManager

   Bases: 

   The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

.. py:currentmodule:: SceneManager

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.render`
              - Render all scenes within an application. To render a specific scene, use the Render method.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.primitives`
              - Gets the primitive manager, which is used to add primitives to your scenes.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.screen_overlays`
              - Gets the screen overlay manager, which is used to add screen overlays to your scenes.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.textures`
              - Gets the texture 2d factory, which can be used to create textures from various sources.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.globe_overlay_settings`
              - Gets the globe overlay settings, which are used to set global settings for all globe overlays.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.scenes`
              - Gets a read-only collection of scenes that are associated with the scene manager.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.initializers`
              - Allows the user to create or initialize primitives, display conditions, tringulators and other types of objects.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.frame_rate`
              - Gets the frame rate class, which can be used to keep track of how fast scenes are being <see ref='Render'>rendered</see>.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SceneManager


Property detail
---------------

.. py:property:: primitives
    :canonical: ansys.stk.core.graphics.SceneManager.primitives
    :type: IPrimitiveManager

    Gets the primitive manager, which is used to add primitives to your scenes.

.. py:property:: screen_overlays
    :canonical: ansys.stk.core.graphics.SceneManager.screen_overlays
    :type: IScreenOverlayManager

    Gets the screen overlay manager, which is used to add screen overlays to your scenes.

.. py:property:: textures
    :canonical: ansys.stk.core.graphics.SceneManager.textures
    :type: ITexture2DFactory

    Gets the texture 2d factory, which can be used to create textures from various sources.

.. py:property:: globe_overlay_settings
    :canonical: ansys.stk.core.graphics.SceneManager.globe_overlay_settings
    :type: IGlobeOverlaySettings

    Gets the globe overlay settings, which are used to set global settings for all globe overlays.

.. py:property:: scenes
    :canonical: ansys.stk.core.graphics.SceneManager.scenes
    :type: ISceneCollection

    Gets a read-only collection of scenes that are associated with the scene manager.

.. py:property:: initializers
    :canonical: ansys.stk.core.graphics.SceneManager.initializers
    :type: IFactoryAndInitializers

    Allows the user to create or initialize primitives, display conditions, tringulators and other types of objects.

.. py:property:: frame_rate
    :canonical: ansys.stk.core.graphics.SceneManager.frame_rate
    :type: IFrameRate

    Gets the frame rate class, which can be used to keep track of how fast scenes are being <see ref='Render'>rendered</see>.


Method detail
-------------






.. py:method:: render(self) -> None
    :canonical: ansys.stk.core.graphics.SceneManager.render

    Render all scenes within an application. To render a specific scene, use the Render method.

    :Returns:

        :obj:`~None`



