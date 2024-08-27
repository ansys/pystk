CentralBodyGraphics
===================

.. py:class:: ansys.stk.core.graphics.CentralBodyGraphics

   The graphical properties associated with a particular central body. Changing the central body graphics will affect how the associated central body is rendered in a scene. For instance, to show or hide the central body, use the show property...

.. py:currentmodule:: CentralBodyGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.color`
              - Gets or sets the color of the central body in the scene.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.specular_color`
              - Gets or sets the specular color of the central body in the scene. The specular color is associated with the specular overlay.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.shininess`
              - Gets or sets the shininess of the central body in the scene. The shininess affects the size and brightness of specular reflection associated with the specular overlay.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.show_imagery`
              - Gets or sets whether the imagery for central body in the scene is shown or hidden.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.show`
              - Gets or sets whether the central body is shown or hidden in the scene. This only affects the central body itself, not the primitives that are associated with it.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.show_label`
              - Gets or sets whether a label with the name of the central body should be rendered in the scene when the camera is at certain distance away from the central body.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.altitude_offset`
              - Gets or sets the altitude that all terrain and imagery will be offset from the surface of the central body in the scene.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.base_overlay`
              - Gets or sets the base globe image overlay associated with the central body in the scene. The base overlay is always rendered before any other imagery...
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.night_overlay`
              - Gets or sets the night globe image overlay associated with the central body in the scene. The night overlay is displayed only on parts of the central body that are not in sun light...
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.specular_overlay`
              - Gets or sets the specular globe image overlay associated with the central body in the scene. The specular overlay is displayed only in the specular highlight of the central body.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.terrain`
              - Gets the collection of terrain overlay associated with the central body in the scene.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.imagery`
              - Gets the collection of imagery associated with the central body in the scene.
            * - :py:attr:`~ansys.stk.core.graphics.CentralBodyGraphics.kml`
              - Gets the kml graphics associated with the central body in the scene.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CentralBodyGraphics


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.color
    :type: agcolor.Color

    Gets or sets the color of the central body in the scene.

.. py:property:: specular_color
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.specular_color
    :type: agcolor.Color

    Gets or sets the specular color of the central body in the scene. The specular color is associated with the specular overlay.

.. py:property:: shininess
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.shininess
    :type: float

    Gets or sets the shininess of the central body in the scene. The shininess affects the size and brightness of specular reflection associated with the specular overlay.

.. py:property:: show_imagery
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.show_imagery
    :type: bool

    Gets or sets whether the imagery for central body in the scene is shown or hidden.

.. py:property:: show
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.show
    :type: bool

    Gets or sets whether the central body is shown or hidden in the scene. This only affects the central body itself, not the primitives that are associated with it.

.. py:property:: show_label
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.show_label
    :type: bool

    Gets or sets whether a label with the name of the central body should be rendered in the scene when the camera is at certain distance away from the central body.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.altitude_offset
    :type: float

    Gets or sets the altitude that all terrain and imagery will be offset from the surface of the central body in the scene.

.. py:property:: base_overlay
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.base_overlay
    :type: IGlobeImageOverlay

    Gets or sets the base globe image overlay associated with the central body in the scene. The base overlay is always rendered before any other imagery...

.. py:property:: night_overlay
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.night_overlay
    :type: IGlobeImageOverlay

    Gets or sets the night globe image overlay associated with the central body in the scene. The night overlay is displayed only on parts of the central body that are not in sun light...

.. py:property:: specular_overlay
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.specular_overlay
    :type: IGlobeImageOverlay

    Gets or sets the specular globe image overlay associated with the central body in the scene. The specular overlay is displayed only in the specular highlight of the central body.

.. py:property:: terrain
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.terrain
    :type: TerrainOverlayCollection

    Gets the collection of terrain overlay associated with the central body in the scene.

.. py:property:: imagery
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.imagery
    :type: ImageCollection

    Gets the collection of imagery associated with the central body in the scene.

.. py:property:: kml
    :canonical: ansys.stk.core.graphics.CentralBodyGraphics.kml
    :type: KmlGraphics

    Gets the kml graphics associated with the central body in the scene.


