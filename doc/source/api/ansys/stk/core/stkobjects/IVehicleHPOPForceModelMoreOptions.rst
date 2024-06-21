IVehicleHPOPForceModelMoreOptions
=================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions

   object
   
   Interface for additional force model options.

.. py:currentmodule:: IVehicleHPOPForceModelMoreOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.drag`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.solar_radiation_pressure`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.static`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.solid_tides`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.ocean_tides`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.radiation_pressure`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.plugin_propagator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPForceModelMoreOptions


Property detail
---------------

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.drag
    :type: IVehicleHPOPForceModelDragOptions

    Get the additional atmospheric drag options.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.solar_radiation_pressure
    :type: IVehicleHPOPSolarRadiationPressureOptions

    Get the additional solar radiation pressure options.

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.static
    :type: IVehicleStatic

    Get the static force model options concerning satellite mass and relativistic accelerations.

.. py:property:: solid_tides
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.solid_tides
    :type: IVehicleSolidTides

    Get the solid tides options.

.. py:property:: ocean_tides
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.ocean_tides
    :type: IVehicleOceanTides

    Get the ocean tides options.

.. py:property:: radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.radiation_pressure
    :type: IVehicleRadiationPressure

    Get the radiation pressure options.

.. py:property:: plugin_propagator
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.plugin_propagator
    :type: IVehiclePluginPropagator

    Get the plugin propagator parameters.


