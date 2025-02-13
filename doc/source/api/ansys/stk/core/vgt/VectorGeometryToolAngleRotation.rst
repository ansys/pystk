VectorGeometryToolAngleRotation
===============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleRotation

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngle`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

.. py:currentmodule:: VectorGeometryToolAngleRotation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleRotation.from_axes`
              - Specify an axes to rotate from.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleRotation.to_axes`
              - Specify an axes to rotate to.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleRotation.reference_direction`
              - Specify a rotation direction.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAngleRotation


Property detail
---------------

.. py:property:: from_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleRotation.from_axes
    :type: VectorGeometryToolAxesReference

    Specify an axes to rotate from.

.. py:property:: to_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleRotation.to_axes
    :type: VectorGeometryToolAxesReference

    Specify an axes to rotate to.

.. py:property:: reference_direction
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleRotation.reference_direction
    :type: PrincipalAxisOfRotationType

    Specify a rotation direction.


