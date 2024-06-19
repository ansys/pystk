IVectorGeometryToolAngleBetweenPlanes
=====================================

.. py:class:: IVectorGeometryToolAngleBetweenPlanes

   object
   
   An angle between two planes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~from_plane`
            * - :py:meth:`~to_plane`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleBetweenPlanes


Property detail
---------------

.. py:property:: from_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleBetweenPlanes.from_plane
    :type: IAgCrdnPlaneRefTo

    Specify the first of the two planes the angle is measured.

.. py:property:: to_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleBetweenPlanes.to_plane
    :type: IAgCrdnPlaneRefTo

    Specify the second of the two planes the angle is measured.


