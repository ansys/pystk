ISensorGraphics
===============

.. py:class:: ansys.stk.core.stkobjects.ISensorGraphics

   object
   
   IAgSnGraphics Interface for a sensor's 2D Graphics properties.

.. py:currentmodule:: ISensorGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.inherit_from_scenario`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.enable`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.line_style`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.line_width`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.enable_boresight_graphics_2d`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.boresight_color`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.boresight_marker_style`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.projection`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.fill_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.percent_translucency`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics.is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorGraphics


Property detail
---------------

.. py:property:: inherit_from_scenario
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.inherit_from_scenario
    :type: bool

    Opt whether sensor 2D graphics are to be inherited from Scenario-level settings.

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.enable
    :type: bool

    If not inherited from Scenario-level settings, opt whether to display sensor 2D graphics.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.color
    :type: agcolor.Color

    The color in which sensor graphics display.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.line_style
    :type: LINE_STYLE

    Select the line style in which sensor 2D graphics display from the AgELineStyle enumeration.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.line_width
    :type: LINE_WIDTH

    Select the line width in which sensor 2D graphics display from the AgELineWidth enumeration.

.. py:property:: enable_boresight_graphics_2d
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.enable_boresight_graphics_2d
    :type: bool

    Opt whether to display boresight graphics for the sensor.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: projection
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.projection
    :type: ISensorProjection

    Get the 2D Projection properties of the sensor.

.. py:property:: fill_visible
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.fill_visible
    :type: bool

    Opt whether to display the region covered by the sensor footprint as a filled area.

.. py:property:: percent_translucency
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.percent_translucency
    :type: float

    Specify the percent translucency of the sensor projection. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the sensor are visible.


