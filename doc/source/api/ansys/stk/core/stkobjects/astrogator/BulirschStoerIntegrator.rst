BulirschStoerIntegrator
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalIntegrator`

   Bulirsch-Stoer Numerical Integrator.

.. py:currentmodule:: BulirschStoerIntegrator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.initial_step`
              - Gets or sets the initial step. Uses time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.use_fixed_step`
              - True if running in fixed-step mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.use_max_step`
              - Whether or not to enforce the maximum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.use_min_step`
              - Whether or not to enforce the minimum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_step`
              - Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.min_step`
              - Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_rel_err`
              - Gets or sets the maximum relative error used to control step size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_sequences`
              - Gets or sets the maximum number of sequences. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_iterations`
              - Gets or sets the maximum number of iterations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.tolerance`
              - Gets or sets the error tolerance for step size control. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.first_safety_coefficient`
              - Gets or sets the first safety coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.second_safety_coefficient`
              - Gets or sets the second safety coefficient. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BulirschStoerIntegrator


Property detail
---------------

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.initial_step
    :type: float

    Gets or sets the initial step. Uses time dimension.

.. py:property:: use_fixed_step
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.use_fixed_step
    :type: bool

    True if running in fixed-step mode.

.. py:property:: use_max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.use_max_step
    :type: bool

    Whether or not to enforce the maximum step.

.. py:property:: use_min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.use_min_step
    :type: bool

    Whether or not to enforce the minimum step.

.. py:property:: max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_step
    :type: float

    Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.min_step
    :type: float

    Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: max_rel_err
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_rel_err
    :type: float

    Gets or sets the maximum relative error used to control step size. Dimensionless.

.. py:property:: max_sequences
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_sequences
    :type: int

    Gets or sets the maximum number of sequences. Dimensionless.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.max_iterations
    :type: int

    Gets or sets the maximum number of iterations. Dimensionless.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.tolerance
    :type: float

    Gets or sets the error tolerance for step size control. Dimensionless.

.. py:property:: first_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.first_safety_coefficient
    :type: float

    Gets or sets the first safety coefficient. Dimensionless.

.. py:property:: second_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator.second_safety_coefficient
    :type: float

    Gets or sets the second safety coefficient. Dimensionless.


