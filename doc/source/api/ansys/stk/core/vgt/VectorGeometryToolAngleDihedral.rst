VectorGeometryToolAngleDihedral
===============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleDihedral

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngle`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IComponent`

   An angle between two vectors about an axis.

.. py:currentmodule:: VectorGeometryToolAngleDihedral

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.from_vector`
              - Specify a first vector to measure the angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.to_vector`
              - Specify a second vector to measure the angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.pole_about`
              - Specify a vector about.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.counter_clockwise_rotation`
              - Specify whether the rotation is counter-clockwise.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.signed_angle`
              - Specify whether the axis of rotation for the angle is aligned with Positive or Negative direction of the about vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAngleDihedral


Property detail
---------------

.. py:property:: from_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.from_vector
    :type: VectorReference

    Specify a first vector to measure the angle.

.. py:property:: to_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.to_vector
    :type: VectorReference

    Specify a second vector to measure the angle.

.. py:property:: pole_about
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.pole_about
    :type: VectorReference

    Specify a vector about.

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.counter_clockwise_rotation
    :type: bool

    Specify whether the rotation is counter-clockwise.

.. py:property:: signed_angle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleDihedral.signed_angle
    :type: bool

    Specify whether the axis of rotation for the angle is aligned with Positive or Negative direction of the about vector.


