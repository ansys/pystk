IArcAltitudeAndDelayOptions
===========================

.. py:class:: IArcAltitudeAndDelayOptions

   object
   
   Interface used to access the altitude options for an Arc procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_default_cruise_altitude`
            * - :py:meth:`~delay_arc_climb_descents`
            * - :py:meth:`~start_arc_altitude`
            * - :py:meth:`~stop_arc_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IArcAltitudeAndDelayOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IArcAltitudeAndDelayOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: delay_arc_climb_descents
    :canonical: ansys.stk.core.stkobjects.aviator.IArcAltitudeAndDelayOptions.delay_arc_climb_descents
    :type: bool

    Delay the climb/descend such that the stop arc altitude will be achieved by the end of the procedure.

.. py:property:: start_arc_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IArcAltitudeAndDelayOptions.start_arc_altitude
    :type: float

    Gets or sets the altitude at the beginning of the arc.

.. py:property:: stop_arc_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IArcAltitudeAndDelayOptions.stop_arc_altitude
    :type: float

    Gets or sets the altitude at the end of the arc.


