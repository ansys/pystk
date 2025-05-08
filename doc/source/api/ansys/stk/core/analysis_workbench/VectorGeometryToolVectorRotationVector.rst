VectorGeometryToolVectorRotationVector
======================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

.. py:currentmodule:: VectorGeometryToolVectorRotationVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector.axes`
              - Specify the axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector.force_minimum_rotation`
              - Insures that the rotation angle will be between 0 and pi. If the angle is increasing at pi, then the axis direction will be negated to keep phi less than pi.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorRotationVector


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector.axes
    :type: VectorGeometryToolAxesReference

    Specify the axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: force_minimum_rotation
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector.force_minimum_rotation
    :type: bool

    Insures that the rotation angle will be between 0 and pi. If the angle is increasing at pi, then the axis direction will be negated to keep phi less than pi.


