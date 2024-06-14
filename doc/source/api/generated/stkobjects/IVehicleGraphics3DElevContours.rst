IVehicleGraphics3DElevContours
==============================

.. py:class:: IVehicleGraphics3DElevContours

   object
   
   Interface for 3D elevation angle contours.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~is_cones_visible`
            * - :py:meth:`~translucency`
            * - :py:meth:`~fill`
            * - :py:meth:`~fill_translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DElevContours


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DElevContours.is_visible
    :type: bool

    Opt whether to display elevation angle contours.

.. py:property:: is_cones_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DElevContours.is_cones_visible
    :type: bool

    Opt whether to display elevation angle contours as filled cones in space.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DElevContours.translucency
    :type: float

    Translucency of elevation contour cone. Dimensionless.

.. py:property:: fill
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DElevContours.fill
    :type: bool

    Opt whether to display elevation angle contours as a filled polygon on the surface of the central body.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DElevContours.fill_translucency
    :type: float

    Translucency of the filled polygon. Dimensionless.


