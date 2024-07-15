VectorGeometryToolVectorProjectAlongVector
==========================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorProjectAlongVector

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`

   A projection of a source vector in the direction of another vector.

.. py:currentmodule:: VectorGeometryToolVectorProjectAlongVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorProjectAlongVector.source_vector`
              - A source vector. Can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorProjectAlongVector.along_vector`
              - A vector along which the source vector is projected. Can be any VGT vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorProjectAlongVector


Property detail
---------------

.. py:property:: source_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorProjectAlongVector.source_vector
    :type: IVectorGeometryToolVector

    A source vector. Can be any VGT vector.

.. py:property:: along_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorProjectAlongVector.along_vector
    :type: IVectorGeometryToolVector

    A vector along which the source vector is projected. Can be any VGT vector.


