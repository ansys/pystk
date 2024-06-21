INRLMSISE_2000
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000

   object
   
   Properties for the NRLMSISE 2000 atmospheric model.

.. py:currentmodule:: INRLMSISE_2000

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.use_approximate_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.computes_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.computes_pressure`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.sun_position`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_source`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.f_10_p7`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.f_10_p7_avg`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.kp`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_geo_magnetic_flux_source`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_geo_magnetic_flux_update_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_filename`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.drag_model_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.drag_model_plugin_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.drag_model_plugin`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.variable_area_history_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.n_plate_definition_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import INRLMSISE_2000


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: atmos_data_source
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_source
    :type: ATMOS_DATA_SOURCE

    Gets or sets the atmospheric model data source - data file or constant values.

.. py:property:: f_10_p7
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.f_10_p7
    :type: float

    Solar Flux (F10.7); the daily Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: f_10_p7_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.f_10_p7_avg
    :type: float

    Average solar Flux (F10.7); the 81-day averaged Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: kp
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.kp
    :type: float

    Geomagnetic Index (Kp). Dimensionless.

.. py:property:: atmos_data_geo_magnetic_flux_source
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_geo_magnetic_flux_source
    :type: GEO_MAGNETIC_FLUX_SOURCE

    Whether to use Kp or Ap data from the flux file.

.. py:property:: atmos_data_geo_magnetic_flux_update_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_geo_magnetic_flux_update_rate
    :type: GEO_MAGNETIC_FLUX_UPDATE_RATE

    Gets or sets the update rate for geomagnetic flux values from the flux file.

.. py:property:: atmos_data_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.atmos_data_filename
    :type: str

    Gets or sets the atmospheric model data file path.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.drag_model_type
    :type: DRAG_MODEL_TYPE

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.drag_model_plugin
    :type: IDragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


