IMtoGraphics3DTrack
===================

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics3DTrack

   object
   
   Interface for setting 3D graphics properties for MTO tracks.

.. py:currentmodule:: IMtoGraphics3DTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.is_visible`
              - Opt whether to display the track in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.marker`
              - Get the track's 3D marker properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.point`
              - Get the track's 3D point properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.model`
              - Get the track's 3D model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.label`
              - Get the track's 3D label properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.swap_distances`
              - Get the track's 3D swap distance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.range_contours`
              - Get the MTO's 3D range contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.drop_lines`
              - Returns an interface allowing you to configure the MTO's drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.id`
              - Get the identification number of the track. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DTrack.should_fade_over_trail_time`
              - Controls whether trailing line fades over trail time.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DTrack


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.is_visible
    :type: bool

    Opt whether to display the track in the 3D Graphics window.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.marker
    :type: IMtoGraphics3DMarker

    Get the track's 3D marker properties.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.point
    :type: IMtoGraphics3DPoint

    Get the track's 3D point properties.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.model
    :type: IMtoGraphics3DModel

    Get the track's 3D model properties.

.. py:property:: label
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.label
    :type: IGraphics3DOffsetLabel

    Get the track's 3D label properties.

.. py:property:: swap_distances
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.swap_distances
    :type: IMtoGraphics3DSwapDistances

    Get the track's 3D swap distance properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.range_contours
    :type: IGraphics3DRangeContours

    Get the MTO's 3D range contour properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.drop_lines
    :type: IMtoGraphics3DDropLines

    Returns an interface allowing you to configure the MTO's drop lines.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.id
    :type: int

    Get the identification number of the track. Dimensionless.

.. py:property:: should_fade_over_trail_time
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.should_fade_over_trail_time
    :type: bool

    Controls whether trailing line fades over trail time.


