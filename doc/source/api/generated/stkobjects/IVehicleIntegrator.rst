IVehicleIntegrator
==================

.. py:class:: IVehicleIntegrator

   object
   
   Interface for HPOP integrator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~integration_model`
            * - :py:meth:`~use_graphics_3d_p`
            * - :py:meth:`~predictor_corrector_scheme`
            * - :py:meth:`~step_size_control`
            * - :py:meth:`~time_regularization`
            * - :py:meth:`~interpolation`
            * - :py:meth:`~report_ephem_on_fixed_time_step`
            * - :py:meth:`~do_not_propagate_below_altitude`
            * - :py:meth:`~allow_position_vel_cov_interpolation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleIntegrator


Property detail
---------------

.. py:property:: integration_model
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.integration_model
    :type: "VEHICLE_INTEGRATION_MODEL"

    Integration method to be used in propagating the orbit.

.. py:property:: use_graphics_3d_p
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.use_graphics_3d_p
    :type: bool

    Opt whether to use VOP, a variation of parameters in universal variables formulation of the equations of motion. Valid in combination with the RKF7(8) and Burlirsch-Stoer integration methods.

.. py:property:: predictor_corrector_scheme
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.predictor_corrector_scheme
    :type: "VEHICLE_PREDICTOR_CORRECTOR_SCHEME"

    Predictor corrector scheme (valid for Gauss-Jackson method only): method for updating acceleration components after corrector has converged.

.. py:property:: step_size_control
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.step_size_control
    :type: "IAgVeStepSizeControl"

    Get the method of integration step size control.

.. py:property:: time_regularization
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.time_regularization
    :type: "IAgVeTimeRegularization"

    Get the time regularization parameters.

.. py:property:: interpolation
    :canonical: ansys.stk.core.stkobjects.IVehicleIntegrator.interpolation
    :type: "IAgVeInterpolation"

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


