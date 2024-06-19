VEHICLE_INTEGRATION_MODEL
=========================

.. py:class:: VEHICLE_INTEGRATION_MODEL

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BULIRSCH_STOER`
              - Bulirsch-Stoer: integration method based on Richardson extrapolation with automatic step size control.

            * - :py:attr:`~GAUSS_JACKSON`
              - Gauss-Jackson: 12th order Gauss-Jackson integration method for second order ODEs.

            * - :py:attr:`~RUNGE_KUTTA4`
              - RK 4: Runge-Kutta integration method of 4th order with no error control for the integration step size.

            * - :py:attr:`~RUNGE_KUTTA_F78`
              - RKF 7(8): Runge-Kutta-Fehlberg integration method of 7th order with 8th order error control for the integration step size.

            * - :py:attr:`~RUNGE_KUTTA_V89_EFFICIENT`
              - RKV 8(9) Efficient: Runge-Kutta-Verner integration method of 8th order with 9th order error control for the integration step size, using the efficient coefficient set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_INTEGRATION_MODEL


