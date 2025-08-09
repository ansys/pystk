AircraftBasicFixedWingAerodynamic
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic

   Class defining the basic fixed wing aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftBasicFixedWingAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_reference_area`
              - Get or set the area of the lifting surface of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_use_compressible_flow`
              - Opt to define the aerodynamic parameters for forward flight with respect to supersonic flight conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_cl0`
              - Get or set the coefficient of lift at zero angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_cl_alpha`
              - Get or set the slope of the coefficient of lift curve.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_min_aoa`
              - Get or set the minimum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_max_aoa`
              - Get or set the maximum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_cd0`
              - Get or set the coefficient of drag of the lifting surface at zero angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_k`
              - Get or set the coefficient of induced drag.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_reference_area`
              - Get or set the area of the lifting surface of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_use_compressible_flow`
              - Opt to define the aerodynamic parameters for takeoff and landing with respect to supersonic flight conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_cl0`
              - Get or set the coefficient of lift at zero angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_cl_alpha`
              - Get or set the slope of the coefficient of lift curve.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_min_aoa`
              - Get or set the minimum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_max_aoa`
              - Get or set the maximum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_cd0`
              - Get or set the coefficient of drag of the lifting surface at zero angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_k`
              - Get or set the coefficient of induced drag.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicFixedWingAerodynamic


Property detail
---------------

.. py:property:: forward_flight_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_reference_area
    :type: float

    Get or set the area of the lifting surface of the aircraft.

.. py:property:: forward_flight_use_compressible_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_use_compressible_flow
    :type: bool

    Opt to define the aerodynamic parameters for forward flight with respect to supersonic flight conditions.

.. py:property:: forward_flight_cl0
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_cl0
    :type: float

    Get or set the coefficient of lift at zero angle of attack.

.. py:property:: forward_flight_cl_alpha
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_cl_alpha
    :type: float

    Get or set the slope of the coefficient of lift curve.

.. py:property:: forward_flight_min_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_min_aoa
    :type: typing.Any

    Get or set the minimum angle of attack possible.

.. py:property:: forward_flight_max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_max_aoa
    :type: typing.Any

    Get or set the maximum angle of attack possible.

.. py:property:: forward_flight_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_cd0
    :type: float

    Get or set the coefficient of drag of the lifting surface at zero angle of attack.

.. py:property:: forward_flight_k
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.forward_flight_k
    :type: float

    Get or set the coefficient of induced drag.

.. py:property:: takeoff_landing_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_reference_area
    :type: float

    Get or set the area of the lifting surface of the aircraft.

.. py:property:: takeoff_landing_use_compressible_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_use_compressible_flow
    :type: bool

    Opt to define the aerodynamic parameters for takeoff and landing with respect to supersonic flight conditions.

.. py:property:: takeoff_landing_cl0
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_cl0
    :type: float

    Get or set the coefficient of lift at zero angle of attack.

.. py:property:: takeoff_landing_cl_alpha
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_cl_alpha
    :type: float

    Get or set the slope of the coefficient of lift curve.

.. py:property:: takeoff_landing_min_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_min_aoa
    :type: typing.Any

    Get or set the minimum angle of attack possible.

.. py:property:: takeoff_landing_max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_max_aoa
    :type: typing.Any

    Get or set the maximum angle of attack possible.

.. py:property:: takeoff_landing_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_cd0
    :type: float

    Get or set the coefficient of drag of the lifting surface at zero angle of attack.

.. py:property:: takeoff_landing_k
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic.takeoff_landing_k
    :type: float

    Get or set the coefficient of induced drag.


