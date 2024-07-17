AircraftExternalProp
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftExternalProp

   Bases: 

   Class defining the external propulsion options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftExternalProp

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.set_prop_filepath`
              - Set the filepath for the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.reload_prop_file`
              - Reload the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.set_density_scaling`
              - Set the option to use density scaling and set the density ratio exponent.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.prop_filepath`
              - Get the filepath for the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.is_valid`
              - Check if the prop file is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.can_set_accel_decel`
              - Check whether you can set the acceleration and deceleration values or whether they are specified in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.max_thrust_accel`
              - Gets or sets the rate at which the aircraft speeds up at max throttle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.min_thrust_decel`
              - Gets or sets the rate at which the aircraft slows down at minimum throttle setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.use_density_scaling`
              - Opt whether to scale the accel/decel performance by the density ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp.density_ratio_exponent`
              - Get the relative impace of atmospheric density on the aircraft's performance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftExternalProp


Property detail
---------------

.. py:property:: prop_filepath
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.prop_filepath
    :type: str

    Get the filepath for the prop file.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.is_valid
    :type: bool

    Check if the prop file is valid.

.. py:property:: can_set_accel_decel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.can_set_accel_decel
    :type: bool

    Check whether you can set the acceleration and deceleration values or whether they are specified in the file.

.. py:property:: max_thrust_accel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.max_thrust_accel
    :type: float

    Gets or sets the rate at which the aircraft speeds up at max throttle.

.. py:property:: min_thrust_decel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.min_thrust_decel
    :type: float

    Gets or sets the rate at which the aircraft slows down at minimum throttle setting.

.. py:property:: use_density_scaling
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.use_density_scaling
    :type: bool

    Opt whether to scale the accel/decel performance by the density ratio.

.. py:property:: density_ratio_exponent
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.density_ratio_exponent
    :type: float

    Get the relative impace of atmospheric density on the aircraft's performance.


Method detail
-------------


.. py:method:: set_prop_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.set_prop_filepath

    Set the filepath for the prop file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: reload_prop_file(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.reload_prop_file

    Reload the prop file.

    :Returns:

        :obj:`~str`









.. py:method:: set_density_scaling(self, useScaling: bool, exponent: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftExternalProp.set_density_scaling

    Set the option to use density scaling and set the density ratio exponent.

    :Parameters:

    **useScaling** : :obj:`~bool`
    **exponent** : :obj:`~float`

    :Returns:

        :obj:`~None`

