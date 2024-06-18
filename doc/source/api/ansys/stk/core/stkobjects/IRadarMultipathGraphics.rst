IRadarMultipathGraphics
=======================

.. py:class:: IRadarMultipathGraphics

   object
   
   IAgRadarMultipathGraphics Interface for a radar's multipath graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show_xmt_to_tgt_grp`
            * - :py:meth:`~xmt_to_tgt_grp_color`
            * - :py:meth:`~xmt_to_tgt_grp_marker_style`
            * - :py:meth:`~show_rcv_to_tgt_grp`
            * - :py:meth:`~rcv_to_tgt_grp_color`
            * - :py:meth:`~rcv_to_tgt_grp_marker_style`
            * - :py:meth:`~show_xmt_to_rcv_grp`
            * - :py:meth:`~xmt_to_rcv_grp_color`
            * - :py:meth:`~xmt_to_rcv_grp_marker_style`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarMultipathGraphics


Property detail
---------------

.. py:property:: show_xmt_to_tgt_grp
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.show_xmt_to_tgt_grp
    :type: bool

    Opt whether to display graphics for the transmit radar to the target ground reflection point.

.. py:property:: xmt_to_tgt_grp_color
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.xmt_to_tgt_grp_color
    :type: agcolor.Color

    Gets or sets the transmit radar to target ground reflection point color.

.. py:property:: xmt_to_tgt_grp_marker_style
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.xmt_to_tgt_grp_marker_style
    :type: str

    Gets or sets the transmit radar to target ground reflection point marker style.

.. py:property:: show_rcv_to_tgt_grp
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.show_rcv_to_tgt_grp
    :type: bool

    Opt whether to display graphics for the receive radar to the target ground reflection point.

.. py:property:: rcv_to_tgt_grp_color
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.rcv_to_tgt_grp_color
    :type: agcolor.Color

    Gets or sets the receive radar to target ground reflection point color.

.. py:property:: rcv_to_tgt_grp_marker_style
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.rcv_to_tgt_grp_marker_style
    :type: str

    Gets or sets the receive radar to target ground reflection point marker style.

.. py:property:: show_xmt_to_rcv_grp
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.show_xmt_to_rcv_grp
    :type: bool

    Opt whether to display graphics for the transmit radar to the receive radar ground reflection point.

.. py:property:: xmt_to_rcv_grp_color
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.xmt_to_rcv_grp_color
    :type: agcolor.Color

    Gets or sets the transmit radar to receive radar ground reflection point color.

.. py:property:: xmt_to_rcv_grp_marker_style
    :canonical: ansys.stk.core.stkobjects.IRadarMultipathGraphics.xmt_to_rcv_grp_marker_style
    :type: str

    Gets or sets the transmit radar to receive radar ground reflection point marker style.


