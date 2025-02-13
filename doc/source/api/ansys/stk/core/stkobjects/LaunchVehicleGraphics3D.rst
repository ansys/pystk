LaunchVehicleGraphics3D
=======================

.. py:class:: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D

   3D Graphics for a launch vehicle.

.. py:currentmodule:: LaunchVehicleGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.model`
              - Get the launch vehicle's 3D model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.trajectory_systems`
              - Get the launch vehicle's 3D trajectory frame properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.proximity`
              - Get the launch vehicle's 3D proximity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.elevation_contours`
              - Get the launch vehicle's 3D elevation contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.covariance_pointing_contour`
              - Get the launch vehicle's 3D covariance pointing properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.trajectory`
              - Get the launch vehicle's 3D trajectory properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.offsets`
              - Get the launch vehicle's 3D offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.range_contours`
              - Get the launch vehicle's 3D range contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.covariance`
              - Get the launch vehicle's 3D covariance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.vector`
              - Get the launch vehicle's 3D vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.data_display`
              - Get the launch vehicle's 3D data display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.model_pointing`
              - Use to point parts of a launch vehicle's model toward a target, such as the Sun or Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.drop_lines`
              - Return an interface allowing to configure launch vehicle's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.saa`
              - Get the launch vehicle's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.velocity_covariance`
              - Get the launch vehicle's 3D velocity covariance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaunchVehicleGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.model
    :type: VehicleGraphics3DModelTrajectory

    Get the launch vehicle's 3D model properties.

.. py:property:: trajectory_systems
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.trajectory_systems
    :type: VehicleGraphics3DSystemsCollection

    Get the launch vehicle's 3D trajectory frame properties.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.proximity
    :type: VehicleGraphics3DTrajectoryProximity

    Get the launch vehicle's 3D proximity properties.

.. py:property:: elevation_contours
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.elevation_contours
    :type: VehicleGraphics3DElevationContours

    Get the launch vehicle's 3D elevation contour properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.covariance_pointing_contour
    :type: VehicleGraphics3DCovariancePointingContour

    Get the launch vehicle's 3D covariance pointing properties.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.trajectory
    :type: VehicleGraphics3DTrajectory

    Get the launch vehicle's 3D trajectory properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.offsets
    :type: Graphics3DOffset

    Get the launch vehicle's 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Get the launch vehicle's 3D range contour properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.covariance
    :type: VehicleGraphics3DCovariance

    Get the launch vehicle's 3D covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.vector
    :type: Graphics3DVector

    Get the launch vehicle's 3D vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.data_display
    :type: Graphics3DDataDisplayCollection

    Get the launch vehicle's 3D data display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Use to point parts of a launch vehicle's model toward a target, such as the Sun or Earth.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.drop_lines
    :type: VehicleGraphics3DTrajectoryDropLines

    Return an interface allowing to configure launch vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.saa
    :type: VehicleGraphics3DSAA

    Get the launch vehicle's South Atlantic Anomaly Contour properties.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.velocity_covariance
    :type: VehicleGraphics3DVelCovariance

    Get the launch vehicle's 3D velocity covariance properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.


