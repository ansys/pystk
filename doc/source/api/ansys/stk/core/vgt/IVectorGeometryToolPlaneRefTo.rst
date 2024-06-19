IVectorGeometryToolPlaneRefTo
=============================

.. py:class:: IVectorGeometryToolPlaneRefTo

   object
   
   Represents a reference to a VGT plane.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_path`
              - Set a new plane using a specified path.
            * - :py:meth:`~set_plane`
              - Set a new plane.
            * - :py:meth:`~get_plane`
              - Return the actual plane object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:meth:`~has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneRefTo



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneRefTo.set_path

    Set a new plane using a specified path.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_plane(self, plane: IVectorGeometryToolPlane) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneRefTo.set_plane

    Set a new plane.

    :Parameters:

    **plane** : :obj:`~IVectorGeometryToolPlane`

    :Returns:

        :obj:`~None`

.. py:method:: get_plane(self) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneRefTo.get_plane

    Return the actual plane object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolPlane`

.. py:method:: has_cyclic_dependency(self, plane: IVectorGeometryToolPlane) -> bool
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneRefTo.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **plane** : :obj:`~IVectorGeometryToolPlane`

    :Returns:

        :obj:`~bool`

