PointBatchPrimitiveFactory
==========================

.. py:class:: ansys.stk.core.graphics.PointBatchPrimitiveFactory

   Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

.. py:currentmodule:: PointBatchPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitiveFactory.initialize`
              - Initialize a default point batch primitive. This is equivalent to constructing a point batch with a set hint of Frequent.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitiveFactory.initialize_with_set_hint`
              - Initialize a new instance of a point batch primitive with the specified set hint.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitiveFactory.minimum_pixel_size_supported`
              - Gets the minimum pixel size supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitiveFactory.maximum_pixel_size_supported`
              - Gets the maximum pixel size supported by the video card.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PointBatchPrimitiveFactory


Property detail
---------------

.. py:property:: minimum_pixel_size_supported
    :canonical: ansys.stk.core.graphics.PointBatchPrimitiveFactory.minimum_pixel_size_supported
    :type: float

    Gets the minimum pixel size supported by the video card.

.. py:property:: maximum_pixel_size_supported
    :canonical: ansys.stk.core.graphics.PointBatchPrimitiveFactory.maximum_pixel_size_supported
    :type: float

    Gets the maximum pixel size supported by the video card.


Method detail
-------------

.. py:method:: initialize(self) -> PointBatchPrimitive
    :canonical: ansys.stk.core.graphics.PointBatchPrimitiveFactory.initialize

    Initialize a default point batch primitive. This is equivalent to constructing a point batch with a set hint of Frequent.

    :Returns:

        :obj:`~PointBatchPrimitive`

.. py:method:: initialize_with_set_hint(self, set_hint: SET_HINT) -> PointBatchPrimitive
    :canonical: ansys.stk.core.graphics.PointBatchPrimitiveFactory.initialize_with_set_hint

    Initialize a new instance of a point batch primitive with the specified set hint.

    :Parameters:

    **set_hint** : :obj:`~SET_HINT`

    :Returns:

        :obj:`~PointBatchPrimitive`



