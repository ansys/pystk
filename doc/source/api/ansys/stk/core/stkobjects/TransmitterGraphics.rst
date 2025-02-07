TransmitterGraphics
===================

.. py:class:: ansys.stk.core.stkobjects.TransmitterGraphics

   Class defining 2D Graphics properties of a Transmitter.

.. py:currentmodule:: TransmitterGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics.show`
              - Opt whether to display graphics for the transmitter object.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics.show_boresight`
              - Opt whether to display boresight graphics for the transmitter's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics.boresight_color`
              - The color in which boresight graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics.boresight_marker_style`
              - The marker style used to represent the boresight graphically.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics.contour_graphics`
              - Get the transmitter's antenna contour graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransmitterGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics.show
    :type: bool

    Opt whether to display graphics for the transmitter object.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the transmitter's antenna.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics.contour_graphics
    :type: AntennaContourGraphics

    Get the transmitter's antenna contour graphics interface.


