IVectorGeometryToolVectorRotationVector
=======================================

.. py:class:: IVectorGeometryToolVectorRotationVector

   object
   
   Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

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
            * - :py:meth:`~force_minimum_rotation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorRotationVector


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorRotationVector.axes
    :type: "IAgCrdnAxesRefTo"

    Specify the axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorRotationVector.reference_axes
    :type: "IAgCrdnAxesRefTo"

    Specify a reference axes.

.. py:property:: force_minimum_rotation
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorRotationVector.force_minimum_rotation
    :type: bool

    Insures that the rotation angle will be between 0 and pi. If the angle is increasing at pi, then the axis direction will be negated to keep phi less than pi.


