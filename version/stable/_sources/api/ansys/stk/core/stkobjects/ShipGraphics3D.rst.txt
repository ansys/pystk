ShipGraphics3D
==============

.. py:class:: ansys.stk.core.stkobjects.ShipGraphics3D

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D`

   3D Graphics attributes for a ship.

.. py:currentmodule:: ShipGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ShipGraphics3D.proximity`
              - Get the ship's 3D proximity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ShipGraphics3D.drop_lines`
              - Return an interface allowing to configure vehicle's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.ShipGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.ShipGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ShipGraphics3D


Property detail
---------------

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.ShipGraphics3D.proximity
    :type: VehicleGraphics3DRouteProximity

    Get the ship's 3D proximity properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.ShipGraphics3D.drop_lines
    :type: VehicleGraphics3DRouteDropLines

    Return an interface allowing to configure vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.ShipGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ShipGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.


