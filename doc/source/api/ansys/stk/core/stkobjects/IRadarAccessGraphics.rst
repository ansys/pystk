IRadarAccessGraphics
====================

.. py:class:: IRadarAccessGraphics

   object
   
   IAgRadarAccessGraphics Interface for a radar's access graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show_snr_contour`
            * - :py:meth:`~snr_contour_type`
            * - :py:meth:`~snr`
            * - :py:meth:`~radar_to_tgt_color`
            * - :py:meth:`~show_bistatic_rdr_to_target`
            * - :py:meth:`~bistatic_rdr_to_target_color`
            * - :py:meth:`~bistatic_rdr_to_target_line_style`
            * - :py:meth:`~bistatic_rdr_to_target_line_width`
            * - :py:meth:`~show_bistatic_xmtr_to_bistatic_rcvr`
            * - :py:meth:`~bistatic_xmtr_to_bistatic_rcvr_color`
            * - :py:meth:`~bistatic_xmtr_to_bistatic_rcvr_line_style`
            * - :py:meth:`~bistatic_xmtr_to_bistatic_rcvr_line_width`
            * - :py:meth:`~show_clutter`
            * - :py:meth:`~clutter_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarAccessGraphics


Property detail
---------------

.. py:property:: show_snr_contour
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.show_snr_contour
    :type: bool

    Opt whether to display graphics for the SNR contour.

.. py:property:: snr_contour_type
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.snr_contour_type
    :type: "RADAR_SNR_CONTOUR_TYPE"

    Gets or sets the SNR contour type.

.. py:property:: snr
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.snr
    :type: float

    Gets or sets the SNR.

.. py:property:: radar_to_tgt_color
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.radar_to_tgt_color
    :type: agcolor.Color

    Gets or sets the Radar to Target access color.

.. py:property:: show_bistatic_rdr_to_target
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.show_bistatic_rdr_to_target
    :type: bool

    Gets or sets the option for showing Bistatic Radar to Target graphics.

.. py:property:: bistatic_rdr_to_target_color
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.bistatic_rdr_to_target_color
    :type: agcolor.Color

    Gets or sets the Bistatic Radar to Target color.

.. py:property:: bistatic_rdr_to_target_line_style
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.bistatic_rdr_to_target_line_style
    :type: "LINE_STYLE"

    Gets or sets the AgELineStyle enumeration for the Bistatic Radar to Target.

.. py:property:: bistatic_rdr_to_target_line_width
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.bistatic_rdr_to_target_line_width
    :type: "LINE_WIDTH"

    Gets or sets the AgELineWidth enumeration for the Bistatic Radar to Target.

.. py:property:: show_bistatic_xmtr_to_bistatic_rcvr
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.show_bistatic_xmtr_to_bistatic_rcvr
    :type: bool

    Gets or sets the option for showing Bistatic Radar Transmitter to Bistatic Radar Receiver graphics.

.. py:property:: bistatic_xmtr_to_bistatic_rcvr_color
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.bistatic_xmtr_to_bistatic_rcvr_color
    :type: agcolor.Color

    Gets or sets the Bistatic Radar Transmitter to Bistatic Radar Receiver color.

.. py:property:: bistatic_xmtr_to_bistatic_rcvr_line_style
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.bistatic_xmtr_to_bistatic_rcvr_line_style
    :type: "LINE_STYLE"

    Gets or sets the AgELineStyle enumeration for the Bistatic Radar Transmitter to Bistatic Radar Receiver.

.. py:property:: bistatic_xmtr_to_bistatic_rcvr_line_width
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.bistatic_xmtr_to_bistatic_rcvr_line_width
    :type: "LINE_WIDTH"

    Gets or sets the AgELineWidth enumeration for the Bistatic Radar Transmitter to Bistatic Radar Receiver.

.. py:property:: show_clutter
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.show_clutter
    :type: bool

    Gets or set the option for showing clutter graphics.

.. py:property:: clutter_color
    :canonical: ansys.stk.core.stkobjects.IRadarAccessGraphics.clutter_color
    :type: agcolor.Color

    Gets or sets the clutter color.


