PropagatorHPOP
==============

.. py:class:: ansys.stk.core.stkobjects.PropagatorHPOP

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the High Precision Orbit Propagator (HPOP).

.. py:currentmodule:: PropagatorHPOP

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.initial_state`
              - Get the satellite's initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.force_model`
              - Get the force model parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.integrator`
              - Get the integrator parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.covariance`
              - Get the covariance parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.display_coordinate_type`
              - The propagator's display coordinate type.



Examples
--------

Set satellite propagator to HPOP and set force model properties

.. code-block:: python

    # Satellitesatellite: Satellite object
    satellite.set_propagator_type(PropagatorType.HPOP)
    satellite.propagator.step = 60
    satellite.propagator.initial_state.representation.assign_cartesian(
        CoordinateSystem.FIXED, 6406.92, -1787.59, -506.422, 2.10185, 6.48871, 3.64041
    )

    forceModel = satellite.propagator.force_model
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    forceModel.central_body_gravity.file = os.path.join(
        installPath, "STKData", "CentralBodies", "Earth", "WGS84_EGM96.grv"
    )
    forceModel.central_body_gravity.maximum_degree = 21
    forceModel.central_body_gravity.maximum_order = 21
    forceModel.drag.use = True
    forceModel.drag.drag_model.cd = 0.01
    forceModel.drag.drag_model.area_mass_ratio = 0.01
    forceModel.solar_radiation_pressure.use = False

    integrator = satellite.propagator.integrator
    integrator.do_not_propagate_below_altitude = -1e6
    integrator.integration_model = VehicleIntegrationModel.RUNGE_KUTTA_FEHLBERG_78
    integrator.step_size_control.method = VehicleMethod.RELATIVE_ERROR
    integrator.step_size_control.error_tolerance = 1e-13
    integrator.step_size_control.minimum_step_size = 0.1
    integrator.step_size_control.maximum_step_size = 30
    integrator.interpolation.method = VehicleInterpolationMethod.LAGRANGE
    integrator.interpolation.order = 7

    satellite.propagator.propagate()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorHPOP


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.initial_state
    :type: VehicleInitialState

    Get the satellite's initial state.

.. py:property:: force_model
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.force_model
    :type: VehicleHPOPForceModel

    Get the force model parameters.

.. py:property:: integrator
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.integrator
    :type: VehicleIntegrator

    Get the integrator parameters.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.covariance
    :type: VehicleCovariance

    Get the covariance parameters.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: display_coordinate_type
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.display_coordinate_type
    :type: PropagatorDisplayCoordinateType

    The propagator's display coordinate type.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










