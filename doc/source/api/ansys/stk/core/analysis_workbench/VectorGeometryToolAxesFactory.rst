VectorGeometryToolAxesFactory
=============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory

   A Factory object to create axes.

.. py:currentmodule:: VectorGeometryToolAxesFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.create`
              - Create a VGT axes using specified name, description and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.is_type_supported`
              - Return true if the type is supported.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.create_plugin_from_display_name`
              - Create an axes component based on a COM axes plugin. For information how to implement and register VGT plugins, see.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.available_plugin_display_names`
              - An array of display names associated with available axes plugins. The elements of the array are strings. Display names are used to create VGT axes based on COM plugins using CreateAxesPluginFromDisplayName method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesFactory


Property detail
---------------

.. py:property:: available_plugin_display_names
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.available_plugin_display_names
    :type: list

    An array of display names associated with available axes plugins. The elements of the array are strings. Display names are used to create VGT axes based on COM plugins using CreateAxesPluginFromDisplayName method.


Method detail
-------------

.. py:method:: create(self, axes_name: str, description: str, axes_type: AxesType) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.create

    Create a VGT axes using specified name, description and type.

    :Parameters:

    **axes_name** : :obj:`~str`
    **description** : :obj:`~str`
    **axes_type** : :obj:`~AxesType`

    :Returns:

        :obj:`~IVectorGeometryToolAxes`

.. py:method:: is_type_supported(self, type: AxesType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

    **type** : :obj:`~AxesType`

    :Returns:

        :obj:`~bool`


.. py:method:: create_plugin_from_display_name(self, axes_name: str, description: str, display_name: str) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory.create_plugin_from_display_name

    Create an axes component based on a COM axes plugin. For information how to implement and register VGT plugins, see.

    :Parameters:

    **axes_name** : :obj:`~str`
    **description** : :obj:`~str`
    **display_name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolAxes`

