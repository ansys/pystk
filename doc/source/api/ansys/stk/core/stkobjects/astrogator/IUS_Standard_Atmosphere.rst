IUS_Standard_Atmosphere
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere

   object
   
   Properties for the US Standard Atmosphere atmospheric model.

.. py:currentmodule:: IUS_Standard_Atmosphere

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.use_approximate_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.computes_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.computes_pressure`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.drag_model_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.drag_model_plugin_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.drag_model_plugin`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.variable_area_history_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.n_plate_definition_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IUS_Standard_Atmosphere


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.drag_model_type
    :type: DRAG_MODEL_TYPE

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.drag_model_plugin
    :type: IDragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


