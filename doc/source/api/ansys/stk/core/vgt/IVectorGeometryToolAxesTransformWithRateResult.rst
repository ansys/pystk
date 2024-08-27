IVectorGeometryToolAxesTransformWithRateResult
==============================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult

   Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

.. py:currentmodule:: IVectorGeometryToolAxesTransformWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.vector`
              - The output vector in the current axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.velocity`
              - The vector velocity.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.vector
    :type: ICartesian3Vector

    The output vector in the current axes.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.velocity
    :type: ICartesian3Vector

    The vector velocity.


