IVehicleGraphics3DTrajectory
============================

.. py:class:: IVehicleGraphics3DTrajectory

   object
   
   3D pass interface for launch vehicles and missiles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~track_data`
            * - :py:meth:`~tick_marks`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DTrajectory


Property detail
---------------

.. py:property:: track_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectory.track_data
    :type: "IAgVeVOTrajectoryTrackData"

    Get the leading/trailing ground track and trajectory data.

.. py:property:: tick_marks
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectory.tick_marks
    :type: "IAgVeVOTrajectoryTickMarks"

    Get the tick mark data.


