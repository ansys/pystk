MtoDefaultGraphics3DTrack
=========================

.. py:class:: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack

   3D graphics properties for default MTO tracks.

.. py:currentmodule:: MtoDefaultGraphics3DTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.is_visible`
              - Opt whether to display the track in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.marker`
              - Get the track's 3D marker properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.point`
              - Get the track's 3D point properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.model`
              - Get the track's 3D model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.label`
              - Get the track's 3D label properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.swap_distances`
              - Get the track's 3D swap distance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.range_contours`
              - Get the MTO's 3D range contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.drop_lines`
              - Returns an interface allowing you to configure the MTO's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.should_fade_over_trail_time`
              - Controls whether trailing line fades over trail time.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoDefaultGraphics3DTrack


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.is_visible
    :type: bool

    Opt whether to display the track in the 3D Graphics window.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.marker
    :type: MtoGraphics3DMarker

    Get the track's 3D marker properties.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.point
    :type: MtoGraphics3DPoint

    Get the track's 3D point properties.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.model
    :type: MtoGraphics3DModel

    Get the track's 3D model properties.

.. py:property:: label
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.label
    :type: Graphics3DOffsetLabel

    Get the track's 3D label properties.

.. py:property:: swap_distances
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.swap_distances
    :type: MtoGraphics3DSwapDistances

    Get the track's 3D swap distance properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.range_contours
    :type: Graphics3DRangeContours

    Get the MTO's 3D range contour properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.drop_lines
    :type: MtoGraphics3DDropLines

    Returns an interface allowing you to configure the MTO's drop lines.

.. py:property:: should_fade_over_trail_time
    :canonical: ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack.should_fade_over_trail_time
    :type: bool

    Controls whether trailing line fades over trail time.


