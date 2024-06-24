IVectorGeometryToolVectorFactory
================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorFactory

   object
   
   A Factory object to create vectors.

.. py:currentmodule:: IVectorGeometryToolVectorFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create`
              - Create a VGT vector using specified name, description and type.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.is_type_supported`
              - Return true if the type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create_displacement_vector`
              - Create a displacement vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create_vector_plugin_from_display_name`
              - Create a vector component based on a COM vector plugin. For information how to implement and register VGT plugins, see.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create_cross_product_vector`
              - Create a cross product C = A x B.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.available_vector_plugin_display_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorFactory


Property detail
---------------

.. py:property:: available_vector_plugin_display_names
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.available_vector_plugin_display_names
    :type: list

    An array of display names associated with available vector plugins. The elements of the array are strings. Display names are used to create VGT vectors based on COM plugins using CreateVectorPluginFromDisplayName method.


Method detail
-------------

.. py:method:: create(self, vectorName: str, description: str, vectorType: VECTOR_GEOMETRY_TOOL_VECTOR_TYPE) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create

    Create a VGT vector using specified name, description and type.

    :Parameters:

    **vectorName** : :obj:`~str`
    **description** : :obj:`~str`
    **vectorType** : :obj:`~VECTOR_GEOMETRY_TOOL_VECTOR_TYPE`

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: is_type_supported(self, type: VECTOR_GEOMETRY_TOOL_VECTOR_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~VECTOR_GEOMETRY_TOOL_VECTOR_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_displacement_vector(self, vectorName: str, originPoint: IVectorGeometryToolPoint, destPoint: IVectorGeometryToolPoint) -> IVectorGeometryToolVectorDisplacement
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create_displacement_vector

    Create a displacement vector.

    :Parameters:

    **vectorName** : :obj:`~str`
    **originPoint** : :obj:`~IVectorGeometryToolPoint`
    **destPoint** : :obj:`~IVectorGeometryToolPoint`

    :Returns:

        :obj:`~IVectorGeometryToolVectorDisplacement`


.. py:method:: create_vector_plugin_from_display_name(self, vectorName: str, description: str, displayName: str) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create_vector_plugin_from_display_name

    Create a vector component based on a COM vector plugin. For information how to implement and register VGT plugins, see.

    :Parameters:

    **vectorName** : :obj:`~str`
    **description** : :obj:`~str`
    **displayName** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: create_cross_product_vector(self, vectorName: str, vectorA: IVectorGeometryToolVector, vectorB: IVectorGeometryToolVector) -> IVectorGeometryToolVectorCross
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFactory.create_cross_product_vector

    Create a cross product C = A x B.

    :Parameters:

    **vectorName** : :obj:`~str`
    **vectorA** : :obj:`~IVectorGeometryToolVector`
    **vectorB** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~IVectorGeometryToolVectorCross`

