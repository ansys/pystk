IVehicleHPOPForceModel
======================

.. py:class:: ansys.stk.core.stkobjects.IVehicleHPOPForceModel

   object
   
   Interface for HPOP force models.

.. py:currentmodule:: IVehicleHPOPForceModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModel.central_body_gravity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModel.solar_radiation_pressure`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModel.drag`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModel.third_body_gravity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModel.more_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModel.eclipsing_bodies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPForceModel


Property detail
---------------

.. py:property:: central_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.central_body_gravity
    :type: IVehicleHPOPCentralBodyGravity

    Get the central body gravity properties.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.solar_radiation_pressure
    :type: IVehicleHPOPSolarRadiationPressure

    Get the solar radiation pressure properties.

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.drag
    :type: IVehicleHPOPForceModelDrag

    Get the atmospheric drag properties.

.. py:property:: third_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.third_body_gravity
    :type: IVehicleThirdBodyGravityCollection

    Get the 3rd-body gravity properties.

.. py:property:: more_options
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.more_options
    :type: IVehicleHPOPForceModelMoreOptions

    Get the additional force model options.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.eclipsing_bodies
    :type: IVehicleEclipsingBodies

    Get the eclipsing bodies.


