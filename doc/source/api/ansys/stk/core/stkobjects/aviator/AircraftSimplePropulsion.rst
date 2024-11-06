AircraftSimplePropulsion
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion

   Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftSimplePropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.set_density_scaling`
              - Set the option to use density scaling and set the density ratio exponent.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.max_thrust_acceleration`
              - Gets or sets the rate at which the aircraft speeds up at max throttle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.min_thrust_deceleration`
              - Gets or sets the rate at which the aircraft slows down at minimum throttle setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.use_density_scaling`
              - Opt whether to scale the accel/decel performance by the density ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.density_ratio_exponent`
              - Get the relative impace of atmospheric density on the aircraft's performance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftSimplePropulsion


Property detail
---------------

.. py:property:: max_thrust_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.max_thrust_acceleration
    :type: float

    Gets or sets the rate at which the aircraft speeds up at max throttle.

.. py:property:: min_thrust_deceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.min_thrust_deceleration
    :type: float

    Gets or sets the rate at which the aircraft slows down at minimum throttle setting.

.. py:property:: use_density_scaling
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.use_density_scaling
    :type: bool

    Opt whether to scale the accel/decel performance by the density ratio.

.. py:property:: density_ratio_exponent
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.density_ratio_exponent
    :type: float

    Get the relative impace of atmospheric density on the aircraft's performance.


Method detail
-------------







.. py:method:: set_density_scaling(self, use_scaling: bool, exponent: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.set_density_scaling

    Set the option to use density scaling and set the density ratio exponent.

    :Parameters:

    **use_scaling** : :obj:`~bool`
    **exponent** : :obj:`~float`

    :Returns:

        :obj:`~None`

