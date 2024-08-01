IVectorGeometryToolAngleFindWithRateResult
==========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult

   Contains the results returned with IAgCrdnAngle.FindCoordinatesWithRate method.

.. py:currentmodule:: IVectorGeometryToolAngleFindWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.angle`
              - The computed angle. The value of the angle is in \"AngleUnit\" dimension.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.angle_rate`
              - The computed angle rate. The value of the angle rate is in \"AngleRateUnit\" dimension.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.vector_from`
              - The first of the two vectors the angle is measured.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.vector_to`
              - The second of the two vectors the angle is measured.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.vector_about`
              - The vector the angle is rotated about.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleFindWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in \"AngleUnit\" dimension.

.. py:property:: angle_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.angle_rate
    :type: typing.Any

    The computed angle rate. The value of the angle rate is in \"AngleRateUnit\" dimension.

.. py:property:: vector_from
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.vector_from
    :type: ICartesian3Vector

    The first of the two vectors the angle is measured.

.. py:property:: vector_to
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.vector_to
    :type: ICartesian3Vector

    The second of the two vectors the angle is measured.

.. py:property:: vector_about
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult.vector_about
    :type: ICartesian3Vector

    The vector the angle is rotated about.


