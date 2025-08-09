MTOGraphics2DTrack
==================

.. py:class:: ansys.stk.core.stkobjects.MTOGraphics2DTrack

   2D graphics attributes for each track in the MTO.

.. py:currentmodule:: MTOGraphics2DTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.show_graphics`
              - Opt whether the track will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.color`
              - Select the color in which the track will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.show_label`
              - Opt whether the track label will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.label_color`
              - Select the color in which the track label will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.marker`
              - Get the display properties for the track marker.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.line`
              - Get the display properties for the track line.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.fade_times`
              - Get the fade times data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.lead_trail_times`
              - Get the lead/trail times data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.range_contours`
              - Get the MTO's 2D range contour graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack.identifier`
              - Get the identification number of the track. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOGraphics2DTrack


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.show_graphics
    :type: bool

    Opt whether the track will be displayed.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.color
    :type: Color

    Select the color in which the track will be displayed.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.show_label
    :type: bool

    Opt whether the track label will be displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.label_color
    :type: Color

    Select the color in which the track label will be displayed.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.marker
    :type: MTOGraphics2DMarker

    Get the display properties for the track marker.

.. py:property:: line
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.line
    :type: MTOGraphics2DLine

    Get the display properties for the track line.

.. py:property:: fade_times
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.fade_times
    :type: MTOGraphics2DFadeTimes

    Get the fade times data.

.. py:property:: lead_trail_times
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.lead_trail_times
    :type: MTOGraphics2DLeadTrailTimes

    Get the lead/trail times data.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.range_contours
    :type: Graphics2DRangeContours

    Get the MTO's 2D range contour graphics.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrack.identifier
    :type: int

    Get the identification number of the track. Dimensionless.


