VehicleHPOPSolarRadiationPressure
=================================

.. py:class:: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure

   Class defining HPOP solar radiation pressure properties.

.. py:currentmodule:: VehicleHPOPSolarRadiationPressure

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.shadow_model`
              - Type of shadow to be used in determining the lighting condition for the satellite - cylincrical, dual cone, or none.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.solar_radiation_pressure_model`
              - Return a solar radiation pressure model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.use`
              - Opt whether to take SRP into account.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.use_boundary_mitigation`
              - Opt whether to correct the state of the satellite after crossing a shadow boundary for errors that may have been introduced by the sudden change in the SRP which occurred during the integration step.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleHPOPSolarRadiationPressure


Property detail
---------------

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.shadow_model
    :type: SolarRadiationPressureShadowModelType

    Type of shadow to be used in determining the lighting condition for the satellite - cylincrical, dual cone, or none.

.. py:property:: solar_radiation_pressure_model
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.solar_radiation_pressure_model
    :type: VehicleHPOPSolarRadiationPressureModel

    Return a solar radiation pressure model.

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.use
    :type: bool

    Opt whether to take SRP into account.

.. py:property:: use_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure.use_boundary_mitigation
    :type: bool

    Opt whether to correct the state of the satellite after crossing a shadow boundary for errors that may have been introduced by the sudden change in the SRP which occurred during the integration step.


