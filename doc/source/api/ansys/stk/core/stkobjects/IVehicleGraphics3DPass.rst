IVehicleGraphics3DPass
======================

.. py:class:: IVehicleGraphics3DPass

   object
   
   3D pass interface for satellites.

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

    from ansys.stk.core.stkobjects import IVehicleGraphics3DPass


Property detail
---------------

.. py:property:: track_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DPass.track_data
    :type: "IAgVeVOOrbitTrackData"

    Get the leading/trailing ground and orbit track data.

.. py:property:: tick_marks
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DPass.tick_marks
    :type: "IAgVeVOOrbitTickMarks"

    Get the tick mark data.


