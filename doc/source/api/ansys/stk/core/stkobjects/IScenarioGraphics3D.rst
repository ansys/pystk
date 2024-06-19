IScenarioGraphics3D
===================

.. py:class:: IScenarioGraphics3D

   object
   
   Scenario 3D Graphics Attributes.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~available_marker_types`
              - Retrieve the list of available MarkerTypes.
            * - :py:meth:`~show_object`
              - Show the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 3d windows.
            * - :py:meth:`~show_objects`
              - Show multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 3d windows.
            * - :py:meth:`~hide_object`
              - Hides the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 3d windows.
            * - :py:meth:`~hide_objects`
              - Hides multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 3d windows.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~chunk_image_cache_size`
            * - :py:meth:`~is_negative_altitude_allowed`
            * - :py:meth:`~small_font`
            * - :py:meth:`~medium_font`
            * - :py:meth:`~large_font`
            * - :py:meth:`~surface_reference`
            * - :py:meth:`~draw_on_terrain`
            * - :py:meth:`~chunk_terrain_cache_size`
            * - :py:meth:`~text_outline_style`
            * - :py:meth:`~text_outline_color`
            * - :py:meth:`~text_antialiasing_enabled`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioGraphics3D


Property detail
---------------

.. py:property:: chunk_image_cache_size
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.chunk_image_cache_size
    :type: int

    Chunk image cache size (MB). The texture cache temporarily stores chunk imagery for the globe. You may need to increase the size of the cache if all specified terrain cannot be loaded at the same time or the terrain is blurry.

.. py:property:: is_negative_altitude_allowed
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.is_negative_altitude_allowed
    :type: bool

    Specify whether to allow negative altitudes for great arc vehicles and for facilities, places and targets.

.. py:property:: small_font
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.small_font
    :type: IAgSc3dFont

    Retrieves small font metrics.

.. py:property:: medium_font
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.medium_font
    :type: IAgSc3dFont

    Retrieves medium font metrics.

.. py:property:: large_font
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.large_font
    :type: IAgSc3dFont

    Retrieves large font metrics.

.. py:property:: surface_reference
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.surface_reference
    :type: SURFACE_REFERENCE

    Opt to display the globe's surface at the mean sea level (MSL) or at the central body's reference ellipsoid (WGS84).

.. py:property:: draw_on_terrain
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.draw_on_terrain
    :type: bool

    If true, lines drawn on the globe such as those that define area and line targets, range rings, vehicle paths, map details, etc. will conform to the terrain on the globe. Otherwise, if terrain is present, the lines may go under or float over the terrain.

.. py:property:: chunk_terrain_cache_size
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.chunk_terrain_cache_size
    :type: int

    Chunk terrain cache size (MB).

.. py:property:: text_outline_style
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.text_outline_style
    :type: TEXT_OUTLINE_STYLE

    Default text outline style.

.. py:property:: text_outline_color
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.text_outline_color
    :type: agcolor.Color

    Default text outline color.

.. py:property:: text_antialiasing_enabled
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.text_antialiasing_enabled
    :type: bool

    True if the text anti-aliasing is turned on.


Method detail
-------------




















.. py:method:: available_marker_types(self) -> list
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.available_marker_types

    Retrieve the list of available MarkerTypes.

    :Returns:

        :obj:`~list`

.. py:method:: show_object(self, truncPath: str, windowID: str) -> None
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.show_object

    Show the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 3d windows.

    :Parameters:

    **truncPath** : :obj:`~str`
    **windowID** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: show_objects(self, truncObjectPaths: list, windowIdOrTitle: str) -> None
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.show_objects

    Show multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 3d windows.

    :Parameters:

    **truncObjectPaths** : :obj:`~list`
    **windowIdOrTitle** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: hide_object(self, truncPath: str, windowID: str) -> None
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.hide_object

    Hides the object identified by its path in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 3d windows.

    :Parameters:

    **truncPath** : :obj:`~str`
    **windowID** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: hide_objects(self, truncObjectPaths: list, windowIdOrTitle: str) -> None
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics3D.hide_objects

    Hides multiple objects in a specified 3D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 3d windows.

    :Parameters:

    **truncObjectPaths** : :obj:`~list`
    **windowIdOrTitle** : :obj:`~str`

    :Returns:

        :obj:`~None`

