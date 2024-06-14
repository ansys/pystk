IBulirschStoerIntegrator
========================

.. py:class:: IBulirschStoerIntegrator

   object
   
   Properties for the Bulirsch-Stoer numerical integrator.

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
            * - :py:meth:`~max_sequences`
            * - :py:meth:`~max_iterations`
            * - :py:meth:`~tolerance`
            * - :py:meth:`~first_safety_coefficient`
            * - :py:meth:`~second_safety_coefficient`


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


