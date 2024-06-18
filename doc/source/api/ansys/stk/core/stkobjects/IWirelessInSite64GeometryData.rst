IWirelessInSite64GeometryData
=============================

.. py:class:: IWirelessInSite64GeometryData

   object
   
   Provide access to the properties and methods for geometry data for the Wireless InSite RT model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`
            * - :py:meth:`~projection_horizontal_datum`
            * - :py:meth:`~supported_building_height_data_attributes`
            * - :py:meth:`~building_height_data_attribute`
            * - :py:meth:`~building_height_reference_method`
            * - :py:meth:`~building_height_unit`
            * - :py:meth:`~override_geometry_tile_origin`
            * - :py:meth:`~geometry_tile_origin_latitude`
            * - :py:meth:`~geometry_tile_origin_longitude`
            * - :py:meth:`~use_terrain_data`
            * - :py:meth:`~terrain_extent_min_latitude`
            * - :py:meth:`~terrain_extent_max_latitude`
            * - :py:meth:`~terrain_extent_min_longitude`
            * - :py:meth:`~terrain_extent_max_longitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IWirelessInSite64GeometryData


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.filename
    :type: str

    Gets or sets the geometry data filename.

.. py:property:: projection_horizontal_datum
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.projection_horizontal_datum
    :type: "PROJECTION_HORIZONTAL_DATUM_TYPE"

    Gets or sets the projection / horizontal datum.

.. py:property:: supported_building_height_data_attributes
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.supported_building_height_data_attributes
    :type: list

    Get an array of supported building height data attributes.

.. py:property:: building_height_data_attribute
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.building_height_data_attribute
    :type: str

    Get or sets the building height data attribute.

.. py:property:: building_height_reference_method
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.building_height_reference_method
    :type: "BUILD_HEIGHT_REFERENCE_METHOD"

    Gets or sets the building height reference method.

.. py:property:: building_height_unit
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.building_height_unit
    :type: "BUILD_HEIGHT_UNIT"

    Gets or sets the building height unit.

.. py:property:: override_geometry_tile_origin
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.override_geometry_tile_origin
    :type: bool

    Gets or sets the option for overriding the geometry tile origin.

.. py:property:: geometry_tile_origin_latitude
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.geometry_tile_origin_latitude
    :type: typing.Any

    Gets or sets the geometry tile origin latitude.

.. py:property:: geometry_tile_origin_longitude
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.geometry_tile_origin_longitude
    :type: typing.Any

    Gets or sets the geometry tile origin longitude.

.. py:property:: use_terrain_data
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.use_terrain_data
    :type: bool

    Gets or sets the option for using terrain data.

.. py:property:: terrain_extent_min_latitude
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.terrain_extent_min_latitude
    :type: typing.Any

    Gets the terrain extent min latitude.

.. py:property:: terrain_extent_max_latitude
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.terrain_extent_max_latitude
    :type: typing.Any

    Gets the terrain extent max latitude.

.. py:property:: terrain_extent_min_longitude
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.terrain_extent_min_longitude
    :type: typing.Any

    Gets the terrain extent min longitude.

.. py:property:: terrain_extent_max_longitude
    :canonical: ansys.stk.core.stkobjects.IWirelessInSite64GeometryData.terrain_extent_max_longitude
    :type: typing.Any

    Gets the terrain extent max longitude.


