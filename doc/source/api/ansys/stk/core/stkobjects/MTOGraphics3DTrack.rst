MTOGraphics3DTrack
==================

.. py:class:: ansys.stk.core.stkobjects.MTOGraphics3DTrack

   3D graphics properties for MTO tracks.

.. py:currentmodule:: MTOGraphics3DTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.drop_lines`
              - Return an interface allowing you to configure the MTO's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.identifier`
              - Get the identification number of the track. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.label`
              - Get the track's 3D label properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.marker`
              - Get the track's 3D marker properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.model`
              - Get the track's 3D model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.point`
              - Get the track's 3D point properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.range_contours`
              - Get the MTO's 3D range contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.should_fade_over_trail_time`
              - Control whether trailing line fades over trail time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.show_graphics`
              - Opt whether to display the track in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack.swap_distances`
              - Get the track's 3D swap distance properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOGraphics3DTrack


Property detail
---------------

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.drop_lines
    :type: MTOGraphics3DDropLines

    Return an interface allowing you to configure the MTO's drop lines.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.identifier
    :type: int

    Get the identification number of the track. Dimensionless.

.. py:property:: label
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.label
    :type: Graphics3DOffsetLabel

    Get the track's 3D label properties.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.marker
    :type: MTOGraphics3DMarker

    Get the track's 3D marker properties.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.model
    :type: MTOGraphics3DModel

    Get the track's 3D model properties.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.point
    :type: MTOGraphics3DPoint

    Get the track's 3D point properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.range_contours
    :type: Graphics3DRangeContours

    Get the MTO's 3D range contour properties.

.. py:property:: should_fade_over_trail_time
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.should_fade_over_trail_time
    :type: bool

    Control whether trailing line fades over trail time.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.show_graphics
    :type: bool

    Opt whether to display the track in the 3D Graphics window.

.. py:property:: swap_distances
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DTrack.swap_distances
    :type: MTOGraphics3DSwapDistances

    Get the track's 3D swap distance properties.


