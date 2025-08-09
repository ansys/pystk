VectorGeometryToolVectorEccentricity
====================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: VectorGeometryToolVectorEccentricity

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity.mean_element_type`
              - Specify the mean element theory type for approximating motion.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity.reference_point`
              - Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorEccentricity


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity.mean_element_type
    :type: MeanElementTheory

    Specify the mean element theory type for approximating motion.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity.reference_point
    :type: VectorGeometryToolPointReference

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.


