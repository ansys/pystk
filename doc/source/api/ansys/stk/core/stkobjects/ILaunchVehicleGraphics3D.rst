ILaunchVehicleGraphics3D
========================

.. py:class:: ILaunchVehicleGraphics3D

   object
   
   3D Graphics for a launch vehicle.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~model`
            * - :py:meth:`~trajectory_systems`
            * - :py:meth:`~proximity`
            * - :py:meth:`~elev_contours`
            * - :py:meth:`~covariance_pointing_contour`
            * - :py:meth:`~trajectory`
            * - :py:meth:`~offsets`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~covariance`
            * - :py:meth:`~vector`
            * - :py:meth:`~data_display`
            * - :py:meth:`~model_pointing`
            * - :py:meth:`~drop_lines`
            * - :py:meth:`~vapor_trail`
            * - :py:meth:`~saa`
            * - :py:meth:`~velocity_covariance`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILaunchVehicleGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.model
    :type: IAgVeTrajectoryVOModel

    Get the launch vehicle's 3D model properties.

.. py:property:: trajectory_systems
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.trajectory_systems
    :type: IAgVeVOSystemsCollection

    Get the launch vehicle's 3D trajectory frame properties.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.proximity
    :type: IAgVeVOTrajectoryProximity

    Get the launch vehicle's 3D proximity properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.elev_contours
    :type: IAgVeVOElevContours

    Get the launch vehicle's 3D elevation contour properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.covariance_pointing_contour
    :type: IAgVeVOCovariancePointingContour

    Get the launch vehicle's 3D covariance pointing properties.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.trajectory
    :type: IAgVeVOTrajectory

    Get the launch vehicle's 3D trajectory properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.offsets
    :type: IAgVOOffset

    Get the launch vehicle's 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.range_contours
    :type: IAgVORangeContours

    Get the launch vehicle's 3D range contour properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.covariance
    :type: IAgVeVOCovariance

    Get the launch vehicle's 3D covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.vector
    :type: IAgVOVector

    Get the launch vehicle's 3D vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.data_display
    :type: IAgVODataDisplayCollection

    Get the launch vehicle's 3D data display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.model_pointing
    :type: IAgVOModelPointing

    Use to point parts of a launch vehicle's model toward a target, such as the Sun or Earth.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.drop_lines
    :type: IAgVeVOTrajectoryDropLines

    Returns an interface allowing to configure launch vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.vapor_trail
    :type: IAgVOVaporTrail

    Vapor trail attributes.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.saa
    :type: IAgVeVOSAA

    Get the launch vehicle's South Atlantic Anomaly Contour properties.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.velocity_covariance
    :type: IAgVeVOVelCovariance

    Get the launch vehicle's 3D velocity covariance properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics3D.radar_cross_section
    :type: IAgRadarCrossSectionVO

    Gets the radar cross section graphics interface.


