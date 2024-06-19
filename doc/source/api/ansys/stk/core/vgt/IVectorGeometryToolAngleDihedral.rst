IVectorGeometryToolAngleDihedral
================================

.. py:class:: IVectorGeometryToolAngleDihedral

   object
   
   An angle between two vectors about an axis.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~from_vector`
            * - :py:meth:`~to_vector`
            * - :py:meth:`~pole_about`
            * - :py:meth:`~counter_clockwise_rotation`
            * - :py:meth:`~signed_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleDihedral


Property detail
---------------

.. py:property:: from_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.from_vector
    :type: IAgCrdnVectorRefTo

    Specify a first vector to measure the angle.

.. py:property:: to_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.to_vector
    :type: IAgCrdnVectorRefTo

    Specify a second vector to measure the angle.

.. py:property:: pole_about
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.pole_about
    :type: IAgCrdnVectorRefTo

    Specify a vector about.

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.counter_clockwise_rotation
    :type: bool

    Specify whether the rotation is counter-clockwise.

.. py:property:: signed_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleDihedral.signed_angle
    :type: bool

    Specify whether the axis of rotation for the angle is aligned with Positive or Negative direction of the about vector.


