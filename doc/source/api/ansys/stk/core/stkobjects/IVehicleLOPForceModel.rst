IVehicleLOPForceModel
=====================

.. py:class:: IVehicleLOPForceModel

   object
   
   Force model interface for LOP propagator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_gravity`
            * - :py:meth:`~third_body_gravity`
            * - :py:meth:`~drag`
            * - :py:meth:`~solar_radiation_pressure`
            * - :py:meth:`~physical_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleLOPForceModel


Property detail
---------------

.. py:property:: central_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.central_body_gravity
    :type: "IAgVeLOPCentralBodyGravity"

    Get the central body gravity parameters.

.. py:property:: third_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.third_body_gravity
    :type: "IAgVeThirdBodyGravity"

    Get the 3rd body gravity parameters.

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.drag
    :type: "IAgVeLOPForceModelDrag"

    Get the atmospheric drag parameters.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.solar_radiation_pressure
    :type: "IAgVeLOPSolarRadiationPressure"

    Get the solar radiation pressure parameters.

.. py:property:: physical_data
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.physical_data
    :type: "IAgVePhysicalData"

    Get the physical data parameters.


