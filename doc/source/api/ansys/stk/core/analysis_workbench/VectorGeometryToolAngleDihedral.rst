VectorGeometryToolAngleDihedral
===============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   An angle between two vectors about an axis.

.. py:currentmodule:: VectorGeometryToolAngleDihedral

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.counter_clockwise_rotation`
              - Specify whether the rotation is counter-clockwise.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.from_vector`
              - Specify a first vector to measure the angle.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.pole_about`
              - Specify a vector about.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.signed_angle`
              - Specify whether the axis of rotation for the angle is aligned with Positive or Negative direction of the about vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.to_vector`
              - Specify a second vector to measure the angle.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAngleDihedral


Property detail
---------------

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.counter_clockwise_rotation
    :type: bool

    Specify whether the rotation is counter-clockwise.

.. py:property:: from_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.from_vector
    :type: VectorGeometryToolVectorReference

    Specify a first vector to measure the angle.

.. py:property:: pole_about
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.pole_about
    :type: VectorGeometryToolVectorReference

    Specify a vector about.

.. py:property:: signed_angle
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.signed_angle
    :type: bool

    Specify whether the axis of rotation for the angle is aligned with Positive or Negative direction of the about vector.

.. py:property:: to_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral.to_vector
    :type: VectorGeometryToolVectorReference

    Specify a second vector to measure the angle.


