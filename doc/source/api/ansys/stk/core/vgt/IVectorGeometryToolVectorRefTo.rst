IVectorGeometryToolVectorRefTo
==============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo

   object
   
   Represents a reference to a VGT vector.

.. py:currentmodule:: IVectorGeometryToolVectorRefTo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.set_path`
              - Set a new vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.set_vector`
              - Set a new vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.get_vector`
              - Return the actual vector object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorRefTo



Method detail
-------------

.. py:method:: set_path(self, path: str) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.set_path

    Set a new vector.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_vector(self, vector: IVectorGeometryToolVector) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.set_vector

    Set a new vector.

    :Parameters:

    **vector** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~None`

.. py:method:: get_vector(self) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.get_vector

    Return the actual vector object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: has_cyclic_dependency(self, vector: IVectorGeometryToolVector) -> bool
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorRefTo.has_cyclic_dependency

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **vector** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~bool`

