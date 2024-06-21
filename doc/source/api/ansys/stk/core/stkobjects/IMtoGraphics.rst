IMtoGraphics
============

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics

   object
   
   MTO 2D Graphics interface.

.. py:currentmodule:: IMtoGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics.tracks`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics.default_track`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics.global_track_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics.is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.tracks
    :type: IMtoGraphics2DTrackCollection

    Get the collection of MTO 2D graphics properties.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.default_track
    :type: IMtoDefaultGraphics2DTrack

    Get the default track 2D graphics.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.global_track_options
    :type: IMtoGraphics2DGlobalTrackOptions

    Get the 2D graphics global settings.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the MTO are visible.


