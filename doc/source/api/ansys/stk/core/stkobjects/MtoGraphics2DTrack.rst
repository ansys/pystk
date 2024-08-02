MtoGraphics2DTrack
==================

.. py:class:: ansys.stk.core.stkobjects.MtoGraphics2DTrack

   2D graphics attributes for each track in the MTO.

.. py:currentmodule:: MtoGraphics2DTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.is_visible`
              - Opt whether the track will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.color`
              - Select the color in which the track will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.label_visible`
              - Opt whether the track label will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.label_color`
              - Select the color in which the track label will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.marker`
              - Get the display properties for the track marker.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.line`
              - Get the display properties for the track line.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.fade_times`
              - Get the fade times data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.lead_trail_times`
              - Get the lead/trail times data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.range_contours`
              - Get the MTO's 2D range contour graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack.id`
              - Get the identification number of the track. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoGraphics2DTrack


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.is_visible
    :type: bool

    Opt whether the track will be displayed.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.color
    :type: agcolor.Color

    Select the color in which the track will be displayed.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.label_visible
    :type: bool

    Opt whether the track label will be displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.label_color
    :type: agcolor.Color

    Select the color in which the track label will be displayed.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.marker
    :type: MtoGraphics2DMarker

    Get the display properties for the track marker.

.. py:property:: line
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.line
    :type: MtoGraphics2DLine

    Get the display properties for the track line.

.. py:property:: fade_times
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.fade_times
    :type: MtoGraphics2DFadeTimes

    Get the fade times data.

.. py:property:: lead_trail_times
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.lead_trail_times
    :type: MtoGraphics2DLeadTrailTimes

    Get the lead/trail times data.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.range_contours
    :type: Graphics2DRangeContours

    Get the MTO's 2D range contour graphics.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DTrack.id
    :type: int

    Get the identification number of the track. Dimensionless.


