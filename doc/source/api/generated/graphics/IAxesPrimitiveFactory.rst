IAxesPrimitiveFactory
=====================

.. py:class:: IAxesPrimitiveFactory

   object
   
   Render an axes in the 3D scene.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize_with_direction`
              - Initialize an axes primitive with the specified reference frame as its source.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IAxesPrimitiveFactory



Method detail
-------------

.. py:method:: initialize_with_direction(self, referenceFrame:"IVectorGeometryToolSystem", axes:"IVectorGeometryToolAxes", font:"IGraphicsFont") -> "IAxesPrimitive"

    Initialize an axes primitive with the specified reference frame as its source.

    :Parameters:

    **referenceFrame** : :obj:`~"IVectorGeometryToolSystem"`
    **axes** : :obj:`~"IVectorGeometryToolAxes"`
    **font** : :obj:`~"IGraphicsFont"`

    :Returns:

        :obj:`~"IAxesPrimitive"`

