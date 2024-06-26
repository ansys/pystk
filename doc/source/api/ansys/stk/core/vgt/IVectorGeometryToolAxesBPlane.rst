IVectorGeometryToolAxesBPlane
=============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane

   object
   
   B-Plane axes using the selected target body and reference vector.

.. py:currentmodule:: IVectorGeometryToolAxesBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.trajectory`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.target_body`
              - Specify a target central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.direction`
              - Specify a direction (incoming or outgoing).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesBPlane


Property detail
---------------

.. py:property:: trajectory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.trajectory
    :type: IVectorGeometryToolPointRefTo

    Specify a trajectory point.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.reference_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a reference vector.

.. py:property:: target_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.target_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a target central body.

.. py:property:: direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.direction
    :type: CRDN_DIRECTION_TYPE

    Specify a direction (incoming or outgoing).


