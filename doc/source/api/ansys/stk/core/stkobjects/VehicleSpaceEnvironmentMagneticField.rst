VehicleSpaceEnvironmentMagneticField
====================================

.. py:class:: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField

   Bases: 

   Magnetic field settings.

.. py:currentmodule:: VehicleSpaceEnvironmentMagneticField

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_b_field_as_array`
              - Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the vehicle's location location. Uses DateFormat and MagneticField Dimensions.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_dipole_l`
              - Compute dipole L-shell parameter at the vehicle's location. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_mc_ilwain_l`
              - Compute McIlwain L-shell parameter at the vehicle's location. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_b_beq`
              - Compute B/Beq (i.e., the ratio of the magnetic field at the vehicle's location to the minimum field intensity along the field line thru the location). Uses DateFormat Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.main_field`
              - Gets or sets the main magnetic field.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.external_field`
              - External magnetic field.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.igrf_update_rate`
              - Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSpaceEnvironmentMagneticField


Property detail
---------------

.. py:property:: main_field
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.main_field
    :type: SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD

    Gets or sets the main magnetic field.

.. py:property:: external_field
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.external_field
    :type: SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD

    External magnetic field.

.. py:property:: igrf_update_rate
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.igrf_update_rate
    :type: float

    Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.


Method detail
-------------







.. py:method:: compute_b_field_as_array(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_b_field_as_array

    Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the vehicle's location location. Uses DateFormat and MagneticField Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_dipole_l(self, time: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_dipole_l

    Compute dipole L-shell parameter at the vehicle's location. Uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_mc_ilwain_l(self, time: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_mc_ilwain_l

    Compute McIlwain L-shell parameter at the vehicle's location. Uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_b_beq(self, time: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField.compute_b_beq

    Compute B/Beq (i.e., the ratio of the magnetic field at the vehicle's location to the minimum field intensity along the field line thru the location). Uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

