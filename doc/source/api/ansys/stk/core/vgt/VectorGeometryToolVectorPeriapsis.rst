VectorGeometryToolVectorPeriapsis
=================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: VectorGeometryToolVectorPeriapsis

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis.reference_point`
              - Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis.mean_element_type`
              - Specify the mean element theory type for approximating motion.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorPeriapsis


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis.reference_point
    :type: VectorGeometryToolPointReference

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis.mean_element_type
    :type: MEAN_ELEMENT_THEORY

    Specify the mean element theory type for approximating motion.


