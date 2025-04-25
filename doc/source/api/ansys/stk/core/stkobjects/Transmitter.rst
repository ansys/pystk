Transmitter
===========

.. py:class:: ansys.stk.core.stkobjects.Transmitter

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining the transmitter object.

.. py:currentmodule:: Transmitter

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.set_model`
              - Do not use this method, as it is deprecated. Use ModelComponentLinking on Transmitter instead. Sets the current transmitter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.supported_models`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on Transmitter instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.model`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on Transmitter instead. Gets the current transmitter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.refraction`
              - Refraction method, a member of the SensorRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.refraction_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.refraction_model`
              - Get a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.graphics_3d`
              - Get the 3D Graphics properties for the transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.graphics`
              - Get the 2D Graphics properties for the transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.rf_environment`
              - Get the object RF environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.laser_environment`
              - Get the object laser environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.model_component_linking`
              - Get the link/embed controller for managing the transmitter model component.



Examples
--------

Transmitter additional Gain

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    txModel = transmitter.model
    gain = txModel.post_transmit_gains_losses.add(-5)  # dB
    gain.identifier = "Example Loss"


Modify a Transmitter Filter

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    txModel = transmitter.model
    txModel.enable_filter = True
    txModel.set_filter("Butterworth")
    recFilter = txModel.filter
    recFilter.lower_bandwidth_limit = -20
    recFilter.upper_bandwidth_limit = 20
    recFilter.cut_off_frequency = 10


Modify a Transmitter's Modulator Properties

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    txModel = transmitter.model
    txModel.set_modulator("BPSK")
    txModel.modulator.scale_bandwidth_automatically = True


Modify a Transmitter's Orientation and Position

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    antennaControl = txModel.antenna_control
    antOrientation = antennaControl.embedded_model_orientation
    antOrientation.assign_az_el(0, 90, 1)  # 1 represents Rotate About Boresight
    antOrientation.position_offset.x = 0.0  # m
    antOrientation.position_offset.y = 1  # m
    antOrientation.position_offset.z = 0.25  # m


Modify a Transmitter's Polarization Properties

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    txModel.enable_polarization = True
    txModel.set_polarization_type(PolarizationType.LINEAR)
    polarization = txModel.polarization
    polarization.reference_axis = PolarizationReferenceAxis.Y
    polarization.tilt_angle = 15  # deg


Modify a Transmitter's Embedded Antenna

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    antennaControl = txModel.antenna_control
    antennaControl.set_embedded_model("Isotropic")
    antennaControl.embedded_model.efficiency = 85  # Percent


Modify a Transmitter's Model Type

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    txModel.frequency = 14  # GHz
    txModel.power = 25  # dBW
    txModel.data_rate = 15  # Mb/sec


Create a New Transmitter Object

.. code-block:: python

    # IStkObject satellite: STK object
    transmitter = satellite.children.new(STKObjectType.TRANSMITTER, "MyTransmitter")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Transmitter


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.Transmitter.supported_models
    :type: list

    Do not use this property, as it is deprecated. Use ModelComponentLinking on Transmitter instead. Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.Transmitter.model
    :type: ITransmitterModel

    Do not use this property, as it is deprecated. Use ModelComponentLinking on Transmitter instead. Gets the current transmitter model.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Transmitter.refraction
    :type: SensorRefractionType

    Refraction method, a member of the SensorRefractionType enumeration.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Transmitter.refraction_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Transmitter.refraction_model
    :type: IRefractionModelBase

    Get a refraction model.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.Transmitter.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Transmitter.graphics_3d
    :type: TransmitterGraphics3D

    Get the 3D Graphics properties for the transmitter.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Transmitter.graphics
    :type: TransmitterGraphics

    Get the 2D Graphics properties for the transmitter.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Transmitter.rf_environment
    :type: ObjectRFEnvironment

    Get the object RF environment settings.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Transmitter.laser_environment
    :type: ObjectLaserEnvironment

    Get the object laser environment settings.

.. py:property:: model_component_linking
    :canonical: ansys.stk.core.stkobjects.Transmitter.model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the transmitter model component.


Method detail
-------------


.. py:method:: set_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Transmitter.set_model

    Do not use this method, as it is deprecated. Use ModelComponentLinking on Transmitter instead. Sets the current transmitter model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: is_refraction_type_supported(self, model: SensorRefractionType) -> bool
    :canonical: ansys.stk.core.stkobjects.Transmitter.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **model** : :obj:`~SensorRefractionType`

    :Returns:

        :obj:`~bool`










