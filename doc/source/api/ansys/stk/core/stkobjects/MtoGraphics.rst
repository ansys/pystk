MtoGraphics
===========

.. py:class:: ansys.stk.core.stkobjects.MtoGraphics

   Bases: 

   MTO 2D Graphics.

.. py:currentmodule:: MtoGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics.tracks`
              - Get the collection of MTO 2D graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics.default_track`
              - Get the default track 2D graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics.global_track_options`
              - Get the 2D graphics global settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics.is_object_graphics_visible`
              - Specify whether graphics attributes of the MTO are visible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoGraphics


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.MtoGraphics.tracks
    :type: IMtoGraphics2DTrackCollection

    Get the collection of MTO 2D graphics properties.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.MtoGraphics.default_track
    :type: IMtoDefaultGraphics2DTrack

    Get the default track 2D graphics.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.MtoGraphics.global_track_options
    :type: IMtoGraphics2DGlobalTrackOptions

    Get the 2D graphics global settings.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.MtoGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the MTO are visible.


