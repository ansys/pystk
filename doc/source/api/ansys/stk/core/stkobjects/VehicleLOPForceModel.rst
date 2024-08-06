VehicleLOPForceModel
====================

.. py:class:: ansys.stk.core.stkobjects.VehicleLOPForceModel

   Class defining the force model for the LOP propagator.

.. py:currentmodule:: VehicleLOPForceModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPForceModel.central_body_gravity`
              - Get the central body gravity parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPForceModel.third_body_gravity`
              - Get the 3rd body gravity parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPForceModel.drag`
              - Get the atmospheric drag parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPForceModel.solar_radiation_pressure`
              - Get the solar radiation pressure parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPForceModel.physical_data`
              - Get the physical data parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleLOPForceModel


Property detail
---------------

.. py:property:: central_body_gravity
    :canonical: ansys.stk.core.stkobjects.VehicleLOPForceModel.central_body_gravity
    :type: VehicleLOPCentralBodyGravity

    Get the central body gravity parameters.

.. py:property:: third_body_gravity
    :canonical: ansys.stk.core.stkobjects.VehicleLOPForceModel.third_body_gravity
    :type: VehicleThirdBodyGravity

    Get the 3rd body gravity parameters.

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.VehicleLOPForceModel.drag
    :type: VehicleLOPForceModelDrag

    Get the atmospheric drag parameters.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.VehicleLOPForceModel.solar_radiation_pressure
    :type: VehicleLOPSolarRadiationPressure

    Get the solar radiation pressure parameters.

.. py:property:: physical_data
    :canonical: ansys.stk.core.stkobjects.VehicleLOPForceModel.physical_data
    :type: VehiclePhysicalData

    Get the physical data parameters.


