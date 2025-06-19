RadarGraphics
=============

.. py:class:: ansys.stk.core.stkobjects.RadarGraphics

   Class defining 2D Graphics properties of a Radar.

.. py:currentmodule:: RadarGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics.show`
              - Opt whether to display graphics for the radar object.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics.show_boresight`
              - Opt whether to display boresight graphics for the radar's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics.boresight_color`
              - The color in which boresight graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics.boresight_marker_style`
              - The marker style used to represent the boresight graphically.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics.contour_graphics`
              - Get the radar's antenna contour graphics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics.access`
              - Get the radar's access graphics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics.multipath`
              - Get the radar's multipath graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.RadarGraphics.show
    :type: bool

    Opt whether to display graphics for the radar object.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.RadarGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the radar's antenna.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.RadarGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.RadarGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: ansys.stk.core.stkobjects.RadarGraphics.contour_graphics
    :type: AntennaContourGraphics

    Get the radar's antenna contour graphics interface.

.. py:property:: access
    :canonical: ansys.stk.core.stkobjects.RadarGraphics.access
    :type: RadarAccessGraphics

    Get the radar's access graphics interface.

.. py:property:: multipath
    :canonical: ansys.stk.core.stkobjects.RadarGraphics.multipath
    :type: RadarMultipathGraphics

    Get the radar's multipath graphics interface.


