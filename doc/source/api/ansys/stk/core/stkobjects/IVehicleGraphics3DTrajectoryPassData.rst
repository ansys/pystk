IVehicleGraphics3DTrajectoryPassData
====================================

.. py:class:: IVehicleGraphics3DTrajectoryPassData

   object
   
   Interface for 3D ground track and trajectory data for a launch vehicle or missile.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~ground_track`
            * - :py:meth:`~trajectory`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DTrajectoryPassData


Property detail
---------------

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryPassData.ground_track
    :type: IAgVeVOLeadTrailData

    Get the 3D ground track data.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryPassData.trajectory
    :type: IAgVeVOLeadTrailData

    Get the 3D trajectory data.


