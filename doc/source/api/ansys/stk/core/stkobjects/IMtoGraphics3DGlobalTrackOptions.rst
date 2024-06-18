IMtoGraphics3DGlobalTrackOptions
================================

.. py:class:: IMtoGraphics3DGlobalTrackOptions

   object
   
   Interface for global 3D graphics MTO track options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~tracks_visible`
            * - :py:meth:`~labels_visible`
            * - :py:meth:`~markers_visible`
            * - :py:meth:`~lines_visible`
            * - :py:meth:`~points_visible`
            * - :py:meth:`~optimize_lines`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DGlobalTrackOptions


Property detail
---------------

.. py:property:: tracks_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DGlobalTrackOptions.tracks_visible
    :type: bool

    Opt whether to display MTO graphics in the 3D graphics window.

.. py:property:: labels_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DGlobalTrackOptions.labels_visible
    :type: bool

    Opt whether to display MTO track labels in the 3D graphics window.

.. py:property:: markers_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DGlobalTrackOptions.markers_visible
    :type: bool

    Opt whether to display MTO track markers in the 3D graphics window.

.. py:property:: lines_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DGlobalTrackOptions.lines_visible
    :type: bool

    Opt whether to display MTO track lines in the 3D graphics window.

.. py:property:: points_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DGlobalTrackOptions.points_visible
    :type: bool

    Opt whether to display MTO track points in the 3D graphics window.

.. py:property:: optimize_lines
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DGlobalTrackOptions.optimize_lines
    :type: bool

    Opt whether interpolated route lines will be displayed with higher accuracy. This can be very resource intensive and may degrade performance, but will improve visual quality.


