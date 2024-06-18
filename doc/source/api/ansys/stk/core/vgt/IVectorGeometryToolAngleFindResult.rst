IVectorGeometryToolAngleFindResult
==================================

.. py:class:: IVectorGeometryToolAngleFindResult

   object
   
   Contains the results returned with IAgCrdnAngle.FindCoordinates method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~angle`
            * - :py:meth:`~vector_from`
            * - :py:meth:`~vector_to`
            * - :py:meth:`~vector_about`


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
    :type: "IAgCartesian3Vector"

    The first of the two vectors the angle is measured.

.. py:property:: vector_to
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_to
    :type: "IAgCartesian3Vector"

    The second of the two vectors the angle is measured.

.. py:property:: vector_about
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult.vector_about
    :type: "IAgCartesian3Vector"

    The vector the angle is rotated about.


