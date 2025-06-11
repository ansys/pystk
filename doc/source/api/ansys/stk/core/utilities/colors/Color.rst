Color
=====

.. py:class:: ansys.stk.core.utilities.colors.Color

   object

   An opaque color representation that can be used with the STK Object Model.

   Examples
   --------
   Get and set a four-channel color for the graphics of an STK graphics primitive:
   >>> from ansys.stk.core.utilities.colors import Colors, ColorRGBA
   >>>
   >>> manager = root.current_scenario.scene_manager
   >>> point = manager.initializers.point_batch_primitive.initialize()
   >>>
   >>> lla_pts = [ 39.88, -75.25, 0,
   >>>             38.85, -77.04, 0,
   >>>             37.37, -121.92, 0 ]
   >>>
   >>> colors = [ Colors.Red,
   >>>         ColorRGBA(Colors.Blue, 127),
   >>>         Colors.from_rgba(0, 255, 0, 127) ]
   >>>
   >>> point.set_cartographic_with_colors('Earth', lla_pts, colors)

   Get and set a three-channel color for the graphics of an STK graphics primitive:
   >>> from ansys.stk.core.stkobjects import STKObjectType
   >>> from ansys.stk.core.utilities.colors import Color, Colors
   >>>
   >>> facility = root.current_scenario.children.new(STKObjectType.FACILITY, "facility1")
   >>>
   >>> facility.graphics.color = Colors.Blue
   >>> facility.graphics.color = Color.from_rgb(127, 255, 212)
   >>> (r, g, b) = facility.graphics.color.get_rgb()

.. py:currentmodule:: Color


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.utilities.colors.Color.from_rgb`
              - Create a new Color from R, G, B values.
            * - :py:attr:`~ansys.stk.core.utilities.colors.Color.get_rgb`
              - Return the R, G, B representation of this color.

Examples
--------

Get and set a four-channel color for the graphics of an STK graphics primitive

.. code-block:: python

    from ansys.stk.core.utilities.colors import Colors, ColorRGBA

    manager = root.current_scenario.scene_manager
    point = manager.initializers.point_batch_primitive.initialize()

    lla_pts = [39.88, -75.25, 0, 38.85, -77.04, 0, 37.37, -121.92, 0]

    colors = [Colors.Red, ColorRGBA(Colors.Blue, 127), Colors.from_rgba(0, 255, 0, 127)]

    point.set_cartographic_with_colors("Earth", lla_pts, colors)


Get and set a three-channel color for the graphics of an STK graphics primitive

.. code-block:: python

    from ansys.stk.core.stkobjects import STKObjectType
    from ansys.stk.core.utilities.colors import Color, Colors

    facility = root.current_scenario.children.new(STKObjectType.FACILITY, "facility1")

    facility.graphics.color = Colors.Blue
    facility.graphics.color = Color.from_rgb(127, 255, 212)
    (r, g, b) = facility.graphics.color.get_rgb()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.utilities.colors import Color


Method detail
-------------

.. py:method:: from_rgb(cls, r: int, g: int, b: int) -> None
    :canonical: ansys.stk.core.utilities.colors.Color.from_rgb

    Create a new Color from R, G, B values.

    :Parameters:

        **r** : :obj:`~int`

        **g** : :obj:`~int`

        **b** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: get_rgb(self)
    :canonical: ansys.stk.core.utilities.colors.Color.get_rgb

    Return the R, G, B representation of this color.


