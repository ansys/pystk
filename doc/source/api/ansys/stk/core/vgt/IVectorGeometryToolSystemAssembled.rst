IVectorGeometryToolSystemAssembled
==================================

.. py:class:: IVectorGeometryToolSystemAssembled

   object
   
   A system assembled from an origin point and a set of reference axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~origin_point`
            * - :py:meth:`~reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemAssembled


Property detail
---------------

.. py:property:: origin_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemAssembled.origin_point
    :type: IAgCrdnPointRefTo

    Specify a point of origin.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemAssembled.reference_axes
    :type: IAgCrdnAxesRefTo

    Specify a reference axes.


