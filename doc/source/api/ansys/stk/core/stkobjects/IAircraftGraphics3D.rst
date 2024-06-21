IAircraftGraphics3D
===================

.. py:class:: ansys.stk.core.stkobjects.IAircraftGraphics3D

   IGreatArcGraphics3D
   
   3D Graphics properties for an aircraft.

.. py:currentmodule:: IAircraftGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraftGraphics3D.proximity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraftGraphics3D.elev_contours`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraftGraphics3D.covariance_pointing_contour`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraftGraphics3D.drop_lines`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraftGraphics3D.vapor_trail`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAircraftGraphics3D.radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAircraftGraphics3D


Property detail
---------------

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.proximity
    :type: IVehicleGraphics3DRouteProximity

    Get the aircraft's 3D proximity properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.elev_contours
    :type: IVehicleGraphics3DElevContours

    Get the aircraft's 3D elevation contour properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.covariance_pointing_contour
    :type: IVehicleGraphics3DCovariancePointingContour

    Get the aircraft's 3D covariance pointing properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.drop_lines
    :type: IVehicleGraphics3DRouteDropLines

    Returns an interface allowing to configure vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.vapor_trail
    :type: IGraphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.radar_cross_section
    :type: IRadarCrossSectionGraphics3D

    Gets the radar cross section graphics interface.


