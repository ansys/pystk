IVehicleGraphics2DSAA
=====================

.. py:class:: IVehicleGraphics2DSAA

   object
   
   South Atlantic Anomaly contour settings.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~use_vehicle_altitude`
            * - :py:meth:`~altitude`
            * - :py:meth:`~is_fill_visible`
            * - :py:meth:`~translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DSAA


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSAA.is_visible
    :type: bool

    Opt whether to display South Atlantic Anomaly contours.

.. py:property:: use_vehicle_altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSAA.use_vehicle_altitude
    :type: bool

    Opt whether to display South Atlantic Anomaly contours at the satellite's altitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSAA.altitude
    :type: float

    Altitude at which South Atlantic Anomaly contours are to display. Uses Distance Dimension.

.. py:property:: is_fill_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSAA.is_fill_visible
    :type: bool

    Opt whether to display a fill in the region within the South Atlantic Anomaly contours.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSAA.translucency
    :type: float

    Percent translucency (0 to 100) for South Atlantic Anomaly contours if contours are filled. Dimensionless.


