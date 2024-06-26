IJacchiaBowman2008
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008

   object
   
   Properties for the Jacchia Bowman 2008 atmospheric density model.

.. py:currentmodule:: IJacchiaBowman2008

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.sun_position`
              - Gets or sets the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.atmos_data_source`
              - Gets or sets the atmospheric model data source - data file or constant values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.f10`
              - Solar Flux (F10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.f10_avg`
              - Average solar Flux (F10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.m10`
              - Solar Flux (M10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.m10_avg`
              - Average solar Flux (M10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.s10`
              - Solar Flux (S10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.s10_avg`
              - Average solar Flux (S10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.y10`
              - Solar Flux (Y10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.y10_avg`
              - Average solar Flux (Y10). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.dst_d_tc`
              - Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.atmos_aug_data_file`
              - Gets or sets the atmospheric model space weather data file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.atmos_aug_dtc_file`
              - Gets or sets the atmospheric model DTC file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.drag_model_type`
              - Drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.drag_model_plugin_name`
              - Gets or sets the name of the drag model plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.n_plate_definition_file`
              - Drag N-Plate definition file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IJacchiaBowman2008


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: atmos_data_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.atmos_data_source
    :type: ATMOS_DATA_SOURCE

    Gets or sets the atmospheric model data source - data file or constant values.

.. py:property:: f10
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.f10
    :type: float

    Solar Flux (F10). Dimensionless.

.. py:property:: f10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.f10_avg
    :type: float

    Average solar Flux (F10). Dimensionless.

.. py:property:: m10
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.m10
    :type: float

    Solar Flux (M10). Dimensionless.

.. py:property:: m10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.m10_avg
    :type: float

    Average solar Flux (M10). Dimensionless.

.. py:property:: s10
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.s10
    :type: float

    Solar Flux (S10). Dimensionless.

.. py:property:: s10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.s10_avg
    :type: float

    Average solar Flux (S10). Dimensionless.

.. py:property:: y10
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.y10
    :type: float

    Solar Flux (Y10). Dimensionless.

.. py:property:: y10_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.y10_avg
    :type: float

    Average solar Flux (Y10). Dimensionless.

.. py:property:: dst_d_tc
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.dst_d_tc
    :type: float

    Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.

.. py:property:: atmos_aug_data_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.atmos_aug_data_file
    :type: str

    Gets or sets the atmospheric model space weather data file path.

.. py:property:: atmos_aug_dtc_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.atmos_aug_dtc_file
    :type: str

    Gets or sets the atmospheric model DTC file path.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.drag_model_type
    :type: DRAG_MODEL_TYPE

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.drag_model_plugin
    :type: IDragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


