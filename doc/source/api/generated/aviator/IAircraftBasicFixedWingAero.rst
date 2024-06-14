IAircraftBasicFixedWingAero
===========================

.. py:class:: IAircraftBasicFixedWingAero

   object
   
   Interface used to access Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~forward_flight_reference_area`
            * - :py:meth:`~forward_flight_use_compressible_flow`
            * - :py:meth:`~forward_flight_cl0`
            * - :py:meth:`~forward_flight_cl_alpha`
            * - :py:meth:`~forward_flight_min_aoa`
            * - :py:meth:`~forward_flight_max_aoa`
            * - :py:meth:`~forward_flight_cd0`
            * - :py:meth:`~forward_flight_k`
            * - :py:meth:`~takeoff_landing_reference_area`
            * - :py:meth:`~takeoff_landing_use_compressible_flow`
            * - :py:meth:`~takeoff_landing_cl0`
            * - :py:meth:`~takeoff_landing_cl_alpha`
            * - :py:meth:`~takeoff_landing_min_aoa`
            * - :py:meth:`~takeoff_landing_max_aoa`
            * - :py:meth:`~takeoff_landing_cd0`
            * - :py:meth:`~takeoff_landing_k`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftBasicFixedWingAero


Property detail
---------------

.. py:property:: forward_flight_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_reference_area
    :type: float

    Gets or sets the area of the lifting surface of the aircraft.

.. py:property:: forward_flight_use_compressible_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_use_compressible_flow
    :type: bool

    Opt to define the aerodynamic parameters for forward flight with respect to supersonic flight conditions.

.. py:property:: forward_flight_cl0
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_cl0
    :type: float

    Gets or sets the coefficient of lift at zero angle of attack.

.. py:property:: forward_flight_cl_alpha
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_cl_alpha
    :type: float

    Gets or sets the slope of the coefficient of lift curve.

.. py:property:: forward_flight_min_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_min_aoa
    :type: typing.Any

    Gets or sets the minimum angle of attack possible.

.. py:property:: forward_flight_max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_max_aoa
    :type: typing.Any

    Gets or sets the maximum angle of attack possible.

.. py:property:: forward_flight_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_cd0
    :type: float

    Gets or sets the coefficient of drag of the lifting surface at zero angle of attack.

.. py:property:: forward_flight_k
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.forward_flight_k
    :type: float

    Gets or sets the coefficient of induced drag.

.. py:property:: takeoff_landing_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_reference_area
    :type: float

    Gets or sets the area of the lifting surface of the aircraft.

.. py:property:: takeoff_landing_use_compressible_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_use_compressible_flow
    :type: bool

    Opt to define the aerodynamic parameters for takeoff and landing with respect to supersonic flight conditions.

.. py:property:: takeoff_landing_cl0
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_cl0
    :type: float

    Gets or sets the coefficient of lift at zero angle of attack.

.. py:property:: takeoff_landing_cl_alpha
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_cl_alpha
    :type: float

    Gets or sets the slope of the coefficient of lift curve.

.. py:property:: takeoff_landing_min_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_min_aoa
    :type: typing.Any

    Gets or sets the minimum angle of attack possible.

.. py:property:: takeoff_landing_max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_max_aoa
    :type: typing.Any

    Gets or sets the maximum angle of attack possible.

.. py:property:: takeoff_landing_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_cd0
    :type: float

    Gets or sets the coefficient of drag of the lifting surface at zero angle of attack.

.. py:property:: takeoff_landing_k
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicFixedWingAero.takeoff_landing_k
    :type: float

    Gets or sets the coefficient of induced drag.


