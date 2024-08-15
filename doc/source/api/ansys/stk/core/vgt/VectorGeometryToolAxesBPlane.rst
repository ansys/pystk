VectorGeometryToolAxesBPlane
============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesBPlane

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   B-Plane axes using the selected target body and reference vector.

.. py:currentmodule:: VectorGeometryToolAxesBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.trajectory`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.target_body`
              - Specify a target central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.direction`
              - Specify a direction (incoming or outgoing).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesBPlane


Property detail
---------------

.. py:property:: trajectory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.trajectory
    :type: VectorGeometryToolPointRefTo

    Specify a trajectory point.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.reference_vector
    :type: VectorGeometryToolVectorRefTo

    Specify a reference vector.

.. py:property:: target_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.target_body
    :type: AnalysisWorkbenchCentralBodyRefTo

    Specify a target central body.

.. py:property:: direction
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesBPlane.direction
    :type: CRDN_DIRECTION_TYPE

    Specify a direction (incoming or outgoing).


