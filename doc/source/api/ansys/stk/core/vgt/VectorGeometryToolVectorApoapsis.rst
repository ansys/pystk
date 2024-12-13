VectorGeometryToolVectorApoapsis
================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: VectorGeometryToolVectorApoapsis

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis.reference_point`
              - Specify a reference point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis.mean_element_type`
              - Specify the mean element theory type for approximating motion.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorApoapsis


Property detail
---------------

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis.mean_element_type
    :type: MeanElementTheory

    Specify the mean element theory type for approximating motion.


