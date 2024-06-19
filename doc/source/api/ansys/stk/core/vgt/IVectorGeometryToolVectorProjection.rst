IVectorGeometryToolVectorProjection
===================================

.. py:class:: IVectorGeometryToolVectorProjection

   object
   
   A projection of a vector computed with respect to a reference plane.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~source`
            * - :py:meth:`~reference_plane`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorProjection


Property detail
---------------

.. py:property:: source
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorProjection.source
    :type: IAgCrdnVectorRefTo

    Specify a source vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorProjection.reference_plane
    :type: IAgCrdnPlaneRefTo

    Specify a reference plane.


