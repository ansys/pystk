RungeKutta2nd3rd
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalIntegrator`

   RK2nd3rd Numerical Integrator.

.. py:currentmodule:: RungeKutta2nd3rd

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.error_control`
              - Get or set the error control method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.high_safety_coefficient`
              - Get or set the 'safety' coefficient used to decrease step size if the error is too high. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.initial_step`
              - Get or set the initial step. Uses time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.low_safety_coefficient`
              - Get or set the 'safety' coefficient used to increase step size if the error is too low. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_absolute_err`
              - Get or set the maximum absolute error; Also used if relative scale is too small. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_iterations`
              - Get or set the maximum iterations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_relative_err`
              - Get or set the maximum relative error used to control step size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_step`
              - Get or set the maximum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.min_step`
              - Get or set the minimum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.use_fixed_step`
              - True if running in fixed-step mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.use_max_step`
              - Whether or not to enforce the maximum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.use_min_step`
              - Whether or not to enforce the minimum step.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import RungeKutta2nd3rd


Property detail
---------------

.. py:property:: error_control
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.error_control
    :type: ErrorControl

    Get or set the error control method.

.. py:property:: high_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.high_safety_coefficient
    :type: float

    Get or set the 'safety' coefficient used to decrease step size if the error is too high. Dimensionless.

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.initial_step
    :type: float

    Get or set the initial step. Uses time dimension.

.. py:property:: low_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.low_safety_coefficient
    :type: float

    Get or set the 'safety' coefficient used to increase step size if the error is too low. Dimensionless.

.. py:property:: max_absolute_err
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_absolute_err
    :type: float

    Get or set the maximum absolute error; Also used if relative scale is too small. Dimensionless.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_iterations
    :type: int

    Get or set the maximum iterations. Dimensionless.

.. py:property:: max_relative_err
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_relative_err
    :type: float

    Get or set the maximum relative error used to control step size. Dimensionless.

.. py:property:: max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.max_step
    :type: float

    Get or set the maximum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.min_step
    :type: float

    Get or set the minimum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: use_fixed_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.use_fixed_step
    :type: bool

    True if running in fixed-step mode.

.. py:property:: use_max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.use_max_step
    :type: bool

    Whether or not to enforce the maximum step.

.. py:property:: use_min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd.use_min_step
    :type: bool

    Whether or not to enforce the minimum step.


