IAircraftGraphics3D
===================

.. py:class:: IAircraftGraphics3D

   IGreatArcGraphics3D
   
   3D Graphics properties for an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~proximity`
            * - :py:meth:`~elev_contours`
            * - :py:meth:`~covariance_pointing_contour`
            * - :py:meth:`~drop_lines`
            * - :py:meth:`~vapor_trail`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAircraftGraphics3D


Property detail
---------------

.. py:property:: proximity
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.proximity
    :type: IAgVeVORouteProximity

    Get the aircraft's 3D proximity properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.elev_contours
    :type: IAgVeVOElevContours

    Get the aircraft's 3D elevation contour properties.

.. py:property:: covariance_pointing_contour
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.covariance_pointing_contour
    :type: IAgVeVOCovariancePointingContour

    Get the aircraft's 3D covariance pointing properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.drop_lines
    :type: IAgVeVORouteDropLines

    Returns an interface allowing to configure vehicle's drop lines.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.vapor_trail
    :type: IAgVOVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics3D.radar_cross_section
    :type: IAgRadarCrossSectionVO

    Gets the radar cross section graphics interface.


