NUMERICAL_INTEGRATOR
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.NUMERICAL_INTEGRATOR

   IntEnum


.. py:currentmodule:: NUMERICAL_INTEGRATOR

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~RUNGE_KUTTA_4TH_ADAPT`
              - A 4th order Runge-Kutta integrator, adapting step size by comparing one full step to two half steps. Although this technique can be quite slow compared to the other algorithms, it is very common and can be used for comparison.

            * - :py:attr:`~RUNGE_KUTTA_FEHLBERG_7TH_8TH`
              - A 7th order Runge-Kutta-Fehlberg integrator with 8th order error control. This is the default integrator used in the HPOP propagator.

            * - :py:attr:`~RUNGE_KUTTA_VERNER_8TH_9TH`
              - A 9th order Runge-Kutta-Verner integrator with 8th order error control.

            * - :py:attr:`~BULIRSCH_STOER`
              - An integrator based on Richardson extrapolation with automatic step size control.

            * - :py:attr:`~GAUSS_JACKSON`
              - A 12th order Gauss-Jackson integrator for second order ODEs. There is currently no error control implemented for this method, meaning that a fixed step size is used.

            * - :py:attr:`~RUNGE_KUTTA_2ND_3RD`
              - A 2nd order Runge-Kutta integrator with 3rd order error control, using Bogacki and Shampine coefficients.

            * - :py:attr:`~RUNGE_KUTTA_4TH_5TH`
              - A 4th order Runge-Kutta integrator with 5th order error control, using Cash-Karp coefficients.

            * - :py:attr:`~RUNGE_KUTTA_4TH`
              - A 4th order Runge-Kutta integrator that does not employ error control.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import NUMERICAL_INTEGRATOR


