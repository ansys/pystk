IMtoDefaultGraphics2DTrack
==========================

.. py:class:: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack

   object
   
   Interface to set 2D graphics attributes for default MTO tracks.

.. py:currentmodule:: IMtoDefaultGraphics2DTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.is_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.label_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.label_color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.marker`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.line`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.fade_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.lead_trail_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.range_contours`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoDefaultGraphics2DTrack


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.is_visible
    :type: bool

    Opt whether the track will be displayed.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.color
    :type: agcolor.Color

    Select the color in which the track will be displayed.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.label_visible
    :type: bool

    Opt whether the track label will be displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.label_color
    :type: agcolor.Color

    Select the color in which the track label will be displayed.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.marker
    :type: IMtoGraphics2DMarker

    Get the display properties for the track marker.

.. py:property:: line
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.line
    :type: IMtoGraphics2DLine

    Get the display properties for the track line.

.. py:property:: fade_times
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.fade_times
    :type: IMtoGraphics2DFadeTimes

    Get the fade times data.

.. py:property:: lead_trail_times
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.lead_trail_times
    :type: IMtoGraphics2DLeadTrailTimes

    Get the lead/trail times data.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMtoDefaultGraphics2DTrack.range_contours
    :type: IGraphics2DRangeContours

    Get the MTO's 2D range contour graphics.


