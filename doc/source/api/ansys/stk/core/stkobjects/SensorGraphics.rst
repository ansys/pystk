SensorGraphics
==============

.. py:class:: ansys.stk.core.stkobjects.SensorGraphics

   Class defining the 2D Graphics properties of a Sensor.

.. py:currentmodule:: SensorGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.inherit_from_scenario`
              - Opt whether sensor 2D graphics are to be inherited from Scenario-level settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.enable`
              - If not inherited from Scenario-level settings, opt whether to display sensor 2D graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.color`
              - The color in which sensor graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.line_style`
              - Select the line style in which sensor 2D graphics display from the LineStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.line_width`
              - Select the line width in which sensor 2D graphics display from the LineWidth enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.enable_boresight_graphics_2d`
              - Opt whether to display boresight graphics for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.boresight_color`
              - The color in which boresight graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.boresight_marker_style`
              - The marker style used to represent the boresight graphically.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.projection`
              - Get the 2D Projection properties of the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.show_fill`
              - Opt whether to display the region covered by the sensor footprint as a filled area.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.percent_translucency`
              - Specify the percent translucency of the sensor projection. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics.show_graphics`
              - Specify whether graphics attributes of the sensor are visible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorGraphics


Property detail
---------------

.. py:property:: inherit_from_scenario
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.inherit_from_scenario
    :type: bool

    Opt whether sensor 2D graphics are to be inherited from Scenario-level settings.

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.enable
    :type: bool

    If not inherited from Scenario-level settings, opt whether to display sensor 2D graphics.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.color
    :type: agcolor.Color

    The color in which sensor graphics display.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.line_style
    :type: LineStyle

    Select the line style in which sensor 2D graphics display from the LineStyle enumeration.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.line_width
    :type: LineWidth

    Select the line width in which sensor 2D graphics display from the LineWidth enumeration.

.. py:property:: enable_boresight_graphics_2d
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.enable_boresight_graphics_2d
    :type: bool

    Opt whether to display boresight graphics for the sensor.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: projection
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.projection
    :type: SensorProjection

    Get the 2D Projection properties of the sensor.

.. py:property:: show_fill
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.show_fill
    :type: bool

    Opt whether to display the region covered by the sensor footprint as a filled area.

.. py:property:: percent_translucency
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.percent_translucency
    :type: float

    Specify the percent translucency of the sensor projection. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.SensorGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the sensor are visible.


