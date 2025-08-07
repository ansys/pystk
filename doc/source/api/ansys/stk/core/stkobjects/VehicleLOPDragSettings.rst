VehicleLOPDragSettings
======================

.. py:class:: ansys.stk.core.stkobjects.VehicleLOPDragSettings

   Class defining advanced atmospheric density options for the LOP propagator.

.. py:currentmodule:: VehicleLOPDragSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPDragSettings.atmosphere_density_model`
              - Atmospheric density model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPDragSettings.atmospheric_density_model`
              - Do not use this property, as it is deprecated. Use AtmosDensityModel instead. Atmospheric density model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPDragSettings.density_weighing_factor`
              - Get or set the scale factor to be used during density calculations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPDragSettings.exponential_density_model_parameters`
              - Get the exponential density modeling parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPDragSettings.maximum_drag_altitude`
              - Maximum drag altitude, above which drag calculations are not considered. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPDragSettings.use_osculating_altitude`
              - Opt whether to use osculating altitude, which uses a short period variation due to J2 perturbations when calculating altitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleLOPDragSettings


Property detail
---------------

.. py:property:: atmosphere_density_model
    :canonical: ansys.stk.core.stkobjects.VehicleLOPDragSettings.atmosphere_density_model
    :type: LOPAtmosphericDensityModel

    Atmospheric density model.

.. py:property:: atmospheric_density_model
    :canonical: ansys.stk.core.stkobjects.VehicleLOPDragSettings.atmospheric_density_model
    :type: AtmosphericDensityModel

    Do not use this property, as it is deprecated. Use AtmosDensityModel instead. Atmospheric density model.

.. py:property:: density_weighing_factor
    :canonical: ansys.stk.core.stkobjects.VehicleLOPDragSettings.density_weighing_factor
    :type: float

    Get or set the scale factor to be used during density calculations. Dimensionless.

.. py:property:: exponential_density_model_parameters
    :canonical: ansys.stk.core.stkobjects.VehicleLOPDragSettings.exponential_density_model_parameters
    :type: VehicleExponentialDensityModelParameters

    Get the exponential density modeling parameters.

.. py:property:: maximum_drag_altitude
    :canonical: ansys.stk.core.stkobjects.VehicleLOPDragSettings.maximum_drag_altitude
    :type: float

    Maximum drag altitude, above which drag calculations are not considered. Uses Distance Dimension.

.. py:property:: use_osculating_altitude
    :canonical: ansys.stk.core.stkobjects.VehicleLOPDragSettings.use_osculating_altitude
    :type: bool

    Opt whether to use osculating altitude, which uses a short period variation due to J2 perturbations when calculating altitude.


