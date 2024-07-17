VehicleAdvanced
===============

.. py:class:: ansys.stk.core.stkobjects.VehicleAdvanced

   Bases: 

   Class defining advanced atmospheric density options for the LOP propagator.

.. py:currentmodule:: VehicleAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAdvanced.atmospheric_density_model`
              - This property is deprecated. Use AtmosDensityModel instead. Atmospheric density model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAdvanced.use_osculating_altitude`
              - Opt whether to use osculating altitude, which uses a short period variation due to J2 perturbations when calculating altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAdvanced.max_drag_altitude`
              - Maximum drag altitude, above which drag calculations are not considered. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAdvanced.density_weighing_factor`
              - Gets or sets the scale factor to be used during density calculations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAdvanced.exp_dens_model_params`
              - Get the exponential density modeling parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAdvanced.atmos_density_model`
              - Atmospheric density model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAdvanced


Property detail
---------------

.. py:property:: atmospheric_density_model
    :canonical: ansys.stk.core.stkobjects.VehicleAdvanced.atmospheric_density_model
    :type: ATMOSPHERIC_DENSITY_MODEL

    This property is deprecated. Use AtmosDensityModel instead. Atmospheric density model.

.. py:property:: use_osculating_altitude
    :canonical: ansys.stk.core.stkobjects.VehicleAdvanced.use_osculating_altitude
    :type: bool

    Opt whether to use osculating altitude, which uses a short period variation due to J2 perturbations when calculating altitude.

.. py:property:: max_drag_altitude
    :canonical: ansys.stk.core.stkobjects.VehicleAdvanced.max_drag_altitude
    :type: float

    Maximum drag altitude, above which drag calculations are not considered. Uses Distance Dimension.

.. py:property:: density_weighing_factor
    :canonical: ansys.stk.core.stkobjects.VehicleAdvanced.density_weighing_factor
    :type: float

    Gets or sets the scale factor to be used during density calculations. Dimensionless.

.. py:property:: exp_dens_model_params
    :canonical: ansys.stk.core.stkobjects.VehicleAdvanced.exp_dens_model_params
    :type: IVehicleExpDensModelParams

    Get the exponential density modeling parameters.

.. py:property:: atmos_density_model
    :canonical: ansys.stk.core.stkobjects.VehicleAdvanced.atmos_density_model
    :type: LOP_ATMOSPHERIC_DENSITY_MODEL

    Atmospheric density model.


