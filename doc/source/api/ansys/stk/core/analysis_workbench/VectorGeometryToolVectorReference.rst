VectorGeometryToolVectorReference
=================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentReference`

   Represents a vector reference.

.. py:currentmodule:: VectorGeometryToolVectorReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.set_path`
              - Set a new vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.set_vector`
              - Set a new vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.get_vector`
              - Return the actual vector object behind the reference. Use IAnalysisWorkbenchComponent.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorReference



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.set_path

    Set a new vector.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_vector(self, vector: IVectorGeometryToolVector) -> None
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.set_vector

    Set a new vector.

    :Parameters:

    **vector** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~None`

.. py:method:: get_vector(self) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.get_vector

    Return the actual vector object behind the reference. Use IAnalysisWorkbenchComponent.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: has_cyclic_dependency(self, vector: IVectorGeometryToolVector) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **vector** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~bool`

