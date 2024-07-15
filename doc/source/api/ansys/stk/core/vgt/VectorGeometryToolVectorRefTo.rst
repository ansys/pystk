VectorGeometryToolVectorRefTo
=============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorRefTo

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchRefTo`

   Represents a vector reference.

.. py:currentmodule:: VectorGeometryToolVectorRefTo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.set_path`
              - Set a new vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.set_vector`
              - Set a new vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.get_vector`
              - Return the actual vector object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorRefTo



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.set_path

    Set a new vector.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_vector(self, vector: IVectorGeometryToolVector) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.set_vector

    Set a new vector.

    :Parameters:

    **vector** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~None`

.. py:method:: get_vector(self) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.get_vector

    Return the actual vector object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: has_cyclic_dependency(self, vector: IVectorGeometryToolVector) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorRefTo.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **vector** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~bool`

