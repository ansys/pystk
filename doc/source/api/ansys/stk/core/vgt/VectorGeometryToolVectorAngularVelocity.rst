VectorGeometryToolVectorAngularVelocity
=======================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Angular velocity vector of one set of axes computed with respect to the reference set.

.. py:currentmodule:: VectorGeometryToolVectorAngularVelocity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity.axes`
              - Specify the axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity.differencing_time_step`
              - Time step used in numerical evaluation of derivatives using central differencing.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorAngularVelocity


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity.axes
    :type: IVectorGeometryToolAxesRefTo

    Specify the axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


