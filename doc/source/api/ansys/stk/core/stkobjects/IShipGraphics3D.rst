IShipGraphics3D
===============

.. py:class:: ansys.stk.core.stkobjects.IShipGraphics3D

   IGreatArcGraphics3D
   
   3D Graphics attributes for a ship.

.. py:currentmodule:: IShipGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IShipGraphics3D.proximity`
              - Get the ship's 3D proximity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IShipGraphics3D.drop_lines`
              - Returns an interface allowing to configure vehicle's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IShipGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.IShipGraphics3D.radar_cross_section`
              - Gets the radar cross section graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IShipGraphics3D


Property detail
---------------

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.proximity
    :type: IVehicleGraphics3DRouteProximity

    Get the ship's 3D proximity properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.drop_lines
    :type: IVehicleGraphics3DRouteDropLines

    Returns an interface allowing to configure vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.vapor_trail
    :type: IGraphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.radar_cross_section
    :type: IRadarCrossSectionGraphics3D

    Gets the radar cross section graphics interface.


