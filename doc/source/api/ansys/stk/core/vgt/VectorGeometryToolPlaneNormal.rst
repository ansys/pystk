VectorGeometryToolPlaneNormal
=============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPlaneNormal

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A plane normal to a vector at a given point.

.. py:currentmodule:: VectorGeometryToolPlaneNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneNormal.normal_vector`
              - Specify a Normal vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneNormal.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneNormal.reference_point`
              - Specify a reference point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPlaneNormal


Property detail
---------------

.. py:property:: normal_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneNormal.normal_vector
    :type: VectorGeometryToolVectorRefTo

    Specify a Normal vector.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneNormal.reference_vector
    :type: VectorGeometryToolVectorRefTo

    Specify a reference vector.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneNormal.reference_point
    :type: VectorGeometryToolPointRefTo

    Specify a reference point.


