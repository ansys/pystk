VectorGeometryToolPointFactory
==============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory

   A Factory object to create points.

.. py:currentmodule:: VectorGeometryToolPointFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.create`
              - Create a VGT point using the specified name, description and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.create_fixed_on_central_body`
              - Create a point fixed on a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.create_plugin_from_display_name`
              - Create a point component based on a COM point plugin. For information how to implement and register VGT plugins, see.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.is_type_supported`
              - Return true if the type is supported.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.available_plugin_display_names`
              - An array of display names associated with available point plugins. The elements of the array are strings. Display names are used to create VGT points based on COM plugins using CreatePointPluginFromDisplayName method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointFactory


Property detail
---------------

.. py:property:: available_plugin_display_names
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.available_plugin_display_names
    :type: list

    An array of display names associated with available point plugins. The elements of the array are strings. Display names are used to create VGT points based on COM plugins using CreatePointPluginFromDisplayName method.


Method detail
-------------


.. py:method:: create(self, point_name: str, description: str, point_type: PointType) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.create

    Create a VGT point using the specified name, description and type.

    :Parameters:

        **point_name** : :obj:`~str`

        **description** : :obj:`~str`

        **point_type** : :obj:`~PointType`


    :Returns:

        :obj:`~IVectorGeometryToolPoint`

.. py:method:: create_fixed_on_central_body(self, point_name: str, description: str, longitude: typing.Any, latitude: typing.Any, altitude: float, reference_shape: SurfaceReferenceShapeType) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.create_fixed_on_central_body

    Create a point fixed on a central body.

    :Parameters:

        **point_name** : :obj:`~str`

        **description** : :obj:`~str`

        **longitude** : :obj:`~typing.Any`

        **latitude** : :obj:`~typing.Any`

        **altitude** : :obj:`~float`

        **reference_shape** : :obj:`~SurfaceReferenceShapeType`


    :Returns:

        :obj:`~IVectorGeometryToolPoint`

.. py:method:: create_plugin_from_display_name(self, point_name: str, description: str, display_name: str) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.create_plugin_from_display_name

    Create a point component based on a COM point plugin. For information how to implement and register VGT plugins, see.

    :Parameters:

        **point_name** : :obj:`~str`

        **description** : :obj:`~str`

        **display_name** : :obj:`~str`


    :Returns:

        :obj:`~IVectorGeometryToolPoint`

.. py:method:: is_type_supported(self, type: PointType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

        **type** : :obj:`~PointType`


    :Returns:

        :obj:`~bool`

