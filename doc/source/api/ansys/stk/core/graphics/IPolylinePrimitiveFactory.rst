IPolylinePrimitiveFactory
=========================

.. py:class:: IPolylinePrimitiveFactory

   object
   
   Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default polyline primitive. This is equivalent to constructing a polyline with a set hint of Frequent and a polyline type of LineStrip.
            * - :py:meth:`~initialize_with_interpolator_and_set_hint`
              - Initialize a polyline primitive with the specified interpolator and setHint.
            * - :py:meth:`~initialize_with_type_and_hint`
              - Initialize a new instance of a polyline primitive with the specified polylineType and setHint.
            * - :py:meth:`~initialize_with_interpolator`
              - Initialize a polyline primitive with the specified interpolator. This is equivalent to constructing a polyline with the specified interpolator and a set hint of Frequent.
            * - :py:meth:`~initialize_with_hint`
              - Initialize a new instance of a polyline primitive with the specified set hint. This is equivalent to constructing a polyline with a polyline type of LineStrip and the specified set hint.
            * - :py:meth:`~initialize_with_type`
              - Initialize a polyline primitive with the specified polylineType. This is equivalent to constructing a polyline with the specified polylineType and a set hint of Frequent.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~minimum_width_supported`
            * - :py:meth:`~maximum_width_supported`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPolylinePrimitiveFactory


Property detail
---------------

.. py:property:: minimum_width_supported
    :canonical: ansys.stk.core.graphics.IPolylinePrimitiveFactory.minimum_width_supported
    :type: float

    Gets the minimum width, in pixels, supported by the video card.

.. py:property:: maximum_width_supported
    :canonical: ansys.stk.core.graphics.IPolylinePrimitiveFactory.maximum_width_supported
    :type: float

    Gets the maximum width, in pixels, supported by the video card.


Method detail
-------------

.. py:method:: initialize(self) -> "IPolylinePrimitive"

    Initialize a default polyline primitive. This is equivalent to constructing a polyline with a set hint of Frequent and a polyline type of LineStrip.

    :Returns:

        :obj:`~"IPolylinePrimitive"`

.. py:method:: initialize_with_interpolator_and_set_hint(self, interpolator:"IPositionInterpolator", setHint:"SET_HINT") -> "IPolylinePrimitive"

    Initialize a polyline primitive with the specified interpolator and setHint.

    :Parameters:

    **interpolator** : :obj:`~"IPositionInterpolator"`
    **setHint** : :obj:`~"SET_HINT"`

    :Returns:

        :obj:`~"IPolylinePrimitive"`

.. py:method:: initialize_with_type_and_hint(self, polylineType:"POLYLINE_TYPE", setHint:"SET_HINT") -> "IPolylinePrimitive"

    Initialize a new instance of a polyline primitive with the specified polylineType and setHint.

    :Parameters:

    **polylineType** : :obj:`~"POLYLINE_TYPE"`
    **setHint** : :obj:`~"SET_HINT"`

    :Returns:

        :obj:`~"IPolylinePrimitive"`

.. py:method:: initialize_with_interpolator(self, interpolator:"IPositionInterpolator") -> "IPolylinePrimitive"

    Initialize a polyline primitive with the specified interpolator. This is equivalent to constructing a polyline with the specified interpolator and a set hint of Frequent.

    :Parameters:

    **interpolator** : :obj:`~"IPositionInterpolator"`

    :Returns:

        :obj:`~"IPolylinePrimitive"`

.. py:method:: initialize_with_hint(self, setHint:"SET_HINT") -> "IPolylinePrimitive"

    Initialize a new instance of a polyline primitive with the specified set hint. This is equivalent to constructing a polyline with a polyline type of LineStrip and the specified set hint.

    :Parameters:

    **setHint** : :obj:`~"SET_HINT"`

    :Returns:

        :obj:`~"IPolylinePrimitive"`

.. py:method:: initialize_with_type(self, polylineType:"POLYLINE_TYPE") -> "IPolylinePrimitive"

    Initialize a polyline primitive with the specified polylineType. This is equivalent to constructing a polyline with the specified polylineType and a set hint of Frequent.

    :Parameters:

    **polylineType** : :obj:`~"POLYLINE_TYPE"`

    :Returns:

        :obj:`~"IPolylinePrimitive"`



