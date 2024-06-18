IAircraftGraphics
=================

.. py:class:: IAircraftGraphics

   IGreatArcGraphics
   
   2D Graphics for an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~elev_contours`
            * - :py:meth:`~swath`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAircraftGraphics


Property detail
---------------

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics.elev_contours
    :type: "IAgVeGfxElevContours"

    Get the aircraft's 2D elevation contour graphics.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics.swath
    :type: "IAgVeGfxSwath"

    Get the aircraft's 2D swath graphics.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IAircraftGraphics.radar_cross_section
    :type: "IAgRadarCrossSectionGraphics"

    Gets the radar cross section graphics interface.


