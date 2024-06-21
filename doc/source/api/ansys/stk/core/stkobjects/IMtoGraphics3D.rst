IMtoGraphics3D
==============

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics3D

   object
   
   Interface for MTO 3D graphics properties.

.. py:currentmodule:: IMtoGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3D.tracks`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3D.default_track`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3D.global_track_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3D


Property detail
---------------

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3D.tracks
    :type: IMtoGraphics3DTrackCollection

    Get the collection of MTO 3D graphics settings.

.. py:property:: default_track
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3D.default_track
    :type: IMtoDefaultGraphics3DTrack

    Get the default track 3D graphics settings.

.. py:property:: global_track_options
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3D.global_track_options
    :type: IMtoGraphics3DGlobalTrackOptions

    Get the MTO global track 3D options.


