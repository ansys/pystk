AntennaGraphics
===============

.. py:class:: ansys.stk.core.stkobjects.AntennaGraphics

   Class defining 2D Graphics properties of a Antenna.

.. py:currentmodule:: AntennaGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaGraphics.show`
              - Opt whether to display graphics for the antenna object.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaGraphics.show_boresight`
              - Opt whether to display boresight graphics for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaGraphics.boresight_color`
              - The color in which boresight graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaGraphics.boresight_marker_style`
              - The marker style used to represent the boresight graphically.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaGraphics.contour_graphics`
              - Get the antenna contour graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.AntennaGraphics.show
    :type: bool

    Opt whether to display graphics for the antenna object.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.AntennaGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the antenna.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.AntennaGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.AntennaGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: ansys.stk.core.stkobjects.AntennaGraphics.contour_graphics
    :type: AntennaContourGraphics

    Get the antenna contour graphics interface.


