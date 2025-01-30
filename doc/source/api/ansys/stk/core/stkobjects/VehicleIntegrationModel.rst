VehicleIntegrationModel
=======================

.. py:class:: ansys.stk.core.stkobjects.VehicleIntegrationModel

   IntEnum


.. py:currentmodule:: VehicleIntegrationModel

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

            * - :py:attr:`~RUNGE_KUTTA_4`
              - RK 4: Runge-Kutta integration method of 4th order with no error control for the integration step size.

            * - :py:attr:`~RUNGE_KUTTA_FEHLBERG_78`
              - RKF 7(8): Runge-Kutta-Fehlberg integration method of 7th order with 8th order error control for the integration step size.

            * - :py:attr:`~RUNGE_KUTTA_VERNER_89_EFFICIENT`
              - RKV 8(9) Efficient: Runge-Kutta-Verner integration method of 8th order with 9th order error control for the integration step size, using the efficient coefficient set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleIntegrationModel


