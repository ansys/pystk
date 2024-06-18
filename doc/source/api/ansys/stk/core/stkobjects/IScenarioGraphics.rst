IScenarioGraphics
=================

.. py:class:: IScenarioGraphics

   object
   
   IAgScGraphics Interface for Scenario-level 2D Graphics attributes.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show_object`
              - Show the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 2d windows.
            * - :py:meth:`~show_objects`
              - Show multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 2d windows.
            * - :py:meth:`~hide_object`
              - Hides the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 2d windows.
            * - :py:meth:`~hide_objects`
              - Hides multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 2d windows.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~labels_visible`
            * - :py:meth:`~sensors_visible`
            * - :py:meth:`~access_lines_visible`
            * - :py:meth:`~access_anim_high`
            * - :py:meth:`~access_stat_high`
            * - :py:meth:`~gnd_tracks_visible`
            * - :py:meth:`~gnd_markers_visible`
            * - :py:meth:`~orbits_visible`
            * - :py:meth:`~orbit_markers_visible`
            * - :py:meth:`~elset_num_visible`
            * - :py:meth:`~centroids_visible`
            * - :py:meth:`~planet_orbits_visible`
            * - :py:meth:`~inertial_position_visible`
            * - :py:meth:`~inertial_position_labels_visible`
            * - :py:meth:`~sub_planet_points_visible`
            * - :py:meth:`~sub_planet_labels_visible`
            * - :py:meth:`~allow_anim_update`
            * - :py:meth:`~text_outline_style`
            * - :py:meth:`~text_outline_color`
            * - :py:meth:`~access_lines_width`
            * - :py:meth:`~access_line_style`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioGraphics


Property detail
---------------

.. py:property:: labels_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.labels_visible
    :type: bool

    Specify whether to show labels of objects on the 2D map (general).

.. py:property:: sensors_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.sensors_visible
    :type: bool

    Specify whether to show sensors on the 2D map.

.. py:property:: access_lines_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.access_lines_visible
    :type: bool

    Specify whether to display lines during animation between objects participating in an access.

.. py:property:: access_anim_high
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.access_anim_high
    :type: bool

    Specify whether to display access animation highlights, i.e. boxes around objects participating in an access.

.. py:property:: access_stat_high
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.access_stat_high
    :type: bool

    Specify whether to display access static highlights, i.e. thick lines overlying the ground track of a vehicle during access periods.

.. py:property:: gnd_tracks_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.gnd_tracks_visible
    :type: bool

    Specify whether to display vehicle ground tracks.

.. py:property:: gnd_markers_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.gnd_markers_visible
    :type: bool

    Specify whether to display vehicle ground markers.

.. py:property:: orbits_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.orbits_visible
    :type: bool

    Specify whether to display satellite orbits and trajectories of missiles and launch vehicles.

.. py:property:: orbit_markers_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.orbit_markers_visible
    :type: bool

    Specify whether to display satellite orbit markers and missile and launch vehicle trajectory markers.

.. py:property:: elset_num_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.elset_num_visible
    :type: bool

    Specify whether to display satellite elset numbers.

.. py:property:: centroids_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.centroids_visible
    :type: bool

    Specify whether to display area target centroids.

.. py:property:: planet_orbits_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.planet_orbits_visible
    :type: bool

    Specify whether to display planetary orbits.

.. py:property:: inertial_position_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.inertial_position_visible
    :type: bool

    Specify whether to display the inertial positions of planets.

.. py:property:: inertial_position_labels_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.inertial_position_labels_visible
    :type: bool

    Specify whether to display labels at the inertial positions of planets.

.. py:property:: sub_planet_points_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.sub_planet_points_visible
    :type: bool

    Specify whether to display sub-planet points.

.. py:property:: sub_planet_labels_visible
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.sub_planet_labels_visible
    :type: bool

    Specify whether to display labels for sub-planet points.

.. py:property:: allow_anim_update
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.allow_anim_update
    :type: bool

    Specify whether to allow animation updates.

.. py:property:: text_outline_style
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.text_outline_style
    :type: "TEXT_OUTLINE_STYLE"

    Default text outline style.

.. py:property:: text_outline_color
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.text_outline_color
    :type: agcolor.Color

    Default text outline color.

.. py:property:: access_lines_width
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.access_lines_width
    :type: int

    Line width of lines between objects participating in an access.

.. py:property:: access_line_style
    :canonical: ansys.stk.core.stkobjects.IScenarioGraphics.access_line_style
    :type: str

    Line style of lines between objects participating in an access.


Method detail
-------------







































.. py:method:: show_object(self, truncPath:str, windowID:str) -> None

    Show the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 2d windows.

    :Parameters:

    **truncPath** : :obj:`~str`
    **windowID** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: show_objects(self, truncObjectPaths:list, windowIdOrTitle:str) -> None

    Show multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 2d windows.

    :Parameters:

    **truncObjectPaths** : :obj:`~list`
    **windowIdOrTitle** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: hide_object(self, truncPath:str, windowID:str) -> None

    Hides the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 2d windows.

    :Parameters:

    **truncPath** : :obj:`~str`
    **windowID** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: hide_objects(self, truncObjectPaths:list, windowIdOrTitle:str) -> None

    Hides multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 2d windows.

    :Parameters:

    **truncObjectPaths** : :obj:`~list`
    **windowIdOrTitle** : :obj:`~str`

    :Returns:

        :obj:`~None`





