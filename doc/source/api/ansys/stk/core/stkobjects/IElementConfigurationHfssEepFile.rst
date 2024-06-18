IElementConfigurationHfssEepFile
================================

.. py:class:: IElementConfigurationHfssEepFile

   object
   
   Provide access to the properties and methods defining an HFSS EEP file element configuration.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`
            * - :py:meth:`~defined_frequencies`
            * - :py:meth:`~gain_type`
            * - :py:meth:`~defined_power_value`
            * - :py:meth:`~user_gain_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IElementConfigurationHfssEepFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationHfssEepFile.filename
    :type: str

    Gets or sets the file.

.. py:property:: defined_frequencies
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationHfssEepFile.defined_frequencies
    :type: str

    Gets the frequencies defined in the file.

.. py:property:: gain_type
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationHfssEepFile.gain_type
    :type: "HFSS_FFD_GAIN_TYPE"

    Gets or sets the gain type.

.. py:property:: defined_power_value
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationHfssEepFile.defined_power_value
    :type: float

    Gets the Defined Power Value for the selected GainType.

.. py:property:: user_gain_factor
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationHfssEepFile.user_gain_factor
    :type: float

    Gets or sets the User Gain Factor.


