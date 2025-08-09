Graphics3DAzElMask
==================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DAzElMask

   Class to define display labels and adjust the translucency of the 3D azimuth-elevation mask for a facility, place or target.

.. py:currentmodule:: Graphics3DAzElMask

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DAzElMask.show_compass_directions`
              - Display of compass directions on the outline of the mask.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DAzElMask.altitude_labels_visible`
              - Display of altitude labels.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DAzElMask.number_of_altitude_labels`
              - The number of altitude labels to display on the outline of the mask.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DAzElMask.interior_translucency`
              - The translucency of the mask, where 1 = completely invisible.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DAzElMask.line_translucency`
              - The translucency of the outline of the mask, where 1 = completely invisible.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DAzElMask.label_swap_distance`
              - Interface to control the level of detail in labels and other screen objects at specified distances.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DAzElMask


Property detail
---------------

.. py:property:: show_compass_directions
    :canonical: ansys.stk.core.stkobjects.Graphics3DAzElMask.show_compass_directions
    :type: bool

    Display of compass directions on the outline of the mask.

.. py:property:: altitude_labels_visible
    :canonical: ansys.stk.core.stkobjects.Graphics3DAzElMask.altitude_labels_visible
    :type: bool

    Display of altitude labels.

.. py:property:: number_of_altitude_labels
    :canonical: ansys.stk.core.stkobjects.Graphics3DAzElMask.number_of_altitude_labels
    :type: int

    The number of altitude labels to display on the outline of the mask.

.. py:property:: interior_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DAzElMask.interior_translucency
    :type: float

    The translucency of the mask, where 1 = completely invisible.

.. py:property:: line_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DAzElMask.line_translucency
    :type: float

    The translucency of the outline of the mask, where 1 = completely invisible.

.. py:property:: label_swap_distance
    :canonical: ansys.stk.core.stkobjects.Graphics3DAzElMask.label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Interface to control the level of detail in labels and other screen objects at specified distances.


