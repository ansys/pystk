IAngleFindAngleWithRateResult
=============================

.. py:class:: ansys.stk.core.vgt.IAngleFindAngleWithRateResult

   Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

.. py:currentmodule:: IAngleFindAngleWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAngleFindAngleWithRateResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.IAngleFindAngleWithRateResult.angle`
              - The computed angle. The value of the angle is in \"AngleUnit\" dimension.
            * - :py:attr:`~ansys.stk.core.vgt.IAngleFindAngleWithRateResult.angle_rate`
              - The computed angle rate. The value of the angle rate is in \"AngleRateUnit\" dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAngleFindAngleWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IAngleFindAngleWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.IAngleFindAngleWithRateResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in \"AngleUnit\" dimension.

.. py:property:: angle_rate
    :canonical: ansys.stk.core.vgt.IAngleFindAngleWithRateResult.angle_rate
    :type: typing.Any

    The computed angle rate. The value of the angle rate is in \"AngleRateUnit\" dimension.


