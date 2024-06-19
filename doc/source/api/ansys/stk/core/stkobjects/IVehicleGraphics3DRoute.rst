IVehicleGraphics3DRoute
=======================

.. py:class:: IVehicleGraphics3DRoute

   object
   
   3D route graphics interface for great arc vehicles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inherit_track_data_from_2d`
            * - :py:meth:`~track_data`
            * - :py:meth:`~waypoint_markers`


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
    :type: IAgVeVOLeadTrailData

    Get the leading/trailing route data.

.. py:property:: waypoint_markers
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRoute.waypoint_markers
    :type: IAgVeVOWaypointMarkersCollection

    Get the waypoint markers data.


