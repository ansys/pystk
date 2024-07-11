IReceiver
=========

.. py:class:: ansys.stk.core.stkobjects.IReceiver

   object
   
   Provide access to the properties and methods defining an Receiver object.

.. py:currentmodule:: IReceiver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.set_model`
              - Set the current receiver model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.supported_models`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.model`
              - Gets the current receiver model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.refraction`
              - Refraction method, a member of the AgESnRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.refraction_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.refraction_model`
              - Gets a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.graphics_3d`
              - Get the 3D Graphics properties for the receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.graphics`
              - Get the 2D Graphics properties for the receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.rf_environment`
              - Gets the object RF environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiver.laser_environment`
              - Gets the object laser environment settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiver


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.IReceiver.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IReceiver.model
    :type: IReceiverModel

    Gets the current receiver model.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.IReceiver.refraction
    :type: SENSOR_REFRACTION_TYPE

    Refraction method, a member of the AgESnRefractionType enumeration.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.IReceiver.refraction_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.IReceiver.refraction_model
    :type: IRefractionModelBase

    Gets a refraction model.

.. py:property:: use_refraction_in_access
    :canonical: ansys.stk.core.stkobjects.IReceiver.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IReceiver.graphics_3d
    :type: IReceiverGraphics3D

    Get the 3D Graphics properties for the receiver.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IReceiver.graphics
    :type: IReceiverGraphics

    Get the 2D Graphics properties for the receiver.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IReceiver.rf_environment
    :type: IObjectRFEnvironment

    Gets the object RF environment settings.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IReceiver.laser_environment
    :type: IObjectLaserEnvironment

    Gets the object laser environment settings.


Method detail
-------------


.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiver.set_model

    Set the current receiver model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: is_refraction_type_supported(self, model: SENSOR_REFRACTION_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IReceiver.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **model** : :obj:`~SENSOR_REFRACTION_TYPE`

    :Returns:

        :obj:`~bool`









