VectorGeometryToolAngleFactory
==============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleFactory

   Bases: 

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

.. py:method:: create(self, angleName: str, description: str, angleType: VECTOR_GEOMETRY_TOOL_ANGLE_TYPE) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleFactory.create

    Create a VGT angle using specified name, description and type.

    :Parameters:

    **angleName** : :obj:`~str`
    **description** : :obj:`~str`
    **angleType** : :obj:`~VECTOR_GEOMETRY_TOOL_ANGLE_TYPE`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: is_type_supported(self, type: VECTOR_GEOMETRY_TOOL_ANGLE_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~VECTOR_GEOMETRY_TOOL_ANGLE_TYPE`

    :Returns:

        :obj:`~bool`

