IVectorGeometryToolAxesRefTo
============================

.. py:class:: IVectorGeometryToolAxesRefTo

   object
   
   Represents a reference to a VGT axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_path`
              - Set a new axes.
            * - :py:meth:`~set_axes`
              - Set a new axes.
            * - :py:meth:`~get_axes`
              - Return the actual axes object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:meth:`~has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesRefTo



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesRefTo.set_path

    Set a new axes.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_axes(self, axes: IVectorGeometryToolAxes) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesRefTo.set_axes

    Set a new axes.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~None`

.. py:method:: get_axes(self) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesRefTo.get_axes

    Return the actual axes object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolAxes`

.. py:method:: has_cyclic_dependency(self, axes: IVectorGeometryToolAxes) -> bool
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesRefTo.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~bool`

