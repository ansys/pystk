IMtoGraphics
============

.. py:class:: IMtoGraphics

   object
   
   MTO 2D Graphics interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~tracks`
            * - :py:meth:`~default_track`
            * - :py:meth:`~global_track_options`
            * - :py:meth:`~is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.tracks
    :type: "IAgMtoGfxTrackCollection"

    Get the collection of MTO 2D graphics properties.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.default_track
    :type: "IAgMtoDefaultGfxTrack"

    Get the default track 2D graphics.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.global_track_options
    :type: "IAgMtoGfxGlobalTrackOptions"

    Get the 2D graphics global settings.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the MTO are visible.


