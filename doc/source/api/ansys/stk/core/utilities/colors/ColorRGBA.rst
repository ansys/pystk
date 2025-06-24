ColorRGBA
=========

.. py:class:: ansys.stk.core.utilities.colors.ColorRGBA

   object

   A variably translucent color representation that can be used with certain methods in the STK Object Model.

.. py:currentmodule:: ColorRGBA


Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.utilities.colors.ColorRGBA.alpha`
              - Gets or sets the ColorRGBA object's value for alpha, which ranges between 0 (fully translucent) and 255 (fully opaque).
            * - :py:attr:`~ansys.stk.core.utilities.colors.ColorRGBA.color`
              - The Color value that contains R, G, B values.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.utilities.colors import ColorRGBA


Property detail
---------------

.. py:property:: alpha
    :canonical: ansys.stk.core.utilities.colors.ColorRGBA.alpha
    :type: float

    Gets or sets the ColorRGBA object's value for alpha, which ranges between 0 (fully translucent) and 255 (fully opaque).

.. py:property:: color
    :canonical: ansys.stk.core.utilities.colors.ColorRGBA.color
    :type: Color

    The Color value that contains R, G, B values.


