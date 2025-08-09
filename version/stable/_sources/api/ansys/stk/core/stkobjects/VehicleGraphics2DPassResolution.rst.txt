VehicleGraphics2DPassResolution
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution

   Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

.. py:currentmodule:: VehicleGraphics2DPassResolution

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.ground_track`
              - Ground track resolution defined in terms of the ephemeris step. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.orbit`
              - Orbit resolution defined in terms of the ephemeris step. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.minimum_ground_track`
              - Minimum ground track resolution defined in terms of the ephemeris step. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.minimum_orbit`
              - Minimum orbit resolution defined in terms of the ephemeris step. Uses Time Dimension.



Examples
--------

Change the graphics resolution of the orbit for a smooth path

.. code-block:: python

    # Satellite satellite: Satellite object
    resolution = satellite.graphics.resolution
    resolution.orbit = 60


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DPassResolution


Property detail
---------------

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.ground_track
    :type: float

    Ground track resolution defined in terms of the ephemeris step. Uses Time Dimension.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.orbit
    :type: float

    Orbit resolution defined in terms of the ephemeris step. Uses Time Dimension.

.. py:property:: minimum_ground_track
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.minimum_ground_track
    :type: float

    Minimum ground track resolution defined in terms of the ephemeris step. Uses Time Dimension.

.. py:property:: minimum_orbit
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution.minimum_orbit
    :type: float

    Minimum orbit resolution defined in terms of the ephemeris step. Uses Time Dimension.


