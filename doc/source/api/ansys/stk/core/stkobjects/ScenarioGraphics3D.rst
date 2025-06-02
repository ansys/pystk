ScenarioGraphics3D
==================

.. py:class:: ansys.stk.core.stkobjects.ScenarioGraphics3D

   Class defining 3D Graphics properties of the Scenario.

.. py:currentmodule:: ScenarioGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.available_marker_types`
              - Retrieve the list of available MarkerTypes.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.show_object`
              - Show the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 3d windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.show_objects`
              - Show multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 3d windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.hide_object`
              - Hides the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 3d windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.hide_objects`
              - Hides multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 3d windows.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.chunk_image_cache_size`
              - Chunk image cache size (MB). The texture cache temporarily stores chunk imagery for the globe. You may need to increase the size of the cache if all specified terrain cannot be loaded at the same time or the terrain is blurry.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.is_negative_altitude_allowed`
              - Specify whether to allow negative altitudes for great arc vehicles and for facilities, places and targets.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.small_font`
              - Retrieve small font metrics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.medium_font`
              - Retrieve medium font metrics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.large_font`
              - Retrieve large font metrics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.surface_reference`
              - Opt to display the globe's surface at the mean sea level (MSL) or at the central body's reference ellipsoid (WGS84).
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.draw_on_terrain`
              - If true, lines drawn on the globe such as those that define area and line targets, range rings, vehicle paths, map details, etc. will conform to the terrain on the globe. Otherwise, if terrain is present, the lines may go under or float over the terrain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.chunk_terrain_cache_size`
              - Chunk terrain cache size (MB).
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.text_outline_style`
              - Default text outline style.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.text_outline_color`
              - Default text outline color.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics3D.text_anti_aliasing_enabled`
              - True if the text anti-aliasing is turned on.



Examples
--------

Change the scenario font

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    scenario = root.current_scenario
    scenario.graphics_3d.medium_font.name = "Arial"
    scenario.graphics_3d.medium_font.point_size = 18
    scenario.graphics_3d.medium_font.bold = True
    scenario.graphics_3d.medium_font.italic = False


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioGraphics3D


Property detail
---------------

.. py:property:: chunk_image_cache_size
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.chunk_image_cache_size
    :type: int

    Chunk image cache size (MB). The texture cache temporarily stores chunk imagery for the globe. You may need to increase the size of the cache if all specified terrain cannot be loaded at the same time or the terrain is blurry.

.. py:property:: is_negative_altitude_allowed
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.is_negative_altitude_allowed
    :type: bool

    Specify whether to allow negative altitudes for great arc vehicles and for facilities, places and targets.

.. py:property:: small_font
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.small_font
    :type: Scenario3dFont

    Retrieve small font metrics.

.. py:property:: medium_font
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.medium_font
    :type: Scenario3dFont

    Retrieve medium font metrics.

.. py:property:: large_font
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.large_font
    :type: Scenario3dFont

    Retrieve large font metrics.

.. py:property:: surface_reference
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.surface_reference
    :type: SurfaceReference

    Opt to display the globe's surface at the mean sea level (MSL) or at the central body's reference ellipsoid (WGS84).

.. py:property:: draw_on_terrain
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.draw_on_terrain
    :type: bool

    If true, lines drawn on the globe such as those that define area and line targets, range rings, vehicle paths, map details, etc. will conform to the terrain on the globe. Otherwise, if terrain is present, the lines may go under or float over the terrain.

.. py:property:: chunk_terrain_cache_size
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.chunk_terrain_cache_size
    :type: int

    Chunk terrain cache size (MB).

.. py:property:: text_outline_style
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.text_outline_style
    :type: TextOutlineStyle

    Default text outline style.

.. py:property:: text_outline_color
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.text_outline_color
    :type: agcolor.Color

    Default text outline color.

.. py:property:: text_anti_aliasing_enabled
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.text_anti_aliasing_enabled
    :type: bool

    True if the text anti-aliasing is turned on.


Method detail
-------------




















.. py:method:: available_marker_types(self) -> list
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.available_marker_types

    Retrieve the list of available MarkerTypes.

    :Returns:

        :obj:`~list`

.. py:method:: show_object(self, trunc_path: str, window_id: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.show_object

    Show the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 3d windows.

    :Parameters:

        **trunc_path** : :obj:`~str`

        **window_id** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: show_objects(self, trunc_object_paths: list, window_id_or_title: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.show_objects

    Show multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 3d windows.

    :Parameters:

        **trunc_object_paths** : :obj:`~list`

        **window_id_or_title** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: hide_object(self, trunc_path: str, window_id: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.hide_object

    Hides the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 3d windows.

    :Parameters:

        **trunc_path** : :obj:`~str`

        **window_id** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: hide_objects(self, trunc_object_paths: list, window_id_or_title: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics3D.hide_objects

    Hides multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 3d windows.

    :Parameters:

        **trunc_object_paths** : :obj:`~list`

        **window_id_or_title** : :obj:`~str`


    :Returns:

        :obj:`~None`

