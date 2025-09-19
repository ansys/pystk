VehicleGraphics2DOrbitPassData
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DOrbitPassData

   VehicleGraphics2DOrbitPassData Class.

.. py:currentmodule:: VehicleGraphics2DOrbitPassData

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DOrbitPassData.ground_track`
              - Ground track display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DOrbitPassData.orbit`
              - Orbit pass display properties.



Examples
--------

Set 2D/3D Pass Display Properties

.. code-block:: python

    # Satellite satellite: Satellite object
    # Display one pass for ground track and orbit on 2D
    passdata = satellite.graphics.pass_data
    groundTrack = passdata.ground_track
    groundTrack.set_lead_data_type(LeadTrailData.ONE_PASS)
    groundTrack.set_trail_same_as_lead
    orbit = passdata.orbit
    orbit.set_lead_data_type(LeadTrailData.ONE_PASS)
    orbit.set_trail_same_as_lead
    # Display one orbit pass and no ground track on 3D
    passdata3D = satellite.graphics_3d.satellite_pass.track_data.pass_data
    groundTrack3D = passdata3D.ground_track
    groundTrack3D.set_lead_data_type(LeadTrailData.NONE)
    groundTrack3D.set_trail_same_as_lead
    orbit3D = passdata3D.orbit
    orbit3D.set_lead_data_type(LeadTrailData.ONE_PASS)
    orbit3D.set_trail_same_as_lead


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DOrbitPassData


Property detail
---------------

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DOrbitPassData.ground_track
    :type: VehicleGraphics2DLeadTrailData

    Ground track display properties.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DOrbitPassData.orbit
    :type: VehicleGraphics2DLeadTrailData

    Orbit pass display properties.


