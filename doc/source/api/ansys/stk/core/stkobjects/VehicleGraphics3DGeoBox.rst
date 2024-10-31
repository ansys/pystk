VehicleGraphics3DGeoBox
=======================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox

   Geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

.. py:currentmodule:: VehicleGraphics3DGeoBox

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.reposition`
              - Reposition the geostationary box.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.show_graphics`
              - Opt whether to show the plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.longitude`
              - Center longitude of the plane at the initial condition of the satellite at epoch. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.north_south`
              - Angular length of the plane from North to South. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.east_west`
              - Angular length of the plane from East to West. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.radius`
              - Gets or sets the radius from the center of the Earth to the center of the plane. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.color`
              - Color of the lines defining the plane.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DGeoBox


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.show_graphics
    :type: bool

    Opt whether to show the plane.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.longitude
    :type: float

    Center longitude of the plane at the initial condition of the satellite at epoch. Uses Longitude Dimension.

.. py:property:: north_south
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.north_south
    :type: float

    Angular length of the plane from North to South. Uses Angle Dimension.

.. py:property:: east_west
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.east_west
    :type: float

    Angular length of the plane from East to West. Uses Angle Dimension.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.radius
    :type: float

    Gets or sets the radius from the center of the Earth to the center of the plane. Uses Distance Dimension.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.color
    :type: agcolor.Color

    Color of the lines defining the plane.


Method detail
-------------













.. py:method:: reposition(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox.reposition

    Reposition the geostationary box.

    :Returns:

        :obj:`~None`

