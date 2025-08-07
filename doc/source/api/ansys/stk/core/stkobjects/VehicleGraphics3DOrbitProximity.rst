VehicleGraphics3DOrbitProximity
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximity`

   Proximity graphics.

.. py:currentmodule:: VehicleGraphics3DOrbitProximity

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.bearing_box`
              - Get the parameters for a bearing box, defining a volume, relative to a bearing from the North, around an object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.bearing_ellipse`
              - Get the parameters for a bearing ellipse, defining an ellipse, relative to a bearing from the North, around the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.control_box`
              - Get the parameters for a control box, defining a volume around the object that moves with the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.ellipsoid`
              - Define the ellipsoid parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.geo_box`
              - Get the parameters for a geostationary box, a planar rectangle centered at a fixed longitude in space and used to visually check that a GEO satellite stays within a certain area.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.line_of_bearing`
              - Get the parameters for a line of bearing parameters drawn from an origin in the direction of a bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.uncertainty_area_label_swap_distance`
              - Area of uncertainty label swap distance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DOrbitProximity


Property detail
---------------

.. py:property:: bearing_box
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.bearing_box
    :type: VehicleGraphics3DBearingBox

    Get the parameters for a bearing box, defining a volume, relative to a bearing from the North, around an object.

.. py:property:: bearing_ellipse
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.bearing_ellipse
    :type: VehicleGraphics3DBearingEllipse

    Get the parameters for a bearing ellipse, defining an ellipse, relative to a bearing from the North, around the object.

.. py:property:: control_box
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.control_box
    :type: VehicleGraphics3DControlBox

    Get the parameters for a control box, defining a volume around the object that moves with the object.

.. py:property:: ellipsoid
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.ellipsoid
    :type: VehicleGraphics3DEllipsoid

    Define the ellipsoid parameters.

.. py:property:: geo_box
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.geo_box
    :type: VehicleGraphics3DGeoBox

    Get the parameters for a geostationary box, a planar rectangle centered at a fixed longitude in space and used to visually check that a GEO satellite stays within a certain area.

.. py:property:: line_of_bearing
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.line_of_bearing
    :type: VehicleGraphics3DLineOfBearing

    Get the parameters for a line of bearing parameters drawn from an origin in the direction of a bearing.

.. py:property:: uncertainty_area_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity.uncertainty_area_label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Area of uncertainty label swap distance.


