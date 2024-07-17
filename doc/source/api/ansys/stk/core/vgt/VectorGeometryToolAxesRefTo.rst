VectorGeometryToolAxesRefTo
===========================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesRefTo

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchRefTo`

   Represents a reference to a VGT axes.

.. py:currentmodule:: VectorGeometryToolAxesRefTo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.set_path`
              - Set a new axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.set_axes`
              - Set a new axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.get_axes`
              - Return the actual axes object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesRefTo



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.set_path

    Set a new axes.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_axes(self, axes: IVectorGeometryToolAxes) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.set_axes

    Set a new axes.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~None`

.. py:method:: get_axes(self) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.get_axes

    Return the actual axes object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolAxes`

.. py:method:: has_cyclic_dependency(self, axes: IVectorGeometryToolAxes) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesRefTo.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~bool`

