IWaveform
=========

.. py:class:: IWaveform

   object
   
   Provide access to the properties and methods defining an antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~type`
            * - :py:meth:`~frequency_specification`
            * - :py:meth:`~frequency`
            * - :py:meth:`~wavelength`
            * - :py:meth:`~power`


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
    :type: "WAVEFORM_TYPE"

    Gets the waveform type enumeration.

.. py:property:: frequency_specification
    :canonical: ansys.stk.core.stkobjects.IWaveform.frequency_specification
    :type: "FREQUENCY_SPEC"

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


