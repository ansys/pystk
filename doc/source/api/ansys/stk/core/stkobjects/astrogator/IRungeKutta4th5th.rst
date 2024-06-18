IRungeKutta4th5th
=================

.. py:class:: IRungeKutta4th5th

   object
   
   Properties for the RK4th5th numerical integrator.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initial_step`
            * - :py:meth:`~use_fixed_step`
            * - :py:meth:`~use_max_step`
            * - :py:meth:`~use_min_step`
            * - :py:meth:`~max_step`
            * - :py:meth:`~min_step`
            * - :py:meth:`~max_rel_err`
            * - :py:meth:`~max_abs_err`
            * - :py:meth:`~high_safety_coefficient`
            * - :py:meth:`~low_safety_coefficient`
            * - :py:meth:`~error_control`
            * - :py:meth:`~max_iterations`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IRungeKutta4th5th


Property detail
---------------

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.initial_step
    :type: float

    Gets or sets the initial step. Uses time dimension.

.. py:property:: use_fixed_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.use_fixed_step
    :type: bool

    True if running in fixed-step mode.

.. py:property:: use_max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.use_max_step
    :type: bool

    Whether or not to enforce the maximum step.

.. py:property:: use_min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.use_min_step
    :type: bool

    Whether or not to enforce the minimum step.

.. py:property:: max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.max_step
    :type: float

    Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.min_step
    :type: float

    Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: max_rel_err
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.max_rel_err
    :type: float

    Gets or sets the maximum relative error used to control step size. Dimensionless.

.. py:property:: max_abs_err
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.max_abs_err
    :type: float

    Gets or sets the maximum absolute error; Also used if relative scale is too small. Dimensionless.

.. py:property:: high_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.high_safety_coefficient
    :type: float

    Gets or sets the 'safety' coefficient used to decrease step size if the error is too high. Dimensionless.

.. py:property:: low_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.low_safety_coefficient
    :type: float

    Gets or sets the 'safety' coefficient used to increase step size if the error is too low. Dimensionless.

.. py:property:: error_control
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.error_control
    :type: "ERROR_CONTROL"

    Gets or sets the error control method.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th.max_iterations
    :type: int

    Gets or sets the maximum iterations. Dimensionless.


