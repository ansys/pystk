AircraftGraphics3D
==================

.. py:class:: ansys.stk.core.stkobjects.AircraftGraphics3D

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D`

   3D Graphics properties for an aircraft.

.. py:currentmodule:: AircraftGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics3D.covariance_pointing_contour`
              - Get the aircraft's 3D covariance pointing properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics3D.drop_lines`
              - Return an interface allowing to configure vehicle's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics3D.elevation_contours`
              - Get the aircraft's 3D elevation contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics3D.proximity`
              - Get the aircraft's 3D proximity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics3D.vapor_trail`
              - Vapor trail attributes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AircraftGraphics3D


Property detail
---------------

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics3D.covariance_pointing_contour
    :type: VehicleGraphics3DCovariancePointingContour

    Get the aircraft's 3D covariance pointing properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics3D.drop_lines
    :type: VehicleGraphics3DRouteDropLines

    Return an interface allowing to configure vehicle's drop lines.

.. py:property:: elevation_contours
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics3D.elevation_contours
    :type: VehicleGraphics3DElevationContours

    Get the aircraft's 3D elevation contour properties.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics3D.proximity
    :type: VehicleGraphics3DRouteProximity

    Get the aircraft's 3D proximity properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.


