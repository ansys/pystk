IMto
====

.. py:class:: ansys.stk.core.stkobjects.IMto

   object
   
   Multi-Track Object (MTO) interface.

.. py:currentmodule:: IMto

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMto.tracks`
              - Get the collection of MTO tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMto.default_track`
              - Get the default MTO track.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMto.global_track_options`
              - Get the global MTO track options.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMto.graphics`
              - Get the MTO's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMto.graphics_3d`
              - Get the MTO's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMto.analysis`
              - Get the MTO's spatial state.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMto


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.IMto.tracks
    :type: IMtoTrackCollection

    Get the collection of MTO tracks.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.IMto.default_track
    :type: IMtoDefaultTrack

    Get the default MTO track.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.IMto.global_track_options
    :type: IMtoGlobalTrackOptions

    Get the global MTO track options.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IMto.graphics
    :type: IMtoGraphics

    Get the MTO's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IMto.graphics_3d
    :type: IMtoGraphics3D

    Get the MTO's 3D Graphics properties.

.. py:property:: analysis
    :canonical: ansys.stk.core.stkobjects.IMto.analysis
    :type: IMtoAnalysis

    Get the MTO's spatial state.


