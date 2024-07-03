IVectorGeometryToolSystemTransformWithRateResult
================================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult

   object
   
   Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

.. py:currentmodule:: IVectorGeometryToolSystemTransformWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult.vector`
              - The transformed vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult.velocity`
              - The vector's velocity.


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
    :type: ICartesian3Vector

    The transformed vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult.velocity
    :type: ICartesian3Vector

    The vector's velocity.


