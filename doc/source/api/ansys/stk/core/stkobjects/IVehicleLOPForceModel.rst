IVehicleLOPForceModel
=====================

.. py:class:: ansys.stk.core.stkobjects.IVehicleLOPForceModel

   object
   
   Force model interface for LOP propagator.

.. py:currentmodule:: IVehicleLOPForceModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModel.central_body_gravity`
              - Get the central body gravity parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModel.third_body_gravity`
              - Get the 3rd body gravity parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModel.drag`
              - Get the atmospheric drag parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModel.solar_radiation_pressure`
              - Get the solar radiation pressure parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModel.physical_data`
              - Get the physical data parameters.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleLOPForceModel


Property detail
---------------

.. py:property:: central_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.central_body_gravity
    :type: IVehicleLOPCentralBodyGravity

    Get the central body gravity parameters.

.. py:property:: third_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.third_body_gravity
    :type: IVehicleThirdBodyGravity

    Get the 3rd body gravity parameters.

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.drag
    :type: IVehicleLOPForceModelDrag

    Get the atmospheric drag parameters.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.solar_radiation_pressure
    :type: IVehicleLOPSolarRadiationPressure

    Get the solar radiation pressure parameters.

.. py:property:: physical_data
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModel.physical_data
    :type: IVehiclePhysicalData

    Get the physical data parameters.


