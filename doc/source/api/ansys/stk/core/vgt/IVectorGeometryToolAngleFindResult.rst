IVectorGeometryToolAngleFindResult
==================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult

   object
   
   Contains the results returned with IAgCrdnAngle.FindCoordinates method.

.. py:currentmodule:: IVectorGeometryToolAngleFindResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.angle`
              - The computed angle. The value of the angle is in \"AngleUnit\" dimension.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_from`
              - The first of the two vectors the angle is measured.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_to`
              - The second of the two vectors the angle is measured.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_about`
              - The vector the angle is rotated about.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleFindResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in \"AngleUnit\" dimension.

.. py:property:: vector_from
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_from
    :type: ICartesian3Vector

    The first of the two vectors the angle is measured.

.. py:property:: vector_to
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_to
    :type: ICartesian3Vector

    The second of the two vectors the angle is measured.

.. py:property:: vector_about
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_about
    :type: ICartesian3Vector

    The vector the angle is rotated about.


