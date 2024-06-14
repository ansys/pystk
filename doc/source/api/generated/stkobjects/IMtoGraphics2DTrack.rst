IMtoGraphics2DTrack
===================

.. py:class:: IMtoGraphics2DTrack

   object
   
   Interface to set 2D graphics attributes for each track in the MTO.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~label_visible`
            * - :py:meth:`~label_color`
            * - :py:meth:`~marker`
            * - :py:meth:`~line`
            * - :py:meth:`~fade_times`
            * - :py:meth:`~lead_trail_times`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~id`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics2DTrack


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.is_visible
    :type: bool

    Opt whether the track will be displayed.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.color
    :type: agcolor.Color

    Select the color in which the track will be displayed.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.label_visible
    :type: bool

    Opt whether the track label will be displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.label_color
    :type: agcolor.Color

    Select the color in which the track label will be displayed.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.marker
    :type: "IAgMtoGfxMarker"

    Get the display properties for the track marker.

.. py:property:: line
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.line
    :type: "IAgMtoGfxLine"

    Get the display properties for the track line.

.. py:property:: fade_times
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.fade_times
    :type: "IAgMtoGfxFadeTimes"

    Get the fade times data.

.. py:property:: lead_trail_times
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.lead_trail_times
    :type: "IAgMtoGfxLeadTrailTimes"

    Get the lead/trail times data.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.range_contours
    :type: "IAgGfxRangeContours"

    Get the MTO's 2D range contour graphics.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrack.id
    :type: int

    Get the identification number of the track. Dimensionless.


