IVehicleGraphics3DOrbitDropLines
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitDropLines

   object
   
   Interface for droplines collections.

.. py:currentmodule:: IVehicleGraphics3DOrbitDropLines

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitDropLines.position`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitDropLines.orbit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DOrbitDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitDropLines.position
    :type: IVehicleGraphics3DDropLinePositionItemCollection

    Get list of droplines from the vehicle's current positions.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitDropLines.orbit
    :type: IVehicleGraphics3DDropLinePathItemCollection

    Get list of droplines at intervals along the vehicle's path.


