VectorGeometryToolPointReference
================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentReference`

   Represents a reference to a VGT point.

.. py:currentmodule:: VectorGeometryToolPointReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.set_path`
              - Set a new point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.set_point`
              - Set a new point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.get_point`
              - Return the actual point object behind the reference. Use IAnalysisWorkbenchComponent.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointReference



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.set_path

    Set a new point.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_point(self, point: IVectorGeometryToolPoint) -> None
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.set_point

    Set a new point.

    :Parameters:

        **point** : :obj:`~IVectorGeometryToolPoint`


    :Returns:

        :obj:`~None`

.. py:method:: get_point(self) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.get_point

    Return the actual point object behind the reference. Use IAnalysisWorkbenchComponent.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolPoint`

.. py:method:: has_cyclic_dependency(self, point: IVectorGeometryToolPoint) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

        **point** : :obj:`~IVectorGeometryToolPoint`


    :Returns:

        :obj:`~bool`

