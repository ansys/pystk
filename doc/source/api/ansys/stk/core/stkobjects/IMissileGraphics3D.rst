IMissileGraphics3D
==================

.. py:class:: IMissileGraphics3D

   object
   
   3D Graphics for missiles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~model`
            * - :py:meth:`~proximity`
            * - :py:meth:`~elev_contours`
            * - :py:meth:`~covariance_pointing_contour`
            * - :py:meth:`~trajectory_systems`
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

    from ansys.stk.core.stkobjects import IMissileGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.model
    :type: IAgVeTrajectoryVOModel

    Get the missile's 3D model graphics.

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.proximity
    :type: IAgVeVOTrajectoryProximity

    Get the missile's 3D proximity graphics.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.elev_contours
    :type: IAgVeVOElevContours

    Get the missile's 3D elevation contour graphics.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.covariance_pointing_contour
    :type: IAgVeVOCovariancePointingContour

    Get the missile's 3D covariance pointing graphics.

.. py:property:: trajectory_systems
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.trajectory_systems
    :type: IAgVeVOSystemsCollection

    Get the missile's 3D trajectory frame graphics.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.trajectory
    :type: IAgVeVOTrajectory

    Get the missile's 3D trajectory graphics.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.offsets
    :type: IAgVOOffset

    Get the missile's 3D offsets graphics.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.range_contours
    :type: IAgVORangeContours

    Get the missile's 3D range contour graphics.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.covariance
    :type: IAgVeVOCovariance

    Get the missile's 3D covariance graphics.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.vector
    :type: IAgVOVector

    Get the missile's 3D vector graphics.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.data_display
    :type: IAgVODataDisplayCollection

    Get the missile's 3D data display graphics.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.model_pointing
    :type: IAgVOModelPointing

    Use to point parts of a facility or vehicle model toward a target, such as the Sun or Earth.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.drop_lines
    :type: IAgVeVOTrajectoryDropLines

    Returns an interface allowing to configure vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.vapor_trail
    :type: IAgVOVaporTrail

    Vapor trail attributes.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.saa
    :type: IAgVeVOSAA

    Get the missile's South Atlantic Anomaly Contour properties.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.velocity_covariance
    :type: IAgVeVOVelCovariance

    Get the missile's 3D velocity covariance properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics3D.radar_cross_section
    :type: IAgRadarCrossSectionVO

    Gets the radar cross section graphics interface.


