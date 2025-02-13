MTO
===

.. py:class:: ansys.stk.core.stkobjects.MTO

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Multi-Track Object (MTO).

.. py:currentmodule:: MTO

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.tracks`
              - Get the collection of MTO tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.default_track`
              - Get the default MTO track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.global_track_options`
              - Get the global MTO track options.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.graphics`
              - Get the MTO's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.graphics_3d`
              - Get the MTO's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.analysis`
              - Get the MTO's spatial state.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTO


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.MTO.tracks
    :type: MTOTrackCollection

    Get the collection of MTO tracks.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.MTO.default_track
    :type: MTODefaultTrack

    Get the default MTO track.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.MTO.global_track_options
    :type: MTOGlobalTrackOptions

    Get the global MTO track options.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.MTO.graphics
    :type: MTOGraphics

    Get the MTO's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.MTO.graphics_3d
    :type: MTOGraphics3D

    Get the MTO's 3D Graphics properties.

.. py:property:: analysis
    :canonical: ansys.stk.core.stkobjects.MTO.analysis
    :type: MTOAnalysis

    Get the MTO's spatial state.


