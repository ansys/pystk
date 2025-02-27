Lighting
========

.. py:class:: ansys.stk.core.graphics.Lighting

   Lighting in the 3D scene.

.. py:currentmodule:: Lighting

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Lighting.enabled`
              - Get or set whether or not lighting is enabled.
            * - :py:attr:`~ansys.stk.core.graphics.Lighting.ambient_intensity`
              - Get or set the ambient intensity throughout the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Lighting.diffuse_intensity`
              - Get or set the diffuse intensity from the sun.
            * - :py:attr:`~ansys.stk.core.graphics.Lighting.night_lights_intensity`
              - Get or set the overall brightness for the night light's image overlay, night overlay.



Examples
--------

Control the Lighting of the 3D scene

.. code-block:: python

    # Scenario scenario: Scenario object
    # Modify the lighting levels
    manager = scenario.scene_manager
    lighting = manager.scenes.item(0).lighting
    lighting.ambient_intensity = 0.20  # Percent
    lighting.diffuse_intensity = 4  # Percent
    lighting.night_lights_intensity = 5  # Percent


Set Vehicle Lighting Properties

.. code-block:: python

    # Satellitesatellite: Satellite object
    lighting = satellite.graphics.lighting
    # Settings for vehicle in sunlight
    sunlight = lighting.sunlight
    sunlight.visible = True
    sunlight.color = Colors.Yellow
    sunlight.line_width = LineWidth.WIDTH4
    # Settings for vehicle in penumbra
    penumbra = lighting.penumbra
    penumbra.visible = True
    penumbra.color = Colors.Orange
    penumbra.line_width = LineWidth.WIDTH3
    # Settings for vehicle in umbra
    umbra = lighting.umbra
    umbra.visible = True
    umbra.color = Colors.Red
    umbra.line_width = LineWidth.WIDTH2


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import Lighting


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.graphics.Lighting.enabled
    :type: bool

    Get or set whether or not lighting is enabled.

.. py:property:: ambient_intensity
    :canonical: ansys.stk.core.graphics.Lighting.ambient_intensity
    :type: float

    Get or set the ambient intensity throughout the scene.

.. py:property:: diffuse_intensity
    :canonical: ansys.stk.core.graphics.Lighting.diffuse_intensity
    :type: float

    Get or set the diffuse intensity from the sun.

.. py:property:: night_lights_intensity
    :canonical: ansys.stk.core.graphics.Lighting.night_lights_intensity
    :type: float

    Get or set the overall brightness for the night light's image overlay, night overlay.


