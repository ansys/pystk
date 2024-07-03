IVectorGeometryToolAngleDihedral
================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral

   object
   
   An angle between two vectors about an axis.

.. py:currentmodule:: IVectorGeometryToolAngleDihedral

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.from_vector`
              - Specify a first vector to measure the angle.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.to_vector`
              - Specify a second vector to measure the angle.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.pole_about`
              - Specify a vector about.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.counter_clockwise_rotation`
              - Specify whether the rotation is counter-clockwise.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.signed_angle`
              - Specify whether the axis of rotation for the angle is aligned with Positive or Negative direction of the about vector.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleDihedral


Property detail
---------------

.. py:property:: from_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.from_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a first vector to measure the angle.

.. py:property:: to_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.to_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a second vector to measure the angle.

.. py:property:: pole_about
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.pole_about
    :type: IVectorGeometryToolVectorRefTo

    Specify a vector about.

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.counter_clockwise_rotation
    :type: bool

    Specify whether the rotation is counter-clockwise.

.. py:property:: signed_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.signed_angle
    :type: bool

    Specify whether the axis of rotation for the angle is aligned with Positive or Negative direction of the about vector.


