IArcAltitudeOptions
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.IArcAltitudeOptions

   object
   
   Interface used to access the altitude options for an Arc procedure.

.. py:currentmodule:: IArcAltitudeOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcAltitudeOptions.use_default_cruise_altitude`
              - Opt whether to use the default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcAltitudeOptions.start_arc_altitude`
              - Gets or sets the altitude at the beginning of the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcAltitudeOptions.stop_arc_altitude`
              - Gets or sets the altitude at the end of the arc.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IArcAltitudeOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IArcAltitudeOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: start_arc_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IArcAltitudeOptions.start_arc_altitude
    :type: float

    Gets or sets the altitude at the beginning of the arc.

.. py:property:: stop_arc_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IArcAltitudeOptions.stop_arc_altitude
    :type: float

    Gets or sets the altitude at the end of the arc.


