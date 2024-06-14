IVectorGeometryToolVectorAngleRate
==================================

.. py:class:: IVectorGeometryToolVectorAngleRate

   object
   
   Angle rate vector perpendicular to the plane in which the angle is defined.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~angle`
            * - :py:meth:`~differencing_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorAngleRate


Property detail
---------------

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngleRate.angle
    :type: "IAgCrdnAngleRefTo"

    Specify an angle. The angle vector will be perpendicular to the plane in which the angle is defined.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngleRate.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


