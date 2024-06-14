IVehicleGraphics3DGeoBox
========================

.. py:class:: IVehicleGraphics3DGeoBox

   object
   
   Interface for geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reposition`
              - Reposition the geostationary box.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~longitude`
            * - :py:meth:`~north_south`
            * - :py:meth:`~east_west`
            * - :py:meth:`~radius`
            * - :py:meth:`~color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DGeoBox


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DGeoBox.is_visible
    :type: bool

    Opt whether to show the plane.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DGeoBox.longitude
    :type: float

    Center longitude of the plane at the initial condition of the satellite at epoch. Uses Longitude Dimension.

.. py:property:: north_south
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DGeoBox.north_south
    :type: float

    Angular length of the plane from North to South. Uses Angle Dimension.

.. py:property:: east_west
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DGeoBox.east_west
    :type: float

    Angular length of the plane from East to West. Uses Angle Dimension.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DGeoBox.radius
    :type: float

    Gets or sets the radius from the center of the Earth to the center of the plane. Uses Distance Dimension.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DGeoBox.color
    :type: agcolor.Color

    Color of the lines defining the plane.


Method detail
-------------













.. py:method:: reposition(self) -> None

    Reposition the geostationary box.

    :Returns:

        :obj:`~None`

