IAircraftExternalProp
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp

   object
   
   Interface used to access the External File Propulsion options for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: IAircraftExternalProp

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.set_prop_filepath`
              - Set the filepath for the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.reload_prop_file`
              - Reload the prop file.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.set_density_scaling`
              - Set the option to use density scaling and set the density ratio exponent.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.prop_filepath`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.is_valid`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.can_set_accel_decel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.max_thrust_accel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.min_thrust_decel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.use_density_scaling`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.density_ratio_exponent`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftExternalProp


Property detail
---------------

.. py:property:: prop_filepath
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.prop_filepath
    :type: str

    Get the filepath for the prop file.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.is_valid
    :type: bool

    Check if the prop file is valid.

.. py:property:: can_set_accel_decel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.can_set_accel_decel
    :type: bool

    Check whether you can set the acceleration and deceleration values or whether they are specified in the file.

.. py:property:: max_thrust_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.max_thrust_accel
    :type: float

    Gets or sets the rate at which the aircraft speeds up at max throttle.

.. py:property:: min_thrust_decel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.min_thrust_decel
    :type: float

    Gets or sets the rate at which the aircraft slows down at minimum throttle setting.

.. py:property:: use_density_scaling
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.use_density_scaling
    :type: bool

    Opt whether to scale the accel/decel performance by the density ratio.

.. py:property:: density_ratio_exponent
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.density_ratio_exponent
    :type: float

    Get the relative impace of atmospheric density on the aircraft's performance.


Method detail
-------------


.. py:method:: set_prop_filepath(self, filepath: str) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.set_prop_filepath

    Set the filepath for the prop file.

    :Parameters:

    **filepath** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: reload_prop_file(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.reload_prop_file

    Reload the prop file.

    :Returns:

        :obj:`~str`









.. py:method:: set_density_scaling(self, useScaling: bool, exponent: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftExternalProp.set_density_scaling

    Set the option to use density scaling and set the density ratio exponent.

    :Parameters:

    **useScaling** : :obj:`~bool`
    **exponent** : :obj:`~float`

    :Returns:

        :obj:`~None`

