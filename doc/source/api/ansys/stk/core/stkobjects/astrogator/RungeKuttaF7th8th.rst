RungeKuttaF7th8th
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalIntegrator`

   RKF7th8th Numerical Integrator.

.. py:currentmodule:: RungeKuttaF7th8th

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.initial_step`
              - Gets or sets the initial step. Uses time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.use_fixed_step`
              - True if running in fixed-step mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.use_max_step`
              - Whether or not to enforce the maximum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.use_min_step`
              - Whether or not to enforce the minimum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_step`
              - Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.min_step`
              - Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_relative_err`
              - Gets or sets the maximum relative error used to control step size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_absolute_err`
              - Gets or sets the maximum absolute error; Also used if relative scale is too small. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.high_safety_coefficient`
              - Gets or sets the 'safety' coefficient used to decrease step size if the error is too high. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.low_safety_coefficient`
              - Gets or sets the 'safety' coefficient used to increase step size if the error is too low. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.error_control`
              - Gets or sets the error control method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_iterations`
              - Gets or sets the maximum iterations. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import RungeKuttaF7th8th


Property detail
---------------

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.initial_step
    :type: float

    Gets or sets the initial step. Uses time dimension.

.. py:property:: use_fixed_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.use_fixed_step
    :type: bool

    True if running in fixed-step mode.

.. py:property:: use_max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.use_max_step
    :type: bool

    Whether or not to enforce the maximum step.

.. py:property:: use_min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.use_min_step
    :type: bool

    Whether or not to enforce the minimum step.

.. py:property:: max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_step
    :type: float

    Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.min_step
    :type: float

    Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: max_relative_err
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_relative_err
    :type: float

    Gets or sets the maximum relative error used to control step size. Dimensionless.

.. py:property:: max_absolute_err
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_absolute_err
    :type: float

    Gets or sets the maximum absolute error; Also used if relative scale is too small. Dimensionless.

.. py:property:: high_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.high_safety_coefficient
    :type: float

    Gets or sets the 'safety' coefficient used to decrease step size if the error is too high. Dimensionless.

.. py:property:: low_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.low_safety_coefficient
    :type: float

    Gets or sets the 'safety' coefficient used to increase step size if the error is too low. Dimensionless.

.. py:property:: error_control
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.error_control
    :type: ErrorControl

    Gets or sets the error control method.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th.max_iterations
    :type: int

    Gets or sets the maximum iterations. Dimensionless.


