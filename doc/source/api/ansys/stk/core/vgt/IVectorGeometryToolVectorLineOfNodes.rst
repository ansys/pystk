IVectorGeometryToolVectorLineOfNodes
====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorLineOfNodes

   object
   
   Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

.. py:currentmodule:: IVectorGeometryToolVectorLineOfNodes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLineOfNodes.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLineOfNodes.reference_point`
              - Specify a reference point.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorLineOfNodes


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLineOfNodes.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLineOfNodes.reference_point
    :type: IVectorGeometryToolPointRefTo

    Specify a reference point.


