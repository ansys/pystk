VectorGeometryToolSystemFactory
===============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolSystemFactory

   A Factory class to create VGT systems.

.. py:currentmodule:: VectorGeometryToolSystemFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemFactory.create`
              - Create a VGT system using the specified name, description and type.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemFactory.is_type_supported`
              - Return true if the specified system type is supported.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolSystemFactory



Method detail
-------------

.. py:method:: create(self, system_name: str, description: str, system_type: SYSTEM_TYPE) -> IVectorGeometryToolSystem
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemFactory.create

    Create a VGT system using the specified name, description and type.

    :Parameters:

    **system_name** : :obj:`~str`
    **description** : :obj:`~str`
    **system_type** : :obj:`~SYSTEM_TYPE`

    :Returns:

        :obj:`~IVectorGeometryToolSystem`

.. py:method:: is_type_supported(self, type: SYSTEM_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemFactory.is_type_supported

    Return true if the specified system type is supported.

    :Parameters:

    **type** : :obj:`~SYSTEM_TYPE`

    :Returns:

        :obj:`~bool`

