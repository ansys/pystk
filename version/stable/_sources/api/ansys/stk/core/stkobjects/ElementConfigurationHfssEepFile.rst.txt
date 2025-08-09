ElementConfigurationHfssEepFile
===============================

.. py:class:: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile

   Class defining an HFSS EEP file element configuration.

.. py:currentmodule:: ElementConfigurationHfssEepFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.filename`
              - Get or set the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_frequencies`
              - Get the frequencies defined in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.gain_type`
              - Get or set the gain type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_power_value`
              - Get the Defined Power Value for the selected GainType.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.user_gain_factor`
              - Get or set the User Gain Factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ElementConfigurationHfssEepFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.filename
    :type: str

    Get or set the file.

.. py:property:: defined_frequencies
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_frequencies
    :type: str

    Get the frequencies defined in the file.

.. py:property:: gain_type
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.gain_type
    :type: HFSSFarFieldDataGainType

    Get or set the gain type.

.. py:property:: defined_power_value
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_power_value
    :type: float

    Get the Defined Power Value for the selected GainType.

.. py:property:: user_gain_factor
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.user_gain_factor
    :type: float

    Get or set the User Gain Factor.


