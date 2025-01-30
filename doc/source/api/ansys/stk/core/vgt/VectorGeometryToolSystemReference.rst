VectorGeometryToolSystemReference
=================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolSystemReference

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentReference`

   Represents a System reference.

.. py:currentmodule:: VectorGeometryToolSystemReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemReference.set_path`
              - Set a new system.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemReference.set_system`
              - Set a new system.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemReference.get_system`
              - Return the actual system object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemReference.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolSystemReference



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemReference.set_path

    Set a new system.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_system(self, system: IVectorGeometryToolSystem) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemReference.set_system

    Set a new system.

    :Parameters:

    **system** : :obj:`~IVectorGeometryToolSystem`

    :Returns:

        :obj:`~None`

.. py:method:: get_system(self) -> IVectorGeometryToolSystem
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemReference.get_system

    Return the actual system object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolSystem`

.. py:method:: has_cyclic_dependency(self, system: IVectorGeometryToolSystem) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemReference.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **system** : :obj:`~IVectorGeometryToolSystem`

    :Returns:

        :obj:`~bool`

