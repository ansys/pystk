IGraphics3DAzElMask
===================

.. py:class:: IGraphics3DAzElMask

   object
   
   Use to display labels and adjust the translucency of the azimuth-elevation mask for a facility, place or target.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compass_directions_visible`
            * - :py:meth:`~altitude_labels_visible`
            * - :py:meth:`~numb_altitude_labels`
            * - :py:meth:`~interior_translucency`
            * - :py:meth:`~line_translucency`
            * - :py:meth:`~label_swap_distance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DAzElMask


Property detail
---------------

.. py:property:: compass_directions_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DAzElMask.compass_directions_visible
    :type: bool

    Display of compass directions on the outline of the mask.

.. py:property:: altitude_labels_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DAzElMask.altitude_labels_visible
    :type: bool

    Display of altitude labels.

.. py:property:: numb_altitude_labels
    :canonical: ansys.stk.core.stkobjects.IGraphics3DAzElMask.numb_altitude_labels
    :type: int

    The number of altitude labels to display on the outline of the mask.

.. py:property:: interior_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DAzElMask.interior_translucency
    :type: float

    The translucency of the mask, where 1 = completely invisible.

.. py:property:: line_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DAzElMask.line_translucency
    :type: float

    The translucency of the outline of the mask, where 1 = completely invisible.

.. py:property:: label_swap_distance
    :canonical: ansys.stk.core.stkobjects.IGraphics3DAzElMask.label_swap_distance
    :type: IAgVOLabelSwapDistance

    Interface to control the level of detail in labels and other screen objects at specified distances.


