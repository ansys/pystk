IMtoGraphics3DTrack
===================

.. py:class:: IMtoGraphics3DTrack

   object
   
   Interface for setting 3D graphics properties for MTO tracks.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~marker`
            * - :py:meth:`~point`
            * - :py:meth:`~model`
            * - :py:meth:`~label`
            * - :py:meth:`~swap_distances`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~drop_lines`
            * - :py:meth:`~id`
            * - :py:meth:`~should_fade_over_trail_time`


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
    :type: "IAgMtoVOMarker"

    Get the track's 3D marker properties.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.point
    :type: "IAgMtoVOPoint"

    Get the track's 3D point properties.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.model
    :type: "IAgMtoVOModel"

    Get the track's 3D model properties.

.. py:property:: label
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.label
    :type: "IAgVOOffsetLabel"

    Get the track's 3D label properties.

.. py:property:: swap_distances
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.swap_distances
    :type: "IAgMtoVOSwapDistances"

    Get the track's 3D swap distance properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.range_contours
    :type: "IAgVORangeContours"

    Get the MTO's 3D range contour properties.

.. py:property:: drop_lines
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.drop_lines
    :type: "IAgMtoVODropLines"

    Returns an interface allowing you to configure the MTO's drop lines.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.id
    :type: int

    Get the identification number of the track. Dimensionless.

.. py:property:: should_fade_over_trail_time
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DTrack.should_fade_over_trail_time
    :type: bool

    Controls whether trailing line fades over trail time.


