AircraftGraphics
================

.. py:class:: ansys.stk.core.stkobjects.AircraftGraphics

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGreatArcGraphics`

   2D Graphics for an aircraft.

.. py:currentmodule:: AircraftGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics.elev_contours`
              - Get the aircraft's 2D elevation contour graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics.swath`
              - Get the aircraft's 2D swath graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.AircraftGraphics.radar_cross_section`
              - Gets the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AircraftGraphics


Property detail
---------------

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics.elev_contours
    :type: VehicleGraphics2DElevContours

    Get the aircraft's 2D elevation contour graphics.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics.swath
    :type: VehicleGraphics2DSwath

    Get the aircraft's 2D swath graphics.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.AircraftGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Gets the radar cross section graphics interface.


