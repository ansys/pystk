IVehicleGraphics3DRoute
=======================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DRoute

   object
   
   3D route graphics interface for great arc vehicles.

.. py:currentmodule:: IVehicleGraphics3DRoute

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DRoute.inherit_track_data_from_2d`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DRoute.track_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DRoute.waypoint_markers`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DRoute


Property detail
---------------

.. py:property:: inherit_track_data_from_2d
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRoute.inherit_track_data_from_2d
    :type: bool

    Opt whether to inherit from 2D route graphics.

.. py:property:: track_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRoute.track_data
    :type: IVehicleGraphics3DLeadTrailData

    Get the leading/trailing route data.

.. py:property:: waypoint_markers
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRoute.waypoint_markers
    :type: IVehicleGraphics3DWaypointMarkersCollection

    Get the waypoint markers data.


