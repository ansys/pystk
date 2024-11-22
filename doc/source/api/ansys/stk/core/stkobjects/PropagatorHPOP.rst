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
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOP.display_coord_type`
              - The propagator's display coordinate type.



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

.. py:property:: display_coord_type
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.display_coord_type
    :type: PROPAGATOR_DISPLAY_COORDINATE_TYPE

    The propagator's display coordinate type.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










