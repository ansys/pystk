VectorGeometryToolVectorDerivative
==================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorDerivative

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A vector derivative of a vector computed with respect to specified axes.

.. py:currentmodule:: VectorGeometryToolVectorDerivative

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.vector`
              - Specify a base vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.differencing_time_step`
              - Time step used in numerical evaluation of derivatives using central differencing.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.force_use_of_numerical_differences`
              - Force the use of numerical differences even if the derivative can be computed analytically.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorDerivative


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a base vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.

.. py:property:: force_use_of_numerical_differences
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDerivative.force_use_of_numerical_differences
    :type: bool

    Force the use of numerical differences even if the derivative can be computed analytically.


