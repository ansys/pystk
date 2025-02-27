AntennaModelANSYSffdFormat
==========================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining an antenna pattern ANSYS ffd model.

.. py:currentmodule:: AntennaModelANSYSffdFormat

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.filename`
              - Get or set the user antenna data filename.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.defined_frequencies`
              - Get the frequencies defined in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.gain_type`
              - Get or set the gain type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.defined_power_value`
              - Get the Defined Power Value for the selected GainType.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.user_gain_factor`
              - Get or set the User Gain Factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelANSYSffdFormat


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.filename
    :type: str

    Get or set the user antenna data filename.

.. py:property:: defined_frequencies
    :canonical: ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.defined_frequencies
    :type: str

    Get the frequencies defined in the file.

.. py:property:: gain_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.gain_type
    :type: HFSSFarFieldDataGainType

    Get or set the gain type.

.. py:property:: defined_power_value
    :canonical: ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.defined_power_value
    :type: float

    Get the Defined Power Value for the selected GainType.

.. py:property:: user_gain_factor
    :canonical: ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat.user_gain_factor
    :type: float

    Get or set the User Gain Factor.


