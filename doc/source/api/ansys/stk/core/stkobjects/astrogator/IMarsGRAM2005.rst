IMarsGRAM2005
=============

.. py:class:: IMarsGRAM2005

   object
   
   Properties for the Mars-GRAM 2005 atmospheric model.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_approximate_altitude`
            * - :py:meth:`~computes_temperature`
            * - :py:meth:`~computes_pressure`
            * - :py:meth:`~sun_position`
            * - :py:meth:`~data_directory`
            * - :py:meth:`~namelist_file`
            * - :py:meth:`~density_type`
            * - :py:meth:`~atmos_data_source`
            * - :py:meth:`~f_10_p7`
            * - :py:meth:`~atmos_data_filename`
            * - :py:meth:`~drag_model_type`
            * - :py:meth:`~drag_model_plugin_name`
            * - :py:meth:`~drag_model_plugin`
            * - :py:meth:`~variable_area_history_file`
            * - :py:meth:`~n_plate_definition_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMarsGRAM2005


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: data_directory
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.data_directory
    :type: str

    Path to the data directory.

.. py:property:: namelist_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.namelist_file
    :type: str

    Full path of namelist file.

.. py:property:: density_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.density_type
    :type: MARS_GRAM_DENSITY_TYPE

    Low, mean, high or randomly perturbed density type.

.. py:property:: atmos_data_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.atmos_data_source
    :type: ATMOS_DATA_SOURCE

    Gets or sets the atmospheric model data source - data file or constant values.

.. py:property:: f_10_p7
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.f_10_p7
    :type: float

    Solar Flux (F10.7); the daily Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: atmos_data_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.atmos_data_filename
    :type: str

    Gets or sets the atmospheric model data file path.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.drag_model_type
    :type: DRAG_MODEL_TYPE

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.drag_model_plugin
    :type: IAgVADragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


