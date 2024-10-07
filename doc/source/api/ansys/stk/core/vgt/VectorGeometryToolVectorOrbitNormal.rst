VectorGeometryToolVectorOrbitNormal
===================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

.. py:currentmodule:: VectorGeometryToolVectorOrbitNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal.reference_point`
              - Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal.mean_element_type`
              - Specify the mean element theory type for approximating motion.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorOrbitNormal


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal.reference_point
    :type: VectorGeometryToolPointReference

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal.mean_element_type
    :type: MEAN_ELEMENT_THEORY

    Specify the mean element theory type for approximating motion.


