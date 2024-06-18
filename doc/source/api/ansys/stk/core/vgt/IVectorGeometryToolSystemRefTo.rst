IVectorGeometryToolSystemRefTo
==============================

.. py:class:: IVectorGeometryToolSystemRefTo

   object
   
   Represents a reference to a VGT system.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_path`
              - Set a new system.
            * - :py:meth:`~set_system`
              - Set a new system.
            * - :py:meth:`~get_system`
              - Return the actual system object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.
            * - :py:meth:`~has_cyclic_dependency`
              - Test whether the input component and the target component form a cyclic dependency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemRefTo



Method detail
-------------

.. py:method:: set_path(self, path:str) -> None

    Set a new system.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_system(self, system:"IVectorGeometryToolSystem") -> None

    Set a new system.

    :Parameters:

    **system** : :obj:`~"IVectorGeometryToolSystem"`

    :Returns:

        :obj:`~None`

.. py:method:: get_system(self) -> "IVectorGeometryToolSystem"

    Return the actual system object behind the reference. Use IAgCrdn.IsValid to test the validity of the returned object.

    :Returns:

        :obj:`~"IVectorGeometryToolSystem"`

.. py:method:: has_cyclic_dependency(self, system:"IVectorGeometryToolSystem") -> bool

    Test whether the input component and the target component form a cyclic dependency.

    :Parameters:

    **system** : :obj:`~"IVectorGeometryToolSystem"`

    :Returns:

        :obj:`~bool`

