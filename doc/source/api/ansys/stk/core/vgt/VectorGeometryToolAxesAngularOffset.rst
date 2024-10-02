VectorGeometryToolAxesAngularOffset
===================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

.. py:currentmodule:: VectorGeometryToolAxesAngularOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.spin_vector`
              - Specify a spin vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.rotation_angle`
              - Specify a rotational angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.fixed_offset_angle`
              - Specify an additional rotational offset.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesAngularOffset


Property detail
---------------

.. py:property:: spin_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.spin_vector
    :type: VectorReference

    Specify a spin vector.

.. py:property:: rotation_angle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.rotation_angle
    :type: VectorGeometryToolAngleReference

    Specify a rotational angle.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: fixed_offset_angle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset.fixed_offset_angle
    :type: float

    Specify an additional rotational offset.


