IReceiverGraphics
=================

.. py:class:: ansys.stk.core.stkobjects.IReceiverGraphics

   object
   
   IAgReceiverGraphics Interface for a receiver's 2D Graphics properties.

.. py:currentmodule:: IReceiverGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics.show`
              - Opt whether to display graphics for the receiver object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics.show_boresight`
              - Opt whether to display boresight graphics for the receiver's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics.boresight_color`
              - The color in which boresight graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics.boresight_marker_style`
              - The marker style used to represent the boresight graphically.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics.contour_graphics`
              - Gets the receiver's antenna contour graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiverGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics.show
    :type: bool

    Opt whether to display graphics for the receiver object.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the receiver's antenna.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics.contour_graphics
    :type: IAntennaContourGraphics

    Gets the receiver's antenna contour graphics interface.


