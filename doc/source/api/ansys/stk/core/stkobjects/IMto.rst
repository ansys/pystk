IMto
====

.. py:class:: IMto

   object
   
   Multi-Track Object (MTO) interface.

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
            * - :py:meth:`~graphics`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~analysis`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMto


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.IMto.tracks
    :type: IAgMtoTrackCollection

    Get the collection of MTO tracks.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.IMto.default_track
    :type: IAgMtoDefaultTrack

    Get the default MTO track.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.IMto.global_track_options
    :type: IAgMtoGlobalTrackOptions

    Get the global MTO track options.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IMto.graphics
    :type: IAgMtoGraphics

    Get the MTO's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IMto.graphics_3d
    :type: IAgMtoVO

    Get the MTO's 3D Graphics properties.

.. py:property:: analysis
    :canonical: ansys.stk.core.stkobjects.IMto.analysis
    :type: IAgMtoAnalysis

    Get the MTO's spatial state.


