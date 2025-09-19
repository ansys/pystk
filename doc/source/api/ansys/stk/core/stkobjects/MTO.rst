MTO
===

.. py:class:: ansys.stk.core.stkobjects.MTO

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Multi-Track Object (MTO).

.. py:currentmodule:: MTO

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.analysis`
              - Get the MTO's spatial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.default_track`
              - Get the default MTO track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.global_track_options`
              - Get the global MTO track options.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.graphics`
              - Get the MTO's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.graphics_3d`
              - Get the MTO's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTO.tracks`
              - Get the collection of MTO tracks.



Examples
--------

Load multi-track object (MTO) track points from a file

.. code-block:: python

    # load_points expects the path an Ephemeris file path
    # MTO mto: MTO Object
    track2 = mto.tracks.add(2)
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    track2.points.load_points(
        os.path.join(installPath, "Data", "Resources", "stktraining", "text", "EphemerisLLATimePosVel_Example.e")
    )
    track2.interpolate = True


Create a New MTO (on the current scenario central body)

.. code-block:: python

    # Scenario scenario: Scenario object
    mto = scenario.children.new(STKObjectType.MTO, "MyMTO")

    root.units_preferences.set_current_unit("DateFormat", "EpSec")

    mtoTimes = [[0], [7200]]
    mtoLats = [[36.77], [34.80]]
    mtoLons = [[-77.25], [-78.37]]
    mtoAlts = [[5], [5]]

    track1 = mto.tracks.add_track(1, mtoTimes, mtoLats, mtoLons, mtoAlts)
    track1.interpolate = True
    # Change the color of the track
    mto.graphics.tracks.get_track_from_identifier(1).color = Colors.Red


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTO


Property detail
---------------

.. py:property:: analysis
    :canonical: ansys.stk.core.stkobjects.MTO.analysis
    :type: MTOAnalysis

    Get the MTO's spatial state.

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

.. py:property:: tracks
    :canonical: ansys.stk.core.stkobjects.MTO.tracks
    :type: MTOTrackCollection

    Get the collection of MTO tracks.


