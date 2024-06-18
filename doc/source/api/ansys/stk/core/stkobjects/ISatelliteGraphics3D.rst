ISatelliteGraphics3D
====================

.. py:class:: ISatelliteGraphics3D

   object
   
   3D Graphics properties of a satellite.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~model`
            * - :py:meth:`~orbit_systems`
            * - :py:meth:`~proximity`
            * - :py:meth:`~elev_contours`
            * - :py:meth:`~saa`
            * - :py:meth:`~covariance_pointing_contour`
            * - :py:meth:`~pass_method`
            * - :py:meth:`~offsets`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~covariance`
            * - :py:meth:`~vector`
            * - :py:meth:`~data_display`
            * - :py:meth:`~model_pointing`
            * - :py:meth:`~drop_lines`
            * - :py:meth:`~b_planes`
            * - :py:meth:`~vapor_trail`
            * - :py:meth:`~velocity_covariance`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISatelliteGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.model
    :type: "IAgSaVOModel"

    Get the satellite's Model properties.

.. py:property:: orbit_systems
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.orbit_systems
    :type: "IAgVeVOSystemsCollection"

    Get the satellite's OrbitSystem properties.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.proximity
    :type: "IAgVeVOOrbitProximity"

    Get the satellite's Proximity properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.elev_contours
    :type: "IAgVeVOElevContours"

    Get the satellite's Elevation Contours properties.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.saa
    :type: "IAgVeVOSAA"

    Get the satellite's South Atlantic Anomaly Contour properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.covariance_pointing_contour
    :type: "IAgVeVOCovariancePointingContour"

    Get the satellite's Covariance Pointing Contour properties.

.. py:property:: pass_method
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.pass_method
    :type: "IAgVeVOPass"

    Get the satellite's Pass properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.offsets
    :type: "IAgVOOffset"

    Get the satellite's Offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.range_contours
    :type: "IAgVORangeContours"

    Get the satellite's Range Contours properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.covariance
    :type: "IAgVeVOCovariance"

    Get the satellite's Covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.vector
    :type: "IAgVOVector"

    Get the satellite's Vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.data_display
    :type: "IAgVODataDisplayCollection"

    Get the satellite's Data Display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.model_pointing
    :type: "IAgVOModelPointing"

    Get the satellite's Model Pointing properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.drop_lines
    :type: "IAgVeVOOrbitDropLines"

    Get the satellite's Droplines properties.

.. py:property:: b_planes
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.b_planes
    :type: "IAgVeVOBPlanes"

    Gets the BPlane.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.vapor_trail
    :type: "IAgVOVaporTrail"

    Vapor trail attributes.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.velocity_covariance
    :type: "IAgVeVOVelCovariance"

    Get the satellite's 3D velocity covariance properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics3D.radar_cross_section
    :type: "IAgRadarCrossSectionVO"

    Gets the radar cross section graphics interface.


