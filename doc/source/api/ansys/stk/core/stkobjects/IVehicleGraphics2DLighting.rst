IVehicleGraphics2DLighting
==========================

.. py:class:: IVehicleGraphics2DLighting

   object
   
   Lighting.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~sunlight`
            * - :py:meth:`~penumbra`
            * - :py:meth:`~umbra`
            * - :py:meth:`~is_sun_light_penumbra_visible`
            * - :py:meth:`~is_penumbra_umbra_visible`
            * - :py:meth:`~is_solar_specular_reflection_point_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DLighting


Property detail
---------------

.. py:property:: sunlight
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLighting.sunlight
    :type: "IAgVeGfxLightingElement"

    Get the display options for regions of sunlight.

.. py:property:: penumbra
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLighting.penumbra
    :type: "IAgVeGfxLightingElement"

    Get the display options for regions of penumbra.

.. py:property:: umbra
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLighting.umbra
    :type: "IAgVeGfxLightingElement"

    Get the display options for regions of umbra.

.. py:property:: is_sun_light_penumbra_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLighting.is_sun_light_penumbra_visible
    :type: bool

    Opt whether to show the dividing line between regions of sunlight and penumbra at the current altitude of the vehicle.

.. py:property:: is_penumbra_umbra_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLighting.is_penumbra_umbra_visible
    :type: bool

    Opt whether to show the dividing line between regions of penumbra and umbra at the current altitude of the vehicle.

.. py:property:: is_solar_specular_reflection_point_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLighting.is_solar_specular_reflection_point_visible
    :type: bool

    Opt whether to draw the solar specular reflection point on the surface of the globe as a white '*'.


