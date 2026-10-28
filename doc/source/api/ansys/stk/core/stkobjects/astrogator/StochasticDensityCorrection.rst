StochasticDensityCorrection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection

   Properties for Stochastic Density Correction.

.. py:currentmodule:: StochasticDensityCorrection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.density_increase_threshold`
              - Open density gain when density ratio increases by this amount.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.density_ratio_root`
              - Mapping of density uncertainty goes as K^(1/n).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.half_life`
              - Density Correction Half-life.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.sigma`
              - Uncertainty in relative density at periapsis for non-Earth atmospheres.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.sigma_scale`
              - Scale Factor for Density Correction Sigma.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StochasticDensityCorrection


Property detail
---------------

.. py:property:: density_increase_threshold
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.density_increase_threshold
    :type: float

    Open density gain when density ratio increases by this amount.

.. py:property:: density_ratio_root
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.density_ratio_root
    :type: float

    Mapping of density uncertainty goes as K^(1/n).

.. py:property:: half_life
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.half_life
    :type: float

    Density Correction Half-life.

.. py:property:: sigma
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.sigma
    :type: float

    Uncertainty in relative density at periapsis for non-Earth atmospheres.

.. py:property:: sigma_scale
    :canonical: ansys.stk.core.stkobjects.astrogator.StochasticDensityCorrection.sigma_scale
    :type: float

    Scale Factor for Density Correction Sigma.


