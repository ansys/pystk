VectorGeometryToolAngleFactory
==============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleFactory

   A Factory object to create angles.

.. py:currentmodule:: VectorGeometryToolAngleFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleFactory.create`
              - Create a VGT angle using specified name, description and type.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleFactory.is_type_supported`
              - Return true if the type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAngleFactory



Method detail
-------------

.. py:method:: create(self, angle_name: str, description: str, angle_type: ANGLE_TYPE) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleFactory.create

    Create a VGT angle using specified name, description and type.

    :Parameters:

    **angle_name** : :obj:`~str`
    **description** : :obj:`~str`
    **angle_type** : :obj:`~ANGLE_TYPE`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: is_type_supported(self, type: ANGLE_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~ANGLE_TYPE`

    :Returns:

        :obj:`~bool`

