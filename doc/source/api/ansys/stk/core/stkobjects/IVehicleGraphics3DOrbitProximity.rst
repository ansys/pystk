IVehicleGraphics3DOrbitProximity
================================

.. py:class:: IVehicleGraphics3DOrbitProximity

   IVehicleGraphics3DProximity
   
   Proximity graphics interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~geo_box`
            * - :py:meth:`~control_box`
            * - :py:meth:`~bearing_box`
            * - :py:meth:`~bearing_ellipse`
            * - :py:meth:`~line_of_bearing`
            * - :py:meth:`~aou_label_swap_distance`
            * - :py:meth:`~ellipsoid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DOrbitProximity


Property detail
---------------

.. py:property:: geo_box
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitProximity.geo_box
    :type: "IAgVeVOGeoBox"

    Get the parameters for a geostationary box, a planar rectangle centered at a fixed longitude in space and used to visually check that a GEO satellite stays within a certain area.

.. py:property:: control_box
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitProximity.control_box
    :type: "IAgVeVOControlBox"

    Get the parameters for a control box, defining a volume around the object that moves with the object.

.. py:property:: bearing_box
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitProximity.bearing_box
    :type: "IAgVeVOBearingBox"

    Get the parameters for a bearing box, defining a volume, relative to a bearing from the North, around an object.

.. py:property:: bearing_ellipse
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitProximity.bearing_ellipse
    :type: "IAgVeVOBearingEllipse"

    Get the parameters for a bearing ellipse, defining an ellipse, relative to a bearing from the North, around the object.

.. py:property:: line_of_bearing
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitProximity.line_of_bearing
    :type: "IAgVeVOLineOfBearing"

    Get the parameters for a line of bearing parameters drawn from an origin in the direction of a bearing.

.. py:property:: aou_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitProximity.aou_label_swap_distance
    :type: "IAgVOLabelSwapDistance"

    Area of uncertainty label swap distance.

.. py:property:: ellipsoid
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitProximity.ellipsoid
    :type: "IAgVeVOEllipsoid"

    Defines the ellipsoid parameters.


