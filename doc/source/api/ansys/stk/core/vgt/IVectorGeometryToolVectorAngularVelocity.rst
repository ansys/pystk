IVectorGeometryToolVectorAngularVelocity
========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity

   object
   
   Angular velocity vector of one set of axes computed with respect to the reference set.

.. py:currentmodule:: IVectorGeometryToolVectorAngularVelocity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.axes`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.reference_axes`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.differencing_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorAngularVelocity


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.axes
    :type: IVectorGeometryToolAxesRefTo

    Specify the axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


