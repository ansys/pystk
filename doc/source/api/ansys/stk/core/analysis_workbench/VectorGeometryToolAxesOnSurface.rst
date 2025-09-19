VectorGeometryToolAxesOnSurface
===============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Topocentric axes located at the reference point's projection on the central body.

.. py:currentmodule:: VectorGeometryToolAxesOnSurface

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface.reference_point`
              - Specify a reference point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface.use_mean_sea_level`
              - Specify whether the reference shape is at the Mean Sea Level.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.

.. py:property:: use_mean_sea_level
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface.use_mean_sea_level
    :type: bool

    Specify whether the reference shape is at the Mean Sea Level.


