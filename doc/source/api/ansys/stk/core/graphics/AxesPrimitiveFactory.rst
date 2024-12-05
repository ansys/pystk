AxesPrimitiveFactory
====================

.. py:class:: ansys.stk.core.graphics.AxesPrimitiveFactory

   Render an axes in the 3D scene.

.. py:currentmodule:: AxesPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.AxesPrimitiveFactory.initialize_with_direction`
              - Initialize an axes primitive with the specified reference frame as its source.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import AxesPrimitiveFactory



Method detail
-------------

.. py:method:: initialize_with_direction(self, reference_frame: IVectorGeometryToolSystem, axes: IVectorGeometryToolAxes, font: GraphicsFont) -> AxesPrimitive
    :canonical: ansys.stk.core.graphics.AxesPrimitiveFactory.initialize_with_direction

    Initialize an axes primitive with the specified reference frame as its source.

    :Parameters:

    **reference_frame** : :obj:`~IVectorGeometryToolSystem`
    **axes** : :obj:`~IVectorGeometryToolAxes`
    **font** : :obj:`~GraphicsFont`

    :Returns:

        :obj:`~AxesPrimitive`

