IVehicleSpaceEnvironmentMagneticField
=====================================

.. py:class:: IVehicleSpaceEnvironmentMagneticField

   object
   
   Magnetic field model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_b_field_as_array`
              - Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the vehicle's location location. Uses DateFormat and MagneticField Dimensions.
            * - :py:meth:`~compute_dipole_l`
              - Compute dipole L-shell parameter at the vehicle's location. Uses DateFormat Dimension.
            * - :py:meth:`~compute_mc_ilwain_l`
              - Compute McIlwain L-shell parameter at the vehicle's location. Uses DateFormat Dimension.
            * - :py:meth:`~compute_b_beq`
              - Compute B/Beq (i.e., the ratio of the magnetic field at the vehicle's location to the minimum field intensity along the field line thru the location). Uses DateFormat Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~main_field`
            * - :py:meth:`~external_field`
            * - :py:meth:`~igrf_update_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSpaceEnvironmentMagneticField


Property detail
---------------

.. py:property:: main_field
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentMagneticField.main_field
    :type: "SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD"

    Gets or sets the main magnetic field.

.. py:property:: external_field
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentMagneticField.external_field
    :type: "SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD"

    External magnetic field.

.. py:property:: igrf_update_rate
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentMagneticField.igrf_update_rate
    :type: float

    Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.


Method detail
-------------







.. py:method:: compute_b_field_as_array(self, time:typing.Any) -> list

    Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the vehicle's location location. Uses DateFormat and MagneticField Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_dipole_l(self, time:typing.Any) -> float

    Compute dipole L-shell parameter at the vehicle's location. Uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_mc_ilwain_l(self, time:typing.Any) -> float

    Compute McIlwain L-shell parameter at the vehicle's location. Uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_b_beq(self, time:typing.Any) -> float

    Compute B/Beq (i.e., the ratio of the magnetic field at the vehicle's location to the minimum field intensity along the field line thru the location). Uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

