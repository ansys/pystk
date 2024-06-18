IVectorPrimitiveFactory
=======================

.. py:class:: IVectorPrimitiveFactory

   object
   
   Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize_with_direction`
              - Initialize a vector primitive with the specified reference frame as its source and pointing in direction dir.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IVectorPrimitiveFactory



Method detail
-------------

.. py:method:: initialize_with_direction(self, referenceFrame:"IVectorGeometryToolSystem", dir:"IVectorGeometryToolVector", font:"IGraphicsFont") -> "IVectorPrimitive"

    Initialize a vector primitive with the specified reference frame as its source and pointing in direction dir.

    :Parameters:

    **referenceFrame** : :obj:`~"IVectorGeometryToolSystem"`
    **dir** : :obj:`~"IVectorGeometryToolVector"`
    **font** : :obj:`~"IGraphicsFont"`

    :Returns:

        :obj:`~"IVectorPrimitive"`

