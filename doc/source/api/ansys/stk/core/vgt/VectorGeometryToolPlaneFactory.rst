VectorGeometryToolPlaneFactory
==============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPlaneFactory

   A Factory object to create VGT planes.

.. py:currentmodule:: VectorGeometryToolPlaneFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneFactory.create`
              - Create a VGT plane using the specified name, description and type.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneFactory.is_type_supported`
              - Return true if the type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPlaneFactory



Method detail
-------------

.. py:method:: create(self, plane_name: str, description: str, plane_type: PLANE_TYPE) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneFactory.create

    Create a VGT plane using the specified name, description and type.

    :Parameters:

    **plane_name** : :obj:`~str`
    **description** : :obj:`~str`
    **plane_type** : :obj:`~PLANE_TYPE`

    :Returns:

        :obj:`~IVectorGeometryToolPlane`

.. py:method:: is_type_supported(self, type: PLANE_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~PLANE_TYPE`

    :Returns:

        :obj:`~bool`

