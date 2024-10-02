VectorGeometryToolVectorLineOfNodes
===================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorLineOfNodes

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

.. py:currentmodule:: VectorGeometryToolVectorLineOfNodes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorLineOfNodes.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorLineOfNodes.reference_point`
              - Specify a reference point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorLineOfNodes


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorLineOfNodes.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorLineOfNodes.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.


