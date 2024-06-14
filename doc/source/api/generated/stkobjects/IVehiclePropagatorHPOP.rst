IVehiclePropagatorHPOP
======================

.. py:class:: IVehiclePropagatorHPOP

   IVehiclePropagator
   
   HPOP propagator interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~step`
            * - :py:meth:`~initial_state`
            * - :py:meth:`~force_model`
            * - :py:meth:`~integrator`
            * - :py:meth:`~covariance`
            * - :py:meth:`~ephemeris_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorHPOP


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorHPOP.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorHPOP.initial_state
    :type: "IAgVeInitialState"

    Get the satellite's initial state.

.. py:property:: force_model
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorHPOP.force_model
    :type: "IAgVeHPOPForceModel"

    Get the force model parameters.

.. py:property:: integrator
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorHPOP.integrator
    :type: "IAgVeIntegrator"

    Get the integrator parameters.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorHPOP.covariance
    :type: "IAgVeCovariance"

    Get the covariance parameters.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorHPOP.ephemeris_interval
    :type: "IAgCrdnEventIntervalSmartInterval"

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`








