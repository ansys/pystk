IShipGraphics3D
===============

.. py:class:: IShipGraphics3D

   IGreatArcGraphics3D
   
   3D Graphics attributes for a ship.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~proximity`
            * - :py:meth:`~drop_lines`
            * - :py:meth:`~vapor_trail`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IShipGraphics3D


Property detail
---------------

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.proximity
    :type: "IAgVeVORouteProximity"

    Get the ship's 3D proximity properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.drop_lines
    :type: "IAgVeVORouteDropLines"

    Returns an interface allowing to configure vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.vapor_trail
    :type: "IAgVOVaporTrail"

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IShipGraphics3D.radar_cross_section
    :type: "IAgRadarCrossSectionVO"

    Gets the radar cross section graphics interface.


