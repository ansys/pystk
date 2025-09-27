StochasticModelParameters
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters

   Properties for Stochastic Model Parameters.

.. py:currentmodule:: StochasticModelParameters

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.diffusion_coefficient`
              - Determine the amount of process noise to be added to state covariance used in the Random Walk model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.error_threshold`
              - Covariance floor for long term mean used in the Vasicek model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.half_life`
              - Half life value for Gauss Markov stochastic process.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.model_type`
              - Type of stochastic model used for SRP correction.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.process_noise_step`
              - Process noise step when minimum floor is hit used in the Vasicek model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.sigma`
              - Root variance of the initial error in the nominal value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.sigma_long_term`
              - Root variance of the initial error in the long term constant value used in the Vasicek model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StochasticModelParameters


Property detail
---------------

.. py:property:: diffusion_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.diffusion_coefficient
    :type: float

    Determine the amount of process noise to be added to state covariance used in the Random Walk model.

.. py:property:: error_threshold
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.error_threshold
    :type: float

    Covariance floor for long term mean used in the Vasicek model.

.. py:property:: half_life
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.half_life
    :type: float

    Half life value for Gauss Markov stochastic process.

.. py:property:: model_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.model_type
    :type: StochasticModel

    Type of stochastic model used for SRP correction.

.. py:property:: process_noise_step
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.process_noise_step
    :type: float

    Process noise step when minimum floor is hit used in the Vasicek model.

.. py:property:: sigma
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.sigma
    :type: float

    Root variance of the initial error in the nominal value.

.. py:property:: sigma_long_term
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticModelParameters.sigma_long_term
    :type: float

    Root variance of the initial error in the long term constant value used in the Vasicek model.


