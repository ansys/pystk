IVectorGeometryToolAngleFindAngleResult
=======================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleResult

   object
   
   Contains the results returned with IAgCrdnAngle.FindAngle method.

.. py:currentmodule:: IVectorGeometryToolAngleFindAngleResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleResult.angle`
              - The computed angle. The value of the angle is in \"AngleUnit\" dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleFindAngleResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in \"AngleUnit\" dimension.


