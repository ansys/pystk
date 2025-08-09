AircraftExternalPropulsion
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion

   Class defining the external propulsion options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftExternalPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.set_propulsion_filepath`
              - Set the filepath for the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.reload_propulsion_file`
              - Reload the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.set_density_scaling`
              - Set the option to use density scaling and set the density ratio exponent.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.propulsion_filepath`
              - Get the filepath for the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.is_valid`
              - Check if the prop file is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.can_set_acceleration_deceleration`
              - Check whether you can set the acceleration and deceleration values or whether they are specified in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.max_thrust_acceleration`
              - Get or set the rate at which the aircraft speeds up at max throttle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.min_thrust_deceleration`
              - Get or set the rate at which the aircraft slows down at minimum throttle setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.use_density_scaling`
              - Opt whether to scale the accel/decel performance by the density ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.density_ratio_exponent`
              - Get the relative impace of atmospheric density on the aircraft's performance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftExternalPropulsion


Property detail
---------------

.. py:property:: propulsion_filepath
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.propulsion_filepath
    :type: str

    Get the filepath for the prop file.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.is_valid
    :type: bool

    Check if the prop file is valid.

.. py:property:: can_set_acceleration_deceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.can_set_acceleration_deceleration
    :type: bool

    Check whether you can set the acceleration and deceleration values or whether they are specified in the file.

.. py:property:: max_thrust_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.max_thrust_acceleration
    :type: float

    Get or set the rate at which the aircraft speeds up at max throttle.

.. py:property:: min_thrust_deceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.min_thrust_deceleration
    :type: float

    Get or set the rate at which the aircraft slows down at minimum throttle setting.

.. py:property:: use_density_scaling
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.use_density_scaling
    :type: bool

    Opt whether to scale the accel/decel performance by the density ratio.

.. py:property:: density_ratio_exponent
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.density_ratio_exponent
    :type: float

    Get the relative impace of atmospheric density on the aircraft's performance.


Method detail
-------------


.. py:method:: set_propulsion_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.set_propulsion_filepath

    Set the filepath for the prop file.

    :Parameters:

        **filepath** : :obj:`~str`


    :Returns:

        :obj:`~str`

.. py:method:: reload_propulsion_file(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.reload_propulsion_file

    Reload the prop file.

    :Returns:

        :obj:`~str`









.. py:method:: set_density_scaling(self, use_scaling: bool, exponent: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion.set_density_scaling

    Set the option to use density scaling and set the density ratio exponent.

    :Parameters:

        **use_scaling** : :obj:`~bool`

        **exponent** : :obj:`~float`


    :Returns:

        :obj:`~None`

