VectorGeometryToolPointGlint
============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Point on central body surface that reflects from source to observer.

.. py:currentmodule:: VectorGeometryToolPointGlint

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint.observer_point`
              - Specify an observer point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint.source_point`
              - Specify a source point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointGlint


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: observer_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint.observer_point
    :type: VectorGeometryToolPointReference

    Specify an observer point.

.. py:property:: source_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint.source_point
    :type: VectorGeometryToolPointReference

    Specify a source point.


