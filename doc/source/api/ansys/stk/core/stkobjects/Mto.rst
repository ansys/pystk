Mto
===

.. py:class:: ansys.stk.core.stkobjects.Mto

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Multi-Track Object (MTO).

.. py:currentmodule:: Mto

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Mto.tracks`
              - Get the collection of MTO tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.Mto.default_track`
              - Get the default MTO track.
            * - :py:attr:`~ansys.stk.core.stkobjects.Mto.global_track_options`
              - Get the global MTO track options.
            * - :py:attr:`~ansys.stk.core.stkobjects.Mto.graphics`
              - Get the MTO's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Mto.graphics_3d`
              - Get the MTO's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Mto.analysis`
              - Get the MTO's spatial state.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Mto


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.Mto.tracks
    :type: MtoTrackCollection

    Get the collection of MTO tracks.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.Mto.default_track
    :type: MtoDefaultTrack

    Get the default MTO track.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.Mto.global_track_options
    :type: MtoGlobalTrackOptions

    Get the global MTO track options.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Mto.graphics
    :type: MtoGraphics

    Get the MTO's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Mto.graphics_3d
    :type: MtoGraphics3D

    Get the MTO's 3D Graphics properties.

.. py:property:: analysis
    :canonical: ansys.stk.core.stkobjects.Mto.analysis
    :type: MtoAnalysis

    Get the MTO's spatial state.


