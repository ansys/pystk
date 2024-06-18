IVehicleGraphics2DAttributesTrajectory
======================================

.. py:class:: IVehicleGraphics2DAttributesTrajectory

   IVehicleGraphics2DAttributesBasic
   
   2D Graphics attributes for launch vehicles and missiles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_ground_track_visible`
            * - :py:meth:`~is_ground_marker_visible`
            * - :py:meth:`~is_trajectory_visible`
            * - :py:meth:`~is_trajectory_marker_visible`
            * - :py:meth:`~pick_string`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DAttributesTrajectory


Property detail
---------------

.. py:property:: is_ground_track_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesTrajectory.is_ground_track_visible
    :type: bool

    Opt whether to show the vehicle's ground track.

.. py:property:: is_ground_marker_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesTrajectory.is_ground_marker_visible
    :type: bool

    Opt whether to show the vehicle's ground marker.

.. py:property:: is_trajectory_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesTrajectory.is_trajectory_visible
    :type: bool

    Opt whether to show the vehicle's trajectory path.

.. py:property:: is_trajectory_marker_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesTrajectory.is_trajectory_marker_visible
    :type: bool

    Opt whether to show the vehicle's trajectory marker.

.. py:property:: pick_string
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesTrajectory.pick_string
    :type: str

    String displayed after instance name when the vehicle line is picked in 2D or 3D.


