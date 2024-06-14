IJacchia_1960
=============

.. py:class:: IJacchia_1960

   object
   
   Properties for the Jacchia 1960 atmospheric model - an outdated atmospheric model provided for making comparisons with other software.

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
            * - :py:meth:`~drag_model_type`
            * - :py:meth:`~drag_model_plugin_name`
            * - :py:meth:`~drag_model_plugin`
            * - :py:meth:`~variable_area_history_file`
            * - :py:meth:`~n_plate_definition_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IJacchia_1960


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: computes_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: computes_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.sun_position
    :type: "SUN_POSITION"

    Gets or sets the sun position computation.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.drag_model_type
    :type: "DRAG_MODEL_TYPE"

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.drag_model_plugin
    :type: "IAgVADragModelPlugin"

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IJacchia_1960.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


