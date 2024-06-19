IAntennaGraphics
================

.. py:class:: IAntennaGraphics

   object
   
   IAgAntennaGraphics Interface for a antenna's 2D Graphics properties.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics.show
    :type: bool

    Opt whether to display graphics for the antenna object.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the antenna.

.. py:property:: boresight_color
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics.boresight_color
    :type: agcolor.Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics.contour_graphics
    :type: IAgAntennaContourGraphics

    Gets the antenna contour graphics interface.


