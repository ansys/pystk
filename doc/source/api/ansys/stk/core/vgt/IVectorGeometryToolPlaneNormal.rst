IVectorGeometryToolPlaneNormal
==============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal

   object
   
   A plane normal to a vector at a given point.

.. py:currentmodule:: IVectorGeometryToolPlaneNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.normal_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.reference_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.reference_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneNormal


Property detail
---------------

.. py:property:: normal_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.normal_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a Normal vector.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.reference_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a reference vector.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.reference_point
    :type: IVectorGeometryToolPointRefTo

    Specify a reference point.


