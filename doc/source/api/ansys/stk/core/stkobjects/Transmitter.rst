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
              - Set the current transmitter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.supported_models`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.model`
              - Gets the current transmitter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.refraction`
              - Refraction method, a member of the AgESnRefractionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.refraction_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.refraction_model`
              - Gets a refraction model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.graphics_3d`
              - Get the 3D Graphics properties for the transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.graphics`
              - Get the 2D Graphics properties for the transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.rf_environment`
              - Gets the object RF environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Transmitter.laser_environment`
              - Gets the object laser environment settings.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Transmitter


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.Transmitter.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.Transmitter.model
    :type: ITransmitterModel

    Gets the current transmitter model.

.. py:property:: refraction
    :canonical: ansys.stk.core.stkobjects.Transmitter.refraction
    :type: SensorRefractionType

    Refraction method, a member of the AgESnRefractionType enumeration.

.. py:property:: refraction_supported_types
    :canonical: ansys.stk.core.stkobjects.Transmitter.refraction_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: refraction_model
    :canonical: ansys.stk.core.stkobjects.Transmitter.refraction_model
    :type: IRefractionModelBase

    Gets a refraction model.

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

    Gets the object RF environment settings.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Transmitter.laser_environment
    :type: ObjectLaserEnvironment

    Gets the object laser environment settings.


Method detail
-------------


.. py:method:: set_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Transmitter.set_model

    Set the current transmitter model by name.

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









