IVectorGeometryToolAxesAngularOffset
====================================

.. py:class:: IVectorGeometryToolAxesAngularOffset

   object
   
   Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~spin_vector`
            * - :py:meth:`~rotation_angle`
            * - :py:meth:`~reference_axes`
            * - :py:meth:`~fixed_offset_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesAngularOffset


Property detail
---------------

.. py:property:: spin_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.spin_vector
    :type: "IAgCrdnVectorRefTo"

    Specify a spin vector.

.. py:property:: rotation_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.rotation_angle
    :type: "IAgCrdnAngleRefTo"

    Specify a rotational angle.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.reference_axes
    :type: "IAgCrdnAxesRefTo"

    Specify a reference axes.

.. py:property:: fixed_offset_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.fixed_offset_angle
    :type: float

    Specify an additional rotational offset.


