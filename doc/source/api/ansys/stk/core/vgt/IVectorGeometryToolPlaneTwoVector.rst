IVectorGeometryToolPlaneTwoVector
=================================

.. py:class:: IVectorGeometryToolPlaneTwoVector

   object
   
   A plane passing through point and containing two given vectors.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_vector`
            * - :py:meth:`~vector2`
            * - :py:meth:`~reference_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneTwoVector


Property detail
---------------

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTwoVector.reference_vector
    :type: "IAgCrdnVectorRefTo"

    Specify a reference vector.

.. py:property:: vector2
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTwoVector.vector2
    :type: "IAgCrdnVectorRefTo"

    Specify a Normal vector.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTwoVector.reference_point
    :type: "IAgCrdnPointRefTo"

    Specify a reference point.


