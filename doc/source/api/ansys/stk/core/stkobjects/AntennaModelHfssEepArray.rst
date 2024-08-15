AntennaModelHfssEepArray
========================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelHfssEepArray

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining an HFSS EEP array antenna model.

.. py:currentmodule:: AntennaModelHfssEepArray

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.width`
              - Gets the array width.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.height`
              - Gets the array height.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.number_of_elements`
              - Gets the number of array elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.supported_beam_direction_provider_types`
              - Gets an array of valid beam direction provider types.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider_type`
              - Gets or sets the beam direction provider type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider`
              - Gets the beam direction provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beamformer_type`
              - Gets or sets beamformer type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beamformer`
              - Gets the beamformer.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.element_configuration`
              - Gets the element configuration.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray.elements`
              - Gets the collection of elements.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelHfssEepArray


Property detail
---------------

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.width
    :type: float

    Gets the array width.

.. py:property:: height
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.height
    :type: float

    Gets the array height.

.. py:property:: number_of_elements
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.number_of_elements
    :type: int

    Gets the number of array elements.

.. py:property:: supported_beam_direction_provider_types
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.supported_beam_direction_provider_types
    :type: list

    Gets an array of valid beam direction provider types.

.. py:property:: beam_direction_provider_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider_type
    :type: DIRECTION_PROVIDER_TYPE

    Gets or sets the beam direction provider type.

.. py:property:: beam_direction_provider
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider
    :type: IDirectionProvider

    Gets the beam direction provider.

.. py:property:: beamformer_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beamformer_type
    :type: BEAMFORMER_TYPE

    Gets or sets beamformer type.

.. py:property:: beamformer
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.beamformer
    :type: IBeamformer

    Gets the beamformer.

.. py:property:: element_configuration
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.element_configuration
    :type: ElementConfigurationHfssEepFile

    Gets the element configuration.

.. py:property:: elements
    :canonical: ansys.stk.core.stkobjects.AntennaModelHfssEepArray.elements
    :type: ElementCollection

    Gets the collection of elements.


