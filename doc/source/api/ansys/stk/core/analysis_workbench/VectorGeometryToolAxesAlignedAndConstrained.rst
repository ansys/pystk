VectorGeometryToolAxesAlignedAndConstrained
===========================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

.. py:currentmodule:: VectorGeometryToolAxesAlignedAndConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_reference_vector`
              - Specify an alignment reference vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_reference_vector`
              - Specify a constraint reference vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_direction`
              - Specify a desired alignment direction and the applicable parameters.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_direction`
              - Specify a desired constraint direction and the applicable parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        VectorGeometryToolAxesAlignedAndConstrained,
    )


Property detail
---------------

.. py:property:: alignment_reference_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_reference_vector
    :type: VectorGeometryToolVectorReference

    Specify an alignment reference vector.

.. py:property:: constraint_reference_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a constraint reference vector.

.. py:property:: alignment_direction
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_direction
    :type: IDirection

    Specify a desired alignment direction and the applicable parameters.

.. py:property:: constraint_direction
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_direction
    :type: IDirection

    Specify a desired constraint direction and the applicable parameters.


