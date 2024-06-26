IBulirschStoerIntegrator
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator

   object
   
   Properties for the Bulirsch-Stoer numerical integrator.

.. py:currentmodule:: IBulirschStoerIntegrator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.initial_step`
              - Gets or sets the initial step. Uses time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.use_fixed_step`
              - True if running in fixed-step mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.use_max_step`
              - Whether or not to enforce the maximum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.use_min_step`
              - Whether or not to enforce the minimum step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_step`
              - Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.min_step`
              - Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_rel_err`
              - Gets or sets the maximum relative error used to control step size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_sequences`
              - Gets or sets the maximum number of sequences. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_iterations`
              - Gets or sets the maximum number of iterations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.tolerance`
              - Gets or sets the error tolerance for step size control. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.first_safety_coefficient`
              - Gets or sets the first safety coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.second_safety_coefficient`
              - Gets or sets the second safety coefficient. Dimensionless.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBulirschStoerIntegrator


Property detail
---------------

.. py:property:: initial_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.initial_step
    :type: float

    Gets or sets the initial step. Uses time dimension.

.. py:property:: use_fixed_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.use_fixed_step
    :type: bool

    True if running in fixed-step mode.

.. py:property:: use_max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.use_max_step
    :type: bool

    Whether or not to enforce the maximum step.

.. py:property:: use_min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.use_min_step
    :type: bool

    Whether or not to enforce the minimum step.

.. py:property:: max_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_step
    :type: float

    Gets or sets the maximum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: min_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.min_step
    :type: float

    Gets or sets the minimum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: max_rel_err
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_rel_err
    :type: float

    Gets or sets the maximum relative error used to control step size. Dimensionless.

.. py:property:: max_sequences
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_sequences
    :type: int

    Gets or sets the maximum number of sequences. Dimensionless.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.max_iterations
    :type: int

    Gets or sets the maximum number of iterations. Dimensionless.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.tolerance
    :type: float

    Gets or sets the error tolerance for step size control. Dimensionless.

.. py:property:: first_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.first_safety_coefficient
    :type: float

    Gets or sets the first safety coefficient. Dimensionless.

.. py:property:: second_safety_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator.second_safety_coefficient
    :type: float

    Gets or sets the second safety coefficient. Dimensionless.


