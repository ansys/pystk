Exponential
===========

.. py:class:: ansys.stk.core.stkobjects.astrogator.Exponential

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Exponential atmospheric propagator function.

.. py:currentmodule:: Exponential

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.reference_density`
              - Get or set the reference density. Uses Density Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.reference_altitude`
              - Get or set the reference altitude. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.scale_altitude`
              - Get or set the scale altitude. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.drag_model_type`
              - Drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.drag_model_plugin_name`
              - Get or set the name of the drag model plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Exponential.n_plate_definition_file`
              - Drag N-Plate definition file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import Exponential


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: reference_density
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.reference_density
    :type: float

    Get or set the reference density. Uses Density Dimension.

.. py:property:: reference_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.reference_altitude
    :type: float

    Get or set the reference altitude. Uses Distance Dimension.

.. py:property:: scale_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.scale_altitude
    :type: float

    Get or set the scale altitude. Uses Distance Dimension.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.drag_model_type
    :type: DragModelType

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.drag_model_plugin_name
    :type: str

    Get or set the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.drag_model_plugin
    :type: DragModelPlugin

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.Exponential.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


