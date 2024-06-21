IMtoGraphics2DFadeTimes
=======================

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes

   object
   
   MTO track fade times interface.

.. py:currentmodule:: IMtoGraphics2DFadeTimes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.use_pre_fade`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.pre_fade_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.use_post_fade`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.post_fade_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics2DFadeTimes


Property detail
---------------

.. py:property:: use_pre_fade
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.use_pre_fade
    :type: bool

    Opt whether to display the track before the time of its first point. Otherwise, the track will always be displayed when the current animation time is before the first point's time.

.. py:property:: pre_fade_time
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.pre_fade_time
    :type: float

    Gets or sets the amount of time before the start time that the track will appear. Uses Time Dimension.

.. py:property:: use_post_fade
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.use_post_fade
    :type: bool

    Opt whether to display the track after the last point's stop time. Otherwise, the track will always be displayed when the current animation time is after the last point's time.

.. py:property:: post_fade_time
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DFadeTimes.post_fade_time
    :type: float

    Gets or sets the amount of time after the stop time that the line will continue to appear. Uses Time Dimension.


