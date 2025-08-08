VectorGeometryToolVectorScaled
==============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

.. py:currentmodule:: VectorGeometryToolVectorScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled.is_normalized`
              - Control whether to convert the reference vector to a unit vector before scalling.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled.reference_vector`
              - A vector being scaled.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled.scale`
              - A scaling multiple.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorScaled


Property detail
---------------

.. py:property:: is_normalized
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled.is_normalized
    :type: bool

    Control whether to convert the reference vector to a unit vector before scalling.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled.reference_vector
    :type: VectorGeometryToolVectorReference

    A vector being scaled.

.. py:property:: scale
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled.scale
    :type: float

    A scaling multiple.


