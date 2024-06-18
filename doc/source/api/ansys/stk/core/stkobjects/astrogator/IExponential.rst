IExponential
============

.. py:class:: IExponential

   object
   
   Properties for the Exponential atmospheric model - a model that calculates atmospheric density using an equation involving a reference density, reference altitude, and scale altitude.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_approximate_altitude`
            * - :py:meth:`~reference_density`
            * - :py:meth:`~reference_altitude`
            * - :py:meth:`~scale_altitude`
            * - :py:meth:`~drag_model_type`
            * - :py:meth:`~drag_model_plugin_name`
            * - :py:meth:`~drag_model_plugin`
            * - :py:meth:`~variable_area_history_file`
            * - :py:meth:`~n_plate_definition_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IExponential


Property detail
---------------

.. py:property:: use_approximate_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: reference_density
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.reference_density
    :type: float

    Gets or sets the reference density. Uses Density Dimension.

.. py:property:: reference_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.reference_altitude
    :type: float

    Gets or sets the reference altitude. Uses Distance Dimension.

.. py:property:: scale_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.scale_altitude
    :type: float

    Gets or sets the scale altitude. Uses Distance Dimension.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.drag_model_type
    :type: "DRAG_MODEL_TYPE"

    Drag model type.

.. py:property:: drag_model_plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.drag_model_plugin_name
    :type: str

    Gets or sets the name of the drag model plugin.

.. py:property:: drag_model_plugin
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.drag_model_plugin
    :type: "IAgVADragModelPlugin"

    Drag model plugin properties.

.. py:property:: variable_area_history_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IExponential.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.


