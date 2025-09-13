Receiver
========

.. py:class:: ansys.stk.core.stkobjects.Receiver

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining the receiver object.

.. py:currentmodule:: Receiver

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.chain_analysis_options`
              - Get the receiver's chain analysis options.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.graphics`
              - Get the 2D Graphics properties for the receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.graphics_3d`
              - Get the 3D Graphics properties for the receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.laser_environment`
              - Get the object laser environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.model_component_linking`
              - Get the link/embed controller for managing the receiver model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.refraction`
              - Refraction method, a member of the SensorRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.refraction_model`
              - Get a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.refraction_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.rf_environment`
              - Get the object RF environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.



Examples
--------

Receiver additional Gain

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model_component_linking.component
    gain = recModel.pre_receive_gains_losses.add(5)  # dB
    gain.identifier = "Example Gain"


Modify Receiver Filter Properties

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model_component_linking.component
    recModel.enable_filter = True
    recModel.filter_component_linking.set_component("Bessel")
    recFilter = recModel.filter_component_linking.component
    recFilter.lower_bandwidth_limit = -20
    recFilter.upper_bandwidth_limit = 20
    recFilter.cut_off_frequency = 10


Modify Receiver Demodulator Properties

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model_component_linking.component
    recModel.select_demodulator_automatically = False
    recModel.set_demodulator("16PSK")


Modify Receiver System Noise Temperature

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.model_component_linking.set_component("Complex Receiver Model")
    recModel = receiver.model_component_linking.component
    recModel.system_noise_temperature.constant_noise_temperature = 280  # K


Modify Orientation of the Receiver Antenna

.. code-block:: python

    # Complex receivers Only
    # Receiver receiver: Receiver object
    receiver.model_component_linking.set_component("Complex Receiver Model")
    recModel = receiver.model_component_linking.component
    antennaControl = recModel.antenna_control
    antOrientation = antennaControl.embedded_model_orientation
    antOrientation.assign_az_el(45, 85, AzElAboutBoresight.ROTATE)
    antOrientation.position_offset.x = 0.5  # m
    antOrientation.position_offset.y = 0.75  # m
    antOrientation.position_offset.z = 1  # m


Modify Receiver Polarization Properties

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model_component_linking.component
    recModel.enable_polarization = True
    recModel.set_polarization_type(PolarizationType.LINEAR)
    polarization = recModel.polarization
    polarization.reference_axis = PolarizationReferenceAxis.Z
    polarization.cross_polarization_leakage = -60  # dB


Modify Receiver Embedded Antenna

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.model_component_linking.set_component("Complex Receiver Model")
    recModel = receiver.model_component_linking.component
    antennaControl = recModel.antenna_control
    antennaControl.embedded_model_component_linking.set_component("Hemispherical")
    antennaControl.embedded_model_component_linking.component.efficiency = 85  # Percent


Modify Receiver Model Type

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.model_component_linking.set_component("Complex Receiver Model")
    recModel = receiver.model_component_linking.component
    recModel.track_frequency_automatically = False
    recModel.frequency = 11.81


Create a New Receiver Object

.. code-block:: python

    # ISTKObject satellite: STK object
    receiver = satellite.children.new(STKObjectType.RECEIVER, "MyReceiver")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Receiver


Property detail
---------------

.. py:property:: chain_analysis_options
    :canonical: ansys.stk.core.stkobjects.Receiver.chain_analysis_options
    :type: ChainAnalysisOptions

    Get the receiver's chain analysis options.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Receiver.graphics
    :type: ReceiverGraphics

    Get the 2D Graphics properties for the receiver.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Receiver.graphics_3d
    :type: ReceiverGraphics3D

    Get the 3D Graphics properties for the receiver.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Receiver.laser_environment
    :type: ObjectLaserEnvironment

    Get the object laser environment settings.

.. py:property:: model_component_linking
    :canonical: ansys.stk.core.stkobjects.Receiver.model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the receiver model component.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Receiver.refraction
    :type: SensorRefractionType

    Refraction method, a member of the SensorRefractionType enumeration.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Receiver.refraction_model
    :type: IRefractionModelBase

    Get a refraction model.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Receiver.refraction_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Receiver.rf_environment
    :type: ObjectRFEnvironment

    Get the object RF environment settings.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.Receiver.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.


Method detail
-------------



.. py:method:: is_refraction_type_supported(self, model: SensorRefractionType) -> bool
    :canonical: ansys.stk.core.stkobjects.Receiver.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **model** : :obj:`~SensorRefractionType`


    :Returns:

        :obj:`~bool`











