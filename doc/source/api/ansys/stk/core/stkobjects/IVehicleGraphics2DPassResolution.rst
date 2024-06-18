IVehicleGraphics2DPassResolution
================================

.. py:class:: IVehicleGraphics2DPassResolution

   object
   
   Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~ground_track`
            * - :py:meth:`~orbit`
            * - :py:meth:`~min_ground_track`
            * - :py:meth:`~min_orbit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DPassResolution


Property detail
---------------

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPassResolution.ground_track
    :type: float

    Ground track resolution defined in terms of the ephemeris step. Uses Time Dimension.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPassResolution.orbit
    :type: float

    Orbit resolution defined in terms of the ephemeris step. Uses Time Dimension.

.. py:property:: min_ground_track
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPassResolution.min_ground_track
    :type: float

    Minimum ground track resolution defined in terms of the ephemeris step. Uses Time Dimension.

.. py:property:: min_orbit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPassResolution.min_orbit
    :type: float

    Minimum orbit resolution defined in terms of the ephemeris step. Uses Time Dimension.


