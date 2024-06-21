IVectorGeometryToolVectorDerivative
===================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative

   object
   
   A vector derivative of a vector computed with respect to specified axes.

.. py:currentmodule:: IVectorGeometryToolVectorDerivative

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.reference_axes`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.differencing_time_step`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.force_use_of_numerical_differences`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorDerivative


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a base vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.

.. py:property:: force_use_of_numerical_differences
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.force_use_of_numerical_differences
    :type: bool

    Force the use of numerical differences even if the derivative can be computed analytically.


