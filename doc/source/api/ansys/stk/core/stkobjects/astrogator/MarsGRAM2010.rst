MarsGRAM2010
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Mars-GRAM 2010 atmospheric propagator function.

.. py:currentmodule:: MarsGRAM2010

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.computes_temperature`
              - Flag indicates whether this model computes temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.computes_pressure`
              - Flag indicates whether this model computes pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.sun_position`
              - Gets or sets the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.data_directory`
              - Path to the data directory.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.namelist_file`
              - Full path of namelist file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.density_type`
              - Low, mean, high or randomly perturbed density type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.atmos_data_source`
              - Gets or sets the atmospheric model data source - data file or constant values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.f_10_p7`
              - Solar Flux (F10.7); the daily Ottawa 10.7 cm solar flux value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.atmos_data_filename`
              - Gets or sets the atmospheric model data file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.drag_model_type`
              - Drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.drag_model_plugin_name`
              - Gets or sets the name of the drag model plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.n_plate_definition_file`
              - Drag N-Plate definition file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MarsGRAM2010


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: data_directory
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.data_directory
    :type: str

    Path to the data directory.

.. py:property:: namelist_file
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.namelist_file
    :type: str

    Full path of namelist file.

.. py:property:: density_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.density_type
    :type: MARS_GRAM_DENSITY_TYPE

    Low, mean, high or randomly perturbed density type.

.. py:property:: atmos_data_source
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.atmos_data_source
    :type: ATMOS_DATA_SOURCE

    Gets or sets the atmospheric model data source - data file or constant values.

.. py:property:: f_10_p7
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.f_10_p7
    :type: float

    Solar Flux (F10.7); the daily Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: atmos_data_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.atmos_data_filename
    :type: str

    Gets or sets the atmospheric model data file path.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.drag_model_type
    :type: DRAG_MODEL_TYPE

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.drag_model_plugin
    :type: IDragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2010.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


