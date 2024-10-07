MtoGraphics2DFadeTimes
======================

.. py:class:: ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes

   MTO track fade times.

.. py:currentmodule:: MtoGraphics2DFadeTimes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.use_pre_fade`
              - Opt whether to display the track before the time of its first point. Otherwise, the track will always be displayed when the current animation time is before the first point's time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.pre_fade_time`
              - Gets or sets the amount of time before the start time that the track will appear. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.use_post_fade`
              - Opt whether to display the track after the last point's stop time. Otherwise, the track will always be displayed when the current animation time is after the last point's time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.post_fade_time`
              - Gets or sets the amount of time after the stop time that the line will continue to appear. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoGraphics2DFadeTimes


Property detail
---------------

.. py:property:: use_pre_fade
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.use_pre_fade
    :type: bool

    Opt whether to display the track before the time of its first point. Otherwise, the track will always be displayed when the current animation time is before the first point's time.

.. py:property:: pre_fade_time
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.pre_fade_time
    :type: float

    Gets or sets the amount of time before the start time that the track will appear. Uses Time Dimension.

.. py:property:: use_post_fade
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.use_post_fade
    :type: bool

    Opt whether to display the track after the last point's stop time. Otherwise, the track will always be displayed when the current animation time is after the last point's time.

.. py:property:: post_fade_time
    :canonical: ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes.post_fade_time
    :type: float

    Gets or sets the amount of time after the stop time that the line will continue to appear. Uses Time Dimension.


