IVehicleAdvanced
================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAdvanced

   object
   
   Interface for advanced drag options for LOP propagator.

.. py:currentmodule:: IVehicleAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAdvanced.atmospheric_density_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAdvanced.use_osculating_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAdvanced.max_drag_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAdvanced.density_weighing_factor`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAdvanced.exp_dens_model_params`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAdvanced.atmos_density_model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAdvanced


Property detail
---------------

.. py:property:: atmospheric_density_model
    :canonical: ansys.stk.core.stkobjects.IVehicleAdvanced.atmospheric_density_model
    :type: ATMOSPHERIC_DENSITY_MODEL

    This property is deprecated. Use AtmosDensityModel instead. Atmospheric density model.

.. py:property:: use_osculating_altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleAdvanced.use_osculating_altitude
    :type: bool

    Opt whether to use osculating altitude, which uses a short period variation due to J2 perturbations when calculating altitude.

.. py:property:: max_drag_altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleAdvanced.max_drag_altitude
    :type: float

    Maximum drag altitude, above which drag calculations are not considered. Uses Distance Dimension.

.. py:property:: density_weighing_factor
    :canonical: ansys.stk.core.stkobjects.IVehicleAdvanced.density_weighing_factor
    :type: float

    Gets or sets the scale factor to be used during density calculations. Dimensionless.

.. py:property:: exp_dens_model_params
    :canonical: ansys.stk.core.stkobjects.IVehicleAdvanced.exp_dens_model_params
    :type: IVehicleExpDensModelParams

    Get the exponential density modeling parameters.

.. py:property:: atmos_density_model
    :canonical: ansys.stk.core.stkobjects.IVehicleAdvanced.atmos_density_model
    :type: LOP_ATMOSPHERIC_DENSITY_MODEL

    Atmospheric density model.


