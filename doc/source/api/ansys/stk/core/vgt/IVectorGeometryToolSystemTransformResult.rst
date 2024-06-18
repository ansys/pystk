IVectorGeometryToolSystemTransformResult
========================================

.. py:class:: IVectorGeometryToolSystemTransformResult

   object
   
   Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemTransformResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemTransformResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemTransformResult.vector
    :type: "IAgCartesian3Vector"

    The transformed vector.


