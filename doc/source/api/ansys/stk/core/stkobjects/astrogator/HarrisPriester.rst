HarrisPriester
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.HarrisPriester

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Harris-Priester atmospheric propagator function.

.. py:currentmodule:: HarrisPriester

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.atmosphere_data_filename`
              - Flux file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.atmosphere_data_source`
              - Get or set the atmospheric model data source - data file or constant values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.computes_pressure`
              - Flag indicates whether this model computes pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.computes_temperature`
              - Flag indicates whether this model computes temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.drag_model_plugin_name`
              - Get or set the name of the drag model plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.drag_model_type`
              - Drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.f_10_p7_avg`
              - Average solar Flux (F10.7); the 81-day averaged Ottawa 10.7 cm solar flux value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.n_plate_definition_file`
              - Drag N-Plate definition file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.sun_position`
              - Get or set the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester.variable_area_history_file`
              - Drag variable area history file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import HarrisPriester


Property detail
---------------

.. py:property:: atmosphere_data_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.atmosphere_data_filename
    :type: str

    Flux file.

.. py:property:: atmosphere_data_source
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.atmosphere_data_source
    :type: AtmosphereDataSource

    Get or set the atmospheric model data source - data file or constant values.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.drag_model_plugin
    :type: DragModelPlugin

    Drag model plugin properties.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.drag_model_plugin_name
    :type: str

    Get or set the name of the drag model plugin.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.drag_model_type
    :type: DragModelType

    Drag model type.

.. py:property:: f_10_p7_avg
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.f_10_p7_avg
    :type: float

    Average solar Flux (F10.7); the 81-day averaged Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.sun_position
    :type: SunPosition

    Get or set the sun position computation.

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.HarrisPriester.variable_area_history_file
    :type: str

    Drag variable area history file.


