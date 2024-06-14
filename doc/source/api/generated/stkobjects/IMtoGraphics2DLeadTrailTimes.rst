IMtoGraphics2DLeadTrailTimes
============================

.. py:class:: IMtoGraphics2DLeadTrailTimes

   object
   
   MTO track lead/trail times interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_lead_trail`
            * - :py:meth:`~lead_time`
            * - :py:meth:`~trail_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics2DLeadTrailTimes


Property detail
---------------

.. py:property:: use_lead_trail
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLeadTrailTimes.use_lead_trail
    :type: bool

    Opt whether to use lead and trail times.

.. py:property:: lead_time
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLeadTrailTimes.lead_time
    :type: float

    Gets or sets the time of the interpolated track route that will be displayed ahead of the track. Uses Time Dimension.

.. py:property:: trail_time
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLeadTrailTimes.trail_time
    :type: float

    Gets or sets the time of the interpolated track route that will be displayed behind the track. Uses Time Dimension.


