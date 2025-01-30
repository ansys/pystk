IWaveform
=========

.. py:class:: ansys.stk.core.stkobjects.IWaveform

   Provide access to the properties and methods defining an antenna model.

.. py:currentmodule:: IWaveform

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveform.name`
              - Gets the waveform name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveform.type`
              - Gets the waveform type enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveform.frequency_specification`
              - Gets or sets the frequency specification.
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveform.frequency`
              - Gets or sets the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveform.wavelength`
              - Gets or sets the wavelength.
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveform.power`
              - Gets the power.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IWaveform


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IWaveform.name
    :type: str

    Gets the waveform name.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IWaveform.type
    :type: WaveformType

    Gets the waveform type enumeration.

.. py:property:: frequency_specification
    :canonical: ansys.stk.core.stkobjects.IWaveform.frequency_specification
    :type: FrequencySpecificationType

    Gets or sets the frequency specification.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IWaveform.frequency
    :type: float

    Gets or sets the frequency.

.. py:property:: wavelength
    :canonical: ansys.stk.core.stkobjects.IWaveform.wavelength
    :type: float

    Gets or sets the wavelength.

.. py:property:: power
    :canonical: ansys.stk.core.stkobjects.IWaveform.power
    :type: float

    Gets the power.


