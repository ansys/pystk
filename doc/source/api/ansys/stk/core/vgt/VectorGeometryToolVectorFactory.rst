VectorGeometryToolVectorFactory
===============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorFactory

   A Factory object to create vectors.

.. py:currentmodule:: VectorGeometryToolVectorFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create`
              - Create a VGT vector using specified name, description and type.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFactory.is_type_supported`
              - Return true if the type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create_displacement_vector`
              - Create a displacement vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create_plugin_from_display_name`
              - Create a vector component based on a COM vector plugin. For information how to implement and register VGT plugins, see.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create_cross_product`
              - Create a cross product C = A x B.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFactory.available_plugin_display_names`
              - An array of display names associated with available vector plugins. The elements of the array are strings. Display names are used to create VGT vectors based on COM plugins using CreateVectorPluginFromDisplayName method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorFactory


Property detail
---------------

.. py:property:: available_plugin_display_names
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFactory.available_plugin_display_names
    :type: list

    An array of display names associated with available vector plugins. The elements of the array are strings. Display names are used to create VGT vectors based on COM plugins using CreateVectorPluginFromDisplayName method.


Method detail
-------------

.. py:method:: create(self, vector_name: str, description: str, vector_type: VECTOR_TYPE) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create

    Create a VGT vector using specified name, description and type.

    :Parameters:

    **vector_name** : :obj:`~str`
    **description** : :obj:`~str`
    **vector_type** : :obj:`~VECTOR_TYPE`

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: is_type_supported(self, type: VECTOR_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~VECTOR_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_displacement_vector(self, vector_name: str, origin_point: IVectorGeometryToolPoint, dest_point: IVectorGeometryToolPoint) -> VectorGeometryToolVectorDisplacement
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create_displacement_vector

    Create a displacement vector.

    :Parameters:

    **vector_name** : :obj:`~str`
    **origin_point** : :obj:`~IVectorGeometryToolPoint`
    **dest_point** : :obj:`~IVectorGeometryToolPoint`

    :Returns:

        :obj:`~VectorGeometryToolVectorDisplacement`


.. py:method:: create_plugin_from_display_name(self, vector_name: str, description: str, display_name: str) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create_plugin_from_display_name

    Create a vector component based on a COM vector plugin. For information how to implement and register VGT plugins, see.

    :Parameters:

    **vector_name** : :obj:`~str`
    **description** : :obj:`~str`
    **display_name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: create_cross_product(self, vector_name: str, vector_a: IVectorGeometryToolVector, vector_b: IVectorGeometryToolVector) -> VectorGeometryToolVectorCross
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFactory.create_cross_product

    Create a cross product C = A x B.

    :Parameters:

    **vector_name** : :obj:`~str`
    **vector_a** : :obj:`~IVectorGeometryToolVector`
    **vector_b** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~VectorGeometryToolVectorCross`

