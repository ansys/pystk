Colors
======

.. py:class:: ansys.stk.core.utilities.colors.Colors

   object

   A factory for creating Color objects that may be used with the STK object model.

   Contains factory methods and named colors.

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

.. py:currentmodule:: Colors


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.utilities.colors.Colors.from_rgb`
              - Create a new Color from R, G, B values in the range [0, 255].
            * - :py:attr:`~ansys.stk.core.utilities.colors.Colors.from_rgba`
              - Create a new Color from R, G, B, A values in the range [0, 255].
            * - :py:attr:`~ansys.stk.core.utilities.colors.Colors.from_argb`
              - Create a new Color from an arbitrary number of values in the range [0, 255], inferred from the arguments provided.

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

    from ansys.stk.core.utilities.colors import Colors


Method detail
-------------

.. py:method:: from_rgb(r: int, g: int, b: int) -> Color
    :canonical: ansys.stk.core.utilities.colors.Colors.from_rgb

    Create a new Color from R, G, B values in the range [0, 255].

    :Parameters:

        **r** : :obj:`~int`

        **g** : :obj:`~int`

        **b** : :obj:`~int`


    :Returns:

        :obj:`~Color`

.. py:method:: from_rgba(r: int, g: int, b: int, a: int) -> ColorRGBA
    :canonical: ansys.stk.core.utilities.colors.Colors.from_rgba

    Create a new Color from R, G, B, A values in the range [0, 255].

    :Parameters:

        **r** : :obj:`~int`

        **g** : :obj:`~int`

        **b** : :obj:`~int`

        **a** : :obj:`~int`


    :Returns:

        :obj:`~ColorRGBA`

.. py:method:: from_argb()
    :canonical: ansys.stk.core.utilities.colors.Colors.from_argb

    Create a new Color from an arbitrary number of values in the range [0, 255], inferred from the arguments provided.


