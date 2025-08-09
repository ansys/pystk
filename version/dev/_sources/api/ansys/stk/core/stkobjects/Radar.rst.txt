Radar
=====

.. py:class:: ansys.stk.core.stkobjects.Radar

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Class defining the radar object.

.. py:currentmodule:: Radar

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.set_model`
              - Do not use this method, as it is deprecated. Use ModelComponentLinking on Radar instead. Sets the current radar model by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.graphics`
              - Get the 2D Graphics properties for the radar.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.graphics_3d`
              - Get the 3D Graphics properties for the radar.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.model`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on Radar instead. Gets the current radar model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.model_component_linking`
              - Get the link/embed controller for managing the radar model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.refraction`
              - Refraction method, a member of the SensorRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.refraction_model`
              - Get a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.refraction_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.rf_environment`
              - Get the object RF Environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.supported_models`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on Radar instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.Radar.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Radar


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Radar.graphics
    :type: RadarGraphics

    Get the 2D Graphics properties for the radar.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Radar.graphics_3d
    :type: RadarGraphics3D

    Get the 3D Graphics properties for the radar.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.Radar.model
    :type: IRadarModel

    Do not use this property, as it is deprecated. Use ModelComponentLinking on Radar instead. Gets the current radar model.

.. py:property:: model_component_linking
    :canonical: ansys.stk.core.stkobjects.Radar.model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar model component.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Radar.refraction
    :type: SensorRefractionType

    Refraction method, a member of the SensorRefractionType enumeration.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Radar.refraction_model
    :type: IRefractionModelBase

    Get a refraction model.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Radar.refraction_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Radar.rf_environment
    :type: ObjectRFEnvironment

    Get the object RF Environment settings.

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.Radar.supported_models
    :type: list

    Do not use this property, as it is deprecated. Use ModelComponentLinking on Radar instead. Gets an array of supported model names.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.Radar.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.


Method detail
-------------


.. py:method:: is_refraction_type_supported(self, model: SensorRefractionType) -> bool
    :canonical: ansys.stk.core.stkobjects.Radar.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **model** : :obj:`~SensorRefractionType`


    :Returns:

        :obj:`~bool`








.. py:method:: set_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Radar.set_model

    Do not use this method, as it is deprecated. Use ModelComponentLinking on Radar instead. Sets the current radar model by name.

    :Parameters:

        **model_name** : :obj:`~str`


    :Returns:

        :obj:`~None`





