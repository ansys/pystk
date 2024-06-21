IVehicleSpaceEnvironmentRadDoseRateElement
==========================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement

   object
   
   Dose rate interface.

.. py:currentmodule:: IVehicleSpaceEnvironmentRadDoseRateElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.electron_dose_rate`
              - Return electron dose rate if it is valid. Uses RadDoseRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.electron_bremsstrahlung_dose_rate`
              - Return electron bremsstrahlung dose rate if it is valid. Uses RadDoseRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.proton_dose_rate`
              - Return proton dose rate if it is valid. Uses RadDoseRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.total_dose_rate`
              - Return total dose rate if it is valid. Uses RadDoseRate Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.shielding_thickness`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_electron_dose_rate_valid`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_electron_bremsstrahlung_dose_rate_valid`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_proton_dose_rate_valid`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_total_dose_rate_valid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSpaceEnvironmentRadDoseRateElement


Property detail
---------------

.. py:property:: shielding_thickness
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.shielding_thickness
    :type: float

    Shielding thickness at which the dose rate information was computed. Uses RadiationShieldThickness Dimension.

.. py:property:: is_electron_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_electron_dose_rate_valid
    :type: bool

    Flag to indicate that the electron dose rate value is valid.

.. py:property:: is_electron_bremsstrahlung_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_electron_bremsstrahlung_dose_rate_valid
    :type: bool

    Flag to indicate that the electron bremsstrahlung dose rate value is valid.

.. py:property:: is_proton_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_proton_dose_rate_valid
    :type: bool

    Flag to indicate that the proton dose rate value is valid.

.. py:property:: is_total_dose_rate_valid
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.is_total_dose_rate_valid
    :type: bool

    Flag to indicate that the total dose rate value is valid.


Method detail
-------------



.. py:method:: electron_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.electron_dose_rate

    Return electron dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`


.. py:method:: electron_bremsstrahlung_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.electron_bremsstrahlung_dose_rate

    Return electron bremsstrahlung dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`


.. py:method:: proton_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.proton_dose_rate

    Return proton dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`


.. py:method:: total_dose_rate(self) -> float
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateElement.total_dose_rate

    Return total dose rate if it is valid. Uses RadDoseRate Dimension.

    :Returns:

        :obj:`~float`

