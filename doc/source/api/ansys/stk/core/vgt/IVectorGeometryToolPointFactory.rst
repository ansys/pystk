IVectorGeometryToolPointFactory
===============================

.. py:class:: IVectorGeometryToolPointFactory

   object
   
   A Factory object to create points.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create a VGT point using the specified name, description and type.
            * - :py:meth:`~is_type_supported`
              - Return true if the type is supported.
            * - :py:meth:`~create_point_plugin_from_display_name`
              - Create a point component based on a COM point plugin. For information how to implement and register VGT plugins, see.
            * - :py:meth:`~create_point_fixed_on_central_body`
              - Create a point fixed on a central body.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~available_point_plugin_display_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointFactory


Property detail
---------------

.. py:property:: available_point_plugin_display_names
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointFactory.available_point_plugin_display_names
    :type: list

    An array of display names associated with available point plugins. The elements of the array are strings. Display names are used to create VGT points based on COM plugins using CreatePointPluginFromDisplayName method.


Method detail
-------------

.. py:method:: create(self, pointName:str, description:str, pointType:"VECTOR_GEOMETRY_TOOL_POINT_TYPE") -> "IVectorGeometryToolPoint"

    Create a VGT point using the specified name, description and type.

    :Parameters:

    **pointName** : :obj:`~str`
    **description** : :obj:`~str`
    **pointType** : :obj:`~"VECTOR_GEOMETRY_TOOL_POINT_TYPE"`

    :Returns:

        :obj:`~"IVectorGeometryToolPoint"`

.. py:method:: is_type_supported(self, type:"VECTOR_GEOMETRY_TOOL_POINT_TYPE") -> bool

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~"VECTOR_GEOMETRY_TOOL_POINT_TYPE"`

    :Returns:

        :obj:`~bool`


.. py:method:: create_point_plugin_from_display_name(self, pointName:str, description:str, displayName:str) -> "IVectorGeometryToolPoint"

    Create a point component based on a COM point plugin. For information how to implement and register VGT plugins, see.

    :Parameters:

    **pointName** : :obj:`~str`
    **description** : :obj:`~str`
    **displayName** : :obj:`~str`

    :Returns:

        :obj:`~"IVectorGeometryToolPoint"`

.. py:method:: create_point_fixed_on_central_body(self, pointName:str, description:str, longitude:typing.Any, latitude:typing.Any, altitude:float, referenceShape:"CRDN_REFERENCE_SHAPE_TYPE") -> "IVectorGeometryToolPoint"

    Create a point fixed on a central body.

    :Parameters:

    **pointName** : :obj:`~str`
    **description** : :obj:`~str`
    **longitude** : :obj:`~typing.Any`
    **latitude** : :obj:`~typing.Any`
    **altitude** : :obj:`~float`
    **referenceShape** : :obj:`~"CRDN_REFERENCE_SHAPE_TYPE"`

    :Returns:

        :obj:`~"IVectorGeometryToolPoint"`

