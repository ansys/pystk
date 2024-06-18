IVectorGeometryToolAxesBPlane
=============================

.. py:class:: IVectorGeometryToolAxesBPlane

   object
   
   B-Plane axes using the selected target body and reference vector.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~trajectory`
            * - :py:meth:`~reference_vector`
            * - :py:meth:`~target_body`
            * - :py:meth:`~direction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesBPlane


Property detail
---------------

.. py:property:: trajectory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.trajectory
    :type: "IAgCrdnPointRefTo"

    Specify a trajectory point.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.reference_vector
    :type: "IAgCrdnVectorRefTo"

    Specify a reference vector.

.. py:property:: target_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.target_body
    :type: "IAgCrdnCentralBodyRefTo"

    Specify a target central body.

.. py:property:: direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesBPlane.direction
    :type: "CRDN_DIRECTION_TYPE"

    Specify a direction (incoming or outgoing).


