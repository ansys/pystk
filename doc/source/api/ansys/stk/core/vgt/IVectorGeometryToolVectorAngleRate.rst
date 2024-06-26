IVectorGeometryToolVectorAngleRate
==================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorAngleRate

   object
   
   Angle rate vector perpendicular to the plane in which the angle is defined.

.. py:currentmodule:: IVectorGeometryToolVectorAngleRate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorAngleRate.angle`
              - Specify an angle. The angle vector will be perpendicular to the plane in which the angle is defined.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorAngleRate.differencing_time_step`
              - Time step used in numerical evaluation of derivatives using central differencing.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorAngleRate


Property detail
---------------

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngleRate.angle
    :type: IVectorGeometryToolAngleRefTo

    Specify an angle. The angle vector will be perpendicular to the plane in which the angle is defined.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngleRate.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


