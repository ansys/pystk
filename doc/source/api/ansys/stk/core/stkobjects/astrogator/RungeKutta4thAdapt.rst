RungeKutta4thAdapt
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalIntegrator`

   RK4thAdapt Numerical Integrator.

.. py:currentmodule:: RungeKutta4thAdapt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.initial_step`
              - Gets or sets the initial step. Uses time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.use_fixed_step`
              - True if running in fixed-step mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.use_max_step`
              - Whether or not to enforce the maximum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.use_min_step`
              - Whether or not to enforce the minimum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_step`
              - Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.min_step`
              - Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_rel_err`
              - Gets or sets the maximum relative error used to control step size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_abs_err`
              - Gets or sets the maximum absolute error; Also used if relative scale is too small. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.high_safety_coefficient`
              - Gets or sets the 'safety' coefficient used to decrease step size if the error is too high. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.low_safety_coefficient`
              - Gets or sets the 'safety' coefficient used to increase step size if the error is too low. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.error_control`
              - Gets or sets the error control method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_iterations`
              - Gets or sets the maximum iterations. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import RungeKutta4thAdapt


Property detail
---------------

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.initial_step
    :type: float

    Gets or sets the initial step. Uses time dimension.

.. py:property:: use_fixed_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.use_fixed_step
    :type: bool

    True if running in fixed-step mode.

.. py:property:: use_max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.use_max_step
    :type: bool

    Whether or not to enforce the maximum step.

.. py:property:: use_min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.use_min_step
    :type: bool

    Whether or not to enforce the minimum step.

.. py:property:: max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_step
    :type: float

    Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.min_step
    :type: float

    Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: max_rel_err
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_rel_err
    :type: float

    Gets or sets the maximum relative error used to control step size. Dimensionless.

.. py:property:: max_abs_err
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_abs_err
    :type: float

    Gets or sets the maximum absolute error; Also used if relative scale is too small. Dimensionless.

.. py:property:: high_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.high_safety_coefficient
    :type: float

    Gets or sets the 'safety' coefficient used to decrease step size if the error is too high. Dimensionless.

.. py:property:: low_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.low_safety_coefficient
    :type: float

    Gets or sets the 'safety' coefficient used to increase step size if the error is too low. Dimensionless.

.. py:property:: error_control
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.error_control
    :type: ERROR_CONTROL

    Gets or sets the error control method.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt.max_iterations
    :type: int

    Gets or sets the maximum iterations. Dimensionless.


