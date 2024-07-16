VectorGeometryToolAngleBetweenPlanes
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleBetweenPlanes

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngle`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   An angle between two planes.

.. py:currentmodule:: VectorGeometryToolAngleBetweenPlanes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleBetweenPlanes.from_plane`
              - Specify the first of the two planes the angle is measured.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleBetweenPlanes.to_plane`
              - Specify the second of the two planes the angle is measured.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAngleBetweenPlanes


Property detail
---------------

.. py:property:: from_plane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleBetweenPlanes.from_plane
    :type: IVectorGeometryToolPlaneRefTo

    Specify the first of the two planes the angle is measured.

.. py:property:: to_plane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleBetweenPlanes.to_plane
    :type: IVectorGeometryToolPlaneRefTo

    Specify the second of the two planes the angle is measured.


