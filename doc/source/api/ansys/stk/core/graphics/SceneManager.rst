SceneManager
============

.. py:class:: ansys.stk.core.graphics.SceneManager

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

            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.frame_rate`
              - Get the frame rate class, which can be used to keep track of how fast scenes are being <see ref='Render'>rendered</see>.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.globe_overlay_settings`
              - Get the globe overlay settings, which are used to set global settings for all globe overlays.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.initializers`
              - Allow the user to create or initialize primitives, display conditions, tringulators and other types of objects.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.primitives`
              - Get the primitive manager, which is used to add primitives to your scenes.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.scenes`
              - Get a read-only collection of scenes that are associated with the scene manager.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.screen_overlays`
              - Get the screen overlay manager, which is used to add screen overlays to your scenes.
            * - :py:attr:`~ansys.stk.core.graphics.SceneManager.textures`
              - Get the texture 2d factory, which can be used to create textures from various sources.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SceneManager


Property detail
---------------

.. py:property:: frame_rate
    :canonical: ansys.stk.core.graphics.SceneManager.frame_rate
    :type: FrameRate

    Get the frame rate class, which can be used to keep track of how fast scenes are being <see ref='Render'>rendered</see>.

.. py:property:: globe_overlay_settings
    :canonical: ansys.stk.core.graphics.SceneManager.globe_overlay_settings
    :type: GlobeOverlaySettings

    Get the globe overlay settings, which are used to set global settings for all globe overlays.

.. py:property:: initializers
    :canonical: ansys.stk.core.graphics.SceneManager.initializers
    :type: FactoryAndInitializers

    Allow the user to create or initialize primitives, display conditions, tringulators and other types of objects.

.. py:property:: primitives
    :canonical: ansys.stk.core.graphics.SceneManager.primitives
    :type: PrimitiveManager

    Get the primitive manager, which is used to add primitives to your scenes.

.. py:property:: scenes
    :canonical: ansys.stk.core.graphics.SceneManager.scenes
    :type: SceneCollection

    Get a read-only collection of scenes that are associated with the scene manager.

.. py:property:: screen_overlays
    :canonical: ansys.stk.core.graphics.SceneManager.screen_overlays
    :type: ScreenOverlayManager

    Get the screen overlay manager, which is used to add screen overlays to your scenes.

.. py:property:: textures
    :canonical: ansys.stk.core.graphics.SceneManager.textures
    :type: Texture2DFactory

    Get the texture 2d factory, which can be used to create textures from various sources.


Method detail
-------------





.. py:method:: render(self) -> None
    :canonical: ansys.stk.core.graphics.SceneManager.render

    Render all scenes within an application. To render a specific scene, use the Render method.

    :Returns:

        :obj:`~None`




