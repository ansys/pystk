IAxesPrimitive
==============

.. py:class:: ansys.stk.core.graphics.IAxesPrimitive

   object
   
   Render an axes in the 3D scene.

.. py:currentmodule:: IAxesPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.lighting`
              - Gets or sets whether the primitive is lit.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.label`
              - Gets or sets the axes label.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.display_label`
              - Gets or sets whether the axes' label is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.display_trace`
              - Gets or sets whether the persistence trace (points) is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.display_sweep`
              - Gets or sets whether the persistence sweep (triangles) is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.display_lines`
              - Gets or sets whether persistence lines are displayed.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.persistence_width`
              - Gets or sets persistence point/line width.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.fade_persistence`
              - Gets or sets whether the persistence path should fade over time.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.persistence_duration`
              - Gets or sets the maximum duration of the persistence path.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.length`
              - Gets or sets the axes' source-to-arrow-tip length.
            * - :py:attr:`~ansys.stk.core.graphics.IAxesPrimitive.width`
              - Gets or sets the width in pixels. As the camera distances changes from this primitive, the geometry will autoscale to maintain this thickness.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IAxesPrimitive


Property detail
---------------

.. py:property:: lighting
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.lighting
    :type: bool

    Gets or sets whether the primitive is lit.

.. py:property:: label
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.label
    :type: str

    Gets or sets the axes label.

.. py:property:: display_label
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.display_label
    :type: bool

    Gets or sets whether the axes' label is displayed.

.. py:property:: display_trace
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.display_trace
    :type: bool

    Gets or sets whether the persistence trace (points) is displayed.

.. py:property:: display_sweep
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.display_sweep
    :type: bool

    Gets or sets whether the persistence sweep (triangles) is displayed.

.. py:property:: display_lines
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.display_lines
    :type: bool

    Gets or sets whether persistence lines are displayed.

.. py:property:: persistence_width
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.persistence_width
    :type: float

    Gets or sets persistence point/line width.

.. py:property:: fade_persistence
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.fade_persistence
    :type: bool

    Gets or sets whether the persistence path should fade over time.

.. py:property:: persistence_duration
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.persistence_duration
    :type: float

    Gets or sets the maximum duration of the persistence path.

.. py:property:: length
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.length
    :type: float

    Gets or sets the axes' source-to-arrow-tip length.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.IAxesPrimitive.width
    :type: float

    Gets or sets the width in pixels. As the camera distances changes from this primitive, the geometry will autoscale to maintain this thickness.


