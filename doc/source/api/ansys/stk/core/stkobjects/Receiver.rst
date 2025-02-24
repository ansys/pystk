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
              - Do not use this method, as it is deprecated. Use ModelComponentLinking on IAgReceiver instead. Sets the current receiver model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.supported_models`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgReceiver instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.model`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgReceiver instead. Gets the current receiver model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Receiver.refraction`
              - Refraction method, a member of the AgESnRefractionType enumeration.
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



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Receiver


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.Receiver.supported_models
    :type: list

    Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgReceiver instead. Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.Receiver.model
    :type: IReceiverModel

    Do not use this property, as it is deprecated. Use ModelComponentLinking on IAgReceiver instead. Gets the current receiver model.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Receiver.refraction
    :type: SensorRefractionType

    Refraction method, a member of the AgESnRefractionType enumeration.

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

    Do not use this method, as it is deprecated. Use ModelComponentLinking on IAgReceiver instead. Sets the current receiver model by name.

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










