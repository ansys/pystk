IVehicleIntegrator
==================

.. py:class:: ansys.stk.core.stkobjects.IVehicleIntegrator

   object
   
   Interface for HPOP integrator.

.. py:currentmodule:: IVehicleIntegrator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.integration_model`
              - Integration method to be used in propagating the orbit.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.use_graphics_3d_p`
              - Opt whether to use VOP, a variation of parameters in universal variables formulation of the equations of motion. Valid in combination with the RKF7(8) and Burlirsch-Stoer integration methods.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.predictor_corrector_scheme`
              - Predictor corrector scheme (valid for Gauss-Jackson method only): method for updating acceleration components after corrector has converged.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.step_size_control`
              - Get the method of integration step size control.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.time_regularization`
              - Get the time regularization parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.interpolation`
              - Get the interpolation parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.report_ephem_on_fixed_time_step`
              - Opt whether ephemeris is to be reported on a fixed time step.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.do_not_propagate_below_altitude`
              - Altitude below which to stop propagation. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleIntegrator.allow_position_vel_cov_interpolation`
              - Get whether to allow pos-vel covariance interpolation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleIntegrator


Property detail
---------------

.. py:property:: integration_model
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.integration_model
    :type: VEHICLE_INTEGRATION_MODEL

    Integration method to be used in propagating the orbit.

.. py:property:: use_graphics_3d_p
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.use_graphics_3d_p
    :type: bool

    Opt whether to use VOP, a variation of parameters in universal variables formulation of the equations of motion. Valid in combination with the RKF7(8) and Burlirsch-Stoer integration methods.

.. py:property:: predictor_corrector_scheme
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.predictor_corrector_scheme
    :type: VEHICLE_PREDICTOR_CORRECTOR_SCHEME

    Predictor corrector scheme (valid for Gauss-Jackson method only): method for updating acceleration components after corrector has converged.

.. py:property:: step_size_control
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.step_size_control
    :type: IVehicleStepSizeControl

    Get the method of integration step size control.

.. py:property:: time_regularization
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.time_regularization
    :type: IVehicleTimeRegularization

    Get the time regularization parameters.

.. py:property:: interpolation
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.interpolation
    :type: IVehicleInterpolation

    Get the interpolation parameters.

.. py:property:: report_ephem_on_fixed_time_step
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.report_ephem_on_fixed_time_step
    :type: bool

    Opt whether ephemeris is to be reported on a fixed time step.

.. py:property:: do_not_propagate_below_altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.do_not_propagate_below_altitude
    :type: float

    Altitude below which to stop propagation. Uses Distance Dimension.

.. py:property:: allow_position_vel_cov_interpolation
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.allow_position_vel_cov_interpolation
    :type: bool

    Get whether to allow pos-vel covariance interpolation.


