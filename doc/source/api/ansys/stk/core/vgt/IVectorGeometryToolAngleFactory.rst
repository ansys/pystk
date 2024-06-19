IVectorGeometryToolAngleFactory
===============================

.. py:class:: IVectorGeometryToolAngleFactory

   object
   
   A Factory object to create angles.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create a VGT angle using specified name, description and type.
            * - :py:meth:`~is_type_supported`
              - Return true if the type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleFactory



Method detail
-------------

.. py:method:: create(self, angleName: str, description: str, angleType: VECTOR_GEOMETRY_TOOL_ANGLE_TYPE) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFactory.create

    Create a VGT angle using specified name, description and type.

    :Parameters:

    **angleName** : :obj:`~str`
    **description** : :obj:`~str`
    **angleType** : :obj:`~VECTOR_GEOMETRY_TOOL_ANGLE_TYPE`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: is_type_supported(self, type: VECTOR_GEOMETRY_TOOL_ANGLE_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~VECTOR_GEOMETRY_TOOL_ANGLE_TYPE`

    :Returns:

        :obj:`~bool`

