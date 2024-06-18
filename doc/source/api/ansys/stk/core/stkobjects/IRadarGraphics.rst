IRadarGraphics
==============

.. py:class:: IRadarGraphics

   object
   
   IAgRadarGraphics Interface for a radar's 2D Graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show`
            * - :py:meth:`~show_boresight`
            * - :py:meth:`~boresight_color`
            * - :py:meth:`~boresight_marker_style`
            * - :py:meth:`~contour_graphics`
            * - :py:meth:`~access`
            * - :py:meth:`~multipath`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics.show
    :type: bool

    Opt whether to display graphics for the radar object.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the radar's antenna.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics.contour_graphics
    :type: "IAgAntennaContourGraphics"

    Gets the radar's antenna contour graphics interface.

.. py:property:: access
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics.access
    :type: "IAgRadarAccessGraphics"

    Gets the radar's access graphics interface.

.. py:property:: multipath
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics.multipath
    :type: "IAgRadarMultipathGraphics"

    Gets the radar's multipath graphics interface.


