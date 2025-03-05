Antenna
=======

.. py:class:: ansys.stk.core.stkobjects.Antenna

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining the antenna object.

.. py:currentmodule:: Antenna

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.set_model`
              - Do not use this method, as it is deprecated. Use ModelComponentLinking on IAgAntenna instead. Sets the current antenna model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.supported_models`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgAntenna instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.model`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgAntenna instead. Gets the current antenna model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.orientation`
              - Get the antenna orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.refraction`
              - Refraction method, a member of the AgESnRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.refraction_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.refraction_model`
              - Get a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.graphics_3d`
              - Get the 3D Graphics properties for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.graphics`
              - Get the 2D Graphics properties for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.rf_environment`
              - Get the object RF environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.laser_environment`
              - Get the object laser environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Antenna.model_component_linking`
              - Get the link/embed controller for managing the antenna model component.



Examples
--------

Modify Antenna Graphics

.. code-block:: python

    # Antenna antenna: Antenna object
    contours = antenna.graphics.contour_graphics
    contours.set_contour_type(AntennaContourType.GAIN)
    contours.show = True
    for i in range(-30, 30, 5):
        contours.contour.levels.add(i)
    antenna.graphics_3d.show_contours = True
    antenna.graphics_3d.volume_graphics.show = True


Modify Antenna Orientation and Position

.. code-block:: python

    # Antenna antenna: Antenna object
    antOrientation = antenna.orientation
    antOrientation.assign_az_el(0, -90, AzElAboutBoresight.ROTATE)
    antOrientation.position_offset.x = 0.0  # m
    antOrientation.position_offset.y = 1  # m
    antOrientation.position_offset.z = 0.25  # m


Modify Antenna Refraction

.. code-block:: python

    # Antenna antenna: Antenna object
    antenna.use_refraction_in_access = True
    antenna.refraction = SensorRefractionType.ITU_R_P834_4
    refraction = antenna.refraction_model
    refraction.ceiling = 5000  # m
    refraction.atmosphere_altitude = 10000  # m
    refraction.knee_bend_factor = 0.2


Modify Antenna Model Type

.. code-block:: python

    # Antenna antenna: Antenna object
    antenna.set_model("Dipole")
    antennaModel = antenna.model
    antennaModel.design_frequency = 15  # GHz
    antennaModel.length = 1.5  # m
    antennaModel.length_to_wavelength_ratio = 45
    antennaModel.efficiency = 85  # Percent


Create a New Antenna Object

.. code-block:: python

    # IStkObject satellite: STK object
    antenna = satellite.children.new(STKObjectType.ANTENNA, "MyAntenna")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Antenna


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.Antenna.supported_models
    :type: list

    Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgAntenna instead. Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.Antenna.model
    :type: IAntennaModel

    Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgAntenna instead. Gets the current antenna model.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.Antenna.orientation
    :type: IOrientation

    Get the antenna orientation.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Antenna.refraction
    :type: SensorRefractionType

    Refraction method, a member of the AgESnRefractionType enumeration.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Antenna.refraction_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Antenna.refraction_model
    :type: IRefractionModelBase

    Get a refraction model.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.Antenna.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Antenna.graphics_3d
    :type: AntennaGraphics3D

    Get the 3D Graphics properties for the antenna.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Antenna.graphics
    :type: AntennaGraphics

    Get the 2D Graphics properties for the antenna.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Antenna.rf_environment
    :type: ObjectRFEnvironment

    Get the object RF environment settings.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Antenna.laser_environment
    :type: ObjectLaserEnvironment

    Get the object laser environment settings.

.. py:property:: model_component_linking
    :canonical: ansys.stk.core.stkobjects.Antenna.model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the antenna model component.


Method detail
-------------


.. py:method:: set_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Antenna.set_model

    Do not use this method, as it is deprecated. Use ModelComponentLinking on IAgAntenna instead. Sets the current antenna model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`






.. py:method:: is_refraction_type_supported(self, model: SensorRefractionType) -> bool
    :canonical: ansys.stk.core.stkobjects.Antenna.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **model** : :obj:`~SensorRefractionType`

    :Returns:

        :obj:`~bool`










