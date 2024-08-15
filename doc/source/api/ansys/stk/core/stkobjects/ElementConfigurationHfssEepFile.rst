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
              - Gets or sets the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_frequencies`
              - Gets the frequencies defined in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.gain_type`
              - Gets or sets the gain type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_power_value`
              - Gets the Defined Power Value for the selected GainType.
            * - :py:attr:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.user_gain_factor`
              - Gets or sets the User Gain Factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ElementConfigurationHfssEepFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.filename
    :type: str

    Gets or sets the file.

.. py:property:: defined_frequencies
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_frequencies
    :type: str

    Gets the frequencies defined in the file.

.. py:property:: gain_type
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.gain_type
    :type: HFSS_FFD_GAIN_TYPE

    Gets or sets the gain type.

.. py:property:: defined_power_value
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.defined_power_value
    :type: float

    Gets the Defined Power Value for the selected GainType.

.. py:property:: user_gain_factor
    :canonical: ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile.user_gain_factor
    :type: float

    Gets or sets the User Gain Factor.


