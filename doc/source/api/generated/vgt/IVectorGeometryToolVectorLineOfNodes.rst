IVectorGeometryToolVectorLineOfNodes
====================================

.. py:class:: IVectorGeometryToolVectorLineOfNodes

   object
   
   Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~reference_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorLineOfNodes


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLineOfNodes.central_body
    :type: "IAgCrdnCentralBodyRefTo"

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLineOfNodes.reference_point
    :type: "IAgCrdnPointRefTo"

    Specify a reference point.


