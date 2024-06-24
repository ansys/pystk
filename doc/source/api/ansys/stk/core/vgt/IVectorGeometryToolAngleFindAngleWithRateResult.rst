IVectorGeometryToolAngleFindAngleWithRateResult
===============================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult

   object
   
   Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

.. py:currentmodule:: IVectorGeometryToolAngleFindAngleWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult.is_valid`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult.angle`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult.angle_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleFindAngleWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in \"AngleUnit\" dimension.

.. py:property:: angle_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult.angle_rate
    :type: typing.Any

    The computed angle rate. The value of the angle rate is in \"AngleRateUnit\" dimension.


