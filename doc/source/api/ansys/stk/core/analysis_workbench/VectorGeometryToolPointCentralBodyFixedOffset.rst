VectorGeometryToolPointCentralBodyFixedOffset
=============================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`

   Point specified by fixed components with respect to central body.

.. py:currentmodule:: VectorGeometryToolPointCentralBodyFixedOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset.central_body`
              - Get the central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset.reference_shape`
              - Choose the point height's reference. Available options are central body ellipsoid (WSG84), terrain or Mean Sea Level.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset.position`
              - A position of the point fixed on the central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        VectorGeometryToolPointCentralBodyFixedOffset,
    )


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset.central_body
    :type: str

    Get the central body.

.. py:property:: reference_shape
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset.reference_shape
    :type: SurfaceReferenceShapeType

    Choose the point height's reference. Available options are central body ellipsoid (WSG84), terrain or Mean Sea Level.

.. py:property:: position
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset.position
    :type: IPosition

    A position of the point fixed on the central body.


