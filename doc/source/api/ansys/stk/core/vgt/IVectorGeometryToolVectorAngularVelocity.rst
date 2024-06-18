IVectorGeometryToolVectorAngularVelocity
========================================

.. py:class:: IVectorGeometryToolVectorAngularVelocity

   object
   
   Angular velocity vector of one set of axes computed with respect to the reference set.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~axes`
            * - :py:meth:`~reference_axes`
            * - :py:meth:`~differencing_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorAngularVelocity


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.axes
    :type: "IAgCrdnAxesRefTo"

    Specify the axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.reference_axes
    :type: "IAgCrdnAxesRefTo"

    Specify a reference axes.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorAngularVelocity.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


