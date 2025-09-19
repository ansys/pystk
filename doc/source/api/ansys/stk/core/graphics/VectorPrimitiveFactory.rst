VectorPrimitiveFactory
======================

.. py:class:: ansys.stk.core.graphics.VectorPrimitiveFactory

   Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

.. py:currentmodule:: VectorPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.VectorPrimitiveFactory.initialize_with_direction`
              - Initialize a vector primitive with the specified reference frame as its source and pointing in direction dir.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import VectorPrimitiveFactory



Method detail
-------------

.. py:method:: initialize_with_direction(self, reference_frame: IVectorGeometryToolSystem, dir: IVectorGeometryToolVector, font: GraphicsFont) -> VectorPrimitive
    :canonical: ansys.stk.core.graphics.VectorPrimitiveFactory.initialize_with_direction

    Initialize a vector primitive with the specified reference frame as its source and pointing in direction dir.

    :Parameters:

        **reference_frame** : :obj:`~IVectorGeometryToolSystem`

        **dir** : :obj:`~IVectorGeometryToolVector`

        **font** : :obj:`~GraphicsFont`


    :Returns:

        :obj:`~VectorPrimitive`

