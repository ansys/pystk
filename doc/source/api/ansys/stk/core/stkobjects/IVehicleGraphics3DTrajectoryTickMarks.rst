IVehicleGraphics3DTrajectoryTickMarks
=====================================

.. py:class:: IVehicleGraphics3DTrajectoryTickMarks

   object
   
   Tick mark data interface for launch vehicles and missiles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~time_between_ticks`
            * - :py:meth:`~ground_track`
            * - :py:meth:`~trajectory`


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
    :type: "IAgVeVOPathTickMarks"

    Get the ground track tick marks.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryTickMarks.trajectory
    :type: "IAgVeVOPathTickMarks"

    Get the trajectory tick marks.


