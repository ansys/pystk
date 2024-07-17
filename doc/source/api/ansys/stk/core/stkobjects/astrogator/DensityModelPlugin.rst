DensityModelPlugin
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Plugin atmospheric density propagator function.

.. py:currentmodule:: DensityModelPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.plugin_identifier`
              - Gets or sets the plugin name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.plugin_config`
              - Get the properties of the selected plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.computes_temperature`
              - Flag indicates whether this model computes temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.computes_pressure`
              - Flag indicates whether this model computes pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.sun_position`
              - Gets or sets the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_source`
              - Gets or sets the atmospheric model data source - data file or constant values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.f10`
              - Solar Flux (F10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.f10_avg`
              - Average solar Flux (F10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.m10`
              - Solar Flux (M10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.m10_avg`
              - Average solar Flux (M10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.s10`
              - Solar Flux (S10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.s10_avg`
              - Average solar Flux (S10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.y10`
              - Solar Flux (Y10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.y10_avg`
              - Average solar Flux (Y10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.kp`
              - Geomagnetic Index (Kp). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.dst_d_tc`
              - Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_geo_magnetic_flux_source`
              - Whether to use Kp or Ap data from the flux file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_geo_magnetic_flux_update_rate`
              - Gets or sets the update rate for geomagnetic flux values from the flux file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_filename`
              - Gets or sets the atmospheric model data file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_aug_data_file`
              - Gets or sets the atmospheric model augmented data file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_aug_dtc_file`
              - Gets or sets the atmospheric model augmented geomagnetic data file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.drag_model_type`
              - Drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin_name`
              - Gets or sets the name of the drag model plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.uses_augmented_space_weather`
              - Flag indicates whether this model uses augmented flux data.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.n_plate_definition_file`
              - Drag N-Plate definition file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DensityModelPlugin


Property detail
---------------

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.plugin_identifier
    :type: str

    Gets or sets the plugin name.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.plugin_config
    :type: IPluginProperties

    Get the properties of the selected plugin.

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: atmos_data_source
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_source
    :type: ATMOS_DATA_SOURCE

    Gets or sets the atmospheric model data source - data file or constant values.

.. py:property:: f10
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.f10
    :type: float

    Solar Flux (F10). Dimensionless.

.. py:property:: f10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.f10_avg
    :type: float

    Average solar Flux (F10). Dimensionless.

.. py:property:: m10
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.m10
    :type: float

    Solar Flux (M10). Dimensionless.

.. py:property:: m10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.m10_avg
    :type: float

    Average solar Flux (M10). Dimensionless.

.. py:property:: s10
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.s10
    :type: float

    Solar Flux (S10). Dimensionless.

.. py:property:: s10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.s10_avg
    :type: float

    Average solar Flux (S10). Dimensionless.

.. py:property:: y10
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.y10
    :type: float

    Solar Flux (Y10). Dimensionless.

.. py:property:: y10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.y10_avg
    :type: float

    Average solar Flux (Y10). Dimensionless.

.. py:property:: kp
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.kp
    :type: float

    Geomagnetic Index (Kp). Dimensionless.

.. py:property:: dst_d_tc
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.dst_d_tc
    :type: float

    Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.

.. py:property:: atmos_data_geo_magnetic_flux_source
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_geo_magnetic_flux_source
    :type: GEO_MAGNETIC_FLUX_SOURCE

    Whether to use Kp or Ap data from the flux file.

.. py:property:: atmos_data_geo_magnetic_flux_update_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_geo_magnetic_flux_update_rate
    :type: GEO_MAGNETIC_FLUX_UPDATE_RATE

    Gets or sets the update rate for geomagnetic flux values from the flux file.

.. py:property:: atmos_data_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_data_filename
    :type: str

    Gets or sets the atmospheric model data file path.

.. py:property:: atmos_aug_data_file
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_aug_data_file
    :type: str

    Gets or sets the atmospheric model augmented data file path.

.. py:property:: atmos_aug_dtc_file
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.atmos_aug_dtc_file
    :type: str

    Gets or sets the atmospheric model augmented geomagnetic data file path.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.drag_model_type
    :type: DRAG_MODEL_TYPE

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin
    :type: IDragModelPlugin

    Drag model plugin properties.

.. py:property:: uses_augmented_space_weather
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.uses_augmented_space_weather
    :type: bool

    Flag indicates whether this model uses augmented flux data.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.DensityModelPlugin.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


