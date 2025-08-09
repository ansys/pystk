ArcAltitudeAndDelayOptions
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions

   Class defining the altitude and delay options for an arc procedure.

.. py:currentmodule:: ArcAltitudeAndDelayOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.use_default_cruise_altitude`
              - Opt whether to use the default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.delay_arc_climb_descents`
              - Delay the climb/descend such that the stop arc altitude will be achieved by the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.start_arc_altitude`
              - Get or set the altitude at the beginning of the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.stop_arc_altitude`
              - Get or set the altitude at the end of the arc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ArcAltitudeAndDelayOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: delay_arc_climb_descents
    :canonical: ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.delay_arc_climb_descents
    :type: bool

    Delay the climb/descend such that the stop arc altitude will be achieved by the end of the procedure.

.. py:property:: start_arc_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.start_arc_altitude
    :type: float

    Get or set the altitude at the beginning of the arc.

.. py:property:: stop_arc_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions.stop_arc_altitude
    :type: float

    Get or set the altitude at the end of the arc.


