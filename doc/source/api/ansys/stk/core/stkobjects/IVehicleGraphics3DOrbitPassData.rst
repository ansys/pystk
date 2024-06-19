IVehicleGraphics3DOrbitPassData
===============================

.. py:class:: IVehicleGraphics3DOrbitPassData

   object
   
   Interface for satellite 3D ground and orbit track data.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DOrbitPassData


Property detail
---------------

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitPassData.ground_track
    :type: IAgVeVOLeadTrailData

    Get the 3D ground track data.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitPassData.orbit
    :type: IAgVeVOLeadTrailData

    Get the 3D orbit track data.


