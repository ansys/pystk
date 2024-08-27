VectorGeometryToolVectorRotationVector
======================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

.. py:currentmodule:: VectorGeometryToolVectorRotationVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector.axes`
              - Specify the axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector.force_minimum_rotation`
              - Insures that the rotation angle will be between 0 and pi. If the angle is increasing at pi, then the axis direction will be negated to keep phi less than pi.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorRotationVector


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector.axes
    :type: VectorGeometryToolAxesRefTo

    Specify the axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector.reference_axes
    :type: VectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: force_minimum_rotation
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector.force_minimum_rotation
    :type: bool

    Insures that the rotation angle will be between 0 and pi. If the angle is increasing at pi, then the axis direction will be negated to keep phi less than pi.


