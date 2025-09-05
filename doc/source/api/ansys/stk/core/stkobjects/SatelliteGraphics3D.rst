SatelliteGraphics3D
===================

.. py:class:: ansys.stk.core.stkobjects.SatelliteGraphics3D

   3D Graphics properties of a satellite.

.. py:currentmodule:: SatelliteGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.b_planes`
              - Get the BPlane.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.covariance`
              - Get the satellite's Covariance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.covariance_pointing_contour`
              - Get the satellite's Covariance Pointing Contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.data_display`
              - Get the satellite's Data Display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.drop_lines`
              - Get the satellite's Droplines properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.elevation_contours`
              - Get the satellite's Elevation Contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.model`
              - Get the satellite's Model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.model_pointing`
              - Get the satellite's Model Pointing properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.offsets`
              - Get the satellite's Offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.orbit_systems`
              - Get the satellite's OrbitSystem properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.proximity`
              - Get the satellite's Proximity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.range_contours`
              - Get the satellite's Range Contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.saa`
              - Get the satellite's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.satellite_pass`
              - Get the satellite's Pass properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.vector`
              - Get the satellite's Vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteGraphics3D.velocity_covariance`
              - Get the satellite's 3D velocity covariance properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SatelliteGraphics3D


Property detail
---------------

.. py:property:: b_planes
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.b_planes
    :type: VehicleGraphics3DBPlanes

    Get the BPlane.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.covariance
    :type: VehicleGraphics3DCovariance

    Get the satellite's Covariance properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.covariance_pointing_contour
    :type: VehicleGraphics3DCovariancePointingContour

    Get the satellite's Covariance Pointing Contour properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.data_display
    :type: Graphics3DDataDisplayCollection

    Get the satellite's Data Display properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.drop_lines
    :type: VehicleGraphics3DOrbitDropLines

    Get the satellite's Droplines properties.

.. py:property:: elevation_contours
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.elevation_contours
    :type: VehicleGraphics3DElevationContours

    Get the satellite's Elevation Contours properties.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.model
    :type: SatelliteGraphics3DModel

    Get the satellite's Model properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Get the satellite's Model Pointing properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.offsets
    :type: Graphics3DOffset

    Get the satellite's Offsets properties.

.. py:property:: orbit_systems
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.orbit_systems
    :type: VehicleGraphics3DSystemsCollection

    Get the satellite's OrbitSystem properties.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.proximity
    :type: VehicleGraphics3DOrbitProximity

    Get the satellite's Proximity properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Get the satellite's Range Contours properties.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.saa
    :type: VehicleGraphics3DSAA

    Get the satellite's South Atlantic Anomaly Contour properties.

.. py:property:: satellite_pass
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.satellite_pass
    :type: VehicleGraphics3DPass

    Get the satellite's Pass properties.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.vector
    :type: Graphics3DVector

    Get the satellite's Vector properties.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.SatelliteGraphics3D.velocity_covariance
    :type: VehicleGraphics3DVelocityCovariance

    Get the satellite's 3D velocity covariance properties.


