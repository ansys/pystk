IVectorGeometryToolSystemTransformWithRateResult
================================================

.. py:class:: IVectorGeometryToolSystemTransformWithRateResult

   object
   
   Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

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
            * - :py:meth:`~velocity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult.vector
    :type: IAgCartesian3Vector

    The transformed vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult.velocity
    :type: IAgCartesian3Vector

    The vector's velocity.


