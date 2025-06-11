VectorGeometryToolVectorOrbitAngularMomentum
============================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

.. py:currentmodule:: VectorGeometryToolVectorOrbitAngularMomentum

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum.reference_point`
              - Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum.mean_element_type`
              - Specify the mean element theory type for approximating motion.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        VectorGeometryToolVectorOrbitAngularMomentum,
    )


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum.reference_point
    :type: VectorGeometryToolPointReference

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum.mean_element_type
    :type: MeanElementTheory

    Specify the mean element theory type for approximating motion.


