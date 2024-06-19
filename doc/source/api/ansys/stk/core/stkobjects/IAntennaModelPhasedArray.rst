IAntennaModelPhasedArray
========================

.. py:class:: IAntennaModelPhasedArray

   object
   
   Provide access to the properties and methods defining a phased array antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~backlobe_suppression`
            * - :py:meth:`~include_element_factor`
            * - :py:meth:`~element_factor_exponent`
            * - :py:meth:`~width`
            * - :py:meth:`~height`
            * - :py:meth:`~number_of_elements`
            * - :py:meth:`~supported_beam_direction_provider_types`
            * - :py:meth:`~beam_direction_provider_type`
            * - :py:meth:`~beam_direction_provider`
            * - :py:meth:`~supported_null_direction_provider_types`
            * - :py:meth:`~null_direction_provider_type`
            * - :py:meth:`~null_direction_provider`
            * - :py:meth:`~beamformer_type`
            * - :py:meth:`~beamformer`
            * - :py:meth:`~element_configuration_type`
            * - :py:meth:`~element_configuration`
            * - :py:meth:`~elements`
            * - :py:meth:`~show_grid`
            * - :py:meth:`~show_labels`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelPhasedArray


Property detail
---------------

.. py:property:: backlobe_suppression
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.backlobe_suppression
    :type: float

    Gets or sets the backlobe suppression.

.. py:property:: include_element_factor
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.include_element_factor
    :type: bool

    Gets or sets the option to include the element factor in the gain response.

.. py:property:: element_factor_exponent
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.element_factor_exponent
    :type: float

    Gets or sets the raised cosine exponent for the element factor.

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.width
    :type: float

    Gets the array width.

.. py:property:: height
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.height
    :type: float

    Gets the array height.

.. py:property:: number_of_elements
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.number_of_elements
    :type: int

    Gets the number of array elements.

.. py:property:: supported_beam_direction_provider_types
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.supported_beam_direction_provider_types
    :type: list

    Gets an array of valid beam direction provider types.

.. py:property:: beam_direction_provider_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.beam_direction_provider_type
    :type: DIRECTION_PROVIDER_TYPE

    Gets or sets the beam direction provider type.

.. py:property:: beam_direction_provider
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.beam_direction_provider
    :type: IAgDirectionProvider

    Gets the beam direction provider.

.. py:property:: supported_null_direction_provider_types
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.supported_null_direction_provider_types
    :type: list

    Gets an array of valid null direction provider types.

.. py:property:: null_direction_provider_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.null_direction_provider_type
    :type: DIRECTION_PROVIDER_TYPE

    Gets or sets the null direction provider type.

.. py:property:: null_direction_provider
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.null_direction_provider
    :type: IAgDirectionProvider

    Gets the null direction provider.

.. py:property:: beamformer_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.beamformer_type
    :type: BEAMFORMER_TYPE

    Gets or sets beamformer type.

.. py:property:: beamformer
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.beamformer
    :type: IAgBeamformer

    Gets the beamformer.

.. py:property:: element_configuration_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.element_configuration_type
    :type: ELEMENT_CONFIGURATION_TYPE

    Gets or sets the element configuration type.

.. py:property:: element_configuration
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.element_configuration
    :type: IAgElementConfiguration

    Gets the element configuration.

.. py:property:: elements
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.elements
    :type: IAgElementCollection

    Gets the collection of elements.

.. py:property:: show_grid
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.show_grid
    :type: bool

    Gets or sets the option to show the grid in the antenna's element viewport GUI.

.. py:property:: show_labels
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPhasedArray.show_labels
    :type: bool

    Gets or sets the option to show the labels in the antenna's element viewport GUI.


