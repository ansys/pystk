IPolylinePrimitiveOptionalParametersFactory
===========================================

.. py:class:: IPolylinePrimitiveOptionalParametersFactory

   object
   
   Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize default polyline primitive optional parameters. All per-segment parameters are initially empty.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPolylinePrimitiveOptionalParametersFactory



Method detail
-------------

.. py:method:: initialize(self) -> IPolylinePrimitiveOptionalParameters
    :canonical: ansys.stk.core.graphics.IPolylinePrimitiveOptionalParametersFactory.initialize

    Initialize default polyline primitive optional parameters. All per-segment parameters are initially empty.

    :Returns:

        :obj:`~IPolylinePrimitiveOptionalParameters`

