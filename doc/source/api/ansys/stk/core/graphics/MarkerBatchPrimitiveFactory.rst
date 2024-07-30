MarkerBatchPrimitiveFactory
===========================

.. py:class:: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory

   Bases: 

   Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

.. py:currentmodule:: MarkerBatchPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize`
              - Initialize a default marker batch primitive...
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_with_set_hint`
              - Initialize a marker batch primitive with the specified setHint...
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_with_size_source`
              - Initialize a marker batch primitive with the specified sizeSource...
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_with_size_source_and_sort_order`
              - Initialize a marker batch primitive with the specified sizeSource and sortOrder...
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_size_source_sort_order_and_set_hint`
              - Initialize a marker batch primitive with the specified sizeSource, sortOrder, and setHint. This is equivalent to constructing a marker batch with the specified arguments and a marker batch rendering method of Automatic.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_size_source_sort_order_set_hint_and_rendering_method`
              - Initialize a marker batch primitive with the specified arguments.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.supported`
              - Determine whether or not the video card supports the marker batch primitive with the given renderingMethod.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MarkerBatchPrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> MarkerBatchPrimitive
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize

    Initialize a default marker batch primitive...

    :Returns:

        :obj:`~MarkerBatchPrimitive`

.. py:method:: initialize_with_set_hint(self, setHint: SET_HINT) -> MarkerBatchPrimitive
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_with_set_hint

    Initialize a marker batch primitive with the specified setHint...

    :Parameters:

    **setHint** : :obj:`~SET_HINT`

    :Returns:

        :obj:`~MarkerBatchPrimitive`

.. py:method:: initialize_with_size_source(self, sizeSource: MARKER_BATCH_SIZE_SOURCE) -> MarkerBatchPrimitive
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_with_size_source

    Initialize a marker batch primitive with the specified sizeSource...

    :Parameters:

    **sizeSource** : :obj:`~MARKER_BATCH_SIZE_SOURCE`

    :Returns:

        :obj:`~MarkerBatchPrimitive`

.. py:method:: initialize_with_size_source_and_sort_order(self, sizeSource: MARKER_BATCH_SIZE_SOURCE, sortOrder: MARKER_BATCH_SORT_ORDER) -> MarkerBatchPrimitive
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_with_size_source_and_sort_order

    Initialize a marker batch primitive with the specified sizeSource and sortOrder...

    :Parameters:

    **sizeSource** : :obj:`~MARKER_BATCH_SIZE_SOURCE`
    **sortOrder** : :obj:`~MARKER_BATCH_SORT_ORDER`

    :Returns:

        :obj:`~MarkerBatchPrimitive`

.. py:method:: initialize_size_source_sort_order_and_set_hint(self, sizeSource: MARKER_BATCH_SIZE_SOURCE, sortOrder: MARKER_BATCH_SORT_ORDER, setHint: SET_HINT) -> MarkerBatchPrimitive
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_size_source_sort_order_and_set_hint

    Initialize a marker batch primitive with the specified sizeSource, sortOrder, and setHint. This is equivalent to constructing a marker batch with the specified arguments and a marker batch rendering method of Automatic.

    :Parameters:

    **sizeSource** : :obj:`~MARKER_BATCH_SIZE_SOURCE`
    **sortOrder** : :obj:`~MARKER_BATCH_SORT_ORDER`
    **setHint** : :obj:`~SET_HINT`

    :Returns:

        :obj:`~MarkerBatchPrimitive`

.. py:method:: initialize_size_source_sort_order_set_hint_and_rendering_method(self, sizeSource: MARKER_BATCH_SIZE_SOURCE, sortOrder: MARKER_BATCH_SORT_ORDER, setHint: SET_HINT, renderingMethod: MARKER_BATCH_RENDERING_METHOD) -> MarkerBatchPrimitive
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.initialize_size_source_sort_order_set_hint_and_rendering_method

    Initialize a marker batch primitive with the specified arguments.

    :Parameters:

    **sizeSource** : :obj:`~MARKER_BATCH_SIZE_SOURCE`
    **sortOrder** : :obj:`~MARKER_BATCH_SORT_ORDER`
    **setHint** : :obj:`~SET_HINT`
    **renderingMethod** : :obj:`~MARKER_BATCH_RENDERING_METHOD`

    :Returns:

        :obj:`~MarkerBatchPrimitive`

.. py:method:: supported(self, renderingMethod: MARKER_BATCH_RENDERING_METHOD) -> bool
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitiveFactory.supported

    Determine whether or not the video card supports the marker batch primitive with the given renderingMethod.

    :Parameters:

    **renderingMethod** : :obj:`~MARKER_BATCH_RENDERING_METHOD`

    :Returns:

        :obj:`~bool`

