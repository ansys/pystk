MtoDefaultGraphics2DTrack
=========================

.. py:class:: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack

   Bases: 

   2D graphics attributes for default MTO tracks.

.. py:currentmodule:: MtoDefaultGraphics2DTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.is_visible`
              - Opt whether the track will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.color`
              - Select the color in which the track will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.label_visible`
              - Opt whether the track label will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.label_color`
              - Select the color in which the track label will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.marker`
              - Get the display properties for the track marker.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.line`
              - Get the display properties for the track line.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.fade_times`
              - Get the fade times data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.lead_trail_times`
              - Get the lead/trail times data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.range_contours`
              - Get the MTO's 2D range contour graphics.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoDefaultGraphics2DTrack


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.is_visible
    :type: bool

    Opt whether the track will be displayed.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.color
    :type: agcolor.Color

    Select the color in which the track will be displayed.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.label_visible
    :type: bool

    Opt whether the track label will be displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.label_color
    :type: agcolor.Color

    Select the color in which the track label will be displayed.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.marker
    :type: IMtoGraphics2DMarker

    Get the display properties for the track marker.

.. py:property:: line
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.line
    :type: IMtoGraphics2DLine

    Get the display properties for the track line.

.. py:property:: fade_times
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.fade_times
    :type: IMtoGraphics2DFadeTimes

    Get the fade times data.

.. py:property:: lead_trail_times
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.lead_trail_times
    :type: IMtoGraphics2DLeadTrailTimes

    Get the lead/trail times data.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack.range_contours
    :type: IGraphics2DRangeContours

    Get the MTO's 2D range contour graphics.


