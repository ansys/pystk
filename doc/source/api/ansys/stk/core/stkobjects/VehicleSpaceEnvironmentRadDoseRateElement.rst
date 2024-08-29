VehicleSpaceEnvironmentRadDoseRateElement
=========================================

.. py:class:: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement

   Class defining dose rate information computed for a shielding thickness.

.. py:currentmodule:: VehicleSpaceEnvironmentRadDoseRateElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.electron_dose_rate`
              - Return electron dose rate if it is valid. Uses RadDoseRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.electron_bremsstrahlung_dose_rate`
              - Return electron bremsstrahlung dose rate if it is valid. Uses RadDoseRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.proton_dose_rate`
              - Return proton dose rate if it is valid. Uses RadDoseRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.total_dose_rate`
              - Return total dose rate if it is valid. Uses RadDoseRate Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.shielding_thickness`
              - Shielding thickness at which the dose rate information was computed. Uses RadiationShieldThickness Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_electron_dose_rate_valid`
              - Flag to indicate that the electron dose rate value is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_electron_bremsstrahlung_dose_rate_valid`
              - Flag to indicate that the electron bremsstrahlung dose rate value is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_proton_dose_rate_valid`
              - Flag to indicate that the proton dose rate value is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_total_dose_rate_valid`
              - Flag to indicate that the total dose rate value is valid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSpaceEnvironmentRadDoseRateElement


Property detail
---------------

.. py:property:: shielding_thickness
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.shielding_thickness
    :type: float

    Shielding thickness at which the dose rate information was computed. Uses RadiationShieldThickness Dimension.

.. py:property:: is_electron_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_electron_dose_rate_valid
    :type: bool

    Flag to indicate that the electron dose rate value is valid.

.. py:property:: is_electron_bremsstrahlung_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_electron_bremsstrahlung_dose_rate_valid
    :type: bool

    Flag to indicate that the electron bremsstrahlung dose rate value is valid.

.. py:property:: is_proton_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_proton_dose_rate_valid
    :type: bool

    Flag to indicate that the proton dose rate value is valid.

.. py:property:: is_total_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.is_total_dose_rate_valid
    :type: bool

    Flag to indicate that the total dose rate value is valid.


Method detail
-------------



.. py:method:: electron_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.electron_dose_rate

    Return electron dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`


.. py:method:: electron_bremsstrahlung_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.electron_bremsstrahlung_dose_rate

    Return electron bremsstrahlung dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`


.. py:method:: proton_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.proton_dose_rate

    Return proton dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`


.. py:method:: total_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement.total_dose_rate

    Return total dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`

