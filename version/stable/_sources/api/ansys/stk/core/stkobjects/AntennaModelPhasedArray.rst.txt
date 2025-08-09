AntennaModelPhasedArray
=======================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelPhasedArray

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a phased array antenna model.

.. py:currentmodule:: AntennaModelPhasedArray

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.backlobe_suppression`
              - Get or set the backlobe suppression.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.include_element_factor`
              - Get or set the option to include the element factor in the gain response.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.element_factor_exponent`
              - Get or set the raised cosine exponent for the element factor.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.width`
              - Get the array width.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.height`
              - Get the array height.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.number_of_elements`
              - Get the number of array elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.supported_beam_direction_provider_types`
              - Get an array of valid beam direction provider types.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.beam_direction_provider_type`
              - Get or set the beam direction provider type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.beam_direction_provider`
              - Get the beam direction provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.supported_null_direction_provider_types`
              - Get an array of valid null direction provider types.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.null_direction_provider_type`
              - Get or set the null direction provider type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.null_direction_provider`
              - Get the null direction provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.beamformer_type`
              - Get or set beamformer type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.beamformer`
              - Get the beamformer.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.element_configuration_type`
              - Get or set the element configuration type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.element_configuration`
              - Get the element configuration.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.elements`
              - Get the collection of elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.show_grid`
              - Get or set the option to show the grid in the antenna's element viewport GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray.show_labels`
              - Get or set the option to show the labels in the antenna's element viewport GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelPhasedArray


Property detail
---------------

.. py:property:: backlobe_suppression
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.backlobe_suppression
    :type: float

    Get or set the backlobe suppression.

.. py:property:: include_element_factor
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.include_element_factor
    :type: bool

    Get or set the option to include the element factor in the gain response.

.. py:property:: element_factor_exponent
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.element_factor_exponent
    :type: float

    Get or set the raised cosine exponent for the element factor.

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.width
    :type: float

    Get the array width.

.. py:property:: height
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.height
    :type: float

    Get the array height.

.. py:property:: number_of_elements
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.number_of_elements
    :type: int

    Get the number of array elements.

.. py:property:: supported_beam_direction_provider_types
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.supported_beam_direction_provider_types
    :type: list

    Get an array of valid beam direction provider types.

.. py:property:: beam_direction_provider_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.beam_direction_provider_type
    :type: DirectionProviderType

    Get or set the beam direction provider type.

.. py:property:: beam_direction_provider
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.beam_direction_provider
    :type: IDirectionProvider

    Get the beam direction provider.

.. py:property:: supported_null_direction_provider_types
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.supported_null_direction_provider_types
    :type: list

    Get an array of valid null direction provider types.

.. py:property:: null_direction_provider_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.null_direction_provider_type
    :type: DirectionProviderType

    Get or set the null direction provider type.

.. py:property:: null_direction_provider
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.null_direction_provider
    :type: IDirectionProvider

    Get the null direction provider.

.. py:property:: beamformer_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.beamformer_type
    :type: BeamformerType

    Get or set beamformer type.

.. py:property:: beamformer
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.beamformer
    :type: IBeamformer

    Get the beamformer.

.. py:property:: element_configuration_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.element_configuration_type
    :type: ElementConfigurationType

    Get or set the element configuration type.

.. py:property:: element_configuration
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.element_configuration
    :type: IElementConfiguration

    Get the element configuration.

.. py:property:: elements
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.elements
    :type: ElementCollection

    Get the collection of elements.

.. py:property:: show_grid
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.show_grid
    :type: bool

    Get or set the option to show the grid in the antenna's element viewport GUI.

.. py:property:: show_labels
    :canonical: ansys.stk.core.stkobjects.AntennaModelPhasedArray.show_labels
    :type: bool

    Get or set the option to show the labels in the antenna's element viewport GUI.


