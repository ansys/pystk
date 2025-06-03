VectorGeometryToolVectorProjectionAlongVector
=============================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjectionAlongVector

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`

   A projection of a source vector in the direction of another vector.

.. py:currentmodule:: VectorGeometryToolVectorProjectionAlongVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjectionAlongVector.source_vector`
              - A source vector. Can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjectionAlongVector.along_vector`
              - A vector along which the source vector is projected. Can be any VGT vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorProjectionAlongVector


Property detail
---------------

.. py:property:: source_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjectionAlongVector.source_vector
    :type: IVectorGeometryToolVector

    A source vector. Can be any VGT vector.

.. py:property:: along_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjectionAlongVector.along_vector
    :type: IVectorGeometryToolVector

    A vector along which the source vector is projected. Can be any VGT vector.


