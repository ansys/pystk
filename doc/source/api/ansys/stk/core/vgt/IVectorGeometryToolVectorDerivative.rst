IVectorGeometryToolVectorDerivative
===================================

.. py:class:: IVectorGeometryToolVectorDerivative

   object
   
   A vector derivative of a vector computed with respect to specified axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~vector`
            * - :py:meth:`~reference_axes`
            * - :py:meth:`~differencing_time_step`
            * - :py:meth:`~force_use_of_numerical_differences`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorDerivative


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.vector
    :type: IAgCrdnVectorRefTo

    Specify a base vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.reference_axes
    :type: IAgCrdnAxesRefTo

    Specify a reference axes.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.

.. py:property:: force_use_of_numerical_differences
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDerivative.force_use_of_numerical_differences
    :type: bool

    Force the use of numerical differences even if the derivative can be computed analytically.


