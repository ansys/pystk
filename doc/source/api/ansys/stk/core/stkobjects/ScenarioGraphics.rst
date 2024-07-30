ScenarioGraphics
================

.. py:class:: ansys.stk.core.stkobjects.ScenarioGraphics

   Bases: 

   Class defining the 2D Graphics properties of a Scenario.

.. py:currentmodule:: ScenarioGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_object`
              - Show the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 2d windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_objects`
              - Show multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 2d windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.hide_object`
              - Hides the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 2d windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.hide_objects`
              - Hides multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 2d windows.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.labels_visible`
              - Specify whether to show labels of objects on the 2D map (general).
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.sensors_visible`
              - Specify whether to show sensors on the 2D map.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_lines_visible`
              - Specify whether to display lines during animation between objects participating in an access.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_anim_high`
              - Specify whether to display access animation highlights, i.e. boxes around objects participating in an access.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_stat_high`
              - Specify whether to display access static highlights, i.e. thick lines overlying the ground track of a vehicle during access periods.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.gnd_tracks_visible`
              - Specify whether to display vehicle ground tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.gnd_markers_visible`
              - Specify whether to display vehicle ground markers.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.orbits_visible`
              - Specify whether to display satellite orbits and trajectories of missiles and launch vehicles.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.orbit_markers_visible`
              - Specify whether to display satellite orbit markers and missile and launch vehicle trajectory markers.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.elset_num_visible`
              - Specify whether to display satellite elset numbers.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.centroids_visible`
              - Specify whether to display area target centroids.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.planet_orbits_visible`
              - Specify whether to display planetary orbits.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.inertial_position_visible`
              - Specify whether to display the inertial positions of planets.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.inertial_position_labels_visible`
              - Specify whether to display labels at the inertial positions of planets.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.sub_planet_points_visible`
              - Specify whether to display sub-planet points.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.sub_planet_labels_visible`
              - Specify whether to display labels for sub-planet points.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.allow_anim_update`
              - Specify whether to allow animation updates.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.text_outline_style`
              - Default text outline style.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.text_outline_color`
              - Default text outline color.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_lines_width`
              - Line width of lines between objects participating in an access.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_line_style`
              - Line style of lines between objects participating in an access.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioGraphics


Property detail
---------------

.. py:property:: labels_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.labels_visible
    :type: bool

    Specify whether to show labels of objects on the 2D map (general).

.. py:property:: sensors_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.sensors_visible
    :type: bool

    Specify whether to show sensors on the 2D map.

.. py:property:: access_lines_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_lines_visible
    :type: bool

    Specify whether to display lines during animation between objects participating in an access.

.. py:property:: access_anim_high
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_anim_high
    :type: bool

    Specify whether to display access animation highlights, i.e. boxes around objects participating in an access.

.. py:property:: access_stat_high
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_stat_high
    :type: bool

    Specify whether to display access static highlights, i.e. thick lines overlying the ground track of a vehicle during access periods.

.. py:property:: gnd_tracks_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.gnd_tracks_visible
    :type: bool

    Specify whether to display vehicle ground tracks.

.. py:property:: gnd_markers_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.gnd_markers_visible
    :type: bool

    Specify whether to display vehicle ground markers.

.. py:property:: orbits_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.orbits_visible
    :type: bool

    Specify whether to display satellite orbits and trajectories of missiles and launch vehicles.

.. py:property:: orbit_markers_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.orbit_markers_visible
    :type: bool

    Specify whether to display satellite orbit markers and missile and launch vehicle trajectory markers.

.. py:property:: elset_num_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.elset_num_visible
    :type: bool

    Specify whether to display satellite elset numbers.

.. py:property:: centroids_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.centroids_visible
    :type: bool

    Specify whether to display area target centroids.

.. py:property:: planet_orbits_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.planet_orbits_visible
    :type: bool

    Specify whether to display planetary orbits.

.. py:property:: inertial_position_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.inertial_position_visible
    :type: bool

    Specify whether to display the inertial positions of planets.

.. py:property:: inertial_position_labels_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.inertial_position_labels_visible
    :type: bool

    Specify whether to display labels at the inertial positions of planets.

.. py:property:: sub_planet_points_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.sub_planet_points_visible
    :type: bool

    Specify whether to display sub-planet points.

.. py:property:: sub_planet_labels_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.sub_planet_labels_visible
    :type: bool

    Specify whether to display labels for sub-planet points.

.. py:property:: allow_anim_update
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.allow_anim_update
    :type: bool

    Specify whether to allow animation updates.

.. py:property:: text_outline_style
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.text_outline_style
    :type: TEXT_OUTLINE_STYLE

    Default text outline style.

.. py:property:: text_outline_color
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.text_outline_color
    :type: agcolor.Color

    Default text outline color.

.. py:property:: access_lines_width
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_lines_width
    :type: int

    Line width of lines between objects participating in an access.

.. py:property:: access_line_style
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_line_style
    :type: str

    Line style of lines between objects participating in an access.


Method detail
-------------







































.. py:method:: show_object(self, truncPath: str, windowID: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_object

    Show the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 2d windows.

    :Parameters:

    **truncPath** : :obj:`~str`
    **windowID** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: show_objects(self, truncObjectPaths: list, windowIdOrTitle: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_objects

    Show multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 2d windows.

    :Parameters:

    **truncObjectPaths** : :obj:`~list`
    **windowIdOrTitle** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: hide_object(self, truncPath: str, windowID: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.hide_object

    Hides the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 2d windows.

    :Parameters:

    **truncPath** : :obj:`~str`
    **windowID** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: hide_objects(self, truncObjectPaths: list, windowIdOrTitle: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.hide_objects

    Hides multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 2d windows.

    :Parameters:

    **truncObjectPaths** : :obj:`~list`
    **windowIdOrTitle** : :obj:`~str`

    :Returns:

        :obj:`~None`





