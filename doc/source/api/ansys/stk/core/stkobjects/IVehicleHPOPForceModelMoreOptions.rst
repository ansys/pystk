IVehicleHPOPForceModelMoreOptions
=================================

.. py:class:: IVehicleHPOPForceModelMoreOptions

   object
   
   Interface for additional force model options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~drag`
            * - :py:meth:`~solar_radiation_pressure`
            * - :py:meth:`~static`
            * - :py:meth:`~solid_tides`
            * - :py:meth:`~ocean_tides`
            * - :py:meth:`~radiation_pressure`
            * - :py:meth:`~plugin_propagator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPForceModelMoreOptions


Property detail
---------------

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.drag
    :type: IAgVeHPOPForceModelDragOptions

    Get the additional atmospheric drag options.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.solar_radiation_pressure
    :type: IAgVeHPOPSolarRadiationPressureOptions

    Get the additional solar radiation pressure options.

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.static
    :type: IAgVeStatic

    Get the static force model options concerning satellite mass and relativistic accelerations.

.. py:property:: solid_tides
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.solid_tides
    :type: IAgVeSolidTides

    Get the solid tides options.

.. py:property:: ocean_tides
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.ocean_tides
    :type: IAgVeOceanTides

    Get the ocean tides options.

.. py:property:: radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.radiation_pressure
    :type: IAgVeRadiationPressure

    Get the radiation pressure options.

.. py:property:: plugin_propagator
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelMoreOptions.plugin_propagator
    :type: IAgVePluginPropagator

    Get the plugin propagator parameters.


