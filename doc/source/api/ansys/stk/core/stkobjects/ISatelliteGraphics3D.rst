ISatelliteGraphics3D
====================

.. py:class:: ansys.stk.core.stkobjects.ISatelliteGraphics3D

   object
   
   3D Graphics properties of a satellite.

.. py:currentmodule:: ISatelliteGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.model`
              - Get the satellite's Model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.orbit_systems`
              - Get the satellite's OrbitSystem properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.proximity`
              - Get the satellite's Proximity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.elev_contours`
              - Get the satellite's Elevation Contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.saa`
              - Get the satellite's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.covariance_pointing_contour`
              - Get the satellite's Covariance Pointing Contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.pass_method`
              - Get the satellite's Pass properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.offsets`
              - Get the satellite's Offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.range_contours`
              - Get the satellite's Range Contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.covariance`
              - Get the satellite's Covariance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.vector`
              - Get the satellite's Vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.data_display`
              - Get the satellite's Data Display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.model_pointing`
              - Get the satellite's Model Pointing properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.drop_lines`
              - Get the satellite's Droplines properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.b_planes`
              - Gets the BPlane.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.velocity_covariance`
              - Get the satellite's 3D velocity covariance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteGraphics3D.radar_cross_section`
              - Gets the radar cross section graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISatelliteGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.model
    :type: ISatelliteGraphics3DModel

    Get the satellite's Model properties.

.. py:property:: orbit_systems
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.orbit_systems
    :type: IVehicleGraphics3DSystemsCollection

    Get the satellite's OrbitSystem properties.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.proximity
    :type: IVehicleGraphics3DOrbitProximity

    Get the satellite's Proximity properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.elev_contours
    :type: IVehicleGraphics3DElevContours

    Get the satellite's Elevation Contours properties.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.saa
    :type: IVehicleGraphics3DSAA

    Get the satellite's South Atlantic Anomaly Contour properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.covariance_pointing_contour
    :type: IVehicleGraphics3DCovariancePointingContour

    Get the satellite's Covariance Pointing Contour properties.

.. py:property:: pass_method
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.pass_method
    :type: IVehicleGraphics3DPass

    Get the satellite's Pass properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.offsets
    :type: IGraphics3DOffset

    Get the satellite's Offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.range_contours
    :type: IGraphics3DRangeContours

    Get the satellite's Range Contours properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.covariance
    :type: IVehicleGraphics3DCovariance

    Get the satellite's Covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.vector
    :type: IGraphics3DVector

    Get the satellite's Vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.data_display
    :type: IGraphics3DDataDisplayCollection

    Get the satellite's Data Display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.model_pointing
    :type: IGraphics3DModelPointing

    Get the satellite's Model Pointing properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.drop_lines
    :type: IVehicleGraphics3DOrbitDropLines

    Get the satellite's Droplines properties.

.. py:property:: b_planes
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.b_planes
    :type: IVehicleGraphics3DBPlanes

    Gets the BPlane.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.vapor_trail
    :type: IGraphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.velocity_covariance
    :type: IVehicleGraphics3DVelCovariance

    Get the satellite's 3D velocity covariance properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.radar_cross_section
    :type: IRadarCrossSectionGraphics3D

    Gets the radar cross section graphics interface.


