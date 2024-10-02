VectorGeometryToolAngleReference
================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleReference

   Bases: :py:class:`~ansys.stk.core.vgt.IComponentReference`

   Represents a reference to a VGT angle.

.. py:currentmodule:: VectorGeometryToolAngleReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleReference.set_path`
              - Set a new angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleReference.set_angle`
              - Set a new angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleReference.get_angle`
              - Return the actual angle object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleReference.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAngleReference



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleReference.set_path

    Set a new angle.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_angle(self, angle: IVectorGeometryToolAngle) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleReference.set_angle

    Set a new angle.

    :Parameters:

    **angle** : :obj:`~IVectorGeometryToolAngle`

    :Returns:

        :obj:`~None`

.. py:method:: get_angle(self) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleReference.get_angle

    Return the actual angle object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: has_cyclic_dependency(self, angle: IVectorGeometryToolAngle) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleReference.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **angle** : :obj:`~IVectorGeometryToolAngle`

    :Returns:

        :obj:`~bool`

