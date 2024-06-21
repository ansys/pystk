IVectorGeometryToolAxesAngularOffset
====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset

   object
   
   Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

.. py:currentmodule:: IVectorGeometryToolAxesAngularOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.spin_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.rotation_angle`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.reference_axes`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.fixed_offset_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesAngularOffset


Property detail
---------------

.. py:property:: spin_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.spin_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a spin vector.

.. py:property:: rotation_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.rotation_angle
    :type: IVectorGeometryToolAngleRefTo

    Specify a rotational angle.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: fixed_offset_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAngularOffset.fixed_offset_angle
    :type: float

    Specify an additional rotational offset.


