Receiver
========

.. py:class:: ansys.stk.core.stkobjects.Receiver

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining the receiver object.

.. py:currentmodule:: Receiver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.set_model`
              - Do not use this method, as it is deprecated. Use ModelComponentLinking on Receiver instead. Sets the current receiver model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.supported_models`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on Receiver instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.model`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on Receiver instead. Gets the current receiver model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.refraction`
              - Refraction method, a member of the SensorRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.refraction_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.refraction_model`
              - Get a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.graphics_3d`
              - Get the 3D Graphics properties for the receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.graphics`
              - Get the 2D Graphics properties for the receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.rf_environment`
              - Get the object RF environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.laser_environment`
              - Get the object laser environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.model_component_linking`
              - Get the link/embed controller for managing the receiver model component.



Examples
--------

Receiver additional Gain

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    gain = recModel.pre_receive_gains_losses.add(5)  # dB
    gain.identifier = "Example Gain"


Modify Receiver Filter Properties

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    recModel.enable_filter = True
    recModel.set_filter("Bessel")
    recFilter = recModel.filter
    recFilter.lower_bandwidth_limit = -20
    recFilter.upper_bandwidth_limit = 20
    recFilter.cut_off_frequency = 10


Modify Receiver Demodulator Properties

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    recModel.select_demodulator_automatically = False
    recModel.set_demodulator("16PSK")


Modify Receiver System Noise Temperature

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    recModel.system_noise_temperature.constant_noise_temperature = 280  # K


Modify Orientation of the Receiver Antenna

.. code-block:: python

    # Complex receivers Only
    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    antennaControl = recModel.antenna_control
    antOrientation = antennaControl.embedded_model_orientation
    antOrientation.assign_az_el(45, 85, AzElAboutBoresight.ROTATE)
    antOrientation.position_offset.x = 0.5  # m
    antOrientation.position_offset.y = 0.75  # m
    antOrientation.position_offset.z = 1  # m


Modify Receiver Polarization Properties

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    recModel.enable_polarization = True
    recModel.set_polarization_type(PolarizationType.LINEAR)
    polarization = recModel.polarization
    polarization.reference_axis = PolarizationReferenceAxis.Z
    polarization.cross_polarization_leakage = -60  # dB


Modify Receiver Embedded Antenna

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    antennaControl = recModel.antenna_control
    antennaControl.set_embedded_model("Hemispherical")
    antennaControl.embedded_model.efficiency = 85  # Percent


Modify Receiver Model Type

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    recModel.track_frequency_automatically = False
    recModel.frequency = 11.81


Create a New Receiver Object

.. code-block:: python

    # IStkObject satellite: STK object
    receiver = satellite.children.new(STKObjectType.RECEIVER, "MyReceiver")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Receiver


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.Receiver.supported_models
    :type: list

    Do not use this property, as it is deprecated. Use ModelComponentLinking on Receiver instead. Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.Receiver.model
    :type: IReceiverModel

    Do not use this property, as it is deprecated. Use ModelComponentLinking on Receiver instead. Gets the current receiver model.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Receiver.refraction
    :type: SensorRefractionType

    Refraction method, a member of the SensorRefractionType enumeration.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Receiver.refraction_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Receiver.refraction_model
    :type: IRefractionModelBase

    Get a refraction model.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.Receiver.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Receiver.graphics_3d
    :type: ReceiverGraphics3D

    Get the 3D Graphics properties for the receiver.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Receiver.graphics
    :type: ReceiverGraphics

    Get the 2D Graphics properties for the receiver.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Receiver.rf_environment
    :type: ObjectRFEnvironment

    Get the object RF environment settings.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Receiver.laser_environment
    :type: ObjectLaserEnvironment

    Get the object laser environment settings.

.. py:property:: model_component_linking
    :canonical: ansys.stk.core.stkobjects.Receiver.model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the receiver model component.


Method detail
-------------


.. py:method:: set_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Receiver.set_model

    Do not use this method, as it is deprecated. Use ModelComponentLinking on Receiver instead. Sets the current receiver model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: is_refraction_type_supported(self, model: SensorRefractionType) -> bool
    :canonical: ansys.stk.core.stkobjects.Receiver.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **model** : :obj:`~SensorRefractionType`

    :Returns:

        :obj:`~bool`










