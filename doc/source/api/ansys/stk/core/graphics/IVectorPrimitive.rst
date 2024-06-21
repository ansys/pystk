IVectorPrimitive
================

.. py:class:: ansys.stk.core.graphics.IVectorPrimitive

   object
   
   Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

.. py:currentmodule:: IVectorPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.lighting`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.label`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.display_label`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.display_magnitude`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.display_ra_dec`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.display_trace`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.display_sweep`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.display_lines`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.persistence_width`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.fade_persistence`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.persistence_duration`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.length`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.width`
            * - :py:attr:`~ansys.stk.core.graphics.IVectorPrimitive.true_scale`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IVectorPrimitive


Property detail
---------------

.. py:property:: lighting
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.lighting
    :type: bool

    Gets or sets whether the primitive is lit.

.. py:property:: label
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.label
    :type: str

    Gets or sets the user-defined label.

.. py:property:: display_label
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.display_label
    :type: bool

    Gets or sets whether the vector's label is displayed.

.. py:property:: display_magnitude
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.display_magnitude
    :type: bool

    Gets or sets whether the vector's magnitude is displayed.

.. py:property:: display_ra_dec
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.display_ra_dec
    :type: bool

    Gets or sets whether the vector's RA-Dec is displayed.

.. py:property:: display_trace
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.display_trace
    :type: bool

    Gets or sets whether the persistence trace (points) is displayed.

.. py:property:: display_sweep
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.display_sweep
    :type: bool

    Gets or sets whether the persistence sweep (triangles) is displayed.

.. py:property:: display_lines
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.display_lines
    :type: bool

    Gets or sets whether persistence lines are displayed.

.. py:property:: persistence_width
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.persistence_width
    :type: float

    Gets or sets persistence point/line width.

.. py:property:: fade_persistence
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.fade_persistence
    :type: bool

    Gets or sets whether the persistence path should fade over time.

.. py:property:: persistence_duration
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.persistence_duration
    :type: float

    Gets or sets the maximum duration of the persistence path.

.. py:property:: length
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.length
    :type: float

    Gets or sets the vector's source-to-arrow-tip length.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.width
    :type: float

    Gets or sets the vector's width in pixels. As the camera distances changes from this primitive, the geometry will autoscale to maintain this thickness.

.. py:property:: true_scale
    :canonical: ansys.stk.core.graphics.IVectorPrimitive.true_scale
    :type: bool

    Gets or sets whether vector's 'true scale' length (based on how the primitive was created) should be used.


