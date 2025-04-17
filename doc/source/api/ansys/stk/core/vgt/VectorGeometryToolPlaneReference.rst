VectorGeometryToolPlaneReference
================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPlaneReference

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentReference`

   Represents a Plane reference.

.. py:currentmodule:: VectorGeometryToolPlaneReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneReference.set_path`
              - Set a new plane using a specified path.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneReference.set_plane`
              - Set a new plane.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneReference.get_plane`
              - Return the actual plane object behind the reference. Use IAnalysisWorkbenchComponent.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneReference.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPlaneReference



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneReference.set_path

    Set a new plane using a specified path.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_plane(self, plane: IVectorGeometryToolPlane) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneReference.set_plane

    Set a new plane.

    :Parameters:

    **plane** : :obj:`~IVectorGeometryToolPlane`

    :Returns:

        :obj:`~None`

.. py:method:: get_plane(self) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneReference.get_plane

    Return the actual plane object behind the reference. Use IAnalysisWorkbenchComponent.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolPlane`

.. py:method:: has_cyclic_dependency(self, plane: IVectorGeometryToolPlane) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneReference.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **plane** : :obj:`~IVectorGeometryToolPlane`

    :Returns:

        :obj:`~bool`

