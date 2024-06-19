IVectorGeometryToolPlaneNormal
==============================

.. py:class:: IVectorGeometryToolPlaneNormal

   object
   
   A plane normal to a vector at a given point.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~normal_vector`
            * - :py:meth:`~reference_vector`
            * - :py:meth:`~reference_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneNormal


Property detail
---------------

.. py:property:: normal_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.normal_vector
    :type: IAgCrdnVectorRefTo

    Specify a Normal vector.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.reference_vector
    :type: IAgCrdnVectorRefTo

    Specify a reference vector.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneNormal.reference_point
    :type: IAgCrdnPointRefTo

    Specify a reference point.


