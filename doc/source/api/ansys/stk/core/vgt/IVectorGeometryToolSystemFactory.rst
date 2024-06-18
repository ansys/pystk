IVectorGeometryToolSystemFactory
================================

.. py:class:: IVectorGeometryToolSystemFactory

   object
   
   A Factory interface to create VGT systems.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create a VGT system using the specified name, description and type.
            * - :py:meth:`~is_type_supported`
              - Return true if the specified system type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemFactory



Method detail
-------------

.. py:method:: create(self, systemName:str, description:str, systemType:"CRDN_SYSTEM_TYPE") -> "IVectorGeometryToolSystem"

    Create a VGT system using the specified name, description and type.

    :Parameters:

    **systemName** : :obj:`~str`
    **description** : :obj:`~str`
    **systemType** : :obj:`~"CRDN_SYSTEM_TYPE"`

    :Returns:

        :obj:`~"IVectorGeometryToolSystem"`

.. py:method:: is_type_supported(self, type:"CRDN_SYSTEM_TYPE") -> bool

    Return true if the specified system type is supported.

    :Parameters:

    **type** : :obj:`~"CRDN_SYSTEM_TYPE"`

    :Returns:

        :obj:`~bool`

