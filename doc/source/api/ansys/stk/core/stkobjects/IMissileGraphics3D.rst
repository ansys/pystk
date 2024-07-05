IMissileGraphics3D
==================

.. py:class:: ansys.stk.core.stkobjects.IMissileGraphics3D

   object
   
   3D Graphics for missiles.

.. py:currentmodule:: IMissileGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.model`
              - Get the missile's 3D model graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.proximity`
              - Get the missile's 3D proximity graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.elev_contours`
              - Get the missile's 3D elevation contour graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.covariance_pointing_contour`
              - Get the missile's 3D covariance pointing graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.trajectory_systems`
              - Get the missile's 3D trajectory frame graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.trajectory`
              - Get the missile's 3D trajectory graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.offsets`
              - Get the missile's 3D offsets graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.range_contours`
              - Get the missile's 3D range contour graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.covariance`
              - Get the missile's 3D covariance graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.vector`
              - Get the missile's 3D vector graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.data_display`
              - Get the missile's 3D data display graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.model_pointing`
              - Use to point parts of a facility or vehicle model toward a target, such as the Sun or Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.drop_lines`
              - Returns an interface allowing to configure vehicle's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.saa`
              - Get the missile's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.velocity_covariance`
              - Get the missile's 3D velocity covariance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics3D.radar_cross_section`
              - Gets the radar cross section graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMissileGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.model
    :type: IVehicleTrajectoryGraphics3DModel

    Get the missile's 3D model graphics.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.proximity
    :type: IVehicleGraphics3DTrajectoryProximity

    Get the missile's 3D proximity graphics.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.elev_contours
    :type: IVehicleGraphics3DElevContours

    Get the missile's 3D elevation contour graphics.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.covariance_pointing_contour
    :type: IVehicleGraphics3DCovariancePointingContour

    Get the missile's 3D covariance pointing graphics.

.. py:property:: trajectory_systems
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.trajectory_systems
    :type: IVehicleGraphics3DSystemsCollection

    Get the missile's 3D trajectory frame graphics.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.trajectory
    :type: IVehicleGraphics3DTrajectory

    Get the missile's 3D trajectory graphics.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.offsets
    :type: IGraphics3DOffset

    Get the missile's 3D offsets graphics.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.range_contours
    :type: IGraphics3DRangeContours

    Get the missile's 3D range contour graphics.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.covariance
    :type: IVehicleGraphics3DCovariance

    Get the missile's 3D covariance graphics.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.vector
    :type: IGraphics3DVector

    Get the missile's 3D vector graphics.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.data_display
    :type: IGraphics3DDataDisplayCollection

    Get the missile's 3D data display graphics.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.model_pointing
    :type: IGraphics3DModelPointing

    Use to point parts of a facility or vehicle model toward a target, such as the Sun or Earth.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.drop_lines
    :type: IVehicleGraphics3DTrajectoryDropLines

    Returns an interface allowing to configure vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.vapor_trail
    :type: IGraphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.saa
    :type: IVehicleGraphics3DSAA

    Get the missile's South Atlantic Anomaly Contour properties.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.velocity_covariance
    :type: IVehicleGraphics3DVelCovariance

    Get the missile's 3D velocity covariance properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.radar_cross_section
    :type: IRadarCrossSectionGraphics3D

    Gets the radar cross section graphics interface.


