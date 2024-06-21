ILaunchVehicleGraphics3D
========================

.. py:class:: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D

   object
   
   3D Graphics for a launch vehicle.

.. py:currentmodule:: ILaunchVehicleGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.model`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.trajectory_systems`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.proximity`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.elev_contours`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.covariance_pointing_contour`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.trajectory`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.offsets`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.range_contours`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.covariance`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.vector`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.data_display`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.model_pointing`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.drop_lines`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.vapor_trail`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.saa`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.velocity_covariance`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILaunchVehicleGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.model
    :type: IVehicleTrajectoryGraphics3DModel

    Get the launch vehicle's 3D model properties.

.. py:property:: trajectory_systems
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.trajectory_systems
    :type: IVehicleGraphics3DSystemsCollection

    Get the launch vehicle's 3D trajectory frame properties.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.proximity
    :type: IVehicleGraphics3DTrajectoryProximity

    Get the launch vehicle's 3D proximity properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.elev_contours
    :type: IVehicleGraphics3DElevContours

    Get the launch vehicle's 3D elevation contour properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.covariance_pointing_contour
    :type: IVehicleGraphics3DCovariancePointingContour

    Get the launch vehicle's 3D covariance pointing properties.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.trajectory
    :type: IVehicleGraphics3DTrajectory

    Get the launch vehicle's 3D trajectory properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.offsets
    :type: IGraphics3DOffset

    Get the launch vehicle's 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.range_contours
    :type: IGraphics3DRangeContours

    Get the launch vehicle's 3D range contour properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.covariance
    :type: IVehicleGraphics3DCovariance

    Get the launch vehicle's 3D covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.vector
    :type: IGraphics3DVector

    Get the launch vehicle's 3D vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.data_display
    :type: IGraphics3DDataDisplayCollection

    Get the launch vehicle's 3D data display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.model_pointing
    :type: IGraphics3DModelPointing

    Use to point parts of a launch vehicle's model toward a target, such as the Sun or Earth.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.drop_lines
    :type: IVehicleGraphics3DTrajectoryDropLines

    Returns an interface allowing to configure launch vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.vapor_trail
    :type: IGraphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.saa
    :type: IVehicleGraphics3DSAA

    Get the launch vehicle's South Atlantic Anomaly Contour properties.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.velocity_covariance
    :type: IVehicleGraphics3DVelCovariance

    Get the launch vehicle's 3D velocity covariance properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.radar_cross_section
    :type: IRadarCrossSectionGraphics3D

    Gets the radar cross section graphics interface.


