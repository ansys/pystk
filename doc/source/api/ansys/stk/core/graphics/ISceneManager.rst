ISceneManager
=============

.. py:class:: ISceneManager

   object
   
   The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~render`
              - Render all scenes within an application. To render a specific scene, use the Render method.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~primitives`
            * - :py:meth:`~screen_overlays`
            * - :py:meth:`~textures`
            * - :py:meth:`~globe_overlay_settings`
            * - :py:meth:`~scenes`
            * - :py:meth:`~initializers`
            * - :py:meth:`~frame_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISceneManager


Property detail
---------------

.. py:property:: primitives
    :canonical: ansys.stk.core.graphics.ISceneManager.primitives
    :type: IAgStkGraphicsPrimitiveManager

    Gets the primitive manager, which is used to add primitives to your scenes.

.. py:property:: screen_overlays
    :canonical: ansys.stk.core.graphics.ISceneManager.screen_overlays
    :type: IAgStkGraphicsScreenOverlayManager

    Gets the screen overlay manager, which is used to add screen overlays to your scenes.

.. py:property:: textures
    :canonical: ansys.stk.core.graphics.ISceneManager.textures
    :type: IAgStkGraphicsTexture2DFactory

    Gets the texture 2d factory, which can be used to create textures from various sources.

.. py:property:: globe_overlay_settings
    :canonical: ansys.stk.core.graphics.ISceneManager.globe_overlay_settings
    :type: IAgStkGraphicsGlobeOverlaySettings

    Gets the globe overlay settings, which are used to set global settings for all globe overlays.

.. py:property:: scenes
    :canonical: ansys.stk.core.graphics.ISceneManager.scenes
    :type: IAgStkGraphicsSceneCollection

    Gets a read-only collection of scenes that are associated with the scene manager.

.. py:property:: initializers
    :canonical: ansys.stk.core.graphics.ISceneManager.initializers
    :type: IAgStkGraphicsFactoryAndInitializers

    Allows the user to create or initialize primitives, display conditions, tringulators and other types of objects.

.. py:property:: frame_rate
    :canonical: ansys.stk.core.graphics.ISceneManager.frame_rate
    :type: IAgStkGraphicsFrameRate

    Gets the frame rate class, which can be used to keep track of how fast scenes are being <see ref='Render'>rendered</see>.


Method detail
-------------






.. py:method:: render(self) -> None
    :canonical: ansys.stk.core.graphics.ISceneManager.render

    Render all scenes within an application. To render a specific scene, use the Render method.

    :Returns:

        :obj:`~None`



