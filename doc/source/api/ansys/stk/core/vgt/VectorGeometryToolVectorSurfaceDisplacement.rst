VectorGeometryToolVectorSurfaceDisplacement
===========================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`

   Displacement between origin and destination points using surface distance and altitude difference.

.. py:currentmodule:: VectorGeometryToolVectorSurfaceDisplacement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.origin_point`
              - An origin point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.destination_point`
              - Destination point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.surface_central_body`
              - Get or set the surface central body property.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.differencing_time_step`
              - Time step used in displacement on surface vector. (derivatives using central differencing).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorSurfaceDisplacement


Property detail
---------------

.. py:property:: origin_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.origin_point
    :type: IVectorGeometryToolPoint

    An origin point.

.. py:property:: destination_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.destination_point
    :type: IVectorGeometryToolPoint

    Destination point.

.. py:property:: surface_central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.surface_central_body
    :type: str

    Get or set the surface central body property.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement.differencing_time_step
    :type: float

    Time step used in displacement on surface vector. (derivatives using central differencing).


