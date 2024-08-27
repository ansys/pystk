US_Standard_Atmosphere
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   US_Standard_Atmosphere atmospheric propagator function.

.. py:currentmodule:: US_Standard_Atmosphere

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.computes_temperature`
              - Flag indicates whether this model computes temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.computes_pressure`
              - Flag indicates whether this model computes pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.drag_model_type`
              - Drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.drag_model_plugin_name`
              - Gets or sets the name of the drag model plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.n_plate_definition_file`
              - Drag N-Plate definition file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import US_Standard_Atmosphere


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.drag_model_type
    :type: DRAG_MODEL_TYPE

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.drag_model_plugin
    :type: DragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


