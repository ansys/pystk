IAntennaModelHfssEepArray
=========================

.. py:class:: IAntennaModelHfssEepArray

   object
   
   Provide access to the properties and methods defining an HFSS EEP array antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~width`
            * - :py:meth:`~height`
            * - :py:meth:`~number_of_elements`
            * - :py:meth:`~supported_beam_direction_provider_types`
            * - :py:meth:`~beam_direction_provider_type`
            * - :py:meth:`~beam_direction_provider`
            * - :py:meth:`~beamformer_type`
            * - :py:meth:`~beamformer`
            * - :py:meth:`~element_configuration_type`
            * - :py:meth:`~element_configuration`
            * - :py:meth:`~elements`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelHfssEepArray


Property detail
---------------

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.width
    :type: float

    Gets the array width.

.. py:property:: height
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.height
    :type: float

    Gets the array height.

.. py:property:: number_of_elements
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.number_of_elements
    :type: int

    Gets the number of array elements.

.. py:property:: supported_beam_direction_provider_types
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.supported_beam_direction_provider_types
    :type: list

    Gets an array of valid beam direction provider types.

.. py:property:: beam_direction_provider_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.beam_direction_provider_type
    :type: DIRECTION_PROVIDER_TYPE

    Gets or sets the beam direction provider type.

.. py:property:: beam_direction_provider
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.beam_direction_provider
    :type: IAgDirectionProvider

    Gets the beam direction provider.

.. py:property:: beamformer_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.beamformer_type
    :type: BEAMFORMER_TYPE

    Gets or sets beamformer type.

.. py:property:: beamformer
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.beamformer
    :type: IAgBeamformer

    Gets the beamformer.

.. py:property:: element_configuration_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.element_configuration_type
    :type: ELEMENT_CONFIGURATION_TYPE

    Gets the element configuration type.

.. py:property:: element_configuration
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.element_configuration
    :type: IAgElementConfiguration

    Gets the element configuration.

.. py:property:: elements
    :canonical: ansys.stk.core.stkobjects.IAntennaModelHfssEepArray.elements
    :type: IAgElementCollection

    Gets the collection of elements.


