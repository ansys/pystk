IVehicleGraphics3DTrajectoryTickMarks
=====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks

   object
   
   Tick mark data interface for launch vehicles and missiles.

.. py:currentmodule:: IVehicleGraphics3DTrajectoryTickMarks

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks.time_between_ticks`
              - Time between tick marks: the time elapsed between each milestone indicated by a tick mark along the vehicle's path. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks.ground_track`
              - Get the ground track tick marks.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks.trajectory`
              - Get the trajectory tick marks.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DTrajectoryTickMarks


Property detail
---------------

.. py:property:: time_between_ticks
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks.time_between_ticks
    :type: float

    Time between tick marks: the time elapsed between each milestone indicated by a tick mark along the vehicle's path. Uses Time Dimension.

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks.ground_track
    :type: IVehicleGraphics3DPathTickMarks

    Get the ground track tick marks.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks.trajectory
    :type: IVehicleGraphics3DPathTickMarks

    Get the trajectory tick marks.


