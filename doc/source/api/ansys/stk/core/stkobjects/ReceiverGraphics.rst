ReceiverGraphics
================

.. py:class:: ansys.stk.core.stkobjects.ReceiverGraphics

   Class defining 2D Graphics properties of a Receiver.

.. py:currentmodule:: ReceiverGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics.show`
              - Opt whether to display graphics for the receiver object.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics.show_boresight`
              - Opt whether to display boresight graphics for the receiver's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics.boresight_color`
              - The color in which boresight graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics.boresight_marker_style`
              - The marker style used to represent the boresight graphically.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics.contour_graphics`
              - Get the receiver's antenna contour graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReceiverGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics.show
    :type: bool

    Opt whether to display graphics for the receiver object.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the receiver's antenna.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics.contour_graphics
    :type: AntennaContourGraphics

    Get the receiver's antenna contour graphics interface.


