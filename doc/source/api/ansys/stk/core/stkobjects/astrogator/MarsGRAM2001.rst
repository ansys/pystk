MarsGRAM2001
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Mars-GRAM 2001 atmospheric propagator function.

.. py:currentmodule:: MarsGRAM2001

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.computes_temperature`
              - Flag indicates whether this model computes temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.computes_pressure`
              - Flag indicates whether this model computes pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.sun_position`
              - Gets or sets the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.data_directory`
              - Path to the data directory.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.namelist_file`
              - Path to namelist file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.density_type`
              - Low, mean, high or randomly perturbed density type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.atmos_data_source`
              - Gets or sets the atmospheric model data source - data file or constant values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.f_10_p7`
              - Solar Flux (F10.7); the daily Ottawa 10.7 cm solar flux value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.atmos_data_filename`
              - Gets or sets the atmospheric model data file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.drag_model_type`
              - Drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.drag_model_plugin_name`
              - Gets or sets the name of the drag model plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.n_plate_definition_file`
              - Drag N-Plate definition file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MarsGRAM2001


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.sun_position
    :type: SunPosition

    Gets or sets the sun position computation.

.. py:property:: data_directory
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.data_directory
    :type: str

    Path to the data directory.

.. py:property:: namelist_file
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.namelist_file
    :type: str

    Path to namelist file.

.. py:property:: density_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.density_type
    :type: MarsGRAMDensityType

    Low, mean, high or randomly perturbed density type.

.. py:property:: atmos_data_source
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.atmos_data_source
    :type: AtmosDataSource

    Gets or sets the atmospheric model data source - data file or constant values.

.. py:property:: f_10_p7
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.f_10_p7
    :type: float

    Solar Flux (F10.7); the daily Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: atmos_data_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.atmos_data_filename
    :type: str

    Gets or sets the atmospheric model data file path.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.drag_model_type
    :type: DragModelType

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.drag_model_plugin
    :type: DragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.MarsGRAM2001.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


