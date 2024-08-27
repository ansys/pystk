VehicleGraphics2DLighting
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DLighting

   Lighting.

.. py:currentmodule:: VehicleGraphics2DLighting

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting.sunlight`
              - Get the display options for regions of sunlight.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting.penumbra`
              - Get the display options for regions of penumbra.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting.umbra`
              - Get the display options for regions of umbra.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting.is_sun_light_penumbra_visible`
              - Opt whether to show the dividing line between regions of sunlight and penumbra at the current altitude of the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting.is_penumbra_umbra_visible`
              - Opt whether to show the dividing line between regions of penumbra and umbra at the current altitude of the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting.is_solar_specular_reflection_point_visible`
              - Opt whether to draw the solar specular reflection point on the surface of the globe as a white '*'.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DLighting


Property detail
---------------

.. py:property:: sunlight
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLighting.sunlight
    :type: VehicleGraphics2DLightingElement

    Get the display options for regions of sunlight.

.. py:property:: penumbra
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLighting.penumbra
    :type: VehicleGraphics2DLightingElement

    Get the display options for regions of penumbra.

.. py:property:: umbra
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLighting.umbra
    :type: VehicleGraphics2DLightingElement

    Get the display options for regions of umbra.

.. py:property:: is_sun_light_penumbra_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLighting.is_sun_light_penumbra_visible
    :type: bool

    Opt whether to show the dividing line between regions of sunlight and penumbra at the current altitude of the vehicle.

.. py:property:: is_penumbra_umbra_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLighting.is_penumbra_umbra_visible
    :type: bool

    Opt whether to show the dividing line between regions of penumbra and umbra at the current altitude of the vehicle.

.. py:property:: is_solar_specular_reflection_point_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLighting.is_solar_specular_reflection_point_visible
    :type: bool

    Opt whether to draw the solar specular reflection point on the surface of the globe as a white '*'.


