IVehicleHPOPSolarRadiationPressure
==================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure

   object
   
   Solar Radiation Pressure (SRP) interface.

.. py:currentmodule:: IVehicleHPOPSolarRadiationPressure

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.use`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.shadow_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.use_boundary_mitigation`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.srp_model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPSolarRadiationPressure


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.use
    :type: bool

    Opt whether to take SRP into account.

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.shadow_model
    :type: SHADOW_MODEL

    Type of shadow to be used in determining the lighting condition for the satellite - cylincrical, dual cone, or none.

.. py:property:: use_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.use_boundary_mitigation
    :type: bool

    Opt whether to correct the state of the satellite after crossing a shadow boundary for errors that may have been introduced by the sudden change in the SRP which occurred during the integration step.

.. py:property:: srp_model
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressure.srp_model
    :type: IVehicleHPOPSRPModel

    Returns a solar radiation pressure model.


