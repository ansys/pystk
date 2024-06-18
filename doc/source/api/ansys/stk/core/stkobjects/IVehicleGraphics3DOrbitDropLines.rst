IVehicleGraphics3DOrbitDropLines
================================

.. py:class:: IVehicleGraphics3DOrbitDropLines

   object
   
   Interface for droplines collections.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~orbit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DOrbitDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitDropLines.position
    :type: "IAgVeVODropLinePosItemCollection"

    Get list of droplines from the vehicle's current positions.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitDropLines.orbit
    :type: "IAgVeVODropLinePathItemCollection"

    Get list of droplines at intervals along the vehicle's path.


