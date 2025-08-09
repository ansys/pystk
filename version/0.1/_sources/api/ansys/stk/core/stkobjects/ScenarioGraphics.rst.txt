ScenarioGraphics
================

.. py:class:: ansys.stk.core.stkobjects.ScenarioGraphics

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

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_label`
              - Specify whether to show labels of objects on the 2D map (general).
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_sensors`
              - Specify whether to show sensors on the 2D map.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_lines_are_visible`
              - Specify whether to display lines during animation between objects participating in an access.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_animation_highlights`
              - Specify whether to display access animation highlights, i.e. boxes around objects participating in an access.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.access_static_highlights`
              - Specify whether to display access static highlights, i.e. thick lines overlying the ground track of a vehicle during access periods.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_ground_tracks`
              - Specify whether to display vehicle ground tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_ground_markers`
              - Specify whether to display vehicle ground markers.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_orbits`
              - Specify whether to display satellite orbits and trajectories of missiles and launch vehicles.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_orbit_markers`
              - Specify whether to display satellite orbit markers and missile and launch vehicle trajectory markers.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_element_set_number`
              - Specify whether to display satellite elset numbers.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_area_target_centroids`
              - Specify whether to display area target centroids.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_planet_orbits`
              - Specify whether to display planetary orbits.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_inertial_position`
              - Specify whether to display the inertial positions of planets.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_inertial_position_labels`
              - Specify whether to display labels at the inertial positions of planets.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_sub_planet_points`
              - Specify whether to display sub-planet points.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.show_sub_planet_labels`
              - Specify whether to display labels for sub-planet points.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGraphics.allow_animation_update`
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

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_label
    :type: bool

    Specify whether to show labels of objects on the 2D map (general).

.. py:property:: show_sensors
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_sensors
    :type: bool

    Specify whether to show sensors on the 2D map.

.. py:property:: access_lines_are_visible
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_lines_are_visible
    :type: bool

    Specify whether to display lines during animation between objects participating in an access.

.. py:property:: access_animation_highlights
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_animation_highlights
    :type: bool

    Specify whether to display access animation highlights, i.e. boxes around objects participating in an access.

.. py:property:: access_static_highlights
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.access_static_highlights
    :type: bool

    Specify whether to display access static highlights, i.e. thick lines overlying the ground track of a vehicle during access periods.

.. py:property:: show_ground_tracks
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_ground_tracks
    :type: bool

    Specify whether to display vehicle ground tracks.

.. py:property:: show_ground_markers
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_ground_markers
    :type: bool

    Specify whether to display vehicle ground markers.

.. py:property:: show_orbits
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_orbits
    :type: bool

    Specify whether to display satellite orbits and trajectories of missiles and launch vehicles.

.. py:property:: show_orbit_markers
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_orbit_markers
    :type: bool

    Specify whether to display satellite orbit markers and missile and launch vehicle trajectory markers.

.. py:property:: show_element_set_number
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_element_set_number
    :type: bool

    Specify whether to display satellite elset numbers.

.. py:property:: show_area_target_centroids
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_area_target_centroids
    :type: bool

    Specify whether to display area target centroids.

.. py:property:: show_planet_orbits
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_planet_orbits
    :type: bool

    Specify whether to display planetary orbits.

.. py:property:: show_inertial_position
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_inertial_position
    :type: bool

    Specify whether to display the inertial positions of planets.

.. py:property:: show_inertial_position_labels
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_inertial_position_labels
    :type: bool

    Specify whether to display labels at the inertial positions of planets.

.. py:property:: show_sub_planet_points
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_sub_planet_points
    :type: bool

    Specify whether to display sub-planet points.

.. py:property:: show_sub_planet_labels
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_sub_planet_labels
    :type: bool

    Specify whether to display labels for sub-planet points.

.. py:property:: allow_animation_update
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.allow_animation_update
    :type: bool

    Specify whether to allow animation updates.

.. py:property:: text_outline_style
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.text_outline_style
    :type: TextOutlineStyle

    Default text outline style.

.. py:property:: text_outline_color
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.text_outline_color
    :type: Color

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







































.. py:method:: show_object(self, trunc_path: str, window_id: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_object

    Show the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the object in all 2d windows.

    :Parameters:

        **trunc_path** : :obj:`~str`

        **window_id** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: show_objects(self, trunc_object_paths: list, window_id_or_title: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.show_objects

    Show multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to show the objects in all 2d windows.

    :Parameters:

        **trunc_object_paths** : :obj:`~list`

        **window_id_or_title** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: hide_object(self, trunc_path: str, window_id: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.hide_object

    Hides the object identified by its path in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide the object in all 2d windows.

    :Parameters:

        **trunc_path** : :obj:`~str`

        **window_id** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: hide_objects(self, trunc_object_paths: list, window_id_or_title: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioGraphics.hide_objects

    Hides multiple objects in a specified 2D window. Users can specify either a window identifier or a window title or 'all' to hide objects in all 2d windows.

    :Parameters:

        **trunc_object_paths** : :obj:`~list`

        **window_id_or_title** : :obj:`~str`


    :Returns:

        :obj:`~None`





