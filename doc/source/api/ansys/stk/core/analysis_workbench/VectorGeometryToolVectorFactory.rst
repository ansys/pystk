VectorGeometryToolVectorFactory
===============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory

   A Factory object to create vectors.

.. py:currentmodule:: VectorGeometryToolVectorFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create`
              - Create a VGT vector using specified name, description and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_cross_product`
              - Create a cross product C = A x B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_displacement_vector`
              - Create a displacement vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_file_vector`
              - Create a vector interpolated from tabulated data from file.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_plugin_from_display_name`
              - Create a vector component based on a COM vector plugin. For information how to implement and register VGT plugins, see.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.is_type_supported`
              - Return true if the type is supported.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.available_plugin_display_names`
              - An array of display names associated with available vector plugins. The elements of the array are strings. Display names are used to create VGT vectors based on COM plugins using CreateVectorPluginFromDisplayName method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorFactory


Property detail
---------------

.. py:property:: available_plugin_display_names
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.available_plugin_display_names
    :type: list

    An array of display names associated with available vector plugins. The elements of the array are strings. Display names are used to create VGT vectors based on COM plugins using CreateVectorPluginFromDisplayName method.


Method detail
-------------


.. py:method:: create(self, vector_name: str, description: str, vector_type: VectorType) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create

    Create a VGT vector using specified name, description and type.

    :Parameters:

        **vector_name** : :obj:`~str`

        **description** : :obj:`~str`

        **vector_type** : :obj:`~VectorType`


    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: create_cross_product(self, vector_name: str, vector_a: IVectorGeometryToolVector, vector_b: IVectorGeometryToolVector) -> VectorGeometryToolVectorCross
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_cross_product

    Create a cross product C = A x B.

    :Parameters:

        **vector_name** : :obj:`~str`

        **vector_a** : :obj:`~IVectorGeometryToolVector`

        **vector_b** : :obj:`~IVectorGeometryToolVector`


    :Returns:

        :obj:`~VectorGeometryToolVectorCross`

.. py:method:: create_displacement_vector(self, vector_name: str, origin_point: IVectorGeometryToolPoint, dest_point: IVectorGeometryToolPoint) -> VectorGeometryToolVectorDisplacement
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_displacement_vector

    Create a displacement vector.

    :Parameters:

        **vector_name** : :obj:`~str`

        **origin_point** : :obj:`~IVectorGeometryToolPoint`

        **dest_point** : :obj:`~IVectorGeometryToolPoint`


    :Returns:

        :obj:`~VectorGeometryToolVectorDisplacement`

.. py:method:: create_file_vector(self, vector_name: str, description: str, file_name: str) -> VectorGeometryToolVectorFile
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_file_vector

    Create a vector interpolated from tabulated data from file.

    :Parameters:

        **vector_name** : :obj:`~str`

        **description** : :obj:`~str`

        **file_name** : :obj:`~str`


    :Returns:

        :obj:`~VectorGeometryToolVectorFile`

.. py:method:: create_plugin_from_display_name(self, vector_name: str, description: str, display_name: str) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.create_plugin_from_display_name

    Create a vector component based on a COM vector plugin. For information how to implement and register VGT plugins, see.

    :Parameters:

        **vector_name** : :obj:`~str`

        **description** : :obj:`~str`

        **display_name** : :obj:`~str`


    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: is_type_supported(self, type: VectorType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

        **type** : :obj:`~VectorType`


    :Returns:

        :obj:`~bool`

